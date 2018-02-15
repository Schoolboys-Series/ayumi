# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00000A20 (CP2 Twilight Misaki)

label block_00000A21:
    # Node: 00000A21 (開始)
    $ HananoRandom = 0

    if judge_lm_condition([]):
        jump block_00000A24

    return

label block_00000A24:
    # Node: 00000A24 (Misaki)
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


    if judge_lm_condition([{ "scope": 0, "content": "C2S6Phase == 1" }]):
        jump block_000016D6
    if judge_lm_condition([{ "scope": 0, "content": "C2QYuuhiPhase == 1" }]):
        jump block_000025B7
    if judge_lm_condition([]):
        jump block_0000193C

    return

label block_000016D6:
    # Node: 000016D6 (友+忍)
    $ sys_ayumi_global_map_character = "tomo_shinobu"
    $ sys_ayumi_global_map_time = "twilight"

    if judge_lm_condition([]):
        jump block_00000A25

    return

label block_00000A25:
    # Node: 00000A25 (Misaki XCTA)
    if judge_lm_condition([{ "scope": 1, "content": "C2S6Phase == 1" }]) and judge_lm_condition([{ "scope": 1, "content": "C2S6Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "misaki", False, True, talk_label="block_00000A22", target_label="block_00000A23") from _call_scb_global_map_141
    elif judge_lm_condition([{ "scope": 1, "content": "C2S6Phase == 1" }]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "misaki", False, True, talk_label="block_00000A22", target_label="block_000025B4") from _call_scb_global_map_142
    elif judge_lm_condition([]) and judge_lm_condition([{ "scope": 1, "content": "C2S6Phase == 1" }]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "misaki", False, True, talk_label="block_000025B5", target_label="block_00000A23") from _call_scb_global_map_143
    elif judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "misaki", False, True, talk_label="block_000025B5", target_label="block_000025B4") from _call_scb_global_map_144
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲学園\"" }]):
        jump block_00000A28
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"住宅街\"" }]):
        jump block_00000A26
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲駅\"" }]):
        jump block_00000A5B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"商店街\"" }]):
        jump block_00000A2F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"公園\"" }]):
        jump block_00003BA5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"昼休み不可\"" }]):
        jump block_00000A25
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" },{ "scope": 1, "content": "C2S6Phase == 1" }]):
        jump block_00000A22
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" },{ "scope": 1, "content": "C2S6Phase == 1" }]):
        jump block_00000A23
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00001FB2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" },{ "scope": 1, "content": "C2QYuuhiPhase == 1" }]):
        jump block_000025B6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" },{ "scope": 1, "content": "C2S6Phase == 1" }]):
        jump block_00001FB0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_000025B5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_000025B4

    return

label block_00000A28:
    # Node: 00000A28 (Misaki school)
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


    if judge_lm_condition([{ "scope": 0, "content": "C2S5 == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "C2SG1 == True" },{ "scope": 3, "content": "C2QYuuhiPhase == 0" }]):
        jump block_00000A6D
    if judge_lm_condition([{ "scope": 0, "content": "C2QYuuhiPhase == 1" },{ "scope": 1, "content": "TalkSchoolQYuuhi == False" }]):
        jump block_000025D2
    if judge_lm_condition([]):
        jump block_0000256D

    return

label block_00000A6D:
    # Node: 00000A6D (Misaki school 雪緒 flag)
    $ sys_lm_menu_item = [{"pos": (216, 280),"image": "images/Chapter 2/Menu/F5/Yukio flag.png","hover": "images/Chapter 2/Menu/F5/Yukio hover.png","name": "雪緒"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (416, 280),"image": "images/Chapter 2/Menu/F5/Shiro.png","hover": "images/Chapter 2/Menu/F5/Shiro hover.png","name": "四朗"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_511
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"雪緒\"" }]):
        jump block_00001772
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"四朗\"" }]):
        jump block_00000A72
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B8E

    return

label block_00001772:
    # Node: 00001772 (雪緒)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_6FE796722EF0405FB1730AFCA7E0319C as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00000A71

    return

label block_00000A71:
    # Node: 00000A71 (F5)
    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？你们两人在这里做什么呢？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3262D60C74654385A3E1B28F01BB2B2E as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊，下午好。{w}\n我们和穗海前辈约好要一起回去，\n所以现在正在等他。"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_76BDC5526C0D455C992334F53B3BACF8 as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "三朗哥也是一起的。真是的……\n四朗总是这么轻视自己的哥哥呐～"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_F69A7F8603174D3296CF7683C5C0D06C as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "听不见不知道我不管♪\n我能和穗海前辈一起就行了，\n剩下的都无所谓——"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_AF7BBF63497B454D86E5E6600D6E3F01 as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "唔……森海前辈也请说他点什么。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦！居然会被那种坏心眼技安吸引，\n森海前辈我完全想不通！"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2687EBBCBF3E4AF7A0DE1AF839CF5AF7 as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 0.4

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "再说一遍。"

    if sys_effect2_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好痛。"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 200
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_DA6600AAC97F4D3CAFE6F2ADAA431ADD as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "穗海前辈——！！久候多时了！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_D5EC6359084E4C79A1257082BC289D09 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊，对了！\n回家路上想顺便去一个地方，\n要是可以的话前辈也一起……"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_14CD0F42E7E7472DA340494245426445 as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "完全无视哥哥了。"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_B88DFA606D384D139F2F3C6326D0D471 as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "哈哈。请不要在意～三朗哥。{w}\n那么森海前辈，我们就先……"
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_D5EC6359084E4C79A1257082BC289D09 as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我们先走了！"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_C3058DD2310F448EBB3F52DA2113AB2E as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "吼吼。这位该不会是落单的？真可怜。"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不、不用你管！今天只是偶然！只是偶然！"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_402B3A34DCAC41AD846641A233A33DED as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那明天见——白痴呆毛——"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校门"))

    if judge_lm_condition([]):
        jump block_00001790

    return

label block_00001790:
    # Node: 00001790 (Flag: START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件已开始。请试着寻找下一个同类{/color}{color=#3A00C4}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    pause 0.7

    stop music fadeout 1
    $ sys_music_current_file = ""

    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"


    if judge_lm_condition([]):
        jump block_00002EFD

    return

label block_00002EFD:
    # Node: 00002EFD (Phase ++)
    $ C2S5Phase = C2S5Phase + 1

    if judge_lm_condition([]):
        jump block_00000A6E

    return

label block_00000A6E:
    # Node: 00000A6E (Misaki school 常磐 flag)
    $ sys_lm_menu_item = [{"pos": (304, 240),"image": "images/Chapter 2/Menu/F5/Tokiwa flag.png","hover": "images/Chapter 2/Menu/F5/Tokiwa hover.png","name": "常磐"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.5, 0.2) from _call_lm_menu_512
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"常磐\"" }]):
        jump block_00000A73

    return

label block_00000A73:
    # Node: 00000A73 (常磐)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_6247A96D3EC64B87BF0825FDF3552F9F as tag_3482C372784E44A89E382266A93F2B14 at center_bottom zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_6247A96D3EC64B87BF0825FDF3552F9F as tag_3482C372784E44A89E382266A93F2B14 at center_bottom zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_C223850065F6443080205D1F61C04C98 "……{w=0.5}这种感觉……那个孩子，难道……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B7BD90C9E0F94D39B930CB8F323D6C2F as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "不过，感觉不到任何恶意。{w}\n{nw}"
    show rs_image_A68CA26FBD59461E9325D30C41EC4694 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "总觉得有种非常不祥的预感。\n……错觉？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "？{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "？"

    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校门"))
    pause 0.8

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4


    if judge_lm_condition([]):
        jump block_00003B98

    return

label block_00003B98:
    # Node: 00003B98 (FLAG: CP2F5)
    call block_00003B90 from _call_block_00003B90

    if judge_lm_condition([]):
        jump block_00003BA2

    return

label block_00003BA2:
    # Node: 00003BA2 (FLAG FINISH)
    $ set_window("(標準)")
    pause 1.5

    if sys_music2_current_file != "sound/BGM/Flag finished.ogg":
        play music2 "sound/BGM/Flag finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件{/color}{color=#3A00C4}“狐的报恩”{/color}{color=#0080FF}成功结束。』{/color}"

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
        jump block_00003BA3

    return

label block_00003BA3:
    # Node: 00003BA3 ()
    $ del HananoRandom

    return

label block_00000A72:
    # Node: 00000A72 (四郎)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_77DF5D5E124F44A8AF4332084D208D1C as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00000A71

    return

label block_00003B8E:
    # Node: 00003B8E (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00003B8D

    return

label block_00003B8D:
    # Node: 00003B8D (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00000A24

    return

label block_000025D2:
    # Node: 000025D2 (夕阳 event)
    pause 0.4

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if sys_music2_current_file != "sound/Effect Sound/Cute 2.ogg":
        play music2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "快看！这就是御咲学园哦——！"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 200
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_92B28690BF524F6E84FED8251700E47B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "哦，这样。"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "反应好淡！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_39D2FAB2A82240CB90EB954F3BA3A473 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "啊，不是……御咲学园的话，\n社团活动时来过很多次了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么嘛，这样啊。"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校门"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002F05

    return

label block_00002F05:
    # Node: 00002F05 (T ++)
    $ TalkSchoolQYuuhi = True

    if judge_lm_condition([]):
        jump block_0000256D

    return

label block_0000256D:
    # Node: 0000256D (Misaki school)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (96, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "屋外トイレへ"}, {"pos": (456, 312),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "学校看板"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_513
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学校看板\"" }]):
        jump block_0000256E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋外トイレへ\"" }]):
        jump block_00002571
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B8E

    return

