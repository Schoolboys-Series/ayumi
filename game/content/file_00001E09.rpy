# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00001E09 (CP3 Twilight 月空友)

label block_00001E0A:
    # Node: 00001E0A (開始)
    $ TalkSakuyaMatsutaF6 = False
    $ TalkItouKimuraF6 = False
    $ TalkIzumiNakayamaF6 = False
    $ TalkShinobuF6 = False
    $ TalkKatouF6 = False
    $ TalkTsubasaF6 = False
    $ TalkSabuShinF6 = False

    if judge_lm_condition([]):
        jump block_00001E0C

    return

label block_00001E0C:
    # Node: 00001E0C (School outside)
    $ set_window("(標準)")
    if sys_music_current_file != "sound/BGM/My precious time of now.ogg":
        play music "sound/BGM/My precious time of now.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time of now.ogg"

    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title(False)
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_ayumi_global_map_character = "tsuki_sora_tomo_school"
    $ sys_ayumi_global_map_time = "twilight"

    if judge_lm_condition([]):
        jump block_00001E37

    return

label block_00001E37:
    # Node: 00001E37 (School outside XCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_outside", False, False, talk_label="block_00001E3A", target_label="block_00001E3B") from _call_scb_global_map_171
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館前\"" }]):
        jump block_00001E13
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" },{ "scope": 1, "content": "TalkSakuyaMatsutaF6 == False" }]):
        jump block_00001E54
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" },{ "scope": 1, "content": "TalkItouKimuraF6 == False" }]):
        jump block_00001E59
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" },{ "scope": 1, "content": "TalkSabuShinF6 and TalkTsubasaF6 and TalkKatouF6 and TalkShinobuF6 and TalkIzumiNakayamaF6 and TalkSakuyaMatsutaF6 and TalkItouKimuraF6 == True" }]):
        jump block_00001E5B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"下駄箱\"" }]):
        jump block_00001E12
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園内\"" }]):
        jump block_00001E0B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00001E3B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00001E37
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00001E3A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00001E37
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001F82
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"中庭\"" },{ "scope": 0, "content": "_lm_selected_value == \"校舎裏\"" }]):
        jump block_0000317C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校門\"" }]):
        jump block_000027F1

    return

label block_00001E13:
    # Node: 00001E13 (Gym outside)
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

    $ set_place_title(_("体育馆前"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1084DAF07A574EC18C0EDEF9E03F423C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001E1B

    return

label block_00001E1B:
    # Node: 00001E1B (Gym outside)
    $ sys_lm_menu_item = [{"pos": (168, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "体育館へ"}, {"pos": (664, 280),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "柔道場へ"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_733
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000424C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館へ\"" },{ "scope": 1, "content": "TalkIzumiNakayamaF6 == False" }]):
        jump block_00001E58
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"柔道場へ\"" }]):
        jump block_00001E3E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"体育館へ\"" }]):
        jump block_00001E53

    return

label block_0000424C:
    # Node: 0000424C (TO: School outside)

    if judge_lm_condition([]):
        jump block_0000424B

    return

label block_0000424B:
    # Node: 0000424B (TO: School outside)

    if judge_lm_condition([]):
        jump block_00001E0C

    return

