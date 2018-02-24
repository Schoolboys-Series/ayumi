# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003FD6 (FLAG: 異我戰紀)

label block_00003FD7:
    # Node: 00003FD7 ()

    if judge_lm_condition([]):
        jump block_00004021

    return

label block_00004021:
    # Node: 00004021 (Phase: 99)
    $ C3S1Phase = 99

    if judge_lm_condition([]):
        jump block_00004022

    return

label block_00004022:
    # Node: 00004022 (F1 START)
    call scb_flag_title(3, _("「异我战纪」")) from _call_scb_flag_title_16

    if judge_lm_condition([]):
        jump block_0000401F

    return

label block_0000401F:
    # Node: 0000401F (異我戰紀 1)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    if sys_music_current_file != "sound/BGM/Afternoon.ogg":
        play music "sound/BGM/Afternoon.ogg" loop
        $ sys_music_current_file = "sound/BGM/Afternoon.ogg"

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    show rs_image_1094C02923E34A60B4DCA6F851A39FB0 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at center_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.5

    window show

    rs_character_D34F60C882F0425E93252349E8C3BC8D "失礼了，请问绫濑忍前辈在吗？"

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，清君，你好呀～忍现在去摘花了哦。"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "很快就会回来，要在这里等吗？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_68B33F61F67D45A5900AAF8747F25ACA as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "上午好，森海前辈，谢谢提醒。那就恭敬不如从命了。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_11C6196C960646A1860CECE1AE21494F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈♪森海前辈！说的也是呐～！\n我也到了能被称呼为前辈的岁数了呐～！"

    show rs_image_27FF4633286B4DF59BF4C1A761DDF98E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼～！有种好伟大的感觉。"

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_D7BB1A8267AE4353950D17F94CE6C389 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "会那么想就一点都不伟大了哦～友亲。\n"
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "你好你好，后辈君。{w=0.3}{nw}"
    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    show rs_image_1094C02923E34A60B4DCA6F851A39FB0 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at right_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend ""

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_8CBDCCA85F2D41C69D53D9882E8E8DE3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D34F60C882F0425E93252349E8C3BC8D "啊……慎、慎太郎前……辈。上次那个……那个……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_29B059D0AECE4F3FBF86EE5DA29B17DF as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_8CBDCCA85F2D41C69D53D9882E8E8DE3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at center_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸欸！？这是什么气氛！难道……清君也被慎酱那个过？！"

    show rs_image_4BBDCD83023642F6923D76BE102A1BB9 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼呼呼……我和这个学校大部分学生都维持着关系哦。"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    show rs_image_C9A169B5FECE487BAE71B3017B79B0B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶诶诶诶诶！？！？"

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_68B33F61F67D45A5900AAF8747F25ACA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D34F60C882F0425E93252349E8C3BC8D "奥村前辈，前几天教我的{color=#FF80FF}打招呼的方法{/color}，像这个样子可以吗……？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "OKOK！从今往后好好使用这个\n{color=#FF80FF}{/color}像是{color=#FF80FF}和前辈那个后的后辈{/color}的打招呼方法即可！！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸欸欸欸欸……"

    show rs_image_1094C02923E34A60B4DCA6F851A39FB0 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "真是太好了！如果有我能做到的事，请不要在意交给我。"

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_29B059D0AECE4F3FBF86EE5DA29B17DF as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "清君真是个理想的后辈啊，因为是武道系的，对前辈的话也非常遵从。"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呐——呐——果然忍是个好前辈？是清君憧憬的前辈吗？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    show rs_image_98DDCAE3975441ECB139AB353E188706 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at center_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D34F60C882F0425E93252349E8C3BC8D "是的！绫濑前辈是我最尊敬的人了。\n空手道非常厉害，也时常保持着进步之心！"

    if sys_effect2_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_19EA6CF277DB411DAAFC4FAD639EE7DA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "练习不曾放松，锻炼也是。几乎是心技体全部都非常优秀的，理想中的人物。"

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_29B059D0AECE4F3FBF86EE5DA29B17DF as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_FB35B45BE8F34C718941BDF10B1073A6 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at center_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_6636F3FA642745AE8103D258F3BF47F2 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦！那么，就由和他相处这么久的我们\n来告诉你他之所以如此强大的秘诀！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_B1B2F785D2ED49CF8DA090E58CB79206 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "请、请务必、请务必告诉我！"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_83D9AE51F7F644FA8FBA1490DE4D4EFE

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_D8FBA8060A9B457F9D8A35FB71E72F10 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "其实意外地非常简单！原动力竟然是！对动画、漫画和游戏的憧憬！！"

    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "也就是所谓的“中二病”呐～"

    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我和忍住在同一幢公寓，有时会听到他喊出游戏或者漫画里的技能名。"

    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "之前有一次为了高涨气氛，还被要求{color=#008080}弹BGM{/color}。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_6270692056B84C53A338DA44C7F6681B as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_29B059D0AECE4F3FBF86EE5DA29B17DF as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "把小忍{color=#008080}画成格斗游戏的角色{/color}的时候他超高兴的呐，\n真是意外～{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_550AF2E6D7FA4B33B8A18AFDAA320248 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_19EA6CF277DB411DAAFC4FAD639EE7DA as tag_988AD5B87A6D42E59078E032C7FA7EB1 at center_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "欸～！欸～！！前辈居然会有这么一面！\n"
    show rs_image_98DDCAE3975441ECB139AB353E188706 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "我也要好好学习，找一个类似的……"

    window hide

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    if sys_music2_current_file != "sound/Effect Sound/Open window 1.ogg":
        play music2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_BEF582EB5C1541099B31FB6D3CD3509F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 0.3

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "等等你们两个，对可爱的后辈灌输什么。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    show rs_image_68B33F61F67D45A5900AAF8747F25ACA as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "绫濑前辈！等候你摘花归来已经很久了。\n没想到会去观赏花卉，真是意外呐。"

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_285E40B50F3F466F9AE41CD837D82E42 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，摘花并不是那个意思……"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友……那是女性为了礼仪用的代称。\n"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_1F7EBBD8148642B1BC2DC1A8430AE7A7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "好～好记住了哦。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_FD381C6412CC4FE7A52F90CB708C2E44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "噫！！学、学到了……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1094C02923E34A60B4DCA6F851A39FB0 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "说起来，清找我有什么事？"

    show rs_image_DD2521E5C93C4C7A9DD6C7B09A64AD4B as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "啊，嗯。其、其实，我有话要对前辈说……\n"
    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "不太方便在这里，可以稍微占用一点时间吗？"

    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……？{w=0.4}嗯，我明白了。那我先离开一会。"

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好的好～的，慢走不送。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    show rs_image_1094C02923E34A60B4DCA6F851A39FB0 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at center_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D34F60C882F0425E93252349E8C3BC8D "奥村前辈，森海前辈，多有打扰了。谢谢你们陪我说话。"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1.5

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "会、会是什么呐，到底会说什么呐。清君找忍到底会说什么呐？？"

    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "这种展开难道不就正是那个嘛～？"

    stop music fadeout 2
    $ sys_music_current_file = ""

    window hide

    pause 2

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_FB35B45BE8F34C718941BDF10B1073A6 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222BBB56F7BA4025B3E942F40786CBC9

    pause 0.5

    window show

    rs_character_D34F60C882F0425E93252349E8C3BC8D "绫、绫濑前辈……那个、嗯……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "怎么了？这个样子。"

    show rs_image_7AA4ECED07D244169095125FC38A41CA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D34F60C882F0425E93252349E8C3BC8D "其实……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    window hide

    pause 0.4

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_1C3AC3BC102640A98B0B848A29849370

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_AF94A35C318D4B85B312BF572DEEDA13 = 0
    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_AF94A35C318D4B85B312BF572DEEDA13 at center_bottom zorder zorder_tag_AF94A35C318D4B85B312BF572DEEDA13 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.9

    if sys_music_current_file != "sound/BGM/Something strange 1.ogg":
        play music "sound/BGM/Something strange 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something strange 1.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，欢迎回来～忍～\n"
    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "呐呐呐，都、都说什么了？"

    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "有点事。{w}对了，今天我会晚些回去，晚饭就不用管我了。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C9A169B5FECE487BAE71B3017B79B0B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！到到到到底怎么了！？明明约好了要一起吃饭的？！"

    show rs_image_D5EEA08F613D4581B90B56569FE7A25D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "现在有了无法推卸的事，所以，只能这样。"

    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸……"
    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "呐，呐……难道说，\n刚才你们所谓的谈话……{w}（吞口水）……"

    show rs_image_864148A734BC4812B08CBBF3D01B3978 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "抱歉，有些需要好好想想的事，等下再说。"

    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……好……\n"
    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "那，明天！明天一定要一起回去一起吃饭哦！！"

    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "好好。"

    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "绝对的哦！"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.9

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_41210EA5B30342049A9A851AEFDF7211 = 100
    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_41210EA5B30342049A9A851AEFDF7211 at center_top zorder zorder_tag_41210EA5B30342049A9A851AEFDF7211 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……嗯。"

    window hide

    pause 0.8

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 400
    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 200
    show rs_image_23E95FF3D12540FB88BD74983BE7800E as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_FB35B45BE8F34C718941BDF10B1073A6 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 0.8

    window show

    rs_character_D34F60C882F0425E93252349E8C3BC8D "其实……{w=0.5}{nw}"
    show rs_image_8CBDCCA85F2D41C69D53D9882E8E8DE3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "我对前辈有一件不情之请。"

    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不情之请？"

    show rs_image_FB35B45BE8F34C718941BDF10B1073A6 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "是的。我的朋友中有个叫做{color=#00FFFF}“中山”{/color}的，\n最近，他好像在放学路上被奇怪的人跟踪了。"

    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "跟踪狂？"

    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "好像就是这样的。{w}几天前我把前辈的事情告诉中山后，\n他希望前辈能帮忙抓住那个可疑人物。"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哦、哦……可是，根本不知道那个跟踪狂是什么样的人，无从下手啊。"

    show rs_image_7AA4ECED07D244169095125FC38A41CA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "这个……这么说很不客气但他希望能和前辈一起回去，\n在现场根据情况处理……"

    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "总之就是保护他。"

    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "就、就是这样子……的。"

    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……{w=0.4}我明白了。如果我可以的话会帮忙的。\n无法事先预防的情况下，这确实是最好的。"

    show rs_image_98DDCAE3975441ECB139AB353E188706 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "非、非常感谢！！谢谢前辈的好意！\n"
    show rs_image_1094C02923E34A60B4DCA6F851A39FB0 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那可以请前辈在今天社团活动结束后开始吗？"

    rs_character_D34F60C882F0425E93252349E8C3BC8D "中山参加了排球部，回家的时间应该和我们很接近。"

    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊，今天……"
    show rs_image_5EEBBCC1A1DD424FA293CA4EA0C6C4C6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.55

    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    extend "不，没事，可以。\n那就来好好考虑对策。"

    show rs_image_68B33F61F67D45A5900AAF8747F25ACA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "好的！那就拜托了！！非常感谢！"

    window hide

    pause 0.5

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.5

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "（被拜托倒是无所谓，可到现在连那孩子长什么样都不知道。）"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 300
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 0.5

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……究竟会是怎样的人呢。"

    window hide

    pause 0.8

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_AF94A35C318D4B85B312BF572DEEDA13
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_41210EA5B30342049A9A851AEFDF7211
    with rs_effect_DCEBC7527B8F4B4EA0FF44E692174034

    pause 2

    $ set_window("イベントモード")
    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_52F632A326A24F87B73C4565A9760408 as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_E9592A382F574338BCE51B690BEBEF00 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    if sys_music_current_file != "sound/BGM/Something comical 1.ogg":
        play music "sound/BGM/Something comical 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something comical 1.ogg"

    pause 0.4

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "啊，初次见面绫濑前辈～今天都请多多关照了～哦☆"

    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 0
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5EEBBCC1A1DD424FA293CA4EA0C6C4C6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "（居然是这种类型的……）"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_6581541AC4C34DE4AD8AE0D6865112C1 as tag_2F2406ABFD334A9FAFFFD526F608E209 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "不过啊，前辈真的超～可～爱～呐～！！\n这下子那个恶心男绝对会出来的～！"

    show rs_image_52F632A326A24F87B73C4565A9760408 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "前辈！到那个时候就拜托了哦～？"

    show rs_image_8CBDCCA85F2D41C69D53D9882E8E8DE3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊、嗯……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_7AA4ECED07D244169095125FC38A41CA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "中山！难得前辈不辞劳苦过来，放尊重点。"

    show rs_image_6581541AC4C34DE4AD8AE0D6865112C1 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "清酱好严厉哦～！所以才说武道系的人啊～\n"
    show rs_image_BACDF64086FF46D591FBC9644AD521FA as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "哦，抱歉☆不是说的前辈哦。"

    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "呃……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_D34F60C882F0425E93252349E8C3BC8D "前辈，真的很抱歉，他是在太失礼了……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不，没事。某种意义上也算安心了。"
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_7AA4ECED07D244169095125FC38A41CA as tag_988AD5B87A6D42E59078E032C7FA7EB1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_52F632A326A24F87B73C4565A9760408 as tag_2F2406ABFD334A9FAFFFD526F608E209 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    extend "我们该走了。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_6581541AC4C34DE4AD8AE0D6865112C1 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "好～的！前辈的勇姿，好期待呐！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "明明是前辈不用出手就解决才更好……"

    window hide

    pause 0.5

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_FB8046DBE16F4BA8BE96613E8F3A850C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_FB35B45BE8F34C718941BDF10B1073A6 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_52F632A326A24F87B73C4565A9760408 as tag_2F2406ABFD334A9FAFFFD526F608E209 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.4

    window show

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "不过说起来啊～"
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    show rs_image_6581541AC4C34DE4AD8AE0D6865112C1 as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "前辈真的{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Boom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 2.ogg"

    extend "又{color=#FF00FF}小只{/color}又{color=#FF00FF}可爱{/color}，{w=0.55}就像{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Gun 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Gun 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Gun 1.ogg"

    extend "{color=#FF00FF}女孩子{/color}一样～呐☆"

    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_D1F333EE573A4AE8B656140B08D6CC17 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_5EEBBCC1A1DD424FA293CA4EA0C6C4C6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_D34F60C882F0425E93252349E8C3BC8D "什、中山！！不许说禁句，何况是一次全都说出来！{w}\n真、真的非常抱歉，绫濑前辈！！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "没、没事，没关系。能毫不掩饰地说出心中所想也算是某种优点……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect3_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_BACDF64086FF46D591FBC9644AD521FA as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "哇☆表扬我了吗？？哇——！！\n"
    show rs_image_6581541AC4C34DE4AD8AE0D6865112C1 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "被前辈表扬了——！"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔～有像你这种类型的人在身边，也算是很新鲜了……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_52F632A326A24F87B73C4565A9760408 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "那我会更多更多地这么说的哦！会更努力的哦！那个那个☆"

    window hide

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    # Gallery unlock: images/CG/Legacy-of-asynchronized-myself/Legacy-of-asynchronized-myself 1-1.png
    $ zorder_rs_image_F8ABD783506148DE8982E63A2D047172 = -100
    show rs_image_F8ABD783506148DE8982E63A2D047172 as rs_image_F8ABD783506148DE8982E63A2D047172 zorder zorder_rs_image_F8ABD783506148DE8982E63A2D047172 onlayer master
    hide rs_image_F8ABD783506148DE8982E63A2D047172

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_F8ABD783506148DE8982E63A2D047172 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.4

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔？"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D34F60C882F0425E93252349E8C3BC8D "你想干什么！"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "身体检查～♪哇，身材好细呐～不过肌肉很结实？不是完全没用呐。"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "想不到会是和{color=#00FFFF}那种话{/color}相匹配的人～"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "诶，哪种话？从清那里听到过什么？"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "那是别的事情哦～跟踪狂什么的会不会快点出来呐。"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "对！前辈！把那家伙打得落花流水时务必也要让我补上一拳哦！解解气♪"

    rs_character_D34F60C882F0425E93252349E8C3BC8D "中山，不要误会了，空手道才不是用来伤害别人的道具……"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "好好……啊？"
    stop music fadeout 0.6
    $ sys_music_current_file = ""

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_36776B46243D4A7D99700F4B8FF44CF1 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    pause 0.3

    extend "那家伙！前辈，就是他！！\n超级恶心的跟踪狂！！那边的阴影里！"

    if sys_music_current_file != "sound/BGM/Strange idea.ogg":
        play music "sound/BGM/Strange idea.ogg" loop
        $ sys_music_current_file = "sound/BGM/Strange idea.ogg"

    rs_character_D34F60C882F0425E93252349E8C3BC8D "真、真的，看上去就很古怪……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那个人的目的到底是什么。"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "哇——！真的好恶心！！前辈！在他逃走前快点抓住！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "是呢，至少听一下对方的理由。"

    window hide

    pause 0.6

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    show rs_image_F7B4BBF8CE1F42548986125166418110 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_35899B38CB87497A86C6FFE9A60CEA05 as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "那边那个！！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "噫！？"

    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "一～直跟着我到底是什么意思！？那种恶心的氛围都破坏环境了！"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "要是害我生病该怎么才好？？不想和你呼吸一样的空气，给我消失。"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "唔、唔……"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "给我说点什么！！"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "你至今为止一直跟踪着的最喜欢最喜欢的对象可是和你说话了啊。"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "还是说太兴奋了说不出话来？？\n"
    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    extend "真恶～心，真是怀疑你这样还能出门的神经！"

    window hide

    pause 0.4

    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_FB8046DBE16F4BA8BE96613E8F3A850C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……呐，我们真的有出现的必要？那孩子不就自己一个人全都处理了嘛……"

    rs_character_D34F60C882F0425E93252349E8C3BC8D "某种意义上那种语言暴力带来的伤害或许更大……"

    window hide

    pause 0.3

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    show rs_image_F7B4BBF8CE1F42548986125166418110 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.4

    window show

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "唔、唔唔唔……"

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    show rs_image_0123524CA5E24154A0F3510F5C639B95 as tag_2F2406ABFD334A9FAFFFD526F608E209 at left_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "这家伙怎么回事，完全不说话！呐，前辈，早点把他打倒！"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不用了，你的言语已经很充足。这个人已经完败了。"

    show rs_image_548B0025EC14496F9D55EDBD556F4843 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "欸欸～！说什么呢！！就算这样我也不能解气！！"

    show rs_image_51752209FD9740FAB88518A45B39FA1D as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "被折腾了这么久，可要好好讨要赔偿！"

    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "可是，对毫无抵抗的人是不能出手的。\n再怎么说用暴力使人屈服是不好的。"

    stop music fadeout 3
    $ sys_music_current_file = ""

    show rs_image_BACDF64086FF46D591FBC9644AD521FA as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "……哈、哈啊？开、开玩笑吧？绫濑前辈居然会说出这种话……"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "前辈什么时候变得这么软弱了？"

    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    show rs_image_B1B2F785D2ED49CF8DA090E58CB79206 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at right_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    rs_character_D34F60C882F0425E93252349E8C3BC8D "你、你、说什么。"

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_6581541AC4C34DE4AD8AE0D6865112C1 as tag_2F2406ABFD334A9FAFFFD526F608E209 at left_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "我可是知道前辈小学时的光荣事迹的哦！\n只要看到不顺眼的人就会上去暴打一顿……"

    show rs_image_7DC581F0926C46E1B9B46277F2729C93 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "才、才没有那种……"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "害什么羞嘛！不是很好嘛。那种很帅气。"

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_52F632A326A24F87B73C4565A9760408 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_014C49487C644BFD95C49FCA0B26030E as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_7F67F5F44DB547A1BE823BA2E67A759D

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "然后，中学时也会对看不顺眼的其他前辈暴打一顿，\n就连现在也经常能听到前辈的暴力新闻。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "这种人现在居然会装好孩子……别做梦了！！"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "前辈不是这种人！\n就像平时一样用最上手的暴力手段直接让对方屈服不就好了！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "怎么可以……我是……"

    window hide

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    pause 0.9

    if sys_effect_current_file != "sound/Effect Sound/God 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/God 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/God 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.9

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "{size=24}{color=#FF00FF}啊啊～果然，是毒舌系的抖S……{/color}{/size}{nw}"
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend ""

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_F8101B0A7E6F44B392F6C520B24C2F1E "{size=32}诶？{/size}"

    window hide

    pause 0.4

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    window show

    if sys_music_current_file != "sound/BGM/Flurry 1.ogg":
        play music "sound/BGM/Flurry 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 1.ogg"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "第一次见面时我就这么觉得了！你才是我理想中男孩子的类型。"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "更多，更多用轻蔑的眼神看着我……！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    show rs_image_20B77D172B0E46CF9955CA6BAE50636F as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "什、什……什么……这家伙……？！"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "我不会伤害你的哦，只要能被你不断欺负就很满足了。"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "……"

    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    show rs_image_B1B2F785D2ED49CF8DA090E58CB79206 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at right_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_20B77D172B0E46CF9955CA6BAE50636F as tag_2F2406ABFD334A9FAFFFD526F608E209 at left_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D34F60C882F0425E93252349E8C3BC8D "中、中山？还好吧？振作一点！"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "……{w=0.5}{nw}"
    show rs_image_51752209FD9740FAB88518A45B39FA1D as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "哦，发现了个有意思的人呢。就那么想被我欺负……？"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "是、是的！……欸！？真、真的要这么做！？"

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    show rs_image_6581541AC4C34DE4AD8AE0D6865112C1 as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "呵呵，行，做就做。真是不错的相遇呐，我和你相性还可以。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "欸！？"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Battle 6.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Battle 6.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Battle 6.ogg"

    # Gallery unlock: images/CG/Legacy-of-asynchronized-myself/Legacy-of-asynchronized-myself 2.png
    $ zorder_rs_image_C8A84981806B4A4DB2B6D92C97AE2032 = -100
    show rs_image_C8A84981806B4A4DB2B6D92C97AE2032 as rs_image_C8A84981806B4A4DB2B6D92C97AE2032 zorder zorder_rs_image_C8A84981806B4A4DB2B6D92C97AE2032 onlayer master
    hide rs_image_C8A84981806B4A4DB2B6D92C97AE2032

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_C8A84981806B4A4DB2B6D92C97AE2032 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_44331B79D1D84C7EAA35F0480004721A

    pause 1

    window show

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "好～！那，从今天开始你就是我的奴隶了！\n要能合我的心情，就会好好欺负你的。"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "先说好，什么时候我没兴趣了，马上给我滚。"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "真、真的嘛！！感嗯戴德！感嗯戴德！"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "也只是我玩腻之前而已呐。那就想法让我满足好了，走♪"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "去、去什么地方？"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "你需要调教，两人独处的话会更方便哦？"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "来，好好干活，奴隶君的第一个工作。"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "遵、遵命！！"

    rs_character_D34F60C882F0425E93252349E8C3BC8D "等、等等！怎么突然这样了！！和那种人一起没问题！？"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "没事没事！我并没有乱来♪"
    if sys_effect_current_file != "sound/Effect Sound/Trumpet 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Trumpet 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Trumpet 1.ogg"

    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    extend "奴隶，前进！！"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "噫！！Yes sir！！！"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "拜拜清酱☆前辈也是——！要玩得高兴哦——！"

    window hide

    pause 0.6

    stop music fadeout 2
    $ sys_music_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 1.2

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    rs_character_D34F60C882F0425E93252349E8C3BC8D "就像飓风一样……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_B1B2F785D2ED49CF8DA090E58CB79206 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "啊……前辈，真的很抱歉！！中山那家伙太无礼了！"

    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸？没事……"

    show rs_image_8CBDCCA85F2D41C69D53D9882E8E8DE3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D34F60C882F0425E93252349E8C3BC8D "特别是居然会说前辈引起过暴力事件！无论如何都无法原谅！！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_DD2521E5C93C4C7A9DD6C7B09A64AD4B as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D34F60C882F0425E93252349E8C3BC8D "前辈的空手道只是基于对游戏和漫画世界纯粹的憧憬才对！"

    show rs_image_8CBDCCA85F2D41C69D53D9882E8E8DE3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "这种力量不可能会用到暴力上的。即便如此，那家伙……！！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "清，不是这样的。\n不，也不能说不是，但我并不是只为那个而不断练习的……"

    show rs_image_FB35B45BE8F34C718941BDF10B1073A6 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "是……这样。"

    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……关于暴力，或许只是被误解了而已。\n在旁人看来或许就是那样的也说不定。"

    show rs_image_864148A734BC4812B08CBBF3D01B3978 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "明明不是为了那种目的而锻炼的，\n却还是被看到了不体面的地方，要好好反省了。"

    show rs_image_7AA4ECED07D244169095125FC38A41CA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D34F60C882F0425E93252349E8C3BC8D "绫濑前辈……"

    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "所以，我很高兴清能有这样的心情，不过不要再继续责备中山君了。"

    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "虽然有些无礼，但仅仅因此出手就只能算暴力。"

    show rs_image_FB35B45BE8F34C718941BDF10B1073A6 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D34F60C882F0425E93252349E8C3BC8D "是……是的。"

    window hide

    pause 0.6

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 3

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_59836EDB597846F2A2C0A683B909166F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    pause 0.6

    window show

    rs_character_DF76892CB0F4478E80A8BB97882BE917 "好，今天的练习就到此为止。面向前，行礼！……互相行礼！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}多谢指教！！{/size}"

    window hide

    pause 0.6

    show rs_image_4A952CA4817E4CAF8759947AF056AFFB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_5EEBBCC1A1DD424FA293CA4EA0C6C4C6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "（唔……不行，根本没法好好练习。）"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "（……没干劲也是无可奈何的，回去好了。{w}\n嗯……约好和谁一起回去来着。）"

    window hide

    pause 0.4

    if sys_music_current_file != "sound/BGM/My precious time of now.ogg":
        play music "sound/BGM/My precious time of now.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time of now.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1.3


    if judge_lm_condition([]):
        jump block_00003FDA

    return

label block_00003FDA:
    # Node: 00003FDA (CP3 Twilight 忍)
    call block_00001B8E from _call_block_00001B8E

    if judge_lm_condition([]):
        jump block_00003FD8

    return

label block_00003FD8:
    # Node: 00003FD8 (異我戦記 2)
    if sys_music_current_file != "sound/BGM/My precious time of now.ogg":
        play music "sound/BGM/My precious time of now.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time of now.ogg"

    $ set_place_title("")

    pause 0.5

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Train 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Train 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Train 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C778499DFA0644D284B0DEC93882F736 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EF2D3A4912BA490B9BDDB92C8700586E

    pause 1.4

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.5

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……所以你觉得那时候大家都说我什么了？真的很过分哦～"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "“碧池太郎”？"

    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！！为什么会知道！？\n{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3F5AF2DAC6F94773B04A709D2558F647 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "这难道不过分吗？！"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "可这就是事实……{w=0.55}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_6A862C1FCD4240298711F04F27EDD9E0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "再说了，为什么性欲会这么强？"

    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_27FF4633286B4DF59BF4C1A761DDF98E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "男性荷尔蒙太多了？"
    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "哇～！那将来我会不会秃顶！"

    show rs_image_83253C644D7341D899A80F5E86570559 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "毕竟体毛越多，头发就越少。"

    show rs_image_3CCC6DE5C5ED405DB1BBB15ECA3CDD44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "明明都是毛，真奇怪～喝酒会不会长大肚子呢～"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "现在还很年轻，不过上年纪后差不多就会那样。\n"
    show rs_image_6A862C1FCD4240298711F04F27EDD9E0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "实话说现在就有点……"

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_C9A169B5FECE487BAE71B3017B79B0B4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "停下！不许继续说了！！\n"
    if sys_music2_current_file != "sound/Effect Sound/Tick tock 1.ogg":
        play music2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_3CCC6DE5C5ED405DB1BBB15ECA3CDD44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    extend "该怎么办？如果我变得比现在要胖的话。"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_B853B4626C714AB6BEEA7293354291C6 "……………………呼。"

    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_FF4A588462534B15B9D5F444704F26BB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哈哈，如、如果真的那样了，我会和友保持一点距离呐。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "太过分了！我们的友情就只有这种程度嘛！？"

    show rs_image_541BC7417880499BB6151B8C86902E0A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哈哈，毕竟只能这样嘛。啊～啊，真奇怪……"

    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "和友说几句后不知为什么心情也好了。"

    show rs_image_0077897C874A47EDBC6EC1288FD65064 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼～！那是因为我就是负离子本身！！"

    show rs_image_6A862C1FCD4240298711F04F27EDD9E0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸——什么东西……好可疑！再说了你真知道负离子是什么吗？"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……总、总而言之，我是治愈系的～！"

    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "难道不是变态系？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_A579F650612D4CA18E2B222221DBF547 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎么可能！还有，那个完全不好笑！？那点程度我也能想出来！"

    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友的笨蛋素质不可能～"

    show rs_image_FF4A588462534B15B9D5F444704F26BB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呵——！！会笑话我是笨蛋的忍也是笨蛋！"

    show rs_image_541BC7417880499BB6151B8C86902E0A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "确实……"
    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "友说不定有着能把人变成笨蛋的能力呢。"

    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么嘛，不要总是这样把别人当成万恶之源……"

    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不，我是在表扬你，虽然只是一丁点。"

    window hide

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_2ECE68226C004D8AB64C8E0BB09BCDE9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.4

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊，说起来，今晚做什么？"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_9538619ECD0849688D07CEC63FB8B083 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{color=#FFFF00}友特供的蛋包饭～♪{/color}吃了这个就会元气满满哦！"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不管怎么说我的蛋包饭里可是放满了肉和起司哦！"

    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这确实很好，但注意不要放多了。上次那个实在是对肠胃不太友好。"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇，明明只是忍，对饭居然这么挑剔！上次做的味道有那么重吗？"
    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊～也许是和超高校级的料理笨蛋一起待时间太久我也被传染了。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_BEF582EB5C1541099B31FB6D3CD3509F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "什么意思，把错误推给别人。"

    window hide

    pause 0.4

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_28CB16F81175458EA97C8F0250448304 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.5

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……哈，太好了。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "什么事？"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没什么～♪比起这个，\n快点回家，快点吃饭，吃完后变得{color=#FFFF00}元气满满{/color}哦！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "（最近经常听到这句话不过，是不是真的很在意呐。）"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 2

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 4

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_59836EDB597846F2A2C0A683B909166F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    pause 0.6

    window show

    rs_character_DF76892CB0F4478E80A8BB97882BE917 "好，今天的练习就到此为止。面向前，行礼！……互相行礼！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=28}多谢指教！！{/size}"

    window hide

    pause 0.6

    show rs_image_4A952CA4817E4CAF8759947AF056AFFB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_68B33F61F67D45A5900AAF8747F25ACA as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_E683F1ECE3314055A6535AFF3A0F039A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    window show

    if sys_music_current_file != "sound/BGM/Afternoon.ogg":
        play music "sound/BGM/Afternoon.ogg" loop
        $ sys_music_current_file = "sound/BGM/Afternoon.ogg"

    rs_character_D34F60C882F0425E93252349E8C3BC8D "前辈，今天也辛苦了！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，你也辛苦了。"

    show rs_image_1094C02923E34A60B4DCA6F851A39FB0 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "前辈，今天发生什么好事了嘛？"

    show rs_image_2D2761902CAE44EC807DF631A55BE304 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸，为什么这么问？"

    show rs_image_FB35B45BE8F34C718941BDF10B1073A6 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "啊，这个……昨天前辈好像在为什么很苦恼的样子，\n今天就没有这个感觉了……"

    show rs_image_4A9AC5BBBA6D44F5B5DCB7EEF0B9EAB6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "是嘛，昨天稍微发生了点事。\n"
    show rs_image_E683F1ECE3314055A6535AFF3A0F039A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "已经被朋友鼓励过所以没关系了。"

    show rs_image_68B33F61F67D45A5900AAF8747F25ACA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D34F60C882F0425E93252349E8C3BC8D "是这样啊。那真是太好了。前辈真的有一个很好的朋友呢。"

    show rs_image_1382C936693A4354B456F9C02B592547 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸。{w=0.5}{nw}"
    show rs_image_FB35B45BE8F34C718941BDF10B1073A6 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_EB543C918F764BD48AF5945B5D7C3278 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "啊，哈哈，是朋友……也许。"

    show rs_image_8CBDCCA85F2D41C69D53D9882E8E8DE3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D34F60C882F0425E93252349E8C3BC8D "我要是也能和那家伙成为这样的朋友就好了……"

    show rs_image_AB838172A2DB46ABA7F4AC2B3C09693D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那家伙是，中山君？"

    show rs_image_7AA4ECED07D244169095125FC38A41CA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "是的。果然和那种来路不明的人一起\n很令人担心。"

    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "不过，就算这么说，我也并没从听说过什么，\n当事人也什么都没说，是不是有些过分干涉了……"

    show rs_image_57981D44BEC64E6E999A769D75A0EC1A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "原来如此。嗯……\n"
    show rs_image_EB543C918F764BD48AF5945B5D7C3278 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "既然如此，稍微去看看样子如何。"

    show rs_image_FB35B45BE8F34C718941BDF10B1073A6 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "欸，可以吗？"

    show rs_image_ECD1914DBFDB442F9D1A9232EEEC99F6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，反正也只是从远处看看以期安心。而且我也有些在意他的情况。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_D1F333EE573A4AE8B656140B08D6CC17 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "前辈……被中山那么无礼地对待还这么热心……"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1382C936693A4354B456F9C02B592547 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_19EA6CF277DB411DAAFC4FAD639EE7DA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "我，包括那一点在内，最喜欢前辈了！！"

    show rs_image_AA6ADB52F38D4A07AB46270DE3FB9136 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "谢、谢谢。"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_B1B2F785D2ED49CF8DA090E58CB79206 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "啊……抱歉！一下子说多了……"

    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "那、那中山在排球部的社团活动应该也结束了，去看看！"

    window hide

    pause 0.8

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A766AF19B9F64CF2A2BFF7735ACB6A29 as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_FB8046DBE16F4BA8BE96613E8F3A850C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1

    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F7B4BBF8CE1F42548986125166418110 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_7D2835EC10DE4438B9BBE9F8CE5454F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    pause 0.4

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if sys_music_current_file != "sound/BGM/Strange idea.ogg":
        play music "sound/BGM/Strange idea.ogg" loop
        $ sys_music_current_file = "sound/BGM/Strange idea.ogg"

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "没想到我会有跟踪别人的一天。"

    rs_character_D34F60C882F0425E93252349E8C3BC8D "哈哈，真奇怪。这次为了不被发现要多加注意。"

    show rs_image_5D3A0AF418B44317B24FC87798F86D15 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "话说回来，之前真的遇见的时候很惊人，\n也只有在那种场合才会有那种展开了。"

    show rs_image_7AA4ECED07D244169095125FC38A41CA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "我也这么觉得。那家伙对那一种好像并不是不行……"

    show rs_image_2D2761902CAE44EC807DF631A55BE304 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那一种？"

    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "那家伙之前也有交往过的人，但很快就分手了，"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "而且是男人……"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_7D2835EC10DE4438B9BBE9F8CE5454F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嘛……毕竟是御咲学园。"

    show rs_image_FB35B45BE8F34C718941BDF10B1073A6 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "不过对方好像是比较强硬的类型，结果也没能好好处理后续。"

    show rs_image_AB838172A2DB46ABA7F4AC2B3C09693D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "既然本来就不合适的话，为什么还会开始交往？"

    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "谁知道……也许是气氛。我也不是很明白……"

    show rs_image_58CAC53C853A4ECC97CAB3038D1CAAF0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "气氛……"

    show rs_image_7AA4ECED07D244169095125FC38A41CA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "所以我觉得这次可能也会那样，关于那个男人我们什么都不知道……"

    show rs_image_57981D44BEC64E6E999A769D75A0EC1A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "是……如果真的发生了什么，就必须去帮忙。"

    show rs_image_DD2521E5C93C4C7A9DD6C7B09A64AD4B as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "正是。我也会在力所能及的范围内援助的。"

    window hide

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 1.5

    if sys_music2_current_file != "sound/Effect Sound/Night insect 1.ogg":
        play music2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B963C3D0E0E24FB59197E3C91C7EFFBD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_5D3A0AF418B44317B24FC87798F86D15 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    window show

    rs_character_D34F60C882F0425E93252349E8C3BC8D "太阳落山很久了。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "即便如此还走到这种几乎没人的地方来，真的没事么……"

    show rs_image_FB35B45BE8F34C718941BDF10B1073A6 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D34F60C882F0425E93252349E8C3BC8D "……？"
    extend "那边，是不是有什么？"

    show rs_image_1F55CB120A6948E28641DFC1C52982EE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "太暗了看不到……"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_E0106261369045C782EB83331069C3DE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "嗯？"

    show rs_image_B1B2F785D2ED49CF8DA090E58CB79206 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "啊？！中、中山被压到墙上了！难、难道是被强硬地……！"

    show rs_image_B5F32270AAE048CBBB7C1FB4F6FD6163 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "快走！！"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    window show

    rs_character_D34F60C882F0425E93252349E8C3BC8D "你想干什么！？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "欸、不、不好！被看到了！！"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "！！？"
    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "会、会被请去喝茶的……！！{w}\n{size=28}呜哇啊啊啊啊啊！！！{/size}"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    rs_character_D34F60C882F0425E93252349E8C3BC8D "前、前辈！危险！！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "！？"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Hit 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 3.ogg"

    # Gallery unlock: images/CG/Legacy-of-asynchronized-myself/Legacy-of-asynchronized-myself 3.png
    $ zorder_rs_image_AD7961BC76E643599E9C50754D2B16E3 = -100
    show rs_image_AD7961BC76E643599E9C50754D2B16E3 as rs_image_AD7961BC76E643599E9C50754D2B16E3 zorder zorder_rs_image_AD7961BC76E643599E9C50754D2B16E3 onlayer master
    hide rs_image_AD7961BC76E643599E9C50754D2B16E3

    show rs_image_AD7961BC76E643599E9C50754D2B16E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_3B6B863A23084F9EA6BFCF3703A3D9F7

    pause 1

    window show

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "唔……！！"

    window hide

    pause 0.4

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_3B6B863A23084F9EA6BFCF3703A3D9F7

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_20B77D172B0E46CF9955CA6BAE50636F as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_B963C3D0E0E24FB59197E3C91C7EFFBD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_8C818451D3534586ADE16DBAE08932F5

    window show

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "大、大叔！！醒醒！？呐！呐！！"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "唔、唔……"

    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_7AA4ECED07D244169095125FC38A41CA as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_32E3E577F0D64693B68294C651781F30 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊……抱、抱歉，一下子就……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    show rs_image_35899B38CB87497A86C6FFE9A60CEA05 as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "你们想干什么！？我们只是……"

    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_8CBDCCA85F2D41C69D53D9882E8E8DE3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at center_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_35899B38CB87497A86C6FFE9A60CEA05 as tag_2F2406ABFD334A9FAFFFD526F608E209 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_32E3E577F0D64693B68294C651781F30 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D34F60C882F0425E93252349E8C3BC8D "抱、抱歉。我只是有些担心你的……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "不用你多管闲事！把大叔弄成这个样子你们想怎么负责！？"

    show rs_image_155C01800ABF4AB78A6214D96342C6E2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "紧要关头避开了要害，应该没有受伤……"

    show rs_image_A766AF19B9F64CF2A2BFF7735ACB6A29 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_6581541AC4C34DE4AD8AE0D6865112C1 as tag_2F2406ABFD334A9FAFFFD526F608E209 at left_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_32E3E577F0D64693B68294C651781F30 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "不愧是，绫濑前辈早就习惯随便打人了呐～"

    show rs_image_0E30439FD01144B48C7028B0B281B659 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊……"

    show rs_image_51752209FD9740FAB88518A45B39FA1D as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "所谓的能不靠暴力解决问题真是太好了，\n避开要害就能被原谅了是不是。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_B1B2F785D2ED49CF8DA090E58CB79206 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at center_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_51752209FD9740FAB88518A45B39FA1D as tag_2F2406ABFD334A9FAFFFD526F608E209 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_0E30439FD01144B48C7028B0B281B659 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "前辈才不是那种人……"

    show rs_image_A766AF19B9F64CF2A2BFF7735ACB6A29 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "就因为是那种人，才会这么做。正因为是那种人，才会有暴力的传闻。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……对不起。"

    show rs_image_8CBDCCA85F2D41C69D53D9882E8E8DE3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D34F60C882F0425E93252349E8C3BC8D "抱歉……要怪也要怪我一开始拉前辈来，所以……"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_35899B38CB87497A86C6FFE9A60CEA05 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "那种东西怎么样都无所谓！！前辈打了人是事实！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……。"

    show rs_image_51752209FD9740FAB88518A45B39FA1D as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "好了快离开，不要再干涉我们了，剩下的我会处理。"

    show rs_image_32E3E577F0D64693B68294C651781F30 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "抱歉……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "还嫌不够烦是不是，快给我走！！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……。"

    window hide

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 3

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D9702ABDB70E4886A88A4038D68B5421 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 3

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Knock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Knock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Knock 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_58A5F7E4F23F45FD8D87DBE5F9130E01 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    show rs_image_58A5F7E4F23F45FD8D87DBE5F9130E01 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.8

    if sys_music_current_file != "sound/BGM/Guitar 1.ogg":
        play music "sound/BGM/Guitar 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Guitar 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.5

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍～好呀，睡了吗……？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍的妈妈说你今天好像不太高兴，所以我来看看情况……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯……没关系。没关系所以……让我一个人静一会……"

    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔，可是……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这次有点……友理解不了的……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是嘛……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，比较难以说明。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "难以说明……"
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "学习上的事情？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    show rs_image_066E0E2B85BF4A8B8B324005BCAAA80F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那是……社团？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍，我确实是笨蛋，可我一直和忍在一起，我想做些什么……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_32E3E577F0D64693B68294C651781F30 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "武道的真理……{w}和友完全无关的事情。所以，抱歉，这次就让我一个人想想。"

    show rs_image_5973F559935642A084B30B2B0A60FDF6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我明白了……晚安。"

    show rs_image_155C01800ABF4AB78A6214D96342C6E2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "晚安……"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    show rs_image_0E30439FD01144B48C7028B0B281B659 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1.6

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_DCEBC7527B8F4B4EA0FF44E692174034

    pause 2.5

    if sys_music2_current_file != "sound/Effect Sound/Swallow 1.ogg":
        play music2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 2

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.4

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_5EEBBCC1A1DD424FA293CA4EA0C6C4C6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "绫濑，为何要叹气，怎么了？"

    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊，不……只是发生了一些事而已。"

    show rs_image_D81691F1A7F841C4BE6CB3D91B4665C7 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "和社团有关的？"

    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "算是……你们怎么样？最近。"

    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这边没什么变化，空经常在外面玩，令人非常寂寞……"

    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "说起来，最近你们都不一起回家了。"

    show rs_image_26E8E308C5D84ECE97F965170D14D1FD as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "正是如此……{w}{w=0.35}{nw}"
    show rs_image_12471979B7D1437085FB86AB6EEB1E51 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "对了，绫濑，\n今天回去的时候一起去之前那个{color=#008080}寿司屋{/color}如何？"

    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，好。吃点好吃的东西说不定也能轻松一些。"

    show rs_image_8F3888CA89DF4DDEB58EC097C79B8FC0 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "好，今天也让我露一手帮帮忙。"

    show rs_image_541BC7417880499BB6151B8C86902E0A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "是呐，那边的情况真的{color=#008080}会露{/color}。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_6F1116E943E349E6A0DE125A5D33B038 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊～想到这么有趣的事，心情也好了不少。"

    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那就好。"

    window hide

    pause 0.7

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_DCEBC7527B8F4B4EA0FF44E692174034

    pause 3

    if sys_music2_current_file != "sound/Effect Sound/Night insect 1.ogg":
        play music2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_53C43FF5997344BAAADBDF967F5E5DBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 3

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if sys_music_current_file != "sound/BGM/Guitar 2.ogg":
        play music "sound/BGM/Guitar 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Guitar 2.ogg"

    # Gallery unlock: images/CG/Legacy-of-asynchronized-myself/Legacy-of-asynchronized-myself 4.png
    $ zorder_rs_image_B254F70E32264E79AF406C3492347538 = -100
    show rs_image_B254F70E32264E79AF406C3492347538 as rs_image_B254F70E32264E79AF406C3492347538 zorder zorder_rs_image_B254F70E32264E79AF406C3492347538 onlayer master
    hide rs_image_B254F70E32264E79AF406C3492347538

    show rs_image_B254F70E32264E79AF406C3492347538 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 1

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "原来如此，这可真是。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "感觉对自己一直以来坚持的事都没有信心了。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "练习并不是为了伤害别人，但不得不伤害到别人的情况也一定存在……"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯。……说起来，{color=#00FFFF}那时候{/color}也是。\n"
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    extend "刚入学时绫濑被不良少年围住……"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    show rs_image_3674A801C36945ADAA1FD191FE78406B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我刚巧路过，要上去帮忙的瞬间，周边的一群不良少年就全都被打飞了。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我没能反应过来发生了什么，只能呆然站立。"

    pause 0.4

    # Gallery unlock: images/CG/Legacy-of-asynchronized-myself/Legacy-of-asynchronized-myself 4.png
    $ zorder_rs_image_B254F70E32264E79AF406C3492347538 = -100
    show rs_image_B254F70E32264E79AF406C3492347538 as rs_image_B254F70E32264E79AF406C3492347538 zorder zorder_rs_image_B254F70E32264E79AF406C3492347538 onlayer master
    hide rs_image_B254F70E32264E79AF406C3492347538

    show rs_image_B254F70E32264E79AF406C3492347538 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 0.4

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那件事已经变成了传闻，连高等部的前辈们也不敢小看了。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那个时候如果不那么做，现在就会受困于他们。不论如何，那都是正当防卫。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "也许。那再怎么说也是我先发动的攻击，或许当时有其他方法也说不定。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "因为已经过去了才能这么想。实际上当场是很难想到的。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯……如果仅仅因为结果好就一切安好，这有些无法接受。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那直白了说就是担心结果可能并不会那么好？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "诶？"

    show rs_image_52820B68402A48B88D6C1517EC79E403 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "对于绫濑来说，\n这是为了保护自己，或者后辈的朋友采取的行动，并且成功了。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "至今为止，因为这些结果才构成了自己的自信。"

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_014C49487C644BFD95C49FCA0B26030E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_7F6C95985A7641738465E73831D557C2

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "但是，同时也对这样的行动所带来的对前辈或者跟踪狂的伤害无法释怀。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "所以，绫濑才无法接受。{w}\n特别是像这次这样把所有矛盾示诸表面的事情，呐。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊……"

    window hide

    pause 0.4

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    # Gallery unlock: images/CG/Legacy-of-asynchronized-myself/Legacy-of-asynchronized-myself 4.png
    $ zorder_rs_image_B254F70E32264E79AF406C3492347538 = -100
    show rs_image_B254F70E32264E79AF406C3492347538 as rs_image_B254F70E32264E79AF406C3492347538 zorder zorder_rs_image_B254F70E32264E79AF406C3492347538 onlayer master
    hide rs_image_B254F70E32264E79AF406C3492347538

    show rs_image_B254F70E32264E79AF406C3492347538 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 0.4

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "可是，这并不是说绫濑就应该毫无抵抗，对后辈的朋友不管不问。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯……如果能在保护什么的时候不会伤害到对方，真的有这样的方法就好了。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "困难的质问呢。绫濑从外表看不出的实力，那部分相对的心思非常细腻。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "月因为过于强大，本身连行使力量的必要都没有，还真是羡慕。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这种体格也并不能改变。\n和月谈过后，或许该整理一下心情了。{w}{w=0.3}{nw}"
    # Gallery unlock: images/CG/Legacy-of-asynchronized-myself/Legacy-of-asynchronized-myself 4-1.png
    $ zorder_rs_image_8C10B311F1B241F380A70CA461F73E5E = -100
    show rs_image_8C10B311F1B241F380A70CA461F73E5E as rs_image_8C10B311F1B241F380A70CA461F73E5E zorder zorder_rs_image_8C10B311F1B241F380A70CA461F73E5E onlayer master
    hide rs_image_8C10B311F1B241F380A70CA461F73E5E

    show rs_image_8C10B311F1B241F380A70CA461F73E5E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.3

    extend "谢谢。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "武道终究不是用来伤害别人的，而是用来磨砺自己的。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "作为站在同样道路上的同伴，我对这件事也很有兴趣。\n能帮上绫濑的忙真是太好了。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不过，时机真是巧，今天能和月这样谈心。"

    window hide

    pause 0.5

    show rs_image_53C43FF5997344BAAADBDF967F5E5DBE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 0.5

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……绫濑真是有一个令人羡慕的朋友呐。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哇，真难得，月会自己表扬自己。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "哈哈，这么理解了啊。\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "算了，那么，该正经吃饭了！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "好！"

    window hide

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 1.3

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    window show

    rs_character_2F154AE49ED54A70AEA327A36C670DDB "{color=#FF00FF}久等了！！金枪鱼上楠、金枪鱼中楠、炙烧、赤身的金枪鱼三味！！！{/color}"

    window hide

    pause 0.8

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_51B8A209554F4DA4B049529627B22211

    pause 3

    if sys_music2_current_file != "sound/Effect Sound/Swallow 1.ogg":
        play music2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 1.4

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1.2

    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊……"

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    show rs_image_1094C02923E34A60B4DCA6F851A39FB0 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_A766AF19B9F64CF2A2BFF7735ACB6A29 as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_D34F60C882F0425E93252349E8C3BC8D "绫濑前辈，早上好！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_6581541AC4C34DE4AD8AE0D6865112C1 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "早上好哦前辈！前几天真是承蒙照顾了呐☆"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你、你们好……{w}中山君是要参加排球部的晨练吗？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_52F632A326A24F87B73C4565A9760408 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "就是啊！空手道部也有晨练真是很辛苦呐～都快觉得不想做了呐～"

    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"
    show rs_image_5EEBBCC1A1DD424FA293CA4EA0C6C4C6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "那个，中山君，前几天真的很抱歉。\n那个是……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_A766AF19B9F64CF2A2BFF7735ACB6A29 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "嗯？为什么要道歉？"

    show rs_image_CA32B3074CBF4DB08BA59AE12141A4F7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸？要说为什么……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    show rs_image_548B0025EC14496F9D55EDBD556F4843 as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "说起来，前辈认识吗？一个金色头发的人，已经被他好好道过歉了。"

    show rs_image_0123524CA5E24154A0F3510F5C639B95 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "但完全听不明白想说什么，不愉快～"

    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "金发的认识的人？不，与其说，可是，之前……"

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    show rs_image_52F632A326A24F87B73C4565A9760408 as tag_2F2406ABFD334A9FAFFFD526F608E209 at left_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "啊，说起之前来！那之后可发生大事了呐～！"

    window hide

    pause 0.6

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 0.5

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    show rs_image_23E95FF3D12540FB88BD74983BE7800E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B963C3D0E0E24FB59197E3C91C7EFFBD as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_20B77D172B0E46CF9955CA6BAE50636F as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    if sys_music2_current_file != "sound/Effect Sound/Night insect 1.ogg":
        play music2 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Night insect 1.ogg"

    pause 0.5

    window show

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "大叔！振作点！！"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "唔……嗯？"

    show rs_image_BACDF64086FF46D591FBC9644AD521FA as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "大叔！醒过来了？还好！？"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "啊……？这、这里是？"

    show rs_image_51752209FD9740FAB88518A45B39FA1D as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "大叔被打了一拳昏过去了！"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "啊……啊……不、不过没关系！！\n"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "我可是M！没、没用的！"

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_51752209FD9740FAB88518A45B39FA1D as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "比起这个来，我被你的温柔感动了！竟然会这么担心我……！！"

    show rs_image_548B0025EC14496F9D55EDBD556F4843 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "因、因为我的东西要是坏了也很气人，坏不坏应该是我来决定……"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "唔！！！我到底修到过什么善果啊！！感激涕零！我发誓一生都会忠诚的！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_0123524CA5E24154A0F3510F5C639B95 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "那、那是当然的！再说了，那个是我而不是大叔决定的。"

    rs_character_865F3F8F53BC4C8AAE6E947130135E5A "失礼了！！不～请打我！被打会很激动的！哈——！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "谁允许你摸我的！？等……大叔！{w=0.55}{color=#FF00FF}啊……{/color}"

    window hide

    pause 0.8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 1.2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_A38C03DA935A42178D4F23B0FCF60FF3 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_548B0025EC14496F9D55EDBD556F4843 as tag_2F2406ABFD334A9FAFFFD526F608E209 at center_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 0.7

    if sys_music_current_file != "sound/BGM/The hope.ogg":
        play music "sound/BGM/The hope.ogg" loop
        $ sys_music_current_file = "sound/BGM/The hope.ogg"

    window show

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "奴隶的状态好过头了，后来可相当麻烦呐……\n真是的，连自己的地位都认不清！"

    show rs_image_51752209FD9740FAB88518A45B39FA1D as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "所以前辈没有需要道歉的理由哦～"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊……是这样。那个……总之，中山君请和那个人幸福。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_20B77D172B0E46CF9955CA6BAE50636F as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "唔——等等！请不要误会！那只是奴隶！不是那个意思！"

    show rs_image_1094C02923E34A60B4DCA6F851A39FB0 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "中山这家伙一直都毫不留情面的东西东西地叫，\n不过在一些奇怪的地方还是很率直的……"

    show rs_image_0123524CA5E24154A0F3510F5C639B95 as tag_2F2406ABFD334A9FAFFFD526F608E209 zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "再说了，我可是真心觉得那就是个奴隶的！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……呐，那个金发的认识的人……"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    show rs_image_B1B2F785D2ED49CF8DA090E58CB79206 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "啊……抱歉，说起必须，我也有要道歉的事。"

    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不，那个就算了……"

    show rs_image_7AA4ECED07D244169095125FC38A41CA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D34F60C882F0425E93252349E8C3BC8D "前辈，这几天真的太麻烦您了。很抱歉把前辈卷入这些事情里。"

    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不，我也想明白了一些事，这也算是个很好的机会了。所以，不需要道歉。"

    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "作为守护某些人的一方，我很在意自己会伤害到其他人想要保护的人。"

    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这只是因为我的思想还不成熟。解决方法还需在练习中慢慢摸索。"

    show rs_image_DD2521E5C93C4C7A9DD6C7B09A64AD4B as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D34F60C882F0425E93252349E8C3BC8D "……！"
    show rs_image_98DDCAE3975441ECB139AB353E188706 as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "前辈这种能冷静分析自己的弱点，\n然后再找出解决方法的前进的步伐{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_19EA6CF277DB411DAAFC4FAD639EE7DA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "真是太棒了！"

    show rs_image_68B33F61F67D45A5900AAF8747F25ACA as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D34F60C882F0425E93252349E8C3BC8D "这并不是那个跟踪狂先生的台词，但我也会发誓一生追随前辈的！！"

    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    show rs_image_0123524CA5E24154A0F3510F5C639B95 as tag_2F2406ABFD334A9FAFFFD526F608E209 at left_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "呐～清酱还没好吗？？我要先走了哦！"

    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_B1B2F785D2ED49CF8DA090E58CB79206 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at left_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "哦、哦！"
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    $ zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 = 300
    show rs_image_1094C02923E34A60B4DCA6F851A39FB0 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at right_top zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    show rs_image_6581541AC4C34DE4AD8AE0D6865112C1 as tag_2F2406ABFD334A9FAFFFD526F608E209 at left_top zorder zorder_tag_2F2406ABFD334A9FAFFFD526F608E209 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.5

    extend "那个……失礼了，前辈！\n等下晨练时再见！"

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "拜拜☆"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.9

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……{w}金发的认识的人{w=0.5}……吗。"

    window hide

    pause 1

    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 2

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 1

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_C989D2B8472147EBAAC08D14FF060BEC as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "忍君，早上好～"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_D81691F1A7F841C4BE6CB3D91B4665C7 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "早上好，绫濑。"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好哦～！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "早上好。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊……忍，早上好～……"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸欸，为什么！为什么只无视我……？？"

    window hide

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    # Gallery unlock: images/CG/Legacy-of-asynchronized-myself/Legacy-of-asynchronized-myself 5.png
    $ zorder_rs_image_6074209F6E654F3580E90BD8FE1A21C8 = -100
    show rs_image_6074209F6E654F3580E90BD8FE1A21C8 as rs_image_6074209F6E654F3580E90BD8FE1A21C8 zorder zorder_rs_image_6074209F6E654F3580E90BD8FE1A21C8 onlayer master
    hide rs_image_6074209F6E654F3580E90BD8FE1A21C8

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_6074209F6E654F3580E90BD8FE1A21C8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_09527D61D3AC4B06AC9CB5A39F0A0855

    pause 1

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "早上好，友。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈……？诶？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦——！一大早眼福眼福♪"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不愧是青梅竹马，打招呼都那么英国风呐～"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "唔唔！空，我们也不能输，赤峰家以后也要这样！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "No thank you。我们家是纯正的和风。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "唔……哥哥最近很难受的，空……"

    pause 0.6

    # Gallery unlock: images/CG/Legacy-of-asynchronized-myself/Legacy-of-asynchronized-myself 5-1.png
    $ zorder_rs_image_2D24925D8776427E806125699BD065DE = -100
    show rs_image_2D24925D8776427E806125699BD065DE as rs_image_2D24925D8776427E806125699BD065DE zorder zorder_rs_image_2D24925D8776427E806125699BD065DE onlayer master
    hide rs_image_2D24925D8776427E806125699BD065DE

    show rs_image_2D24925D8776427E806125699BD065DE as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "各种意义上，谢谢了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔呼呼！不客气。"

    window hide

    pause 1.5

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_B458977B6F2E4C8ABD6196FDA6E1C3C8

    pause 3

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F95856ACBC5A49B2B61D4DBB1E7B4294 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    if sys_music_current_file != "sound/BGM/Afternoon.ogg":
        play music "sound/BGM/Afternoon.ogg" loop
        $ sys_music_current_file = "sound/BGM/Afternoon.ogg"

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.4

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "（不战而屈人之兵的方法……也不是避开要害就行……）"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "（……总之先回家吧。）"

    window hide

    pause 0.8

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1


    if judge_lm_condition([]):
        jump block_00003FD9

    return

label block_00003FD9:
    # Node: 00003FD9 (CP3 Twilight Misaki 忍)
    call block_00001BFD from _call_block_00001BFD

    if judge_lm_condition([]):
        jump block_000041D0

    return

label block_000041D0:
    # Node: 000041D0 (異我戦記 3)
    $ set_window("イベントモード")
    pause 1

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    stop music fadeout 2
    $ sys_music_current_file = ""

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7B49313C1C0A4D8E8C250CC79F444E2D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.4

    if sys_music_current_file != "sound/BGM/Something strange 1.ogg":
        play music "sound/BGM/Something strange 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something strange 1.ogg"

    window show

    rs_character_EFAEA045306D442E91F2D2673F9A7598 "哦，那边那个小个子兄弟！来和我们说说话不～？"

    rs_character_465092F46302440596C3A08B731FB883 "其实啊，我们现在缺钱，手头不怎么宽裕呐。\n你那个制服是御咲学园的，是私立学校的小少爷咯？"

    rs_character_F900916318564E31BA1CEC6F06D32E57 "所以说～稍——微借点儿钱花怎么样？稍——微给点就行！"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "（又是这个……还没想出什么方法，\n就算是这些人受伤后也是会有因此悲伤的人。）"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_EFAEA045306D442E91F2D2673F9A7598 "拜托你了～啊？"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_465092F46302440596C3A08B731FB883 "话说，你明明看着是个男孩子，长得还挺可爱呐～"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_F900916318564E31BA1CEC6F06D32E57 "像某电视剧一样男装上学？真是的话陪我们喝个茶怎么样～"

    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "喝茶的钱还是有的……啊，顺便，我确实是男生。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_F900916318564E31BA1CEC6F06D32E57 "真的～？算了，反正你挺可爱的，怎么都行了。{w}\n借钱和喝茶，你选？"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哇——请停手——救救我。"

    rs_character_465092F46302440596C3A08B731FB883 "乱叫喊什么？不想受苦的话好好回答。"

    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这是我的台词。受伤的话家里的妈妈可是会担心的。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_EFAEA045306D442E91F2D2673F9A7598 "混蛋，不吃点苦头不知道是不……"

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.6

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "（……只能上了。）"

    window hide

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_59FECE64AFAC4F92A18E4C5924F90E4F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A3455294BD06448697B172E9BDA4243D

    pause 1

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg"

    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_EFAEA045306D442E91F2D2673F9A7598 "疼……疼疼疼！？"

    rs_character_9EDF48057FB84D428D56198A69E2880E "真是的，不可以对少年出手哦～我也是一直在忍耐呐～"

    window hide

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    # Gallery unlock: images/CG/Legacy-of-asynchronized-myself/Legacy-of-asynchronized-myself 6.png
    $ zorder_rs_image_0BF98EB1ECCB4B0E884CBC033AC9F50E = -100
    show rs_image_0BF98EB1ECCB4B0E884CBC033AC9F50E as rs_image_0BF98EB1ECCB4B0E884CBC033AC9F50E zorder zorder_rs_image_0BF98EB1ECCB4B0E884CBC033AC9F50E onlayer master
    hide rs_image_0BF98EB1ECCB4B0E884CBC033AC9F50E

    show rs_image_0BF98EB1ECCB4B0E884CBC033AC9F50E as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    pause 0.8

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你、你是……"

    rs_character_9EDF48057FB84D428D56198A69E2880E "还好不？少年们腻腻歪歪的样子确实很饱眼福不过～"

    rs_character_EFAEA045306D442E91F2D2673F9A7598 "疼疼！！认输！认输！！"

    rs_character_465092F46302440596C3A08B731FB883 "什么人啊这个大叔！？"

    rs_character_F900916318564E31BA1CEC6F06D32E57 "一边去混蛋老头！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "我才25！对一个正当青年的人用那种称呼岂不是很失礼吗！？"

    rs_character_465092F46302440596C3A08B731FB883 "吃下这一击！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_4D8F1D6A70C24A34A3E6C37B69619470 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_9EDF48057FB84D428D56198A69E2880E "吼——！"

    rs_character_465092F46302440596C3A08B731FB883 "唔！？"

    rs_character_F900916318564E31BA1CEC6F06D32E57 "有破绽！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_51451FBF94C8444AA5696178E72CE210 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_9EDF48057FB84D428D56198A69E2880E "图样！！"

    rs_character_F900916318564E31BA1CEC6F06D32E57 "唔……"

    window hide

    pause 0.4

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB = 200
    show rs_image_7B49313C1C0A4D8E8C250CC79F444E2D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_4692ED5E5B26488589FEF7BB7C852930 as tag_135F5559064C4A88B1AD47AAB0AE18BB at center_top zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.7

    window show

    rs_character_9EDF48057FB84D428D56198A69E2880E "玩玩的话我是挺高兴的，玩过火可就会肌肉疼了。"

    show rs_image_98CFF5BD14C64F1DB96BAB3E3168E810 as tag_135F5559064C4A88B1AD47AAB0AE18BB zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "基本上都是顺着你们的体势来的，应该不会受伤的～"

    hide tag_135F5559064C4A88B1AD47AAB0AE18BB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFAEA045306D442E91F2D2673F9A7598 "可恶！莫名其妙的老头！！给我记住！！"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_465092F46302440596C3A08B731FB883 "笨蛋笨蛋！！大叔！！"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_F900916318564E31BA1CEC6F06D32E57 "老龄臭！！"

    window hide

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dash 1.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    $ zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB = 300
    show rs_image_4692ED5E5B26488589FEF7BB7C852930 as tag_135F5559064C4A88B1AD47AAB0AE18BB at right_top zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_9EDF48057FB84D428D56198A69E2880E "嗯——被迫屈服的青少年流着眼泪说着强硬的台词……不错不错♪♪"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_CA32B3074CBF4DB08BA59AE12141A4F7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……那个，非常感谢救了我。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_98CFF5BD14C64F1DB96BAB3E3168E810 as tag_135F5559064C4A88B1AD47AAB0AE18BB zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "很好！少年的幸福就是我的幸福！\n视线总是下意识跟随少年的习惯能派上用场真是太好了。"

    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……{w=0.4}好像很强的样子，请问是对武道有兴趣吗？"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3AD096BAE82A4EF8833A719597517605 as tag_135F5559064C4A88B1AD47AAB0AE18BB zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "啊、啊～嗯，{w=0.45}学过{color=#00FFFF}合气道{/color}，一种从柔术派生出来的新的武道。"

    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……大哥。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_FC95DD3798C64A10A0E54539AB0D93E2 as tag_135F5559064C4A88B1AD47AAB0AE18BB zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "大、大哥也太……啊哈哈♪♪"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    show rs_image_D37BD99933D640558EDE55BF285BD05F as tag_135F5559064C4A88B1AD47AAB0AE18BB zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_9EDF48057FB84D428D56198A69E2880E "对、对不起，怎么了？"

    pause 0.3

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_AFACE878401B4E26BE0872550A11D696 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.4

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我正在学习空手道，可是，如果要保护一个人，就必定会伤害到其他人。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "最近一直在烦恼这个……可是，看到大哥解决事件的方法后非常在意。"

    rs_character_9EDF48057FB84D428D56198A69E2880E "……这样吗。以柔克刚，试试也不错吧？{w}合气道。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "真想看看你穿道服的样子！真好啊，道服！\n火热的身体！涨红的面容！挥洒的汗水！裸露的胸前！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "……"

    hide tag_135F5559064C4A88B1AD47AAB0AE18BB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB = 300
    show rs_image_DF15114974EF49E58EECE21C61E86DE1 as tag_135F5559064C4A88B1AD47AAB0AE18BB at center_top zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "啊啊哦～{w=0.5}{nw}"
    show rs_image_D37BD99933D640558EDE55BF285BD05F as tag_135F5559064C4A88B1AD47AAB0AE18BB zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……说认真的，我很推荐。\n合气道的理念和你的理想更加接近。"

    rs_character_9EDF48057FB84D428D56198A69E2880E "但是，继续练习空手道也并无不可。{w}以刚制柔，双方都有各自的优点。"

    hide tag_135F5559064C4A88B1AD47AAB0AE18BB
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB = 300
    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_D37BD99933D640558EDE55BF285BD05F as tag_135F5559064C4A88B1AD47AAB0AE18BB at right_top zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "然后与自己的想法融合，最后融会贯通……{w}大哥平常练习的地方是？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3AD096BAE82A4EF8833A719597517605 as tag_135F5559064C4A88B1AD47AAB0AE18BB zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "哦，要来我家道场吗！？我很高兴呐～♪"

    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……{w=0.4}说起来，大哥，我们是不是见过？"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "为何要这么说？"

    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "只是觉得不是第一次见面……但想不起名字，抱歉。"

    show rs_image_FC95DD3798C64A10A0E54539AB0D93E2 as tag_135F5559064C4A88B1AD47AAB0AE18BB zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "嗯，确实我非常想和御咲学园的孩子们维持好关系不过，\n基本没什么机会，如果要说见面的话……"

    show rs_image_D37BD99933D640558EDE55BF285BD05F as tag_135F5559064C4A88B1AD47AAB0AE18BB zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "啊，你们的学园祭我去过了，是不是那时候……？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_98CFF5BD14C64F1DB96BAB3E3168E810 as tag_135F5559064C4A88B1AD47AAB0AE18BB zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "呀呀，这可能就是命运的相见。偶然遇到的两个人其实在前世是……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "作为同习武道的人，单纯波长比较接近罢了。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3AD096BAE82A4EF8833A719597517605 as tag_135F5559064C4A88B1AD47AAB0AE18BB zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "啊……嗯……是这样……"

    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "后请在道场多多指教了。我叫做绫濑忍，大哥呢？"

    hide tag_135F5559064C4A88B1AD47AAB0AE18BB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB = 200
    show rs_image_4692ED5E5B26488589FEF7BB7C852930 as tag_135F5559064C4A88B1AD47AAB0AE18BB at center_top zorder zorder_tag_135F5559064C4A88B1AD47AAB0AE18BB onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    rs_character_374BAB4922B14C9986D4B6FA70E4287A "我是{color=#FFFF00}诹访部翔平{/color}！{w=0.45}请多关照！"

    window hide

    pause 1

    stop music fadeout 3.5
    $ sys_music_current_file = ""

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_135F5559064C4A88B1AD47AAB0AE18BB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_B458977B6F2E4C8ABD6196FDA6E1C3C8

    pause 3.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_48D26C14A18B4805B108A02B239C32FF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_671363D9CAC84829ABC139CB758B363E

    pause 1

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    if sys_music_current_file != "sound/BGM/The past precious.ogg":
        play music "sound/BGM/The past precious.ogg" loop
        $ sys_music_current_file = "sound/BGM/The past precious.ogg"

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸～开始练习空手道以外的武道了啊，真是热心。"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "并不是因为失败而离开，只是因为想要更进一步。\n想到就要做，趁热打铁。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇，又在说难明白的话了～"

    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不过，我觉得确实应该见过。"

    show rs_image_3CCC6DE5C5ED405DB1BBB15ECA3CDD44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那个叫做诹访部的人？可是，他有25岁哦？\n那个人可能和忍有什么接点，啊？"

    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不明白。他好像去过我们的学园祭，也许是那时候残留的印象。"

    show rs_image_FF4A588462534B15B9D5F444704F26BB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸～在那种忙不过来的时候？一般早就忘了。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔唔……总～觉得很奇怪……忍～没背着我在暗地里做什么吧～？"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_F9B0C2D0E2D84D6D85BC37C697E5F928 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "笨蛋，我又不是友。"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜、呜。可是，我很担心啊。\n突然出现又那么厉害，不会是特地这么做的？"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊……那个人的目标涵盖范围非常广。"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_3F5AF2DAC6F94773B04A709D2558F647 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "看——！果然果然！！"

    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不过，没关系的。那么担心的话友也来不就好了？"

    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？合气道？"

    show rs_image_541BC7417880499BB6151B8C86902E0A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，也可以作为防身术，学了也不会有损失的。"

    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸～可是我怕痛……"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_6A862C1FCD4240298711F04F27EDD9E0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "说的也是呐。对友这样没毅力的太难了。"

    show rs_image_3F5AF2DAC6F94773B04A709D2558F647 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔！{w=0.5}{nw}"
    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……我会考虑一下的。"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这是绝对不会来的意思吧。\n"
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "说起来，不用准备晚饭吗？"

    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，已经这个时间了！不好不好。"

    show rs_image_0DCD6DA8D946484F9F316BDB90DB6D40 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那为了庆祝忍君踏上新的台阶，今天我就大展身手！友特制的蛋包饭！"

    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "又是这个。"
    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "不过，只要吃了就会{color=#FFFF00}元气满满{/color}，\n乘势如此也不错。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_27FF4633286B4DF59BF4C1A761DDF98E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦♪忍也喜欢上那段话了呐！\n"
    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……话说回来，忍也能好好做出料理就好了。"

    show rs_image_BEF582EB5C1541099B31FB6D3CD3509F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你说什么？"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么也没有哦！料理就由我来教，忍就教教我防身术！"

    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "好好，必须要保护好重中之重的友的身体呢。"

    show rs_image_2A528A20757145A78087B876421EFAF4 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就是！我们一起加油，忍！"

    window hide

    pause 1

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_51B8A209554F4DA4B049529627B22211

    call scb_flag_title_end(3, _("「异我战纪」")) from _call_scb_flag_title_end_18

    if judge_lm_condition([]):
        jump block_000041CE

    return

label block_000041CE:
    # Node: 000041CE (Phase: 0)
    $ C3S1Phase = 0
    if Chapter <> 3:
        $ del C3S1Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_000041DF
    if judge_lm_condition([]):
        jump block_000041D1

    return

label block_000041DF:
    # Node: 000041DF ()

    return

label block_000041D1:
    # Node: 000041D1 (FINISH)
    $ C3S1 = True
    $ TalkTsukiSoraF1After = True
    if ((C1SG2 == False) or (C2SG2 == False)) and (C3S2 == True) and (C3S3 == True):
        $ SYSBreakCurrentChapter = True

    if judge_lm_condition([]):
        jump block_000041DD

    return

label block_000041DD:
    # Node: 000041DD (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_22

    if judge_lm_condition([]):
        jump block_000041DE

    return

label block_000041DE:
    # Node: 000041DE (FLAG FINISH)
    $ set_window("(標準)")
    pause 1.5

    if sys_music2_current_file != "sound/BGM/Flag finished.ogg":
        play music2 "sound/BGM/Flag finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件{/color}{color=#008A45}“异我战记”{/color}{color=#0080FF}成功结束。』{/color}"

    window hide


    if judge_lm_condition([{ "scope": 0, "content": "VarExists(\"SYSBreakCurrentChapter\") == True" }]):
        jump block_000041DF
    if judge_lm_condition([]):
        jump block_000041E0

    return

label block_000041E0:
    # Node: 000041E0 (RESET)
    pause 4

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5


    if judge_lm_condition([]):
        jump block_000041DF

    return

