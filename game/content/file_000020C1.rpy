# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 000020C1 (小林翻歌牌)

label block_000020C2:
    # Node: 000020C2 (開始)
    $ CurrentIndex = -1
    $ CardList = 0
    $ FailCount = 0
    $ CurrentCardNumber = 0
    $ CardStatus = 0
    $ WinCount = 0
    $ LoseCount = 0
    $ CurrentResult = 0

    $ set_place_title(False)

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    image karuta_title = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#000000",
        size=30,
        text_align=0)

    if judge_lm_condition([{ "scope": 0, "content": "GKarutaViewMode == True" }]):
        jump block_00002259
    if judge_lm_condition([]):
        jump block_000025C4

    return

label block_00002259:
    # Node: 00002259 (View mode)
    $ set_window("カルタ")
    
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 400
    hide tag_ECFB5B509A334A868686B3435242BF90
    show rs_image_CE6D20694D9B4549B61DEB04A06351CF as tag_063DF7E916A1424E84C7F9FED562D399 at center_top zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    show rs_image_2C8E8B393EE049EE81DAA6E2AF4CD3F6 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_4AFEA28C2CEB4651BB0258C8206CD0EB

    show karuta_title (_("可以看拿到的歌牌哦。")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000224E

    return

label block_0000224E:
    # Node: 0000224E (画像選択)
    $ sys_lm_menu_item = [
        {"pos": (51, 186),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/1.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[0] == True"}],"name": "N1"},
        {"pos": (104, 186),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/2.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[1] == True"}],"name": "N2"},
        {"pos": (157, 186),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/3.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[2] == True"}],"name": "N3"},
        {"pos": (210, 186),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/4.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[3] == True"}],"name": "N4"},
        {"pos": (263, 186),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/5.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[4] == True"}],"name": "N5"},
        {"pos": (316, 186),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/6.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[5] == True"}],"name": "N6"},
        {"pos": (369, 186),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/7.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[6] == True"}],"name": "N7"},
        {"pos": (422, 186),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/8.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[7] == True"}],"name": "N8"},
        {"pos": (475, 186),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/9.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[8] == True"}],"name": "N9"},
        {"pos": (528, 186),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/10.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[9] == True"}],"name": "N10"},
        {"pos": (581, 186),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/11.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[10] == True"}],"name": "N11"},
        {"pos": (634, 186),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/12.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[11] == True"}],"name": "N12"},
        {"pos": (51, 289),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/13.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[12] == True"}],"name": "R13"},
        {"pos": (104, 289),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/14.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[13] == True"}],"name": "R14"},
        {"pos": (157, 289),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/15.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[14] == True"}],"name": "R15"},
        {"pos": (210, 289),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/16.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[15] == True"}],"name": "R16"},
        {"pos": (263, 289),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/17.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[16] == True"}],"name": "R17"},
        {"pos": (316, 289),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/18.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[17] == True"}],"name": "R18"},
        {"pos": (369, 289),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/19.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[18] == True"}],"name": "R19"},
        {"pos": (422, 289),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/20.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[19] == True"}],"name": "R20"},
        {"pos": (475, 289),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/21.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[20] == True"}],"name": "R21"},
        {"pos": (51, 397),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/22.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[21] == True"}],"name": "SR22"},
        {"pos": (104, 397),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/23.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[22] == True"}],"name": "SR23"},
        {"pos": (157, 397),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/24.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[23] == True"}],"name": "SR24"},
        {"pos": (210, 397),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/25.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[24] == True"}],"name": "SR25"},
        {"pos": (263, 397),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/26.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[25] == True"}],"name": "SR26"},
        {"pos": (316, 397),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/27.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[26] == True"}],"name": "SR27"},
        {"pos": (369, 397),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/28.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[27] == True"}],"name": "SR28"},
        {"pos": (422, 397),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/29.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[28] == True"}],"name": "SR29"},
        {"pos": (475, 397),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/30.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[29] == True"}],"name": "SR30"},
        {"pos": (528, 397),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/31.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[30] == True"}],"name": "SR31"},
        {"pos": (581, 397),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/32.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[31] == True"}],"name": "SR32"},
        {"pos": (51, 506),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/33.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[32] == True"}],"name": "SSR33"},
        {"pos": (104, 506),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/34.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[33] == True"}],"name": "SSR34"},
        {"pos": (157, 506),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/35.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[34] == True"}],"name": "SSR35"},
        {"pos": (210, 506),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/36.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[35] == True"}],"name": "SSR36"},
        {"pos": (263, 506),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/37.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[36] == True"}],"name": "SSR37"},
        {"pos": (316, 506),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/38.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[37] == True"}],"name": "SSR38"},
        {"pos": (369, 506),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/39.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[38] == True"}],"name": "SSR39"},
        {"pos": (422, 506),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/40.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[39] == True"}],"name": "SSR40"},
        {"pos": (475, 506),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/41.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[40] == True"}],"name": "SSR41"},
        {"pos": (528, 506),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/42.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[41] == True"}],"name": "SSR42"},
        {"pos": (581, 506),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/43.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[42] == True"}],"name": "SSR43"},
        {"pos": (634, 506),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/PREVIEW/44.png","hover": "","condition":[{"scope":0,"content":"GKarutaStage[43] == True"}],"name": "SSR44"},
        {"pos": (760, 560),"image": "images/Games/Karuta-game-from-Kobayashi/Viewer/Close.png","hover": "","name": "Close"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_731
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Close\"" }]):
        jump block_0000238A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"N1\"" }]):
        jump block_000039D6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"N2\"" }]):
        jump block_000039D7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"N3\"" }]):
        jump block_000039D8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"N4\"" }]):
        jump block_000039D9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"N5\"" }]):
        jump block_000039DA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"N6\"" }]):
        jump block_000039DB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"N7\"" }]):
        jump block_000039DC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"N8\"" }]):
        jump block_000039DD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"N9\"" }]):
        jump block_000039DE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"N10\"" }]):
        jump block_000039DF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"N11\"" }]):
        jump block_000039E0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"N12\"" }]):
        jump block_000039E1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"R13\"" }]):
        jump block_000039E2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"R14\"" }]):
        jump block_000039E3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"R15\"" }]):
        jump block_000039E4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"R16\"" }]):
        jump block_000039E5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"R17\"" }]):
        jump block_000039E6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"R18\"" }]):
        jump block_000039E7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"R19\"" }]):
        jump block_000039E8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"R20\"" }]):
        jump block_000039E9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"R21\"" }]):
        jump block_000039EA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SR22\"" }]):
        jump block_000039EC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SR23\"" }]):
        jump block_000039EB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SR24\"" }]):
        jump block_000039EE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SR25\"" }]):
        jump block_000039ED
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SR26\"" }]):
        jump block_000039F0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SR27\"" }]):
        jump block_000039EF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SR28\"" }]):
        jump block_000039F2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SR29\"" }]):
        jump block_000039F1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SR30\"" }]):
        jump block_000039F5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SR31\"" }]):
        jump block_000039F4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SR32\"" }]):
        jump block_000039F3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SSR33\"" }]):
        jump block_000039F6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SSR34\"" }]):
        jump block_000039F7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SSR35\"" }]):
        jump block_000039F8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SSR36\"" }]):
        jump block_000039F9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SSR37\"" }]):
        jump block_000039FA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SSR38\"" }]):
        jump block_000039FB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SSR39\"" }]):
        jump block_000039FC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SSR40\"" }]):
        jump block_000039FD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SSR41\"" }]):
        jump block_000039FE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SSR42\"" }]):
        jump block_000039FF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SSR43\"" }]):
        jump block_00003A00
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SSR44\"" }]):
        jump block_00003A01

    return