label block_0000256E:
    # Node: 0000256E (Board)
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
        jump block_0000256D

    return

label block_00002571:
    # Node: 00002571 (Outside toilet)
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
        jump block_00002570

    return

label block_00002570:
    # Node: 00002570 (Outside toilet)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_514
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A28

    return

label block_00000A26:
    # Node: 00000A26 (Residential street)
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
        jump block_00000A2A

    return

label block_00000A2A:
    # Node: 00000A2A (Residential street)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (552, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (696, 360),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "隠し"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_515
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003B8E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000A38
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"隠し\"" }]):
        jump block_00000A3E

    return

label block_00000A38:
    # Node: 00000A38 (Residential street turning)
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


    if judge_lm_condition([{ "scope": 0, "content": "C2QYuuhiPhase == 1" },{ "scope": 1, "content": "TalkResidentialQYuuhi == False" }]):
        jump block_000025BC
    if judge_lm_condition([]):
        jump block_00000A39

    return

label block_000025BC:
    # Node: 000025BC (夕阳 event)
    pause 0.4

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4DE7491D04004FC5BE18A0FEB043C1BF as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_bottom zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_53FF68C192E3494AB005C1909579AFFB "这么说很突然，但能让我拍张照吗？"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "诶……可以是可以？？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "他是和我同年级的小岛君，\n所属新闻部，所以一直带着相机。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DC3BE1DD2EA84C89ABC5052469A25C0E as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "谢谢你帮我介绍。\n我是小岛，初次见面。"

    show rs_image_4DE7491D04004FC5BE18A0FEB043C1BF as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "再说一次，抱歉，请让我拍张照。{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "其实看到你的第一眼就被吸引了。"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦——！好直白！！"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "啊、啊哈哈。真不好意思。\n没问题，如果我可以的话。"

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "（呵呵，原来我这么帅。下次找守炫耀炫耀♪）"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9511CC62DD3C41CB9B75011464423CB6 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "非常感谢。{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "真的是很美丽的{color=#FF8000}发色{/color}……太漂亮了。"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "原来是那个！？"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——！\n要这么说的话也夸夸我的发色好不好！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1654C244584349A6B0811665076020BD as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "森海君明显就是染的，是特技。"

    show rs_image_9511CC62DD3C41CB9B75011464423CB6 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_53FF68C192E3494AB005C1909579AFFB "而他的则更像是自然形成的，真是神秘。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_9E7F7ED47EEE46378763123AB08C7BA3 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_53FF68C192E3494AB005C1909579AFFB "那么视线请稍微下移一点。{w}\n……{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Shoot 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shoot 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shoot 1.ogg"

    show rs_image_9E7F7ED47EEE46378763123AB08C7BA3 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.5

    show rs_image_9511CC62DD3C41CB9B75011464423CB6 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……谢谢。失礼了。"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1.2

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7CD15457AE944572B69C674A367B222F as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "……不愧是御咲学园……和传闻一样全是超有个性的人……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是呐——"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7CED1BC765EE4A5B93B9DC7719B0D0AB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不，你也好不到……\n{w=0.4}{nw}"
    show rs_image_5BFDB437B1014058A738F5AA563DD520 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……没什么。该走了。"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("住宅街路口"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002F06

    return

label block_00002F06:
    # Node: 00002F06 (T ++)
    $ TalkResidentialQYuuhi = True

    if judge_lm_condition([]):
        jump block_00000A39

    return

label block_00000A39:
    # Node: 00000A39 (Residential street turning)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (120, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "花乃湯"}, {"pos": (512, 320),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "神社"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_516
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"花乃湯\"" }]):
        jump block_00000A44
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"神社\"" }]):
        jump block_00000A42
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A26

    return

label block_00000A44:
    # Node: 00000A44 (Hanano)
    stop music2 fadeout 0.2
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


    if judge_lm_condition([]):
        jump block_00000A45

    return

label block_00000A45:
    # Node: 00000A45 (Hanano)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (392, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "ポスター"}, {"pos": (232, 272),"image": "images/Menu/Shougintoki.png","hover": "images/Menu/Shougintoki hover.png","name": "翔銀時"}, {"pos": (80, 280),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_517
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A38
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000A56
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"翔銀時\"" }]):
        jump block_00002F15
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ポスター\"" }]):
        jump block_00001F77

    return

label block_00000A56:
    # Node: 00000A56 (River)
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


    if judge_lm_condition([]):
        jump block_00000A57

    return

label block_00000A57:
    # Node: 00000A57 (River)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_518
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A44

    return

label block_00002F15:
    # Node: 00002F15 (Random)
    $ HananoRandom = Random(3)

    if judge_lm_condition([{ "scope": 0, "content": "HananoRandom == 0" }]):
        jump block_00000A53
    if judge_lm_condition([{ "scope": 0, "content": "C2S4 == False" },{ "scope": 1, "content": "HananoRandom == 1" }]):
        jump block_00002580
    if judge_lm_condition([{ "scope": 0, "content": "HananoRandom == 2" }]):
        jump block_00002583
    if judge_lm_condition([{ "scope": 0, "content": "C2S4 == True" },{ "scope": 1, "content": "HananoRandom == 1" }]):
        jump block_00002584

    return

label block_00000A53:
    # Node: 00000A53 (翔銀時 1)
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
        jump block_00000A45

    return

label block_00002580:
    # Node: 00002580 (翔銀時 2)
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
        jump block_00000A45

    return

label block_00002583:
    # Node: 00002583 (翔銀時 3)
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
        jump block_00000A45

    return

label block_00002584:
    # Node: 00002584 (翔銀時 F4后)
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
        jump block_00000A45

    return

label block_00001F77:
    # Node: 00001F77 (Poster)
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


    if judge_lm_condition([]):
        jump block_00000A45

    return

label block_00000A42:
    # Node: 00000A42 (Jinja)
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


    if judge_lm_condition([{ "scope": 0, "content": "C2QYuuhiPhase == 1" },{ "scope": 1, "content": "TalkJinjaQYuuhi == False" }]):
        jump block_000025BB
    if judge_lm_condition([]):
        jump block_00000A43

    return

label block_000025BB:
    # Node: 000025BB (夕阳 event)
    pause 0.4

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 200
    show rs_image_B1728541CB614DC3B3B8761531DAF257 as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_bottom zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    window show

    rs_character_62324AD297554FE987C680452CEE232E "啊……"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "哦……你好。好久不见。"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀，两人认识？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D7B35A9D4B274A52A4297801D3F24C5B as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "与其说认识，我{color=#008080}之前向他告白但被拒绝了{/color}。{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_7E59A2176D39420B9834CA747672CADF as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀！"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_0D2D5FDA05EE493FA401028119FC985D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "等、等等！别在这种时候……！"

    show rs_image_7C86294AACD0425D9BF004B5021B12F4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_212C5F34B12743C08BEAB235356CD423 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "呵，只是说说。这可是被拒绝一方的特权。"

    show rs_image_38E2853E83D641CFA189A9FC46AB7AD5 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "那我先走了，以后再见。"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_FFC620A1302E417EBD9CB71C6CDE9274

    pause 1.2

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7CED1BC765EE4A5B93B9DC7719B0D0AB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "啊，真的走了……"

    show rs_image_7CD15457AE944572B69C674A367B222F as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "那孩子还是一副不忙不急的样子。{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_6E5666B6FFA14A90B735045E7DE61D9A as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "口气也和{color=#800080}那家伙{/color}一样缺德……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "你还真是受欢迎呐～真好～真羡慕～"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_39D2FAB2A82240CB90EB954F3BA3A473 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不，这种程度还算不上～"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "至少谦虚一点嘛～{w}\n啊——我也想变得受欢迎呐～！"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("神社"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002F07

    return

label block_00002F07:
    # Node: 00002F07 (T ++)
    $ TalkJinjaQYuuhi = True

    if judge_lm_condition([]):
        jump block_00000A43

    return

label block_00000A43:
    # Node: 00000A43 (Jinja)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_519
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A38

    return

label block_00000A3E:
    # Node: 00000A3E (Square)
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
        jump block_00000A3F

    return

label block_00000A3F:
    # Node: 00000A3F (Square)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (624, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "泉の公園"}, {"pos": (120, 328),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "？？？"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_520
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉の公園\"" }]):
        jump block_00000A51
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A26
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"？？？\"" }]):
        jump block_00000A40

    return

label block_00000A51:
    # Node: 00000A51 (Spring water park)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

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
        jump block_00000A52

    return

label block_00000A52:
    # Node: 00000A52 (Spring water part)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_521
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A3E

    return

