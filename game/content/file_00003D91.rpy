# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003D91 (FLAG: 集合-御咲花車祭)

label block_00003D92:
    # Node: 00003D92 ()

    if judge_lm_condition([]):
        jump block_00003D95

    return

label block_00003D95:
    # Node: 00003D95 (Phase: 99)
    if Not(VarExists("C3S3Phase")):
        $ C3S3Phase = 0
    $ C3S3Phase = 99

    if judge_lm_condition([]):
        jump block_00003D93

    return

label block_00003D93:
    # Node: 00003D93 (F3 START)
    call scb_flag_title(3, _("「集合！御咲花车祭」")) from _call_scb_flag_title_9

    if judge_lm_condition([]):
        jump block_00003D94

    return

label block_00003D94:
    # Node: 00003D94 (集合！御咲花車祭 1)
    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Swallow 1.ogg":
        play music2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E231059B50CB41C989713074B50A8CA5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_8EC5717E792241CB9E9610819A6E1D46

    pause 3

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    show rs_image_32E34DC6044942FDB2E664C9223A1A28 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_AC95315BDCC64DF3BEF960A040CBBAF4

    pause 1.3

    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "这下麻烦了，没想到会有这种事……"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "偏偏还在明天就要开始的这种时候……"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "这么下去{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#FF80C0}“御咲花车祭”{/color}就会……{w}\n有什么补救措施……"

    if sys_effect2_current_file != "sound/Effect Sound/Tick tock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}唔～嗯……{/size}"

    pause 0.7

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "大家久等了——！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=36}！！{/size}"

    window hide

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    # Gallery unlock: images/CG/Join-misaki-danjiri/Join-misaki-danjiri 1.png
    $ zorder_rs_image_7E57D7A3B6704964B8907157D0B72E75 = -100
    show rs_image_7E57D7A3B6704964B8907157D0B72E75 as rs_image_7E57D7A3B6704964B8907157D0B72E75 zorder zorder_rs_image_7E57D7A3B6704964B8907157D0B72E75 onlayer master
    hide rs_image_7E57D7A3B6704964B8907157D0B72E75

    show rs_image_7E57D7A3B6704964B8907157D0B72E75 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_266255D4821A4095BCA7860D44F0A511

    pause 1

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "试衣完成！怎样？我们阳光的样子！！"

    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "唔～果然还是有些羞耻……"

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "奥村，把空这种官能的样子暴露在外是很危险的。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "说什么呢！这可是{color=#FF80C0}“花车祭”{/color}的传统服装！\n那种擅自的想法，绝对不可能。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊，难道说，看到空的这个样子，月前面忍不住了？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "正如所言！！没法好好隐藏我也很困扰的！"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦哦♪别的孩子看到阿月的这个样子一定也会兴奋起来，\n连锁反应最后整个现场就会变成乱交Party呐！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不、不是很明白你们的意思……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "每年都这么合身呐！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "完全没有臭男人的感觉，简直就是艺术造型。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "能合法目睹这种姿态，简直就是转瞬的幸福……"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "最后那个很奇怪哦。"

    window hide

    pause 0.8

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_2EB4DEBFAA7D4D7FB0F8D20EF70EC6B4 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_58B37DE9B2B24E25A37C53248345E177 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_38E5FD9401554234979B7D2AF21E9AFA as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-90, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_74B3A688276A401A820C8D2C80E347EF

    pause 0.8

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "只有无趣的大人的话花朵会稍显不足的。"

    show rs_image_4292311494D4406AA0D609703C39F49C as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不要那么自卑嘛，冲着大叔们的衣装来的人不是也有很多嘛♪"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "哇哈哈哈，不愧是干营业的慎酱，嘴真甜。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "不过啊，一开始就那么点儿大的三人现在也长大了呢。"

    show rs_image_41C276D60DE54F71BFF69F4FA0E19CDA as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那时候还只是小学低学年而已。"

    show rs_image_BE3858715C4E440D80A379541F538131 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "认识奥村也是在那次祭典上。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "慎太郎君变化最大了呐，过去是那么的……"

    show rs_image_F5186167C2294ABAB47BD67D9904B105 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊哈～真是的～不要说了嘛～黑历史黑历史！请都忘掉。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "那时候也有很多孩子参加，场面很热闹……呢……"

    show rs_image_DDDE29C308C4473AA90F7632D5BC0D5B as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "发生什么了？"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "其实本来要参加的隔壁镇的儿童团体突然又联络说不来了……"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_93050D2F5F324CBF9845F575E5F67101 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "诶诶！！为什么为什么！？\n还觉得好不容易能亲眼目睹正太们圆滚滚的屁股来着！！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "我们也很期待啊……{w}咳咳，那边的家长团队来抱怨了。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "说是祭典的衣服太裸露，对孩子们影响不好……"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_4708238BC13D4887A03F5DD83E4C6AA7 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "实际上带着不纯目的的人也确实有……现在，就在这里。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9AA1F628998843DBBE8B6BA2427A099B as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "哈，到底怎么不好了！这种说法简直无理取闹！"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1F3AA5C8A5894654BD2457FA8C0BFCC1 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "就是就是！居然对如此古典而又阳光的装束横加指责，太不讲道理了！"

    show rs_image_9783CCC7591640848A343D1105399B1D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "你们两个请摸着自己的胸口重新审视一下自己的发言……"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "好不容易准备了这么多儿童用服装……"

    show rs_image_2AA914C13B304BEAA71FBC9C3CE8797D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "确实那太浪费了……"

    show rs_image_DDDE29C308C4473AA90F7632D5BC0D5B as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "说起来，为何要特地请临城的团队过来？"

    show rs_image_76882A91850246D0AEE0A23B0F069E2E as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_D86BD1DCBA2D43DEA3FFEC59D6AFB0BB as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "御咲花车祭是很多人都会来的热闹的节日……特别是，一部分人。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "咳咳！可也确实在年复一年地衰弱，现在已经到了或许不得不停下的情况。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "所以我们才会和临镇合作，希望能获得一些观光客源。"

    show rs_image_79C255A7A8234730BE4AD701D4E483DC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "是这样啊……我也一直在参加，一直很喜欢这个，不想突然消失。"

    show rs_image_87793ED3ABD64D14ADCFDF51E4B916B5 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "我也一样。传统不该断绝。\n{w=0.5}{nw}"
    show rs_image_E30D33E9CFEA46A0AEE5231544CE5769 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "对了，明天不是休息日，祭典是在放学时间。"

    show rs_image_45D38107B87742ADB49411D94E8B210D as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "看准那个时候，试着劝诱一些人参加祭典如何。"

    show rs_image_D79BFDF332C94759949D8F385F23F8A9 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "或许可行！本来花车祭就是要大家在一起才热闹的活动嘛。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_ECCF1A52B5B24205ABB5752C81AAD79D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "去和街上的年轻孩子们搭话，让他们穿上这套衣服，\n再邀请他们参加，这样的作战♪"

    show rs_image_4292311494D4406AA0D609703C39F49C as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我觉得也是个好方法！\n之前的全镇大会因为下雨被迫中止，奖品还剩下不少。"

    show rs_image_7B287CB40A5A40A78E97B3F56B002E48 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "处理起来也很麻烦，就用这些当礼物请他们参加如何？"

    show rs_image_21A22B1859AA4941B2C61DE287F5E553 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "是呐，有那种程度的报酬也会好很多。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "那么就拜托你们了。\n山车{size=12}{color=#C0C0C0}（祭典时那群人扛的那个）{/color}{/size}就交给我们，尽可能多找些能参加的孩子。"

    show rs_image_58B37DE9B2B24E25A37C53248345E177 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "我们明白了。{w}\n{nw}"
    show rs_image_EF1CA449D9DD4A1A81FB1168489462C4 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……今年本来也想坐山车的。"

    show rs_image_BE3858715C4E440D80A379541F538131 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "明年还有机会的。"

    show rs_image_ECCF1A52B5B24205ABB5752C81AAD79D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "对～对，就算为了那个我们也要努力！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "还能有这么愿意帮忙的孩子真是太好了……"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "这样以后的花车祭，或者说御咲市就高枕无忧了呢。"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_40BD583A95C74300ACB4618268AB48FF

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 = 200
    show rs_image_B7E2FD9714DF4EF0A712370A5AEFF12A as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 at center_top zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.4

    window show

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "看样子已经谈好了。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "翔银时先生！特意过来了吗！！"

    show rs_image_7197DF88471C4D66A7505D8DFC72D61F as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "嗯，想早一步看看慎太郎他们的阳光姿态。\n当天也会期待的，你们也要好好加油。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "是的！！我们明白了！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "不过翔银时先生的孙子今年不能参加还真是遗憾……"

    show rs_image_CC61CB4A283E4FCD8F2E04E37E005917 as tag_ACAAB0A43F254041BE2C5833D3FC0CE4 zorder zorder_tag_ACAAB0A43F254041BE2C5833D3FC0CE4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6E3CA81A269B47A3B5128DB98C414527 "毕竟不是周末，明年试着改成双休日或许会更好。"

    window hide

    pause 0.8

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_ACAAB0A43F254041BE2C5833D3FC0CE4
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    pause 3.5

    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Drum 1.ogg"

    show rs_image_C8358BF2E1A9420A98A9BDCA038D626C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    # Gallery unlock: images/CG/Join-misaki-danjiri/Join-misaki-danjiri 2-1.png
    $ zorder_rs_image_97433B7ED6534086BEE73738CC688FD8 = -100
    show rs_image_97433B7ED6534086BEE73738CC688FD8 as rs_image_97433B7ED6534086BEE73738CC688FD8 zorder zorder_rs_image_97433B7ED6534086BEE73738CC688FD8 onlayer master
    hide rs_image_97433B7ED6534086BEE73738CC688FD8

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_97433B7ED6534086BEE73738CC688FD8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1

    if sys_music_current_file != "sound/BGM/Drum.ogg":
        play music "sound/BGM/Drum.ogg" loop
        $ sys_music_current_file = "sound/BGM/Drum.ogg"

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那么！花车祭的宣传要喊出来！加油征集人选！"
    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "{size=28}好了——上！！{/size}"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    rs_character_6C33AC9430994705AE070406BF54210A "{size=28}DO-KOI-SA-SHYA！！{/size}"

    window hide

    pause 1

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 1


    if judge_lm_condition([]):
        jump block_00003D96

    return

label block_00003D96:
    # Node: 00003D96 (CP3 Daytime Misaki 慎太郎月空)
    call block_00001D36 from _call_block_00001D36

    if judge_lm_condition([]):
        jump block_000041F7

    return

label block_000041F7:
    # Node: 000041F7 (集合！御咲花車祭 2)
    $ set_window("イベントモード")
    stop music fadeout 2
    $ sys_music_current_file = ""

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 2

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E231059B50CB41C989713074B50A8CA5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_6B0609ABE3C348F3A84F5E9250E70BE7

    pause 1.8

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_12471979B7D1437085FB86AB6EEB1E51 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_63B7FCD9DF38442BA0683EF60F550969 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_0082B8EA494C49D7B202B0DC39D7AC3F as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-90, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_32E34DC6044942FDB2E664C9223A1A28 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "太棒了！热闹起来了热闹起来了♪"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这样一来御咲花车祭明年也能顺利继续了，真的太好了。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "要是在我们这一代断绝，就不好对后人交代了。"

    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "对对！正因为有这个祭典现在才有了我们的友情嘛！"

    show rs_image_C989D2B8472147EBAAC08D14FF060BEC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "太大惊小怪了，慎酱，我们是从中学开始才慢慢变得关系好的。"

    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "奥村和{color=#00FFFF}那时候{/color}比起来确实变化很大呐。"

    show rs_image_15F70AA27431427FADF805F167EE684B as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯，不过，明白得把握分寸这一点没变。{w}\n{nw}"
    show rs_image_C989D2B8472147EBAAC08D14FF060BEC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "刚见面的那个时候也……"
    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_229EB6C626CB4AD79FA6063567685C64 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_B4A2258019834560B2658037BA91A812 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_30CFC5FBE4104C718C904D0C834E6E9A as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "唔，想起来了。"

    show rs_image_D7BB1A8267AE4353950D17F94CE6C389 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哈哈，那时候真的对不起了。不过那也是我的交流方法呐。"

    window hide

    pause 0.9

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_51B8A209554F4DA4B049529627B22211

    pause 2.5

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 3.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 3.ogg"

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 0
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_23E95FF3D12540FB88BD74983BE7800E as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_65FB514C0D3B40558703DF2D35F42E17 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04460297D37A447D8CE6298460DB7159

    pause 1.4

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_36A93F6F7FCF48C09A392CB4F1641E2D as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_EDBE31E1BBCA469392FCFBB541869D0F as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "呐呐，哥哥，那孩子……"

    window hide

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_0FA01FA43D804675A701624FAEA2174B as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 1.3

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_EAA3963C4AAB4B40B1892D5734C49773 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_EDBE31E1BBCA469392FCFBB541869D0F as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "一、一直看着这边。为什么。"

    show rs_image_43A92AD398344F4CA5C9A7E8B8BB30EF as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "学校也不一样，不明白。"

    show rs_image_EDBE31E1BBCA469392FCFBB541869D0F as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不过那孩子去年的祭典上也在哦。可能和我们同岁。"

    show rs_image_36A93F6F7FCF48C09A392CB4F1641E2D as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "一个人在那里做什么。有没有认识的人呐。"

    show rs_image_D53DD6BA55FB48F4848D8FF58314958D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "啊，对了！因为寂寞才会看这边的。以前看到的时候也觉得是这样的。"

    show rs_image_0958BEF515FC4BEDB7CAED059E6594C0 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥！我们去和他说说话！"

    show rs_image_C478DAE1143B48E2A30E6AA4B62A0A34 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "欸。可、可是……"

    show rs_image_D53DD6BA55FB48F4848D8FF58314958D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "没关系！去打个招呼！这是礼仪和教养。"

    show rs_image_EAA3963C4AAB4B40B1892D5734C49773 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯、嗯，是呐。好。"

    window hide

    pause 0.4

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 0.4

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_0FA01FA43D804675A701624FAEA2174B as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3BC0411E559D49E38A86F531E7DC85FF

    pause 0.8

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_EAA3963C4AAB4B40B1892D5734C49773 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_69FBB116E5314C399CA15A15DEF01385 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那个，你好。我叫做空，这是我的哥哥月。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "你、你好……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_C85AE28FFB9C45D9A151B43A15022C76 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……"

    show rs_image_D53DD6BA55FB48F4848D8FF58314958D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那个啊，我们在上小学三年级哦。然后我们是兄弟，是双胞胎哦！"

    show rs_image_0FA01FA43D804675A701624FAEA2174B as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欸……"

    show rs_image_36A93F6F7FCF48C09A392CB4F1641E2D as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "你、你的名字是？你多大了？"

    show rs_image_C85AE28FFB9C45D9A151B43A15022C76 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "奥村慎太郎……和你们一样……"

    show rs_image_0958BEF515FC4BEDB7CAED059E6594C0 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "果然同年呐！慎太郎君，这次的祭典和我们一起怎么样。"

    show rs_image_67BFBFF1C1564DEABD3FF67B1C2A408B as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯、嗯……一起也会更有趣的。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……{w=0.5}{nw}"
    show rs_image_15236DB83FF447988A834435AA5BECF1 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "可以吗？"

    show rs_image_D53DD6BA55FB48F4848D8FF58314958D as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "当然可以了！对不对，哥哥。"

    show rs_image_36A93F6F7FCF48C09A392CB4F1641E2D as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯，好、好好相处吧。我叫月，这是我的弟弟……"

    show rs_image_43A92AD398344F4CA5C9A7E8B8BB30EF as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥，自我介绍的话刚才已经做过了。"

    show rs_image_C478DAE1143B48E2A30E6AA4B62A0A34 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "啊、是，抱歉。"

    show rs_image_0FA01FA43D804675A701624FAEA2174B as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……"
    show rs_image_15236DB83FF447988A834435AA5BECF1 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "稍微等一下。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.6

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_36A93F6F7FCF48C09A392CB4F1641E2D as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_EDBE31E1BBCA469392FCFBB541869D0F as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C33AC9430994705AE070406BF54210A "？？"

    window hide

    pause 0.8

    # Gallery unlock: images/CG/Join-misaki-danjiri/Join-misaki-danjiri 3.png
    $ zorder_rs_image_A43CCBE3B95A40109DF2A73F21CB816A = -100
    show rs_image_A43CCBE3B95A40109DF2A73F21CB816A as rs_image_A43CCBE3B95A40109DF2A73F21CB816A zorder zorder_rs_image_A43CCBE3B95A40109DF2A73F21CB816A onlayer master
    hide rs_image_A43CCBE3B95A40109DF2A73F21CB816A

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A43CCBE3B95A40109DF2A73F21CB816A as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "手，伸出来。给你谢礼，谢谢你邀请我。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哇！是什么是什么！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    # Gallery unlock: images/CG/Join-misaki-danjiri/Join-misaki-danjiri 4.png
    $ zorder_rs_image_8C98F73227E949DAA5A09717C8CF0B1E = -100
    show rs_image_8C98F73227E949DAA5A09717C8CF0B1E as rs_image_8C98F73227E949DAA5A09717C8CF0B1E zorder zorder_rs_image_8C98F73227E949DAA5A09717C8CF0B1E onlayer master
    hide rs_image_8C98F73227E949DAA5A09717C8CF0B1E

    show rs_image_8C98F73227E949DAA5A09717C8CF0B1E as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.4

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "蜘蛛先生。{w}刚才路边捡的。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_6C354BF3257840209C797C6559B792C2

    extend "{size=32}噫呀啊啊啊啊啊！！！！！{/size}"

    window hide

    pause 1

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 100
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 100
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_12471979B7D1437085FB86AB6EEB1E51 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_C8509382B1E34741B9130C4CA5DE55D6 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_D7BB1A8267AE4353950D17F94CE6C389 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-90, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_32E34DC6044942FDB2E664C9223A1A28 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 0.6

    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "想起来就直冒冷汗……！"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "毕竟空在那不久前刚开始害怕虫子呐。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "天真无邪有时也很恐怖……"

    show rs_image_CB70B28808D840B5A51436CA4E858F49 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "慎酱那时候那么安静，真的很有成熟的感觉呐。"

    show rs_image_4D5E70DCADBB4F2CA52AB49DED72D7C5 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "说到这一点，现在正相反呐。是什么导致的？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "到底是为什么——呢！说不定是因为和两人见面哦。"

    show rs_image_C989D2B8472147EBAAC08D14FF060BEC as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欸～～！好像有点开心呐。能打开慎酱的心灵之窗什么的！"

    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "就是这样就是这样♪"

    show rs_image_D81691F1A7F841C4BE6CB3D91B4665C7 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……"

    window hide

    pause 1

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 400
    $ zorder_tag_C35197E0A50A470FA7C5D15E6DAEFAA0 = 200
    show rs_image_23E95FF3D12540FB88BD74983BE7800E as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_7AC620439A6042AF98D62C983235F7D4 as tag_C35197E0A50A470FA7C5D15E6DAEFAA0 at center_bottom zorder zorder_tag_C35197E0A50A470FA7C5D15E6DAEFAA0 onlayer master
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    pause 1

    $ zorder_tag_24B3A49A9E5E4F6283DD3ADAF445EC35 = 300
    $ zorder_tag_B5AF370F249D4C84BB709DC5FDDD49A9 = 300
    show rs_image_0FA01FA43D804675A701624FAEA2174B as tag_24B3A49A9E5E4F6283DD3ADAF445EC35 at right_top zorder zorder_tag_24B3A49A9E5E4F6283DD3ADAF445EC35 onlayer master
    show rs_image_36A93F6F7FCF48C09A392CB4F1641E2D as tag_B5AF370F249D4C84BB709DC5FDDD49A9 at left_top zorder zorder_tag_B5AF370F249D4C84BB709DC5FDDD49A9 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.5

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "阿月喜欢空？"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯，喜欢哦。"

    show rs_image_15236DB83FF447988A834435AA5BECF1 as tag_24B3A49A9E5E4F6283DD3ADAF445EC35 zorder zorder_tag_24B3A49A9E5E4F6283DD3ADAF445EC35 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "空是男孩子，阿月也是男孩子哦？而且你们是兄弟哦？"

    show rs_image_67BFBFF1C1564DEABD3FF67B1C2A408B as tag_B5AF370F249D4C84BB709DC5FDDD49A9 zorder zorder_tag_B5AF370F249D4C84BB709DC5FDDD49A9 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "和这个没有关系，喜欢就是喜欢。对喜欢的事物说喜欢，难道不可以？"

    show rs_image_C85AE28FFB9C45D9A151B43A15022C76 as tag_24B3A49A9E5E4F6283DD3ADAF445EC35 zorder zorder_tag_24B3A49A9E5E4F6283DD3ADAF445EC35 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……"
    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "近亲相奸……"

    show rs_image_36A93F6F7FCF48C09A392CB4F1641E2D as tag_B5AF370F249D4C84BB709DC5FDDD49A9 zorder zorder_tag_B5AF370F249D4C84BB709DC5FDDD49A9 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯？近……？"

    show rs_image_15236DB83FF447988A834435AA5BECF1 as tag_24B3A49A9E5E4F6283DD3ADAF445EC35 zorder zorder_tag_24B3A49A9E5E4F6283DD3ADAF445EC35 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不，什么都没有。"

    window hide

    pause 0.5

    hide tag_24B3A49A9E5E4F6283DD3ADAF445EC35
    hide tag_B5AF370F249D4C84BB709DC5FDDD49A9
    show rs_image_A6EB165FEA4F43D98FA0D7F5088E39A4 as tag_C35197E0A50A470FA7C5D15E6DAEFAA0 zorder zorder_tag_C35197E0A50A470FA7C5D15E6DAEFAA0 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.7

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……呐，阿月，人是，各不……各不……嗯。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "各不相同？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……对，各不相同的。"

    window hide

    stop music2 fadeout 2.5
    $ sys_music2_current_file = ""

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    pause 1.5

    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_2EDCBF8750D348A8A06B06DB4F635C1C as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_29B059D0AECE4F3FBF86EE5DA29B17DF as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_32E34DC6044942FDB2E664C9223A1A28 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_C35197E0A50A470FA7C5D15E6DAEFAA0
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 0.8

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg"

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "让我们有了现在这样的缘分的祭典，以后也要慎重对待积极参加呐。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "真是的，所以说没那么夸张～"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "今年一定会成为这几年最热闹的一次，评价也会刷刷刷地涨上去！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_C98211B62EA04A368AA5021885891661 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "只要我们在御咲花车祭就不会消失！我们结缘的神灵，非常感谢——！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_4D5E70DCADBB4F2CA52AB49DED72D7C5 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_48394E3397A94AD090308D24BFC677E3 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_E21ACD1443A4402AA37E7CE200FF6D4C as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "三位～宴会已经开始了！快来快来！！"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_3AD3CC529F514E6299E88A1EFA0C1998 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "对对！这才是正题！！好——！今年也要放开了吃——！！"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.7

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_FE681BB78F1F4D339A2566A5D9707982 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_02ECE9B805B742C6B558DFD2FD5D2608 as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那个场合让我们认识的是空，也就是说，空就是神明！！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欸？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_B4F55DFE937C4D9B8956BB29AB3AB0B3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "不愧是空！！终于成为神了……！\n嗯，其实以前就觉得空是我的神明……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_460C6B5F6FA34A3E939381F99A268C0E as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "唔——说什么不着边际的话呢！我要先走了哦！"

    if sys_effect2_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    show rs_image_4683860EE22143EDB1980090E250F53A as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.55

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_A9272CFB7442404397033A5CA243E723 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "啊，等、等等我，空～！"

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 2

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    call scb_flag_title_end(3, _("「集合！御咲花车祭」")) from _call_scb_flag_title_end_11

    if judge_lm_condition([]):
        jump block_000041FB

    return

label block_000041FB:
    # Node: 000041FB (Phase: 0)
    $ C3S3Phase = 0
    if Chapter <> 3:
        $ del C3S3Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_00004224
    if judge_lm_condition([]):
        jump block_000041FA

    return

label block_00004224:
    # Node: 00004224 ()

    return

label block_000041FA:
    # Node: 000041FA (FINISH)
    $ C3S3 = True
    if ((C1SG2 == False) or (C2SG2 == False)) and (C3S1 == True) and (C3S2 == True):
        $ SYSBreakCurrentChapter = True

    if judge_lm_condition([]):
        jump block_00004225

    return

label block_00004225:
    # Node: 00004225 (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_12

    if judge_lm_condition([]):
        jump block_00004226

    return

label block_00004226:
    # Node: 00004226 (FLAG FINISH)
    $ set_window("(標準)")
    pause 1.5

    if sys_music2_current_file != "sound/BGM/Flag finished.ogg":
        play music2 "sound/BGM/Flag finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件{/color}{color=#AA0055}“集合！御咲花车祭”{/color}{color=#0080FF}成功结束。』{/color}"

    window hide


    if judge_lm_condition([{ "scope": 0, "content": "VarExists(\"SYSBreakCurrentChapter\") == True" }]):
        jump block_00004224
    if judge_lm_condition([]):
        jump block_00004227

    return

label block_00004227:
    # Node: 00004227 (RESET)
    pause 4

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5


    if judge_lm_condition([]):
        jump block_00004224

    return

