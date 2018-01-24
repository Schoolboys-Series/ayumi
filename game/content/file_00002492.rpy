# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00002492 (向左向右看)

label block_00002493:
    # Node: 00002493 (開始)
    $ WinCount = 0
    $ LoseCount = 0
    $ Direction = 0

    $ set_place_title(False)

    if judge_lm_condition([]):
        jump block_00002494

    return

label block_00002494:
    # Node: 00002494 (Background)
    $ set_window("イベントモード")
    $ zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 = 100
    $ zorder_tag_785986DA3E45437F86349ADFE1D48F65 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_E2D067C3F2BE4328877C1AB2D1DA1358 = 400
    show rs_image_9F1237FF00C1491988191E9951FA67B8 as tag_BB92C9F2A35745708E1E70CBF033E3C3 at center_bottom zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_1B5A1C35A67D4834BD403367DB242CF6 as tag_785986DA3E45437F86349ADFE1D48F65 at center_top zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    show rs_image_38AAC7CBF1C048418BB73977873FF00A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_533E2F01D5554238B77AB01C0A714BE3 as tag_E2D067C3F2BE4328877C1AB2D1DA1358 at center_bottom zorder zorder_tag_E2D067C3F2BE4328877C1AB2D1DA1358 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.5

    if sys_music_current_file != "sound/BGM/Ailurus fulgens.ogg":
        play music "sound/BGM/Ailurus fulgens.ogg" loop
        $ sys_music_current_file = "sound/BGM/Ailurus fulgens.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『当贝——和箭头{/color}{color=#80FFFF}方向相同{/color}{color=#0080FF}时，\n请迅速点按{/color}{color=#80FFFF}屏幕任何位置{/color}{color=#0080FF}。三局两胜。\n那么……{/color}{w}{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "{color=#FF00FF}开始{/color}{color=#FF00FF}{b}！{/b}{/color}』"

    window hide


    if judge_lm_condition([]):
        jump block_00002923

    return

label block_00002923:
    # Node: 00002923 (Random)
    $ Direction = Random(2)

    if judge_lm_condition([{ "scope": 0, "content": "WinCount + LoseCount == 3" },{ "scope": 1, "content": "VarExists(\"C1S4Phase\") == True" }]):
        jump block_000024E0
    if judge_lm_condition([{ "scope": 0, "content": "WinCount + LoseCount == 3" }]):
        jump block_00003282
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 1" }]):
        jump block_00002921
    if judge_lm_condition([]):
        jump block_00002922

    return

label block_000024E0:
    # Node: 000024E0 (Finish F1)
    pause 0.5

    $ set_place_title(_("河边"))

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    hide tag_E2D067C3F2BE4328877C1AB2D1DA1358
    hide tag_BB92C9F2A35745708E1E70CBF033E3C3
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_785986DA3E45437F86349ADFE1D48F65
    with rs_effect_E36043F8C80E4415B6B2D5553D497F8B

    pause 1.5


    if judge_lm_condition([{ "scope": 0, "content": "WinCount < LoseCount" }]):
        jump block_0000292C
    if judge_lm_condition([]):
        jump block_000024E1

    return

label block_0000292C:
    # Node: 0000292C (Lose)
    $ set_window("(標準)")
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_788AB1D278244B129D0C9F9230156AD7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    show rs_image_E7FB89F14D554B59971676B5C3A3F54D as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "{color=#FF8040}贝——{/color}的胜利哦！\n好开心！下次也要一起玩！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_8CD2535C08AE46B7B132445AFB7B0757 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "（不、不能太投入，\n在那种异空间里时间太久脑袋会变奇怪的……）"

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg"


    if judge_lm_condition([]):
        jump block_000036F4

    return

label block_000036F4:
    # Node: 000036F4 ()
    $ del WinCount
    $ del LoseCount
    $ del Direction

    return

label block_000024E1:
    # Node: 000024E1 (Win)
    $ set_window("(標準)")
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_788AB1D278244B129D0C9F9230156AD7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    show rs_image_E7FB89F14D554B59971676B5C3A3F54D as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "{color=#FF80FF}四朗{/color}的胜利哦！\n好开心！下次也要一起玩！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_8CD2535C08AE46B7B132445AFB7B0757 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "（不、不能太投入，\n在那种异空间里时间太久脑袋会变奇怪的……）"

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_259DAA3A48AE4C88AAFFA198DA88CA62 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg"


    if judge_lm_condition([]):
        jump block_000036F4

    return

label block_00003282:
    # Node: 00003282 (Finish)
    pause 0.5

    $ set_place_title(_("河边"))

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    hide tag_E2D067C3F2BE4328877C1AB2D1DA1358
    hide tag_BB92C9F2A35745708E1E70CBF033E3C3
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_785986DA3E45437F86349ADFE1D48F65
    with rs_effect_E36043F8C80E4415B6B2D5553D497F8B

    pause 1.5


    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 3" }]):
        jump block_00004253
    if judge_lm_condition([{ "scope": 0, "content": "WinCount > LoseCount" },{ "scope": 1, "content": "END == True" }]):
        jump block_00002FF5
    if judge_lm_condition([{ "scope": 0, "content": "END == True" }]):
        jump block_00002FF4
    if judge_lm_condition([]):
        jump block_00004254

    return

label block_00004253:
    # Node: 00004253 (CHECK)

    if judge_lm_condition([{ "scope": 0, "content": "C3QShiro == True" }]):
        jump block_00004254
    if judge_lm_condition([{ "scope": 0, "content": "WinCount < LoseCount" }]):
        jump block_0000292D
    if judge_lm_condition([]):
        jump block_000027B9

    return

label block_00004254:
    # Node: 00004254 (CHECK)

    if judge_lm_condition([{ "scope": 0, "content": "WinCount > LoseCount" }]):
        jump block_00003F36
    if judge_lm_condition([]):
        jump block_00003F35

    return

label block_00003F36:
    # Node: 00003F36 (Win C3)
    $ set_window("(標準)")
    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_8861B7E1375F4D40AC5B5B4F86821894 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7AC620439A6042AF98D62C983235F7D4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈！是我赢了～♪"

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    pause 0.3

    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"


    if judge_lm_condition([]):
        jump block_00003978

    return

label block_00003978:
    # Node: 00003978 ()
    $ del WinCount
    $ del LoseCount
    $ del Direction

    return

label block_00003F35:
    # Node: 00003F35 (Lose C3)
    $ set_window("(標準)")
    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_2A275097531843819D64C7AD61316D2B as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7AC620439A6042AF98D62C983235F7D4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……居然会输给小熊猫……"

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    pause 0.3

    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"


    if judge_lm_condition([]):
        jump block_00003978

    return

label block_0000292D:
    # Node: 0000292D (Lose C3Q四朗)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7AC620439A6042AF98D62C983235F7D4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 = 200
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_059C21EE40DA45BB8CEE77053FCF922C as tag_BB92C9F2A35745708E1E70CBF033E3C3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_311C0DF0CF504684BAB1C36398430D4D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "（拍手）～。{color=#FF8040}贝——{/color}的胜利～！"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哈哈♪好高兴——！"

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "姆姆♪"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB92C9F2A35745708E1E70CBF033E3C3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 = 300
    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_628CBB6D3CA24E23958195F453C57AF1 as tag_BB92C9F2A35745708E1E70CBF033E3C3 at right_top zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是嘛是嘛，很怀念的呐？\n{w=0.6}{nw}"
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_166E61569A9246C3AEB94A8278FC2C50 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "来摸一下……"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_BB92C9F2A35745708E1E70CBF033E3C3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "姆！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好痛！这、这家伙居然用头撞我！？"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 = 200
    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BFC4A160DFDF465C82BD02885E29367D as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_652D7701AFFE418E87F460AA0381F86F as tag_BB92C9F2A35745708E1E70CBF033E3C3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不、不是很明白不过，是对前辈看不顺眼的意思吧。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——为什么……"

    show rs_image_166E61569A9246C3AEB94A8278FC2C50 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "姆——姆。姆、姆呼。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "{color=#FF8000}『友很不讨喜，但欢迎来玩。』{/color}"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "这样说的。"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "总觉得被看扁了……{w}那我有兴趣的时候再回来好了。"

    window hide

    pause 0.8

    stop music fadeout 2.2
    $ sys_music_current_file = ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_BB92C9F2A35745708E1E70CBF033E3C3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 1.5

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_0000425B

    return

label block_0000425B:
    # Node: 0000425B (C3Q四朗)
    $ C3QShiro = True
    $ TalkTsubasaQShiroAfter = True

    if judge_lm_condition([]):
        jump block_000027BB

    return

label block_000027BB:
    # Node: 000027BB (QUEST FINISH)
    $ set_window("(標準)")
    if sys_music2_current_file != "sound/BGM/Quest Finished.ogg":
        play music2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Quest Finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    window hide

    pause 0.8


    if judge_lm_condition([]):
        jump block_00003978

    return

label block_000027B9:
    # Node: 000027B9 (Win C3Q四朗)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7AC620439A6042AF98D62C983235F7D4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 = 200
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    show rs_image_059C21EE40DA45BB8CEE77053FCF922C as tag_BB92C9F2A35745708E1E70CBF033E3C3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_311C0DF0CF504684BAB1C36398430D4D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "（拍手）～。{color=#FF80FF}前辈{/color}的胜利～！"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哈哈♪好高兴——！"

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "姆姆♪"

    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB92C9F2A35745708E1E70CBF033E3C3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 = 300
    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_628CBB6D3CA24E23958195F453C57AF1 as tag_BB92C9F2A35745708E1E70CBF033E3C3 at right_top zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是嘛是嘛，很怀念的呐？\n{w=0.6}{nw}"
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_166E61569A9246C3AEB94A8278FC2C50 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    extend "来摸一下……"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_BB92C9F2A35745708E1E70CBF033E3C3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "姆！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好痛！这、这家伙居然用头撞我！？"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    $ zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 = 200
    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BFC4A160DFDF465C82BD02885E29367D as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    show rs_image_652D7701AFFE418E87F460AA0381F86F as tag_BB92C9F2A35745708E1E70CBF033E3C3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不、不是很明白不过，\n是对前辈看不顺眼的意思吧。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——为什么……"

    show rs_image_166E61569A9246C3AEB94A8278FC2C50 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6F33979BA6C944E5A96C6C4DD753C97F "姆——姆。姆、姆呼。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 200
    show rs_image_48E89875ADC24E3987D4AA23DC193AA4 as tag_A469B787E7E7466FA1613F380A4CBF41 at center_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "{color=#FF8000}『友很不讨喜，但欢迎来玩。』{/color}"

    show rs_image_E390D3BA5C4D4B61AAF854D34D0E8413 as tag_A469B787E7E7466FA1613F380A4CBF41 zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "这样说的。"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "总觉得被看扁了……{w}那我有兴趣的时候再回来好了。"

    window hide

    pause 0.8

    stop music fadeout 2.2
    $ sys_music_current_file = ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_BB92C9F2A35745708E1E70CBF033E3C3
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 1.5

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_0000425B

    return

label block_00002FF5:
    # Node: 00002FF5 (Win)
    $ set_window("(標準)")
    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_8861B7E1375F4D40AC5B5B4F86821894 as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7AC620439A6042AF98D62C983235F7D4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈！是我赢了～♪"

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    pause 0.3

    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"


    if judge_lm_condition([]):
        jump block_00003978

    return

label block_00002FF4:
    # Node: 00002FF4 (Lose)
    $ set_window("(標準)")
    $ zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_2A275097531843819D64C7AD61316D2B as tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 at center_bottom zorder zorder_tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6 onlayer master
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7AC620439A6042AF98D62C983235F7D4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……居然会输给小熊猫……"

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_DD3F6E8E956D4F1BB1131F81FF9AA4F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    pause 0.3

    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"


    if judge_lm_condition([]):
        jump block_00003978

    return

label block_00002921:
    # Node: 00002921 (Random 右)
    $ Direction = Random(10)

    if judge_lm_condition([{ "scope": 0, "content": "Direction == 0" }]):
        jump block_000024A2
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 1" }]):
        jump block_000024A1
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 2" }]):
        jump block_000024A0
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 3" }]):
        jump block_0000249F
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 4" }]):
        jump block_000024A7
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 5" }]):
        jump block_000024A6
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 6" }]):
        jump block_000024A5
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 7" }]):
        jump block_000024A4
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 8" }]):
        jump block_000024AD
    if judge_lm_condition([]):
        jump block_0000367A

    return

label block_000024A2:
    # Node: 000024A2 (右○１)

    show rs_image_1A58ECC9283B4ED7850AF9BBDB2A6F41 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_1B5A1C35A67D4834BD403367DB242CF6 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_0000291F

    return

label block_0000291F:
    # Node: 0000291F (右○)
    $ sys_lm_menu_item = [{"pos": (0, 0),"image": "images/EFFECT/COLOR/Total transparent.png","hover": "","name": "クリック"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0.4, 0, 0) from _call_lm_menu_372
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クリック\"" }]):
        jump block_0000291D
    if judge_lm_condition([]):
        jump block_00002922

    return

