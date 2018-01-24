# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 0000116D (阿月測眼力)

label block_0000116E:
    # Node: 0000116E (開始)
    $ CorrectCount = 0
    $ CurrentIndex = -1
    $ TotalCount = 0
    $ TimeState = 0

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    if judge_lm_condition([]):
        jump block_000037DC

    return

label block_000037DC:
    # Node: 000037DC (PREPARE)
    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ set_place_title(False)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 1.5

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_69E470D45F2C464CA4A1DAED028068FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    if sys_music2_current_file != "sound/BGM/Series - Akamine brothers.ogg":
        play music2 "sound/BGM/Series - Akamine brothers.ogg" loop
        $ sys_music2_current_file = "sound/BGM/Series - Akamine brothers.ogg"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Break 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    show rs_image_ED4EBC53C3F040A5B5A519ACC94246AA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_C29BFF9F2C814823B4B63C9D37A39E79

    pause 0.4


    if judge_lm_condition([]):
        jump block_000037BA

    return

label block_000037BA:
    # Node: 000037BA (PREPARE)
    if Chapter > 2 and (GTsukiTestSoraMode == False):
        $ TimeState = 2
    elif GTsukiTestSoraMode == True:
        $ TimeState = 1
    else:
        $ TimeState = 0

    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestStage == 5" }]):
        jump block_00002A8F
    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestStage == 0" }]):
        jump block_00002CCF
    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestStage == 1" }]):
        jump block_00002CD0
    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestStage == 2" }]):
        jump block_00002CD1
    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestStage == 3" }]):
        jump block_00002CD2
    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestStage == 4" }]):
        jump block_00002CD3

    return

label block_00002A8F:
    # Node: 00002A8F (選擇)
    $ sys_lm_menu_item = [{"pos": (32, 134),"image": "images/Games/Tsukis-concentration-test/Find 1.png","hover": "images/Games/Tsukis-concentration-test/Find 1 hover.png","name": "Find1"}, {"pos": (288, 134),"image": "images/Games/Tsukis-concentration-test/Find 2.png","hover": "images/Games/Tsukis-concentration-test/Find 2 hover.png","name": "Find2"}, {"pos": (552, 134),"image": "images/Games/Tsukis-concentration-test/Find 3.png","hover": "images/Games/Tsukis-concentration-test/Find 3 hover.png","name": "Find3"}, {"pos": (32, 350),"image": "images/Games/Tsukis-concentration-test/Number 1.png","hover": "images/Games/Tsukis-concentration-test/Number 1 hover.png","name": "Number1"}, {"pos": (288, 350),"image": "images/Games/Tsukis-concentration-test/Number 2.png","hover": "images/Games/Tsukis-concentration-test/Number 2 hover.png","name": "Number2"}, {"pos": (552, 350),"image": "images/Games/Tsukis-concentration-test/Return.png","hover": "images/Games/Tsukis-concentration-test/Return hover.png","name": "Return"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_673
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Return\"" }]):
        jump block_000037DD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Find1\"" }]):
        jump block_00002CCF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Number1\"" }]):
        jump block_00002CD0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Find2\"" }]):
        jump block_00002CD1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Number2\"" }]):
        jump block_00002CD2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Find3\"" }]):
        jump block_00002CD3

    return

label block_000037DD:
    # Node: 000037DD (RESET)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    if judge_lm_condition([]):
        jump block_000037C0

    return

label block_000037C0:
    # Node: 000037C0 ()
    $ del CorrectCount
    $ del CurrentIndex
    $ del TotalCount
    $ del TimeState

    stop music2 fadeout 0.5
    $ sys_music_current_file = ""

    $ reverse_volume("music", 0.7)

    return

label block_00002CCF:
    # Node: 00002CCF (Find 1)
    $ TotalCount = 10

    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 2" }]):
        jump block_000037B1
    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 1" }]):
        jump block_00002CC9
    if judge_lm_condition([]):
        jump block_00001172

    return

label block_000037B1:
    # Node: 000037B1 (Find 1 冬)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_0CBEE3104B544997B9F152690F79B463 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的训练是“{color=#0080FF}寻找正确选项{/color}”。\n然而，存在{color=#FF0000}时间限制{/color}。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "就看你能多快找到正确答案了。{w}\n来，开始了。"

    window hide


    if judge_lm_condition([]):
        jump block_000037B0

    return

label block_000037B0:
    # Node: 000037B0 (Update)
    $ CurrentIndex = CurrentIndex + 1
    if CurrentIndex < 10:
        if TimeState == 2:
            show rs_image_62DDFA5A234046A99A6D1D7E88EA46C2 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        elif TimeState == 1:
            show rs_image_C33AC4318DF74FED80B18E300D08A925 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        else:
            show rs_image_5C82B57D70084E5EBD789404205EDC04 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop

        $ zorder_tag_348CF07D60744BC79223A712FCFA9BD9 = 400
        if CurrentIndex < 4:
            show rs_image_937A282FBFF24D248621A92D245DDA8C as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
            with rs_effect_777EBB3BEF314C5187906634D1CE341E

            pause 0.5

        elif CurrentIndex < 8:
            show rs_image_B328C7BDA73A41388D184B977F7C8835 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
            with rs_effect_777EBB3BEF314C5187906634D1CE341E

            pause 0.5

        else:
            show rs_image_5CFD07A8448C400696FFD63D4E01D216 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
            with rs_effect_777EBB3BEF314C5187906634D1CE341E

            pause 0.5


    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 0" }]):
        jump block_0000117C
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 1" }]):
        jump block_00001180
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 2" }]):
        jump block_00001188
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 3" }]):
        jump block_00001189
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 4" }]):
        jump block_00002942
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 5" }]):
        jump block_0000293D
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 6" }]):
        jump block_00002938
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 7" }]):
        jump block_00002935
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 8" }]):
        jump block_00002945
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 9" }]):
        jump block_00002949
    if judge_lm_condition([]):
        jump block_000037FF

    return

label block_0000117C:
    # Node: 0000117C (1)
    $ sys_lm_choice_item = ["TALPIDAE", "TALPIDEA", "TALPIDOE", "PANTS"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_1B379FA2CC1B4F89A6A2343999BEC286 = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_1B379FA2CC1B4F89A6A2343999BEC286 zorder zorder_rs_image_choice_1B379FA2CC1B4F89A6A2343999BEC286 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_10
    hide rs_image_choice_1B379FA2CC1B4F89A6A2343999BEC286
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"TALPIDAE\"" }]):
        jump block_000037AC
    if judge_lm_condition([]):
        jump block_000037AD

    return

label block_000037AC:
    # Node: 000037AC (對)
    play effect "sound/Effect Sound/Correct 1.ogg" noloop

    show rs_image_0C55A05D870D4AFD8FA6561C542AEB06 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if TimeState == 2:
        show rs_image_2594659CB59F456896B2EF27AD70323C as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "干得好！"

    elif TimeState == 1:
        show rs_image_7E2778FA3D624F319D303738D4143BE5 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "非常好哦！"
    else:
        show rs_image_CA7FB6339967475B8EDC72EB94052C60 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        
        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "干得好！"
    
    window hide

    $ CorrectCount = CorrectCount + 1

    if judge_lm_condition([]):
        jump block_000037B0

    return

label block_000037AD:
    # Node: 000037AD (錯)
    play effect "sound/Effect Sound/Wrong 1.ogg" noloop

    show rs_image_4C358D6358994092B67D2FE620F9E858 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if TimeState == 2:
        show rs_image_89E17548BB5E44C3928F3166B177C150 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不行啊。"

    elif TimeState == 1:
        show rs_image_B63B525194554F0BBF36CCFF8577D5AC as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "好可惜。"
    else:
        show rs_image_5CE8CAA349B8484888F68CD67D37CBFD as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        
        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不行啊。"
    
    window hide

    if judge_lm_condition([]):
        jump block_000037B0

    return

label block_00001180:
    # Node: 00001180 (2)
    $ sys_lm_choice_item = ["BIKINI", "TALPIDAE", "TALPIDEA", "TALPIDOE"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_83833B5A795A47849F9ADD4FA411CDBD = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_83833B5A795A47849F9ADD4FA411CDBD zorder zorder_rs_image_choice_83833B5A795A47849F9ADD4FA411CDBD onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_11
    hide rs_image_choice_83833B5A795A47849F9ADD4FA411CDBD
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"TALPIDAE\"" }]):
        jump block_000037AC
    if judge_lm_condition([]):
        jump block_000037AD

    return

label block_00001188:
    # Node: 00001188 (3)
    $ sys_lm_choice_item = ["TOLPIDAE", "TALPIDAE", "TOLPIDIE", "PANTS", "AILURUS FULGENS", "TALPIDEE"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_F11C995DDACF418EA455E6F3D115D55A = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_F11C995DDACF418EA455E6F3D115D55A zorder zorder_rs_image_choice_F11C995DDACF418EA455E6F3D115D55A onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_12
    hide rs_image_choice_F11C995DDACF418EA455E6F3D115D55A
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"TALPIDAE\"" }]):
        jump block_000037AC
    if judge_lm_condition([]):
        jump block_000037AD

    return

