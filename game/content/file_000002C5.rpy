# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 000002C5 (CP1 作哉散歩)

label block_000002C6:
    # Node: 000002C6 (開始)

    if judge_lm_condition([]):
        jump block_0000366B

    return

label block_0000366B:
    # Node: 0000366B (TO: Misaki)

    if judge_lm_condition([]):
        jump block_0000366A

    return

label block_0000366A:
    # Node: 0000366A (TO: Misaki)

    if judge_lm_condition([]):
        jump block_000007F0

    return

label block_000007F0:
    # Node: 000007F0 (Misaki)
    $ set_window("(標準)")
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    $ set_place_title(False)
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_ayumi_global_map_character = "sakuya_tsubasachan"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([]):
        jump block_000007F1

    return

label block_000007F1:
    # Node: 000007F1 (Misaki XCTA)
    if judge_lm_condition([]) and judge_lm_condition([]):
        call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "misaki", False, True, talk_label="block_000007EE", target_label="block_000007EF") from _call_scb_global_map_14
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲学園\"" }]):
        jump block_000007F4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"住宅街\"" }]):
        jump block_000007F2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲駅\"" }]):
        jump block_00000836
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"商店街\"" }]):
        jump block_00000806
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"公園\"" }]):
        jump block_000007F5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"昼休み不可\"" }]):
        jump block_000007FA
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_000007EE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_000007EF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_00001FC6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00001FC9

    return

label block_000007F4:
    # Node: 000007F4 (School door)
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

    $ set_place_title(_("校门"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000007F3

    return

label block_000007F3:
    # Node: 000007F3 (School door)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_142
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000007F0

    return

label block_000007F2:
    # Node: 000007F2 (Residential street)
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

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D7154940FF02439388BA1F87BDD543E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C1S4Phase == 1" }]):
        jump block_00000801
    if judge_lm_condition([]):
        jump block_000007F7

    return

label block_00000801:
    # Node: 00000801 (F4: 四朗)
    pause 0.5

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "{size=36}穗海前辈——！！！{/size}"

    window hide

    pause 0.8

    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 0.8

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 9.png
    $ zorder_rs_image_ADFD6891D3AF42CA8301DDC64AE2F5D7 = -100
    show rs_image_ADFD6891D3AF42CA8301DDC64AE2F5D7 as rs_image_ADFD6891D3AF42CA8301DDC64AE2F5D7 zorder zorder_rs_image_ADFD6891D3AF42CA8301DDC64AE2F5D7 onlayer master
    hide rs_image_ADFD6891D3AF42CA8301DDC64AE2F5D7

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 300
    show rs_image_ADFD6891D3AF42CA8301DDC64AE2F5D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 0.8

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "前辈好～！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哦，四朗啊。嗯？雪绪怎么没在一起？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "他走的太慢，我就先他过来了☆"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊，还是老样子呐。要是又被训了我可不管。{w}\n篮球那边还行？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "当然！我的梦想是不断练习、\n熟练后进入御咲学园和前辈一起出席大赛！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈哈，我很期待呐{w}……说起来，四朗，\n没注意到？还是说已经克服那个弱点了？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "诶？什么事？"

    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "我们正在散步中。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪汪！"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Break 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 9-1.png
    $ zorder_rs_image_0F106B8E35274818A2D1764D5EC4CEFF = -100
    show rs_image_0F106B8E35274818A2D1764D5EC4CEFF as rs_image_0F106B8E35274818A2D1764D5EC4CEFF zorder zorder_rs_image_0F106B8E35274818A2D1764D5EC4CEFF onlayer master
    hide rs_image_0F106B8E35274818A2D1764D5EC4CEFF

    show rs_image_0F106B8E35274818A2D1764D5EC4CEFF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DC82470256CA4B6C829719736E9F7A91

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "！？！？"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "{size=32}噫呀啊啊啊啊！有、有狗！？{/size}{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    extend "{size=32}我{/size}{size=28}最{/size}{size=24}讨{/size}{size=20}厌{/size}{size=16}狗{/size}{size=14}了{/size}——"

    window hide

    pause 0.8

    $ set_window("(標準)")
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D7154940FF02439388BA1F87BDD543E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_76BDC5526C0D455C992334F53B3BACF8 as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "飞猫扑火……"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈哈……{w}雪绪，难得你过来，四朗却已经先逃了。"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AF7BBF63497B454D86E5E6600D6E3F01 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7009C1117C004F51829614A203C67DE7 "确实是呐～{w}那家伙真是的，为什么这么怕狗呢。"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "四朗的哥哥也是一样的，{w}到底为什么呢。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_427E9B184717439BA377834C6F4BEA90 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "好！下次就由我来好好调教他，让他克服怕狗的毛病！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "别、别了，勉强他也有些太可怜了不是吗？"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F48A0F9526F54B8AABC36F9A9C446AA8 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "才不是，这也是为了他好！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("住宅街"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00002B00

    return

label block_00002B00:
    # Node: 00002B00 (Phase ++)
    $ C1S4Phase = C1S4Phase + 1

    if judge_lm_condition([]):
        jump block_000007F7

    return

label block_000007F7:
    # Node: 000007F7 (Residential street 雪緖)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (152, 288),"image": "images/Chapter 1/Menu/Yukio.png","hover": "images/Chapter 1/Menu/Yukio hover.png","name": "雪緒"}, {"pos": (552, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_143
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000007F0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_0000080F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"雪緒\"" }]):
        jump block_0000080D

    return

