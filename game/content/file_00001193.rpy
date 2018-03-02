# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00001193 (三朗美髮店)

label block_00001194:
    # Node: 00001194 (開始)
    $ SelectedTarget = 0

    $ set_place_title(False)

    if judge_lm_condition([{ "scope": 0, "content": "Chapter > 1" }]):
        jump block_00002EC8
    if judge_lm_condition([]):
        jump block_00001195

    return

label block_00002EC8:
    # Node: 00002EC8 (Background CP23EOS)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_589411E603304F8697C6E45AD2F54993 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.35

    show rs_image_D7AC7403C04640D483DCA1818D0D32FB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_0F272834000249D880A7A79DD0E0BA25 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.4

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "HEY，欢迎光临！！来做个好的形象！"


    if judge_lm_condition([{ "scope": 0, "content": "CXQSabuImechen == False" }]):
        jump block_00002ECA
    if judge_lm_condition([]):
        jump block_00002ED4

    return

label block_00002ECA:
    # Node: 00002ECA (First time)
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "客人是第一次来？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "本店可以免费提供和平时不一个口味的{color=#00FFFF}形象转换{/color}哦～"

    window hide

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    show rs_image_DCCF4EEB965C4E919D05F60C37C10ECB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E


    if judge_lm_condition([]):
        jump block_0000368E

    return

label block_0000368E:
    # Node: 0000368E (選擇)
    $ sys_lm_menu_item = [{"pos": (8, 152),"image": "images/Saburos-Salon/AVATAR/Tomo.png","hover": "images/Saburos-Salon/AVATAR/Tomo hover.png","name": "友"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, -0.001) from _call_lm_menu_281
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"友\"" }]):
        jump block_00002ECC

    return

label block_00002ECC:
    # Node: 00002ECC (友)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_BB9125A8E31E49DBB38AF58B4E2E4CCC as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_DC9ADBFBED9F4E669FC42A99F64FFD2E as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_C34B7E515C454982A4812C9E32BD50E7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好咧！赌上我的本事，给你弄个好造型！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=36}{color=#00FFFF}Let's IMECHEN！！{/color}{/size}"

    window hide

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 0.7


    if judge_lm_condition([]):
        jump block_00002EC9

    return

label block_00002EC9:
    # Node: 00002EC9 (1)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Scene changing 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_589411E603304F8697C6E45AD2F54993 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57F79897CE2D49FC8E9CC05EC4072D27

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_2A054FA123984C2AAB5FF6EF7EA2729C as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『头发终于被{/color}{color=#00FFFF}拉直{/color}{color=#0080FF}了！』{/color}"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嘛，差不多就这样了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦！不错！！梦寐以求的直发——！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "现在我能想到的样式还很少，\n{color=#00FFFF}多经历一些事再回来{/color}应该会多起来！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "还有，换什么造型全看我钦定，\n有些兴趣在里面就忍忍好了。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "之后会给你复原的，并不会真剪下去，\n放心就是。再怎么说就是玩玩嘛！"

    window hide

    pause 0.8

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00002ECE

    return

label block_00002ECE:
    # Node: 00002ECE (Tomo)
    $ GSabuImechenTomoState = GSabuImechenTomoState + 1

    if judge_lm_condition([{ "scope": 0, "content": "END == True" }]):
        jump block_00003F37
    if judge_lm_condition([{ "scope": 0, "content": "Chapter == 3" }]):
        jump block_00004014
    if judge_lm_condition([]):
        jump block_00002ECD

    return

label block_00003F37:
    # Node: 00003F37 (Roof)
    $ set_window("(標準)")
    if sys_music_current_file != "sound/BGM/End of semester.ogg":
        play music "sound/BGM/End of semester.ogg" loop
        $ sys_music_current_file = "sound/BGM/End of semester.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_place_title(_("屋顶"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.4


    if judge_lm_condition([]):
        jump block_00003F38

    return

label block_00003F38:
    # Node: 00003F38 (三朗)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window show

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_EEEB5A55C0BC41D983795AF5F604A6E7 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "感谢帮忙——！"

    show rs_image_46DCDD9346A640B580641D51A5DAF0F0 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "最近有些喜欢上帮人弄头发了。\n改改发型就能变形象，是不是很有意思？"

    show rs_image_3ACBBD4629FF422BBF1AE90C6CE5A2BF as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "后面会练出更多好看的发型的，记得常来哦♪"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_00002489

    return

label block_00002489:
    # Node: 00002489 (QUEST FINISH)
    if sys_music2_current_file != "sound/BGM/Quest Finished.ogg":
        play music2 "sound/BGM/Quest Finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Quest Finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『委托成功结束』{/color}"

    pause 0.8

    window hide


    if judge_lm_condition([]):
        jump block_00002A77

    return

label block_00002A77:
    # Node: 00002A77 (CXQSabuImechen)
    $ CXQSabuImechen = True

    if judge_lm_condition([]):
        jump block_00003691

    return

label block_00003691:
    # Node: 00003691 ()
    $ del SelectedTarget

    return

label block_00004014:
    # Node: 00004014 (CP3)

    if judge_lm_condition([{ "scope": 0, "content": "C3ShowLastWarning == True" }]):
        jump block_000030ED
    if judge_lm_condition([]):
        jump block_000030E9

    return

label block_000030ED:
    # Node: 000030ED (Roof)
    $ set_window("(標準)")
    if sys_music_current_file != "sound/BGM/Start scene.ogg":
        play music "sound/BGM/Start scene.ogg" loop
        $ sys_music_current_file = "sound/BGM/Start scene.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_place_title(_("屋顶"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.4


    if judge_lm_condition([]):
        jump block_000030EA

    return

label block_000030EA:
    # Node: 000030EA (三朗)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window show

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_EEEB5A55C0BC41D983795AF5F604A6E7 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "感谢帮忙——！"

    show rs_image_46DCDD9346A640B580641D51A5DAF0F0 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "最近有些喜欢上帮人弄头发了。\n改改发型就能变形象，是不是很有意思？"

    show rs_image_3ACBBD4629FF422BBF1AE90C6CE5A2BF as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "后面会练出更多好看的发型的，记得常来哦♪"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_00002489

    return

label block_000030E9:
    # Node: 000030E9 (Roof)
    $ set_window("(標準)")
    if sys_music_current_file != "sound/BGM/Chapter 3.ogg":
        play music "sound/BGM/Chapter 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 3.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_place_title(_("屋顶"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.4


    if judge_lm_condition([]):
        jump block_000030EA

    return

label block_00002ECD:
    # Node: 00002ECD (Roof)
    $ set_window("(標準)")
    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_place_title(_("屋顶"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.4


    if judge_lm_condition([]):
        jump block_00002ECF

    return

label block_00002ECF:
    # Node: 00002ECF (三朗)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window show

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_2F053DD5EF4C49B388E430ED01FE5A69 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "感谢帮忙——！"

    show rs_image_62D35A6C85144BF796E08D1132E03CA7 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "最近有些喜欢上帮人弄头发了。\n改改发型就能变形象，是不是很有意思？"

    show rs_image_C3ABF38C2BB8427E9EA82889DB41D4D1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "后面会练出更多好看的发型的，记得常来哦♪"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_00002489

    return

label block_00002ED4:
    # Node: 00002ED4 (CP1后)
    window hide

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    show rs_image_DCCF4EEB965C4E919D05F60C37C10ECB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E


    if judge_lm_condition([]):
        jump block_00001197

    return

style saburou_imechen_back_button:
    vertical True
    size 30
    color "#FE6666"
    hover_color "#FFB0CF"
    font "font/zcool-happy-ayumi-extended.ttf"
style saburou_imechen_back_button_2:
    size 40
    color "#EA2280"
    hover_color "#FFFFFF"
    font "font/zcool-happy-ayumi-extended.ttf"
    outlines [(absolute(3), "#FFFFFF", absolute(0), absolute(0))]
    hover_outlines [(absolute(3), "#EA2280", absolute(0), absolute(0))]

label block_00001197:
    # Node: 00001197 (選擇)
    $ sys_lm_menu_item = [{"pos": (8, 152),"image": "images/Saburos-Salon/AVATAR/Tomo.png","hover": "images/Saburos-Salon/AVATAR/Tomo hover.png","name": "友"}, {"pos": (128, 152),"image": "images/Saburos-Salon/AVATAR/Tsubasa.png","hover": "images/Saburos-Salon/AVATAR/Tsubasa hover.png","name": "つばさ"}, {"pos": (256, 152),"image": "images/Saburos-Salon/AVATAR/Sakuya.png","hover": "images/Saburos-Salon/AVATAR/Sakuya hover.png","name": "作哉"}, {"pos": (8, 272),"image": "images/Saburos-Salon/AVATAR/Shinobu.png","hover": "images/Saburos-Salon/AVATAR/Shinobu hover.png","name": "しのぶ"}, {"pos": (130, 272),"image": "images/Saburos-Salon/AVATAR/Tsuki.png","hover": "images/Saburos-Salon/AVATAR/Tsuki hover.png","name": "月"}, {"pos": (256, 272),"image": "images/Saburos-Salon/AVATAR/Sora.png","hover": "images/Saburos-Salon/AVATAR/Sora hover.png","name": "空"}, {"pos": (8, 416),"image": "images/Saburos-Salon/AVATAR/Saburo.png","hover": "images/Saburos-Salon/AVATAR/Saburo hover.png","name": "三朗"}, {"pos": (130, 414),"image": "images/Saburos-Salon/AVATAR/Shintaro.png","hover": "images/Saburos-Salon/AVATAR/Shintaro hover.png","name": "慎太郎"}, {"pos": (320, 460),"type":"textbutton", "style": "saburou_imechen_back_button", "text": _("返回"),"name": "戻る"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, -0.001) from _call_lm_menu_282
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"友\"" }]):
        jump block_00003735
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_00003738
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"作哉\"" }]):
        jump block_0000373B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_00003737
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"月\"" }]):
        jump block_00003739
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"空\"" }]):
        jump block_0000373A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗\"" }]):
        jump block_0000373C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"慎太郎\"" }]):
        jump block_00003736
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"戻る\"" }]):
        jump block_00003781

    return

