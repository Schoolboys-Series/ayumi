# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003AA2 (FLAG: 我是直的，現無對象)

label block_00003AA3:
    # Node: 00003AA3 ()

    if judge_lm_condition([]):
        jump block_00003AA5

    return

label block_00003AA5:
    # Node: 00003AA5 (Phase: 99)
    if Not(VarExists("C2S4Phase")):
        $ C2S4Phase = 0
    $ C2S4Phase = 99

    if judge_lm_condition([]):
        jump block_00003AA4

    return

label block_00003AA4:
    # Node: 00003AA4 (F4 START)
    call scb_flag_title(2, _("「我是直的，现无对象」")) from _call_scb_flag_title_5

    if judge_lm_condition([]):
        jump block_00003AA6

    return

label block_00003AA6:
    # Node: 00003AA6 (我是直的，現無對象 1)
    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Battle 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 2.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_AB6075791E544455A4C21B3DCBA52E1C as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 1.5

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_222BBB56F7BA4025B3E942F40786CBC9

    if sys_music_current_file != "sound/BGM/Something comical 1.ogg":
        play music "sound/BGM/Something comical 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something comical 1.ogg"

    window show

    pause 0.3

    rs_character_6E824DBDDF4448E1ADD5937984ABFE61 "不行……心理准备还……"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "都到这一步了，就不要压抑自己的欲望了嘛，呐，行不行？"

    rs_character_6E824DBDDF4448E1ADD5937984ABFE61 "嗯……为了三朗君，我会加油的……"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈哈，一起向着快感的高峰出发！"

    rs_character_6E824DBDDF4448E1ADD5937984ABFE61 "嗯，不过，我还是第一次，会不会痛呢……"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "没事儿，我的技术可是很好的，可是学习了很多钻研出来的。"

    rs_character_6E824DBDDF4448E1ADD5937984ABFE61 "嗯嗯……我不是在说这个。我是在说三朗君会不会觉得痛。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "欸？我不会痛。\n"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    extend "诶……不是这么回事儿么？"

    rs_character_6E824DBDDF4448E1ADD5937984ABFE61 "诶？是吗？那就好。那我就不用在意了。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嗯、嗯！吓了一跳～果然还是预习不足呐。"

    rs_character_6E824DBDDF4448E1ADD5937984ABFE61 "抱歉抱歉，三郎君会自己预习的话，就是做那个呐。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嗯。{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "……嗯？"

    rs_character_6E824DBDDF4448E1ADD5937984ABFE61 "谢谢，没想到会尝试开发自己。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嗯{w=0.35}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "嗯？"

    stop music fadeout 2
    $ sys_music_current_file = ""

    rs_character_6E824DBDDF4448E1ADD5937984ABFE61 "那为了回应这股努力，\n"
    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_368B77480A054493BB9DAE441AA65BC2

    if sys_music_current_file != "sound/BGM/Angel and Demon.ogg":
        play music "sound/BGM/Angel and Demon.ogg" loop
        $ sys_music_current_file = "sound/BGM/Angel and Demon.ogg"

    extend "{size=28}{color=#FF0000}我会好好干（三朗）的！{/color}{/size}"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "诶！？"

    if sys_effect_current_file != "sound/Effect Sound/Yoo 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Yoo 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Yoo 1.ogg"

    rs_character_6E824DBDDF4448E1ADD5937984ABFE61 "三朗君，请接受我全身心的爱（和那个）！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "诶！？"
    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_28F784D09B6C4DC7923149F266748707 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{size=36}哈啊啊啊啊！？！？{/size}"

    window hide

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 0.4

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_FB2122B2C37749959CAE94CCB5D33314 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1EE78B9E5E0C4B64B6BF7F897E926F62

    pause 0.8

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_D544765C4BA64EC6B46D01C4A92BD5D1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/BGM/Daily 2.ogg":
        play music "sound/BGM/Daily 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 2.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈……哈……哈……是、是梦……太好了。"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "混蛋，可恶的同志诱惑……最后还是混入我的梦境里了么！！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "同志退散！！同志退散！！哈！呀！哈！呀！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我是……{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{size=32}直的啊啊啊啊啊！！！{/size}"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    rs_character_9EDF48057FB84D428D56198A69E2880E "呼……呼……"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊？"
    if sys_effect_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FB2122B2C37749959CAE94CCB5D33314 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……我去！！！\n为为为、为何这家伙会睡在旁边！？！？"

    window hide

    pause 0.5

    # Gallery unlock: images/CG/I-am-none-gay-with-no-lovers/I-am-none-gay-with-no-lovers 3.png
    $ zorder_rs_image_17EE1054E0774C6E887A51B6D6F9809F = -100
    show rs_image_17EE1054E0774C6E887A51B6D6F9809F as rs_image_17EE1054E0774C6E887A51B6D6F9809F zorder zorder_rs_image_17EE1054E0774C6E887A51B6D6F9809F onlayer master
    hide rs_image_17EE1054E0774C6E887A51B6D6F9809F

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_17EE1054E0774C6E887A51B6D6F9809F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.5

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "负责警戒的猫呢！！？\n"
    if sys_effect3_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    extend "啊？！被木天蓼放倒了……"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "切……一网打尽啊……奥村慎太郎，恐怖的存在！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼……"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不过说起来……{w}来都来了还睡个什么劲儿。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这里不是该我吐槽不许夜袭么？没个装傻的槽就没法吐了啊。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……呃！！别摆出一副可爱的睡脸啊！\n尤其是软软的脸和猫一样的嘴……"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=15}……{/size}"
    extend "{size=15}……一直都让我那么遭罪，\n偶尔也让我报复一下嘛{/size}{w}{size=15}……笨蛋。{/size}"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "………"
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    extend "不对我说什么胡话！？\n不对不对不对！！那不是我的意思！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊——不干了！全都是木天蓼的错！！\n那么闹心的梦也是，莫名其妙的话也是……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我绝对不是那个意思！\n"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    extend "我是、{size=28}直的啊啊啊！！！{/size}"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……三酱……呼呼。"

    if sys_effect2_current_file != "sound/Effect Sound/Worried 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Worried 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Worried 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "诶？梦话……梦、梦到我了……？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……{w}……"
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    stop music fadeout 0.5
    $ sys_music_current_file = ""

    extend "好烦……呼……"

    if sys_effect_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……"

    window hide

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2


    if judge_lm_condition([]):
        jump block_00003AA7

    return

label block_00003AA7:
    # Node: 00003AA7 (CP2 Daytime 三朗)
    call block_00001106 from _call_block_00001106

    if judge_lm_condition([]):
        jump block_00003AA9

    return

label block_00003AA9:
    # Node: 00003AA9 (我是直的，現無對象 2)
    $ set_window("イベントモード")
    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Scene changing 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_001EA37977AB4970A356FF4439EE6480

    stop music fadeout 0.5
    $ sys_music_current_file = ""

    pause 0.7

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    if sys_music_current_file != "sound/BGM/Twilight.ogg":
        play music "sound/BGM/Twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Twilight.ogg"

    show rs_image_E438E07503F648BB805CA72FB7D9AC70 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_FAE04D9AEB58490C92EEB463378364AF

    pause 0.7

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A08F830C7B7A48D9AE269614FEAC7E8C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.5

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_AAC229C565304B76BADD3819ED261CD1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不管走到什么地方都只有同志。\n到底怎么了啊，这个世界～～～！"

    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……嗯？{w=0.45}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_center zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3C9E62B61C1744D1BDFDAD9A5EDD41C6 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊……呀♪那边的是御咲女学院的各位～♪"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_center zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_DFA5315B887F4308A9E050235004ED07 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "香气飘飘，空气也那么纯洁。吸……呼……啊，好香。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_center zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E54B94670E804565963ECDB491A87076 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "果然还是女孩子好，一次也好，想在床上试试翻云♪覆雨呐～"

    show rs_image_9BD814B82EB04FBCA4D4A9D9FE4C070D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "肯定会是可爱的脸蛋和平稳的呼吸……脸也软软的。\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_center zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "比起来男人就烂多了！！{w}要是能变成女人就好了！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊，不行，\n真的变了的话我不就像刚才梦里那样会被男人给抱……"
    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_center zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "恶——！！"

    window hide

    pause 0.5

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    window show

    rs_character_A1E4458713DF4089A94BCAD1B8D4D614 "啊啊～男生之间的恋爱真是凄美！\n好想看看他们结婚的样子。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_4A2CA25FB4B640959638DB7E4E820D2A "不久之前，\n{color=#00FFFF}有个很矮的男孩子华丽地把他的朋友公主抱下了车{/color}呐！"

    rs_character_4A2CA25FB4B640959638DB7E4E820D2A "肯定直接带回家，整晚都在做这样的～那样的事哦♪"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_DC955F52E6A64DA4AF5EE9FFC2512F9C "呀——！那是什么好想看！！最棒了♪{w}\n说起电车，我也在车站看到过！"

    rs_character_DC955F52E6A64DA4AF5EE9FFC2512F9C "{color=#00FFFF}社团活动结束后的男孩子就这么\n靠着别的男孩子睡着了{/color}！真的很亲密哦！"

    rs_character_DC955F52E6A64DA4AF5EE9FFC2512F9C "而且那两个人看上去像是兄弟哦……禁断的爱！"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=36}{color=#FF80C0}妄想停不下来～♪{/color}{/size}"

    pause 0.35

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_9C6627EBA4894AB883E9F13296A23034 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_FB2122B2C37749959CAE94CCB5D33314 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if sys_effect_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9CE409DAE147469DBD509038CF1C42F0

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "噫！！拜托了你们别也被同志恶灵附身了……！！"

    window hide

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    stop music fadeout 2
    $ sys_music_current_file = ""

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A08F830C7B7A48D9AE269614FEAC7E8C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_center zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔！！什么飞过来了！\n"
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_7C42D527AA2A48348F9A478BB5F543EC as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    extend "……陆田和杉本的……应援海报……？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呃！！就是因为这种东西到处乱贴同志气氛才这么重的。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_music_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music_current_file = "sound/Effect Sound/Wind 1.ogg"

    # Gallery unlock: images/CG/I-am-none-gay-with-no-lovers/I-am-none-gay-with-no-lovers 2.png
    $ zorder_rs_image_C514C7B43BB94588B7E6F6DE0405902C = -100
    show rs_image_C514C7B43BB94588B7E6F6DE0405902C as rs_image_C514C7B43BB94588B7E6F6DE0405902C zorder zorder_rs_image_C514C7B43BB94588B7E6F6DE0405902C onlayer master
    hide rs_image_C514C7B43BB94588B7E6F6DE0405902C

    show rs_image_C514C7B43BB94588B7E6F6DE0405902C as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9616F933879E44CF9FC74D8A58CB9559

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "寄宿着魔鬼的疾病源泉！现在我就来破坏你！毁灭吧！！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}撕——{/size}{nw}"
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_3BAD6C55495B461FA2E97E4F71C22AF7

    extend ""

    stop music fadeout 1
    $ sys_music_current_file = ""

    pause 0.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_A08F830C7B7A48D9AE269614FEAC7E8C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "再说这俩货也没意思，除了荤段子什么也不会。"

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_AFACE878401B4E26BE0872550A11D696 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9EDF48057FB84D428D56198A69E2880E "{size=32}啊啊啊啊啊啊啊啊啊啊啊啊！！！{/size}"

    pause 0.4

    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_DC107C264C484B3A8306E39B61626CF6

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "！？"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_9ADA3ECA775E4BF5904664E9A36296FB as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_D7414D2091574B1EB8E73CCE2D059C48 as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.7

    window show

    if sys_music_current_file != "sound/BGM/Manzai.ogg":
        play music "sound/BGM/Manzai.ogg" loop
        $ sys_music_current_file = "sound/BGM/Manzai.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_D8F7AF82CDFF4CD8A8E72C266EF308A7 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "等等大哥！！你啥意思！？{w}\n你到底、啥意思！？"

    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "诶……啊……！？\n你、你是、杉、杉本……"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "真人！？"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D7414D2091574B1EB8E73CCE2D059C48 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "呜哇——看着就很嫌弃我。这可是打击哦，超大的打击。"

    show rs_image_D8F7AF82CDFF4CD8A8E72C266EF308A7 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "再怎么也不用到那地步吧。而且还说了那么伤人的话～"

    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不、不是……不是这么回事，这里面有很深的理由……"

    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "心情有些不爽来着，但没想到本人就在，没注意到。"

    if sys_effect_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Duang 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D7414D2091574B1EB8E73CCE2D059C48 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "居然又说明星没存在感！？受打击了，我要去博客上抱怨。"

    show rs_image_D8F7AF82CDFF4CD8A8E72C266EF308A7 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "“被某中学生哥哥好好讽刺了一顿”\n"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "……所以让我先拍张照。"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "什么玩意儿！！都说是误会了！你这家伙被害妄想也太深了！"

    $ record_volume("music")
    $ renpy.music.set_volume(0.5, 1, "music")

    if sys_effect_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_D6ADB3B2DBE647DC91A820FFA6D351E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_3E50473C6BE74F0694DCDB246EF2B19A

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这个时代要是在网上被发了照片，肯定会被你的粉丝打死的！"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "是哦，大哥，要是受的话还好点，不过洞可是会被填得满满的哦。\n"
    if sys_effect2_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Ding 1.ogg"

    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_FB2122B2C37749959CAE94CCB5D33314 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "我是说那个{color=#FF00FF}洞{/color}♪"

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    $ reverse_volume("music", 1)

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_A08F830C7B7A48D9AE269614FEAC7E8C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "所以所以，可以的话请做个不怀好意的表情。好的，微笑。"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "噫——！！我、我什么都会做的！总之放过我！！"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "什么——的！都是玩笑哦。大哥真是谈得上来的人呐♪"

    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "简直就是理想的客人～不过偏偏讨厌我们真是可惜呐。"

    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "都说了不是讨厌你们，刚才只是一时没管住嘴。"

    show rs_image_D8F7AF82CDFF4CD8A8E72C266EF308A7 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "吼——没管住嘴～"

    show rs_image_5FBD78374DA74E3DAE8DB6DA14DD5616 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "说、说起来，杉本……先生为何会在这儿？而且只有一个人。"

    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "最近有个工作要去这附近的“御咲学园”这么所中学，今天就是先来看看。"

    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "本来和陆田以及经理人一起来的，不过那些人现在迷路了，我正在找。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_7303A840CCBB4DFCA4E6D8A50257852D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不，你才是那个迷路的。\n"
    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "御咲学园么，就是我上学的地方嘛。"

    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "欸——！是这样吗！这可真是不得了的偶遇呐。"

    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "原来如此，我被那里的学生冷嘲热讽了！\n"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_7DBEBFAAD60F4BB3AE69BBA96A86BAFA as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "完全不想工作了！"

    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呃……那个……算了！作为道歉，要我带你去学校么？"

    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "既然如此请带我看看附近。有什么有意思的地方吗？"

    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "有意思的地方？嗯……好，总之先走起？"

    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "好——的。\n{w=0.5}{nw}"
    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "哦，请问你的名字是？"

    show rs_image_97AEAB5F7F86404C83B970C313450D38 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "猫山。猫山三朗。"

    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "是嘛！那么就是三朗前辈！请多多指教！"

    window hide

    pause 0.4

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 2

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7187539787BF4F9188E6E2F99CB1B900 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.8

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg"

    window show

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_9BD814B82EB04FBCA4D4A9D9FE4C070D as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_7C178421D3DA4E2CB70D4336919888FB "啊哈哈哈，三朗前辈真的很有趣呐♪"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "欸、是么～多谢多谢。"

    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7C178421D3DA4E2CB70D4336919888FB "所以说，那个真正的理由是什么？"

    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "理由？"

    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "撕我们海报的理由。看上去也不像是真的讨厌我们。"

    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那个……只是有点小烦恼罢了……"

    show rs_image_48C471BCCD7E4FA88928531D9D1DD333 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "欸～原来是有苦衷的。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "那，是什么？色色的恋爱的事情？说起这个岁数的烦恼只能是那个了！"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_871E0CFED93745B19E9B12161459C49C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不对！不是那么回事！！\n我们学校是男校，根本就不会有那种事好不。"

    show rs_image_55BA6F9211CF475F8927D40CFEC977B2 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "诶？为什么？男生之间的恋爱也是很普通的哦？"
    # I had deleted all comments but except this: Is this game a game that in purpose to lead people to gay's road?

    show rs_image_7303A840CCBB4DFCA4E6D8A50257852D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "肯定不普通啊……确实是有那种情侣不过……"

    show rs_image_D8F7AF82CDFF4CD8A8E72C266EF308A7 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "嗯～？不觉得有些矛盾吗？一边承认着现实，一边又否认着它。"

    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不是，所以说……我喜欢的是女人，所以那个和我无关。"

    show rs_image_48C471BCCD7E4FA88928531D9D1DD333 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "嗯——"

    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……"

    stop music fadeout 1
    $ sys_music_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "……真心？"

    show rs_image_5FBD78374DA74E3DAE8DB6DA14DD5616 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "当、当然的！"

    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "……呐，三朗哥。接下来我的提问，请只用是和否回答。"

    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "是、是。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "第一问！你现在有在意的人吗？"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_7187539787BF4F9188E6E2F99CB1B900 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D544765C4BA64EC6B46D01C4A92BD5D1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "嗯～？到底是什么～？滴答滴答滴答叮——！"

    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "是、是。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "第二问！关于刚才撕破海报的事，是因为上面有“那种内容”才撕的？"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_7187539787BF4F9188E6E2F99CB1B900 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……是。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "第三问！你不讨厌我。"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_7187539787BF4F9188E6E2F99CB1B900 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_AAC229C565304B76BADD3819ED261CD1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "是。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_7DBEBFAAD60F4BB3AE69BBA96A86BAFA as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "第四问！倒不如说，想抱杉本上床！？"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_7187539787BF4F9188E6E2F99CB1B900 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "否。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Quiz 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Quiz 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Quiz 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "第五问！你喜欢女孩子。"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_7187539787BF4F9188E6E2F99CB1B900 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_3DD22550A42C40F8BB7B0F82E5DBE06E as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "是！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_D544765C4BA64EC6B46D01C4A92BD5D1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "好～的，结束！辛苦了！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……这是什么？"

    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "杉本问卷的结果发表！三朗前辈，你的烦恼就是……"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window hide

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    window show

    pause 0.3

    rs_character_7C178421D3DA4E2CB70D4336919888FB "“明明喜欢女生却很在意一位男生，并因此困扰”！！"

    if sys_effect_current_file != "sound/Effect Sound/Correct 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Correct 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Correct 1.ogg"

    if sys_effect2_current_file != "sound/Effect Sound/Clap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clap 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clap 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_64C987B3866E43999077769BDA7EB8C7 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_7C178421D3DA4E2CB70D4336919888FB "就是这样！觉得好的客人请鼓掌！鼓掌！谢谢大家！"

    window hide

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.7

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    window show

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_7187539787BF4F9188E6E2F99CB1B900 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_FB2122B2C37749959CAE94CCB5D33314 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "！？！？不对不对不对——！！不可能是那样！！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_7DBEBFAAD60F4BB3AE69BBA96A86BAFA as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "看这个反应，果然对了？哇——♪奖金有多少？"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_871E0CFED93745B19E9B12161459C49C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "听我说话！\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_871E0CFED93745B19E9B12161459C49C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "再说出题人要什么奖金！！"

    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "哦哦～精辟的双重吐槽！最近的业余人士还真是能干呐♪"

    show rs_image_A4E2B01D0ECA431CB76DADC3863D74BF as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不……我是男……那家伙是……"

    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "三朗前辈，为什么要这么排斥？"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_A4E2B01D0ECA431CB76DADC3863D74BF as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我、普通就好。我想要维持普通的人生。只是这样罢了。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_7C178421D3DA4E2CB70D4336919888FB "“普通”……自己创造一个没有实体的世界的话，这个世界观就会变得充满束缚。"

    show rs_image_D8F7AF82CDFF4CD8A8E72C266EF308A7 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "理所当然地就会退而选择和大多数人一样的道路，就能安心。\n不过，也并不是说和别人不一样就不普通了。"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_BE8486E53367484D8879711D82BE0D21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……说了些深奥的话呢，明明就是个小孩子。"

    show rs_image_55BA6F9211CF475F8927D40CFEC977B2 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "普不普通不是那么重要的事情！不过，反过来会更容易理解哦。"

    show rs_image_4D1311D27FDA4670AB1582678631B9C9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "？"

    stop music fadeout 2
    $ sys_music_current_file = ""

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A6EB165FEA4F43D98FA0D7F5088E39A4 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.4

    rs_character_7C178421D3DA4E2CB70D4336919888FB "三朗前辈，再来一个小环节。主持人当然是我。"

    window hide

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    window show

    rs_character_7C178421D3DA4E2CB70D4336919888FB "那么大家一起火力全开！！{w}\n喜闻乐见的！！{w=0.5}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Clap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Clap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Clap 1.ogg"

    extend "{size=36}{color=#FF0000}野球拳环节！！{/color}{/size}"

    window hide

    pause 0.7

    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    $ set_window("体育祭、音楽祭")
    window show

    pause 0.3

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#FF0000}接下来角色会不断出现，{/color}{w}\n{color=#FF0000}请一一和他们进行野球拳对决。{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#FF0000}每人三局两胜，{/color}{w}\n{color=#FF0000}请加油获得胜利。{/color}"

    window hide

    $ set_window("イベントモード")
    pause 0.5

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_86B1C26C60CF4E839CF11A136041A03A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_FB2122B2C37749959CAE94CCB5D33314 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if sys_effect2_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Drum 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    pause 0.7

    window show

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "为、为啥会变成这样！！？"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "好了好了，为了不被我的粉丝们埋了，请带着必死的信念加油哦！"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    show rs_image_388ABE71A7C0480E9A406F1C2CA9B003 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "噫——！只有这个饶了我！！我干！！我干还不行么！！！"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_239594E579914FF49F149CE30BEBD5CF

    pause 1


    if judge_lm_condition([]):
        jump block_00003B70

    return

label block_00003B70:
    # Node: 00003B70 (PREPARE)
    $ YKKAllyLifePoint = [0] * 3
    $ YKKEnemyLifePoint = [0] * 3
    $ YKKCGList = [0] * 3
    $ YKKAllyLifePoint[0] = "images/Games/Yakyuken/Lifepoint/Saburo/3.png"
    $ YKKAllyLifePoint[1] = "images/Games/Yakyuken/Lifepoint/Saburo/2.png"
    $ YKKAllyLifePoint[2] = "images/Games/Yakyuken/Lifepoint/Saburo/1.png"
    $ YKKCharacter = 0
    $ YKKLoseScene = 0
    $ YKKMustWin = False

    if judge_lm_condition([]):
        jump block_00003B71

    return

label block_00003B71:
    # Node: 00003B71 (野球拳: 月)
    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F7B4BBF8CE1F42548986125166418110 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.6

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_9A51889A5B884F76838CF8C5D3725812 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_77C99743D39944F9AD8542E6C1310363 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我记得你是二班的……到底怎么了？"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "旁边这位好像有些面熟……"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9ADA3ECA775E4BF5904664E9A36296FB as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "闭嘴！说明什么的都见鬼去！！\n来一场无悔无怨的三局胜负！！上了！！"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_4C999211D44D42EEB0A2295444C7519D

    pause 0.9


    if judge_lm_condition([]):
        jump block_00003B72

    return

label block_00003B72:
    # Node: 00003B72 (野球拳 月)
    $ YKKEnemyLifePoint[0] = "images/Games/Yakyuken/Lifepoint/Tsuki/3.png"
    $ YKKEnemyLifePoint[1] = "images/Games/Yakyuken/Lifepoint/Tsuki/2.png"
    $ YKKEnemyLifePoint[2] = "images/Games/Yakyuken/Lifepoint/Tsuki/1.png"
    $ YKKCGList[0] = "rs_image_7807C68AFE0D45CA9679A08B5635D87F"
    $ YKKCGList[1] = "rs_image_F0B942BCF3F345D994A483AC7B298635"
    $ YKKCGList[2] = "rs_image_F232B64B26E9462499506723A75A2478"
    $ YKKCharacter = 0

    if judge_lm_condition([]):
        jump block_00003B58

    return

label block_00003B58:
    # Node: 00003B58 (野球拳)
    call block_000007CB from _call_block_000007CB

    if judge_lm_condition([{ "scope": 0, "content": "YKKIsWinner == True" }]):
        jump block_00003B73
    if judge_lm_condition([]):
        jump block_00003B74

    return

label block_00003B73:
    # Node: 00003B73 (Win)
    if sys_effect_current_file != "sound/Effect Sound/Trumpet 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Trumpet 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Trumpet 1.ogg"

    # Gallery unlock: images/Games/Yakyuken/CG/Tsuki/Yakyuken Tsuki 1.png
    $ zorder_rs_image_E9A663366FCD424F80AA4C9F0F50B783 = -100
    show rs_image_E9A663366FCD424F80AA4C9F0F50B783 as rs_image_E9A663366FCD424F80AA4C9F0F50B783 zorder zorder_rs_image_E9A663366FCD424F80AA4C9F0F50B783 onlayer master
    hide rs_image_E9A663366FCD424F80AA4C9F0F50B783

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_479B902B71B64D31843B2CBF35A7C19D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E9A663366FCD424F80AA4C9F0F50B783 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥！？哥哥——！！"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "唔……我居然会……！作为赤峰家长男这简直是耻辱……"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B79

    return

label block_00003B79:
    # Node: 00003B79 (野球拳 伊藤)
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_FB8046DBE16F4BA8BE96613E8F3A850C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.6

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_DDAC64C11C734DEB837A32D6A1C90288 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_F22822BF03BF404AA4D836728AC17B45 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "猫山！这到底是在做什么！？"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_FB2122B2C37749959CAE94CCB5D33314 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "闭嘴——！！别念叨了给我脱！！！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "之前就觉得是个笨蛋了，没想到有这么……"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_4C999211D44D42EEB0A2295444C7519D

    pause 0.9


    if judge_lm_condition([]):
        jump block_00003B7C

    return

label block_00003B7C:
    # Node: 00003B7C (野球拳 伊藤)
    $ YKKEnemyLifePoint[0] = "images/Games/Yakyuken/Lifepoint/Itou/3.png"
    $ YKKEnemyLifePoint[1] = "images/Games/Yakyuken/Lifepoint/Itou/2.png"
    $ YKKEnemyLifePoint[2] = "images/Games/Yakyuken/Lifepoint/Itou/1.png"
    $ YKKCGList[0] = "rs_image_77ADCB3F3FFE4790ACF1CFA1B370D10E"
    $ YKKCGList[1] = "rs_image_F07581615155432B859CC7C4EA5BB50A"
    $ YKKCGList[2] = "rs_image_8914D7D41D88433BA466B30E72553022"
    $ YKKCharacter = 1

    if judge_lm_condition([]):
        jump block_00003B7D

    return

label block_00003B7D:
    # Node: 00003B7D (野球拳)
    call block_000007CB from _call_block_000007CB_1

    if judge_lm_condition([{ "scope": 0, "content": "YKKIsWinner == True" }]):
        jump block_00003B7E
    if judge_lm_condition([]):
        jump block_00003B81

    return

label block_00003B7E:
    # Node: 00003B7E (Win)
    if sys_effect_current_file != "sound/Effect Sound/Trumpet 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Trumpet 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Trumpet 1.ogg"

    # Gallery unlock: images/Games/Yakyuken/CG/Itou/Yakyuken Itou 1.png
    $ zorder_rs_image_8FE737664EDE4EC7B0E8209B406F0C83 = -100
    show rs_image_8FE737664EDE4EC7B0E8209B406F0C83 as rs_image_8FE737664EDE4EC7B0E8209B406F0C83 zorder zorder_rs_image_8FE737664EDE4EC7B0E8209B406F0C83 onlayer master
    hide rs_image_8FE737664EDE4EC7B0E8209B406F0C83

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_479B902B71B64D31843B2CBF35A7C19D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8FE737664EDE4EC7B0E8209B406F0C83 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "伊藤嘛，皮肤又白，也没长毛，好工口啊。"

    rs_character_710A38AC94C841779DB701B5AC1010FD "不、不用你管！给我等着笨蛋！！"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B80

    return

label block_00003B80:
    # Node: 00003B80 (野球拳 忍)
    $ set_window("イベントモード")
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7B49313C1C0A4D8E8C250CC79F444E2D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.6

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_6EA040B97356486ABE5FD91F92B543D2 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AB838172A2DB46ABA7F4AC2B3C09693D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "猫君，下午好——！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你好。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_871E0CFED93745B19E9B12161459C49C as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你们就成为我剑上的雨蚀好了～！！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_5001328A201E490CB770173E51647B16 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_2D2761902CAE44EC807DF631A55BE304 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊？"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_4C999211D44D42EEB0A2295444C7519D

    pause 0.9


    if judge_lm_condition([]):
        jump block_00003B82

    return

label block_00003B82:
    # Node: 00003B82 (野球拳 忍)
    $ YKKEnemyLifePoint[0] = "images/Games/Yakyuken/Lifepoint/Shinobu/3.png"
    $ YKKEnemyLifePoint[1] = "images/Games/Yakyuken/Lifepoint/Shinobu/2.png"
    $ YKKEnemyLifePoint[2] = "images/Games/Yakyuken/Lifepoint/Shinobu/1.png"
    $ YKKCGList[0] = "rs_image_45595CAD90274C6792ED17A5D287AC73"
    $ YKKCGList[1] = "rs_image_4FFF4D5081EF48C48C56351B30912D0D"
    $ YKKCGList[2] = "rs_image_66A4E0F049264A14B7EC2B8586906585"
    $ YKKCharacter = 2

    if judge_lm_condition([]):
        jump block_00003B83

    return

label block_00003B83:
    # Node: 00003B83 (野球拳)
    call block_000007CB from _call_block_000007CB_2

    if judge_lm_condition([{ "scope": 0, "content": "YKKIsWinner == True" }]):
        jump block_00003B85
    if judge_lm_condition([]):
        jump block_00003B84

    return

label block_00003B85:
    # Node: 00003B85 (Win)
    if sys_effect_current_file != "sound/Effect Sound/Trumpet 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Trumpet 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Trumpet 1.ogg"

    # Gallery unlock: images/Games/Yakyuken/CG/Shinobu/Yakyuken Shinobu 1.png
    $ zorder_rs_image_9F56029B7C3B4A9A846CEBD0C4ABA9F6 = -100
    show rs_image_9F56029B7C3B4A9A846CEBD0C4ABA9F6 as rs_image_9F56029B7C3B4A9A846CEBD0C4ABA9F6 zorder zorder_rs_image_9F56029B7C3B4A9A846CEBD0C4ABA9F6 onlayer master
    hide rs_image_9F56029B7C3B4A9A846CEBD0C4ABA9F6

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_479B902B71B64D31843B2CBF35A7C19D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9F56029B7C3B4A9A846CEBD0C4ABA9F6 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "警察叔叔——！这里有露出狂——！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……切。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Hit 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 2.ogg"

    extend ""

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔欸！"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B86

    return

label block_00003B86:
    # Node: 00003B86 (野球拳 四朗)
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_BAA43B4F4198492BA4DCD8836A92877B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.6

    window show

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_DAF069330C204448B235C93753D17CB4 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我竟然不得不对自己的弟弟刀兵相向……\n现实真是比任何故事都要残酷啊。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 200
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_9A28E545991346B283D7739D7FF58074 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊——？说什么呢这个人。"

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗的哥哥有时让人觉得很背后一凉呐。"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_4C999211D44D42EEB0A2295444C7519D

    pause 0.9


    if judge_lm_condition([]):
        jump block_00003B88

    return

label block_00003B88:
    # Node: 00003B88 (野球拳 四朗)
    $ YKKEnemyLifePoint[0] = "images/Games/Yakyuken/Lifepoint/Shiro/3.png"
    $ YKKEnemyLifePoint[1] = "images/Games/Yakyuken/Lifepoint/Shiro/2.png"
    $ YKKEnemyLifePoint[2] = "images/Games/Yakyuken/Lifepoint/Shiro/1.png"
    $ YKKCGList[0] = "rs_image_82FBA261F8B743E2B7905761A51E8130"
    $ YKKCGList[1] = "rs_image_C1CF19D2F51147BEA158A4A080C53E8E"
    $ YKKCGList[2] = "rs_image_05A1F8B8E2FC4BF48EEB4DCDD2746CEC"
    $ YKKCharacter = 3
    $ YKKMustWin = True

    if judge_lm_condition([]):
        jump block_00003B89

    return

label block_00003B89:
    # Node: 00003B89 (野球拳)
    call block_000007CB from _call_block_000007CB_3

    if judge_lm_condition([]):
        jump block_00003B8B

    return

label block_00003B8B:
    # Node: 00003B8B (CLEAR)
    $ del YKKAllyLifePoint
    $ del YKKEnemyLifePoint
    $ del YKKCGList
    $ del YKKCharacter
    $ del YKKLoseScene
    $ del YKKMustWin
    $ del YKKIsWinner

    if judge_lm_condition([]):
        jump block_00003B8A

    return

label block_00003B8A:
    # Node: 00003B8A (Win)
    if sys_effect_current_file != "sound/Effect Sound/Trumpet 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Trumpet 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Trumpet 1.ogg"

    # Gallery unlock: images/Games/Yakyuken/CG/Shiro/Yakyuken Shiro 1.png
    $ zorder_rs_image_C66C10E625D1487C81DE82A7A6963CE1 = -100
    show rs_image_C66C10E625D1487C81DE82A7A6963CE1 as rs_image_C66C10E625D1487C81DE82A7A6963CE1 zorder zorder_rs_image_C66C10E625D1487C81DE82A7A6963CE1 onlayer master
    hide rs_image_C66C10E625D1487C81DE82A7A6963CE1

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_479B902B71B64D31843B2CBF35A7C19D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C66C10E625D1487C81DE82A7A6963CE1 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "为什么我必须要遇到这种事！！"

    rs_character_7009C1117C004F51829614A203C67DE7 "哈哈，四朗和三朗前辈都好狂热呐。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "这都是三朗前辈的成长所必须的，请适当忍耐一下。"

    rs_character_7009C1117C004F51829614A203C67DE7 "啊咧？难道是……杉本先生？"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "嗯，陆田和杉本的杉本哦——很荣幸阁下能认识我们哦——！"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_BFEF6FC2749A4B06BF8978A9085171B6 as tag_4233D225ED0D43968B3A0D890F587FEB at right_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_7009C1117C004F51829614A203C67DE7 "嗯～！一直在电视上看你们的节目哦。"

    rs_character_7009C1117C004F51829614A203C67DE7 "竟然能想到那样的捏他真是太感动了。\n可以的话，等下请给我签名。"

    show rs_image_55BA6F9211CF475F8927D40CFEC977B2 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "多么令人高兴的话语！当然！我很荣幸哦——♪"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你们！把我搁在一边儿擅自玩什么亲密！！"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "是啊是啊！到底怎么回事给我说明一下！！"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "哦不好意思……嗯？难道说这个状况……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "灵光一闪！"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_9A28E545991346B283D7739D7FF58074 as tag_4233D225ED0D43968B3A0D890F587FEB at right_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    extend "你是我的粉丝对不对。\n找你商量个事可以吗？"

    rs_character_7009C1117C004F51829614A203C67DE7 "嗯～是什么呐～"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "{size=15}如此如此这般那般……{w}可以拜托你吗？{/size}"

    rs_character_7009C1117C004F51829614A203C67DE7 "{size=15}只是这种事的话，嗯，请务必。{/size}"

    window hide

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_28F784D09B6C4DC7923149F266748707 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_BBB78A424C474639A21FB2A283A1830A as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    if sys_effect_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    show rs_image_2719E3FFCF414ACABFD2F4D60C5BCCB0 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    if sys_effect_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    # Gallery unlock: images/CG/I-am-none-gay-with-no-lovers/I-am-none-gay-with-no-lovers 9-2.png
    $ zorder_rs_image_B5626DFE23C0455A8A9CD7A2A8AA44A0 = -100
    show rs_image_B5626DFE23C0455A8A9CD7A2A8AA44A0 as rs_image_B5626DFE23C0455A8A9CD7A2A8AA44A0 zorder zorder_rs_image_B5626DFE23C0455A8A9CD7A2A8AA44A0 onlayer master
    hide rs_image_B5626DFE23C0455A8A9CD7A2A8AA44A0

    show rs_image_B5626DFE23C0455A8A9CD7A2A8AA44A0 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.85

    window show

    if sys_effect_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "干什么啊你们！！？？"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "没什么，只是给素质优异的人提供难以忘怀的体验哦。"

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗……这下就没有被排除在外了哦，高兴吗～？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不是这个问题！！"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "果然就算给三朗前辈看这个也没有任何感觉呐～原来如此。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "怎么会有看自己弟弟的裸体还能感觉到什么的人啊！！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "嗯，算了总之就是这样了。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "好的！以上就是心跳不已♪只有男人的野球拳大赛。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不觉得节目名变了么。"

    window hide

    pause 0.7

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2.5


    if judge_lm_condition([]):
        jump block_00003AAE

    return

label block_00003AAE:
    # Node: 00003AAE (我是直的，現無對象 3)
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_530777FF5DE0403C85E0F13A632298D3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.5

    if sys_music_current_file != "sound/BGM/Afternoon.ogg":
        play music "sound/BGM/Afternoon.ogg" loop
        $ sys_music_current_file = "sound/BGM/Afternoon.ogg"

    window show

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_7C178421D3DA4E2CB70D4336919888FB "呼～♪真是盛况空前呐。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_AAC229C565304B76BADD3819ED261CD1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你……到底为何做那些事……"

    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "我来解释♪{w}对了，说起来，\n刚才的野球拳大赛后身体没觉得冷吗？"

    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "刚好那里有澡堂！快快！剩下的话就在里面说！"

    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "诶，不，那边那个是……"

    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "拒绝和我一起入浴可是不会被粉丝们原谅的！\n"
    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_3BC0411E559D49E38A86F531E7DC85FF

    extend "快走——！"

    window hide

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E7A7EFABF8B949FEADD23029D844B4E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DBD419D745264B4E813D8F16E2E85B4E

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "………"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "有人吗！男生两人拜托了——！"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_796EA76CCD7948EDA05987B346FF8E44 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "来了，欢迎光临！\n{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_E0FD99FA821A4792A2559534C21033C3 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "——三、三酱！！杉、杉酱！？"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D7A3D9A3B4904F1DB6EB21C74B3A9624 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哇啊啊啊啊！！！超少见的！！\n我是你的铁杆粉丝！！请务必和我握手！！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_796EA76CCD7948EDA05987B346FF8E44 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_55BA6F9211CF475F8927D40CFEC977B2 as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "那个……称呼你为慎太郎前辈可以吗？\n能收看我们的节目，我感到非常荣幸！"

    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "慎太郎前辈和三朗前辈是朋友吗？"

    show rs_image_B7769D775A0F445A8B5689912EB3352E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "朋友什么的，是我的甜心！！\n"
    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_796EA76CCD7948EDA05987B346FF8E44 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "请和我结婚。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_871E0CFED93745B19E9B12161459C49C as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "怎么可能笨蛋！！犯病了我非得要和个男人！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_7303A840CCBB4DFCA4E6D8A50257852D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "还有今天为何要在我旁边睡觉？那对心脏很不好的别干了！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_E808A92AE67540E88F11A5EEEB9325DD as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊……说起来确实发生过呐。最近总是觉得很累，咳咳……"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_B7769D775A0F445A8B5689912EB3352E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "本想就那样趁睡着的时候做点什么的。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_7303A840CCBB4DFCA4E6D8A50257852D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "果、果然如此……连木天蓼都准备了，真是有劳你了。"

    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "总之我去洗澡了！"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_E808A92AE67540E88F11A5EEEB9325DD as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不错嘛——三酱和杉酱都进去了，我也想一起啊……咳咳。"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_7C178421D3DA4E2CB70D4336919888FB "……"

    show rs_image_796EA76CCD7948EDA05987B346FF8E44 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "杉酱，有什么事嘛吗"

    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "没有……真的很容易看出来呐。"

    show rs_image_0D25BDFC92E049B19E3827F7101688C0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "？"

    show rs_image_783A51AACF354348924C712751A648F9 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "说起来，为什么会来我们这边？？"

    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "刚才的“心跳不已♪只有男人的野球拳大赛”上\n看多了那些画面，看着就觉得冷了就……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D7A3D9A3B4904F1DB6EB21C74B3A9624 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欸欸欸欸欸！？不错嘛——！！我也要和三酱玩野球拳～！！"

    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "哦♪慎太郎前辈跃跃欲试！！\n"
    stop music fadeout 0.5
    $ sys_music_current_file = ""

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_86B1C26C60CF4E839CF11A136041A03A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    pause 0.5

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "那么这里无论如何都必须加赛一场～！！"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "出来——！三朗前辈！三——朗——前——辈！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_6440D6C806CA421DA7B4B79725153866 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "干、干嘛！！等、等等！！让我穿上内裤！！！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "紧急情况！！花乃汤的奥村慎太郎参战！！\n野球拳最终决战！！开始！！！"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_6C2965CB0398406E88B7AF94413DDC5C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "停——！！这不公平主持人！！！\n我就一条内裤直接就不战而败了！！！"

    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "那就干脆战败者全脱光就好了嘛！！\n这下该没有怨言了！！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_783A51AACF354348924C712751A648F9 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "要是赢了，直接顺势做下去也没关系吗？？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 300
    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "当然！！"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_8C9AD1F8BFF54CCFBA256DB7EB668DA0 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不可能！！！"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_F54388151A304B869E4DA0116AFC95E7 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_6C2965CB0398406E88B7AF94413DDC5C as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "吼吼吼，三酱，主持人都允许了，做好觉悟哦。"

    show rs_image_8C9AD1F8BFF54CCFBA256DB7EB668DA0 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你这家伙不是还在感冒么！！恶化了怎么行！？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_AD75CBCFA4E24CC7ABD340D46A100708 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "感冒什么的早就被兴奋给冲没了！！\n"
    show rs_image_F54388151A304B869E4DA0116AFC95E7 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "别说了上！！我来了～～！！"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_4C999211D44D42EEB0A2295444C7519D

    pause 0.9

    # Gallery unlock: images/Games/Yakyuken/CG/Shintaro/Yakyuken Shintaro 2.png
    $ zorder_rs_image_C8CDD0393EE8457FAB6E6746ACFC16B4 = -100
    show rs_image_C8CDD0393EE8457FAB6E6746ACFC16B4 as rs_image_C8CDD0393EE8457FAB6E6746ACFC16B4 zorder zorder_rs_image_C8CDD0393EE8457FAB6E6746ACFC16B4 onlayer master
    hide rs_image_C8CDD0393EE8457FAB6E6746ACFC16B4

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_9EEEA1BE275245F69D2CBDC443AA4142 = 300
    $ zorder_tag_19556E53939043CAAFFEEEA7F99D768A = 300
    show rs_image_C8CDD0393EE8457FAB6E6746ACFC16B4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_9F919CF942CA44BEB3F56CBCC81C9CB8 as tag_9EEEA1BE275245F69D2CBDC443AA4142 at center_bottom zorder zorder_tag_9EEEA1BE275245F69D2CBDC443AA4142 onlayer master
    show rs_image_0D75F8B6CF794F1585C092A44110EF33 as tag_19556E53939043CAAFFEEEA7F99D768A at center_top zorder zorder_tag_19556E53939043CAAFFEEEA7F99D768A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_445345A84BCD459E8C2AC2BA7651355B = 200
    show rs_image_3FDAF1D21ADF42CB88D0E1036D606D54 as tag_445345A84BCD459E8C2AC2BA7651355B at center_bottom zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_FD68A346D7D44E428AFB4158847AC3EE

    pause 1.2

    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_86F3BBBA9EB74881AC89CD8328868CD6 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_582B28E0E2DD42FA964BF576F8F12DBD as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    pause 0.5

    if sys_effect3_current_file != "sound/Effect Sound/Yoo 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Yoo 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Yoo 1.ogg"

    show rs_image_B3EE009F700A45B3977802B904CFE952 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_3A4BA4C12CE946B5B47CA31B0DB6CAC2

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_9453C611A6E44C138BAD374653AB1038 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Break 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    $ zorder_tag_93E1ED3B9EFB461486972450D09B1393 = 300
    show rs_image_29F1CF10388847AC865DE47D926EB220 as tag_93E1ED3B9EFB461486972450D09B1393 at Transform(xpos=128, ypos=220) zorder zorder_tag_93E1ED3B9EFB461486972450D09B1393 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    $ zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 = 300
    show rs_image_26D8970A553148548DEBB169BD8083D9 as tag_98EEC70DEB344EA5BDB430BB03A0BBE7 at Transform(xpos=464, ypos=220) zorder zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Hit 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 2.ogg"

    $ zorder_tag_62B301F7D3B54E57A3E8F7E6E0E8B145 = 400
    show rs_image_99E5D61DF982413DA7EBF936D43DC9FA as tag_62B301F7D3B54E57A3E8F7E6E0E8B145 at center_top zorder zorder_tag_62B301F7D3B54E57A3E8F7E6E0E8B145 onlayer master
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    hide tag_62B301F7D3B54E57A3E8F7E6E0E8B145
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_9EEEA1BE275245F69D2CBDC443AA4142
    hide tag_19556E53939043CAAFFEEEA7F99D768A
    hide tag_93E1ED3B9EFB461486972450D09B1393
    hide tag_445345A84BCD459E8C2AC2BA7651355B
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_98EEC70DEB344EA5BDB430BB03A0BBE7
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Trumpet 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Trumpet 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Trumpet 1.ogg"

    # Gallery unlock: images/Games/Yakyuken/CG/Shintaro/Yakyuken Shintaro 2.png
    $ zorder_rs_image_C8CDD0393EE8457FAB6E6746ACFC16B4 = -100
    show rs_image_C8CDD0393EE8457FAB6E6746ACFC16B4 as rs_image_C8CDD0393EE8457FAB6E6746ACFC16B4 zorder zorder_rs_image_C8CDD0393EE8457FAB6E6746ACFC16B4 onlayer master
    hide rs_image_C8CDD0393EE8457FAB6E6746ACFC16B4

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_479B902B71B64D31843B2CBF35A7C19D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C8CDD0393EE8457FAB6E6746ACFC16B4 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "太好了！我赢了！！啊……不过……你……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "切，输了啊～可以，我……"

    window hide

    if sys_effect3_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Waoh 1.ogg"

    # Gallery unlock: images/Games/Yakyuken/CG/Shintaro/Yakyuken Shintaro 1.png
    $ zorder_rs_image_C93E3A8AE8DA46FA8F4E3883F10E4A0A = -100
    show rs_image_C93E3A8AE8DA46FA8F4E3883F10E4A0A as rs_image_C93E3A8AE8DA46FA8F4E3883F10E4A0A zorder zorder_rs_image_C93E3A8AE8DA46FA8F4E3883F10E4A0A onlayer master
    hide rs_image_C93E3A8AE8DA46FA8F4E3883F10E4A0A

    show rs_image_C93E3A8AE8DA46FA8F4E3883F10E4A0A as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.5

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好了，三酱。请仔细看好。"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "给、给我停下！！很不舒服对不？\n行了，抓紧穿上衣服，别着凉了。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欸～一小会没关系的。该做就做才是男子汉不是吗？"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我我我、我明白了！好了看过了！行了！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "根本没在看。主持人！客人的兴致不怎么好！"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "原来如此原来如此♪{w}……算了，那就在这里结束好了！"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "慎太郎前辈辛苦了。抱歉打扰你工作了。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "那么我们就去洗澡了。慎太郎前辈也不要勉强了，保重哦。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "等、等会儿见。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "切——请慢用——"

    window hide

    pause 0.7

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1.5

    $ set_window("イベントモード")
    if sys_effect2_current_file != "sound/Effect Sound/Bathroom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bathroom 2.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Bathroom 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_3D45A7FC99584EC48CA484154ACF4CA8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 1.2

    # Gallery unlock: images/CG/I-am-none-gay-with-no-lovers/I-am-none-gay-with-no-lovers 4.png
    $ zorder_rs_image_B23B20310413456B97F5A62F21EB8231 = -100
    show rs_image_B23B20310413456B97F5A62F21EB8231 as rs_image_B23B20310413456B97F5A62F21EB8231 zorder zorder_rs_image_B23B20310413456B97F5A62F21EB8231 onlayer master
    hide rs_image_B23B20310413456B97F5A62F21EB8231

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 200
    show rs_image_B23B20310413456B97F5A62F21EB8231 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 0.5

    window show

    rs_character_7C178421D3DA4E2CB70D4336919888FB "呼啊啊～～～。\n好・棒・棒・的・水・温・啊啊啊～"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "三朗前辈？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嗯？啊，没事，真心很不错呐～！"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "什么啊这里，明明在同志圈里听说了的，\n结果就这么普通。清扫得太干净了。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呃！？你知道？？"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "嗯，这里暗地里还是很有名的哦～星期三？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好像是……"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "三朗前辈一直强调自己是直的，对这些却很了解呐。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……偶然之下不小心知道的……"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "嗯——？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "…………"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "有件事先说清楚。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嗯？"

    pause 0.4

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "三朗前辈，你已经很“普通”了，所以不用太担心。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "欸？"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "和你所说的“普通”不同的是，比如，这么看着我的话……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    # Gallery unlock: images/CG/I-am-none-gay-with-no-lovers/I-am-none-gay-with-no-lovers 4-1.png
    $ zorder_rs_image_1DB63445D5FA4A8F90EE59842CB17587 = -100
    show rs_image_1DB63445D5FA4A8F90EE59842CB17587 as rs_image_1DB63445D5FA4A8F90EE59842CB17587 zorder zorder_rs_image_1DB63445D5FA4A8F90EE59842CB17587 onlayer master
    hide rs_image_1DB63445D5FA4A8F90EE59842CB17587

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1DB63445D5FA4A8F90EE59842CB17587 as tag_0BDB8A4A05BB44ED81AE140BE96066BD at center_bottom zorder zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "噫！！？"

    if sys_effect_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "肯定会想那个那个了♪我是说那方面。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "不过，三朗前辈不同。这个通过刚才的游戏已经了解了。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "欸、欸……"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "那么进入下一个环节，\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    # Gallery unlock: images/CG/I-am-none-gay-with-no-lovers/I-am-none-gay-with-no-lovers 4-1.png
    $ zorder_rs_image_1DB63445D5FA4A8F90EE59842CB17587 = -100
    show rs_image_1DB63445D5FA4A8F90EE59842CB17587 as rs_image_1DB63445D5FA4A8F90EE59842CB17587 zorder zorder_rs_image_1DB63445D5FA4A8F90EE59842CB17587 onlayer master
    hide rs_image_1DB63445D5FA4A8F90EE59842CB17587

    show rs_image_1DB63445D5FA4A8F90EE59842CB17587 as tag_0BDB8A4A05BB44ED81AE140BE96066BD zorder zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    extend "你，喜欢慎太郎前辈对不对？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呃！？！？所以说不是……"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "可以了，这些不着边际的话已经听腻了。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "你能感觉到我的话里存在矛盾。不过，构成你烦恼的核心正是这个。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "你想要爱上女生的“普通”意识，和你对慎太郎前辈的感情有了冲突。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "所以，面对其他人，不论是男是女，你都不会有任何想法。"

    window hide

    pause 0.3

    show rs_image_C64C83CF9569441D995A82BA3F3F49A4 as tag_0BDB8A4A05BB44ED81AE140BE96066BD zorder zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.4

    window show

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……不明白啊，就算你这么说……"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "不明白也没关系！不坦白承认的话问题是解决不了的。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "因为性别问题而无法接受对慎太郎前辈的想法，\n就算去找别的女孩子或是其他什么人也没用的。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "请放心，不论同性恋还是异性恋，大家都只是会爱上其他人的普通人类。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "只不过，不同人很“普通”地拥有着不同的世界观，\n所以喜欢上的人有可能是同性，也有可能是异性。"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "同性恋什么的，也不过是事后才有的分类。\n"
    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    # Gallery unlock: images/CG/I-am-none-gay-with-no-lovers/I-am-none-gay-with-no-lovers 4-1.png
    $ zorder_rs_image_1DB63445D5FA4A8F90EE59842CB17587 = -100
    show rs_image_1DB63445D5FA4A8F90EE59842CB17587 as rs_image_1DB63445D5FA4A8F90EE59842CB17587 zorder zorder_rs_image_1DB63445D5FA4A8F90EE59842CB17587 onlayer master
    hide rs_image_1DB63445D5FA4A8F90EE59842CB17587

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1DB63445D5FA4A8F90EE59842CB17587 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不需要那么限制你的心灵也没关系的！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……你真的比我小么？"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "就像在游戏的世界，请用经验来估计年龄。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_7C178421D3DA4E2CB70D4336919888FB "不用决定好的“普通”让自己满意后成长的话，\n以后，可就尝不到回忆年少之时的甜头了哦。"

    window hide

    pause 0.5

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_0BDB8A4A05BB44ED81AE140BE96066BD
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    stop effect2 fadeout 2.5
    $ sys_effect2_current_file = ""

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E7A7EFABF8B949FEADD23029D844B4E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.5

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.3

    rs_character_7C178421D3DA4E2CB70D4336919888FB "呼～好不错的地方！！慎太郎前辈！水温最棒了♪"

    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "拜此所赐也放松下来了，要好好为这次的活动努力练习了～"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_783A51AACF354348924C712751A648F9 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 at right_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那很好嘛～这次的工作难道是和三酱玩漫才？"

    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "不不，是我和陆田在做的活动的一环，这次要在阁下的学校演讲。"

    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "而抽奖中了的三朗前辈会有特别观赏排练的机会哦。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D7A3D9A3B4904F1DB6EB21C74B3A9624 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "是吗！！好羡慕～！一定会好好享受这次演讲的～！"

    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "请务必！到时候也能像今天一样好好把学到的东西说出来就好了呐。"
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_796EA76CCD7948EDA05987B346FF8E44 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "对不对，三朗前辈？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……"

    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_0D25BDFC92E049B19E3827F7101688C0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦呀～？三酱脸很红哦？难道泡过头了？？"

    show rs_image_783A51AACF354348924C712751A648F9 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "真是的，要注意哦～？晕过去就不好了呐～"

    show rs_image_B7769D775A0F445A8B5689912EB3352E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "下次三酱再来的时候就由我好好照顾了哦！"

    show rs_image_BE8486E53367484D8879711D82BE0D21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_BE8486E53367484D8879711D82BE0D21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_0D25BDFC92E049B19E3827F7101688C0 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯……？我的脸上有什么东西吗？"

    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……{w=0.45}只是觉得你很可爱啊什么的。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_E0FD99FA821A4792A2559534C21033C3 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呃！？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_9ADA3ECA775E4BF5904664E9A36296FB as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊——很棒的澡堂！谢了！走了！"

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    window hide

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_530777FF5DE0403C85E0F13A632298D3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.6

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 at right_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "咻——咻——♪"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "请不要起哄……"

    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "有何不可～有何不可～♪总算是迈出一步了呐～♪"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_2B49DF326D8641F283BDF0EC54525573 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "今后就全看我的选择……了么……"

    window hide

    pause 0.4

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BAA43B4F4198492BA4DCD8836A92877B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D7FF18D0A8E140CE95D5B9C6EE2CC48D as tag_0C07D2341065492CB0EDF00452D574E1 at center_top zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_AC46DBAAAEE24C10AECA19E0EDA27051

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "唔哦哦哦哦！！！！杉本！！！！"

    window hide

    hide tag_0C07D2341065492CB0EDF00452D574E1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_530777FF5DE0403C85E0F13A632298D3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_DC107C264C484B3A8306E39B61626CF6

    window show

    rs_character_7C178421D3DA4E2CB70D4336919888FB "好呀！那个可爱的声音是，陆田君～！！\n下午好——这边哦～！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 200
    show rs_image_F68539D279214C24AB4E888AA6B342A0 as tag_0C07D2341065492CB0EDF00452D574E1 at right_top zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "你至今为止都去什么地方鬼混了！！\n经理和员工都快吓死了！！！"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_7DBEBFAAD60F4BB3AE69BBA96A86BAFA as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "抱歉抱歉，下次会注意的——"

    show rs_image_EAA2EF7FB3CF4DC8B7F90D9F76D373E7 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "真是的，算了。\n"
    show rs_image_D2E31CDD8AE14CA4A56BC2EFC98D23CB as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "说起来，那个……这位是……？"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_0C07D2341065492CB0EDF00452D574E1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 200
    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 at center_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_D2E31CDD8AE14CA4A56BC2EFC98D23CB as tag_0C07D2341065492CB0EDF00452D574E1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "我的志愿徒弟！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "并不是。"

    show rs_image_EAA2EF7FB3CF4DC8B7F90D9F76D373E7 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "抱歉，我家笨蛋添麻烦了。"

    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊，没有没有，倒不如说添麻烦的是我这一边。"

    show rs_image_9BD814B82EB04FBCA4D4A9D9FE4C070D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "真的，很厉害啊，你们。\n"
    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_6B387DE0988444BA9024CD57D9D7D7D2 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    show rs_image_909AB6EEDA4E46FEBDCAC93ADC5C7F8C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……以后会给你们加油的，我也会加油的。"

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "……？"

    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_7C178421D3DA4E2CB70D4336919888FB "……♪"

    hide tag_0C07D2341065492CB0EDF00452D574E1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 200
    show rs_image_D422C7DC5B73410C8BD514BC40726CCB as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_1561FC74CECA43F896E80A6050FD4EB8 as tag_0C07D2341065492CB0EDF00452D574E1 at right_top zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_6E0C80C17CC249E2A7A71BB4349C957B "非常感谢——！"

    window hide

    pause 0.5

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_0C07D2341065492CB0EDF00452D574E1
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_DCEBC7527B8F4B4EA0FF44E692174034

    pause 3.5

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A46E468ABE0345679EB63CE570AD59F9

    if sys_music_current_file != "sound/BGM/Chapter 2.ogg":
        play music "sound/BGM/Chapter 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 2.ogg"

    pause 1

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_16307A41F14F432794505E1BCE894C4D as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "慎酱今天休息呢。\n最近一直觉得状态不好，果然还是感冒了呐——"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_450A0D9747F349C29DFC736685CCE2E1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "都已经在咳嗽了。就算是那家伙也抗不过病毒呐。"

    show rs_image_3F5554F53A7B45479BEADD4F5C64C5A8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……希望不是重病。没关系……应该……"

    show rs_image_50933515F8C74F238CEB85C20581CB9F as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "干嘛那么认真？不就是个感冒么？"

    show rs_image_BE01B5CFD6254405BD2B3509A79F98FB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸，嗯，是呐，就是那样。\n可慎酱，工作也很辛苦……"

    show rs_image_3C97D8F2A5614AFD8E3AA590022130E5 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "小孩子怎么可能做容易生病的工作。\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3E862BE64DCF450391CA5AF6BB298B88 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……不过，也确实做了很多那种事。"

    show rs_image_D4205184C879446BA42F7CD4B4690552 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶，猫君原来是知道的！！{w}\n{w=0.3}{nw}"
    show rs_image_2842D32718114B4B95C9326B8B4A1C25 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "那我就直说了，其实有点不安……"

    show rs_image_CD7C30ACF1B54A819AB1F3E4DDB8B23A as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……什么玩意。"

    pause 0.5

    stop music fadeout 0.6
    $ sys_music_current_file = ""

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "艾滋。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "艾滋？"

    if sys_music_current_file != "sound/Effect Sound/Phychological 1.ogg":
        play music "sound/Effect Sound/Phychological 1.ogg" loop
        $ sys_music_current_file = "sound/Effect Sound/Phychological 1.ogg"

    pause 0.4

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我也是最近才知道的，会因为H感染的病毒。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "特别是从后面那种更容易。所以，相比之下男性要更危险。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "只要发病就几乎无法治愈，{w}\n最坏的情况下{w=0.4}可、可能……{w=0.5}{nw}"
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    extend "{color=#800000}会死……{/color}"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{color=#800000}那是……{/color}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{color=#800000}啊，不过不过！！\n现在好好喝药的话不会发展到那一步的！！！{/color}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{color=#800000}所以就算万一真的发生了什么也一定没关系的！！{/color}"

    window hide

    pause 0.4

    show rs_image_D6ADB3B2DBE647DC91A820FFA6D351E3 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_70CBDC11EF294C119157F3EF7DBA9096

    pause 2.5

    stop music fadeout 1
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A5BCDD6D75B04D3A81952DEB9E8F3D00

    pause 2.8

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    if sys_music_current_file != "sound/BGM/My precious time.ogg":
        play music "sound/BGM/My precious time.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time.ogg"

    # Gallery unlock: images/CG/I-am-none-gay-with-no-lovers/I-am-none-gay-with-no-lovers 5.png
    $ zorder_rs_image_63D04BFE31F74541BAC4E3BE874F04D4 = -100
    show rs_image_63D04BFE31F74541BAC4E3BE874F04D4 as rs_image_63D04BFE31F74541BAC4E3BE874F04D4 zorder zorder_rs_image_63D04BFE31F74541BAC4E3BE874F04D4 onlayer master
    hide rs_image_63D04BFE31F74541BAC4E3BE874F04D4

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 200
    show rs_image_63D04BFE31F74541BAC4E3BE874F04D4 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 1

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你这家伙！！！既然知道这个怎么不去阻止他！！？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "朋友就算死了也无所谓是不是！！！？？\n说得还挺开心的混蛋！！啊！！！"

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔！？对不起……！！对不起……！！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友！？\n住手！！想对友干什么！！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "猫山！？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君！？猫山君！！！"

    window hide

    pause 0.5

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_501E507A51854A0FB97DFB72172A8F2F

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_182A55C1C2764F289D996ED811AAFCA8 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BB061DFD88F54F52968CDD7DACA5EE3A as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    pause 0.5

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊……抱、抱歉……我有些激动了，真的很抱歉，没、没事不？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_2537850284E64CC8BAFBB790452506A5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你这……竟敢对友……！"

    show rs_image_8817D1FBC02B43DC85496AD5A961FA7F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍快住手！！\n"
    show rs_image_D8C0F0C20CBC42BCB833A97CCE0D009C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_2842D32718114B4B95C9326B8B4A1C25 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "猫君也……对不起。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_611C45CBE2A74199BAD0B2792507D06C as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君，真的没关系吗！？"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_182A55C1C2764F289D996ED811AAFCA8 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "谢、谢谢，翼君……"

    window hide

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    show rs_image_856822D0F30B4AF0AE8688F27D9CE9B2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_3BC0411E559D49E38A86F531E7DC85FF

    pause 0.8

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_77A0ADE141D04F83AE5399D0943CDF27 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_BB061DFD88F54F52968CDD7DACA5EE3A as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "刚才是怎么了，发生什么了？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "没事……怎么说，一下子没能控制住……"

    show rs_image_7DB0427AB8E441CDBDB81F258D509BA0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "等下最好去道个歉。不然的话会被那个矮个子宰了的。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嗯……"

    window hide

    pause 0.4

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 3.5

    if sys_effect_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 1.5

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    if sys_music_current_file != "sound/BGM/Daily 1.ogg":
        play music "sound/BGM/Daily 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 1.ogg"

    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 1

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "慎酱！{w=0.8}……{w}感冒好了呐——！太好了——！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯——好久没感冒了真的好难受呢——\n睡也不好不睡也不好，简直就是地狱啊～"

    window hide

    pause 0.3

    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_88D1205AA473480CA2A73E26453C1F61 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_6EA78EC2093A46F097116A0C2CBB397C as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "既然都得病了就不要再乱来了。\n我以后会提醒你的，毕竟我们经常去那里。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_8AB2C4C1CCAE4D5EB9E1B90A74D4DBD5 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀～真的吗♪真是的，阿月的男人味每次都被迷得神魂颠倒呐～"

    show rs_image_A62DFA8FA08E4BD2B83B9B282B530095 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "果然只要慎酱在气氛都变得明快了呢。真的，能这么快治好太好了～"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_F94E205F8A284E458577A43CDCB23962 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_ECD1914DBFDB442F9D1A9232EEEC99F6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，不可或缺的。\n"
    show rs_image_58CAC53C853A4ECC97CAB3038D1CAAF0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……哦，那是。"

    window hide

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_5FBD78374DA74E3DAE8DB6DA14DD5616 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "失礼了……\n"
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "森海，昨天那个真的很抱歉。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_35B9BEFBF42E474DB41387E9345C36B4 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "无所谓了～其实真的不用一次次这么在意的，对不对，忍。"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_7D2835EC10DE4438B9BBE9F8CE5454F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，像什么下跪五分钟之类的，\n就算在电视剧戏剧里也很少见的，不要再做了。"

    show rs_image_AAC229C565304B76BADD3819ED261CD1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不，还是需要做到那一步的。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_77C99743D39944F9AD8542E6C1310363 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_12E394DC341C4685AB17E83FEED856C9 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_9A51889A5B884F76838CF8C5D3725812 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欸。什么啊这么严肃的谈话～？我不在的时候发生什么了？？"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我是第一次听说。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我也是。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_34FCB0450F2F463BBF3511F7F6A14AFB as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_EB543C918F764BD48AF5945B5D7C3278 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "真的没事，都已经过去了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_4D1311D27FDA4670AB1582678631B9C9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……奥村，你，感冒好了？"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_8AB2C4C1CCAE4D5EB9E1B90A74D4DBD5 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "三酱……！在关心我吗！？特地来看我的样子的吗！？？"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_8C8329CA4FC34C279A723168C0AA6CC0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我很感激哦！！！爱你！！！呀——好棒！抱抱！！"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "别、别胡说笨蛋！\n"
    show rs_image_909AB6EEDA4E46FEBDCAC93ADC5C7F8C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不过看这个样子确实没关系了。"

    show rs_image_3B13044431874BE09020F9368D6A8C29 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "完全没问题了～☆性欲也恢复如常了哦～♪"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_CA176C5A71144199A2E3AE0C60846C57 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "感冒的时候完全提不起兴致呐～"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_06FD3372A1FE4B4FB675F0FFE43B7CB3 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "对对，空空如也的垃圾桶！"

    show rs_image_253B2776672D49EA928D506D0DCEB77F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯我有经验！"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_1F55CB120A6948E28641DFC1C52982EE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "垃圾桶……哦，说起来{color=#008080}确实有{/color}。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_A31753D19AB548D69BF2EDF6A9B96349 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_9BD814B82EB04FBCA4D4A9D9FE4C070D as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那——那个啊，我有些话想对奥村说，借他一下行不？"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_77C99743D39944F9AD8542E6C1310363 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-85, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_9A51889A5B884F76838CF8C5D3725812 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=410, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C33AC9430994705AE070406BF54210A "请便。"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8AB2C4C1CCAE4D5EB9E1B90A74D4DBD5 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欸！？什么什么！？三酱居然会单独找我！！"

    if sys_effect3_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_8C8329CA4FC34C279A723168C0AA6CC0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "而且在大庭广众之下说要借走！！呀——好棒！抱抱！！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "闭嘴！行了！快走！！"

    window hide

    pause 0.6

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 2.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.2

    show rs_image_5D3FCC78D14F42C78DDA6B5C08A83D04 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.8

    show rs_image_905E9C679FD7435E8DF16A4ECBCB85EA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.2

    show rs_image_B9CA56F5AE0646B5806D66BEA8955E7D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    pause 0.7

    if sys_music_current_file != "sound/BGM/Lively twilight.ogg":
        play music "sound/BGM/Lively twilight.ogg" loop
        $ sys_music_current_file = "sound/BGM/Lively twilight.ogg"

    pause 0.3

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "时间不多，我就单刀直入了？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯、嗯，什么？"

    window hide

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    # Gallery unlock: images/CG/I-am-none-gay-with-no-lovers/I-am-none-gay-with-no-lovers 6-1.png
    $ zorder_rs_image_01A535C9B5DB4CB99B85DD6BAC669F41 = -100
    show rs_image_01A535C9B5DB4CB99B85DD6BAC669F41 as rs_image_01A535C9B5DB4CB99B85DD6BAC669F41 zorder zorder_rs_image_01A535C9B5DB4CB99B85DD6BAC669F41 onlayer master
    hide rs_image_01A535C9B5DB4CB99B85DD6BAC669F41

    show rs_image_01A535C9B5DB4CB99B85DD6BAC669F41 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    pause 0.5

    window show

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "奥村，我喜欢你。{w}\n和我……{w=0.55}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "交往。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欸——！诶、诶！？\n"
    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    extend "诶诶诶诶诶诶诶诶诶！！！！！？？？？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不是玩笑也不是耍帅，我是真心的。{w}\n非常烦恼，非常迷茫，不断思考得出的。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "迄今为止，那么害怕认清自己的心情，\n不过，现在终于可以了，所以就传达出来了。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不敢相信……至今为止完全……虽说素质确实没问题。"

    # Gallery unlock: images/CG/I-am-none-gay-with-no-lovers/I-am-none-gay-with-no-lovers 6-2.png
    $ zorder_rs_image_4BE6749A7DEF47B28C893ED7AEE021E1 = -100
    show rs_image_4BE6749A7DEF47B28C893ED7AEE021E1 as rs_image_4BE6749A7DEF47B28C893ED7AEE021E1 zorder zorder_rs_image_4BE6749A7DEF47B28C893ED7AEE021E1 onlayer master
    hide rs_image_4BE6749A7DEF47B28C893ED7AEE021E1

    show rs_image_4BE6749A7DEF47B28C893ED7AEE021E1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "并不是，突然喜欢上了男人什么的。{w}……我也是有很多苦衷的。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "任何时候给我答复都行，取决于你。我会一直等下去的。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦、哦……我明白了。唔……唔……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_752F624A21E3452FB6700D56F37A557F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊～～～结束！一共就这些！{w}我先回去了。"

    if sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "果然一起回去还是耻度爆表，再见！"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.7

    window show

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_C5F31BAC461D43B9A8E59CAB2E60793D as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……三酱……"

    window hide

    pause 0.6

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.3

    if sys_effect_current_file != "sound/Effect Sound/Class bell 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2604FEB26CCC4082BC90CCE4B5300A9E

    pause 1.5

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_46B09605979B44EBA877032E0832F21E as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_A5B05E7D36FC49258CAE9B6EEA5B58E4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 0.5

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "三酱，那个，关于刚才的回答……"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "诶……哦。"

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Worried 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Worried 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Worried 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.3

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那个～"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊，等、等等。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "吸————呼————"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……好，放马过来！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "如果我可以的话……{w}再说了，我也是喜欢三酱的。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那、那就是说……"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_7F497F24D349433FB39C83C619E61AB8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哈哈。"
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    extend "在下不才，还请多多关照了。"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.4

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……！！请、请多多关照！！我们要一起走下去！！"

    window hide

    # Gallery unlock: images/CG/I-am-none-gay-with-no-lovers/I-am-none-gay-with-no-lovers 7.png
    $ zorder_rs_image_63048BA95B7241CCA1206E32EEB5617C = -100
    show rs_image_63048BA95B7241CCA1206E32EEB5617C as rs_image_63048BA95B7241CCA1206E32EEB5617C zorder zorder_rs_image_63048BA95B7241CCA1206E32EEB5617C onlayer master
    hide rs_image_63048BA95B7241CCA1206E32EEB5617C

    show rs_image_63048BA95B7241CCA1206E32EEB5617C as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_222BBB56F7BA4025B3E942F40786CBC9

    pause 0.8

    window show

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "三酱，很、很痛的！会、会被大家看到的！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈哈，这就是至今为止被戏弄的报复！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀～怎么说呐，多谢招待。这种感觉，完全不同……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "总之就是好羞耻。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈哈。活该——♪"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "以、以后肯定会习惯的！这种感觉也只有现在……"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呵——是么。\n那就只有现在给笨拙的奥村提供点福利。"
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊，对了，不知道咬咬耳朵会怎么样。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀！！真是的——！快住手～～！！"

    window hide

    pause 1

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_04460297D37A447D8CE6298460DB7159

    pause 2.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C2BC5AE332C140ADBD70171FF2BD7F19 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 1.5

    if sys_effect2_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_5EC43923809E45738DC8EC45FC86E73F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_CFCEEA46658B45C38D3ED429DE9FF37D as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "奥村，结果如何？"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_0E66EED4593D45DE99868C4E6769E92E as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "三酱……"
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_C5F31BAC461D43B9A8E59CAB2E60793D as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    if sys_music_current_file != "sound/BGM/The hope.ogg":
        play music "sound/BGM/The hope.ogg" loop
        $ sys_music_current_file = "sound/BGM/The hope.ogg"

    extend "全部阴性！\n这下就可以不用担心地亲亲热热热了～♪"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……能真心为我的身体考虑，真的太感谢了，三酱。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_13B7182BD8624D30A2A9822B541AB274 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "作为……恋人……那是当然的。"

    show rs_image_C5F31BAC461D43B9A8E59CAB2E60793D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "三酱的这种地方，我觉得很棒哦♪"

    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔……都、都是一家人说什么呢！倒是给我好好考虑以后怎么做。"

    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "再说了，为何非得去圈子里？\n被那么对待，你父母就没什么想法么？"

    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……生气了？"

    show rs_image_BE8486E53367484D8879711D82BE0D21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嗯。"

    show rs_image_06FD3372A1FE4B4FB675F0FFE43B7CB3 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "最初的原因正是我自己。小时候在店里帮忙的只有每周日。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "一开始，只有那些过激的人才会出手，后来慢慢就多了。"

    show rs_image_46B09605979B44EBA877032E0832F21E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我也觉得不坏，感觉不错，不过重要的是尝到甜头的回头客越来越多了。"

    show rs_image_E435B1F7BF9B4AB280BA8F0C6B392FB1 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "让我也有了一种微妙的优越感，就像自己在支持着自家的澡堂一样……"

    show rs_image_D544765C4BA64EC6B46D01C4A92BD5D1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "也就是说，父母并不知道？"

    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不管是我的事，还是圈子里的事，他们都不知道。\n"
    show rs_image_06FD3372A1FE4B4FB675F0FFE43B7CB3 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "怎么会有卖自己孩子的无情父母呢。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "就像客人们说的，大人之间的秘密。我也主动担任了周日的浴室清扫。"

    show rs_image_AAC229C565304B76BADD3819ED261CD1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那个就不能不干了么？至少你不许去了……"

    show rs_image_D88BEA8DA4D145D5B87F3A179B88BE87 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "唔～嗯。说实话，\n现在我家的营业呃很大程度上靠的是圈子里的知名度。"

    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "在网上看到后以我为目标来的人不在少数，比较困难呐～"

    show rs_image_4D1311D27FDA4670AB1582678631B9C9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……我不是在怪你，但那某种意义上，这也是一种不尊重。"

    show rs_image_BE8486E53367484D8879711D82BE0D21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你的双亲可是为了澡堂在认真努力的，\n就算在这种意义上你也不能继续了。"

    show rs_image_A6E2B83133264FE2AC7ED2F9767DAB76 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……嗯，抱歉。看来必须想出一个新方法来了。"

    show rs_image_13EEE138043542FB90557CFB44BADDE4 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦！当然，我也会一起的。会慢慢变好的，安心就好。"

    show rs_image_909AB6EEDA4E46FEBDCAC93ADC5C7F8C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那么，剩下的话就到你家再说。\n那个地方气氛也比较放松，也像是会有进展的样子！"

    show rs_image_A15B5B9C211846009204F1689FC8781E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯……是呐！回家了——回家了——！"

    window hide

    pause 0.5

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1.2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_84FFC5F453EF42B4930F22019DFD44D0 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_08C43A31F7C049DDB885DFB2FB7A471D as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_2B49DF326D8641F283BDF0EC54525573 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊～说是那么说，好方法也不是那么容易想出来的。{w}\n肯定不能维持现状，但不这么做客人肯定会减少。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "唔～嗯。确实客人会减少，\n但完全不让客人减少也是太理想化了。"

    show rs_image_5FBD78374DA74E3DAE8DB6DA14DD5616 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "就像我在不喜欢男人的情况下仍然喜欢上了你一样，\n从中找出一些好的地方就行了吧。"

    show rs_image_E435B1F7BF9B4AB280BA8F0C6B392FB1 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯～……啊，正在话中不过，\n{w=0.5}{nw}"
    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "说不定我的行动也是导致客人减少的一个原因。"

    show rs_image_178EB238919E4D3E993E1EDC3E68F09B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "怎么说？"

    show rs_image_A6E2B83133264FE2AC7ED2F9767DAB76 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "以我为目的的客人确实多了，不过相对的其他一般客人也就少了。"

    show rs_image_AAC229C565304B76BADD3819ED261CD1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊——……就像我家老爷子那样，\n被不知情的人知道后会怕的不敢来的地方呢。"

    show rs_image_97AEAB5F7F86404C83B970C313450D38 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "既然如此，专注于增加那部分客人不就行了！"

    show rs_image_08C43A31F7C049DDB885DFB2FB7A471D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不不～比起那些一般客人，冲我来的明显要多得多。"

    show rs_image_06FD3372A1FE4B4FB675F0FFE43B7CB3 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "自己说有点那个，我还真是魔性呐。"

    show rs_image_2B49DF326D8641F283BDF0EC54525573 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "要是能想到在其他客人的忍受范围内\n满足这部分客人的方法就完美了……"

    show rs_image_703A7A7ABA4F41909E06EDD001459F9F as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "唔～嗯。那种程度的接客，GAY们和正太控们真的会满足吗。"

    show rs_image_BE8486E53367484D8879711D82BE0D21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不，虽说情况各种各样，\n但公共场合之下做别人不喜欢的事是肯定不允许的。"

    show rs_image_5F7F71AF58394C1898380FA26B3DC19B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那点程度就给我好好忍着！不过，至少要以他们会来这种程度对待呢。"

    show rs_image_2B49DF326D8641F283BDF0EC54525573 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那个，正太控是……喜欢年轻男孩子的人……？"

    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯嗯，不同人喜欢的年龄层次差距很大，\n我家的话主要是喜欢中学生的，毕竟冲着我来的。"

    show rs_image_AAC229C565304B76BADD3819ED261CD1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那些所谓的正太控，不跟他们做就不行么？"

    show rs_image_DFA5315B887F4308A9E050235004ED07 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不是很明白不过，真心喜欢的话，\n不是应该为那种努力工作的样子感动么？"

    show rs_image_12E394DC341C4685AB17E83FEED856C9 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦……也有道理。毕竟H也不是全部。"

    show rs_image_9387C2EF08BB4EFABA360A19A1E02C8B as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "穿条稍微短点的裤子接客应该就差不多了。"

    show rs_image_40F4B3A56AFE46FCB14F4500CD625791 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "得上网找找适合制服的短裤……"

    show rs_image_C89084D62C814F9485051B8CC617A899 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那点程度的话普通的客人也不会说什么，不是很好么！？"
    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯，是呐。然后就是，我家在圈子里的那些传闻了。"

    show rs_image_A6E2B83133264FE2AC7ED2F9767DAB76 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "一开始就是在学校里传开的，\n事到如今我再去澄清也完全不会被相信吧。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_BE8486E53367484D8879711D82BE0D21 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那就由我来！由我来四处澄清！！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "真的吗？可能会很麻烦的，可以吗？"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_909AB6EEDA4E46FEBDCAC93ADC5C7F8C as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那不是你该在意的地方。互相分担一下麻烦的事不是么。"

    show rs_image_13EEE138043542FB90557CFB44BADDE4 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "目的一致，只要互相尽全力就好了！对不。"

    show rs_image_C5F31BAC461D43B9A8E59CAB2E60793D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "三酱……{w}\n{w=0.4}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    # Gallery unlock: images/CG/I-am-none-gay-with-no-lovers/I-am-none-gay-with-no-lovers 8.png
    $ zorder_rs_image_E8909DD316534842888A95088CBFE945 = -100
    show rs_image_E8909DD316534842888A95088CBFE945 as rs_image_E8909DD316534842888A95088CBFE945 zorder zorder_rs_image_E8909DD316534842888A95088CBFE945 onlayer master
    hide rs_image_E8909DD316534842888A95088CBFE945

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_E8909DD316534842888A95088CBFE945 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.4

    extend "最喜欢了♪"

    window hide

    pause 1

    show rs_image_530777FF5DE0403C85E0F13A632298D3 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_DCEBC7527B8F4B4EA0FF44E692174034

    pause 2.7

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 400
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003AAC

    return

label block_00003AAC:
    # Node: 00003AAC (Phase: 98)
    $ C2S4Phase = C2S4Phase - 1

    if judge_lm_condition([]):
        jump block_00003AAD

    return

label block_00003AAD:
    # Node: 00003AAD (CP2 Daytime 三朗)
    call block_00001106 from _call_block_00001106_1

    if judge_lm_condition([]):
        jump block_00003AB5

    return

label block_00003AB5:
    # Node: 00003AB5 (我是直的，現無對象 4)
    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_AEF730D86D5343AF81880AC735BAFAC6 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 0.6

    $ set_window("イベントモード")
    window show

    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 200
    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_A6BDA5B155414D99AB52F15BEBCC03D6 as tag_0C07D2341065492CB0EDF00452D574E1 at right_top zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    rs_character_7C178421D3DA4E2CB70D4336919888FB "呀，三朗前辈。"

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "你好。"

    hide tag_0C07D2341065492CB0EDF00452D574E1
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_1AC471B83CA745FC99DFBE878C4B76B2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "杉本先生！？还有陆田先生也！啊，说起来演讲是今天。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_D8F7AF82CDFF4CD8A8E72C266EF308A7 as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_4270FFC84A7349BBA09AEC87EEEB8374 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "好无情～连受过那么多照顾的人的事都记不住。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔，这还真是抱歉。"

    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "开玩笑的，看起来也好像很忙的样子，\n我们这边其实也忙成一团乱了。"

    show rs_image_260B6EA5E2024E0FB6E0794B290A9A13 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "那么抱歉打扰，我们得走了。"

    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_9ADA3ECA775E4BF5904664E9A36296FB as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊。那个！我、我多亏杉本先生终于明白了自己！"

    show rs_image_909AB6EEDA4E46FEBDCAC93ADC5C7F8C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "真的、非常感谢！！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    show rs_image_A63B42C307234264B96E3CFB1DB70A3E as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7C178421D3DA4E2CB70D4336919888FB "不客气。今后要更加率直地前进哦。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_E54B94670E804565963ECDB491A87076 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "是！能感染心底的话语呐，谢谢！！"

    window hide

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_DFA3500588174872BA20EBF28D506BD4
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B07A8E220AE74102B4BA1B35DB2728B1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_DFA3500588174872BA20EBF28D506BD4 = 200
    $ zorder_tag_0C07D2341065492CB0EDF00452D574E1 = 200
    show rs_image_EF41876385624D9AA00C7184151E7B34 as tag_DFA3500588174872BA20EBF28D506BD4 at left_top zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    show rs_image_D2E31CDD8AE14CA4A56BC2EFC98D23CB as tag_0C07D2341065492CB0EDF00452D574E1 at right_top zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    pause 0.3

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "……那个人看起来很仰慕你啊，难道真的是徒弟？"

    show rs_image_7B65B699C52F4E6CBDB4D49A5A082D25 as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7C178421D3DA4E2CB70D4336919888FB "已经毕业了哦。\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_08DE3E55D82547A2976A4EC1795ECD1A as tag_DFA3500588174872BA20EBF28D506BD4 zorder zorder_tag_DFA3500588174872BA20EBF28D506BD4 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那么为了解决其他更多烦恼我们走吧！"
    show rs_image_A6BDA5B155414D99AB52F15BEBCC03D6 as tag_0C07D2341065492CB0EDF00452D574E1 zorder zorder_tag_0C07D2341065492CB0EDF00452D574E1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_40D73C5DA312475C905F6D1BC2C39FB7 "好的。"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    rs_character_6E0C80C17CC249E2A7A71BB4349C957B "{size=32}要加油了！！{/size}"

    window hide

    pause 0.4

    hide tag_DFA3500588174872BA20EBF28D506BD4
    hide tag_0C07D2341065492CB0EDF00452D574E1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_E7A7EFABF8B949FEADD23029D844B4E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_F58ABF21359B4B2EA4ED7022D95A52FE as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欢迎光临～！两位客人～♪"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_3D45A7FC99584EC48CA484154ACF4CA8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_BCC96979835C48B5A3DDA509A4B82C4B as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "客人，水温如何？有什么问题要直说哦～"

    window hide

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    if sys_effect_current_file != "sound/Effect Sound/Bathroom 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Bathroom 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Bathroom 3.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C64C83CF9569441D995A82BA3F3F49A4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9E09486464FF4D6B9B164050310B14B2

    pause 0.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=30}下次请继续光临！{/size}"

    pause 0.4

    window hide

    pause 0.8

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_B6D2CFDC1CB5407EACD7FBC1D100D198

    call scb_flag_title_end(2, _("「我是直的，现无对象」")) from _call_scb_flag_title_end_7

    if judge_lm_condition([]):
        jump block_00003AB1

    return

label block_00003AB1:
    # Node: 00003AB1 (Phase: 0)
    $ C2S4Phase = 0
    if Chapter <> 2:
        $ del C2S4Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_00003AB6
    if judge_lm_condition([]):
        jump block_00003AB4

    return

label block_00003AB6:
    # Node: 00003AB6 ()

    return

label block_00003AB4:
    # Node: 00003AB4 (FINISH)
    $ C2S4 = True
    $ TalkShintaroF4After = True
    $ TalkSumoRikuF4After = True
    $ TalkSaburoF4After = True

    if judge_lm_condition([]):
        jump block_00003AB8

    return

label block_00003AB8:
    # Node: 00003AB8 (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_5

    if judge_lm_condition([]):
        jump block_00003AB6

    return

label block_00003B84:
    # Node: 00003B84 (TO: Lose)

    if judge_lm_condition([]):
        jump block_00003B81

    return

label block_00003B81:
    # Node: 00003B81 (TO: Lose)

    if judge_lm_condition([]):
        jump block_00003B74

    return

label block_00003B74:
    # Node: 00003B74 (Lose)
    $ YKKLoseScene = Random(4)

    if judge_lm_condition([{ "scope": 0, "content": "YKKLoseScene == 0" }]):
        jump block_00003B75
    if judge_lm_condition([{ "scope": 0, "content": "YKKLoseScene == 1" }]):
        jump block_00003B76
    if judge_lm_condition([{ "scope": 0, "content": "YKKLoseScene == 2" }]):
        jump block_00003B77
    if judge_lm_condition([]):
        jump block_00003B78

    return

label block_00003B75:
    # Node: 00003B75 (1)
    hide tag_9EEEA1BE275245F69D2CBDC443AA4142
    hide tag_19556E53939043CAAFFEEEA7F99D768A
    hide tag_AD81C50A7A3E4C2484B608BBA4A55087
    hide tag_445345A84BCD459E8C2AC2BA7651355B
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    pause 1

    if sys_effect3_current_file != "sound/Effect Sound/Sorry 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Sorry 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Sorry 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_D123F79A6B5940889E3CF0422ABE8095 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_40F7FF2696DF4E32B61F8E217EFC8A9A

    pause 0.8

    window show

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_6C2965CB0398406E88B7AF94413DDC5C as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔……可恶～"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B7A

    return

label block_00003B7A:
    # Node: 00003B7A (TO: Character)

    if judge_lm_condition([]):
        jump block_00003B7B

    return

label block_00003B7B:
    # Node: 00003B7B (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "YKKCharacter == 0" }]):
        jump block_00003B79
    if judge_lm_condition([]):
        jump block_00003B7F

    return

label block_00003B7F:
    # Node: 00003B7F (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "YKKCharacter == 1" }]):
        jump block_00003B80
    if judge_lm_condition([]):
        jump block_00003B87

    return

label block_00003B87:
    # Node: 00003B87 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "YKKCharacter == 2" }]):
        jump block_00003B86

    return

label block_00003B76:
    # Node: 00003B76 (2)
    hide tag_9EEEA1BE275245F69D2CBDC443AA4142
    hide tag_19556E53939043CAAFFEEEA7F99D768A
    hide tag_AD81C50A7A3E4C2484B608BBA4A55087
    hide tag_445345A84BCD459E8C2AC2BA7651355B
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    pause 1

    if sys_effect3_current_file != "sound/Effect Sound/Sorry 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Sorry 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Sorry 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_D123F79A6B5940889E3CF0422ABE8095 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_40F7FF2696DF4E32B61F8E217EFC8A9A

    pause 0.8

    window show

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_91D6AB046C4B44AD8E8AD4C9C9DC7407 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊嚏！！为、为什么会这样！！"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B7A

    return

label block_00003B77:
    # Node: 00003B77 (3)
    hide tag_9EEEA1BE275245F69D2CBDC443AA4142
    hide tag_19556E53939043CAAFFEEEA7F99D768A
    hide tag_AD81C50A7A3E4C2484B608BBA4A55087
    hide tag_445345A84BCD459E8C2AC2BA7651355B
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    pause 1

    if sys_effect3_current_file != "sound/Effect Sound/Sorry 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Sorry 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Sorry 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_D123F79A6B5940889E3CF0422ABE8095 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_40F7FF2696DF4E32B61F8E217EFC8A9A

    pause 0.8

    window show

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_6440D6C806CA421DA7B4B79725153866 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这个混蛋——！！好羞耻……"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B7A

    return

label block_00003B78:
    # Node: 00003B78 (4)
    hide tag_9EEEA1BE275245F69D2CBDC443AA4142
    hide tag_19556E53939043CAAFFEEEA7F99D768A
    hide tag_AD81C50A7A3E4C2484B608BBA4A55087
    hide tag_445345A84BCD459E8C2AC2BA7651355B
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    pause 1

    if sys_effect3_current_file != "sound/Effect Sound/Sorry 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Sorry 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Sorry 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_D123F79A6B5940889E3CF0422ABE8095 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_40F7FF2696DF4E32B61F8E217EFC8A9A

    pause 0.8

    window show

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_6C2965CB0398406E88B7AF94413DDC5C as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……为什么我要被这样对待！？"

    window hide

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B7A

    return