label block_00001189:
    # Node: 00001189 (4)
    $ sys_lm_choice_item = ["BIKINI", "TOLPIDAE", "TOLPLDAE", "TALPIDAE", "TOLPODOE", "PANTS", "TSUBASA", "AUTUMN FOLIAGE", "TALPTALP", "MORIUMI"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_0D4228B3D1844EFA9048105701AF6B8D = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_0D4228B3D1844EFA9048105701AF6B8D zorder zorder_rs_image_choice_0D4228B3D1844EFA9048105701AF6B8D onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_13
    hide rs_image_choice_0D4228B3D1844EFA9048105701AF6B8D
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"TALPIDAE\"" }]):
        jump block_000037AC
    if judge_lm_condition([]):
        jump block_000037AD

    return

label block_00002942:
    # Node: 00002942 (5)
    $ sys_lm_choice_item = ["TSUMIKI", "TSUBOMI", "TSUBAME", "TSUBASA"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_17A46DE7C1D34C8CB8BBFBDDF01546FF = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_17A46DE7C1D34C8CB8BBFBDDF01546FF zorder zorder_rs_image_choice_17A46DE7C1D34C8CB8BBFBDDF01546FF onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_14
    hide rs_image_choice_17A46DE7C1D34C8CB8BBFBDDF01546FF
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"TSUBASA\"" }]):
        jump block_000037AC
    if judge_lm_condition([]):
        jump block_000037AD

    return

label block_0000293D:
    # Node: 0000293D (6)
    $ sys_lm_choice_item = ["TSUBASE", "TSUBASO", "TSUBASA", "TSUPASA"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_AFAFE8031277463BA6EBDD574B6C109A = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_AFAFE8031277463BA6EBDD574B6C109A zorder zorder_rs_image_choice_AFAFE8031277463BA6EBDD574B6C109A onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_15
    hide rs_image_choice_AFAFE8031277463BA6EBDD574B6C109A
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"TSUBASA\"" }]):
        jump block_000037AC
    if judge_lm_condition([]):
        jump block_000037AD

    return

label block_00002938:
    # Node: 00002938 (7)
    $ sys_lm_choice_item = ["SHIPASA", "SHIBASA", "TSUPAZA", "TSUBAZA", "TSUBASA", "TSUPASA"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_7F84A03771F9440C876B5E691BF9829A = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_7F84A03771F9440C876B5E691BF9829A zorder zorder_rs_image_choice_7F84A03771F9440C876B5E691BF9829A onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_16
    hide rs_image_choice_7F84A03771F9440C876B5E691BF9829A
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"TSUBASA\"" }]):
        jump block_000037AC
    if judge_lm_condition([]):
        jump block_000037AD

    return

label block_00002935:
    # Node: 00002935 (8)
    $ sys_lm_choice_item = ["SAKUYA", "TSUPASA", "ZUBASA", "TSBASA", "ZUBAZA", "PANTS", "TSUBAZA", "TSUHAZA", "TSUPAZA", "TSUBASA"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_9096A9F36E3548749C64941C6DF45D84 = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_9096A9F36E3548749C64941C6DF45D84 zorder zorder_rs_image_choice_9096A9F36E3548749C64941C6DF45D84 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_17
    hide rs_image_choice_9096A9F36E3548749C64941C6DF45D84
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"TSUBASA\"" }]):
        jump block_000037AC
    if judge_lm_condition([]):
        jump block_000037AD

    return

label block_00002945:
    # Node: 00002945 (9)
    $ sys_lm_choice_item = ["VIBRETAR", "VIBRETOR", "VIBRATER", "VIBRATER", "VIBRETER", "VIBROTAR", "VIBRATOR", "VIBROTER", "VIBRATOR", "VINROTOR"]
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_9F795D25CA394C2C929431F095AFB307 = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_9F795D25CA394C2C929431F095AFB307 zorder zorder_rs_image_choice_9F795D25CA394C2C929431F095AFB307 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_18
    hide rs_image_choice_9F795D25CA394C2C929431F095AFB307
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"VIBRATOR\"" }]):
        jump block_000037AC
    if judge_lm_condition([]):
        jump block_000037AD

    return

label block_00002949:
    # Node: 00002949 (10)
    $ sys_lm_choice_item = ["VIBRETAR", "VIBROTAR", "VIBROTER", "VIBROTOR", "VIBRATRR", "VIBRATOR", "VIBRATER", "VIBRATAR", "VIBRETER", "VIBRETOE"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_3BCEA4502A124AAF89265111F33CB7FC = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_3BCEA4502A124AAF89265111F33CB7FC zorder zorder_rs_image_choice_3BCEA4502A124AAF89265111F33CB7FC onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_19
    hide rs_image_choice_3BCEA4502A124AAF89265111F33CB7FC
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"VIBRATOR\"" }]):
        jump block_000037AC
    if judge_lm_condition([]):
        jump block_000037AD

    return

label block_000037FF:
    # Node: 000037FF (TO: Result)

    if judge_lm_condition([]):
        jump block_00003800

    return

label block_00003800:
    # Node: 00003800 (TO: Result)

    if judge_lm_condition([]):
        jump block_000037B2

    return

label block_000037B2:
    # Node: 000037B2 (TO: Result)

    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 0" },{ "scope": 1, "content": "GTsukiTestStage == 5" },{ "scope": 1, "content": "(CorrectCount / float(TotalCount)) >= 0.7" }]):
        jump block_000037B4
    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 1" },{ "scope": 1, "content": "GTsukiTestStage == 5" },{ "scope": 1, "content": "(CorrectCount / float(TotalCount)) >= 0.7" }]):
        jump block_000037B6
    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 2" },{ "scope": 1, "content": "GTsukiTestStage == 5" },{ "scope": 1, "content": "(CorrectCount / float(TotalCount)) >= 0.7" }]):
        jump block_000037B5
    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 0" }]):
        jump block_000037B7
    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 1" }]):
        jump block_000037B9
    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 2" }]):
        jump block_000037B8

    return

label block_000037B4:
    # Node: 000037B4 (Phase 1-1)

    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestStage == 5" }]):
        jump block_000037BB
    if judge_lm_condition([]):
        jump block_000029A9

    return

label block_000037BB:
    # Node: 000037BB (Final 月)
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "[TotalCount]问中[CorrectCount]问正确！{w}做的不错。\n什么时候想再次挑战随时来找我。{w=0.7}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "{i}以上、解散！{/i}"

    window hide

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_31FEF114566B4AB483D935C987B9E096
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.7

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_000037BF

    return

label block_000037BF:
    # Node: 000037BF ()
    $ del CorrectCount
    $ del CurrentIndex
    $ del TotalCount
    $ del TimeState

    stop music2 fadeout 0.5
    $ sys_music_current_file = ""

    $ reverse_volume("music", 0.7)

    return

label block_000029A9:
    # Node: 000029A9 (Next 月)
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "[TotalCount]问中[CorrectCount]问正确！{w}做的不错。\n看样子可以挑战{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#FF00FF}下个问题{/color}了。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "下次会换个更难的问题。\n准备好了随时来找我。{w=0.7}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "{i}以上、解散！{/i}"

    window hide

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_31FEF114566B4AB483D935C987B9E096
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.7

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00002A8B

    return

label block_00002A8B:
    # Node: 00002A8B (GTsukiTestStage ++)
    $ GTsukiTestStage = GTsukiTestStage + 1

    if judge_lm_condition([{ "scope": 0, "content": "CXQTsukiTest == False" }]):
        jump block_0000381C
    if judge_lm_condition([]):
        jump block_000037BF

    return

label block_0000381C:
    # Node: 0000381C (QUEST FINISH)
    $ set_window("(標準)")
    if sys_effect2_current_file != "sound/BGM/Quest Finished.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_effect2_current_file = "sound/BGM/Quest Finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    window hide

    pause 0.8


    if judge_lm_condition([]):
        jump block_0000381B

    return

label block_0000381B:
    # Node: 0000381B (CXQTsukiTest: T)
    $ CXQTsukiTest = True

    if judge_lm_condition([]):
        jump block_000037BF

    return

label block_000037B6:
    # Node: 000037B6 (Phase 1-3)

    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestStage == 5" }]):
        jump block_000037BD
    if judge_lm_condition([]):
        jump block_000037BC

    return

label block_000037BD:
    # Node: 000037BD (Final 空)
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "[TotalCount]问中[CorrectCount]问正确！{w}很不错哦。\n什么时候想再次挑战请随时来找我。{w=0.7}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "{i}以上、解散♪{/i}"

    window hide

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_31FEF114566B4AB483D935C987B9E096
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.7

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_000037BF

    return

label block_000037BC:
    # Node: 000037BC (Next 空)
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "[TotalCount]问中[CorrectCount]问正确！{w}真的很努力了。\n看样子可以挑战{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#FF00FF}下个问题{/color}了呐。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "下次会换更难的问题。\n准备好了请随时来找我哦。{w=0.7}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "{i}以上、解散♪{/i}"

    window hide

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_31FEF114566B4AB483D935C987B9E096
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.7

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00002A8B

    return

label block_000037B5:
    # Node: 000037B5 (Phase 1-2)

    if judge_lm_condition([{ "scope": 0, "content": "GTsukiTestStage == 5" }]):
        jump block_000037BB
    if judge_lm_condition([]):
        jump block_000029A9

    return