label block_0000080F:
    # Node: 0000080F (Residential street turning)
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

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A4E74E94E7C549809795CEBC732E6326 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000810

    return

label block_00000810:
    # Node: 00000810 (Residential street turning)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (120, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "花乃湯"}, {"pos": (512, 320),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "神社"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_144
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"花乃湯\"" }]):
        jump block_0000081F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"神社\"" }]):
        jump block_0000081D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000007F2

    return

label block_0000081F:
    # Node: 0000081F (花乃湯)
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

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BB828FFB3AED43E6BB07C3169278015F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000820

    return

label block_00000820:
    # Node: 00000820 (花乃湯)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (392, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "ポスター"}, {"pos": (232, 272),"image": "images/Menu/Shougintoki.png","hover": "images/Menu/Shougintoki hover.png","name": "翔銀時"}, {"pos": (80, 280),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_145
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000080F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000831
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"翔銀時\"" }]):
        jump block_0000082E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"ポスター\"" }]):
        jump block_00001F74

    return

label block_00000831:
    # Node: 00000831 (River)
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

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_788AB1D278244B129D0C9F9230156AD7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000832

    return

label block_00000832:
    # Node: 00000832 (River)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_146
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000081F

    return

label block_0000082E:
    # Node: 0000082E (翔銀時)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_CA5DCF09EC6F43D3BF094A232BE224FB as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "你好。你来过这家花乃汤吗。\n店长的儿子应该和你同年。"

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
        jump block_00000820

    return

label block_00001F74:
    # Node: 00001F74 (Poster)
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
        jump block_00000820

    return

label block_0000081D:
    # Node: 0000081D (神社)
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

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_65FB514C0D3B40558703DF2D35F42E17 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_0000081E

    return

label block_0000081E:
    # Node: 0000081E (神社)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_147
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000080F

    return

label block_0000080D:
    # Node: 0000080D (雪緒)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_B88DFA606D384D139F2F3C6326D0D471 as tag_4233D225ED0D43968B3A0D890F587FEB at center_bottom zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "我会好好调教四朗的，敬请期待！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("住宅街"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_000007F7

    return

label block_00000836:
    # Node: 00000836 (御咲站)
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

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_07BACEE3C1C64F1DAD61CD240DF0C2E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_0000083A

    return

label block_0000083A:
    # Node: 0000083A (御咲站)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (336, 352),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_148
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000007F0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_000008B1

    return

label block_000008B1:
    # Node: 000008B1 (Inside)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "STAY，小翼。{w}\n狗不能进入车站，前面不能走了。"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F1AE8B76A99E4FC297AF2F180FA7033F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪？"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不过，\n像是导盲犬那种受过训练的可以进去的样子。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "小翼也想去考一个试试？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_83E2064E232640149A12D7598C5FE5C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪！"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嗯嗯，不错的回答呐。\n小翼这么聪明，说不定能考上呢♪"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("御咲站"))
    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"


    if judge_lm_condition([]):
        jump block_00000836

    return

label block_00000806:
    # Node: 00000806 (Shopping street)
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

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5F022B91486841699EAC5FE3BDC0F5CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00000808

    return

label block_00000808:
    # Node: 00000808 (Shopping street)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (104, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_149
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000366D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00000818

    return

label block_0000366D:
    # Node: 0000366D (TO: Misaki)

    if judge_lm_condition([]):
        jump block_0000366C

    return

label block_0000366C:
    # Node: 0000366C (TO: Misaki)

    if judge_lm_condition([]):
        jump block_0000366B

    return

label block_00000818:
    # Node: 00000818 (Inside)
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "STAY，小翼。{w}\n前面人太多，太危险了。"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F1AE8B76A99E4FC297AF2F180FA7033F as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_bottom zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("商店街"))
    if sys_effect2_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"


    if judge_lm_condition([]):
        jump block_00000808

    return

label block_000007F5:
    # Node: 000007F5 (Park)
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

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AC1A95BA21694004A67885C809E98CFF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "C1S4Phase == 1" }]):
        jump block_000007F8
    if judge_lm_condition([]):
        jump block_000007FB

    return

label block_000007F8:
    # Node: 000007F8 (Park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_150
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000366B

    return

label block_000007FB:
    # Node: 000007FB (Park 小林 flag)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (160, 184),"image": "images/Chapter 1/Menu/Kobayashi flag.png","hover": "images/MENU/Kobayashi hover.png","name": "小林"}, {"pos": (320, 184),"image": "images/MENU/Minami.png","hover": "images/MENU/Minami hover.png","name": "南"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_151
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_0000366B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"小林\"" }]):
        jump block_000023DC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"南\"" }]):
        jump block_000023DD

    return

label block_000023DC:
    # Node: 000023DC (F4: 小林)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_F3C56AC05CFF4764BCEAA3638847A04F as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00000800

    return

label block_00000800:
    # Node: 00000800 (F4)
    window show

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_0DD616D8E2914FC2859CDB40FCB50F1A as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_EA79386263E543A88D4DC03B8BD44485 "啊！是作哉哥和小翼——！"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_83E2064E232640149A12D7598C5FE5C3 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪汪汪♪"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_3171B5940A5B4E6FAB23370F6FC4A7EC as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9A978AAD07624C598B6179F23F51FB2D "乖乖☆{w}小翼今天也很开心呐——！"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_E714266E48C34071B1AFC8E511D39DD5 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "作哉哥，那个啊！\n我们发现了超有意思的事哦！"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_645DF0E195CF42798B8F728CE5EAEEE2 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "大家一起去玩！{w}小翼也要去♪"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_83E2064E232640149A12D7598C5FE5C3 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪汪！"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "抱歉，今天不行，课还没上完。{w}\n放学后也有社团活动，下次再说好了。"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_1FF2B98C6C1E44809702A907624A30EB as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "欸～！{w}\n{nw}"
    show rs_image_F3C56AC05CFF4764BCEAA3638847A04F as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，那小翼留下来陪我们玩好了。\n一起来吗？"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "太危险了不行。今天就先忍忍。"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_19B48A464F434AC7830B9BFFF091AB3F as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9A978AAD07624C598B6179F23F51FB2D "作哉哥好小气——"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_1FF2B98C6C1E44809702A907624A30EB as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA79386263E543A88D4DC03B8BD44485 "小气——"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_F1AE8B76A99E4FC297AF2F180FA7033F as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪——"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_E862399617D0416D954F0F9E73A9355E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不行就是不行！{w}{w}\n等会再见，你们先去玩好了。\n来小翼，说再见。"

    window hide

    $ set_window("イベントモード")
    pause 0.3

    # Gallery unlock: images/CG/Inconceivable-story-of-wong-mew/Inconceivable-story-of-wong-mew 10.png
    $ zorder_rs_image_B4FB83ADF72E4DEDA77384FEB0F94E44 = -100
    show rs_image_B4FB83ADF72E4DEDA77384FEB0F94E44 as rs_image_B4FB83ADF72E4DEDA77384FEB0F94E44 zorder zorder_rs_image_B4FB83ADF72E4DEDA77384FEB0F94E44 onlayer master
    hide rs_image_B4FB83ADF72E4DEDA77384FEB0F94E44

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    show rs_image_B4FB83ADF72E4DEDA77384FEB0F94E44 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.5

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_244536AD39AF4697B223756F943650AA "再见——！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_F87850A1F3524EDDB3556FD58C8BDA3B "“再见——♪”"

    window hide

    pause 0.5

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.6

    $ set_place_title(_("公园"))
    pause 1.3

    $ set_place_title("")
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    stop music fadeout 2
    $ sys_music_current_file = ""


    if judge_lm_condition([]):
        jump block_000036FC

    return

label block_000036FC:
    # Node: 000036FC (FLAG: 不可思議！猫狗物語)
    call block_000036FB from _call_block_000036FB

    if judge_lm_condition([]):
        jump block_000036F7

    return

label block_000036F7:
    # Node: 000036F7 ()

    return

label block_000023DD:
    # Node: 000023DD (F4: 南)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_BEF9DE93926B41AEA207953580E58EC3 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_18D40E17D40245CA8A541878C16B1175 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00000800

    return

label block_000007FA:
    # Node: 000007FA (Not allowed)

    if judge_lm_condition([]):
        jump block_000007F1

    return

label block_000007EE:
    # Node: 000007EE (Conversation)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "今天也要好好散步\n把该处理的都处理了呐♪"

    window hide

    $ set_window("(標準)")

    return

label block_000007EF:
    # Node: 000007EF (Target)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『请试着寻找下一个同类{/color}{color=#008000}事件{/color}{color=#0080FF}。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00001FC6:
    # Node: 00001FC6 (Abandon)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    jump block_00002AFF

    return

label block_00002AFF:
    # Node: 00002AFF (RESET FLAG)
    $ C1S1Phase = 0
    $ C1S2Phase = 0
    $ C1S3Phase = 0
    $ C1S4Phase = 0
    $ C1S5Phase = 0

    if judge_lm_condition([]):
        jump block_00003727

    return

label block_00003727:
    # Node: 00003727 ()

    return

label block_00001FC9:
    # Node: 00001FC9 (Character)
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