label block_0000291D:
    # Node: 0000291D (右成功)
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_533E2F01D5554238B77AB01C0A714BE3 as tag_E2D067C3F2BE4328877C1AB2D1DA1358 zorder zorder_tag_E2D067C3F2BE4328877C1AB2D1DA1358 onlayer master
    show rs_image_B88D8D4EDBF24CDDB2EFF78AAAE590EF as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_07B2737B6ED5411CAA7B250F6E0119B5 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7


    if judge_lm_condition([]):
        jump block_0000292F

    return

label block_0000292F:
    # Node: 0000292F (Win)
    $ WinCount = WinCount + 1

    if judge_lm_condition([]):
        jump block_00003677

    return

label block_00003677:
    # Node: 00003677 (TO: Random)

    if judge_lm_condition([]):
        jump block_00003676

    return

label block_00003676:
    # Node: 00003676 (TO: Random)

    if judge_lm_condition([]):
        jump block_00002923

    return

label block_00002922:
    # Node: 00002922 (Random 左)
    $ Direction = Random(10)

    if judge_lm_condition([{ "scope": 0, "content": "Direction == 0" }]):
        jump block_00002495
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 1" }]):
        jump block_0000249B
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 2" }]):
        jump block_0000249C
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 3" }]):
        jump block_0000249E
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 4" }]):
        jump block_000024AA
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 5" }]):
        jump block_000024A9
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 6" }]):
        jump block_000024A8
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 7" }]):
        jump block_000024AB
    if judge_lm_condition([{ "scope": 0, "content": "Direction == 8" }]):
        jump block_000024AD
    if judge_lm_condition([]):
        jump block_0000367A

    return