label block_00003735:
    # Node: 00003735 (SetTarget: 友)
    $ SelectedTarget = 0

    if judge_lm_condition([]):
        jump block_0000373D

    return

label block_0000373D:
    # Node: 0000373D (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedTarget == 0" }]):
        jump block_00003732
    if judge_lm_condition([]):
        jump block_00003740

    return

label block_00003732:
    # Node: 00003732 (TO: 友)

    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTomoState == 6" }]):
        jump block_00002486
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTomoState == 1" },{ "scope": 0, "content": "GSabuImechenTomoState == 2" },{ "scope": 1, "content": "C1SG1 == True" },{ "scope": 0, "content": "GSabuImechenTomoState == 3" },{ "scope": 1, "content": "C2SG1 == True" },{ "scope": 0, "content": "GSabuImechenTomoState == 4" },{ "scope": 1, "content": "C3SG1 == True" },{ "scope": 0, "content": "GSabuImechenTomoState == 5" },{ "scope": 1, "content": "C3SG2 == True" }]):
        jump block_00001198
    if judge_lm_condition([]):
        jump block_0000373E

    return

label block_00002486:
    # Node: 00002486 (Review)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("(標準)")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "行了，已经没想法了！\n我想不出新的发型了。{w}要看看以前的设计么？"

    window hide

    $ set_window("イベントモード")

    if judge_lm_condition([]):
        jump block_00002454

    return

label block_00002454:
    # Node: 00002454 (選擇)
    $ sys_lm_choice_item = ["看", "不想看"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_1
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"看\"" }]):
        jump block_000029CF
    if judge_lm_condition([]):
        jump block_0000260A

    return

label block_000029CF:
    # Node: 000029CF (1)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_894199D30F034634AE608180960D7570 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_C34B7E515C454982A4812C9E32BD50E7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029D0

    return

label block_000029D0:
    # Node: 000029D0 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_283
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029CD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029D1
    if judge_lm_condition([]):
        jump block_00003734

    return

label block_000029CD:
    # Node: 000029CD (2)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_1EA10230BA38411E92B071966D1BC0B7 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_2A054FA123984C2AAB5FF6EF7EA2729C as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029CE

    return

label block_000029CE:
    # Node: 000029CE (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_284
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029CB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029CF
    if judge_lm_condition([]):
        jump block_00003734

    return

label block_000029CB:
    # Node: 000029CB (3)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_BBC048B62C9E43909547D0860C90C723 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_09E95A2C02EE4C38AB2CA24FBD2C53E1 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029CC

    return

label block_000029CC:
    # Node: 000029CC (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_285
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029C7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029CD
    if judge_lm_condition([]):
        jump block_00003734

    return

label block_000029C7:
    # Node: 000029C7 (4)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_4AAD04CAF4DB48BABB5033ED570FA64A as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_1F69193F8E5442D18D95F1E87B478B61 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029CA

    return

label block_000029CA:
    # Node: 000029CA (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_286
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029C6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029CB
    if judge_lm_condition([]):
        jump block_00003734

    return

label block_000029C6:
    # Node: 000029C6 (5)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_A92B42BFF9B9482293D7D44EFF9D4539 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_A5602981CAB84B6F8DA65308C26D39AF as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029C8

    return

label block_000029C8:
    # Node: 000029C8 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_287
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029C5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029C7
    if judge_lm_condition([]):
        jump block_00003734

    return

label block_000029C5:
    # Node: 000029C5 (6)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_5755D01206954077A7698867C1B875B6 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_77A3013C1D6E4B69A30A9E0285420802 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029C9

    return

label block_000029C9:
    # Node: 000029C9 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_288
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029C6
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029D1
    if judge_lm_condition([]):
        jump block_00003734

    return

label block_000029D1:
    # Node: 000029D1 (7)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_CBB481179D3244D5B306890A1AD7AF3C as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_D319C19F382946958C2DDDEFE0B35C0B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029D2

    return

label block_000029D2:
    # Node: 000029D2 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_289
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029CF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029C5
    if judge_lm_condition([]):
        jump block_00003734

    return

label block_00003734:
    # Node: 00003734 (TO: START)

    if judge_lm_condition([]):
        jump block_00003743

    return

label block_00003743:
    # Node: 00003743 (TO: START)

    if judge_lm_condition([]):
        jump block_0000374C

    return

label block_0000374C:
    # Node: 0000374C (TO: START)

    if judge_lm_condition([]):
        jump block_00003752

    return

label block_00003752:
    # Node: 00003752 (TO: START)

    if judge_lm_condition([]):
        jump block_00003766

    return

label block_00003766:
    # Node: 00003766 (TO: START)

    if judge_lm_condition([]):
        jump block_0000376F

    return

label block_0000376F:
    # Node: 0000376F (TO: START)

    if judge_lm_condition([]):
        jump block_00003775

    return

label block_00003775:
    # Node: 00003775 (TO: START)

    if judge_lm_condition([]):
        jump block_0000377D

    return

label block_0000377D:
    # Node: 0000377D (TO: START)

    if judge_lm_condition([]):
        jump block_00003746

    return

label block_00003746:
    # Node: 00003746 (TO: START)

    if judge_lm_condition([]):
        jump block_00003733

    return

label block_00003733:
    # Node: 00003733 (TO: START)

    if judge_lm_condition([{ "scope": 0, "content": "Chapter > 1" }]):
        jump block_00002ED4
    if judge_lm_condition([]):
        jump block_00002443

    return

label block_00002443:
    # Node: 00002443 (CP1)
    window hide

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    show rs_image_566D296EAB9E4AC48A093665CD619A3F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E


    if judge_lm_condition([]):
        jump block_00001197

    return

label block_0000260A:
    # Node: 0000260A (不看)

    if judge_lm_condition([]):
        jump block_00003734

    return

label block_00001198:
    # Node: 00001198 (PRE)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_BB9125A8E31E49DBB38AF58B4E2E4CCC as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_DC9ADBFBED9F4E669FC42A99F64FFD2E as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_C34B7E515C454982A4812C9E32BD50E7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你自己对不。行，说上就上！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=36}{color=#00FFFF}Let's IMECHEN！！{/color}{/size}"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 1

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Scene changing 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_589411E603304F8697C6E45AD2F54993 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57F79897CE2D49FC8E9CC05EC4072D27

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTomoState == 1" }]):
        jump block_00001199
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTomoState == 2" }]):
        jump block_00002441
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTomoState == 3" }]):
        jump block_00002442
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTomoState == 4" }]):
        jump block_00002455
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTomoState == 5" }]):
        jump block_00002456

    return

label block_00001199:
    # Node: 00001199 (2)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_09E95A2C02EE4C38AB2CA24FBD2C53E1 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}小修小改{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了一下！』{/color}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？有、有什么变化嘛？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好——好看看。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……？{w}……啊！我重要的呆毛没了！？"


    if judge_lm_condition([]):
        jump block_00003730

    return

label block_00003730:
    # Node: 00003730 (RESET)
    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002A88

    return

label block_00002A88:
    # Node: 00002A88 (Tomo)
    $ GSabuImechenTomoState = GSabuImechenTomoState + 1

    if judge_lm_condition([]):
        jump block_00003754

    return

