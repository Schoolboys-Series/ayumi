# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003984 (CHAPTER 1)

label block_00003985:
    # Node: 00003985 ()
    $ TalkNoriF5 = False
    $ TalkBookstoreF5 = False
    $ TalkTsubasaF1After = False
    $ TalkTsukiSoraF1After = False
    $ TalkItouKimuraF1After = False
    $ TalkShintaroF3After = False
    $ TalkTsubasaF4After = False
    $ TalkShinobuF5After = False
    $ TalkKimuraQKimuraConferenceAfter = False
    $ TalkTsubasaQTsubasaAfter = False
    $ TalkKimura = 0
    $ TalkItou = 0
    $ TalkKatou = 0
    $ TalkTsubasa = 0
    $ TalkMatsuta = 0
    $ TalkIzumi = 0
    $ TalkSatou = 0
    $ TalkSakuya = 0
    $ TalkSora = 0
    $ TalkShintaro = 0
    $ TalkShinobu = 0
    $ TalkOkajima = 0
    $ QKimuraCheck1 = False
    $ QSabushinCheck1 = False
    $ QTsubasaCheck1 = False
    $ F5Check1 = False
    $ C1S1Phase = 0
    $ C1S2Phase = 0
    $ C1S3Phase = 0
    $ C1S4Phase = 0
    $ C1S5Phase = 0
    $ C1QNewsclubPhase = 0
    $ C1QSabushinPhase = 0
    $ C1QTsubasaPhase = 0
    $ C1QMatsutaPhase = 0

    if judge_lm_condition([]):
        jump block_00003992

    return

label block_00003992:
    # Node: 00003992 (Chapter: 1)
    $ Chapter = 1

    if judge_lm_condition([]):
        jump block_00003986

    return

label block_00003986:
    # Node: 00003986 (Opening Celemony)
    call block_00000129 from _call_block_00000129

    if judge_lm_condition([]):
        jump block_00003987

    return

label block_00003987:
    # Node: 00003987 (Daytime)
    call block_000001B1 from _call_block_000001B1

    if judge_lm_condition([{ "scope": 0, "content": "SYSReviewMode == True" }]):
        jump block_00003FBB
    if judge_lm_condition([]):
        jump block_00003994

    return

label block_00003FBB:
    # Node: 00003FBB (Data passby)
    $ E_TAG_TalkOkajimaInitNumber = Max(TalkOkajima, E_TAG_TalkOkajimaInitNumber)

    if judge_lm_condition([]):
        jump block_00003CB7

    return

label block_00003CB7:
    # Node: 00003CB7 ()
    $ del TalkNoriF5
    $ del TalkBookstoreF5
    $ del TalkTsubasaF1After
    $ del TalkTsukiSoraF1After
    $ del TalkItouKimuraF1After
    $ del TalkShintaroF3After
    $ del TalkTsubasaF4After
    $ del TalkShinobuF5After
    $ del TalkKimuraQKimuraConferenceAfter
    $ del TalkTsubasaQTsubasaAfter
    $ del TalkKimura
    $ del TalkItou
    $ del TalkKatou
    $ del TalkTsubasa
    $ del TalkMatsuta
    $ del TalkIzumi
    $ del TalkSatou
    $ del TalkSakuya
    $ del TalkSora
    $ del TalkShintaro
    $ del TalkShinobu
    $ del TalkOkajima
    $ del QKimuraCheck1
    $ del QSabushinCheck1
    $ del QTsubasaCheck1
    $ del F5Check1
    $ del C1S1Phase
    $ del C1S2Phase
    $ del C1S3Phase
    $ del C1S4Phase
    $ del C1S5Phase
    $ del C1QNewsclubPhase
    $ del C1QSabushinPhase
    $ del C1QTsubasaPhase
    $ del C1QMatsutaPhase

    return