label block_00002495:
    # Node: 00002495 (左○１)

    show rs_image_1294321972354D459206CE61E5EBCB56 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_7CAA7DD563B5419F924FC7C46B728CEE as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002496

    return

label block_00002496:
    # Node: 00002496 (左○)
    $ sys_lm_menu_item = [{"pos": (0, 0),"image": "images/EFFECT/COLOR/Total transparent.png","hover": "","name": "クリック"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0.4, 0, 0) from _call_lm_menu_373
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クリック\"" }]):
        jump block_00002497
    if judge_lm_condition([]):
        jump block_00002921

    return

label block_00002497:
    # Node: 00002497 (左成功)
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_533E2F01D5554238B77AB01C0A714BE3 as tag_E2D067C3F2BE4328877C1AB2D1DA1358 zorder zorder_tag_E2D067C3F2BE4328877C1AB2D1DA1358 onlayer master
    show rs_image_B88D8D4EDBF24CDDB2EFF78AAAE590EF as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_07B2737B6ED5411CAA7B250F6E0119B5 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7


    if judge_lm_condition([]):
        jump block_0000292F

    return

label block_0000249B:
    # Node: 0000249B (左○２)

    show rs_image_1294321972354D459206CE61E5EBCB56 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_E331F891C11E42DDB235CAD8165D054C as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002496

    return