label block_000037B7:
    # Node: 000037B7 (Phase 3-1)

    if judge_lm_condition([]):
        jump block_000037B3

    return

label block_000037B3:
    # Node: 000037B3 (Retry 月)
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    show rs_image_5CE8CAA349B8484888F68CD67D37CBFD as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "[TotalCount]问中[CorrectCount]问正确！{w}你很努力了。\n不过，这个水平还不足以挑战{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#FF00FF}下个问题{/color}。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "下次我们再试一次。\n准备好了随时来找我。{w=0.7}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "{i}以上、解散！{/i}"

    window hide

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_31FEF114566B4AB483D935C987B9E096
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.7

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_000037BF

    return

label block_000037B9:
    # Node: 000037B9 (Phase 3-3)

    if judge_lm_condition([]):
        jump block_000037BE

    return

label block_000037BE:
    # Node: 000037BE (Retry 空)
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "[TotalCount]问中[CorrectCount]问正确！{w}很不错哦。\n不过，这样还不足以挑战{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#FF00FF}下个问题{/color}呐。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "等准备好了来找我，\n我们再试一次。{w=0.7}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "{i}以上、解散♪{/i}"

    window hide

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_31FEF114566B4AB483D935C987B9E096
    hide tag_348CF07D60744BC79223A712FCFA9BD9
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.7

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_000037BF

    return

label block_000037B8:
    # Node: 000037B8 (Phase 3-2)

    if judge_lm_condition([]):
        jump block_000037B3

    return

label block_00002CC9:
    # Node: 00002CC9 (Find 1 空)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_4913C76A3FD641CBAFC2DC49CA8837AF as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么，头脑训练要开始了哦。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这次的训练是“{color=#0080FF}寻找正确选项{/color}”。\n不过，一定要小心{color=#FF0000}时间限制{/color}哦。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "速速找到正确答案就好了呐。{w}\n来，开始了。"

    window hide


    if judge_lm_condition([]):
        jump block_000037B0

    return

label block_00001172:
    # Node: 00001172 (Find 1 月)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_0305038F51BC401396154F294FEAA2E7 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的训练是“{color=#0080FF}寻找正确选项{/color}”。\n然而，存在{color=#FF0000}时间限制{/color}。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "就看你能多快找到正确答案了。{w}\n来，开始了。"

    window hide


    if judge_lm_condition([]):
        jump block_000037B0

    return

label block_00002CD0:
    # Node: 00002CD0 (Number 1)
    $ TotalCount = 9

    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 2" }]):
        jump block_000032AA
    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 1" }]):
        jump block_00002CCA
    if judge_lm_condition([]):
        jump block_00002954

    return

label block_000032AA:
    # Node: 000032AA (Number 1 冬)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_0CBEE3104B544997B9F152690F79B463 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的任务是选择恰当的{color=#0080FF}数字{/color}。\n接下来会不断出现各种数字，尝试记住他们。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，开始。"

    window show


    if judge_lm_condition([]):
        jump block_000037CD

    return

label block_000037CD:
    # Node: 000037CD (Update)
    $ CurrentIndex = CurrentIndex + 1
    if CurrentIndex < 9:
        if TimeState == 2:
            show rs_image_62DDFA5A234046A99A6D1D7E88EA46C2 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        elif TimeState == 1:
            show rs_image_C33AC4318DF74FED80B18E300D08A925 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        else:
            show rs_image_5C82B57D70084E5EBD789404205EDC04 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop

        $ zorder_tag_348CF07D60744BC79223A712FCFA9BD9 = 400
        if CurrentIndex < 4:
            show rs_image_450E72BACA8C41E386BD3F2E287115E3 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
            with rs_effect_777EBB3BEF314C5187906634D1CE341E

            pause 0.5

        elif CurrentIndex < 8:
            show rs_image_6992278163DA45AE8B9F944BEE610150 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
            with rs_effect_777EBB3BEF314C5187906634D1CE341E

            pause 0.5

        else:
            show rs_image_317AE85C1BE748B89D08636A300C6541 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
            with rs_effect_777EBB3BEF314C5187906634D1CE341E

            pause 0.5

    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 0" }]):
        jump block_000037CE
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 1" }]):
        jump block_000037CF
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 2" }]):
        jump block_000037D0
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 3" }]):
        jump block_000037D1
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 4" }]):
        jump block_000037D2
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 5" }]):
        jump block_000037D4
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 6" }]):
        jump block_000037D7
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 7" }]):
        jump block_000037D8
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 8" }]):
        jump block_000037D9
    if judge_lm_condition([]):
        jump block_00003800

    return

label block_000037CE:
    # Node: 000037CE (1)
    $ set_window("イベントモード")
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}九{/size}{w=0.4}{size=32}五{/size}{w=0.4}{size=32}八{/size}{w=0.4}{size=32}四{/size}{w=0.4}{size=32}零{/size}{w=0.4}{size=32}三{/size}{w=0.4}{size=32}六{/size}{w=0.4}{size=32}二{/size}{w=0.4}{size=32}一{/size}{w=4}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_68975D5C597543F1B6B1FD797877D460 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_000037CB

    return

label block_000037CB:
    # Node: 000037CB (1)
    $ sys_lm_choice_item = ["零", "七", "二", "一"]
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_241C139EC36F4669BDDF61A2B5DCC91F = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_241C139EC36F4669BDDF61A2B5DCC91F zorder zorder_rs_image_choice_241C139EC36F4669BDDF61A2B5DCC91F onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_20
    hide rs_image_choice_241C139EC36F4669BDDF61A2B5DCC91F
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"七\"" }]):
        jump block_000037CA
    if judge_lm_condition([]):
        jump block_000037CC

    return

label block_000037CA:
    # Node: 000037CA (對)
    play effect "sound/Effect Sound/Correct 1.ogg" noloop

    show rs_image_0C55A05D870D4AFD8FA6561C542AEB06 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if TimeState == 2:
        show rs_image_2594659CB59F456896B2EF27AD70323C as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "干得好！"

    elif TimeState == 1:
        show rs_image_7E2778FA3D624F319D303738D4143BE5 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "非常好哦！"
    else:
        show rs_image_CA7FB6339967475B8EDC72EB94052C60 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        
        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "干得好！"
    
    window hide

    $ CorrectCount = CorrectCount + 1

    if judge_lm_condition([]):
        jump block_000037DB

    return

label block_000037DB:
    # Node: 000037DB (TO: Update)

    if judge_lm_condition([]):
        jump block_000037CD

    return

label block_000037CC:
    # Node: 000037CC (錯)
    play effect "sound/Effect Sound/Wrong 1.ogg" noloop

    show rs_image_4C358D6358994092B67D2FE620F9E858 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if TimeState == 2:
        show rs_image_89E17548BB5E44C3928F3166B177C150 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不行啊。"

    elif TimeState == 1:
        show rs_image_B63B525194554F0BBF36CCFF8577D5AC as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "好可惜。"
    else:
        show rs_image_5CE8CAA349B8484888F68CD67D37CBFD as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        
        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不行啊。"
    
    window hide

    if judge_lm_condition([]):
        jump block_000037DA

    return

label block_000037DA:
    # Node: 000037DA (TO: Update)

    if judge_lm_condition([]):
        jump block_000037CD

    return

label block_000037CF:
    # Node: 000037CF (2)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}五{/size}{w=0.4}{size=32}三{/size}{w=0.4}{size=32}一{/size}{w=0.4}{size=32}九{/size}{w=0.4}{size=32}七{/size}{w=0.4}{size=32}四{/size}{w=0.4}{size=32}零{/size}{w=0.4}{size=32}六{/size}{w=0.4}{size=32}八{/size}{w=4}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_68975D5C597543F1B6B1FD797877D460 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_000037C9

    return

label block_000037C9:
    # Node: 000037C9 (2)
    $ sys_lm_choice_item = ["二", "八", "零", "一"]
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_F8BF5C02932E4E93BB71218AC7B4D9AA = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_F8BF5C02932E4E93BB71218AC7B4D9AA zorder zorder_rs_image_choice_F8BF5C02932E4E93BB71218AC7B4D9AA onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_21
    hide rs_image_choice_F8BF5C02932E4E93BB71218AC7B4D9AA
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"二\"" }]):
        jump block_000037CA
    if judge_lm_condition([]):
        jump block_000037CC

    return

label block_000037D0:
    # Node: 000037D0 (3)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}一{/size}{w=0.4}{size=32}七{/size}{w=0.4}{size=32}三{/size}{w=0.4}{size=32}五{/size}{w=0.4}{size=32}零{/size}{w=0.4}{size=32}九{/size}{w=0.4}{size=32}八{/size}{w=0.4}{size=32}二{/size}{w=0.4}{size=32}六{/size}{w=4}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_68975D5C597543F1B6B1FD797877D460 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_000037C8

    return