label block_00003754:
    # Node: 00003754 (TO: 選擇)

    if judge_lm_condition([]):
        jump block_00003731

    return

label block_00003731:
    # Node: 00003731 (TO: 選擇)

    if judge_lm_condition([{ "scope": 0, "content": "Chapter > 1" }]):
        jump block_00002F58
    if judge_lm_condition([]):
        jump block_00002F57

    return

label block_00002F58:
    # Node: 00002F58 (CP1后)
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    show rs_image_DCCF4EEB965C4E919D05F60C37C10ECB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E


    if judge_lm_condition([]):
        jump block_00001197

    return

label block_00002F57:
    # Node: 00002F57 (CP1)
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    show rs_image_566D296EAB9E4AC48A093665CD619A3F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E


    if judge_lm_condition([]):
        jump block_00001197

    return

label block_00002441:
    # Node: 00002441 (3)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_1F69193F8E5442D18D95F1E87B478B61 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『试着做了个{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}江户武士{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}的样子！』{/color}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这绝对是在胡闹对不对。"


    if judge_lm_condition([]):
        jump block_00003730

    return

label block_00002442:
    # Node: 00002442 (4)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_A5602981CAB84B6F8DA65308C26D39AF as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}剪短{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "总觉得变矮了～"


    if judge_lm_condition([]):
        jump block_00003730

    return

label block_00002455:
    # Node: 00002455 (5)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_77A3013C1D6E4B69A30A9E0285420802 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『做成了{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}流行风{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦！感觉好先进♪"


    if judge_lm_condition([]):
        jump block_00003730

    return

label block_00002456:
    # Node: 00002456 (6)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_D319C19F382946958C2DDDEFE0B35C0B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『做成了{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}其他角色{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}的样子！』{/color}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！？这、这是……{w}\n没、真的没关系？“我”还在不在……？"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『森海友的发型{/color}{color=#FF00FF}就这些{/color}{color=#0080FF}了。』{/color}"


    if judge_lm_condition([]):
        jump block_00003730

    return

label block_0000373E:
    # Node: 0000373E (TO: No idea)

    if judge_lm_condition([]):
        jump block_00002485

    return

label block_00002485:
    # Node: 00002485 (No idea)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("(標準)")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "还没想到新发型，对不住。"

    window hide

    $ set_window("イベントモード")

    if judge_lm_condition([]):
        jump block_00001197

    return

label block_00003740:
    # Node: 00003740 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedTarget == 1" }]):
        jump block_0000373F
    if judge_lm_condition([]):
        jump block_00003748

    return

label block_0000373F:
    # Node: 0000373F (TO: 慎太郎)

    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenShintaroState == 4" }]):
        jump block_00002A7C
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenShintaroState == 0" },{ "scope": 1, "content": "C1SG1 == True" },{ "scope": 0, "content": "GSabuImechenShintaroState == 1" },{ "scope": 1, "content": "C2SG1 == True" },{ "scope": 0, "content": "GSabuImechenShintaroState == 2" },{ "scope": 1, "content": "C3SG1 == True" },{ "scope": 0, "content": "GSabuImechenShintaroState == 3" },{ "scope": 1, "content": "C3SG2 == True" }]):
        jump block_00002482
    if judge_lm_condition([]):
        jump block_00003745

    return

label block_00002A7C:
    # Node: 00002A7C (Review)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("(標準)")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "行了，已经没想法了！\n我想不出新的发型了。{w}要看看以前的设计么？"

    window hide

    $ set_window("イベントモード")

    if judge_lm_condition([]):
        jump block_00002A7B

    return

label block_00002A7B:
    # Node: 00002A7B (選擇)
    $ sys_lm_choice_item = ["看", "不想看"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_2
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"看\"" }]):
        jump block_00002A13
    if judge_lm_condition([]):
        jump block_00003744

    return

label block_00002A13:
    # Node: 00002A13 (1)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_894199D30F034634AE608180960D7570 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_C878CBCF89004F8CA6E7BAABD623A66D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002A14

    return

label block_00002A14:
    # Node: 00002A14 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_290
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_00002A11
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_00002A0C
    if judge_lm_condition([]):
        jump block_00003743

    return

label block_00002A11:
    # Node: 00002A11 (2)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_4CC42B1EF0D74AF3BE60822D58A13172 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_80119DFCF4A4458F94B1E0EBACA79F24 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002A12

    return

label block_00002A12:
    # Node: 00002A12 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_291
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_00002A0F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_00002A13
    if judge_lm_condition([]):
        jump block_00003743

    return

label block_00002A0F:
    # Node: 00002A0F (3)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_1EA10230BA38411E92B071966D1BC0B7 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_00DCC3536E654082984D35630FDF327D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002A10

    return

label block_00002A10:
    # Node: 00002A10 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_292
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_00002A0B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_00002A11
    if judge_lm_condition([]):
        jump block_00003743

    return

label block_00002A0B:
    # Node: 00002A0B (4)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_45CCED0BC2D444528CCB5B6E74E07347 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_1B5B81B232DF4312A2A7716870FF699F as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002A0D

    return

label block_00002A0D:
    # Node: 00002A0D (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_293
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_00002A0C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_00002A0F
    if judge_lm_condition([]):
        jump block_00003743

    return

label block_00002A0C:
    # Node: 00002A0C (5)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_5755D01206954077A7698867C1B875B6 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_CE57F3AE035B4917BC563C6B90DCDCF3 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002A0E

    return

label block_00002A0E:
    # Node: 00002A0E (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_294
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_00002A13
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_00002A0B
    if judge_lm_condition([]):
        jump block_00003743

    return

label block_00003744:
    # Node: 00003744 (不看)

    if judge_lm_condition([]):
        jump block_00003743

    return

label block_00002482:
    # Node: 00002482 (PRE)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_BB9125A8E31E49DBB38AF58B4E2E4CCC as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_4EC3A128E15E49439045295D75FE1E30 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_C878CBCF89004F8CA6E7BAABD623A66D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这家伙是不。行，说上就上！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=36}{color=#00FFFF}Let's IMECHEN！！{/color}{/size}"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 1

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Scene changing 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_589411E603304F8697C6E45AD2F54993 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57F79897CE2D49FC8E9CC05EC4072D27

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenShintaroState == 0" }]):
        jump block_0000247E
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenShintaroState == 1" }]):
        jump block_0000247F
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenShintaroState == 2" }]):
        jump block_00002480
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenShintaroState == 3" }]):
        jump block_00002481

    return

label block_0000247E:
    # Node: 0000247E (1)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_80119DFCF4A4458F94B1E0EBACA79F24 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『把头发{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}熨了{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼呼♪底子好就是怎么都好看啊♪"


    if judge_lm_condition([]):
        jump block_00003741

    return

label block_00003741:
    # Node: 00003741 (RESET)
    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002ACA

    return

label block_00002ACA:
    # Node: 00002ACA (Shintaro)
    $ GSabuImechenShintaroState = GSabuImechenShintaroState + 1

    if judge_lm_condition([]):
        jump block_00003742

    return

label block_00003742:
    # Node: 00003742 (TO: 選擇)

    if judge_lm_condition([]):
        jump block_00003754

    return

label block_0000247F:
    # Node: 0000247F (2)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_00DCC3536E654082984D35630FDF327D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}拉直{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "和平时的我不一个感觉对不？"


    if judge_lm_condition([]):
        jump block_00003741

    return

label block_00002480:
    # Node: 00002480 (3)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_1B5B81B232DF4312A2A7716870FF699F as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『头发全都{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}向后梳理{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……我倒是知道很适合这个的角色不过……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "偶、偶然的吧？\n戴上这个全都梳到后面只是偶然有点合适而已吧？"


    if judge_lm_condition([]):
        jump block_00003741

    return

label block_00002481:
    # Node: 00002481 (4)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_CE57F3AE035B4917BC563C6B90DCDCF3 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『做成了{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}流行风{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "和某LV5很像的发型呐——"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『奥村慎太郎的发型{/color}{color=#FF00FF}就这些{/color}{color=#0080FF}了。』{/color}"


    if judge_lm_condition([]):
        jump block_00003741

    return

label block_00003745:
    # Node: 00003745 (TO: No idea)

    if judge_lm_condition([]):
        jump block_0000373E

    return

label block_00003748:
    # Node: 00003748 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedTarget == 2" }]):
        jump block_00003747
    if judge_lm_condition([]):
        jump block_00003755

    return