label block_0000249C:
    # Node: 0000249C (左○３)

    show rs_image_811F5A9DE5214D44938117C1A609FAD1 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_E331F891C11E42DDB235CAD8165D054C as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002496

    return

label block_0000249E:
    # Node: 0000249E (左○４)

    show rs_image_811F5A9DE5214D44938117C1A609FAD1 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_7CAA7DD563B5419F924FC7C46B728CEE as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002496

    return

label block_000024AA:
    # Node: 000024AA (右×１)

    show rs_image_1294321972354D459206CE61E5EBCB56 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_1B5A1C35A67D4834BD403367DB242CF6 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002920

    return

label block_00002920:
    # Node: 00002920 (右×)
    $ sys_lm_menu_item = [{"pos": (0, 0),"image": "images/EFFECT/COLOR/Total transparent.png","hover": "","name": "クリック"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0.4, 0, 0) from _call_lm_menu_374
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クリック\"" }]):
        jump block_0000291E
    if judge_lm_condition([]):
        jump block_00002921

    return

label block_0000291E:
    # Node: 0000291E (右失敗)
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_533E2F01D5554238B77AB01C0A714BE3 as tag_E2D067C3F2BE4328877C1AB2D1DA1358 zorder zorder_tag_E2D067C3F2BE4328877C1AB2D1DA1358 onlayer master
    show rs_image_CAB356CBF3B940BCA386522C65912083 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_755D612D42F44947B2A0CCDA88BCE8E4 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7


    if judge_lm_condition([]):
        jump block_00002930

    return

label block_00002930:
    # Node: 00002930 (Lost)
    $ LoseCount = LoseCount + 1

    if judge_lm_condition([]):
        jump block_00003679

    return

label block_00003679:
    # Node: 00003679 (TO: Random)

    if judge_lm_condition([]):
        jump block_00003678

    return

label block_00003678:
    # Node: 00003678 (TO: Random)

    if judge_lm_condition([]):
        jump block_00002923

    return

label block_000024A9:
    # Node: 000024A9 (右×２)

    show rs_image_1294321972354D459206CE61E5EBCB56 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_2C00E73A14FE422EA3CDCAE348E37304 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002920

    return