label block_000037C8:
    # Node: 000037C8 (3)
    $ sys_lm_choice_item = ["五", "四", "七", "八"]
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_53274BD68F444D98AE12437B1105E8FC = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_53274BD68F444D98AE12437B1105E8FC zorder zorder_rs_image_choice_53274BD68F444D98AE12437B1105E8FC onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_22
    hide rs_image_choice_53274BD68F444D98AE12437B1105E8FC
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"四\"" }]):
        jump block_000037CA
    if judge_lm_condition([]):
        jump block_000037CC

    return

label block_000037D1:
    # Node: 000037D1 (4)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}三{/size}{w=0.4}{size=32}二{/size}{w=0.4}{size=32}一{/size}{w=0.4}{size=32}一{/size}{w=0.4}{size=32}一{/size}{w=0.4}{size=32}二{/size}{w=0.4}{size=32}一{/size}{w=0.4}{size=32}三{/size}{w=0.4}{size=32}三{/size}{w=3}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_4B988B65021947468BC13BBB543C39DE as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_000037C7

    return

label block_000037C7:
    # Node: 000037C7 (4)
    $ sys_lm_choice_item = ["一", "二", "三", "四"]
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_3496E662377644009B7B93F157D8D34E = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_3496E662377644009B7B93F157D8D34E zorder zorder_rs_image_choice_3496E662377644009B7B93F157D8D34E onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_23
    hide rs_image_choice_3496E662377644009B7B93F157D8D34E
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三\"" }]):
        jump block_000037CA
    if judge_lm_condition([]):
        jump block_000037CC

    return

label block_000037D2:
    # Node: 000037D2 (5)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}一{/size}{w=0.4}{size=32}四{/size}{w=0.4}{size=32}一{/size}{w=0.4}{size=32}二{/size}{w=0.4}{size=32}三{/size}{w=0.4}{size=32}四{/size}{w=0.4}{size=32}三{/size}{w=0.4}{size=32}四{/size}{w=3}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_9100FA30DBF24263AEDD9D6F5828B7F1 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_000037D3

    return

label block_000037D3:
    # Node: 000037D3 (5)
    $ sys_lm_choice_item = ["一", "二", "三", "四"]
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_F328D585D9034C79A3A7177049F7FECB = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_F328D585D9034C79A3A7177049F7FECB zorder zorder_rs_image_choice_F328D585D9034C79A3A7177049F7FECB onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_24
    hide rs_image_choice_F328D585D9034C79A3A7177049F7FECBn
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"二\"" }]):
        jump block_000037CA
    if judge_lm_condition([]):
        jump block_000037CC

    return

label block_000037D4:
    # Node: 000037D4 (6)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}{color=#FFFF00}一{/color}{/size}{w=0.4}{size=32}{color=#0000FF}一{/color}{/size}{w=0.4}{size=32}{color=#0000FF}二{/color}{/size}{w=0.4}{size=32}{color=#FF0000}三{/color}{/size}{w=0.4}{size=32}{color=#FFFF00}一{/color}{/size}{w=0.4}{size=32}{color=#FFFF00}三{/color}{/size}{w=0.4}{size=32}{color=#008000}三{/color}{/size}{w=0.4}{size=32}{color=#008000}二{/color}{/size}{w=3}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_9EC61F0B429746AA9DF80EE60877B435 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_000037D5

    return

label block_000037D5:
    # Node: 000037D5 (6)
    $ sys_lm_choice_item = ["一", "二", "三", "四"]
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_5C3E7E4659404D3CB9CD83AE3137F787 = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_5C3E7E4659404D3CB9CD83AE3137F787 zorder zorder_rs_image_choice_5C3E7E4659404D3CB9CD83AE3137F787 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_25
    hide rs_image_choice_5C3E7E4659404D3CB9CD83AE3137F787
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"二\"" }]):
        jump block_000037CA
    if judge_lm_condition([]):
        jump block_000037CC

    return

label block_000037D7:
    # Node: 000037D7 (7)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}{color=#FF0000}一{/color}{/size}{w=0.4}{size=32}{color=#008000}三{/color}{/size}{w=0.4}{size=32}{color=#FF00FF}二{/color}{/size}{w=0.4}{size=32}{color=#FF00FF}二{/color}{/size}{w=0.4}{size=32}{color=#0000FF}四{/color}{/size}{w=0.4}{size=32}{color=#0000FF}四{/color}{/size}{w=0.4}{size=32}{color=#FF0000}一{/color}{/size}{w=3}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_F906F307C98F48CF9E248BFC6B9F4139 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_000037C4

    return

label block_000037C4:
    # Node: 000037C4 (7)
    $ sys_lm_choice_item = ["绿", "黄", "红", "粉"]
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_4CE9191BC68C4EA895FFA769EEA06585 = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_4CE9191BC68C4EA895FFA769EEA06585 zorder zorder_rs_image_choice_4CE9191BC68C4EA895FFA769EEA06585 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_26
    hide rs_image_choice_4CE9191BC68C4EA895FFA769EEA06585
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"粉\"" }]):
        jump block_000037CA
    if judge_lm_condition([]):
        jump block_000037CC

    return

label block_000037D8:
    # Node: 000037D8 (8)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}{color=#0000FF}一{/color}{/size}{w=0.4}{size=32}{color=#FF0000}二{/color}{/size}{w=0.4}{size=32}{color=#0000FF}三{/color}{/size}{w=0.4}{size=32}{color=#0000FF}四{/color}{/size}{w=0.4}{size=32}{color=#FF0000}五{/color}{/size}{w=0.4}{size=32}{color=#FF0000}六{/color}{/size}{w=0.4}{size=32}{color=#0000FF}七{/color}{/size}{w=3}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_3D970EC1DA1D44E08E6A4D0159B6E0AB as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_000037C2

    return

label block_000037C2:
    # Node: 000037C2 (8)
    $ sys_lm_choice_item = ["红", "蓝"]
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_D45750E559D6425D82D937C112A762F8 = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_D45750E559D6425D82D937C112A762F8 zorder zorder_rs_image_choice_D45750E559D6425D82D937C112A762F8 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_27
    hide rs_image_choice_D45750E559D6425D82D937C112A762F8
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"蓝\"" }]):
        jump block_000037CA
    if judge_lm_condition([]):
        jump block_000037CC

    return

label block_000037D9:
    # Node: 000037D9 (9)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}{color=#008000}一{/color}{/size}{w=0.4}{size=32}{color=#800080}二{/color}{/size}{w=0.4}{size=32}{color=#FF0000}三{/color}{/size}{w=0.4}{size=32}{color=#FFFF00}四{/color}{/size}{w=0.4}{size=32}{color=#FF00FF}五{/color}{/size}{w=0.4}{size=32}{color=#0000FF}六{/color}{/size}{w=3}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_840F76BD432C469DBAC5C88D5846CACB as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_000037C3

    return

label block_000037C3:
    # Node: 000037C3 (9)
    $ sys_lm_choice_item = ["绿", "蓝", "红", "黄"]
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_371264FDB9C943BD9A0D3C767005AC6E = 10000
    show rs_image_CA6560AE36944ABEAE3093667EBB093D as rs_image_choice_371264FDB9C943BD9A0D3C767005AC6E zorder zorder_rs_image_choice_371264FDB9C943BD9A0D3C767005AC6E onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 2.666666666666667) from _call_lm_choice_28
    hide rs_image_choice_371264FDB9C943BD9A0D3C767005AC6E
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"绿\"" }]):
        jump block_000037CA
    if judge_lm_condition([]):
        jump block_000037CC

    return

label block_00002CCA:
    # Node: 00002CCA (Number 1 空)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_4913C76A3FD641CBAFC2DC49CA8837AF as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么，头脑训练要开始了哦。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这次的任务是选择恰当的{color=#0080FF}数字{/color}。\n接下来会不断出现各种数字，请试着记住他们。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么，准备——{w}开始！"

    window show


    if judge_lm_condition([]):
        jump block_000037CD

    return

label block_00002954:
    # Node: 00002954 (Number 1 月)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_0305038F51BC401396154F294FEAA2E7 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的任务是选择恰当的{color=#0080FF}数字{/color}。\n接下来会不断出现各种数字，尝试记住他们。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，开始。"

    window show


    if judge_lm_condition([]):
        jump block_000037CD

    return

label block_00002CD1:
    # Node: 00002CD1 (Find 2)
    $ TotalCount = 10

    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 2" }]):
        jump block_000032AB
    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 1" }]):
        jump block_00002CCB
    if judge_lm_condition([]):
        jump block_00002A3D

    return