label block_00000A40:
    # Node: 00000A40 (Forest)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

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


    if judge_lm_condition([{ "scope": 0, "content": "C2QYuuhiPhase == 1" }]):
        jump block_000025BE
    if judge_lm_condition([{ "scope": 0, "content": "FEnterForest == False" },{ "scope": 0, "content": "C2S6 == True" },{ "scope": 1, "content": "TalkYuuhiMamoruF6After == False" }]):
        jump block_00000A41
    if judge_lm_condition([]):
        jump block_000025BA

    return

label block_000025BE:
    # Node: 000025BE (Forest 2)
    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_B2C094D4282F40B5A89E6A05B31DA22B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "啊！等等！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5BFDB437B1014058A738F5AA563DD520 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "前面太危险了，\n你这样的普通人最好别去，\n我们该离开了。"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（什么高高在上的语气——！\n还有这个说话方式！{w}\n欸？说起来，这个人和我同年级么？）"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("迷之地点"))

    if judge_lm_condition([]):
        jump block_00000A3E

    return

label block_00000A41:
    # Node: 00000A41 (Forest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_522
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A3E

    return

label block_000025BA:
    # Node: 000025BA (Forest 1)
    pause 0.4

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#FF00FF}啪啪啪……！{/color}"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "啊……！那里……！不行……"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什、什么东西？好奇怪的……呻吟声……！？\n难道是妖怪……？"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇、哇——！快逃——！！"

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_3BC0411E559D49E38A86F531E7DC85FF

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_1AE46FC5165244729B37AB2893E5B8FC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_57471360F48A413AB843A4E46D8C5541 "唔……糟了，玩得太过火忘记巡逻了。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_DA7FAE4A86A54E75A9AF53E94703E05A as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_57471360F48A413AB843A4E46D8C5541 "算了，反正他也没到森林里来，\n结果至少不坏……"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    pause 0.5

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

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

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EA055EB7B6EB43248D57A79268B22FB3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00002F04

    return

label block_00002F04:
    # Node: 00002F04 (Cancel: First)
    $ FEnterForest = False

    if judge_lm_condition([]):
        jump block_00000A3F

    return

label block_00000A5B:
    # Node: 00000A5B (Misaki station)
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
        jump block_00000A5F

    return

label block_00000A5F:
    # Node: 00000A5F (Misaki station)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (336, 352),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (200, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "路線図"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_523
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" },{ "scope": 1, "content": "C2S6Phase == 1" }]):
        jump block_00002F29
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003BA8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00003BC0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"路線図\"" }]):
        jump block_00002431

    return

label block_00002F29:
    # Node: 00002F29 (F6)
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，对了！"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C2A28861C0A44DC6AAE17E0ABA1BE61C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "怎么了？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忘记买调料了。赶快回商店街买。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A43C35FAF6E4488E87E8829D5D8E84E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "直接在宝咲买不就好了。"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔～所以才说不谙世事的小少爷呀～{w}\n宝咲物价太高了！\n快——快——！别多说了快走。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("御咲站"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000A5F

    return

label block_00003BA8:
    # Node: 00003BA8 (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00003BA7

    return

label block_00003BA7:
    # Node: 00003BA7 (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00003BA4

    return

label block_00003BA4:
    # Node: 00003BA4 (TO: Misaki)

    if judge_lm_condition([]):
        jump block_00003B8E

    return

label block_00003BC0:
    # Node: 00003BC0 (Station)
    $ zorder_tag_D71B998959E446A69B3BAF1EFCCB35F6 = 400

    if judge_lm_condition([]):
        jump block_00003BC1

    return

label block_00003BC1:
    # Node: 00003BC1 (選擇)
    call scb_bus_selector(show_misaki=False, show_takarasaki=True, show_umesaki=True) from _call_scb_bus_selector_9

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"宝咲\"" }]):
        jump block_00000A3C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"梅咲\"" }]):
        jump block_00000A46
    if judge_lm_condition([]):
        jump block_00003BC2

    return

label block_00000A3C:
    # Node: 00000A3C (宝咲)
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
        jump block_00000A47

    return

label block_00000A47:
    # Node: 00000A47 (宝咲)
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


    if judge_lm_condition([{ "scope": 0, "content": "C2S6 == True" },{ "scope": 1, "content": "TalkYuuhiMamoruF6After == True" }]):
        jump block_00002605
    if judge_lm_condition([{ "scope": 0, "content": "C2QYuuhiPhase == 1" }]):
        jump block_00002589
    if judge_lm_condition([{ "scope": 0, "content": "C2QYuuhiPhase == 0" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "C2QYuuhi == False" }]):
        jump block_00000A48
    if judge_lm_condition([]):
        jump block_0000257E

    return

label block_00002605:
    # Node: 00002605 (宝咲 夕阳 守)
    $ sys_lm_menu_item = [{"pos": (616, 240),"image": "images/Menu/Mamoru.png","hover": "images/Menu/Mamoru hover.png","name": "マモル"}, {"pos": (464, 240),"image": "images/Menu/Yuuhi.png","hover": "images/Menu/Yuuhi hover.png","name": "ユウヒ"}, {"pos": (312, 264),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_524
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ユウヒ\"" }]):
        jump block_00002606
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"マモル\"" }]):
        jump block_00002607
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000A49
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003BC3

    return

label block_00002606:
    # Node: 00002606 (夕阳)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_3DD7D9D931A84116A4B51038A067F814 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002604

    return

label block_00002604:
    # Node: 00002604 (F6After)
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    show rs_image_AD6987B2589A420C8E39B0044CFF9E0B as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at center_bottom zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_57471360F48A413AB843A4E46D8C5541 "旅行期间落下的现在可要多巡逻补回来。"

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_6E5666B6FFA14A90B735045E7DE61D9A as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔——我还没从假期里缓过神来。"

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 300
    show rs_image_0310ED729B07455DA8B46628FE3224B3 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at center_bottom zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "认真一点！怪物们还在等着我们。{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_FD1F58D97A264566ACCFB1A2666968A1 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "……各种意义上♪"

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_D5C06AFEF9574BDEAEB0662A05CBCB2C as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔……\n{w=0.5}{nw}"
    show rs_image_39D2FAB2A82240CB90EB954F3BA3A473 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "哦、哦……♪"

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("宝咲"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002605

    return

label block_00002607:
    # Node: 00002607 (守)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_AD6987B2589A420C8E39B0044CFF9E0B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002604

    return

label block_00000A49:
    # Node: 00000A49 (宝咲 inside)
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
        jump block_00000A4A

    return

label block_00000A4A:
    # Node: 00000A4A (宝咲 inside)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (384, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_525
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A47
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00003BC5

    return

label block_00003BC5:
    # Node: 00003BC5 (Home)

    if judge_lm_condition([]):
        jump block_000025AD

    return

label block_000025AD:
    # Node: 000025AD (選擇)
    call scb_selector(_("回家？"), [{"name":"はい", "content":_("没问题")}, {"name":"いいえ", "content":_("还有其他事情没做完")}]) from _call_scb_selector_62

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" },{ "scope": 1, "content": "C2QYuuhiPhase == 1" },{ "scope": 2, "content": "TalkHomeQYuuhi == False" }]):
        jump block_000025B3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_000025B0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00000A4A

    return

label block_000025B3:
    # Node: 000025B3 (夕阳 event)
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

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_7CD15457AE944572B69C674A367B222F as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 0.3

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "打扰了……{w}\n{nw}"
    show rs_image_7CED1BC765EE4A5B93B9DC7719B0D0AB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "那个，为什么要回家？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我买过那本书，\n所以去书店前先来家里看看♪\n坐和放宽就好！！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_92B28690BF524F6E84FED8251700E47B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "原、原来如此……那拜托了。"

    if sys_effect3_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那——个——放什么地方了呐。欸？没有？？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "！！啊……借给朋友了……\n抱歉，现在家里没有～"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DD2EC41CBF6F4252BA591DB60AA41B9A as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "欸……"

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("友的房间"))

    if judge_lm_condition([]):
        jump block_00002F09

    return

label block_00002F09:
    # Node: 00002F09 (T ++)
    $ TalkHomeQYuuhi = True

    if judge_lm_condition([]):
        jump block_000025AE

    return

label block_000025AE:
    # Node: 000025AE (Home)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Out.png","hover": "images/MOVING/ACTIONS/Out hover.png","name": "移動"}, {"pos": (408, 192),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "写真"}, {"pos": (176, 312),"image": "images/MOVING/ACTIONS/Focusing.png","hover": "images/MOVING/ACTIONS/Focusing hover.png","name": "休む"}, {"pos": (528, 312),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "勉強する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_526
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000025A6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"休む\"" }]):
        jump block_000025AB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"写真\"" }]):
        jump block_000025B1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"勉強する\"" }]):
        jump block_000025A4

    return

label block_000025A6:
    # Node: 000025A6 (Out)
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
        jump block_00000A49

    return

label block_000025AB:
    # Node: 000025AB (Rest)

    if judge_lm_condition([]):
        jump block_000025A9

    return