label block_00003994:
    # Node: 00003994 (體育祭)
    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 200
    show rs_image_D7F70E4230154502BB28D6BA8AC09D91 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_bottom zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "老师，我来了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（紧张不安……不知道这次会被骂什么。）"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8F48584787114538888D5C0B826EDE5F as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "嗯，辛苦了。\n"
    show rs_image_1557B4E76EEC4D0E8F827C8C42924E5F as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "其实，关于马上就到的{color=#FF8000}体育祭{/color}\n有些事情必须要和你商量。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，是这么回事啊！\n嗯！必须要开始准备了呐！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7B5A8FFA4600478D826C2E4E4FAD069E as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "正是如此。\n这次本来应该是先召集所有班长开会分组的……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_9C78AB751CDB49FDA83251FA5B4A3825 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "总之去和二班一组。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？嗯？"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7B5A8FFA4600478D826C2E4E4FAD069E as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "“上次败给了三四班呢……这次可一定要一雪前耻。”\n去和二班的海老师这么说！"

    show rs_image_D7F70E4230154502BB28D6BA8AC09D91 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "事已至此我们绝不会与三四班合作。\n所以，交给你了，森海。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就、就算说交给我……\n分组本来就是看运气的啊。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Onboard 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Onboard 1.ogg"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4E68A2DC06DC4980B15518EDB26D1FCD as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "精神决定物质！！总之给我做好。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好、好的……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（滑子老师意外的好单纯呐。\n我个人倒是输赢无所谓，反正也不擅长运动——）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8F48584787114538888D5C0B826EDE5F as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "赢了的话我请大家喝果汁。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "！？\n太好了——！我会加油的——！！"

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
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 1.5

    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 1

    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_3F2B220CD95B4BC6AAD59B3FE6C7DF0B as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8F070BDCB04D4336AC7465096F0E3084 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.5

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "综上，今天的总结会结束了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "大家再见！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}明天见。{/size}"

    pause 0.25

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 200
    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "班长和体育委员记得去四班教室开体育祭的分组会。"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DFF43C28E0D9414492DE4927927BBDBF as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_907B8C088A814A069D35867C58E3A86C "明白。"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 200
    show rs_image_87A4A951CCF94134BEC8CCB7D574B6E1 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "森海，别忘了。"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜，压力好大……"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_52907CFE4828483C99DC76C46D873DD0 as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "？"

    window hide

    pause 0.4

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    if sys_music2_current_file != "sound/Effect Sound/Open window 1.ogg":
        play music2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C7B1077A391E4C9D9DCED82A454EBA1B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_DFF43C28E0D9414492DE4927927BBDBF as tag_61A891D6A6D047DC93695DA12E13CC75 at left_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_80AC1FBCF08D4C6283030181039745BE as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.4

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "神佛保佑……。"

    show rs_image_173B284E6DC843AF812C237128860894 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "太大惊小怪了。分到什么不都一样么。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "才不好——这里已经被卷进老师们的阴谋里了！"

    show rs_image_FCAFA927EAA1420E8D01012A37344D27 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "啊？"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_225A15956FFB4AC2B4A3ACD0192F135D as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=460, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "你、你好，友君。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_D2BB5C80C5EC436C81AD2A89675FF109 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦哦——翼啾——！\n"
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_DB50197E13884F45AFBB23A957B18CA1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    extend "翼君也来祈祷！祈祷我们能分到同一组！"

    show rs_image_DEB70960E8944B33903B14177D8DC211 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸！啊、嗯！当、当然！{w=0.55}{nw}"
    show rs_image_17557F1248C548988DBCF710ECE91AC3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "(^o^)。"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_0101B4A16FA94D81BACA3AB5A5E27790 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……呼。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    pause 0.3

    rs_character_6841442962184324BB3E7182C533A97B "那么请从一班开始按顺序上来抽签。"

    window hide

    pause 0.6

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_1C3AC3BC102640A98B0B848A29849370

    pause 2.5

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Dont be afraid!! (Instrument).ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Dont be afraid!! (Instrument).ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Dont be afraid!! (Instrument).ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 1

    show rs_image_8F070BDCB04D4336AC7465096F0E3084 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    if sys_music2_current_file != "sound/Effect Sound/Clamorous 1.ogg":
        play music2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    pause 0.5

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_EAF549F11EDE4A5AA68FCD7AECAB1DEF as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_D2BB5C80C5EC436C81AD2A89675FF109 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好——了！肃静——！大家肃静——！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_11E9CB4CF92548E88CF101664A977D06 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那么！二年级{color=#FF0000}红队{/color}的大家！\n谢谢你们今天特地过来！"

    show rs_image_8CE08F208261448AB0AB50BEE127AB04 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这次我们同处一队，一定是命运的引导！\n大家一起亲密合作向着胜利……"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}人声噪杂{/size}{w=0.4}{size=28}@￥&amp;@#{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_0BDBAB46852441A1A55BE2EB34CF561F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_4E534C3CC3ED418EA9C8155C87F1BCBB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那个，安静！唔，大家根本就没在听我的话！"

    show rs_image_F4E69F65605A49BCA7659DDD9B7624D5 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "集合两个班，又没有老师在现场，很难维持秩序呢。\n"
    show rs_image_08C285D4068B443CA62FFF7164C88026 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……仔细看看，没来的人也有。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_376CA53D8BF64CE497CF774B53A38857 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "混蛋——！太不给面子了——！"

    show rs_image_70C4C5BDAB0647638B31D8F61A4438FD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "今天就要决定下各个项目的选手了，该、该怎么做。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    show rs_image_342469B7E318428586C1F76696312BCB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "给我肃静——！！你们的班长就在讲台上——！\n给我保持安静——！好好听我们说话——！"

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    show rs_image_F3D233F763D6421EBDC0A1616D4F0D6F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.9

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.5

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "大家看过来——！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "慎酱！到底去什么地方鬼混了！！"

    window hide

    pause 0.5

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Impact 2.ogg"

    # Gallery unlock: images/CG/Sports celemony.png
    $ zorder_rs_image_B4E4E5696DB74835907C35BB91F9BD19 = -100
    show rs_image_B4E4E5696DB74835907C35BB91F9BD19 as rs_image_B4E4E5696DB74835907C35BB91F9BD19 zorder zorder_rs_image_B4E4E5696DB74835907C35BB91F9BD19 onlayer master
    hide rs_image_B4E4E5696DB74835907C35BB91F9BD19

    show rs_image_B4E4E5696DB74835907C35BB91F9BD19 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 0.8

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我们，红队应援团的队服就准备是这个样子了——！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "音乐和舞蹈会由松田亲完成的样子——"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "也和其他年级的责任人取得了一些交涉上的进展，敬请期待。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "很帅嘛！全班都有？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "不好意思猫山，这衣服只有四人的。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "再怎么说没那么多钱做全班的，所以就只给体型好的四个人做了。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "其他人就将就着在体操服外面套上学生制服跟着跳好了。{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_D9CD4282EE0542318302CA8D9133A611 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "欸——！那样看上去太逊了！木村，和我换！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "不要不要才不要——♪\n反正你步伐不稳、骨质不佳，穿不了这衣服。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "什么！？"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空，如何？合适嘛？"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那个，嗯。我觉得很好。不愧是哥哥。"

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "嗯，四位确实如同绘卷般。小岛君，快拍！"

    rs_character_53FF68C192E3494AB005C1909579AFFB "是的，部长。\n视线请稍微下移～好的，茄子。"

    window hide

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Shoot 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Shoot 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    pause 0.8

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_6C7D131D881A4E7296FCD71C208CF53F as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_376CA53D8BF64CE497CF774B53A38857 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8F070BDCB04D4336AC7465096F0E3084 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.6

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔。唔呜……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君，我们要一起加油。"

    show rs_image_40378AEBEABC4F1181A8ACEC0693C48A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我会去询问二班所有人希望参加的项目，友君就请负责一班的。"

    show rs_image_943958ACE1594083BA9B66D14E70D431 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可是，问完后该怎么做？只是我们决定的话之后要是被拒……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_10B88B501E394D0BB0E3D5ECDC8DF543 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "天知道。无视。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "都说了要讨论。既然他们不听，也就不用管了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_4E534C3CC3ED418EA9C8155C87F1BCBB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼、翼君，生气了？"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8


    if judge_lm_condition([]):
        jump block_00003988

    return

label block_00003988:
    # Node: 00003988 (體育祭)
    call block_00000333 from _call_block_00000333

    if judge_lm_condition([]):
        jump block_0000398D

    return

label block_0000398D:
    # Node: 0000398D (After event)
    $ set_window("イベントモード")
    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_0D1A14CC6DD549EA877967C087A4F0E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C3AC3BC102640A98B0B848A29849370

    pause 2

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    if sys_music_current_file != "sound/BGM/Night.ogg":
        play music "sound/BGM/Night.ogg" loop
        $ sys_music_current_file = "sound/BGM/Night.ogg"

    show rs_image_48D26C14A18B4805B108A02B239C32FF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7AE3125258BC4D33A7DBD94B1EAB358D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_090583914F36486EA2E7A56AF765A727 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……今天好累。我要睡——"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    show rs_image_EA10E33B759D46E7921B02D950347983 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "等等，睡觉之前必须先洗澡。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_FA5B703A676F4C829E63A8555EB84BD5 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D3337C6701A1424493940A3CA157D89B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼～"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_9EDA7F9D083C40B38F8A696E765C90E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "今天出了这么多汗，太不卫生了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼～"

    show rs_image_EA10E33B759D46E7921B02D950347983 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "听到了没？真是的。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯～\n"
    show rs_image_6FBF7F2D5928430F8627C4EEA3F08C63 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……帮我和忍和妈妈说“便当很好吃”。"

    show rs_image_7AE3125258BC4D33A7DBD94B1EAB358D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这我明白，但睡觉前还是必须先洗澡。"

    show rs_image_FA5B703A676F4C829E63A8555EB84BD5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "早上会冲的，先让我睡～"

    show rs_image_EA10E33B759D46E7921B02D950347983 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔……算了。好，晚安。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "晚安——"

    window hide

    pause 0.3

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    show rs_image_48D26C14A18B4805B108A02B239C32FF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_7AE3125258BC4D33A7DBD94B1EAB358D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哦，对了，明天我早上有晨练，\n"
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    show rs_image_D3337C6701A1424493940A3CA157D89B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    extend "还有，你应该没忘，明天开始要……"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_090583914F36486EA2E7A56AF765A727 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯～？"
    show rs_image_FA5B703A676F4C829E63A8555EB84BD5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "嗯～。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_EA10E33B759D46E7921B02D950347983 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_48D26C14A18B4805B108A02B239C32FF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "千万别忘了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_FA5B703A676F4C829E63A8555EB84BD5 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D3337C6701A1424493940A3CA157D89B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯～"

    window hide

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_53C43FF5997344BAAADBDF967F5E5DBE as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 2.5

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 2.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_52A4FB95B188448396BFCDB678787F82 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    pause 2.3

    show rs_image_B444FDE4EF1A43E5A2345A44A71061D5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Alarm 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Alarm 1.ogg"

    pause 2.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Switch 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Switch 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_090583914F36486EA2E7A56AF765A727 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯～\n"
    if sys_music2_current_file != "sound/Effect Sound/Stupid 1.ogg":
        play music2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_9B8DAC89E5144010A4E0E9EF7657680E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "啊——好痛，肌肉痛，真的好痛……"

    show rs_image_6215465F385F4702A227A74F52C707E0 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "今天就先别嗡嗡了……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_9B8DAC89E5144010A4E0E9EF7657680E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "话说回来，为什么体育祭第二天还要上学啊，\n所以才说私立学校……"

    window hide

    pause 0.4

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.4

    if sys_music_current_file != "sound/BGM/Chapter 3.ogg":
        play music "sound/BGM/Chapter 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 3.ogg"

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Train 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Train 1.ogg"

    show rs_image_0FE13B27C36F40D6A48872A82DF3AE41 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    pause 1

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……总觉得心神不宁。\n"
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……呃？{w=0.65}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "什么？！"

    window hide

    pause 0.5

    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_98508F03C2B54E6595F99F669212CD79 as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_441F8D4294324B4C9C6A6800165D3B7D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.9

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_0999797A178545CBA5F244F41BBA50B1
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 200
    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 200
    show rs_image_6581541AC4C34DE4AD8AE0D6865112C1 as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_DD2521E5C93C4C7A9DD6C7B09A64AD4B as tag_988AD5B87A6D42E59078E032C7FA7EB1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.9

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 200
    $ zorder_tag_A997D3C41A7C476C9FB30A36F31332FC = 200
    show rs_image_42C3B526C247471AA015209476FA27F8 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    show rs_image_55DB6FBFD0DE48D4B5742B0743451560 as tag_A997D3C41A7C476C9FB30A36F31332FC at center_top zorder zorder_tag_A997D3C41A7C476C9FB30A36F31332FC onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.9

    hide tag_A997D3C41A7C476C9FB30A36F31332FC
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.3

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（诶，不是……难道……）"

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{size=28}（今天开始换{/size}{size=28}{color=#00FFFF}冬装{/color}{/size}{size=28}了——！！？）{/size}"

    window hide

    pause 1.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_E6A0D20A1A914A0CBCF8DCED075CD75A

    stop music fadeout 3
    $ sys_music_current_file = ""

    pause 4

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_32D0BBC2E623421F81987D13AFF8B019 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1.5

    $ zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD = 300
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_514AB31E9F5945EEA9AD0CA77359CA06 as tag_0BDB8A4A05BB44ED81AE140BE96066BD at center_bottom zorder zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD onlayer master
    show rs_image_9C058B4785934A84B6E833C97FAFAA9B _("{font=font/zcool-happy-ayumi-extended.ttf}第一章 完成{/font}") as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_center zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 2

    $ set_window("体育祭、音楽祭")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#000000}请保存至今为止的进度。{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_0000398F

    return

label block_0000398F:
    # Node: 0000398F (Set: SaveCaption)
    $ _lm_save_caption = "第一章結束后"

    if judge_lm_condition([]):
        jump block_0000398E

    return

label block_0000398E:
    # Node: 0000398E (Save)
    call screen save

    if judge_lm_condition([]):
        jump block_0000398A

    return

label block_0000398A:
    # Node: 0000398A (SaveCaption: NULL)
    $ _lm_save_caption = ""

    if judge_lm_condition([]):
        jump block_00003E8E

    return

label block_00003E8E:
    # Node: 00003E8E (Generate parameter)
    $ C2TalkOkajimaInitNumber = 0
    $ C2TalkOkajimaInitNumber = TalkOkajima

    if judge_lm_condition([]):
        jump block_0000398B

    return

label block_0000398B:
    # Node: 0000398B (CLEAR)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_0BDB8A4A05BB44ED81AE140BE96066BD
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 1


    if judge_lm_condition([]):
        jump block_00003993

    return

label block_00003993:
    # Node: 00003993 (CHAPTER 2)
    $ del TalkNoriF5
    $ del TalkBookstoreF5
    $ del TalkTsubasaF1After
    $ del TalkTsukiSoraF1After
    $ del TalkItouKimuraF1After
    $ del TalkShintaroF3After
    $ del TalkTsubasaF4After
    $ del TalkShinobuF5After
    $ del TalkKimuraQKimuraConferenceAfter
    $ del TalkTsubasaQTsubasaAfter
    $ del TalkKimura
    $ del TalkItou
    $ del TalkKatou
    $ del TalkTsubasa
    $ del TalkMatsuta
    $ del TalkIzumi
    $ del TalkSatou
    $ del TalkSakuya
    $ del TalkSora
    $ del TalkShintaro
    $ del TalkShinobu
    $ del TalkOkajima
    $ del QKimuraCheck1
    $ del QSabushinCheck1
    $ del QTsubasaCheck1
    $ del F5Check1
    $ del C1S1Phase
    $ del C1S2Phase
    $ del C1S3Phase
    $ del C1S4Phase
    $ del C1S5Phase
    $ del C1QNewsclubPhase
    $ del C1QSabushinPhase
    $ del C1QTsubasaPhase
    $ del C1QMatsutaPhase
    jump block_00003962

    return