label block_000032AB:
    # Node: 000032AB (Find 2 冬)
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_0CBEE3104B544997B9F152690F79B463 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的训练也是“{color=#0080FF}寻找正确选项{/color}”。\n然而，存在{color=#FF0000}时间限制{/color}。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "比上次要难得多，做好觉悟比较好。{w}\n那么，开始。"

    window hide


    if judge_lm_condition([]):
        jump block_000037E7

    return

label block_000037E7:
    # Node: 000037E7 (Update)
    $ CurrentIndex = CurrentIndex + 1
    if CurrentIndex < 10:
        if TimeState == 2:
            show rs_image_62DDFA5A234046A99A6D1D7E88EA46C2 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        elif TimeState == 1:
            show rs_image_C33AC4318DF74FED80B18E300D08A925 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        else:
            show rs_image_5C82B57D70084E5EBD789404205EDC04 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop

        $ zorder_tag_348CF07D60744BC79223A712FCFA9BD9 = 400
        if CurrentIndex < 3:
            show rs_image_AF3D318D00D44EE6BA9CEAF429AB9280 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
            with rs_effect_777EBB3BEF314C5187906634D1CE341E

            pause 0.5

        elif CurrentIndex < 6:
            show rs_image_0AED61BC2F8B4824A1EF6A5C042AE0B1 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
            with rs_effect_777EBB3BEF314C5187906634D1CE341E

            pause 0.5
            
        elif CurrentIndex < 8:
            show rs_image_DB3492F41C0F4CA693801087CD1A588F as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
            with rs_effect_777EBB3BEF314C5187906634D1CE341E

            pause 0.5
            
        else:
            show rs_image_ADF0CD37F0A14DB48CCF4E2912649EC2 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
            with rs_effect_777EBB3BEF314C5187906634D1CE341E

            pause 0.5
            

    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 0" }]):
        jump block_000037F5
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 1" }]):
        jump block_000037F6
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 2" }]):
        jump block_000037F7
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 3" }]):
        jump block_000037F8
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 4" }]):
        jump block_000037F9
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 5" }]):
        jump block_000037FA
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 6" }]):
        jump block_000037FB
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 7" }]):
        jump block_000037FC
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 8" }]):
        jump block_000037FD
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 9" }]):
        jump block_000037FE
    if judge_lm_condition([]):
        jump block_000037B2

    return

label block_000037F5:
    # Node: 000037F5 (1)
    $ sys_lm_choice_item = ["SCHOOLBOYZ", "SCHOLOBOYS", "SCHOLLBOYS", "SCHOOLBOYS", "SCHOOLBOLS"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_DCAE90EF30D34071B4B9DBC2A3D3F630 = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_DCAE90EF30D34071B4B9DBC2A3D3F630 zorder zorder_rs_image_choice_DCAE90EF30D34071B4B9DBC2A3D3F630 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_29
    hide rs_image_choice_DCAE90EF30D34071B4B9DBC2A3D3F630
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SCHOOLBOYS\"" }]):
        jump block_000037E3
    if judge_lm_condition([]):
        jump block_000037EA

    return

label block_000037E3:
    # Node: 000037E3 (對)
    play effect "sound/Effect Sound/Correct 1.ogg" noloop

    show rs_image_0C55A05D870D4AFD8FA6561C542AEB06 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if TimeState == 2:
        show rs_image_2594659CB59F456896B2EF27AD70323C as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "干得好！"

    elif TimeState == 1:
        show rs_image_7E2778FA3D624F319D303738D4143BE5 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "非常好哦！"
    else:
        show rs_image_CA7FB6339967475B8EDC72EB94052C60 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        
        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "干得好！"
    
    window hide

    $ CorrectCount = CorrectCount + 1

    if judge_lm_condition([]):
        jump block_000037E7

    return

label block_000037EA:
    # Node: 000037EA (錯)
    play effect "sound/Effect Sound/Wrong 1.ogg" noloop

    show rs_image_4C358D6358994092B67D2FE620F9E858 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if TimeState == 2:
        show rs_image_89E17548BB5E44C3928F3166B177C150 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不行啊。"

    elif TimeState == 1:
        show rs_image_B63B525194554F0BBF36CCFF8577D5AC as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "好可惜。"
    else:
        show rs_image_5CE8CAA349B8484888F68CD67D37CBFD as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        
        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不行啊。"
    
    window hide

    if judge_lm_condition([]):
        jump block_000037E7

    return

label block_000037F6:
    # Node: 000037F6 (2)
    $ sys_lm_choice_item = ["SCHOLOBOYS", "SCHOOLBOYZ", "SCHOLBOOYS", "SCHOOLBOYS", "SCHOOLBLOS"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_00813C2DBCCA493397B9907D70BA98D3 = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_00813C2DBCCA493397B9907D70BA98D3 zorder zorder_rs_image_choice_00813C2DBCCA493397B9907D70BA98D3 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_30
    hide rs_image_choice_00813C2DBCCA493397B9907D70BA98D3
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SCHOOLBOYS\"" }]):
        jump block_000037E3
    if judge_lm_condition([]):
        jump block_000037EA

    return

label block_000037F7:
    # Node: 000037F7 (3)
    $ sys_lm_choice_item = ["SCHLOOBOYZ", "SCHOLOBOYZ", "SCHLOOBOYS", "SCHOOLBOYZ", "SCHOULBOYS", "SCHLOLBOYS", "SCHOLOBOYS", "SCHOOLBOYS"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_3E97EF4D459F4C33AECE4B5AF55B7F78 = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_3E97EF4D459F4C33AECE4B5AF55B7F78 zorder zorder_rs_image_choice_3E97EF4D459F4C33AECE4B5AF55B7F78 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_31
    hide rs_image_choice_3E97EF4D459F4C33AECE4B5AF55B7F78
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"SCHOOLBOYS\"" }]):
        jump block_000037E3
    if judge_lm_condition([]):
        jump block_000037EA

    return

label block_000037F8:
    # Node: 000037F8 (4)
    $ sys_lm_choice_item = ["AYUMU", "AYOMU", "AYOMI", "AYUMI", "AYAMI"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_8A7F5CA1A6F241D08C2D60611E3B8FFF = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_8A7F5CA1A6F241D08C2D60611E3B8FFF zorder zorder_rs_image_choice_8A7F5CA1A6F241D08C2D60611E3B8FFF onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_32
    hide rs_image_choice_8A7F5CA1A6F241D08C2D60611E3B8FFF
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"AYUMI\"" }]):
        jump block_000037E3
    if judge_lm_condition([]):
        jump block_000037EA

    return

label block_000037F9:
    # Node: 000037F9 (5)
    $ sys_lm_choice_item = ["AYUMA", "AYOMI", "AYOMO", "AYAMI", "AYAMA", "AYUMI", "AYUMU"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_35D2C5B564414653A1819680A1141DF7 = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_35D2C5B564414653A1819680A1141DF7 zorder zorder_rs_image_choice_35D2C5B564414653A1819680A1141DF7 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_33
    hide rs_image_choice_35D2C5B564414653A1819680A1141DF7
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"AYUMI\"" }]):
        jump block_000037E3
    if judge_lm_condition([]):
        jump block_000037EA

    return

label block_000037FA:
    # Node: 000037FA (6)
    $ sys_lm_choice_item = ["AYIMI", "AYIMU", "AYOMO", "AYAMA", "AYAMI", "AYOMI", "AYOMU", "AYUMU", "AYUMI", "AYUMA"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_7859591D790243BA8A83F691FE390487 = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_7859591D790243BA8A83F691FE390487 zorder zorder_rs_image_choice_7859591D790243BA8A83F691FE390487 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_34
    hide rs_image_choice_7859591D790243BA8A83F691FE390487
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"AYUMI\"" }]):
        jump block_000037E3
    if judge_lm_condition([]):
        jump block_000037EA

    return

label block_000037FB:
    # Node: 000037FB (7)
    $ sys_lm_choice_item = ["WALFS", "WOLPZ", "WOLPUS", "FOLFS", "WOLFZ", "WOLWZ", "WOLFS", "WOLWS"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_9E438EBC046644CDB494F8BECDE09F08 = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_9E438EBC046644CDB494F8BECDE09F08 zorder zorder_rs_image_choice_9E438EBC046644CDB494F8BECDE09F08 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_35
    hide rs_image_choice_9E438EBC046644CDB494F8BECDE09F08
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"WOLFS\"" }]):
        jump block_000037E3
    if judge_lm_condition([]):
        jump block_000037EA

    return

label block_000037FC:
    # Node: 000037FC (8)
    $ sys_lm_choice_item = ["WOPOS", "WALFZ", "WOPAS", "WOLAS", "WOPLS", "WALFS", "WOLPZ", "WOLFZ", "WOLFS", "WOLPS"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_C89809FD0CD949ACB4BEE0905CBA4A12 = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_C89809FD0CD949ACB4BEE0905CBA4A12 zorder zorder_rs_image_choice_C89809FD0CD949ACB4BEE0905CBA4A12 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_36
    hide rs_image_choice_C89809FD0CD949ACB4BEE0905CBA4A12
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"WOLFS\"" }]):
        jump block_000037E3
    if judge_lm_condition([]):
        jump block_000037EA

    return

label block_000037FD:
    # Node: 000037FD (9)
    $ sys_lm_choice_item = ["PRAECAHTATER", "PRAECAHTATOR", "PRAECANTATOR", "PRAECANTETOR", "PRAECENTATOR"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_8199EF66C19849CD9EFF10ED1ED5C376 = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_8199EF66C19849CD9EFF10ED1ED5C376 zorder zorder_rs_image_choice_8199EF66C19849CD9EFF10ED1ED5C376 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_37
    hide rs_image_choice_8199EF66C19849CD9EFF10ED1ED5C376
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"PRAECANTATOR\"" }]):
        jump block_000037E3
    if judge_lm_condition([]):
        jump block_000037EA

    return