label block_000024A8:
    # Node: 000024A8 (右×３)

    show rs_image_811F5A9DE5214D44938117C1A609FAD1 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_1B5A1C35A67D4834BD403367DB242CF6 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002920

    return

label block_000024AB:
    # Node: 000024AB (右×４)

    show rs_image_811F5A9DE5214D44938117C1A609FAD1 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_2C00E73A14FE422EA3CDCAE348E37304 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002920

    return

label block_000024AD:
    # Node: 000024AD (正面×１)

    show rs_image_8C9C81B5D0E647A5A05518899B00E2EF as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_1B5A1C35A67D4834BD403367DB242CF6 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002926

    return

label block_00002926:
    # Node: 00002926 (正面×)
    $ sys_lm_menu_item = [{"pos": (0, 0),"image": "images/EFFECT/COLOR/Total transparent.png","hover": "","name": "クリック"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0.4, 0, 0) from _call_lm_menu_375
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クリック\"" }]):
        jump block_0000292A
    if judge_lm_condition([]):
        jump block_00002923

    return

label block_0000292A:
    # Node: 0000292A (正面失敗)
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_533E2F01D5554238B77AB01C0A714BE3 as tag_E2D067C3F2BE4328877C1AB2D1DA1358 zorder zorder_tag_E2D067C3F2BE4328877C1AB2D1DA1358 onlayer master
    show rs_image_CAB356CBF3B940BCA386522C65912083 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_755D612D42F44947B2A0CCDA88BCE8E4 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7


    if judge_lm_condition([]):
        jump block_00002930

    return

label block_0000367A:
    # Node: 0000367A (正面×２)

    show rs_image_FE12AB1EB51B4E15940A78C58668093B as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_E331F891C11E42DDB235CAD8165D054C as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002926

    return

label block_000024A1:
    # Node: 000024A1 (右○２)

    show rs_image_1A58ECC9283B4ED7850AF9BBDB2A6F41 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_2C00E73A14FE422EA3CDCAE348E37304 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_0000291F

    return

label block_000024A0:
    # Node: 000024A0 (右○３)

    show rs_image_3C3B7861426540029F0F8C085344430A as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_1B5A1C35A67D4834BD403367DB242CF6 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_0000291F

    return

label block_0000249F:
    # Node: 0000249F (右○４)

    show rs_image_3C3B7861426540029F0F8C085344430A as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_2C00E73A14FE422EA3CDCAE348E37304 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_0000291F

    return

label block_000024A7:
    # Node: 000024A7 (左×１)

    show rs_image_1A58ECC9283B4ED7850AF9BBDB2A6F41 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_E331F891C11E42DDB235CAD8165D054C as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002499

    return

label block_00002499:
    # Node: 00002499 (左×)
    $ sys_lm_menu_item = [{"pos": (0, 0),"image": "images/EFFECT/COLOR/Total transparent.png","hover": "","name": "クリック"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0.4, 0, 0) from _call_lm_menu_376
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"クリック\"" }]):
        jump block_0000249A
    if judge_lm_condition([]):
        jump block_00002922

    return

label block_0000249A:
    # Node: 0000249A (左失敗)
    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_533E2F01D5554238B77AB01C0A714BE3 as tag_E2D067C3F2BE4328877C1AB2D1DA1358 zorder zorder_tag_E2D067C3F2BE4328877C1AB2D1DA1358 onlayer master
    show rs_image_CAB356CBF3B940BCA386522C65912083 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_755D612D42F44947B2A0CCDA88BCE8E4 as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7


    if judge_lm_condition([]):
        jump block_00002930

    return

label block_000024A6:
    # Node: 000024A6 (左×２)

    show rs_image_1A58ECC9283B4ED7850AF9BBDB2A6F41 as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_7CAA7DD563B5419F924FC7C46B728CEE as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002499

    return

label block_000024A5:
    # Node: 000024A5 (左×３)

    show rs_image_3C3B7861426540029F0F8C085344430A as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_E331F891C11E42DDB235CAD8165D054C as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002499

    return

label block_000024A4:
    # Node: 000024A4 (左×４)

    show rs_image_3C3B7861426540029F0F8C085344430A as tag_BB92C9F2A35745708E1E70CBF033E3C3 zorder zorder_tag_BB92C9F2A35745708E1E70CBF033E3C3 onlayer master
    show rs_image_7CAA7DD563B5419F924FC7C46B728CEE as tag_785986DA3E45437F86349ADFE1D48F65 zorder zorder_tag_785986DA3E45437F86349ADFE1D48F65 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if judge_lm_condition([]):
        jump block_00002499

    return