label block_0000238A:
    # Node: 0000238A (CLEAR)
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    hide karuta_title
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_063DF7E916A1424E84C7F9FED562D399
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_7ACA96681ED8438984D635078E9C20A5

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00003975

    return

label block_00003975:
    # Node: 00003975 ()
    $ reverse_volume("music", 1)
    $ del CurrentIndex
    $ del CardList
    $ del FailCount
    $ del CurrentCardNumber
    $ del CardStatus
    $ del WinCount
    $ del LoseCount
    $ del CurrentResult

    return

label block_000039D6:
    # Node: 000039D6 (1)
    
    show karuta_title (_("『{color=#FF0000}滑{/color}子老师是 直的不能再直的 爱妻爱家庭』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_510C7639F6334B35960D486511B3970E as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_00003A02:
    # Node: 00003A02 (RESET)
    pause

    hide tag_F5CAC51F065941419386D50C5611A8A2
    with rs_effect_7ACA96681ED8438984D635078E9C20A5

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    show rs_image_2C8E8B393EE049EE81DAA6E2AF4CD3F6 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show karuta_title (_("可以看拿到的歌牌哦。")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000224E

    return

label block_000039D7:
    # Node: 000039D7 (2)
    
    show karuta_title (_("『{color=#FF0000}半{/color}夜昏暗暗 却从未知少年处 收到了询问』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_F99A0A4DEEC345098D99DCEB3FAC95BF as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039D8:
    # Node: 000039D8 (3)
    
    show karuta_title (_("『{color=#FF0000}坐{/color}立难安时 就一定要这么做 拿起电摩君』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_69DF9B6C5F1C4EC29F79D4AB2F2101B6 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039D9:
    # Node: 000039D9 (4)
    
    show karuta_title (_("『{color=#FF0000}期{/color}待写头条 追寻梦幻与真实 寻找大新闻』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_98D8A1598E8E4F2F993F739F2447DA8C as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039DA:
    # Node: 000039DA (5)
    
    show karuta_title (_("『{color=#FF0000}小{/color}心这么做 一个不好就会被 其他人撞到』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_22E16882E1B040AAAD9E6853112124BC as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039DB:
    # Node: 000039DB (6)
    
    show karuta_title (_("『{color=#FF0000}什{/color}么是道路 无视就好来散步 这就是小翼』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_6559EBEC43804E3AAD5D8F1C2E2A2DC5 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039DC:
    # Node: 000039DC (7)
    
    show karuta_title (_("『{color=#FF0000}想{/color}不想看看 让我也来教教你 这个好姿势』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_C23D0315DD614452AE5FB29E8BADD324 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039DD:
    # Node: 000039DD (8)
    
    show karuta_title (_("『{color=#FF0000}一{/color}之濑翼君 有时突然变病娇 恋爱的烦恼』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_85BFACA926584B89AF51699ED10C88B0 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039DE:
    # Node: 000039DE (9)
    
    show karuta_title (_("『{color=#FF0000}据{/color}传花乃汤 一周里的某一天 非常之热闹』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_B208372FB0764022A2543AD63A5A5646 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039DF:
    # Node: 000039DF (10)
    
    show karuta_title (_("『{color=#FF0000}猫{/color}山两兄弟 如果闻了木天蓼 倒地起不了』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_F00FE54FEBA54097BDAD2E16C937B833 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039E0:
    # Node: 000039E0 (11)
    
    show karuta_title (_("『{color=#FF0000}觉{/color}得是不良 其实只是在装样 反正也不小』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_7E85FBC27D024A4F832E08F24FE93E3C as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039E1:
    # Node: 000039E1 (12)
    
    show karuta_title (_("『{color=#FF0000}做{/color}饭小能手 只要站在厨房里 一做炸一地』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_AA3CA1A3D722488D8604516194418E53 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039E2:
    # Node: 000039E2 (13)
    
    show karuta_title (_("『{color=#FF0000}总{/color}共两根毛 不过今天的表情 变换不安宁』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_1EB995EF565B4025B49DF45569003D0E as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039E3:
    # Node: 000039E3 (14)
    
    show karuta_title (_("『{color=#FF0000}魔{/color}法师夕阳 一直都和触手斗 总是被吃透』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_B95957CE8BE34B008D9696FA6860DAF0 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039E4:
    # Node: 000039E4 (15)
    
    show karuta_title (_("『{color=#FF0000}早{/color}被迷住的 社团训练的经理 今天也亲密』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_F66E2BBD1FA74EB68A43A71F5145D1D9 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039E5:
    # Node: 000039E5 (16)
    
    show karuta_title (_("『{color=#FF0000}就{/color}算是英雄 男人都受不了的 快乐也没跑』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_2CCCCA5593894D2E966BFDF6FBE77C2F as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039E6:
    # Node: 000039E6 (17)
    
    show karuta_title (_("『{color=#FF0000}动{/color}不动斗嘴 一边疑似是不良 一边优等生』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_D47940680F4F48C489A61CE734DAFC84 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039E7:
    # Node: 000039E7 (18)
    
    show karuta_title (_("『{color=#FF0000}加{/color}藤酱的话 喜欢的人的年龄 或许非常高』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_119DB3B158614410A4B5031B4B213EE9 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039E8:
    # Node: 000039E8 (19)
    
    show karuta_title (_("『{color=#FF0000}居{/color}然要迟到 快快叫九尾帮忙 瞬间到学校』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_664763C2113A4A1FA975AE23585159A6 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039E9:
    # Node: 000039E9 (20)
    
    show karuta_title (_("『{color=#FF0000}于{/color}远处等待 只要他一直幸福 那便都安好』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_B83FB3A2DAE54623ACB7A190F5F5DCCE as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039EA:
    # Node: 000039EA (21)
    
    show karuta_title (_("『{color=#FF0000}铁{/color}拳的制裁 其实深层理由是 仅仅为朋友』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_71135BB99DBA4BFF88AA761F6D0B252C as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039EC:
    # Node: 000039EC (22)
    
    show karuta_title (_("『{color=#FF0000}所{/color}谓的变态 稍微给尝点甜头 马上服帖帖』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_5CD06E0770554450AE7FCBEA7EE146CD as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039EB:
    # Node: 000039EB (23)
    
    show karuta_title (_("『{color=#FF0000}逐{/color}渐变温暖 正因为如此感觉 一把揽入怀』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_39ABDFA4D054484FBF899ACAE5270C51 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039EE:
    # Node: 000039EE (24)
    
    show karuta_title (_("『{color=#FF0000}学{/color}校音乐室 放学后只想和你 两个人一起』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_E54334F908C54BA1AF6215D648A9D736 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039ED:
    # Node: 000039ED (25)
    
    show karuta_title (_("『{color=#FF0000}看{/color}似是糖球 吃下去就能抵达 梦想的世界』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_4AA57FE7935F486BB1CDEEF7CF800B3A as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039F0:
    # Node: 000039F0 (26)
    
    show karuta_title (_("『{color=#FF0000}痛{/color}苦不安时 陪在身边的就是 最好的朋友』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_762E7E2922D5484F9B8AE853F7FFAD0D as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039EF:
    # Node: 000039EF (27)
    
    show karuta_title (_("『{color=#FF0000}憧{/color}憬着前辈 看向前辈的目光 星星般闪耀』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_1280D1DFC62D4E148664A4EA6981A547 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039F2:
    # Node: 000039F2 (28)
    
    show karuta_title (_("『{color=#FF0000}只{/color}有这个呐 观察少年的日常 可停不下来』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_DF7C8FE6364746B48B087C7C3C25D99C as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039F1:
    # Node: 000039F1 (29)
    
    show karuta_title (_("『{color=#FF0000}本{/color}来是敌人 何时才能得实现 这股恋爱心』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_B79ACB89380B4BE2B3C585632CA8A6AD as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039F5:
    # Node: 000039F5 (30)
    
    show karuta_title (_("『{color=#FF0000}机{/color}智如佐藤 煽动前辈的好手 结果真有效』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_444C06F48EE044AAB53BD868E969A1E7 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039F4:
    # Node: 000039F4 (31)
    
    show karuta_title (_("『{color=#FF0000}得{/color}道终成仙 超越一切快感的 大贤者大人』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_2467C9FE8E36401C8FB34C78BF0E87EE as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039F3:
    # Node: 000039F3 (32)
    
    show karuta_title (_("『{color=#FF0000}又{/color}要拌嘴了 传达一切想法的 超发球攻击』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_EA1EB2050489467E956E2A08D95A8686 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039F6:
    # Node: 000039F6 (33)
    
    show karuta_title (_("『{color=#FF0000}按{/color}摩又按摩 不过特别菜单是 某个人独享』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_C6619EA574B446F38DF56BA875952B54 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039F7:
    # Node: 000039F7 (34)
    
    show karuta_title (_("『{color=#FF0000}可{/color}爱小熊猫 作者两人都说了 大家要去看』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_63647F60C90F4CD89174E5AE43954714 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039F8:
    # Node: 000039F8 (35)
    
    show karuta_title (_("『{color=#FF0000}自{/color}从那天起 学院生活成为了 仅有的一切』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_FF7B494373C846D1B2C2E4931DE42B9B as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039F9:
    # Node: 000039F9 (36)
    
    show karuta_title (_("『{color=#FF0000}背{/color}着双肩包 还被画到漫画里 工口意义上』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_3F01F44D46844E96B5D46D1EC9ACC59B as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039FA:
    # Node: 000039FA (37)
    
    show karuta_title (_("『{color=#FF0000}九{/color}尾大人啊 为何喜欢类型是 肌肉型的啊』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_7D3C107802E7496695FF888CE6B56C9F as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039FB:
    # Node: 000039FB (38)
    
    show karuta_title (_("『{color=#FF0000}变{/color}成露出狂 即便如此也要做 上啊野球拳』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_28CCFD0CD7FD42AAA8E8CDB961B094B0 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039FC:
    # Node: 000039FC (39)
    
    show karuta_title (_("『{color=#FF0000}黑{/color}色比基尼 魅惑人心小三角 俗称V型线』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_517466B8F3D34D369B9381E3FB6B2557 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039FD:
    # Node: 000039FD (40)
    
    show karuta_title (_("『{color=#FF0000}不{/color}分攻和受 不用多说交出来 全交给慎酱』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_F05AB6BB97E045DB835B16E295850479 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039FE:
    # Node: 000039FE (41)
    
    show karuta_title (_("『{color=#FF0000}传{/color}统兜裆布 身体心灵都看来 威风加帅气』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_5CBE9D5D84B548EE9EED84FD559C2A19 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000039FF:
    # Node: 000039FF (42)
    
    show karuta_title (_("『{color=#FF0000}大{/color}量下流梗 如同潮水一般来 最后却停了』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_2291F9210EA24B0E92EE39C32F25C2A0 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_00003A00:
    # Node: 00003A00 (43)
    
    show karuta_title (_("『{color=#FF0000}喝{/color}酒到天亮 本来喝酒这件事 仅大人才好』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_610DDA7D479F4F158A055FF6A5FF60A0 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_00003A01:
    # Node: 00003A01 (44)
    
    show karuta_title (_("『{color=#FF0000}那{/color}个组织的 威风凛凛美男子 原来是兄弟』{nw}")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01
    show rs_image_989A2137014649A1B159FDDDA8F1DDFD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F5CAC51F065941419386D50C5611A8A2 = 500
    show rs_image_2D63738EF28A4EEA8C61ABC3F12BA1A0 as tag_F5CAC51F065941419386D50C5611A8A2 at Transform(xpos=246, ypos=174) zorder zorder_tag_F5CAC51F065941419386D50C5611A8A2 onlayer master
    with rs_effect_7ACA96681ED8438984D635078E9C20A5


    if judge_lm_condition([]):
        jump block_00003A02

    return

label block_000025C4:
    # Node: 000025C4 (Prepare)
    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_84D7210FBBF34E428243573CCC75C981

    pause 1.5

    $ set_window("カルタ")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AB0B595EA9E74A18A91A6B63BE09E780 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 500
    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 500
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 500
    show rs_image_2D66580B8E7D43CD9D46BD73F15B291B as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3F0E353CFDB748D89954EDA3CA501941 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_0013370D932E48D7BA71F9ABB90D97FE as tag_063DF7E916A1424E84C7F9FED562D399 at center_top zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    pause 0.7

    show karuta_title (_("准备开始读牌了。")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    show karuta_title (_("根据我的话的第一个字选牌，多者即赢。")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    show karuta_title (_("那么，准备……")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    if judge_lm_condition([]):
        jump block_00003998

    return

label block_00003998:
    # Node: 00003998 (SetCard)
    $ renpy.show("images/Games/Karuta-game-from-Kobayashi/Number/0.png", at_list=[Transform(xpos=24, ypos=235)], what=renpy.easy.displayable("images/Games/Karuta-game-from-Kobayashi/Number/0.png"), tag="WinNumber", zorder=200)
    $ renpy.show("images/Games/Karuta-game-from-Kobayashi/Number/0.png", at_list=[Transform(xpos=696, ypos=235)], what=renpy.easy.displayable("images/Games/Karuta-game-from-Kobayashi/Number/0.png"), tag="LoseNumber", zorder=200)
    $ CardList = [0] * 12
    $ CardStatus = [True] * 12
    $ TargetCardIndex = 0
    $ RandomLimit = 44
    if (Chapter == 2) and (C2SG1 == False):
        $ RandomLimit = 12
    elif ((Chapter == 2) and (C2SG1 == True)) or ((Chapter > 2) and (C3SG1 == False)):
        $ RandomLimit = 21
    elif  (Chapter > 2) and (C3SG1 == True) and (C3SG2 == False):
        $ RandomLimit = 32
    $ CardExisted = False
    $ _i = 0
    $ _j = 0
    while _i < 12:
        $ CardExisted = True
        while CardExisted == True:
            $ TargetCardIndex = Random(RandomLimit) + 1
            $ CardExisted = False
            $ _j = 0
            $ sys_while_condition_977AD97C39B24D6BB4F4B7F4614AD944 = True
            label sys_while_label_977AD97C39B24D6BB4F4B7F4614AD944:
            while _j < _i and sys_while_condition_977AD97C39B24D6BB4F4B7F4614AD944 == True:
                if CardList[_j] == TargetCardIndex:
                    $ CardExisted = True
                    $ sys_while_condition_977AD97C39B24D6BB4F4B7F4614AD944 = False
                    jump sys_while_label_977AD97C39B24D6BB4F4B7F4614AD944
                $ _j = _j + 1
        $ del sys_while_condition_977AD97C39B24D6BB4F4B7F4614AD944
        $ CardList[_i] = TargetCardIndex
        $ _i += 1
    $ del _j
    $ del CardExisted
    $ del TargetCardIndex
    $ del RandomLimit
    $ CardX = 170
    $ CardY = 151
    $ _i = 0
    while _i < 12:
        $ renpy.show("images/Games/Karuta-game-from-Kobayashi/Thumbnail/" |str_combine| CardList[_i] |str_combine| ".png", at_list=[Transform(xpos=CardX, ypos=CardY)], what=renpy.easy.displayable("images/Games/Karuta-game-from-Kobayashi/Thumbnail/" |str_combine| CardList[_i] |str_combine| ".png"), tag="Card" |str_combine| _i, zorder=100)
        $ CardX = CardX + 119
        if (_i == 3) or (_i == 7):
            $ CardX = 170
            $ CardY = CardY + 149
        $ _i = _i + 1
    $ del _i
    $ del CardX
    $ del CardY

    if judge_lm_condition([]):
        jump block_00003999

    return

label block_00003999:
    # Node: 00003999 (Start)
    if sys_music2_current_file != "sound/BGM/Drum.ogg":
        play music2 "sound/BGM/Drum.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Drum.ogg"

    show karuta_title (_("开始！")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    if judge_lm_condition([]):
        jump block_0000399A

    return

label block_0000399A:
    # Node: 0000399A (Update)

    if CurrentCardNumber > 0:
        $ CoverX = 0
        $ CoverY = 0
        if CurrentIndex < 4:
            $ CoverY = 151
        elif CurrentIndex < 8:
            $ CoverY = 300
        else:
            $ CoverY = 449
        if (CurrentIndex == 0) or (CurrentIndex == 4) or (CurrentIndex == 8):
            $ CoverX = 170
        elif (CurrentIndex == 1) or (CurrentIndex == 5) or (CurrentIndex == 9):
            $ CoverX = 289
        elif (CurrentIndex == 2) or (CurrentIndex == 6) or (CurrentIndex == 10):
            $ CoverX = 408
        else:
            $ CoverX = 527
        $ renpy.show("images/Games/Karuta-game-from-Kobayashi/Cover.png", at_list=[Transform(xpos=CoverX, ypos=CoverY)], what=renpy.easy.displayable("images/Games/Karuta-game-from-Kobayashi/Cover.png"), tag="Cover" |str_combine| CurrentIndex, zorder=200)
        $ renpy.hide("WinNumber")
        $ renpy.hide("LoseNumber")
        $ renpy.show("images/Games/Karuta-game-from-Kobayashi/Number/" |str_combine| WinCount |str_combine| ".png", at_list=[Transform(xpos=24, ypos=235)], what=renpy.easy.displayable("images/Games/Karuta-game-from-Kobayashi/Number/" |str_combine| WinCount |str_combine| ".png"), tag="WinNumber", zorder=200)
        $ renpy.show("images/Games/Karuta-game-from-Kobayashi/Number/" |str_combine| LoseCount |str_combine| ".png", at_list=[Transform(xpos=696, ypos=235)], what=renpy.easy.displayable("images/Games/Karuta-game-from-Kobayashi/Number/" |str_combine| LoseCount |str_combine| ".png"), tag="LoseNumber", zorder=200)
        $ del CoverX
        $ del CoverY
    if FailCount == 3:
        $ CurrentCardNumber = 45
    elif (WinCount + FailCount + LoseCount) < 12:
        $ sys_while_condition_844C28430F63439C82123251A77198BB = True
        label sys_while_label_844C28430F63439C82123251A77198BB:
        while True and sys_while_condition_844C28430F63439C82123251A77198BB == True:
            $ CurrentIndex = Random(12)
            if CardStatus[CurrentIndex] == True:
                $ sys_while_condition_844C28430F63439C82123251A77198BB = False
                jump sys_while_label_844C28430F63439C82123251A77198BB
        $ del sys_while_condition_844C28430F63439C82123251A77198BB
        $ CurrentCardNumber = CardList[CurrentIndex]
        $ CardStatus[CurrentIndex] = False
    else:
        $ CurrentCardNumber = 45
    
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 1" }]):
        jump block_000039A0
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 2" }]):
        jump block_000039A1
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 3" }]):
        jump block_000039A2
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 4" }]):
        jump block_000039A3
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 5" }]):
        jump block_000039A4
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 6" }]):
        jump block_000039A5
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 7" }]):
        jump block_000039A6
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 8" }]):
        jump block_000039A7
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 9" }]):
        jump block_000039A8
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 10" }]):
        jump block_000039A9
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 11" }]):
        jump block_000039AA
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 12" }]):
        jump block_000039AB
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 13" }]):
        jump block_000039AC
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 14" }]):
        jump block_000039AD
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 15" }]):
        jump block_000039AE
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 16" }]):
        jump block_000039AF
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 17" }]):
        jump block_000039B0
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 18" }]):
        jump block_000039B1
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 19" }]):
        jump block_000039B2
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 20" }]):
        jump block_000039B3
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 21" }]):
        jump block_000039B4
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 22" }]):
        jump block_000039BF
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 23" }]):
        jump block_000039BE
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 24" }]):
        jump block_000039BD
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 25" }]):
        jump block_000039BC
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 26" }]):
        jump block_000039BB
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 27" }]):
        jump block_000039BA
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 28" }]):
        jump block_000039B9
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 29" }]):
        jump block_000039B8
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 30" }]):
        jump block_000039B7
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 31" }]):
        jump block_000039B6
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 32" }]):
        jump block_000039B5
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 33" }]):
        jump block_000039C0
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 34" }]):
        jump block_000039C1
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 35" }]):
        jump block_000039C2
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 36" }]):
        jump block_000039C3
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 37" }]):
        jump block_000039C4
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 38" }]):
        jump block_000039C5
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 39" }]):
        jump block_000039C6
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 40" }]):
        jump block_000039C7
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 41" }]):
        jump block_000039C8
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 42" }]):
        jump block_000039C9
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 43" }]):
        jump block_000039CA
    if judge_lm_condition([{ "scope": 0, "content": "CurrentCardNumber == 44" }]):
        jump block_000039CB
    if judge_lm_condition([]):
        jump block_000039CE

    return

label block_0000399C:
    # Node: 0000399C (Selector)
    pause 0.1
    call lm_menu([
        {"image":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","hover":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","name":"01","pos":(170,151)},
        {"image":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","hover":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","name":"02","pos":(289,151)},
        {"image":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","hover":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","name":"03","pos":(408,151)},
        {"image":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","hover":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","name":"04","pos":(527,151)},
        {"image":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","hover":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","name":"05","pos":(170,300)},
        {"image":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","hover":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","name":"06","pos":(289,300)},
        {"image":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","hover":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","name":"07","pos":(408,300)},
        {"image":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","hover":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","name":"08","pos":(527,300)},
        {"image":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","hover":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","name":"09","pos":(170,499)},
        {"image":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","hover":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","name":"10","pos":(289,499)},
        {"image":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","hover":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","name":"11","pos":(408,499)},
        {"image":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","hover":"rs_image_345982F54C7E4D819B8EFD9BB1463E34","name":"12","pos":(527,499)},
    ], {}, (Random(1501) + 500) / float(1000)) from _call_lm_menu_732
    if _lm_selected_value == "":
        $ LoseCount = LoseCount + 1
        $ CurrentResult = 0
    elif CardList[_lm_selected_index] == CurrentCardNumber:
        $ GKarutaStage[CurrentCardNumber - 1] = True
        $ WinCount = WinCount + 1
        $ CurrentResult = 1
    else:
        $ FailCount = FailCount + 1
        $ CurrentResult = 2

    pause 0.1

    if judge_lm_condition([{ "scope": 0, "content": "CurrentResult == 0" }]):
        jump block_000039D2
    if judge_lm_condition([{ "scope": 0, "content": "CurrentResult == 1" }]):
        jump block_000039D4
    if judge_lm_condition([{ "scope": 0, "content": "CurrentResult == 2" }]):
        jump block_0000399E

    return

label block_000039D2:
    # Node: 000039D2 (Timeover)
    if sys_effect2_current_file != "sound/Effect Sound/Eye shine 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Eye shine 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Eye shine 1.ogg"

    $ zorder_tag_AC2A781923074987B89EFF82C1C606E7 = 500
    show rs_image_A91E74B6874A4367AFACA7A60A9659EC as tag_AC2A781923074987B89EFF82C1C606E7 zorder zorder_tag_AC2A781923074987B89EFF82C1C606E7 onlayer master
    show rs_image_CB9A3B7C3FB14F81B2F472B12826B614 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0013370D932E48D7BA71F9ABB90D97FE as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    show rs_image_3F0E353CFDB748D89954EDA3CA501941 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    show karuta_title (_("漂亮！")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ renpy.pause(2, hard=True)

    if judge_lm_condition([]):
        jump block_000039CD

    return

label block_000039CD:
    # Node: 000039CD (TO: RESET)

    if judge_lm_condition([]):
        jump block_000039CC

    return

label block_000039CC:
    # Node: 000039CC (TO: RESET)

    if judge_lm_condition([]):
        jump block_0000399B

    return

label block_0000399B:
    # Node: 0000399B (RESET)
    if sys_effect3_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_2D66580B8E7D43CD9D46BD73F15B291B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3F0E353CFDB748D89954EDA3CA501941 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    show rs_image_0013370D932E48D7BA71F9ABB90D97FE as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    hide tag_AC2A781923074987B89EFF82C1C606E7
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    
    if judge_lm_condition([]):
        jump block_0000399A

    return

label block_000039D4:
    # Node: 000039D4 (Correct)
    if sys_effect2_current_file != "sound/Effect Sound/Eye shine 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Eye shine 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Eye shine 1.ogg"

    $ zorder_tag_AC2A781923074987B89EFF82C1C606E7 = 500
    show rs_image_3C7EEE2FD7C44450926F5BF4222D3790 as tag_AC2A781923074987B89EFF82C1C606E7 zorder zorder_tag_AC2A781923074987B89EFF82C1C606E7 onlayer master
    show rs_image_2D66580B8E7D43CD9D46BD73F15B291B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_0013370D932E48D7BA71F9ABB90D97FE as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    show rs_image_27A9CE608540480586E95E611EE27408 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    show karuta_title (_("哦！")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ renpy.pause(2, hard=True)

    if judge_lm_condition([]):
        jump block_000039CD

    return

label block_0000399E:
    # Node: 0000399E (Wrong)
    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_AC2A781923074987B89EFF82C1C606E7 = 500
    show rs_image_601DB506811341439D5AD034B152D4B1 as tag_AC2A781923074987B89EFF82C1C606E7 zorder zorder_tag_AC2A781923074987B89EFF82C1C606E7 onlayer master
    show rs_image_CB9A3B7C3FB14F81B2F472B12826B614 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_01044D5E34704EB59BE69F0E074703D2 as tag_063DF7E916A1424E84C7F9FED562D399 zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    show rs_image_345982F54C7E4D819B8EFD9BB1463E34 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    show karuta_title (_("只有三次选错机会哦。")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ renpy.pause(2, hard=True)

    if judge_lm_condition([]):
        jump block_000039CD

    return

label block_000039A0:
    # Node: 000039A0 (1)
    
    show karuta_title (_("『{color=#FF0000}滑{/color}子老师是 直的不能再直的 爱妻爱家庭』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039A1:
    # Node: 000039A1 (2)
    
    show karuta_title (_("『{color=#FF0000}半{/color}夜昏暗暗 却从未知少年处 收到了询问』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039A2:
    # Node: 000039A2 (3)
    
    show karuta_title (_("『{color=#FF0000}坐{/color}立难安时 就一定要这么做 拿起电摩君』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039A3:
    # Node: 000039A3 (4)
    
    show karuta_title (_("『{color=#FF0000}期{/color}待写头条 追寻梦幻与真实 寻找大新闻』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039A4:
    # Node: 000039A4 (5)
    
    show karuta_title (_("『{color=#FF0000}小{/color}心这么做 一个不好就会被 其他人撞到』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039A5:
    # Node: 000039A5 (6)
    
    show karuta_title (_("『{color=#FF0000}什{/color}么是道路 无视就好来散步 这就是小翼』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039A6:
    # Node: 000039A6 (7)
    
    show karuta_title (_("『{color=#FF0000}想{/color}不想看看 让我也来教教你 这个好姿势』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039A7:
    # Node: 000039A7 (8)
    
    show karuta_title (_("『{color=#FF0000}一{/color}之濑翼君 有时突然变病娇 恋爱的烦恼』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039A8:
    # Node: 000039A8 (9)
    
    show karuta_title (_("『{color=#FF0000}据{/color}传花乃汤 一周里的某一天 非常之热闹』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039A9:
    # Node: 000039A9 (10)
    
    show karuta_title (_("『{color=#FF0000}猫{/color}山两兄弟 如果闻了木天蓼 倒地起不了』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039AA:
    # Node: 000039AA (11)
    
    show karuta_title (_("『{color=#FF0000}觉{/color}得是不良 其实只是在装样 反正也不小』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039AB:
    # Node: 000039AB (12)
    
    show karuta_title (_("『{color=#FF0000}做{/color}饭小能手 只要站在厨房里 一做炸一地』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039AC:
    # Node: 000039AC (13)
    
    show karuta_title (_("『{color=#FF0000}总{/color}共两根毛 不过今天的表情 变换不安宁』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039AD:
    # Node: 000039AD (14)
    
    show karuta_title (_("『{color=#FF0000}魔{/color}法师夕阳 一直都和触手斗 总是被吃透』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039AE:
    # Node: 000039AE (15)
    
    show karuta_title (_("『{color=#FF0000}早{/color}被迷住的 社团训练的经理 今天也亲密』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039AF:
    # Node: 000039AF (16)
    
    show karuta_title (_("『{color=#FF0000}就{/color}算是英雄 男人都受不了的 快乐也没跑』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039B0:
    # Node: 000039B0 (17)
    
    show karuta_title (_("『{color=#FF0000}动{/color}不动斗嘴 一边疑似是不良 一边优等生』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039B1:
    # Node: 000039B1 (18)
    
    show karuta_title (_("『{color=#FF0000}加{/color}藤酱的话 喜欢的人的年龄 或许非常高』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039B2:
    # Node: 000039B2 (19)
    
    show karuta_title (_("『{color=#FF0000}居{/color}然要迟到 快快叫九尾帮忙 瞬间到学校』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039B3:
    # Node: 000039B3 (20)
    
    show karuta_title (_("『{color=#FF0000}于{/color}远处等待 只要他一直幸福 那便都安好』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039B4:
    # Node: 000039B4 (21)
    
    show karuta_title (_("『{color=#FF0000}铁{/color}拳的制裁 其实深层理由是 仅仅为朋友』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039BF:
    # Node: 000039BF (22)
    
    show karuta_title (_("『{color=#FF0000}所{/color}谓的变态 稍微给尝点甜头 马上服帖帖』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039BE:
    # Node: 000039BE (23)
    
    show karuta_title (_("『{color=#FF0000}逐{/color}渐变温暖 正因为如此感觉 一把揽入怀』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039BD:
    # Node: 000039BD (24)
    
    show karuta_title (_("『{color=#FF0000}学{/color}校音乐室 放学后只想和你 两个人一起』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039BC:
    # Node: 000039BC (25)
    
    show karuta_title (_("『{color=#FF0000}看{/color}似是糖球 吃下去就能抵达 梦想的世界』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039BB:
    # Node: 000039BB (26)
    
    show karuta_title (_("『{color=#FF0000}痛{/color}苦不安时 陪在身边的就是 最好的朋友』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039BA:
    # Node: 000039BA (27)
    
    show karuta_title (_("『{color=#FF0000}憧{/color}憬着前辈 看向前辈的目光 星星般闪耀』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039B9:
    # Node: 000039B9 (28)
    
    show karuta_title (_("『{color=#FF0000}只{/color}有这个呐 观察少年的日常 可停不下来』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039B8:
    # Node: 000039B8 (29)
    
    show karuta_title (_("『{color=#FF0000}本{/color}来是敌人 何时才能得实现 这股恋爱心』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039B7:
    # Node: 000039B7 (30)
    
    show karuta_title (_("『{color=#FF0000}机{/color}智如佐藤 煽动前辈的好手 结果真有效』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039B6:
    # Node: 000039B6 (31)
    
    show karuta_title (_("『{color=#FF0000}得{/color}道终成仙 超越一切快感的 大贤者大人』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039B5:
    # Node: 000039B5 (32)
    
    show karuta_title (_("『{color=#FF0000}又{/color}要拌嘴了 传达一切想法的 超发球攻击』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039C0:
    # Node: 000039C0 (33)
    
    show karuta_title (_("『{color=#FF0000}按{/color}摩又按摩 不过特别菜单是 某个人独享』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039C1:
    # Node: 000039C1 (34)
    
    show karuta_title (_("『{color=#FF0000}可{/color}爱小熊猫 作者两人都说了 大家要去看』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039C2:
    # Node: 000039C2 (35)
    
    show karuta_title (_("『{color=#FF0000}自{/color}从那天起 学院生活成为了 仅有的一切』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039C3:
    # Node: 000039C3 (36)
    
    show karuta_title (_("『{color=#FF0000}背{/color}着双肩包 还被画到漫画里 工口意义上』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039C4:
    # Node: 000039C4 (37)
    
    show karuta_title (_("『{color=#FF0000}九{/color}尾大人啊 为何喜欢类型是 肌肉型的啊』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039C5:
    # Node: 000039C5 (38)
    
    show karuta_title (_("『{color=#FF0000}变{/color}成露出狂 即便如此也要做 上啊野球拳』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039C6:
    # Node: 000039C6 (39)
    
    show karuta_title (_("『{color=#FF0000}黑{/color}色比基尼 魅惑人心小三角 俗称V型线』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039C7:
    # Node: 000039C7 (40)
    
    show karuta_title (_("『{color=#FF0000}不{/color}分攻和受 不用多说交出来 全交给慎酱』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039C8:
    # Node: 000039C8 (41)
    
    show karuta_title (_("『{color=#FF0000}传{/color}统兜裆布 身体心灵都看来 威风加帅气』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039C9:
    # Node: 000039C9 (42)
    
    show karuta_title (_("『{color=#FF0000}大{/color}量下流梗 如同潮水一般来 最后却停了』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039CA:
    # Node: 000039CA (43)
    
    show karuta_title (_("『{color=#FF0000}喝{/color}酒到天亮 本来喝酒这件事 仅大人才好』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039CB:
    # Node: 000039CB (44)
    
    show karuta_title (_("『{color=#FF0000}那{/color}个组织的 威风凛凛美男子 原来是兄弟』")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_0000399C

    return

label block_000039CE:
    # Node: 000039CE (CLEAR)
    show karuta_title (_("到此为止！")) as karuta_title at Transform(xpos=40,ypos=19) zorder 1000 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide WinNumber
    hide LoseNumber
    hide Card0
    hide Card1
    hide Card2
    hide Card3
    hide Card4
    hide Card5
    hide Card6
    hide Card7
    hide Card8
    hide Card9
    hide Card10
    hide Card11
    hide Cover0
    hide Cover1
    hide Cover2
    hide Cover3
    hide Cover4
    hide Cover5
    hide Cover6
    hide Cover7
    hide Cover8
    hide Cover9
    hide Cover10
    hide Cover11
    with rs_effect_EF2A46F3AC1640F184034E18DCB12407

    if sys_effect_current_file != "sound/Effect Sound/Yoo 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Yoo 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Yoo 1.ogg"

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide karuta_title
    hide tag_063DF7E916A1424E84C7F9FED562D399
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_EF2A46F3AC1640F184034E18DCB12407

    pause 2

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_000039CF

    return

label block_000039CF:
    # Node: 000039CF ()
    $ reverse_volume("music", 1)
    $ del CurrentIndex
    $ del CardList
    $ del FailCount
    $ del CurrentCardNumber
    $ del CardStatus
    $ del WinCount
    $ del LoseCount
    $ del CurrentResult

    return