label block_00001E58:
    # Node: 00001E58 (Gym)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ set_window("イベントモード")
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
    show rs_image_8EF7DA6C1A7E413ABBCA2ED9C5607E64 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8EF7DA6C1A7E413ABBCA2ED9C5607E64 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}一球切断！{/size}{w}\n{size=28}哦！！{/size}"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_73111533664E41C1A6D3DF6263EA7D68 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at right_top zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "前辈！！最后一球！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_02D8BA367982421D9C311E611AB26226 as tag_2F2406ABFD334A9FAFFFD526F608E209 at left_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A751683772E84A83B9CDA0EADC2D57CE "交给我！！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_E411FC07EE6847AEA19BD391EB91F5F0 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_66F6E7DB8C934D08BC4950E1F2E03C6A as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=36}攻击！！！{/size}"

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.3

    rs_character_A751683772E84A83B9CDA0EADC2D57CE "好！！"

    rs_character_8D9249CA1389416BAF6A122851E276D0 "很棒哦！！前辈！！"

    show rs_image_0102266CD54340CC87D5BB21C7BF9EE8 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A751683772E84A83B9CDA0EADC2D57CE "还是多亏了翔的托球啊，不愧是。\n我打起来最容易的位置球就一直在那里。"

    show rs_image_46EC9099511E4845AD599DD55A9A3DB2 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "哈哈，以后也会为了让前辈打起来更容易多加练习的。"

    show rs_image_BB9A4D78B92244598FD49D2FEECA3896 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A751683772E84A83B9CDA0EADC2D57CE "嗯，我会期待的！"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 200
    show rs_image_8ECC49973C11442A962560B3A4F31542 as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "……"

    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_1084DAF07A574EC18C0EDEF9E03F423C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D81691F1A7F841C4BE6CB3D91B4665C7 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_3BC0411E559D49E38A86F531E7DC85FF

    pause 0.3

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "排球中团队合作是必不可少的。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "单人是不可能完成整个攻击流程的。很不错。"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF


    if judge_lm_condition([]):
        jump block_00003178

    return

label block_00003178:
    # Node: 00003178 (T ++)
    $ TalkIzumiNakayamaF6 = True

    if judge_lm_condition([]):
        jump block_0000424D

    return

label block_0000424D:
    # Node: 0000424D (TO: School outside)

    if judge_lm_condition([]):
        jump block_0000424C

    return