label block_000037FE:
    # Node: 000037FE (10)
    $ sys_lm_choice_item = ["PRAECAHTATOR", "PRAECANTATOR", "PRAECENTATOR", "PREACANTATOR", "PRAECANTATER", "PRAECANTETER", "PRAEHANTATOR", "PRAECAHTOTER"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_F90A22B7C51046FA839D6A64AC122AAA = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_F90A22B7C51046FA839D6A64AC122AAA zorder zorder_rs_image_choice_F90A22B7C51046FA839D6A64AC122AAA onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_38
    hide rs_image_choice_F90A22B7C51046FA839D6A64AC122AAA
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"PRAECANTATOR\"" }]):
        jump block_000037E3
    if judge_lm_condition([]):
        jump block_000037EA

    return

label block_00002CCB:
    # Node: 00002CCB (Find 2 空)
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_4913C76A3FD641CBAFC2DC49CA8837AF as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么，头脑训练要开始了哦。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这次的训练是“{color=#0080FF}寻找正确选项{/color}”。\n不过，也要小心{color=#FF0000}时间限制{/color}哦。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "比上次要难很多，一定小心哦。{w}\n加油，准备——{w}开始！"

    window hide


    if judge_lm_condition([]):
        jump block_000037E7

    return

label block_00002A3D:
    # Node: 00002A3D (Find 2 月)
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_0305038F51BC401396154F294FEAA2E7 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的训练也是“{color=#0080FF}寻找正确选项{/color}”。\n然而，存在{color=#FF0000}时间限制{/color}。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "比上次要难得多，做好觉悟比较好。{w}\n那么，开始。"

    window hide


    if judge_lm_condition([]):
        jump block_000037E7

    return

label block_00002CD2:
    # Node: 00002CD2 (Number 2)
    $ TotalCount = 9

    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 2" }]):
        jump block_000032AC
    if judge_lm_condition([{ "scope": 0, "content": "TimeState == 1" }]):
        jump block_00002CCC
    if judge_lm_condition([]):
        jump block_00002990

    return

label block_000032AC:
    # Node: 000032AC (Number 2 冬)
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_0CBEE3104B544997B9F152690F79B463 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的任务是选择恰当的{color=#0080FF}数字{/color}。\n接下来会不断出现各种数字，尝试记住他们。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不用多说，难度肯定比上次高。{w}那么，开始。"

    window show


    if judge_lm_condition([]):
        jump block_00003813

    return

label block_00003813:
    # Node: 00003813 (Update)
    $ CurrentIndex = CurrentIndex + 1
    if CurrentIndex < 9:
        if TimeState == 2:
            show rs_image_62DDFA5A234046A99A6D1D7E88EA46C2 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        elif TimeState == 1:
            show rs_image_C33AC4318DF74FED80B18E300D08A925 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        else:
            show rs_image_5C82B57D70084E5EBD789404205EDC04 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop

        $ zorder_tag_348CF07D60744BC79223A712FCFA9BD9 = 400

        if CurrentIndex < 3:
            show rs_image_450E72BACA8C41E386BD3F2E287115E3 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
            with rs_effect_777EBB3BEF314C5187906634D1CE341E

            pause 0.5

        elif CurrentIndex < 6:
            show rs_image_6992278163DA45AE8B9F944BEE610150 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
            with rs_effect_777EBB3BEF314C5187906634D1CE341E

            pause 0.5

        else:
            show rs_image_317AE85C1BE748B89D08636A300C6541 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
            with rs_effect_777EBB3BEF314C5187906634D1CE341E

            pause 0.5


    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 0" }]):
        jump block_00002991
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 1" }]):
        jump block_00002998
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 2" }]):
        jump block_0000299C
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 3" }]):
        jump block_00002A31
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 4" }]):
        jump block_00002A33
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 5" }]):
        jump block_00002A39
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 6" }]):
        jump block_000029A8
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 7" }]):
        jump block_000029A1
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 8" }]):
        jump block_0000299E
    if judge_lm_condition([]):
        jump block_00003818

    return

label block_00002991:
    # Node: 00002991 (1)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}４{/size}{w=0.4}{size=32}０{/size}{w=0.4}{size=32}９{/size}{w=0.4}{size=32}３{/size}{w=0.4}{size=32}８{/size}{w=0.4}{size=32}７{/size}{w=0.4}{size=32}５{/size}{w=0.4}{size=32}２{/size}{w=0.4}{size=32}６{/size}{w=2.5}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_68975D5C597543F1B6B1FD797877D460 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002993

    return

label block_00002993:
    # Node: 00002993 (1)
    $ sys_lm_choice_item = ["０", "７", "２", "１"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_39
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"１\"" }]):
        jump block_00003801
    if judge_lm_condition([]):
        jump block_00003816

    return

label block_00003801:
    # Node: 00003801 (對)
    play effect "sound/Effect Sound/Correct 1.ogg" noloop

    show rs_image_0C55A05D870D4AFD8FA6561C542AEB06 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if TimeState == 2:
        show rs_image_2594659CB59F456896B2EF27AD70323C as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "干得好！"

    elif TimeState == 1:
        show rs_image_7E2778FA3D624F319D303738D4143BE5 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "非常好哦！"
    else:
        show rs_image_CA7FB6339967475B8EDC72EB94052C60 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        
        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "干得好！"
    
    window hide

    $ CorrectCount = CorrectCount + 1

    if judge_lm_condition([]):
        jump block_00003810

    return

label block_00003810:
    # Node: 00003810 (TO: Update)

    if judge_lm_condition([]):
        jump block_00003813

    return

label block_00003816:
    # Node: 00003816 (錯)
    play effect "sound/Effect Sound/Wrong 1.ogg" noloop

    show rs_image_4C358D6358994092B67D2FE620F9E858 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if TimeState == 2:
        show rs_image_89E17548BB5E44C3928F3166B177C150 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不行啊。"

    elif TimeState == 1:
        show rs_image_B63B525194554F0BBF36CCFF8577D5AC as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "好可惜。"
    else:
        show rs_image_5CE8CAA349B8484888F68CD67D37CBFD as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        
        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不行啊。"
    
    window hide

    if judge_lm_condition([]):
        jump block_00003817

    return

label block_00003817:
    # Node: 00003817 (TO: Update)

    if judge_lm_condition([]):
        jump block_00003813

    return

label block_00002998:
    # Node: 00002998 (2)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}４{/size}{w=0.4}{size=32}１{/size}{w=0.4}{size=32}３{/size}{w=0.4}{size=32}０{/size}{w=0.4}{size=32}５{/size}{w=0.4}{size=32}８{/size}{w=0.4}{size=32}９{/size}{w=0.4}{size=32}７{/size}{w=0.4}{size=32}２{/size}{w=2.5}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_68975D5C597543F1B6B1FD797877D460 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002995

    return

label block_00002995:
    # Node: 00002995 (2)
    $ sys_lm_choice_item = ["３", "６", "７", "９"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_40
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"６\"" }]):
        jump block_00003801
    if judge_lm_condition([]):
        jump block_00003816

    return

label block_0000299C:
    # Node: 0000299C (3)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}９{/size}{w=0.4}{size=32}３{/size}{w=0.4}{size=32}０{/size}{w=0.4}{size=32}５{/size}{w=0.4}{size=32}２{/size}{w=0.4}{size=32}４{/size}{w=0.4}{size=32}７{/size}{w=0.4}{size=32}５{/size}{w=0.4}{size=32}６{/size}{w=2.5}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_68975D5C597543F1B6B1FD797877D460 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002999

    return

label block_00002999:
    # Node: 00002999 (3)
    $ sys_lm_choice_item = ["４", "１", "２", "３"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_41
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"３\"" }]):
        jump block_00003801
    if judge_lm_condition([]):
        jump block_00003816

    return

label block_00002A31:
    # Node: 00002A31 (4)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}５{/size}{w=0.4}{size=32}９{/size}{w=0.4}{size=32}９{/size}{w=0.4}{size=32}４{/size}{w=0.4}{size=32}４{/size}{w=0.4}{size=32}５{/size}{w=0.4}{size=32}４{/size}{w=0.4}{size=32}９{/size}{w=3}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_1908B52A43414A2A93CEC7888568A43A as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002A32

    return

label block_00002A32:
    # Node: 00002A32 (4)
    $ sys_lm_choice_item = ["１", "２", "３", "４"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_42
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"２\"" }]):
        jump block_00003801
    if judge_lm_condition([]):
        jump block_00003816

    return

label block_00002A33:
    # Node: 00002A33 (5)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}８{/size}{w=0.4}{size=32}６{/size}{w=0.4}{size=32}２{/size}{w=0.4}{size=32}４{/size}{w=0.4}{size=32}６{/size}{w=0.4}{size=32}２{/size}{w=0.4}{size=32}７{/size}{w=0.4}{size=32}８{/size}{w=0.4}{size=32}２{/size}{w=3}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_BA3A35B15B3642E296E0A438FB0CE11A as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002A34

    return

label block_00002A34:
    # Node: 00002A34 (5)
    $ sys_lm_choice_item = ["１", "２", "３", "４"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_43
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"１\"" }]):
        jump block_00003801
    if judge_lm_condition([]):
        jump block_00003816

    return