label block_000025A9:
    # Node: 000025A9 (選擇)
    call scb_selector(_("今天没有其他安排了？"), [{"name":"はい", "content":_("休息")}, {"name":"いいえ", "content":_("时间还早")}]) from _call_scb_selector_63

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_000025AE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" },{ "scope": 1, "content": "C2QYuuhiPhase == 1" }]):
        jump block_000025C1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_000025A7

    return

label block_000025C1:
    # Node: 000025C1 (Rest Denied)
    window show

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_DD2EC41CBF6F4252BA591DB60AA41B9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "……"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊、哈哈，我是开玩笑的。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("友的房间"))

    if judge_lm_condition([]):
        jump block_000025AE

    return

label block_000025A7:
    # Node: 000025A7 (Next day)
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

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"


    if judge_lm_condition([]):
        jump block_00003CBB

    return

label block_00003CBB:
    # Node: 00003CBB (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_13

    if judge_lm_condition([]):
        jump block_00003BC8

    return

label block_00003BC8:
    # Node: 00003BC8 ()
    $ del HananoRandom

    $ reverse_volume("music", 1)

    return

label block_000025B1:
    # Node: 000025B1 (Photo)
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
        jump block_000025AE

    return

label block_000025A4:
    # Node: 000025A4 (StudyCount)

    if judge_lm_condition([]):
        jump block_000025A3

    return

label block_000025A3:
    # Node: 000025A3 (選擇)
    call scb_selector(_("试着学习一下？"), [{"name":"はい", "content":_("学习")}, {"name":"いいえ", "content":_("学个毛习")}]) from _call_scb_selector_64

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" },{ "scope": 1, "content": "C2QYuuhiPhase == 1" }]):
        jump block_000025C1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00002F18
    if judge_lm_condition([]):
        jump block_000025AE

    return

label block_00002F18:
    # Node: 00002F18 (StudyCount)
    if StudyCount <> 3 and C2SG1 == False:
        $ StudyCount = StudyCount + 1

    if judge_lm_condition([]):
        jump block_000025A2

    return

label block_000025A2:
    # Node: 000025A2 (Night)
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
        jump block_00002F32

    return

label block_00002F32:
    # Node: 00002F32 (Redirect)
    $ C2StudyRedirect = True

    if judge_lm_condition([]):
        jump block_000025A5

    return

label block_000025A5:
    # Node: 000025A5 (CP2 Night Misaki)
    call block_00000BD6 from _call_block_00000BD6

    if judge_lm_condition([]):
        jump block_00003BC7

    return

label block_00003BC7:
    # Node: 00003BC7 ()
    $ del HananoRandom

    return

label block_000025B0:
    # Node: 000025B0 (Home)
    stop music2 fadeout 0.2
    $ sys_music2_current_file = ""

    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

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


    if judge_lm_condition([]):
        jump block_000025AE

    return

label block_00003BC3:
    # Node: 00003BC3 (Station)
    $ zorder_tag_D71B998959E446A69B3BAF1EFCCB35F6 = 400

    if judge_lm_condition([]):
        jump block_00000A54

    return

label block_00000A54:
    # Node: 00000A54 (選擇)
    call scb_bus_selector(show_misaki=True, show_takarasaki=False, show_umesaki=True) from _call_scb_bus_selector_10


    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"乗らない\"" },{ "scope": 1, "content": "C2S6 == True" },{ "scope": 2, "content": "TalkYuuhiMamoruF6After == True" }]):
        jump block_00003FC2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"乗らない\"" }]):
        jump block_00003BD1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲\"" }]):
        jump block_00000A3D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"梅咲\"" }]):
        jump block_00000A46

    return

label block_00003FC2:
    # Node: 00003FC2 (Return)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00002605

    return

label block_00003BD1:
    # Node: 00003BD1 (Return)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([{ "scope": 0, "content": "C2QYuuhi == False" },{ "scope": 1, "content": "C2QYuuhiPhase == 0" },{ "scope": 2, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" }]):
        jump block_00000A48
    if judge_lm_condition([{ "scope": 0, "content": "C2QYuuhiPhase == 1" }]):
        jump block_00002589
    if judge_lm_condition([]):
        jump block_0000257E

    return

label block_00000A48:
    # Node: 00000A48 (宝咲 夕阳 quest)
    $ sys_lm_menu_item = [{"pos": (495, 232),"image": "images/Chapter 2/Menu/Yuuhi quest.png","hover": "images/MENU/Yuuhi hover.png","name": "ユウヒ"}, {"pos": (312, 264),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_527
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003BC3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000A49
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ユウヒ\"" }]):
        jump block_00000AC9

    return

label block_00000AC9:
    # Node: 00000AC9 (夕阳 QUEST)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 200
    show rs_image_8E33B5A194C04191BF5B97267D0E7930 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "请等一下！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，我？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7CED1BC765EE4A5B93B9DC7719B0D0AB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "很抱歉叫住你。{w}\n你书包上那个挂饰应该是\n{color=#FF8000}“见习魔法师”{/color}系列的周边没错。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_329CA2CB58C84F88AAF9DF582F9ED34D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，什么什么，你也是这个的粉丝？\n没想到慎酱意外还有男子初中生会读，\n这个世界真奇妙！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_39D2FAB2A82240CB90EB954F3BA3A473 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "那个……这个漫画在什么地方能买到？"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，你没读过？{w}\n嗯——这附近最方便的就是\n{color=#0080FF}御咲商店街{/color}了。"

    if sys_effect2_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9E6D3E7952F24718986090F2393125F3 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "很抱歉不过，能带我去么！？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸～我现在要回家的说……"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DD2EC41CBF6F4252BA591DB60AA41B9A as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "拜托了！我、我真的很在意！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔，被拜托到这个程度……{w}\n好的好的，反正电车是月票，\n友A梦会带你去的。"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CBDED26CFF754EDEA327F90E8315E9AC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "非常感谢！！"

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
        jump block_00002588

    return

label block_00002588:
    # Node: 00002588 (QUEST START)
    if sys_music2_current_file != "sound/BGM/Flag.ogg":
        play music2 "sound/BGM/Flag.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托已经开始，请达成目标。』{/color}"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002EFE

    return

label block_00002EFE:
    # Node: 00002EFE (Phase ++)
    $ C2QYuuhiPhase = C2QYuuhiPhase + 1

    if judge_lm_condition([]):
        jump block_00002589

    return

label block_00002589:
    # Node: 00002589 (宝咲 empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (352, 264),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_528
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000A49
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003BC3

    return

label block_0000257E:
    # Node: 0000257E (宝咲 夕阳)
    $ sys_lm_menu_item = [{"pos": (495, 232),"image": "images/Menu/Yuuhi.png","hover": "images/Menu/Yuuhi hover.png","name": "ユウヒ"}, {"pos": (312, 264),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_529
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ユウヒ\"" },{ "scope": 1, "content": "C2QYuuhi == True" },{ "scope": 2, "content": "TalkYuuhi == 0" }]):
        jump block_000025B2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ユウヒ\"" }]):
        jump block_0000257F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000A49
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003BC3

    return

label block_000025B2:
    # Node: 000025B2 (夕阳 1)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_3DD7D9D931A84116A4B51038A067F814 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_39D2FAB2A82240CB90EB954F3BA3A473 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "你好，之前真是麻烦你了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没事——！能让喜欢那部作品的人增加是好事。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那本漫画的剧情似乎是\n以现实中的都市传说为为蓝本的。\n真的还是假的？你怎么看？"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6E5666B6FFA14A90B735045E7DE61D9A as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "谁、谁知道……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就算是真的也角色塑造过头了呐——！{w}\n怎么会有那种冒冒失失整天H的正义的伙伴呢——"

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3E315F12F5FF4112BFC640AAE02E10D7 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    show rs_image_7CED1BC765EE4A5B93B9DC7719B0D0AB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "哈哈……说的是……"

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
        jump block_00002F2A

    return

label block_00002F2A:
    # Node: 00002F2A (T ++)
    $ TalkYuuhi = TalkYuuhi + 1

    if judge_lm_condition([]):
        jump block_0000257E

    return

label block_0000257F:
    # Node: 0000257F (夕阳 2)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 300
    show rs_image_92B28690BF524F6E84FED8251700E47B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at center_bottom zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "多亏和那家伙组队，空余时间慢慢有了一些。"

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
        jump block_0000257E

    return

label block_00000A3D:
    # Node: 00000A3D (御咲)
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
        jump block_00000A5B

    return

label block_00000A46:
    # Node: 00000A46 (梅咲)
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
        jump block_00000A59

    return

label block_00000A59:
    # Node: 00000A59 (梅咲)
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


    if judge_lm_condition([{ "scope": 0, "content": "C2SG1 == True" }]):
        jump block_00002587
    if judge_lm_condition([]):
        jump block_00000A5E

    return

label block_00002587:
    # Node: 00002587 (梅咲 翔平)
    $ sys_lm_menu_item = [{"pos": (144, 280),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}, {"pos": (536, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "バス停"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (360, 168),"image": "images/Menu/Shouhei.png","hover": "images/Menu/Shouhei hover.png","name": "翔平"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_530
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"翔平\"" }]):
        jump block_00002585
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"バス停\"" }]):
        jump block_00000A65
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000A63
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A5D

    return

label block_00002585:
    # Node: 00002585 (翔平)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_A127E32D945B4125B278653C460DB2DC as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "呼呼……{w=0.4}{nw}"
    show rs_image_A22A1BB5A368407CB61C4A33509228C5 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不对不对。\n哈哈，你好，你是御咲学园的学生呐。"

    show rs_image_E926B2A719124103B91FE1B37CA2FA0D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "其实我也是从那里毕业的。\n如何？学校生活还不错？"

    show rs_image_A127E32D945B4125B278653C460DB2DC as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9EDF48057FB84D428D56198A69E2880E "说、说起来，\n快到学园祭了是不是。{w}\n时间允许的话我可能会去的。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("梅咲"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00002587

    return

label block_00000A65:
    # Node: 00000A65 (梅咲 square)
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


    if judge_lm_condition([]):
        jump block_00000A67

    return

label block_00000A67:
    # Node: 00000A67 (梅咲 square)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_531
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A59

    return

label block_00000A63:
    # Node: 00000A63 (梅咲 inside)
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
        jump block_00000A66

    return

label block_00000A66:
    # Node: 00000A66 (梅咲 inside)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (120, 336),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "隠し"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_532
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"隠し\"" }]):
        jump block_00000A62
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A59

    return

label block_00000A62:
    # Node: 00000A62 (Alley)
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


    if judge_lm_condition([]):
        jump block_00000A64

    return

label block_00000A64:
    # Node: 00000A64 (Alley)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_533
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A63

    return

label block_00000A5D:
    # Node: 00000A5D (Station)
    $ zorder_tag_D71B998959E446A69B3BAF1EFCCB35F6 = 400

    if judge_lm_condition([]):
        jump block_00000A61

    return

label block_00000A61:
    # Node: 00000A61 (選擇)
    call scb_bus_selector(show_misaki=True, show_takarasaki=True, show_umesaki=False) from _call_scb_bus_selector_11


    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"乗らない\"" },{ "scope": 1, "content": "C2SG1 == True" }]):
        jump block_00002587
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"乗らない\"" }]):
        jump block_00003BD2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲\"" }]):
        jump block_00000A3D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"宝咲\"" }]):
        jump block_00000A3C

    return

label block_00003BD2:
    # Node: 00003BD2 (Return)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00000A5E

    return

label block_00000A5E:
    # Node: 00000A5E (梅咲)
    $ sys_lm_menu_item = [{"pos": (144, 280),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}, {"pos": (536, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "バス停"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_534
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A5D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000A63
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"バス停\"" }]):
        jump block_00000A65

    return

label block_00003BC2:
    # Node: 00003BC2 (Return)
    hide tag_D71B998959E446A69B3BAF1EFCCB35F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00000A5F

    return

label block_00002431:
    # Node: 00002431 (Map)
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_507B7F77C4F74464A02D5387DFA7FE2C as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    show rs_image_BE48A05A53B3438C89C8FA4DF06E1A0D as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00000A5F

    return

label block_00000A2F:
    # Node: 00000A2F (Shopping street)
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
        jump block_00000A31

    return

label block_00000A31:
    # Node: 00000A31 (Shopping street)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (288, 192),"image": "images/Menu/Sumoto.png","hover": "images/Menu/Sumoto hover.png","name": "杉本"}, {"pos": (472, 192),"image": "images/Menu/Rikuta.png","hover": "images/Menu/Rikuta hover.png","name": "陸田"}, {"pos": (104, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_535
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003BA8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000A3A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"陸田\"" }]):
        jump block_00000A32
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"杉本\"" }]):
        jump block_00000A2E

    return

label block_00000A3A:
    # Node: 00000A3A (Shopping street inside)
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


    if judge_lm_condition([{ "scope": 0, "content": "C2S6 == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase == 0" },{ "scope": 2, "content": "C2QYuuhiPhase == 0" },{ "scope": 3, "content": "C2S6Phase == 1" }]):
        jump block_000016D3
    if judge_lm_condition([]):
        jump block_00000A3B

    return

label block_000016D3:
    # Node: 000016D3 (Shopping street Dark-lesser flag)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (216, 216),"image": "images/Chapter 2/Menu/Dark lesser.png","hover": "images/Chapter 2/Menu/Dark lesser hover.png","name": "レッサー"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_536
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A2F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"レッサー\"" }]):
        jump block_000016D4

    return

label block_000016D4:
    # Node: 000016D4 (F6)
    show rs_image_91F4C74E7B844945A9976F914A36207F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.8

    window show

    stop music fadeout 2
    $ sys_music_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 300
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12BEDD8AB7E749DCA40215016D03CA83 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_F3B907D24B914291A42F02BC76FE9F29 "唔……！"

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 300
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_412090826A6C42E2B3347E4BAD9CB105 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_B648ADE2B9494D34A3A54A78261040F3 "唔唔唔……！"

    if sys_music_current_file != "sound/BGM/Flurry 1.ogg":
        play music "sound/BGM/Flurry 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 1.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀——！他们是谁——！！"

    show rs_image_37DD260DB3B64875AFF0FBF4F01BD3E9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "别惹上关系比较好。快走。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_12BEDD8AB7E749DCA40215016D03CA83 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_F3B907D24B914291A42F02BC76FE9F29 "稍等，少年哟。"

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 300
    show rs_image_412090826A6C42E2B3347E4BAD9CB105 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    if sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_84659F85E1274169824D6CD3526AEBF8 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_B648ADE2B9494D34A3A54A78261040F3 "过来，少年们哟。"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇追过来了！？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_37DD260DB3B64875AFF0FBF4F01BD3E9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "怎、怎么这么快！腿那么短应该……！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——！哇——！{w}\n{nw}"
    if sys_effect3_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Fall down 1.ogg"

    extend "……呜啊！？"

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_42FB5E6C09A645C38CF6A8D06A4BE7B9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友！！快起来！别让事态更复杂了！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……太恐怖了完全吓得不敢动……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_12BEDD8AB7E749DCA40215016D03CA83 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_84659F85E1274169824D6CD3526AEBF8 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀——！谁来救救我！！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9EDF48057FB84D428D56198A69E2880E "{size=28}{color=#FF0000}幻想火炎{/color}{/size}{size=20}（物理）{/size}{size=28}！！{/size}"

    window hide

    pause 0.4

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title("")
    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003BB3

    return

label block_00003BB3:
    # Node: 00003BB3 (FLAG: CP2F6)
    call block_00003BAD from _call_block_00003BAD

    if judge_lm_condition([]):
        jump block_00003BBF

    return

label block_00003BBF:
    # Node: 00003BBF (FLAG FINISH)
    $ set_window("(標準)")
    pause 1.5

    if sys_music2_current_file != "sound/BGM/Flag finished.ogg":
        play music2 "sound/BGM/Flag finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件{/color}{color=#AA0055}“欢迎来到食人狼之馆”{/color}{color=#0080FF}成功结束。』{/color}"

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
        jump block_00003BB4

    return

label block_00003BB4:
    # Node: 00003BB4 ()
    $ del HananoRandom

    return

label block_00000A3B:
    # Node: 00000A3B (Shopping street inside)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (128, 304),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "本屋"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_537
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00000A2F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"本屋\"" },{ "scope": 1, "content": "C2QYuuhiPhase == 1" }]):
        jump block_00002586
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"本屋\"" }]):
        jump block_00000A4F

    return

label block_00002586:
    # Node: 00002586 (夕阳 QUEST)
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

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    pause 1.8

    if sys_music_current_file != "sound/BGM/Something comical 1.ogg":
        play music "sound/BGM/Something comical 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something comical 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4647E66D4861417FB077A035A142C3DA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 1

    # Gallery unlock: images/CG/Yuuhi quest 1.png
    $ zorder_rs_image_96F52A116B95488881F36C7B55C08BD0 = -100
    show rs_image_96F52A116B95488881F36C7B55C08BD0 as rs_image_96F52A116B95488881F36C7B55C08BD0 zorder zorder_rs_image_96F52A116B95488881F36C7B55C08BD0 onlayer master
    hide rs_image_96F52A116B95488881F36C7B55C08BD0

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_96F52A116B95488881F36C7B55C08BD0 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Paper 1.ogg"

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "………………"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（为什么停在刚开始了，明明后面才是激展开的说。）"

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "（……和传闻一样是以我为模型的漫画。{w}\n主人公的名字是{color=#FF8000}“夕日”{/color}……这个作者到底是什么人？）"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "（哦，这个{color=#3A00C4}“NORI”{/color}就是以朔为原型的！）"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "（……真是一点都不明白，真正的那家伙眼神要更好……）"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    # Gallery unlock: images/CG/Yuuhi quest 1.png
    $ zorder_rs_image_96F52A116B95488881F36C7B55C08BD0 = -100
    show rs_image_96F52A116B95488881F36C7B55C08BD0 as rs_image_96F52A116B95488881F36C7B55C08BD0 zorder zorder_rs_image_96F52A116B95488881F36C7B55C08BD0 onlayer master
    hide rs_image_96F52A116B95488881F36C7B55C08BD0

    show rs_image_96F52A116B95488881F36C7B55C08BD0 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊～这个场景的夕日真的很没用呐！"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔！我才不会犯这种低级错误！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶？"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "啊……哈哈，有些代入感情太多了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦、哦……"
    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "啊！这个地方的NORI作画超级崩坏的～"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_829EA2AED9E74CD48751411FB95D579D as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "那家伙很可爱的！才不会有这种脸！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸欸？？"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不……那个……"

    show rs_image_C528CA6C6F534006B6F789027BE5C781 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "你……"

    show rs_image_13B2B8013F16410E97AC3B196323838B as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔……"

    if sys_effect2_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_6EA79B30E52B4FE8B90AB55D569F24D3 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真是想到好地方了呐～！确实，下一卷NORI的人设就改了。"

    show rs_image_D41A51E2B16F4674B1A8FB746C8F1328 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "你所知道的NORI，不知道后面能不能看到呢。"

    show rs_image_253B2776672D49EA928D506D0DCEB77F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "你的眼神和夕日很像，很投入剧情呐。{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_6EA79B30E52B4FE8B90AB55D569F24D3 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "就那么想看被触手这个那个的剧情嘛！"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_CA65E37C24FB460390BADAD95767936C as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "欸、欸！呃！差不多……"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_CA176C5A71144199A2E3AE0C60846C57 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "原来如此原来如此！那快继续看！下一页就是正篇了！"

    show rs_image_BEE780ABA64C4D7ABB8972D17BDCBFAB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "哦、哦……不过站着看也不好，总之先买下来好了。"

    show rs_image_9E7B821A26DB4648BA5980B3C4E75E0D as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "抱歉，让你陪我到现在，非常感谢。"

    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.35

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    show rs_image_A6E70EA9F30F4DE4AD20434ED388ACFF as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "STOP！"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_C528CA6C6F534006B6F789027BE5C781 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那本书是{color=#FF0000}十八禁{/color}的不能买。"

    window hide

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Ding 1.ogg"

    stop music fadeout 2.2
    $ sys_music_current_file = ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 1.5

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_000025C7

    return

label block_000025C7:
    # Node: 000025C7 (QUEST FINISH)
    $ set_window("(標準)")
    if sys_music2_current_file != "sound/BGM/Quest Finished.ogg":
        play music2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Quest Finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    window hide

    pause 0.9


    if judge_lm_condition([]):
        jump block_00002F02

    return

label block_00002F02:
    # Node: 00002F02 (C2Q夕阳)
    $ C2QYuuhiPhase = 0
    $ C2QYuuhi = True

    if judge_lm_condition([]):
        jump block_00003BA7

    return

label block_00000A4F:
    # Node: 00000A4F (Bookstore)
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


    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"本屋\"" },{ "scope": 1, "content": "C2QYuuhi == True" },{ "scope": 2, "content": "C2SNori == False" }]):
        jump block_000025BD
    if judge_lm_condition([]):
        jump block_00000A50

    return

label block_000025BD:
    # Node: 000025BD (朔 event)
    pause 0.5

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那孩子在看的漫画是……"

    window hide

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.8

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

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    pause 2

    if sys_music_current_file != "sound/BGM/Something comical 1.ogg":
        play music "sound/BGM/Something comical 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something comical 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4647E66D4861417FB077A035A142C3DA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 1

    # Gallery unlock: images/CG/Yuuhi quest 2.png
    $ zorder_rs_image_B6DB788D29BB4DFCBACCD696EA1D68EC = -100
    show rs_image_B6DB788D29BB4DFCBACCD696EA1D68EC as rs_image_B6DB788D29BB4DFCBACCD696EA1D68EC zorder zorder_rs_image_B6DB788D29BB4DFCBACCD696EA1D68EC onlayer master
    hide rs_image_B6DB788D29BB4DFCBACCD696EA1D68EC

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_B6DB788D29BB4DFCBACCD696EA1D68EC as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Paper 1.ogg"

    window show

    rs_character_62324AD297554FE987C680452CEE232E "（和传闻一样，是以我为原型的漫画，而且……）"

    rs_character_62324AD297554FE987C680452CEE232E "（先不说夕阳那笨样子的再现程度，我有的时候也画得太不像样了。）"

    rs_character_62324AD297554FE987C680452CEE232E "（……是为了让漫画看起来有趣么……）"

    rs_character_62324AD297554FE987C680452CEE232E "（不过，剧情还算可以，去给触手它们看看好了。）"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    $ zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E = 200
    show rs_image_9AD45D644515456B9DF8ED034B70000C as tag_E99970E1386B453DAF81C3AE2C72BE8E at center_top zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_62324AD297554FE987C680452CEE232E "我买了。"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "对不起哦，小弟弟，\n这本书是只有成人才能购买的大人的书哦。"

    show rs_image_F33F4D4959B947DB9755DD0A59FB7942 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "啊？"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "所以我是不能卖给小弟弟你的。"

    show rs_image_76EBFB69D3934625A3E97B836F99E8BC as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "真是有趣的发言。为什么以我为原型的漫画我却不能买？"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "原型？……不太明白，\n不过我是不能让你们小孩子看这么过激的内容的。"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "我明白你的立场，所以只是站着看看还是可以的……"

    show rs_image_F33F4D4959B947DB9755DD0A59FB7942 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "过激？"
    if sys_effect2_current_file != "sound/Effect Sound/Gun 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Gun 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Gun 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_9F8EA032E81344E3B32B192681064721 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    extend "{color=#FF00FF}这一页{/color}{w=0.3}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Boom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 2.ogg"

    show rs_image_46726D80EC7B4D48AD2EFED4CDD37F1C as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    extend "还是{color=#FF00FF}这一页{/color}？{w=0.3}{nw}"
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_7F6C95985A7641738465E73831D557C2

    extend ""

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "等，等等，大庭广众之下不要传播那种内容！"

    show rs_image_76BFBAD96CEB4046A3782EFCCAAFAF80 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "这就算过激？真是可笑。"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_9327E92116934E66A96F4E0381646B64 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "实际上作为原型的我做的可更厉害哦。"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "更厉害……？最、最近的孩子真是开放～"

    show rs_image_76EBFB69D3934625A3E97B836F99E8BC as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "正是。现在这种程度根本不算过激。所以，赶紧卖给我。"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "对不起，这是不可能的。"

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_09FDF2AB25994C3CAC45D2D3129D86F4 as tag_E99970E1386B453DAF81C3AE2C72BE8E zorder zorder_tag_E99970E1386B453DAF81C3AE2C72BE8E onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_62324AD297554FE987C680452CEE232E "切……算了。记得以后晚上注意点。"

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_3604BCEDB55E4C4F9EEADD42420298FE as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇，那就是所谓的怪物客人……店长也真是辛苦呐。"

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "没，没什么……{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "也许有点{color=#FF80FF}觉醒{/color}了也说不定。"

    window hide

    pause 0.8

    stop music fadeout 2.2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 1.5

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00002F08

    return

label block_00002F08:
    # Node: 00002F08 (C2S朔)
    $ C2SNori = True

    if judge_lm_condition([]):
        jump block_00003BA7

    return

label block_00000A50:
    # Node: 00000A50 (選擇)
    call scb_selector(_("接下来怎么做？"), [{"name":"時間を潰す", "content":_("在这里打发时间")}, {"name":"やめておく", "content":_("去别处看看")}]) from _call_scb_selector_65

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"やめておく\"" }]):
        jump block_00000A3A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"時間を潰す\"" }]):
        jump block_000025C8

    return

label block_000025C8:
    # Node: 000025C8 (Night)
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
        jump block_000025C9

    return

label block_000025C9:
    # Node: 000025C9 (Shopping street empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_538
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([]):
        jump block_000025CA

    return

label block_000025CA:
    # Node: 000025CA (CP2 Night Misaki)
    call block_00000BD6 from _call_block_00000BD6_1

    if judge_lm_condition([]):
        jump block_00003BAB

    return

label block_00003BAB:
    # Node: 00003BAB ()
    $ del HananoRandom

    return

label block_00000A32:
    # Node: 00000A32 (陸田)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_9E0771C128CD4195A4659B2B4FBF28F2 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([{ "scope": 0, "content": "C2S4 == True" },{ "scope": 1, "content": "TalkSumoRiku > 0" },{ "scope": 2, "content": "TalkSumoRikuF4After == True" }]):
        jump block_0000257C
    if judge_lm_condition([{ "scope": 0, "content": "C2S5 == True" },{ "scope": 1, "content": "TalkSumoRiku > 0" },{ "scope": 2, "content": "TalkSumoRikuF5After == True" }]):
        jump block_0000257A
    if judge_lm_condition([{ "scope": 0, "content": "TalkSumoRiku == 1" }]):
        jump block_00002579
    if judge_lm_condition([{ "scope": 0, "content": "TalkSumoRiku > 1" }]):
        jump block_0000257B
    if judge_lm_condition([]):
        jump block_00002578

    return

label block_0000257C:
    # Node: 0000257C (杉本陸田 F4后)
    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "两位！之前谢谢你们来我们学校演讲！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A0C64D06D4EA4F92855510FDDE59881B as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "那是我们该说的。\n特地招待我们去真是感激不尽。"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1822EC419F9A4507B966E729B92CF65B as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "不过，要说的话其实去御咲学园还有别的目的～"

    show rs_image_D747C71854D04857B61E7060B46E16CF as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7C178421D3DA4E2CB70D4336919888FB "知道吗，御咲学园里\n{w=0.4}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Finger Snap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    extend "似乎会{color=#800080}“出来”{/color}哦？"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "令人心神不宁的，白色的……\n{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5A33491B84034DD2AB1830E78EB16F23 as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……{color=#8000FF}幽霊{/color}！{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_467657E5638242B4A3C3A83FCDCA736C as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "刚才是不是想歪了♪"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_DF31FBF962C346808370F71AAC5FE215 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "似乎在喜欢鬼怪话题的人中还很有名的样子。"

    show rs_image_BF5966E1F19E4459A8639805C22B453E as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "我们也试着申请过取材，但被拒绝了。"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1822EC419F9A4507B966E729B92CF65B as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "本来还想上一次鬼怪类节目的。{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_E1BDBBDA17C84DDCB73CA8B889AA7685 as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    extend "……所以这时候就要用最终手段！找校长来……"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BBD28F8E0F67444D8010E771B520C48A as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "给我忘掉你那{color=#FF00FF}潜规则{/color}！"

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2FB61747AED54E08ACC1F998C30D040F as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "呀——！被将了一军呐☆"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("商店街"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00002F77

    return

label block_00002F77:
    # Node: 00002F77 (END: TalkF4After)
    $ TalkSumoRikuF4After = False

    if judge_lm_condition([]):
        jump block_00003BAA

    return

label block_00003BAA:
    # Node: 00003BAA (TO: Shopping street)

    if judge_lm_condition([]):
        jump block_00003BA9

    return

label block_00003BA9:
    # Node: 00003BA9 (TO: Shopping street)

    if judge_lm_condition([]):
        jump block_00000A31

    return

label block_0000257A:
    # Node: 0000257A (杉本陸田 F5后)
    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_5A33491B84034DD2AB1830E78EB16F23 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_7C178421D3DA4E2CB70D4336919888FB "之前的节目去了车站附近叫做\n{color=#FF00FF}『Mädchen Café』{/color}\n的女仆咖啡店。"

    show rs_image_71CB04B02B4B48DFAA5213665555BCB0 as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "结果顺势陆田君的女仆装就上镜了。"

    if sys_effect2_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2FB61747AED54E08ACC1F998C30D040F as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "呀～♪那可真是超～可爱的！！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3CA3C6E0C60746A1A2486C9D01A035A5 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "这、这种小事不用告诉友同学的，笨蛋杉本！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_E1BDBBDA17C84DDCB73CA8B889AA7685 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "反正迟早会知道的。{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "毕竟照片上推特了，\n而且已经有一万点赞了。"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2741AFFDC8664D7F999B4F8C5DE3F1E5 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "啊！？你什么时候干的！！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_467657E5638242B4A3C3A83FCDCA736C as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "宣传宣传♪\n为了让我们出名还是有必要做的♪"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("商店街"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00002F78

    return

label block_00002F78:
    # Node: 00002F78 (END: TalkF5After)
    $ TalkSumoRikuF5After = False

    if judge_lm_condition([]):
        jump block_00003BAA

    return

label block_00002579:
    # Node: 00002579 (杉本陸田 2)
    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说起来，两位为什么来御咲呢？"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9E0771C128CD4195A4659B2B4FBF28F2 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "因为有个节目“Yo~i Go!”一直在这附近取景。"

    show rs_image_A0C64D06D4EA4F92855510FDDE59881B as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "请务必观看。"
    show rs_image_BF5966E1F19E4459A8639805C22B453E as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "说是这么说，\n但这是早上十点的节目。\n友同学应该没时间看。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这样——真遗憾。{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "啊，不过，也许那孩子会录像呐。"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7753ED91AD104B6C8767AA10B5191840 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "哦，那孩子是？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我的一个朋友，很喜欢这类节目，\n是你们的大粉丝！下次我去问问他录没录下来。"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1822EC419F9A4507B966E729B92CF65B as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "哦～？听起来友同学好像对我们没什么兴趣呐～"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "才、才没有那回事！\n实际见面后我也很喜欢你们的！"

    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E1BDBBDA17C84DDCB73CA8B889AA7685 as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "哦哦！那我和陆田君你更喜欢谁？"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！那个——这个……"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3CA3C6E0C60746A1A2486C9D01A035A5 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "停下杉本，友同学很困扰的。\n适可而止就好。"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("商店街"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00002F13

    return

label block_00002F13:
    # Node: 00002F13 (T ++)
    $ TalkSumoRiku = TalkSumoRiku + 1

    if judge_lm_condition([]):
        jump block_00000A31

    return

label block_0000257B:
    # Node: 0000257B (杉本陸田 3)
    window show

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，对了，之前说的我那个朋友\n说你们如果出写真集他一定会买。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "所以说你们有没有打算出呢？"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E1BDBBDA17C84DDCB73CA8B889AA7685 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "嗯嗯，写真集。{w}\n{nw}"
    show rs_image_71CB04B02B4B48DFAA5213665555BCB0 as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……干脆我们直接拍裸体画集如何，陆田君！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BBD28F8E0F67444D8010E771B520C48A as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "绝对不要。"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_1822EC419F9A4507B966E729B92CF65B as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "欸——！肯定会大卖的。"
    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_E1BDBBDA17C84DDCB73CA8B889AA7685 as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "对了对了，\n至少这个地方的人绝对全都会买的！"

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_71CB04B02B4B48DFAA5213665555BCB0 as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "哦！正好商店街有家有趣的店，\n就在那边卖限定纪念品好了！"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_767DA33F80F84FEA9AAF27A753D98CC9 as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "给当地创造收入，\n充实财政和我们的钱包，\n一石二鸟！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3CA3C6E0C60746A1A2486C9D01A035A5 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "没那么顺利。而且没必要。"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_E1BDBBDA17C84DDCB73CA8B889AA7685 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "不不，谁知道呢。\n其实对少年们饥饿难耐的人有的是♪{w}\n……{w=0.4}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_467657E5638242B4A3C3A83FCDCA736C as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    extend "比如说屏幕前的你！！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_4B9533E6E39449D886CFE2CAC3DC64DA as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "在和谁说话？"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("商店街"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00002F13

    return

label block_00002578:
    # Node: 00002578 (杉本陸田 1)
    window show

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊！是{color=#FF8040}陆田＆杉本{/color}！\n哇——！又来御咲了呐！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A569046BCD024D88AE82AC60195924D4 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "谢谢，你好。\n记得你在相扑大赛现场出现过。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对呀——对呀——！\n好高兴♪还记得我呐！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E1BDBBDA17C84DDCB73CA8B889AA7685 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "顾客就是上帝……\n这就是我们的工作MODE！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "MODE{size=12}{color=#C0C0C0}（日文读法MOTO）{/color}{/size}！好高大上！{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "说起来我的名字正好和那个相反，\nTOMO！友哦～！请多关照了！"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说笑的——♪"

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Ding 1.ogg"

    hide tag_E0B8A219896B49168D47409135D3624F
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 1

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不、那个～对了，\n实际看上去你们果然很可爱呐。\n只是这样也足以招到一大批粉丝了。"

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BF5966E1F19E4459A8639805C22B453E as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "谢、谢谢。\n不过实际上还是希望客人\n比起我们本身多看看我们的演出……"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_2FB61747AED54E08ACC1F998C30D040F as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "嘛！反正这个世界可爱就是正义♪{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_C88671E398BA45A6AB98E1C93AC93B9D as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "也能好好利用{color=#FF00FF}潜规则{/color}！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BBD28F8E0F67444D8010E771B520C48A as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "什么东西！！\n这个梗地图炮太大以后别用了！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_767DA33F80F84FEA9AAF27A753D98CC9 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "不愧是陆田君！\n今天的吐槽也是这么精辟呐♪{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    extend "对！吐槽当然是越快越好！"

    if sys_effect2_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_467657E5638242B4A3C3A83FCDCA736C as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "不过，床上的“{color=#FF00FF}吐槽{/color}”就\n必须要有时间长度了呐♪{w}\n不要在意你的速度，陆田君☆"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2741AFFDC8664D7F999B4F8C5DE3F1E5 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "天知道！！\n{w=0.35}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_BBD28F8E0F67444D8010E771B520C48A as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不，你就该被弄到直不起腰来！"

    if sys_effect2_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    show rs_image_BBD28F8E0F67444D8010E771B520C48A as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "然后第二天爬着去医院挂号！\n你就该这么来一次长长记性！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_1822EC419F9A4507B966E729B92CF65B as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "不，陆田君的尺寸恐怕做不到。嗯。"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_4B9533E6E39449D886CFE2CAC3DC64DA as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "也对。{w=0.4}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2741AFFDC8664D7F999B4F8C5DE3F1E5 as tag_E0B8A219896B49168D47409135D3624F zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……才不对！\n道歉！现在立马道歉！！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 200
    show rs_image_767DA33F80F84FEA9AAF27A753D98CC9 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "以上——谢谢各位收看——"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——！鼓掌鼓掌鼓掌！{w}\n不错！名组合！\n果然杉本陆田的下流梗就是好！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "以后我也会支持你们的！请加油！"

    hide tag_E0B8A219896B49168D47409135D3624F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("商店街"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00002F13

    return

label block_00000A2E:
    # Node: 00000A2E (杉本)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ zorder_tag_E0B8A219896B49168D47409135D3624F = 300
    show rs_image_7753ED91AD104B6C8767AA10B5191840 as tag_E0B8A219896B49168D47409135D3624F at center_bottom zorder zorder_tag_E0B8A219896B49168D47409135D3624F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([{ "scope": 0, "content": "C2S4 == True" },{ "scope": 1, "content": "TalkSumoRiku > 0" },{ "scope": 2, "content": "TalkSumoRikuF4After == True" }]):
        jump block_0000257C
    if judge_lm_condition([{ "scope": 0, "content": "C2S5 == True" },{ "scope": 1, "content": "TalkSumoRiku > 0" },{ "scope": 2, "content": "TalkSumoRikuF5After == True" }]):
        jump block_0000257A
    if judge_lm_condition([{ "scope": 0, "content": "TalkSumoRiku == 1" }]):
        jump block_00002579
    if judge_lm_condition([{ "scope": 0, "content": "TalkSumoRiku > 1" }]):
        jump block_0000257B
    if judge_lm_condition([]):
        jump block_00002578

    return

label block_00003BA5:
    # Node: 00003BA5 (TO: Park)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"


    if judge_lm_condition([]):
        jump block_00000A29

    return

label block_00000A29:
    # Node: 00000A29 (Park)
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


    if judge_lm_condition([{ "scope": 0, "content": "CXQKaruta == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "C2QYuuhiPhase == 0" }]):
        jump block_00002574
    if judge_lm_condition([]):
        jump block_00000A2C

    return

label block_00002574:
    # Node: 00002574 (Park 小林 quest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (160, 184),"image": "images/Menu/Kobayashi quest.png","hover": "images/Menu/Kobayashi hover.png","name": "小林"}, {"pos": (320, 184),"image": "images/Menu/Minami.png","hover": "images/Menu/Minami hover.png","name": "南"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_539
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小林\"" }]):
        jump block_00000A33
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"南\"" }]):
        jump block_00000A34
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003BA8

    return

label block_00000A33:
    # Node: 00000A33 (小林)
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

    rs_character_EA79386263E543A88D4DC03B8BD44485 "什么嘛，一股老人气——？{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_E714266E48C34071B1AFC8E511D39DD5 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那下次就不叫“友哥”改叫“友叔”好了。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔，年轻人就是不知轻重！我还宝刀未……{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "不不不，这个梗对你们还太早了。"

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
        jump block_000025C3

    return

label block_000025C3:
    # Node: 000025C3 (小林翻歌牌)
    call block_000020C2 from _call_block_000020C2_2

    if judge_lm_condition([{ "scope": 0, "content": "CXQKaruta == False" }]):
        jump block_000025C5
    if judge_lm_condition([]):
        jump block_00003C86

    return

label block_000025C5:
    # Node: 000025C5 (After)
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

    rs_character_9A978AAD07624C598B6179F23F51FB2D "虽然不知道是什么时候，\n但下次遇到爷爷时我们会多要一些牌的。"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("公园"))

    if judge_lm_condition([]):
        jump block_000025C6

    return

label block_000025C6:
    # Node: 000025C6 (QUEST FINISH)
    $ set_window("(標準)")
    if sys_music2_current_file != "sound/BGM/Quest Finished.ogg":
        play music2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Quest Finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    window hide

    pause 0.8


    if judge_lm_condition([]):
        jump block_00002F19

    return

label block_00002F19:
    # Node: 00002F19 (CXQKaruta)
    $ CXQKaruta = True

    if judge_lm_condition([]):
        jump block_00002F1B

    return

label block_00002F1B:
    # Node: 00002F1B (CLEAR)
    $ GKarutaViewMode = False

    if judge_lm_condition([]):
        jump block_00000A2C

    return

label block_00000A2C:
    # Node: 00000A2C (Park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (160, 184),"image": "images/Menu/Kobayashi.png","hover": "images/Menu/Kobayashi hover.png","name": "小林"}, {"pos": (320, 184),"image": "images/Menu/Minami.png","hover": "images/Menu/Minami hover.png","name": "南"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_540
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003BA8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小林\"" },{ "scope": 1, "content": "CXQKaruta == True" }]):
        jump block_00002577
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"南\"" },{ "scope": 1, "content": "CXQKaruta == True" }]):
        jump block_00002576
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"南\"" }]):
        jump block_00000A34
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小林\"" }]):
        jump block_00002F28

    return

label block_00002577:
    # Node: 00002577 (小林)
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
        jump block_000025C2

    return

label block_000025C2:
    # Node: 000025C2 (選擇)
    call scb_selector("", [{"name":"はい", "content":_("好呀")}, {"name":"いいえ", "content":_("以后再说")}]) from _call_scb_selector_66

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_000025C3
    if judge_lm_condition([]):
        jump block_00002F1B

    return

label block_00002576:
    # Node: 00002576 (南)
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
        jump block_00002F1A

    return

label block_00002F1A:
    # Node: 00002F1A (ViewMode)
    $ GKarutaViewMode = True

    if judge_lm_condition([]):
        jump block_000025C2

    return

label block_00000A34:
    # Node: 00000A34 (南)
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


    if judge_lm_condition([{ "scope": 0, "content": "CXQKaruta == False" },{ "scope": 1, "content": "C2S1Phase + C2S2Phase + C2S3Phase + C2S4Phase + C2S5Phase + C2S6Phase == 0" },{ "scope": 2, "content": "C2QYuuhiPhase == 0" }]):
        jump block_00002574
    if judge_lm_condition([]):
        jump block_00000A2C

    return

label block_00002F28:
    # Node: 00002F28 (小林)
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
        jump block_00000A2C

    return

label block_00003C86:
    # Node: 00003C86 (CLEAR)
    $ GKarutaViewMode = False

    if judge_lm_condition([]):
        jump block_00003BA5

    return

label block_00000A22:
    # Node: 00000A22 (Conversation F6)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍——我们要不要去什么地方玩？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "无所谓，友说了算。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真是的，老是推给别人——！"

    window hide

    $ set_window("(標準)")

    return

label block_00000A23:
    # Node: 00000A23 (Target F6)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『请试着寻找下一个同类{/color}{color=#AA0055}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001FB2:
    # Node: 00001FB2 (Abandon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    jump block_00002F03

    return

label block_00002F03:
    # Node: 00002F03 (RESET)
    $ C2S1Phase = 0
    $ C2S2Phase = 0
    $ C2S3Phase = 0
    $ C2S4Phase = 0
    $ C2S5Phase = 0
    $ C2S6Phase = 0
    $ C2QYuuhiPhase = 0

    if judge_lm_condition([]):
        jump block_00000A21

    return

label block_000025B6:
    # Node: 000025B6 (Character 友+夕阳)
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

label block_00001FB0:
    # Node: 00001FB0 (Character 友+忍)
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

label block_000025B5:
    # Node: 000025B5 (Conversation Q夕阳)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "请带我到书店！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好的好——的。"

    window hide

    $ set_window("(標準)")

    return

label block_000025B4:
    # Node: 000025B4 (Target Q夕阳)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『带夕阳到商店街的书店。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_000025B7:
    # Node: 000025B7 (友+夕阳)
    $ sys_ayumi_global_map_character = "tomo_yuuhi"
    $ sys_ayumi_global_map_time = "twilight"

    if judge_lm_condition([]):
        jump block_00000A25

    return

label block_0000193C:
    # Node: 0000193C (友)
    $ sys_ayumi_global_map_character = "tomo"
    $ sys_ayumi_global_map_time = "twilight"

    if judge_lm_condition([{ "scope": 0, "content": "C2S5Phase == 1" }]):
        jump block_00000A25
    if judge_lm_condition([]):
        jump block_00001FB4

    return

label block_00001FB4:
    # Node: 00001FB4 (Misaki LCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "misaki", True, False, talk_label="block_00001FB7", target_label="block_00001FB6") from _call_scb_global_map_145
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲学園\"" }]):
        jump block_00000A28
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"住宅街\"" }]):
        jump block_00000A26
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"商店街\"" }]):
        jump block_00000A2F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"公園\"" }]):
        jump block_00003BA5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲駅\"" }]):
        jump block_00000A5B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"昼休み\"" }]):
        jump block_0000256C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00001FB7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00001FB6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00001FB4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FB5

    return

label block_0000256C:
    # Node: 0000256C (Lunchtime)
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

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"


    if judge_lm_condition([]):
        jump block_00003BA6

    return

label block_00003BA6:
    # Node: 00003BA6 ()
    $ del HananoRandom

    return

label block_00001FB7:
    # Node: 00001FB7 (Conversation)
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

label block_00001FB6:
    # Node: 00001FB6 (Target)
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

label block_00001FB5:
    # Node: 00001FB5 (Character)
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