label block_00001E3E:
    # Node: 00001E3E (Judo)
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

    $ set_place_title(_("柔道场"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4A952CA4817E4CAF8759947AF056AFFB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001E40

    return

label block_00001E40:
    # Node: 00001E40 (Judo)
    $ sys_lm_menu_item = [{"pos": (312, 280),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_734
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001E13
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" },{ "scope": 1, "content": "TalkShinobuF6 == False" }]):
        jump block_00001E57
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_0000317E

    return

label block_00001E57:
    # Node: 00001E57 (Judo)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ set_window("イベントモード")
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
    show rs_image_59836EDB597846F2A2C0A683B909166F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_245E81919395436088F3AAD2288945FC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "呼……"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 200
    show rs_image_4AB46F193DCB4AA8AA203C4685E658D8 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at right_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    rs_character_D34F60C882F0425E93252349E8C3BC8D "前辈好像有些累了呐。要不要休息一下？"

    show rs_image_72FEE9FEDE554732A906F7E56D61283D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸，有吗？那就很难集中精神了呢，\n我先去洗个脸再回来练习。"

    show rs_image_461F07A09F944E20832D4FE21024D6E5 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "好的，我明白了！"

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 200
    show rs_image_4AB46F193DCB4AA8AA203C4685E658D8 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at center_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_174D79C3A78E4614A51BFD2F8EDAB6F5 "绫濑前辈的毅力好强……\n每天早上好像都会加练的样子。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_1A07E2A402C04AB29AB5BB32DC2F26B6 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "但正因为什么都不说才更加伟大！！\n我也要朝着那种方向努力！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_4A952CA4817E4CAF8759947AF056AFFB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_FFC620A1302E417EBD9CB71C6CDE9274

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍的晨练原来是自己加的啊……"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "绫濑君的练习量可是非常惊人的，连我都自愧不如。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "正是。回家后我们也要加强练习。"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF


    if judge_lm_condition([]):
        jump block_00003179

    return

label block_00003179:
    # Node: 00003179 (T ++)
    $ TalkShinobuF6 = True

    if judge_lm_condition([]):
        jump block_0000424D

    return

label block_0000317E:
    # Node: 0000317E (Abandon)
    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "没必要再回到这里了。"

    window hide


    if judge_lm_condition([]):
        jump block_00001E40

    return

label block_00001E53:
    # Node: 00001E53 (Abandon)
    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "没必要再回到这里了。"

    window hide


    if judge_lm_condition([]):
        jump block_00001E1B

    return

label block_00001E54:
    # Node: 00001E54 (Atrium)
    $ set_window("イベントモード")
    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_819903C0E7144FDDADE04672BA6B63AE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 200
    show rs_image_CB9A767748514086B206A416DC2F4F21 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_6B92563C627F4FB7AD493644CEE2A9FF as tag_724406A84D7141298EFF0D864FAE1534 at left_top zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "这次一定要给SUMIRE学园那些家伙点颜色看。\n上次只是侥幸胜利就翘得上天……"

    show rs_image_9BFF07F6F66B427BA0660B3CACAB82E5 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "可三号射手猫山已经走了，从外侧的进攻会很难……\n不想个方案的话。"

    show rs_image_4E8D8D71098A481FA26474FD3AB0B4A6 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "是啊……"
    show rs_image_EA92771579CF44E69B0D1339C604BE30 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "混蛋，那只笨猫，突然就要退部……"

    show rs_image_A2B49B3B262A404DB416A6619C0479DF as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "怎么？寂寞了？作酱♪"

    show rs_image_ABCDB84A85954DBE9B12EF56BA5AFBFF as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "恶！！谁会对那种家伙！{w}\n{nw}"
    show rs_image_0BB48545B9A64D38B2802E4FAFC7EEB6 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "还有听着很恶心别再用那家伙的语气说话了！"

    show rs_image_DBB810C4B9C249FBB373B3C6FC840FD3 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "真是的"
    show rs_image_3B8B95D3CF0846B0ADA81E6C2C640219 as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……寂寞的作君身边还有我哦，安心就好。"

    show rs_image_ABCDB84A85954DBE9B12EF56BA5AFBFF as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你管的太多了！"
    show rs_image_848FD89B9ABB4814BD710E90E77C9549 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "休息结束，回去了松田！\n绝对要把那群人打倒！！"

    show rs_image_A2B49B3B262A404DB416A6619C0479DF as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "哦。"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_724406A84D7141298EFF0D864FAE1534
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.8

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_FE681BB78F1F4D339A2566A5D9707982 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "篮球部的各位气势很高呐～"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "下周就有练习比赛，肯定想再加把劲吧。"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF


    if judge_lm_condition([]):
        jump block_00003175

    return

label block_00003175:
    # Node: 00003175 (T ++)
    $ TalkSakuyaMatsutaF6 = True

    if judge_lm_condition([]):
        jump block_0000424C

    return

label block_00001E59:
    # Node: 00001E59 (Schoolhouse)
    $ set_window("イベントモード")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title(False)
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_51A12E9EAB2B492E9FD30BC2C01A5C1B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    show rs_image_817AA9F7C79C4F26B2EBFB6B1B35A678 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_8E7F54C178A24E3A8D6E1F82AE74FB00 as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呐，我今天可是非常努力了啊，\n给点奖励好不好，伊藤。"

    show rs_image_A3C244E638B14C1D8D471099D0041B0E as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_710A38AC94C841779DB701B5AC1010FD "唔，我、我明白了。可是，一开始是……！"

    if sys_effect2_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 0.3

    rs_character_E3F6ADD43DE44A428E1224756613C694 "知道了，从{color=#FF00FF}亲吻{/color}开始？{w}伊藤……"

    rs_character_710A38AC94C841779DB701B5AC1010FD "木村……"

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_B550C4E9D1DB474BBEDD133EA85FDFC5 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_9D80F5870F2249459239D301CED743C6 as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这个不对。去别的地方。"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B550C4E9D1DB474BBEDD133EA85FDFC5 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_9D80F5870F2249459239D301CED743C6 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_D8FBA8060A9B457F9D8A35FB71E72F10 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！那两个人要做吗！！？\n感觉不错！再让我多看看！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_FE681BB78F1F4D339A2566A5D9707982 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不可，走了。"

    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎么可以……"

    window hide

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.6

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF


    if judge_lm_condition([]):
        jump block_00003176

    return

label block_00003176:
    # Node: 00003176 (T ++)
    $ TalkItouKimuraF6 = True

    if judge_lm_condition([]):
        jump block_0000424C

    return

label block_00001E5B:
    # Node: 00001E5B (School door 2)
    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title(False)
    with rs_effect_E6A0D20A1A914A0CBCF8DCED075CD75A

    $ set_window("イベントモード")
    pause 3

    show rs_image_28CB16F81175458EA97C8F0250448304 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C3AC3BC102640A98B0B848A29849370

    pause 2

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_D81691F1A7F841C4BE6CB3D91B4665C7 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_F95856ACBC5A49B2B61D4DBB1E7B4294 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 0.8

    window show

    if sys_music_current_file != "sound/BGM/Lively twilight.ogg":
        play music "sound/BGM/Lively twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Lively twilight.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"

    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "如何？森海。看到大家的样子，有什么感想？"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "大家都很厉害。{w}\n{nw}"
    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "感觉……{w=0.55}{nw}"
    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "想要做些什么……"

    show rs_image_5123C7F475964032872A280F4A7CF163 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "用尽全力做某事的时候大多是无自觉的，但也魅力四射。"

    show rs_image_BDC291B5081C42168C8A1886FB5FACD3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "一定，今后森海也会是这种样子。\n现在，目标就在那里，而你有需要去做的事。"

    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……我也想像那样努力。现在也非常想去社团……"

    show rs_image_D6385A1D6C184F9A93FE94370445F27F as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "就是这股气势！肯定吹奏乐部的大家也是这么想的。"

    show rs_image_A52160C305F54813BC6542DBBC09E25D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "下次带着这种想法参加社团活动，\n应该就不会再觉得自己格格不入了。"

    show rs_image_D81691F1A7F841C4BE6CB3D91B4665C7 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "为了不忘掉现在的心情，适当自恋一下也是个方法。"

    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！？自恋？就是说要喜欢上自己？？"

    show rs_image_12471979B7D1437085FB86AB6EEB1E51 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "对。要觉得正在努力的自己很帅气，要为自己陶醉。"

    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "因为不论何时，自己的身边都一定会有自己存在。\n这就意味着不可能没有盟友。"

    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦哦……！！感觉多了一个好强大的盟友呐！{w}\n{nw}"
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "谢谢。明天我会试试的！！"

    show rs_image_C989D2B8472147EBAAC08D14FF060BEC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯！加油哦！友君！"

    show rs_image_12471979B7D1437085FB86AB6EEB1E51 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空，我们也不能输给森海。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_34E241C96D16409BBECDFE411E12F665 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好——的！！那么三人一起鼓起勇气！喊出来！"

    window hide

    pause 0.5

    # Gallery unlock: images/CG/Revolution-march/Revolution-march 5.png
    $ zorder_rs_image_03063425963043719D0E021E3257FDBB = -100
    show rs_image_03063425963043719D0E021E3257FDBB as rs_image_03063425963043719D0E021E3257FDBB zorder zorder_rs_image_03063425963043719D0E021E3257FDBB onlayer master
    hide rs_image_03063425963043719D0E021E3257FDBB

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_03063425963043719D0E021E3257FDBB as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 1

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "一、二——！！加油！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=36}哦——！！！{/size}"

    window hide

    pause 1.5

    show rs_image_AFACE878401B4E26BE0872550A11D696 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    stop music fadeout 5
    $ sys_music_current_file = ""

    pause 3.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_B6D2CFDC1CB5407EACD7FBC1D100D198

    pause 4


    if judge_lm_condition([]):
        jump block_00004247

    return

label block_00004247:
    # Node: 00004247 ()
    $ del TalkSakuyaMatsutaF6
    $ del TalkItouKimuraF6
    $ del TalkIzumiNakayamaF6
    $ del TalkShinobuF6
    $ del TalkKatouF6
    $ del TalkTsubasaF6
    $ del TalkSabuShinF6

    return

label block_00001E12:
    # Node: 00001E12 (Shoe cupboard)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("鞋箱"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E9592A382F574338BCE51B690BEBEF00 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001E1A

    return

label block_00001E1A:
    # Node: 00001E1A (Shoe cupboard)
    $ sys_lm_menu_item = [{"pos": (160, 96),"image": "images/Menu/Nameko.png","hover": "images/Menu/Nameko hover.png","name": "滑子"}, {"pos": (672, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "校庭へ行く"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_735
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000424C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校庭へ行く\"" },{ "scope": 1, "content": "TalkKatouF6 == False" }]):
        jump block_00001E56
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"滑子\"" }]):
        jump block_00001E5D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"校庭へ行く\"" }]):
        jump block_0000317F

    return