label block_00002A39:
    # Node: 00002A39 (6)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}{color=#008000}５{/color}{/size}{w=0.4}{size=32}{color=#FF8000}２{/color}{/size}{w=0.4}{size=32}{color=#FF0000}９{/color}{/size}{w=0.4}{size=32}{color=#0000FF}５{/color}{/size}{w=0.4}{size=32}{color=#FFFF00}２{/color}{/size}{w=0.4}{size=32}{color=#008000}９{/color}{/size}{w=0.4}{size=32}{color=#FF8040}５{/color}{/size}{w=0.4}{size=32}１{/size}{w=0.4}{size=32}{color=#0000FF}９{/color}{/size}{w=3}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_78B83B4A2F2E4E9C9E00870B7C567047 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002A3B

    return

label block_00002A3B:
    # Node: 00002A3B (6)
    $ sys_lm_choice_item = ["１", "２", "３", "４"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_44
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"２\"" }]):
        jump block_00003801
    if judge_lm_condition([]):
        jump block_00003816

    return

label block_000029A8:
    # Node: 000029A8 (7)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}{color=#FF0000}９{/color}{/size}{w=0.4}{size=32}８{/size}{w=0.4}{size=32}{color=#0000FF}７{/color}{/size}{w=0.4}{size=32}６{/size}{w=0.4}{size=32}{color=#008000}５{/color}{/size}{w=0.4}{size=32}４{/size}{w=0.4}{size=32}{color=#FFFF00}３{/color}{/size}{w=0.4}{size=32}２{/size}{w=0.4}{size=32}{color=#FF8040}１{/color}{/size}{w=0.4}{size=32}０{/size}{w=3}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_DB5EC36E01C647DC96B9407DD2D3B764 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_000029A5

    return

label block_000029A5:
    # Node: 000029A5 (7)
    $ sys_lm_choice_item = ["绿色", "白色", "粉色", "橘色"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_45
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"白色\"" }]):
        jump block_00003801
    if judge_lm_condition([]):
        jump block_00003816

    return

label block_000029A1:
    # Node: 000029A1 (8)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}{color=#008000}０{/color}{/size}{w=0.4}{size=32}{color=#0000FF}１{/color}{/size}{w=0.4}{size=32}{color=#008000}２{/color}{/size}{w=0.4}{size=32}{color=#0000FF}３{/color}{/size}{w=0.4}{size=32}{color=#FFFF00}４{/color}{/size}{w=0.4}{size=32}{color=#FF0000}５{/color}{/size}{w=0.4}{size=32}{color=#FFFF00}６{/color}{/size}{w=0.4}{size=32}{color=#FF0000}７{/color}{/size}{w=0.4}{size=32}{color=#FF8000}８{/color}{/size}{w=0.4}{size=32}{color=#FF8000}９{/color}{/size}{w=3}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_B43ACF55F9A049D5BE9D6F41AD95DD06 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_0000299F

    return

label block_0000299F:
    # Node: 0000299F (8)
    $ sys_lm_choice_item = ["红色", "黄色", "紫色", "白色"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_46
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"红色\"" }]):
        jump block_00003801
    if judge_lm_condition([]):
        jump block_00003816

    return

label block_0000299E:
    # Node: 0000299E (9)
    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}{color=#FFFF00}０{/color}{/size}{w=0.4}{size=32}{color=#C0C0C0}７{/color}{/size}{w=0.4}{size=32}{color=#FF0000}２{/color}{/size}{w=0.4}{size=32}{color=#800080}１{/color}{/size}{w=0.4}{size=32}{color=#FF00FF}８{/color}{/size}{w=0.4}{size=32}{color=#008000}０{/color}{/size}{w=0.4}{size=32}{color=#FF8000}１{/color}{/size}{w=0.4}{size=32}{color=#00FFFF}４{/color}{/size}{w=0.4}{size=32}{color=#008000}５{/color}{/size}{w=0.4}{size=32}４{/size}{w=0.4}{size=32}{color=#0000FF}５{/color}{/size}{w=3}{nw}"
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_C5134219762B4D2FA324A911DD3C178C as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.5


    if judge_lm_condition([]):
        jump block_0000299D

    return

label block_0000299D:
    # Node: 0000299D (9)
    $ sys_lm_choice_item = ["蓝色", "橘色", "粉色", "灰色", "白色", "黄色", "绿色"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_47
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"粉色\"" }]):
        jump block_00003801
    if judge_lm_condition([]):
        jump block_00003816

    return

label block_00003818:
    # Node: 00003818 (TO: Result)

    if judge_lm_condition([]):
        jump block_000037B2

    return

label block_00002CCC:
    # Node: 00002CCC (Number 2 空)
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_4913C76A3FD641CBAFC2DC49CA8837AF as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么，头脑训练要开始了哦。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这次的任务是选择恰当的{color=#0080FF}数字{/color}。\n接下来会不断出现各种数字，请试着记住他们。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "请注意比上次要难了一些哦。准备——{w}开始！"

    window show


    if judge_lm_condition([]):
        jump block_00003813

    return

label block_00002990:
    # Node: 00002990 (Number 2 月)
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_0305038F51BC401396154F294FEAA2E7 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的任务是选择恰当的{color=#0080FF}数字{/color}。\n接下来会不断出现各种数字，尝试记住他们。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不用多说，难度肯定比上次高。{w}那么，开始。"

    window show


    if judge_lm_condition([]):
        jump block_00003813

    return

label block_00002CD3:
    # Node: 00002CD3 (Find 3)
    $ TotalCount = 10

    if judge_lm_condition([{ "scope": 0, "content": "TimeState== 2" }]):
        jump block_000032AE
    if judge_lm_condition([{ "scope": 0, "content": "TimeState== 1" }]):
        jump block_00002CCD
    if judge_lm_condition([]):
        jump block_0000296B

    return

label block_000032AE:
    # Node: 000032AE (Find 3 冬)
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_0CBEE3104B544997B9F152690F79B463 as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那么，接下来开始头脑训练。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的训练仍然是“{color=#0080FF}寻找正确选项{/color}”。\n然而，存在{color=#FF0000}时间限制{/color}。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的非常困难，一定要好好努力。{w}\n那么，开始。"

    window hide


    if judge_lm_condition([]):
        jump block_00003833

    return

label block_00003833:
    # Node: 00003833 (Update)
    $ CurrentIndex = CurrentIndex + 1
    if CurrentIndex < 10:
        if TimeState == 2:
            show rs_image_62DDFA5A234046A99A6D1D7E88EA46C2 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        elif TimeState == 1:
            show rs_image_C33AC4318DF74FED80B18E300D08A925 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C
        else:
            show rs_image_5C82B57D70084E5EBD789404205EDC04 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
            with rs_effect_29912DDD51A1413D8CA4C0208EECE15C

    $ zorder_tag_348CF07D60744BC79223A712FCFA9BD9 = 400

    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 0" }]):
        jump block_00002A1C
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 1" }]):
        jump block_00002A20
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 2" }]):
        jump block_00002A23
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 3" }]):
        jump block_0000296E
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 4" }]):
        jump block_0000297F
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 5" }]):
        jump block_00002980
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 6" }]):
        jump block_00002981
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 7" }]):
        jump block_00002971
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 8" }]):
        jump block_00002983
    if judge_lm_condition([{ "scope": 0, "content": "CurrentIndex == 9" }]):
        jump block_00002982
    if judge_lm_condition([]):
        jump block_00003834

    return

label block_00002A1C:
    # Node: 00002A1C (1)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_22D773B0F8354CDAA23994409E496E01 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    pause 0.5

    if judge_lm_condition([]):
        jump block_00002A19

    return

label block_00002A19:
    # Node: 00002A19 (1)
    $ sys_lm_choice_item = ["ユフヒ", "ユウピ", "ユウヒ", "ヱウヒ"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_05F5027EB878467AA1394A4C55048F4B = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_05F5027EB878467AA1394A4C55048F4B zorder zorder_rs_image_choice_05F5027EB878467AA1394A4C55048F4B onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_48
    hide rs_image_choice_05F5027EB878467AA1394A4C55048F4B
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ユウヒ\"" }]):
        jump block_0000381D
    if judge_lm_condition([]):
        jump block_00003831

    return

label block_0000381D:
    # Node: 0000381D (對)
    play effect "sound/Effect Sound/Correct 1.ogg" noloop

    show rs_image_0C55A05D870D4AFD8FA6561C542AEB06 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if TimeState == 2:
        show rs_image_2594659CB59F456896B2EF27AD70323C as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "干得好！"

    elif TimeState == 1:
        show rs_image_7E2778FA3D624F319D303738D4143BE5 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "非常好哦！"
    else:
        show rs_image_CA7FB6339967475B8EDC72EB94052C60 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        
        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "干得好！"
    
    window hide

    $ CorrectCount = CorrectCount + 1

    if judge_lm_condition([]):
        jump block_0000382E

    return

label block_0000382E:
    # Node: 0000382E (TO: Update)

    if judge_lm_condition([]):
        jump block_00003833

    return

label block_00003831:
    # Node: 00003831 (錯)
    play effect "sound/Effect Sound/Wrong 1.ogg" noloop

    show rs_image_4C358D6358994092B67D2FE620F9E858 as tag_348CF07D60744BC79223A712FCFA9BD9 zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    if TimeState == 2:
        show rs_image_89E17548BB5E44C3928F3166B177C150 as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不行啊。"

    elif TimeState == 1:
        show rs_image_B63B525194554F0BBF36CCFF8577D5AC as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

        window show

        rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "好可惜。"
    else:
        show rs_image_5CE8CAA349B8484888F68CD67D37CBFD as tag_31FEF114566B4AB483D935C987B9E096 zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
        with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F
        
        window show

        rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不行啊。"
    
    window hide

    if judge_lm_condition([]):
        jump block_00003832

    return

label block_00003832:
    # Node: 00003832 (TO: Update)

    if judge_lm_condition([]):
        jump block_00003833

    return

label block_00002A20:
    # Node: 00002A20 (2)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_8E82228C596D439B883A659987F31545 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002A1D

    return

label block_00002A1D:
    # Node: 00002A1D (2)
    $ sys_lm_choice_item = ["胡", "朝", "期", "朔"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_5AED53E5C866490386DC5B71E2D52A3E = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_5AED53E5C866490386DC5B71E2D52A3E zorder zorder_rs_image_choice_5AED53E5C866490386DC5B71E2D52A3E onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_49
    hide rs_image_choice_5AED53E5C866490386DC5B71E2D52A3E
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"朔\"" }]):
        jump block_0000381D
    if judge_lm_condition([]):
        jump block_00003831

    return