label block_00003747:
    # Node: 00003747 (TO: 忍)

    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenShinobuState == 5" }]):
        jump block_00002A84
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenShinobuState == 0" },{ "scope": 0, "content": "GSabuImechenShinobuState == 1" },{ "scope": 1, "content": "C1SG1 == True" },{ "scope": 0, "content": "GSabuImechenShinobuState == 2" },{ "scope": 1, "content": "C2SG1 == True" },{ "scope": 0, "content": "GSabuImechenShinobuState == 3" },{ "scope": 1, "content": "C3SG1 == True" },{ "scope": 0, "content": "GSabuImechenShinobuState == 4" },{ "scope": 1, "content": "C3SG2 == True" }]):
        jump block_0000245A
    if judge_lm_condition([]):
        jump block_0000374D

    return

label block_00002A84:
    # Node: 00002A84 (Review)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("(標準)")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "行了，已经没想法了！\n我想不出新的发型了。{w}要看看以前的设计么？"

    window hide

    $ set_window("イベントモード")

    if judge_lm_condition([]):
        jump block_00002A83

    return

label block_00002A83:
    # Node: 00002A83 (選擇)
    $ sys_lm_choice_item = ["看", "不想看"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_3
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"看\"" }]):
        jump block_000029DD
    if judge_lm_condition([]):
        jump block_0000374B

    return

label block_000029DD:
    # Node: 000029DD (1)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_894199D30F034634AE608180960D7570 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_177E44EC21914EB897484E9D7A6A8C4B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029DE

    return

label block_000029DE:
    # Node: 000029DE (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_295
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029DB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029D3
    if judge_lm_condition([]):
        jump block_0000374C

    return

label block_000029DB:
    # Node: 000029DB (2)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_A92B42BFF9B9482293D7D44EFF9D4539 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_4636641D0103498B9E71F6AA62BB0DC8 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029DC

    return

label block_000029DC:
    # Node: 000029DC (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_296
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029D9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029DD
    if judge_lm_condition([]):
        jump block_0000374C

    return

label block_000029D9:
    # Node: 000029D9 (3)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_D0B42774E1274D47B41392CA1B52668E as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_F3BD0CBF95D34CDD8AE2A97AB28DB03D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029DA

    return

label block_000029DA:
    # Node: 000029DA (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_297
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029D5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029DB
    if judge_lm_condition([]):
        jump block_0000374C

    return

label block_000029D5:
    # Node: 000029D5 (4)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_1EA10230BA38411E92B071966D1BC0B7 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_04AFC59B6ED149419AB53053B5394693 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029D6

    return

label block_000029D6:
    # Node: 000029D6 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_298
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029D4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029D9
    if judge_lm_condition([]):
        jump block_0000374C

    return

label block_000029D4:
    # Node: 000029D4 (5)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_57FC758EAC8E4134AB579D79C52D6DEF as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_274C0479F32F42AFB7492F8FFC232263 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029D7

    return

label block_000029D7:
    # Node: 000029D7 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_299
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029D3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029D5
    if judge_lm_condition([]):
        jump block_0000374C

    return

label block_000029D3:
    # Node: 000029D3 (6)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_5755D01206954077A7698867C1B875B6 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_A44AB636A7A14C878405BC64B52B7FE4 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029D8

    return

label block_000029D8:
    # Node: 000029D8 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_300
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029D4
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029DD
    if judge_lm_condition([]):
        jump block_0000374C

    return

label block_0000374B:
    # Node: 0000374B (不看)

    if judge_lm_condition([]):
        jump block_0000374C

    return

label block_0000245A:
    # Node: 0000245A (PRE)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_BB9125A8E31E49DBB38AF58B4E2E4CCC as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_AFA500DBEC89463FA3CB949C1E335B4B as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_177E44EC21914EB897484E9D7A6A8C4B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这家伙是不。行，说上就上！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=36}{color=#00FFFF}Let's IMECHEN！！{/color}{/size}"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 1

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Scene changing 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_589411E603304F8697C6E45AD2F54993 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57F79897CE2D49FC8E9CC05EC4072D27

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenShinobuState == 0" }]):
        jump block_00002458
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenShinobuState == 1" }]):
        jump block_00002459
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenShinobuState == 2" }]):
        jump block_0000245B
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenShinobuState == 3" }]):
        jump block_0000245C
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenShinobuState == 4" }]):
        jump block_0000245D

    return

label block_00002458:
    # Node: 00002458 (1)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_4636641D0103498B9E71F6AA62BB0DC8 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}剪短{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "夏天剪过的发型呐。下次再试试好了。"


    if judge_lm_condition([]):
        jump block_00003749

    return

label block_00003749:
    # Node: 00003749 (RESET)
    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002AC9

    return

label block_00002AC9:
    # Node: 00002AC9 (Shinobu)
    $ GSabuImechenShinobuState = GSabuImechenShinobuState + 1

    if judge_lm_condition([]):
        jump block_0000374A

    return

label block_0000374A:
    # Node: 0000374A (TO: 選擇)

    if judge_lm_condition([]):
        jump block_00003742

    return

label block_00002459:
    # Node: 00002459 (2)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_F3BD0CBF95D34CDD8AE2A97AB28DB03D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『试着{/color}{color=#0080FF}{b}〈{/b}{/color}{color=#00FFFF}重塑造型{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸——我的头发还能变出这种感觉啊。"


    if judge_lm_condition([]):
        jump block_00003749

    return

label block_0000245B:
    # Node: 0000245B (3)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_04AFC59B6ED149419AB53053B5394693 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}拉直{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……和鬼太郎似的。"


    if judge_lm_condition([]):
        jump block_00003749

    return

label block_0000245C:
    # Node: 0000245C (4)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_274C0479F32F42AFB7492F8FFC232263 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『使用了改良后的剪短——{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}剪短2{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "总觉得变年轻了。"


    if judge_lm_condition([]):
        jump block_00003749

    return

label block_0000245D:
    # Node: 0000245D (5)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_A44AB636A7A14C878405BC64B52B7FE4 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『做成了{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}流行风{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "拿漫画来说就像什么地方的少爷似的。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『绫濑忍的发型{/color}{color=#FF00FF}就这些{/color}{color=#0080FF}了。』{/color}"


    if judge_lm_condition([]):
        jump block_00003749

    return

label block_0000374D:
    # Node: 0000374D (TO: No idea)

    if judge_lm_condition([]):
        jump block_00003745

    return

label block_00003755:
    # Node: 00003755 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedTarget == 3" }]):
        jump block_0000374E
    if judge_lm_condition([]):
        jump block_00003768

    return

label block_0000374E:
    # Node: 0000374E (TO: 翼)

    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTsubasaState == 5" }]):
        jump block_00002A7E
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTsubasaState == 0" },{ "scope": 0, "content": "GSabuImechenTsubasaState == 1" },{ "scope": 1, "content": "C1SG1 == True" },{ "scope": 0, "content": "GSabuImechenTsubasaState == 2" },{ "scope": 1, "content": "C2SG1 == True" },{ "scope": 0, "content": "GSabuImechenTsubasaState == 3" },{ "scope": 1, "content": "C3SG1 == True" },{ "scope": 0, "content": "GSabuImechenTsubasaState == 4" },{ "scope": 1, "content": "C3SG2 == True" }]):
        jump block_0000245F
    if judge_lm_condition([]):
        jump block_00003753

    return

label block_00002A7E:
    # Node: 00002A7E (Review)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("(標準)")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "行了，已经没想法了！\n我想不出新的发型了。{w}要看看以前的设计么？"

    window hide

    $ set_window("イベントモード")

    if judge_lm_condition([]):
        jump block_00002A7D

    return

label block_00002A7D:
    # Node: 00002A7D (選擇)
    $ sys_lm_choice_item = ["看", "不想看"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_4
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"看\"" }]):
        jump block_00002445
    if judge_lm_condition([]):
        jump block_00003751

    return

label block_00002445:
    # Node: 00002445 (1)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_894199D30F034634AE608180960D7570 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_E6B1282B6A714F08AC52BD08D45B30DB as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002447

    return

label block_00002447:
    # Node: 00002447 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_301
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_00002448
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_00002450
    if judge_lm_condition([]):
        jump block_00003752

    return

label block_00002448:
    # Node: 00002448 (2)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_D0B42774E1274D47B41392CA1B52668E as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_CA93DB5E164B418D8979A23A156BC755 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002449

    return

label block_00002449:
    # Node: 00002449 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_302
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_0000244A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_00002445
    if judge_lm_condition([]):
        jump block_00003752

    return

label block_0000244A:
    # Node: 0000244A (3)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_E98C1D708D5B4A24BDDF904D56FCD559 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_3410CDDCD7754679B6CD5F56B085977F as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_0000244B

    return

label block_0000244B:
    # Node: 0000244B (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_303
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_0000244C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_00002448
    if judge_lm_condition([]):
        jump block_00003752

    return

label block_0000244C:
    # Node: 0000244C (4)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_C5C34814BD2A4070B3541007ED121A85 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_AE80962A08ED41FB884A2558F163B6FD as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_0000244D

    return

label block_0000244D:
    # Node: 0000244D (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_304
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_0000244E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_0000244A
    if judge_lm_condition([]):
        jump block_00003752

    return

label block_0000244E:
    # Node: 0000244E (5)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_A92B42BFF9B9482293D7D44EFF9D4539 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_B02AC07BA0764B1F99A0A086A27399D7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_0000244F

    return

label block_0000244F:
    # Node: 0000244F (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_305
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_00002450
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_0000244C
    if judge_lm_condition([]):
        jump block_00003752

    return

label block_00002450:
    # Node: 00002450 (6)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_5755D01206954077A7698867C1B875B6 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_D42796E0778C44F7AD67E4BC7A76442B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002451

    return

label block_00002451:
    # Node: 00002451 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_306
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_0000244E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_00002445
    if judge_lm_condition([]):
        jump block_00003752

    return

label block_00003751:
    # Node: 00003751 (不看)

    if judge_lm_condition([]):
        jump block_00003752

    return

label block_0000245F:
    # Node: 0000245F (PRE)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_BB9125A8E31E49DBB38AF58B4E2E4CCC as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_730C63C3A79F4EFB8591E4EA48D58136 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_E6B1282B6A714F08AC52BD08D45B30DB as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这家伙是不。行，说上就上！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=36}{color=#00FFFF}Let's IMECHEN！！{/color}{/size}"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 1

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Scene changing 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_589411E603304F8697C6E45AD2F54993 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57F79897CE2D49FC8E9CC05EC4072D27

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTsubasaState == 0" }]):
        jump block_00002460
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTsubasaState == 1" }]):
        jump block_00002461
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTsubasaState == 2" }]):
        jump block_00002462
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTsubasaState == 3" }]):
        jump block_00002463
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTsubasaState == 4" }]):
        jump block_00002464

    return

label block_00002460:
    # Node: 00002460 (1)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_CA93DB5E164B418D8979A23A156BC755 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『试着{/color}{color=#0080FF}{b}〈{/b}{/color}{color=#00FFFF}重塑造型{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哇、哇！好厉害！\n现在的发型还能改成这个样子呐。"


    if judge_lm_condition([]):
        jump block_0000374F

    return

label block_0000374F:
    # Node: 0000374F (RESET)
    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002ACB

    return

label block_00002ACB:
    # Node: 00002ACB (Tsubasa)
    $ GSabuImechenTsubasaState = GSabuImechenTsubasaState + 1

    if judge_lm_condition([]):
        jump block_00003750

    return

label block_00003750:
    # Node: 00003750 (TO: 選擇)

    if judge_lm_condition([]):
        jump block_0000374A

    return

label block_00002461:
    # Node: 00002461 (2)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_3410CDDCD7754679B6CD5F56B085977F as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『使用了改良后的重塑造型——{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}重塑造型2{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "总、总觉得本就不多的存在感现在一点不剩了。"


    if judge_lm_condition([]):
        jump block_0000374F

    return

label block_00002462:
    # Node: 00002462 (3)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_AE80962A08ED41FB884A2558F163B6FD as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『使用了{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}杀马特 (SMART){/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜哇！？？这、这是什么！？这是我……！？"


    if judge_lm_condition([]):
        jump block_0000374F

    return

label block_00002463:
    # Node: 00002463 (4)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_B02AC07BA0764B1F99A0A086A27399D7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}剪短{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这就像在说“快来欺负我”……"


    if judge_lm_condition([]):
        jump block_0000374F

    return

label block_00002464:
    # Node: 00002464 (5)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_D42796E0778C44F7AD67E4BC7A76442B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『做成了{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}流行风{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这、这就是流行……？不明觉厉……"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『一之濑翼的发型{/color}{color=#FF00FF}就这些{/color}{color=#0080FF}了。』{/color}"


    if judge_lm_condition([]):
        jump block_0000374F

    return

label block_00003753:
    # Node: 00003753 (TO: No idea)

    if judge_lm_condition([]):
        jump block_0000374D

    return

label block_00003768:
    # Node: 00003768 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedTarget == 4" }]):
        jump block_00003762
    if judge_lm_condition([]):
        jump block_00003770

    return

label block_00003762:
    # Node: 00003762 (TO: 月)

    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTsukiState == 4" }]):
        jump block_00002A7A
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTsukiState == 0" },{ "scope": 1, "content": "C1SG1 == True" },{ "scope": 0, "content": "GSabuImechenTsukiState == 1" },{ "scope": 1, "content": "C2SG1 == True" },{ "scope": 0, "content": "GSabuImechenTsukiState == 2" },{ "scope": 1, "content": "C3SG1 == True" },{ "scope": 0, "content": "GSabuImechenTsukiState == 3" },{ "scope": 1, "content": "C3SG2 == True" }]):
        jump block_0000246B
    if judge_lm_condition([]):
        jump block_00003763

    return

label block_00002A7A:
    # Node: 00002A7A (Review)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("(標準)")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "行了，已经没想法了！\n我想不出新的发型了。{w}要看看以前的设计么？"

    window hide

    $ set_window("イベントモード")

    if judge_lm_condition([]):
        jump block_00002A79

    return

label block_00002A79:
    # Node: 00002A79 (選擇)
    $ sys_lm_choice_item = ["看", "不想看"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_5
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"看\"" }]):
        jump block_000029F5
    if judge_lm_condition([]):
        jump block_00003767

    return

label block_000029F5:
    # Node: 000029F5 (1)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_894199D30F034634AE608180960D7570 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_3983E2874D6542E3834A737817C2EC54 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029F6

    return

label block_000029F6:
    # Node: 000029F6 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_307
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029F3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029EC
    if judge_lm_condition([]):
        jump block_00003766

    return

label block_000029F3:
    # Node: 000029F3 (2)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_A92B42BFF9B9482293D7D44EFF9D4539 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_3AA37179D6564E06B16D16BE8E676895 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029F4

    return

label block_000029F4:
    # Node: 000029F4 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_308
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029F1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029F5
    if judge_lm_condition([]):
        jump block_00003766

    return

label block_000029F1:
    # Node: 000029F1 (3)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_F12A780EBDA34DD59C3DD756969C2059 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_AF0BFAD9BBDC44D798A1A12BCC8077F9 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029F2

    return

label block_000029F2:
    # Node: 000029F2 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_309
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029ED
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029F3
    if judge_lm_condition([]):
        jump block_00003766

    return

label block_000029ED:
    # Node: 000029ED (4)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_4CC42B1EF0D74AF3BE60822D58A13172 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_A0527BA171B94D50BE6038E0DACEE91E as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029F0

    return

label block_000029F0:
    # Node: 000029F0 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_310
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029EC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029F1
    if judge_lm_condition([]):
        jump block_00003766

    return

label block_000029EC:
    # Node: 000029EC (5)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_C5C34814BD2A4070B3541007ED121A85 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_0229895F6C554C638930333569778988 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029EE

    return

label block_000029EE:
    # Node: 000029EE (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_311
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029F5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029ED
    if judge_lm_condition([]):
        jump block_00003766

    return

label block_00003767:
    # Node: 00003767 (不看)

    if judge_lm_condition([]):
        jump block_00003766

    return

label block_0000246B:
    # Node: 0000246B (PRE)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_BB9125A8E31E49DBB38AF58B4E2E4CCC as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_5091BF764256440993A63CD926D0E369 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_3983E2874D6542E3834A737817C2EC54 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这家伙是不。行，说上就上！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=36}{color=#00FFFF}Let's IMECHEN！！{/color}{/size}"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 1

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Scene changing 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_589411E603304F8697C6E45AD2F54993 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57F79897CE2D49FC8E9CC05EC4072D27

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTsukiState == 0" }]):
        jump block_0000246C
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTsukiState == 1" }]):
        jump block_0000246D
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTsukiState == 2" }]):
        jump block_0000246E
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenTsukiState == 3" }]):
        jump block_0000246F

    return

label block_0000246C:
    # Node: 0000246C (1)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_3AA37179D6564E06B16D16BE8E676895 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}剪短{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯，很方便活动，很好。"


    if judge_lm_condition([]):
        jump block_00003764

    return

label block_00003764:
    # Node: 00003764 (RESET)
    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002ACC

    return

label block_00002ACC:
    # Node: 00002ACC (Tsuki)
    $ GSabuImechenTsukiState = GSabuImechenTsukiState + 1

    if judge_lm_condition([]):
        jump block_00003765

    return

label block_00003765:
    # Node: 00003765 (TO: 選擇)

    if judge_lm_condition([]):
        jump block_00003750

    return

label block_0000246D:
    # Node: 0000246D (2)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_AF0BFAD9BBDC44D798A1A12BCC8077F9 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『变成{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}长发{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "哈哈哈，空看到肯定会吓一跳的。"


    if judge_lm_condition([]):
        jump block_00003764

    return

label block_0000246E:
    # Node: 0000246E (3)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_A0527BA171B94D50BE6038E0DACEE91E as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『把头发{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}熨了{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这就是所谓的时下风啊。\n也许有人觉得好，但至少我觉得不好。"


    if judge_lm_condition([]):
        jump block_00003764

    return

label block_0000246F:
    # Node: 0000246F (4)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_0229895F6C554C638930333569778988 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『使用了{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}杀马特 (SMART){/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "绝对不能带着这种发型练习剑道。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『赤峰月的发型{/color}{color=#FF00FF}就这些{/color}{color=#0080FF}了。』{/color}"


    if judge_lm_condition([]):
        jump block_00003764

    return

label block_00003763:
    # Node: 00003763 (TO: No idea)

    if judge_lm_condition([]):
        jump block_00003753

    return

label block_00003770:
    # Node: 00003770 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedTarget == 5" }]):
        jump block_00003769
    if judge_lm_condition([]):
        jump block_00003777

    return

label block_00003769:
    # Node: 00003769 (TO: 空)

    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSoraState == 4" }]):
        jump block_00002A86
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSoraState == 0" },{ "scope": 1, "content": "C1SG1 == True" },{ "scope": 0, "content": "GSabuImechenSoraState == 1" },{ "scope": 1, "content": "C2SG1 == True" },{ "scope": 0, "content": "GSabuImechenSoraState == 2" },{ "scope": 1, "content": "C3SG1 == True" },{ "scope": 0, "content": "GSabuImechenSoraState == 3" },{ "scope": 1, "content": "C3SG2 == True" }]):
        jump block_00002478
    if judge_lm_condition([]):
        jump block_0000376A

    return

label block_00002A86:
    # Node: 00002A86 (Review)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("(標準)")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "行了，已经没想法了！\n我想不出新的发型了。{w}要看看以前的设计么？"

    window hide

    $ set_window("イベントモード")

    if judge_lm_condition([]):
        jump block_00002A85

    return

label block_00002A85:
    # Node: 00002A85 (選擇)
    $ sys_lm_choice_item = ["看", "不想看"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_6
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"看\"" }]):
        jump block_000029FF
    if judge_lm_condition([]):
        jump block_0000376E

    return

label block_000029FF:
    # Node: 000029FF (1)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_894199D30F034634AE608180960D7570 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_AA79FD55320E4C6194C0DD2CBE71F207 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002A00

    return

label block_00002A00:
    # Node: 00002A00 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_312
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029FD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029F7
    if judge_lm_condition([]):
        jump block_0000376F

    return

label block_000029FD:
    # Node: 000029FD (2)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_A92B42BFF9B9482293D7D44EFF9D4539 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_0D8A1505E1B043ACAC577AEB479DB79C as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029FE

    return

label block_000029FE:
    # Node: 000029FE (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_313
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029F9
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029FF
    if judge_lm_condition([]):
        jump block_0000376F

    return

label block_000029F9:
    # Node: 000029F9 (3)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_F12A780EBDA34DD59C3DD756969C2059 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_F3A29FBF00064D019AB7706E4C9C02B6 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029FC

    return

label block_000029FC:
    # Node: 000029FC (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_314
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029F8
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029FD
    if judge_lm_condition([]):
        jump block_0000376F

    return

label block_000029F8:
    # Node: 000029F8 (4)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_4CC42B1EF0D74AF3BE60822D58A13172 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_707A07A566244756A4CF71F3E024004B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029FA

    return

label block_000029FA:
    # Node: 000029FA (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_315
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029F7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029F9
    if judge_lm_condition([]):
        jump block_0000376F

    return

label block_000029F7:
    # Node: 000029F7 (5)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_5755D01206954077A7698867C1B875B6 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_A905D928D0914A20B932E5B8C07CD8B7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029FB

    return

label block_000029FB:
    # Node: 000029FB (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_316
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029FF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029F8
    if judge_lm_condition([]):
        jump block_0000376F

    return

label block_0000376E:
    # Node: 0000376E (不看)

    if judge_lm_condition([]):
        jump block_0000376F

    return

label block_00002478:
    # Node: 00002478 (PRE)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_BB9125A8E31E49DBB38AF58B4E2E4CCC as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_C310E7BEA01C48469BE4D363D5DFFE85 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_AA79FD55320E4C6194C0DD2CBE71F207 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这家伙是不。行，说上就上！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=36}{color=#00FFFF}Let's IMECHEN！！{/color}{/size}"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 1

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Scene changing 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_589411E603304F8697C6E45AD2F54993 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57F79897CE2D49FC8E9CC05EC4072D27

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSoraState == 0" }]):
        jump block_00002474
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSoraState == 1" }]):
        jump block_00002475
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSoraState == 2" }]):
        jump block_00002476
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSoraState == 3" }]):
        jump block_00002477

    return

label block_00002474:
    # Node: 00002474 (1)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_0D8A1505E1B043ACAC577AEB479DB79C as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}剪短{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "剪短头发会不会显得更小啊……"


    if judge_lm_condition([]):
        jump block_0000376C

    return

label block_0000376C:
    # Node: 0000376C (RESET)
    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002ACD

    return

label block_00002ACD:
    # Node: 00002ACD (Sora)
    $ GSabuImechenSoraState = GSabuImechenSoraState + 1

    if judge_lm_condition([]):
        jump block_0000376D

    return

label block_0000376D:
    # Node: 0000376D (TO: 選擇)

    if judge_lm_condition([]):
        jump block_00003765

    return

label block_00002475:
    # Node: 00002475 (2)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_F3A29FBF00064D019AB7706E4C9C02B6 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『变成{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}长发{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哇，和我完全不像了。"


    if judge_lm_condition([]):
        jump block_0000376C

    return

label block_00002476:
    # Node: 00002476 (3)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_707A07A566244756A4CF71F3E024004B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『把头发{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}熨了{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊，这个或许不错！想让哥哥也看看呐。"


    if judge_lm_condition([]):
        jump block_0000376C

    return

label block_00002477:
    # Node: 00002477 (4)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_A905D928D0914A20B932E5B8C07CD8B7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『做成了{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}流行风{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "好厉害！这种我自己是无论如何都做不出来的哦。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『赤峰空的发型{/color}{color=#FF00FF}就这些{/color}{color=#0080FF}了。』{/color}"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_0000376C

    return

label block_0000376A:
    # Node: 0000376A (TO: No idea)

    if judge_lm_condition([]):
        jump block_00003763

    return

label block_00003777:
    # Node: 00003777 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedTarget == 6" }]):
        jump block_00003771
    if judge_lm_condition([]):
        jump block_00003779

    return

label block_00003771:
    # Node: 00003771 (TO: 作哉)

    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSakuyaState == 5" }]):
        jump block_00002A80
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSakuyaState == 0" },{ "scope": 0, "content": "GSabuImechenSakuyaState == 1" },{ "scope": 1, "content": "C1SG1 == True" },{ "scope": 0, "content": "GSabuImechenSakuyaState == 2" },{ "scope": 1, "content": "C2SG1 == True" },{ "scope": 0, "content": "GSabuImechenSakuyaState == 3" },{ "scope": 1, "content": "C3SG1 == True" },{ "scope": 0, "content": "GSabuImechenSakuyaState == 4" },{ "scope": 1, "content": "C3SG2 == True" }]):
        jump block_00002465
    if judge_lm_condition([]):
        jump block_00003774

    return

label block_00002A80:
    # Node: 00002A80 (Review)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("(標準)")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "行了，已经没想法了！\n我想不出新的发型了。{w}要看看以前的设计么？"

    window hide

    $ set_window("イベントモード")

    if judge_lm_condition([]):
        jump block_00002A7F

    return

label block_00002A7F:
    # Node: 00002A7F (選擇)
    $ sys_lm_choice_item = ["看", "不想看"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_7
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"看\"" }]):
        jump block_000029E9
    if judge_lm_condition([]):
        jump block_00003776

    return

label block_000029E9:
    # Node: 000029E9 (1)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_894199D30F034634AE608180960D7570 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_C9B9F5E00E8149FCADB791E475237446 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029EA

    return

label block_000029EA:
    # Node: 000029EA (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_317
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029E7
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029DF
    if judge_lm_condition([]):
        jump block_00003775

    return

label block_000029E7:
    # Node: 000029E7 (2)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_BBC048B62C9E43909547D0860C90C723 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_CA440EE67348463AB92D9447C63F647D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029E8

    return

label block_000029E8:
    # Node: 000029E8 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_318
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029E5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029E9
    if judge_lm_condition([]):
        jump block_00003775

    return

label block_000029E5:
    # Node: 000029E5 (3)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_4CC42B1EF0D74AF3BE60822D58A13172 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_B11E1CF01B064E5DB126023B7A28B32B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029E6

    return

label block_000029E6:
    # Node: 000029E6 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_319
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029E3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029E7
    if judge_lm_condition([]):
        jump block_00003775

    return

label block_000029E3:
    # Node: 000029E3 (4)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_D0B42774E1274D47B41392CA1B52668E as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_0A0DC856099A47ACA9BC66ACFE22BBEA as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029E4

    return

label block_000029E4:
    # Node: 000029E4 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_320
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029E1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029E5
    if judge_lm_condition([]):
        jump block_00003775

    return

label block_000029E1:
    # Node: 000029E1 (5)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_A92B42BFF9B9482293D7D44EFF9D4539 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_14DFAF47AE73453C9BCDFD7B31D9954F as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029E2

    return

label block_000029E2:
    # Node: 000029E2 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_321
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029DF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029E3
    if judge_lm_condition([]):
        jump block_00003775

    return

label block_000029DF:
    # Node: 000029DF (6)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_5755D01206954077A7698867C1B875B6 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_583B82EEF7ED428F81D15A3E3F81D3A8 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_000029E0

    return

label block_000029E0:
    # Node: 000029E0 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_322
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_000029E1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_000029E9
    if judge_lm_condition([]):
        jump block_00003775

    return

label block_00003776:
    # Node: 00003776 (不看)

    if judge_lm_condition([]):
        jump block_00003775

    return

label block_00002465:
    # Node: 00002465 (PRE)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_BB9125A8E31E49DBB38AF58B4E2E4CCC as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_C64218A33F3C419F8C84F6FCFE71A376 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_C9B9F5E00E8149FCADB791E475237446 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这家伙是不。行，说上就上！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=36}{color=#00FFFF}Let's IMECHEN！！{/color}{/size}"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 1

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Scene changing 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_589411E603304F8697C6E45AD2F54993 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57F79897CE2D49FC8E9CC05EC4072D27

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSakuyaState == 0" }]):
        jump block_00002466
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSakuyaState == 1" }]):
        jump block_00002467
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSakuyaState == 2" }]):
        jump block_00002468
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSakuyaState == 3" }]):
        jump block_00002469
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSakuyaState == 4" }]):
        jump block_0000246A

    return

label block_00002466:
    # Node: 00002466 (1)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_CA440EE67348463AB92D9447C63F647D as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}小修小改{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了一下！』{/color}"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "诶，本来前面的头发就很碍事，\n不错，看看社团活动时怎么样好了。"


    if judge_lm_condition([]):
        jump block_00003772

    return

label block_00003772:
    # Node: 00003772 (RESET)
    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002ACE

    return

label block_00002ACE:
    # Node: 00002ACE (Sakuya)
    $ GSabuImechenSakuyaState = GSabuImechenSakuyaState + 1

    if judge_lm_condition([]):
        jump block_00003773

    return

label block_00003773:
    # Node: 00003773 (TO: 選擇)

    if judge_lm_condition([]):
        jump block_0000376D

    return

label block_00002467:
    # Node: 00002467 (2)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_B11E1CF01B064E5DB126023B7A28B32B as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『把头发{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}熨了{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……很不想这么说，但有股地痞流氓感。"


    if judge_lm_condition([]):
        jump block_00003772

    return

label block_00002468:
    # Node: 00002468 (3)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_0A0DC856099A47ACA9BC66ACFE22BBEA as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『试着{/color}{color=#0080FF}{b}〈{/b}{/color}{color=#00FFFF}重塑造型{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "想、想笑就笑啊……反正本来就不合适。"


    if judge_lm_condition([]):
        jump block_00003772

    return

label block_00002469:
    # Node: 00002469 (4)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_14DFAF47AE73453C9BCDFD7B31D9954F as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}剪短{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "欸——欸——不错嘛。其实想想这么短也挺好的。"


    if judge_lm_condition([]):
        jump block_00003772

    return

label block_0000246A:
    # Node: 0000246A (5)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_583B82EEF7ED428F81D15A3E3F81D3A8 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『做成了{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}流行风{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "猫山，你绝对是在胡闹。这东西也叫流行！？"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『穂海作哉的发型{/color}{color=#FF00FF}就这些{/color}{color=#0080FF}了。』{/color}"


    if judge_lm_condition([]):
        jump block_00003772

    return

label block_00003774:
    # Node: 00003774 (TO: No idea)

    if judge_lm_condition([]):
        jump block_0000376A

    return

label block_00003779:
    # Node: 00003779 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedTarget == 7" }]):
        jump block_00003778

    return

label block_00003778:
    # Node: 00003778 (TO: 三朗)

    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSaburoState == 4" }]):
        jump block_00002A82
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSaburoState == 0" },{ "scope": 1, "content": "C1SG1 == True" },{ "scope": 0, "content": "GSabuImechenSaburoState == 1" },{ "scope": 1, "content": "C2SG1 == True" },{ "scope": 0, "content": "GSabuImechenSaburoState == 2" },{ "scope": 1, "content": "C3SG1 == True" },{ "scope": 0, "content": "GSabuImechenSaburoState == 3" },{ "scope": 1, "content": "C3SG2 == True" }]):
        jump block_0000247D
    if judge_lm_condition([]):
        jump block_0000377A

    return

label block_00002A82:
    # Node: 00002A82 (Review)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ set_window("(標準)")
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "行了，已经没想法了！\n我想不出新的发型了。{w}要看看以前的设计么？"

    window hide

    $ set_window("イベントモード")

    if judge_lm_condition([]):
        jump block_00002A81

    return

label block_00002A81:
    # Node: 00002A81 (選擇)
    $ sys_lm_choice_item = ["看", "不想看"]
    $ sys_lm_choice_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_choice(sys_lm_choice_item, sys_lm_choice_sound, 0) from _call_lm_choice_8
    $ del sys_lm_choice_item
    $ del sys_lm_choice_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"看\"" }]):
        jump block_00002A09
    if judge_lm_condition([]):
        jump block_0000377E

    return

label block_00002A09:
    # Node: 00002A09 (1)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_894199D30F034634AE608180960D7570 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_CCC94E3EE52C403B8603610866670DB7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002A0A

    return

label block_00002A0A:
    # Node: 00002A0A (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_323
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_00002A07
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_00002A01
    if judge_lm_condition([]):
        jump block_0000377D

    return

label block_00002A07:
    # Node: 00002A07 (2)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_E6276A6B6BAB45928A46E9AB7B036BD1 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_675ACF90DAB5469BAE539C5AAC6FBDCE as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002A08

    return

label block_00002A08:
    # Node: 00002A08 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_324
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_00002A05
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_00002A09
    if judge_lm_condition([]):
        jump block_0000377D

    return

label block_00002A05:
    # Node: 00002A05 (3)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_C5C34814BD2A4070B3541007ED121A85 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_7B7958DF419C46338578545DECFB0FC6 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002A06

    return

label block_00002A06:
    # Node: 00002A06 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_325
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_00002A02
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_00002A07
    if judge_lm_condition([]):
        jump block_0000377D

    return

label block_00002A02:
    # Node: 00002A02 (4)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_A92B42BFF9B9482293D7D44EFF9D4539 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_41A63C6A68184B67BFDDE7FC82A440C6 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002A03

    return

label block_00002A03:
    # Node: 00002A03 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_326
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_00002A01
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_00002A05
    if judge_lm_condition([]):
        jump block_0000377D

    return

label block_00002A01:
    # Node: 00002A01 (5)
    if sys_effect2_current_file != "sound/Effect Sound/Clipper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clipper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clipper 1.ogg"

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_4CC42B1EF0D74AF3BE60822D58A13172 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_64F290CC0B9444A5AD38CFAAD8286ECC as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398


    if judge_lm_condition([]):
        jump block_00002A04

    return

label block_00002A04:
    # Node: 00002A04 (Navigator)
    $ sys_lm_menu_item = [{"pos": (672, 528),"type": "textbutton","text":_("返回"),"style":"saburou_imechen_back_button_2","name": "戻る"}, {"pos": (626, 280),"image": "images/Saburos-Salon/Next.png","hover": "images/Saburos-Salon/Next hover.png","name": "右"}, {"pos": (95, 280),"image": "images/Saburos-Salon/Previous.png","hover": "images/Saburos-Salon/Previous hover.png","name": "左"}]
    $ sys_lm_menu_sound = {}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0, -0.001) from _call_lm_menu_327
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"右\"" }]):
        jump block_00002A09
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"左\"" }]):
        jump block_00002A02
    if judge_lm_condition([]):
        jump block_0000377D

    return

label block_0000377E:
    # Node: 0000377E (不看)

    if judge_lm_condition([]):
        jump block_0000377D

    return

label block_0000247D:
    # Node: 0000247D (PRE)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_BB9125A8E31E49DBB38AF58B4E2E4CCC as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_DE5160B4388142C6ABE1E93389C14B57 as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_CCC94E3EE52C403B8603610866670DB7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这家伙是不。\n等下，我！？……算了，上就上。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=36}{color=#00FFFF}Let's IMECHEN！！{/color}{/size}"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 1

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Scene changing 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_589411E603304F8697C6E45AD2F54993 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57F79897CE2D49FC8E9CC05EC4072D27

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"


    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSaburoState == 0" }]):
        jump block_00002479
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSaburoState == 1" }]):
        jump block_0000247A
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSaburoState == 2" }]):
        jump block_0000247B
    if judge_lm_condition([{ "scope": 0, "content": "GSabuImechenSaburoState == 3" }]):
        jump block_0000247C

    return

label block_00002479:
    # Node: 00002479 (1)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_675ACF90DAB5469BAE539C5AAC6FBDCE as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『采用了{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}无发胶{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}设计！』{/color}"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呜……没有发胶提不起精神——"


    if judge_lm_condition([]):
        jump block_0000377B

    return

label block_0000377B:
    # Node: 0000377B (RESET)
    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00002ACF

    return

label block_00002ACF:
    # Node: 00002ACF (Saburo)
    $ GSabuImechenSaburoState = GSabuImechenSaburoState + 1

    if judge_lm_condition([]):
        jump block_0000377C

    return

label block_0000377C:
    # Node: 0000377C (TO: 選擇)

    if judge_lm_condition([]):
        jump block_00003773

    return

label block_0000247A:
    # Node: 0000247A (2)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_7B7958DF419C46338578545DECFB0FC6 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『使用了{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}杀马特 (SMART){/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "如何！挺硬的不！"


    if judge_lm_condition([]):
        jump block_0000377B

    return

label block_0000247B:
    # Node: 0000247B (3)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_41A63C6A68184B67BFDDE7FC82A440C6 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}剪短{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}了！』{/color}"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "短发也不错是不是？我不管什么都合适呐——♪"


    if judge_lm_condition([]):
        jump block_0000377B

    return

label block_0000247C:
    # Node: 0000247C (4)
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_64F290CC0B9444A5AD38CFAAD8286ECC as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『把头发{/color}{color=#00FFFF}{b}〈{/b}{/color}{color=#00FFFF}熨了{/color}{color=#00FFFF}{b}〉{/b}{/color}{color=#0080FF}！』{/color}"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "时下的熨发也很合适！不愧是我。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『猫山三朗的发型{/color}{color=#FF00FF}就这些{/color}{color=#0080FF}了。』{/color}"


    if judge_lm_condition([]):
        jump block_0000377B

    return

label block_0000377A:
    # Node: 0000377A (TO: No idea)

    if judge_lm_condition([]):
        jump block_00003774

    return

label block_00003738:
    # Node: 00003738 (SetTarget: 翼)
    $ SelectedTarget = 3

    if judge_lm_condition([]):
        jump block_0000373D

    return

label block_0000373B:
    # Node: 0000373B (SetTarget: 作哉)
    $ SelectedTarget = 6

    if judge_lm_condition([]):
        jump block_0000373D

    return

label block_00003737:
    # Node: 00003737 (SetTarget: 忍)
    $ SelectedTarget = 2

    if judge_lm_condition([]):
        jump block_0000373D

    return

label block_00003739:
    # Node: 00003739 (SetTarget: 月)
    $ SelectedTarget = 4

    if judge_lm_condition([]):
        jump block_0000373D

    return

label block_0000373A:
    # Node: 0000373A (SetTarget: 空)
    $ SelectedTarget = 5

    if judge_lm_condition([]):
        jump block_0000373D

    return

label block_0000373C:
    # Node: 0000373C (SetTarget: 三朗)
    $ SelectedTarget = 7

    if judge_lm_condition([]):
        jump block_0000373D

    return

label block_00003736:
    # Node: 00003736 (SetTarget: 慎太郎)
    $ SelectedTarget = 1

    if judge_lm_condition([]):
        jump block_0000373D

    return

label block_00003781:
    # Node: 00003781 (RESET)
    stop music fadeout 0.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00003692

    return

label block_00003692:
    # Node: 00003692 ()
    $ del SelectedTarget

    return

label block_00001195:
    # Node: 00001195 (Background CP1)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_589411E603304F8697C6E45AD2F54993 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.35

    show rs_image_D7AC7403C04640D483DCA1818D0D32FB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_3162A701832142CCB65B73EEA9FB0323 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.4

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "HEY，欢迎光临！！来做个好的形象！"


    if judge_lm_condition([{ "scope": 0, "content": "CXQSabuImechen == False" }]):
        jump block_00001196
    if judge_lm_condition([]):
        jump block_00002443

    return

label block_00001196:
    # Node: 00001196 (First time)
    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "客人是第一次来？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "本店可以免费提供和平时不一个口味的{color=#00FFFF}形象转换{/color}哦～"

    window hide

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    show rs_image_566D296EAB9E4AC48A093665CD619A3F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E


    if judge_lm_condition([]):
        jump block_00002483

    return

label block_00002483:
    # Node: 00002483 (選擇)
    $ sys_lm_menu_item = [{"pos": (8, 152),"image": "images/Saburos-Salon/AVATAR/Tomo.png","hover": "images/Saburos-Salon/AVATAR/Tomo hover.png","name": "友"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, -0.001) from _call_lm_menu_328
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([]):
        jump block_00002484

    return

label block_00002484:
    # Node: 00002484 (友)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    show rs_image_00E77EE8BD7447E6A8930277008B1CBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_BB9125A8E31E49DBB38AF58B4E2E4CCC as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    $ zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 = 100
    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_DC9ADBFBED9F4E669FC42A99F64FFD2E as tag_CCB6D21AA43D4C57B10D3D14A711E963 at center_top zorder zorder_tag_CCB6D21AA43D4C57B10D3D14A711E963 onlayer master
    show rs_image_C34B7E515C454982A4812C9E32BD50E7 as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好咧！赌上我的本事，给你弄个好造型！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=36}{color=#00FFFF}Let's IMECHEN！！{/color}{/size}"

    window hide

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    pause 0.7


    if judge_lm_condition([]):
        jump block_00002440

    return

label block_00002440:
    # Node: 00002440 (1)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Scene changing 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_589411E603304F8697C6E45AD2F54993 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57F79897CE2D49FC8E9CC05EC4072D27

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_F12981B3CF794DEA86CFB94275B48CFB = 300
    show rs_image_2A054FA123984C2AAB5FF6EF7EA2729C as tag_F12981B3CF794DEA86CFB94275B48CFB at center_bottom zorder zorder_tag_F12981B3CF794DEA86CFB94275B48CFB onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『头发终于被{/color}{color=#00FFFF}拉直{/color}{color=#0080FF}了！』{/color}"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嘛，差不多就这样了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦！不错！！梦寐以求的直发——！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "现在我能想到的样式还很少，\n{color=#00FFFF}多经历一些事再回来{/color}应该会多起来！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "还有，换什么造型全看我钦定，\n有些兴趣在里面就忍忍好了。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "之后会给你复原的，并不会真剪下去，\n放心就是。再怎么说就是玩玩嘛！"

    window hide

    pause 0.8

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_F12981B3CF794DEA86CFB94275B48CFB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 1

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00002A76

    return

label block_00002A76:
    # Node: 00002A76 (Tomo)
    $ GSabuImechenTomoState = GSabuImechenTomoState + 1

    if judge_lm_condition([]):
        jump block_00002488

    return

label block_00002488:
    # Node: 00002488 (Roof)
    $ set_window("(標準)")
    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_place_title(_("屋顶"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.4


    if judge_lm_condition([]):
        jump block_00002487

    return

label block_00002487:
    # Node: 00002487 (三朗)
    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    window show

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_104E19984CF747D19D3CC74E9452E4A0 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_bottom zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "感谢帮忙——！"

    show rs_image_562F2C0F75454AEC893C9821564C213D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "最近有些喜欢上帮人弄头发了。\n改改发型就能变形象，是不是很有意思？"

    show rs_image_2D4319C2F7C346428F7F6BAA6DAFF9CB as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "后面会练出更多好看的发型的，记得常来哦♪"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if judge_lm_condition([]):
        jump block_00002489

    return