label block_00001E56:
    # Node: 00001E56 (Playground)
    $ set_window("イベントモード")
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
    show rs_image_F6470A84AD8845BE97EAAA615A68C2F5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F6470A84AD8845BE97EAAA615A68C2F5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    window show

    rs_character_6A4C8856F501443E989BAF157EE55554 "下一轮！击球！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_3CB0A714815E467E9D3CF5E4373AC649 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_81D16F74A3C44B8982DB528D7D934850 "拜托了！！"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Baseball 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Baseball 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Baseball 1.ogg"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_A77C32C7E5794F80918CD998555CF13B as tag_61A891D6A6D047DC93695DA12E13CC75 at center_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_81D16F74A3C44B8982DB528D7D934850 "欸！！变、变化球……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_6A4C8856F501443E989BAF157EE55554 "发什么呆！都说了要击球了！！{w}\n再来一次！！看好～！"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Baseball 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Baseball 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Baseball 1.ogg"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    pause 0.4

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 200
    show rs_image_056F33630D5B4256B5C35361E58C2EB6 as tag_61A891D6A6D047DC93695DA12E13CC75 at center_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_81D16F74A3C44B8982DB528D7D934850 "呜哇……坏球……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    rs_character_6A4C8856F501443E989BAF157EE55554 "就算是坏球能出局也别不去接啊！！"

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_3CB0A714815E467E9D3CF5E4373AC649 as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "唔哦哦哦哦！！{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    rs_character_6A4C8856F501443E989BAF157EE55554 "欸欸看好——！！"

    pause 0.6

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_E9592A382F574338BCE51B690BEBEF00 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_B3256942BF0C4567BBE53ABE31023DE2 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_02ECE9B805B742C6B558DFD2FD5D2608 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.3

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "一会在投手板上，一会又飞到休息区，\n真是不得了的击球呐……"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不过，全都在千钧一发之际救下来了。也许只是偶然……"

    show rs_image_B550C4E9D1DB474BBEDD133EA85FDFC5 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那种场面一瞬的犹豫都会失败。\n某种意义上，非常接近正式比赛。"

    show rs_image_A51FC16534344AB291AA801BC1DAFEA2 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "棒球部的练习也很辛苦呐～……"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF


    if judge_lm_condition([]):
        jump block_0000317A

    return

label block_0000317A:
    # Node: 0000317A (T ++)
    $ TalkKatouF6 = True

    if judge_lm_condition([]):
        jump block_0000424D

    return

label block_00001E5D:
    # Node: 00001E5D (滑子)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_D7F70E4230154502BB28D6BA8AC09D91 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_bottom zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_7B5A8FFA4600478D826C2E4E4FAD069E as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "森海，身体没事了？"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，是的。感觉好多了。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9C78AB751CDB49FDA83251FA5B4A3825 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "这样啊。今天就好好休息。{w}\n各科的作业不想做就别做了，\n我会向老师们说明的。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真的！？太好了——♪♪{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_7B5A8FFA4600478D826C2E4E4FAD069E as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    extend "…………啊。"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8F48584787114538888D5C0B826EDE5F as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "这么有精神那就没问题了，作业还是要做……"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "咳、咳咳。{w}我会尽量的～……"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("中庭"))

    if judge_lm_condition([]):
        jump block_00001E1A

    return

label block_0000317F:
    # Node: 0000317F (Abandon)
    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "没必要再回到这里了。"

    window hide


    if judge_lm_condition([]):
        jump block_00001E1A

    return

label block_00001E0B:
    # Node: 00001E0B (School inside)
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title(False)
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_ayumi_global_map_character = "tsuki_sora_tomo_school"
    $ sys_ayumi_global_map_time = "twilight"

    if judge_lm_condition([]):
        jump block_00001E36

    return

label block_00001E36:
    # Node: 00001E36 (School inside XCTX)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "school_inside", False, False, talk_label="block_00001F1D", target_label="block_00001E4D") from _call_scb_global_map_172
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"廊下\"" }]):
        jump block_00001E0D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"屋上\"" }]):
        jump block_00001E0E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"音楽室\"" }]):
        jump block_00001E0F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" },{ "scope": 1, "content": "TalkTsubasaF6 == False" }]):
        jump block_00001E55
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"トイレ\"" }]):
        jump block_00001E11
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"学園外\"" }]):
        jump block_00001E0C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"放課後不可\"" }]):
        jump block_00001E36
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00001F1D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00001E4D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00001E36
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001F83
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"図書室\"" }]):
        jump block_00001E52

    return

label block_00001E0D:
    # Node: 00001E0D (Aisle 2)
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

    $ set_place_title(_("二楼走廊"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4B5F763E9F424591A5E354CF41830363 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001E17

    return

label block_00001E17:
    # Node: 00001E17 (廊下)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (152, 208),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "踊り場へ"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_736
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00004250
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"踊り場へ\"" },{ "scope": 1, "content": "TalkSabuShinF6 == False" }]):
        jump block_00001E5A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"踊り場へ\"" }]):
        jump block_0000317D

    return

label block_00004250:
    # Node: 00004250 (TO: School inside)

    if judge_lm_condition([]):
        jump block_0000424F

    return

label block_0000424F:
    # Node: 0000424F (TO: School inside)

    if judge_lm_condition([]):
        jump block_00001E0B

    return

label block_00001E5A:
    # Node: 00001E5A (Classroom)
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
    show rs_image_346C660582324EEE9245E6CC5D0DEE40 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_61DF088BB68345749E26C196F82492B4 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    window show

    show rs_image_E21ACD1443A4402AA37E7CE200FF6D4C as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊，等等！三酱，这里的字用粉色的！\n好不容易做个看板，要做到最好！"

    show rs_image_78AAFDF80423489CB9D3E414C6D0A594 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "欸？是么……\n我觉得花乃汤应该是那种深绿的感觉啊……"

    show rs_image_4BA562125E914D049B3A68EC3F0DB8A1 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "果然是吗……"
    show rs_image_AD906DE4351649D4A088A775E16D4592 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "好，这块看板就用来抹掉那种印象！"

    show rs_image_DEC2F822DD03433CB37D42439376833B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……还有啊，三酱。{w}\n{nw}"
    show rs_image_075F12352E04495CB718DBEB1B7D807C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_7B9421782EFE49138E5AADFCD59A037D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "现在，只有我们两个哦。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_17BD4756EE4547C7999FB0FE558D991B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "欸？嗯……算是。"

    show rs_image_A2E7C1AAED834AD7861668C6EE330F80 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那……一点点也好，稍微亲热一点，应该不会生气对不对？"

    show rs_image_23970544C9224BB4B785B8FB367471BC as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔……哦、哦……"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "姆呼呼～♪三～酱☆"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "等等！别捏那边！越线了……{w}{color=#FF00FF}啊///{/color}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_4EDED0024E6F4F5DB4944ED53F7CAD3C

    extend ""

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4B5F763E9F424591A5E354CF41830363 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_B3256942BF0C4567BBE53ABE31023DE2 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_B62939FE188646B19F924D8B074E376A as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊～真是的！明明到中间为止还很好的！！"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "森海，忘掉最后那部分，只记得前面努力工作那部分就好。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_11C6196C960646A1860CECE1AE21494F as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔哈～再来点再来点♪"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_89D53127B93243A194D7108DECE8802F as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_68A5D37E75C44024B6EB05C9646C1428 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君！不许看了！快走了！"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_A579F650612D4CA18E2B222221DBF547 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸欸欸！明明接下来就是最重要的时候了！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B62939FE188646B19F924D8B074E376A as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_889F2AF205E140788BE374915197CA80 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_71FE39D448264F1B86FB7E3459E84840 "不对！！！"

    window hide

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00003177

    return

label block_00003177:
    # Node: 00003177 (T ++)
    $ TalkSabuShinF6 = True

    if judge_lm_condition([]):
        jump block_00004250

    return

label block_0000317D:
    # Node: 0000317D (Abandon)
    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "没必要再回到这里了。"

    window hide


    if judge_lm_condition([]):
        jump block_00001E17

    return

label block_00001E0E:
    # Node: 00001E0E (Roof)
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

    $ set_place_title(_("屋顶"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C5A69FE639934E6FB6B6BCD7FD68AD03 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001E5C

    return

label block_00001E5C:
    # Node: 00001E5C (Empty)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_737
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00004250

    return

label block_00001E0F:
    # Node: 00001E0F (Music room)
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

    $ set_place_title(_("音乐室"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DA8B982D5B7A4579B98471DE18545375 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001E5C

    return

label block_00001E55:
    # Node: 00001E55 (Library)
    $ set_window("イベントモード")
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
    show rs_image_A96A942FC030416C8083CDFCFD593955 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_54984C82CD7C4D86A32BA7AFE5015CD1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……insulin deficiency can lead to diabetes and sometimes hypertension will……"

    rs_character_62D2A2AA61774A129B8EF3867F430DA8 "一之濑，最近经常看到你呢。可不要学习过头发烧哦。"

    show rs_image_F0AF18EA5ED94E6B9426EA7B01961357 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "谢、谢谢你担心。"
    show rs_image_E3D2D87C0D4C4A54B7016B01E2AC7D10 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "像我这样的新手\n这种程度刚刚好。哈哈……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_11EDEE45EEC54880894088C6FDDA3960 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_02AF4E98AE404A37BBF5189D1BD66AE6 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CB70B28808D840B5A51436CA4E858F49 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_FFC620A1302E417EBD9CB71C6CDE9274

    pause 0.3

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "一之濑最近每天放学后都会来学习呐。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "想要精通饲育，非常热心呢～真的很努力呐……"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF


    if judge_lm_condition([]):
        jump block_0000317B

    return

label block_0000317B:
    # Node: 0000317B (T ++)
    $ TalkTsubasaF6 = True

    if judge_lm_condition([]):
        jump block_00004250

    return

label block_00001E11:
    # Node: 00001E11 (Toilet)
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

    $ set_place_title(_("厕所"))
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_ACB3328CB0AC47999DDC17D52F9A104B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00001E5C

    return

label block_00001F1D:
    # Node: 00001F1D (Conversation)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "（……话说回来，\n今天突然要散步，到底怎么了？）"

    window hide

    $ set_window("(標準)")

    return

label block_00001E4D:
    # Node: 00001E4D (Target)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『在学校里散散步。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001F83:
    # Node: 00001F83 (Character)
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

label block_00001E52:
    # Node: 00001E52 (Abandon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "没必要再回到这里了。"

    window hide

    $ zorder_tag_521EB228B90943B3A2B33F87C47D3A0E = 200
    $ zorder_tag_88D3209FDD1D4A2E8369A5A61DF50852 = 400


    if judge_lm_condition([]):
        jump block_00001E0B

    return

label block_00001E3B:
    # Node: 00001E3B (Target)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    $ set_window("チャット")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『在学校里散散步。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001E3A:
    # Node: 00001E3A (Conversation)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("チャット")
    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说起来，今天体育课做什么了？"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "和二班的比赛。{w}\n因为是哥哥所以完全被对方挑衅了。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "当、当时别无选择。\n那个叫穗海的动不动就大放厥词……"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "算了，\n最后变成非常激烈的比赛了呐。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "倒不如说在我看来\n哥哥对他说的每句话都反应太过度了。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "普通看上去的话，\n作哉君是个好人哦？"

    rs_character_ADD720FBAC63461E98F721222823122D "不可能！！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不用这么同步……\n你们两个真是讲不通道理。"

    window hide

    $ set_window("(標準)")

    return

label block_00001F82:
    # Node: 00001F82 (Character)
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

label block_0000317C:
    # Node: 0000317C (Abandon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "没必要再回到这里了。"

    window hide

    $ zorder_tag_521EB228B90943B3A2B33F87C47D3A0E = 200
    $ zorder_tag_88D3209FDD1D4A2E8369A5A61DF50852 = 400


    if judge_lm_condition([]):
        jump block_0000424C

    return

label block_000027F1:
    # Node: 000027F1 (School door 1)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "友君，再多散散步如何。"

    window hide

    $ zorder_tag_521EB228B90943B3A2B33F87C47D3A0E = 200
    $ zorder_tag_88D3209FDD1D4A2E8369A5A61DF50852 = 400


    if judge_lm_condition([]):
        jump block_00001E0C

    return