label block_00002A23:
    # Node: 00002A23 (3)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_2D8BF86857164020A9EAB9FB12589221 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002A21

    return

label block_00002A21:
    # Node: 00002A21 (3)
    $ sys_lm_choice_item = ["滑子老师", "骨子老师", "滑了老师", "滑子老帅"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_2F9265ED7DF4442EB836548A5709F60F = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_2F9265ED7DF4442EB836548A5709F60F zorder zorder_rs_image_choice_2F9265ED7DF4442EB836548A5709F60F onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_50
    hide rs_image_choice_2F9265ED7DF4442EB836548A5709F60F
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"滑子老师\"" }]):
        jump block_0000381D
    if judge_lm_condition([]):
        jump block_00003831

    return

label block_0000296E:
    # Node: 0000296E (4)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_7602EA7D281E4A2E85C6C66CC4B8E2F8 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002972

    return

label block_00002972:
    # Node: 00002972 (4)
    $ sys_lm_choice_item = ["林森友", "森梅友", "森海反", "森海友"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_0639AB2BA95B401492A391200C78B011 = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_0639AB2BA95B401492A391200C78B011 zorder zorder_rs_image_choice_0639AB2BA95B401492A391200C78B011 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_51
    hide rs_image_choice_0639AB2BA95B401492A391200C78B011
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"森海友\"" }]):
        jump block_0000381D
    if judge_lm_condition([]):
        jump block_00003831

    return

label block_0000297F:
    # Node: 0000297F (5)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_850A05AF50FD449E9FCA0E4EAFC4C81E as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002973

    return

label block_00002973:
    # Node: 00002973 (5)
    $ sys_lm_choice_item = ["绫頼しのぶ", "绫濑しのぶ", "绫濑しのぷ", "绫濑じのぶ", "绫濑しのふ"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_7D8CAF2A55254ACCB78885F032F5A078 = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_7D8CAF2A55254ACCB78885F032F5A078 zorder zorder_rs_image_choice_7D8CAF2A55254ACCB78885F032F5A078 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_52
    hide rs_image_choice_7D8CAF2A55254ACCB78885F032F5A078
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"绫濑しのぶ\"" }]):
        jump block_0000381D
    if judge_lm_condition([]):
        jump block_00003831

    return

label block_00002980:
    # Node: 00002980 (6)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_7611B06CA5B34E45B2DA09E11B45FC58 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002974

    return

label block_00002974:
    # Node: 00002974 (6)
    $ sys_lm_choice_item = ["二之濑つばさ", "一之濑つはさ", "一之頼つばさ", "一之濑つばさ", "三之濑つばさ", "一之濑つぱさ"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_E348662588A3474894C1141AE69BBD1D = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_E348662588A3474894C1141AE69BBD1D zorder zorder_rs_image_choice_E348662588A3474894C1141AE69BBD1D onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_53
    hide rs_image_choice_E348662588A3474894C1141AE69BBD1D
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"一之濑つばさ\"" }]):
        jump block_0000381D
    if judge_lm_condition([]):
        jump block_00003831

    return

label block_00002981:
    # Node: 00002981 (7)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_4058FB9489B7472193678C5B76FF8BCD as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002975

    return

label block_00002975:
    # Node: 00002975 (7)
    $ sys_lm_choice_item = ["奥村真太郎", "奥材慎太郎", "奥村慎大朗", "奥村慎太朗", "奥村慎犬郎", "奥村慎太郎", "奥村清太郎"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_03718855072C40A182512A8F05E99B14 = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_03718855072C40A182512A8F05E99B14 zorder zorder_rs_image_choice_03718855072C40A182512A8F05E99B14 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_54
    hide rs_image_choice_03718855072C40A182512A8F05E99B14
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"奥村慎太郎\"" }]):
        jump block_0000381D
    if judge_lm_condition([]):
        jump block_00003831

    return

label block_00002971:
    # Node: 00002971 (8)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_49B9A509A95847ED97C21C7BF4C2068F as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002977

    return

label block_00002977:
    # Node: 00002977 (8)
    $ sys_lm_choice_item = ["穂梅作哉", "补海作哉", "穂海昨哉", "穂海作哉", "穂海乍哉", "穂悔作哉", "穂侮作哉"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_E9C37A1566994DC69FCAFD1B6F810616 = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_E9C37A1566994DC69FCAFD1B6F810616 zorder zorder_rs_image_choice_E9C37A1566994DC69FCAFD1B6F810616 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_55
    hide rs_image_choice_E9C37A1566994DC69FCAFD1B6F810616
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"穂海作哉\"" }]):
        jump block_0000381D
    if judge_lm_condition([]):
        jump block_00003831

    return

label block_00002983:
    # Node: 00002983 (9)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_7FFD4D8519BF4BF7A822FA32E2ABE7B6 as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    pause 0.5


    if judge_lm_condition([]):
        jump block_0000297A

    return

label block_0000297A:
    # Node: 0000297A (9)
    $ sys_lm_choice_item = ["猫山三郎", "猫山三朗", "猫川三朗", "猫山二朗", "猫山三郞", "描山三朗", "苗山三朗"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_C0A569E0CF1349E8A2AA1379F8B7BB2B = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_C0A569E0CF1349E8A2AA1379F8B7BB2B zorder zorder_rs_image_choice_C0A569E0CF1349E8A2AA1379F8B7BB2B onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_56
    hide rs_image_choice_C0A569E0CF1349E8A2AA1379F8B7BB2B
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"猫山三朗\"" }]):
        jump block_0000381D
    if judge_lm_condition([]):
        jump block_00003831

    return

label block_00002982:
    # Node: 00002982 (10)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    show rs_image_9A9723751F1A41DA806AA4FAF61DE1AB as tag_348CF07D60744BC79223A712FCFA9BD9 at center_bottom zorder zorder_tag_348CF07D60744BC79223A712FCFA9BD9 onlayer master
    with rs_effect_777EBB3BEF314C5187906634D1CE341E

    pause 0.5


    if judge_lm_condition([]):
        jump block_0000297E

    return

label block_0000297E:
    # Node: 0000297E (10)
    $ sys_lm_choice_item = ["赤峰空", "赤蜂空", "赤峰究", "赤峰月", "赤锋空", "赤烽空", "亦峰空", "赤峰突", "赤逢空", "赤俸空"]
    $ random.shuffle(sys_lm_choice_item)
    $ sys_lm_choice_sound = {}
    $ zorder_rs_image_choice_A32E0D211BE24DD59D34DEB433431636 = 10000
    show rs_image_6C86822B75984401BA6BA0B58A7D6CA5 as rs_image_choice_A32E0D211BE24DD59D34DEB433431636 zorder zorder_rs_image_choice_A32E0D211BE24DD59D34DEB433431636 onlayer master
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 3.3333333333333335) from _call_lm_choice_57
    hide rs_image_choice_A32E0D211BE24DD59D34DEB433431636
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"赤峰空\"" }]):
        jump block_0000381D
    if judge_lm_condition([]):
        jump block_00003831

    return

label block_00003834:
    # Node: 00003834 (TO: Result)

    if judge_lm_condition([]):
        jump block_00003818

    return

label block_00002CCD:
    # Node: 00002CCD (Find 3 空)
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_31FEF114566B4AB483D935C987B9E096 = 300
    show rs_image_4913C76A3FD641CBAFC2DC49CA8837AF as tag_31FEF114566B4AB483D935C987B9E096 at center_bottom zorder zorder_tag_31FEF114566B4AB483D935C987B9E096 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那么，头脑训练要开始了哦。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这次的训练是“{color=#0080FF}寻找正确选项{/color}”。\n不过，也要小心{color=#FF0000}时间限制{/color}哦。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这次的非常困难，请一定要注意。{w}\n加油，准备——{w}开始！"

    window hide


    if judge_lm_condition([]):
        jump block_00003833

    return

label block_0000296B: