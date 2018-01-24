# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 0000390D (FLAG: 久遠回憶)

label block_0000390E:
    # Node: 0000390E ()

    if judge_lm_condition([]):
        jump block_0000390F

    return

label block_0000390F:
    # Node: 0000390F (Phase: 99)
    if Not(VarExists("C1S5Phase")):
        $ C1S5Phase = 0
    $ C1S5Phase = 99

    if judge_lm_condition([]):
        jump block_0000397E

    return

label block_0000397E:
    # Node: 0000397E (F5 START)
    call scb_flag_title(1, _("「久远回忆」"), "rs_image_23D4891106E849B3821D574553A19EF6") from _call_scb_flag_title_10

    if judge_lm_condition([]):
        jump block_00003910

    return

label block_00003910:
    # Node: 00003910 (久遠回憶 1)
    $ set_window("イベントモード")
    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_75FF9F1806CB4303B3C6FA0F85C6B4E6 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 1

    show rs_image_40977ADC555F41629B45159FB51D8798 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 1

    show rs_image_76EAC7F0C8EB4109814927F3F679AEC7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 2

    show rs_image_A1B95DB5524442E4BEBF32BAE17F8F8E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Bell 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Bell 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Bell 2.ogg"

    show rs_image_A1B95DB5524442E4BEBF32BAE17F8F8E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 0.5

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "早上好～！"

    rs_character_69E4C25BE6F24CC0A44F7F54179040D3 "啊啦，早上好友君！稍等一下哦～。"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_69E4C25BE6F24CC0A44F7F54179040D3 "忍！友君来了哦～差不多该收起春假的心情了。"

    window hide

    pause 0.8

    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 1

    # Gallery unlock: images/CG/Prelife-memory/Prelife-memory 1.png
    $ zorder_rs_image_CEDACC94A9174ACEBB28422618EB83AD = -100
    show rs_image_CEDACC94A9174ACEBB28422618EB83AD as rs_image_CEDACC94A9174ACEBB28422618EB83AD zorder zorder_rs_image_CEDACC94A9174ACEBB28422618EB83AD onlayer master
    hide rs_image_CEDACC94A9174ACEBB28422618EB83AD

    show rs_image_CEDACC94A9174ACEBB28422618EB83AD as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EF2D3A4912BA490B9BDDB92C8700586E

    pause 0.5

    window show

    pause 0.3

    if sys_music_current_file != "sound/BGM/The past precious.ogg":
        play music "sound/BGM/The past precious.ogg" loop
        $ sys_music_current_file = "sound/BGM/The past precious.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "早上好，友。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊哈哈哈♪怎么回事嘛，忍的头发～好厉害的睡姿——！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不……不用你管。再说了友也没有说别人的立场。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我的是本来就有的（呆毛）哦！"

    rs_character_69E4C25BE6F24CC0A44F7F54179040D3 "该走了哦你们，今天就是新学期了，要好好学习哦！"

    rs_character_B853B4626C714AB6BEEA7293354291C6 "好——的——"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    window hide

    pause 0.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_76EAC7F0C8EB4109814927F3F679AEC7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_C8A7A9763D4C445088DB9B5CF31A7D6D as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "今天开始就是六年级了！学校的头头哦～\n也可以做团体操了♪"

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F8218B60CA674EDDA9B94C8DA568E8B0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸～团体操很麻烦的。"

    show rs_image_3F78FB00BCED4DCC86A9E39C814D40EA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说什么呐！不是超帅的嘛！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "裸足哦！也有在拍手哦！！我以前就很憧憬了哦～！"

    show rs_image_7E08762184A342409082DE4098B70327 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "是吗。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_DB6DCC736BCD4CC6B741DB826442FC30 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇，完全没有兴趣！感觉很没气氛哦忍！"

    show rs_image_1503A55409E04E4282A40803C56C9FEC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "难道不是修学旅行那边更有意思？"

    show rs_image_C8A7A9763D4C445088DB9B5CF31A7D6D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，也对！那个也很开心哦～♪\n忍！到时候绝对要分到同一个组哦！"

    show rs_image_F8218B60CA674EDDA9B94C8DA568E8B0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……在那之前，是不是在一个班都不知道。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_4E9BDB9405C34046BB4DB184FE211080 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，说起来也是……"

    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔～这次也和忍一个班就好了呐。对不对呀，忍？"

    show rs_image_EF29254D67B448F48CD5987CB3746ED7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……我倒是无所谓。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_4E9BDB9405C34046BB4DB184FE211080 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真是的——感觉好没劲！"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    # Gallery unlock: images/CG/Prelife-memory/Prelife-memory 2.png
    $ zorder_rs_image_709A0F8E88FC4927B3F2872F13C17FA7 = -100
    show rs_image_709A0F8E88FC4927B3F2872F13C17FA7 as rs_image_709A0F8E88FC4927B3F2872F13C17FA7 zorder zorder_rs_image_709A0F8E88FC4927B3F2872F13C17FA7 onlayer master
    hide rs_image_709A0F8E88FC4927B3F2872F13C17FA7

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_709A0F8E88FC4927B3F2872F13C17FA7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.4

    window show

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，由实阿姨好！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……早上好。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "啊啦啊啦，友酱和忍酱，你们早。\n今天开始要上学了呐。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯，今天开始就是六年级了哦！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友太孩子气了……"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "哦，已经六年级了啊，总觉得没多久呐。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "能像这样茁壮成长，阿姨很高兴哦。{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    extend "神啊，请务必守护这些孩子……"

    if sys_effect2_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "阿、阿姨感动过头了。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "啊啦，对不起哦。人老了就容易动感情了呐。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "不过也真的长大了。不久之前明明还只有这么一点的。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈，我比忍还要高哦♪"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "没这回事。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——绝对是我比较高。看，视线是我比较高嘛。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "说什么呢，那只是错觉。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "cuòjué？"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "那让阿姨来量一下？"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "好了，两人放下书包背靠背站好哦～"

    window hide

    # Gallery unlock: images/CG/Prelife-memory/Prelife-memory 3.png
    $ zorder_rs_image_D9D9BBF18FFA4E278F5E7FF9A7D00AF2 = -100
    show rs_image_D9D9BBF18FFA4E278F5E7FF9A7D00AF2 as rs_image_D9D9BBF18FFA4E278F5E7FF9A7D00AF2 zorder zorder_rs_image_D9D9BBF18FFA4E278F5E7FF9A7D00AF2 onlayer master
    hide rs_image_D9D9BBF18FFA4E278F5E7FF9A7D00AF2

    show rs_image_D9D9BBF18FFA4E278F5E7FF9A7D00AF2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎样？怎样？？我比较高？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不可能的，应该是一样高。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "唔……{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "啊，友酱好像稍微高一点哦。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——哇——！太好了太好了～♪"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔……"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "没关系的，忍酱很快就会长高的。{w}\n然后就会成为非常有男子气概的大人哦。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "小时候长得那么像女孩子，被左邻右舍好可爱好可爱地叫……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    window hide

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_76EAC7F0C8EB4109814927F3F679AEC7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_4E9BDB9405C34046BB4DB184FE211080 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊～阿姨，不行的，不能说那种话的！\n忍对这个非常在意，很可怜的～！"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "啊啦，是吗？对不起哦，忍酱。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "不过，忍酱将来绝对会是美少年哦～{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "阿姨我可以保证♪"

    show rs_image_DB6DCC736BCD4CC6B741DB826442FC30 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——！！阿姨，我呢我呢——？"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "友酱也是哦！"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    if sys_effect_current_file != "sound/Effect Sound/Trumpet 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Trumpet 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Trumpet 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "耶♪♪"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    window hide

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4A350FEF4FAA4A548C456B441273F09D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 1.5

    show rs_image_B53ABA9A3FD64740BFD28F2AACA8FEAC as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 1

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1503A55409E04E4282A40803C56C9FEC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8D269274348D4471842CE1A9610C5E4E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    show rs_image_C8A7A9763D4C445088DB9B5CF31A7D6D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    show rs_image_EF29254D67B448F48CD5987CB3746ED7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.5

    window hide

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1E452D70E5C547059D37DC526E22F054 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.4

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_E56D079CF9A9403B947B2DF8ACB86745 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_4DC4F6088E084A41874643F391473935 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    pause 0.3

    if sys_effect3_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "看，果然是我比较高嘛！两厘米哦！"

    show rs_image_0D797E52B2C54A78BF3F724C4C8F9F06 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "烦死了……很快就会被追上的。"

    show rs_image_8AA7B98D29D34C418C34CC74D86EFA3F as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "其他呢其他呢～？"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_7C6690C89A92417B86D452D3284FBA0A as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊咧！？握力输了……\n忍好厉害——意外的很有力气呐。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_4F856FB2B4664C1D80A42D37B4A39A79 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "呵呵。"

    show rs_image_E78B5CA09EC943E597B65FF4852E5C74 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不会是握力计坏了～？\n忍不可能这么有力气的，来握握我的手。"

    if sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……嗯！"

    show rs_image_8780B91C5C7A4DEDA4F1752F1344E327 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_E58D83DB9E234DE7AAB86A64350E6FC8

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊疼疼疼疼！！！！弃权弃权！！！{w}\n这、这是真的……"

    show rs_image_0DB917D142CD47D99E27C8F723FE86E5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……我有这么大的力气啊。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_527B98EA639A40B28847198A4BC5CE64 "好了，检测结束的同学请回教室换衣服哦。\n所有人都检测完成后，就要开始放学前的总结会了哦——"

    window hide

    pause 0.4

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B53ABA9A3FD64740BFD28F2AACA8FEAC as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    window show

    rs_character_527B98EA639A40B28847198A4BC5CE64 "那么，要先告诉大家一件事。{w}\n下周会有一位男生转入我们班哦。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{size=36}欸——！！！{/size}"

    rs_character_527B98EA639A40B28847198A4BC5CE64 "所以……{w}大家要怎么做呢？"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{size=36}好好相处！{/size}"

    rs_character_527B98EA639A40B28847198A4BC5CE64 "对哦。大家一直都在好好相处，\n可是那个孩子还完全不了解大家哦。"

    rs_character_527B98EA639A40B28847198A4BC5CE64 "一定在担心能不能和大家好好相处，\n有不明白的事情的时候一定要好好帮助他哦。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{size=36}好——！{/size}"

    rs_character_527B98EA639A40B28847198A4BC5CE64 "那么今天的课结束了！{w}\n最后，“回家的路上小心过马路”！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if sys_effect3_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "{size=32}{/size}{size=36}回家的路上小心过马路{/size}{size=32}！{/size}"

    rs_character_527B98EA639A40B28847198A4BC5CE64 "大家再见！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    extend "{size=36}老师再见！！{/size}"

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window hide

    pause 0.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4A350FEF4FAA4A548C456B441273F09D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_1503A55409E04E4282A40803C56C9FEC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_422CEAA0768946AF8E1A713B2CB845CF as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "转校生会是怎样的人呐～！好期待哦！"

    show rs_image_F8218B60CA674EDDA9B94C8DA568E8B0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我无所谓……"

    show rs_image_DB6DCC736BCD4CC6B741DB826442FC30 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "又来了～很没气氛的哦～"

    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……我实在不能理解友所谓的“气氛”到底指的是什么。"

    show rs_image_C8A7A9763D4C445088DB9B5CF31A7D6D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "有气氛就是有气氛嘛！气氛气氛！就是气氛很好的意思！"

    show rs_image_2E15079D93F042638344B24315ECF18B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那是什么，为什么我必须要适应友周围的气氛？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "再说了，我和友真的合得来？"

    show rs_image_8D269274348D4471842CE1A9610C5E4E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸……这、这个……就、就算这么生气也……"

    show rs_image_F8218B60CA674EDDA9B94C8DA568E8B0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这不公平。我不喜欢。"

    show rs_image_06FBA0115C924EB89765D7CAFA0D532E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……以后不会再说的……"

    show rs_image_D66809B07DBB47B58D9A2808822498AA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊，我不是这个意……{w}\n{nw}"
    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……不……我、忘东西了……"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window hide

    pause 0.4

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4A350FEF4FAA4A548C456B441273F09D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.4

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜……"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    show rs_image_39BA5B8CF114437EB5FCE26D91B9FAD5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "刚才就在看了，说实话，那很不靠谱吧～"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "森海～别再和那种家伙玩了，累不累？"

    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没、没有这回事。老师也说了，\n大家要好好相处，忍会很可怜的……"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "说是可怜，你自己不也……？{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "那个，怎么说的来着……"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "自作自受？"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "对！自作自受！和那种无趣的家伙在一起你也是自作自受！"

    show rs_image_06FBA0115C924EB89765D7CAFA0D532E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不是的，没有这回事……我们是朋友……不能这样做的……"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "可是啊，就算我们找他说话也一直没觉得有什么意思，无趣而且灰暗！"

    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "长得也和女孩子一样，人妖啊，哈哈哈哈！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_7CFC2D3570394463AE9EB2953AC6BE86 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "给我住口！！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "什、什么啊，有什么不满么。"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "算了，别管了，放任那两人自生自灭不就好了？走了走了。"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "哦……"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window hide

    pause 0.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_4A350FEF4FAA4A548C456B441273F09D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_06FBA0115C924EB89765D7CAFA0D532E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    window show

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……好可怜……"

    window hide

    pause 0.3

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_4A350FEF4FAA4A548C456B441273F09D as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_F800B17A2FA64BEBA751423EA81301AE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_F9DBAF1EE9EF4C7F828153AA794ECB5E

    pause 0.3

    window show

    pause 0.3

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    show rs_image_81CF27D906FA4867BCAEC4C85AAC1840 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    window hide

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B53ABA9A3FD64740BFD28F2AACA8FEAC as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_527B98EA639A40B28847198A4BC5CE64 "接下来介绍转校生——"

    rs_character_527B98EA639A40B28847198A4BC5CE64 "今天这位{color=#FF00FF}逆濑荒哉{/color}君就是我们班的一员了哦。\n来逆濑君，做一下自我介绍。"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    show rs_image_AD98FF52060B467081E8E309526CF300 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at center_top zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.5

    window show

    rs_character_06E99199BFCE4C93B1F3942F0090429B "我是几天前从东京搬过来的逆濑荒哉。"

    show rs_image_93274A5024EC4DB48BC9078403E617D2 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_06E99199BFCE4C93B1F3942F0090429B "小学的最后一年，虽然不会和大家相处太久，请多多关照。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "厉害，金发——{w}\n{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    extend "有点恐怖呐……{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "好酷——是城里人。"

    rs_character_527B98EA639A40B28847198A4BC5CE64 "那么座位就在……绫濑君，你旁边可以吗？"

    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1503A55409E04E4282A40803C56C9FEC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……？……好。"

    rs_character_527B98EA639A40B28847198A4BC5CE64 "逆濑君就请坐在这位同学旁边哦。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    show rs_image_AD98FF52060B467081E8E309526CF300 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at center_top zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_06E99199BFCE4C93B1F3942F0090429B "我明白了。"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    show rs_image_EF29254D67B448F48CD5987CB3746ED7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_B77CF96CC6094B549EE21B026980683E as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at left_top zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    window show

    pause 0.3

    rs_character_06E99199BFCE4C93B1F3942F0090429B "绫濑桑{size=12}{color=#C0C0C0}（同龄不亲密非正式场合多用于称呼女性）{/color}{/size}，请多关照。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸……啊……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "绫濑“桑”，那家伙是男的哦。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_AD98FF52060B467081E8E309526CF300 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_06E99199BFCE4C93B1F3942F0090429B "诶，真的？！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{size=36}哈哈哈哈！！！{/size}"

    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_6EBDB8D5A1AD4DF082F5B765D83DE7CD as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_06E99199BFCE4C93B1F3942F0090429B "抱歉抱歉，绫濑君，长得太奇怪了一下子没能认出来。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=36}哈哈哈！！！{/size}"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "等、等等……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_527B98EA639A40B28847198A4BC5CE64 "好了！不要捉弄别人！！！绫濑君也不喜欢的，明白吗？"

    rs_character_527B98EA639A40B28847198A4BC5CE64 "要体谅别人！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{size=36}……好——{/size}"

    pause 0.4

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    show rs_image_AD98FF52060B467081E8E309526CF300 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at center_top zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_06E99199BFCE4C93B1F3942F0090429B "……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_93274A5024EC4DB48BC9078403E617D2 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_06E99199BFCE4C93B1F3942F0090429B "{size=16}（什么啊，被吓了一跳。……对不？）{/size}"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "{size=16}（你很明白嘛♪）{/size}"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "{size=16}（……多关照了，逆濑。）{/size}"

    show rs_image_B77CF96CC6094B549EE21B026980683E as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_06E99199BFCE4C93B1F3942F0090429B "{size=16}（嗯，我也是。）{/size}"

    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    window hide

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1E452D70E5C547059D37DC526E22F054 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍……真的没关系？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……什么事？"

    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "还说什么事……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_39BA5B8CF114437EB5FCE26D91B9FAD5 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    show rs_image_B77CF96CC6094B549EE21B026980683E as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    rs_character_06E99199BFCE4C93B1F3942F0090429B "绫濑酱{size=12}{color=#C0C0C0}（同龄不亲密多用于称呼女性）{/color}{/size}，刚才抱歉了☆"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "哈哈哈哈！绫濑“酱”！完全被当做女孩子了！"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "逆濑，你真有意思。"

    show rs_image_F800B17A2FA64BEBA751423EA81301AE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    show rs_image_7CFC2D3570394463AE9EB2953AC6BE86 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "快……快住手！"

    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    show rs_image_AD98FF52060B467081E8E309526CF300 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at center_top zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_06E99199BFCE4C93B1F3942F0090429B "绫濑酱旁边那个是谁？"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "嗯……森海？"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "那家伙和绫濑一样没意思，还是别认识比较好。"

    show rs_image_6EBDB8D5A1AD4DF082F5B765D83DE7CD as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_06E99199BFCE4C93B1F3942F0090429B "欸——是吗。说起来，森海头上的那个……{w}\n{nw}"
    show rs_image_B77CF96CC6094B549EE21B026980683E as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "算了，不说了。"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "欸，什么什么？怎么？"

    show rs_image_1FB04C4573E84E4DAF670EB9FD7BD6C6 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_06E99199BFCE4C93B1F3942F0090429B "等会告诉你。"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "跟我们走，会带你转转学校的。"

    show rs_image_B77CF96CC6094B549EE21B026980683E as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_06E99199BFCE4C93B1F3942F0090429B "哦，谢了♪"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好不舒服的感觉。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……嗯。"

    window hide

    pause 0.5

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_D950F63EF18B4E0ABAE213B4ED33B9B4

    pause 2

    if sys_effect3_current_file != "sound/Effect Sound/Rain 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Rain 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Rain 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_2BD0E40E817E44B28F8F0279FD7035C3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 2

    show rs_image_533AAAC44B2D41CB82225B285E277639 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    stop effect3 fadeout 2
    $ sys_effect3_current_file = ""

    pause 1

    if sys_music_current_file != "sound/BGM/My precious time - piano.ogg":
        play music "sound/BGM/My precious time - piano.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time - piano.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_39BA5B8CF114437EB5FCE26D91B9FAD5 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1503A55409E04E4282A40803C56C9FEC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    show rs_image_1FB04C4573E84E4DAF670EB9FD7BD6C6 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_B77CF96CC6094B549EE21B026980683E as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at left_top zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    show rs_image_F800B17A2FA64BEBA751423EA81301AE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.8

    show rs_image_1E452D70E5C547059D37DC526E22F054 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1503A55409E04E4282A40803C56C9FEC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    show rs_image_D66809B07DBB47B58D9A2808822498AA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_6EBDB8D5A1AD4DF082F5B765D83DE7CD as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at left_top zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    show rs_image_1FB04C4573E84E4DAF670EB9FD7BD6C6 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    show rs_image_F800B17A2FA64BEBA751423EA81301AE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1FB04C4573E84E4DAF670EB9FD7BD6C6 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    show rs_image_81CF27D906FA4867BCAEC4C85AAC1840 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_AD98FF52060B467081E8E309526CF300 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    show rs_image_7CFC2D3570394463AE9EB2953AC6BE86 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.7

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_533AAAC44B2D41CB82225B285E277639 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_34FA0D57799A4460A99781122493D86A

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_7CFC2D3570394463AE9EB2953AC6BE86 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "适……适可而止！总是这么欺负人不觉得很可怜吗！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}…………{/size}"

    if sys_effect_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Wind 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=14}…小……烦人——……{/size}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=14}……呵呵呵……\n……啊～说起来那个真……呵呵……{/size}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=14}……不好，我快不敢看了，呵呵……{/size}"

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "你们………"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_1FB04C4573E84E4DAF670EB9FD7BD6C6 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at left_top zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_06E99199BFCE4C93B1F3942F0090429B "可怜什么的，我们只是在开玩笑，不用那么上纲上线。"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "真的很无趣呐——"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "所以才说小……"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "欸？小？小什么？？"

    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什、什么啊……？刚才一直在……"

    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F800B17A2FA64BEBA751423EA81301AE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友，请就此打住。"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_8D269274348D4471842CE1A9610C5E4E as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，等等我，忍！"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Wind 1.ogg"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "说起来啊，逆濑，你真是天才。"

    rs_character_06E99199BFCE4C93B1F3942F0090429B "是嘛？那个不管谁都会那么想的。"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "哈哈哈哈！！不愧是城里人！"

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    window hide

    pause 0.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1E452D70E5C547059D37DC526E22F054 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    pause 0.8

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍、没事……？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……友，有句话我必须说明白。"

    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什、什么？"

    show rs_image_2E15079D93F042638344B24315ECF18B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "希望你不要再把“可怜”挂在嘴边了。"

    show rs_image_39BA5B8CF114437EB5FCE26D91B9FAD5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶？"

    show rs_image_F800B17A2FA64BEBA751423EA81301AE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "只会让我觉得更悲惨。也许正如他们所说，只是恶质的玩笑。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "可被这样一说……{w=1}“被欺负的正是……{w=0.5}我”。{w}\n{nw}"
    show rs_image_81CF27D906FA4867BCAEC4C85AAC1840 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……所以，不要说了。"

    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我、我……我只是在为忍好……"

    show rs_image_2E15079D93F042638344B24315ECF18B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你的所作所为并没有好结果。\n我并不想隐藏什么，也不想因此受伤。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "而且友的反应太大了，变相带动了他们的话题。"

    show rs_image_06FBA0115C924EB89765D7CAFA0D532E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是、是这样……"

    show rs_image_F800B17A2FA64BEBA751423EA81301AE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "对，就是这样。所以……{w}求你了，保持沉默吧。"

    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可、可是、可是……！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍被那样对待……难道让我站在一边看着……？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我们是……朋友……对不对……呜……"

    pause 0.3

    if sys_effect3_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_CFE8F9FD29E14010B581297CB997BF44 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我……明明是……忍、忍的……朋友……\n可……（抽泣）……哇……！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_D66809B07DBB47B58D9A2808822498AA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友！？等……等等！……不要哭……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_CFE8F9FD29E14010B581297CB997BF44 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可是！我……我是……忍的朋友……！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……我想帮……呜……可……！哇！哇啊啊啊——！！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友……"

    window hide

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_F708B3E5BAC74DE399384A41501B1B38 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    window show

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……明明从小就在一起的……{w}\n明明这么喜欢……的！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对忍说这么……过分的话，我也……！{w}\n很讨厌很痛苦……哇啊啊啊！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "对不起……友，嗯，是啊，\n友为了我很努力了，对不起。"

    window hide

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_1E452D70E5C547059D37DC526E22F054 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_3FC8F7E928AF4CC4946C11ECF4120803 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "真的…对不起……谢谢……\n对不起……！！呜……哇啊啊……"

    if sys_effect3_current_file != "sound/Effect Sound/Rain 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Rain 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Rain 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_2BD0E40E817E44B28F8F0279FD7035C3 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D6BC962AE17948D893E50BE9B4670973

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}呜啊啊啊！！{/size}"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_B6D2CFDC1CB5407EACD7FBC1D100D198

    stop music fadeout 3
    $ sys_music_current_file = ""

    stop effect3 fadeout 2
    $ sys_effect3_current_file = ""

    pause 4

    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    show rs_image_A1B95DB5524442E4BEBF32BAE17F8F8E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    window show

    rs_character_3A742340BEAD415FAC80AFEA0A84B586 "我们走了。"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_47F13A8A6643413691290FE8226AE77C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 0.6

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    window show

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7E08762184A342409082DE4098B70327 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    if sys_music_current_file != "sound/BGM/The past precious.ogg":
        play music "sound/BGM/The past precious.ogg" loop
        $ sys_music_current_file = "sound/BGM/The past precious.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好想睡……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "没睡醒？昨天晚上做什么了？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔～嗯……电脑～很好玩呐～玩得有些过头了～"

    show rs_image_1503A55409E04E4282A40803C56C9FEC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊～之前你说过买了电脑呐。{w}\n不过，太过火的话视力会下降的。"

    show rs_image_39BA5B8CF114437EB5FCE26D91B9FAD5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "眼镜……说不定也不错呐～"

    show rs_image_F8218B60CA674EDDA9B94C8DA568E8B0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "太无忧无虑了。姿势会变坏，头发也会乱糟糟的哦。"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_41210EA5B30342049A9A851AEFDF7211 = 200
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_2E15079D93F042638344B24315ECF18B as tag_41210EA5B30342049A9A851AEFDF7211 at center_top zorder zorder_tag_41210EA5B30342049A9A851AEFDF7211 onlayer master
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4E9BDB9405C34046BB4DB184FE211080 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_41210EA5B30342049A9A851AEFDF7211
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_2E15079D93F042638344B24315ECF18B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "总的来说，姿势变坏，视力下降，打乱生活习惯，\n最终表现在外表上。明白了？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4E9BDB9405C34046BB4DB184FE211080 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔。"

    show rs_image_F8218B60CA674EDDA9B94C8DA568E8B0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "觉睡不好的话上课也无法认真听讲，\n上课不能认真听讲的话，学习也会退步。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "然后再用越来越少的休息时间去玩电脑，睡眠更加不足……\n整个就是恶性循环。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4E9BDB9405C34046BB4DB184FE211080 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔唔。"

    show rs_image_2E15079D93F042638344B24315ECF18B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "稍微自制一点哦？不要因为妈妈不在就太放纵了。"

    show rs_image_DB6DCC736BCD4CC6B741DB826442FC30 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯嗯……我会注意的。{w}不过啊，不觉得忍君，角色性格变了吗？"

    show rs_image_D66809B07DBB47B58D9A2808822498AA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "诶？没有。"

    show rs_image_39BA5B8CF114437EB5FCE26D91B9FAD5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不，和之前不太一样了，但好像也没什么明显的变化……"

    show rs_image_F8218B60CA674EDDA9B94C8DA568E8B0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "什么意思？错觉？"

    show rs_image_DB6DCC736BCD4CC6B741DB826442FC30 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是错觉～？"

    show rs_image_EF29254D67B448F48CD5987CB3746ED7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，很普通……的……{w=0.4}对不对？"

    show rs_image_39BA5B8CF114437EB5FCE26D91B9FAD5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不，那个，为什么要用问句，是我在问忍好不好。"

    show rs_image_F8218B60CA674EDDA9B94C8DA568E8B0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔……这种绕圈子的说话方式，和那些电脑玩多了的人一样。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_3F78FB00BCED4DCC86A9E39C814D40EA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸！不该显得很有知识才对嘛？"

    if sys_effect2_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_297D12A37B1F462D8B77493FEF02B193 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "像是宅男。"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4E9BDB9405C34046BB4DB184FE211080 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么——！！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    if sys_effect2_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "啊啦啊啦，两人今天也很活跃呐。"

    window hide

    pause 0.6

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E4EBFCBF8642432D983EFD32ED4B980B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1

    show rs_image_1E452D70E5C547059D37DC526E22F054 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_B53ABA9A3FD64740BFD28F2AACA8FEAC as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 1

    window show

    stop music fadeout 0.1
    $ sys_music_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    show rs_image_1FB04C4573E84E4DAF670EB9FD7BD6C6 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at center_top zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    rs_character_06E99199BFCE4C93B1F3942F0090429B "来得好啊！{color=#FF0000}小强脑袋{/color}。"

    if sys_music_current_file != "sound/Effect Sound/Phychological 1.ogg":
        play music "sound/Effect Sound/Phychological 1.ogg" loop
        $ sys_music_current_file = "sound/Effect Sound/Phychological 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    with rs_effect_7F6C95985A7641738465E73831D557C2

    pause 0.4

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "！？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "！！"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=36}哈哈哈哈！！！{/size}"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9762785FEB1642A48FE9FA825670E189

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "呵呵呵！！不错的绰号嘛，森海！"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "果然水准就是不一样。"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "逆濑君没说我们都没发现，呵呵……"

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "呵呵……早上好呀小强酱。{w}\n哈哈……好低贱哦，不要过来哦——{w}\n嘻嘻……被那么说“好可怜”哦——"

    rs_character_06E99199BFCE4C93B1F3942F0090429B "正相反，是大家都没往那边想～我转过来的第一天就发现了。"

    rs_character_06E99199BFCE4C93B1F3942F0090429B "那个，不是和小强的触角很像嘛。"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "哇哈哈哈哈哈！不好，命中笑点了！！！"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "哈哈哈哈！逆濑最强了～！"

    pause 0.4

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    extend "{size=32}{color=#FF0000}哈哈哈哈！！！{/color}{/size}"

    pause 0.5

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "为……什……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友……！"

    stop music2 fadeout 0.5
    $ sys_music2_current_file = ""

    stop music fadeout 0.5
    $ sys_music_current_file = ""

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1E452D70E5C547059D37DC526E22F054 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_3FBF9470026545738C69B18D7D539AA9

    pause 0.8

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_06FBA0115C924EB89765D7CAFA0D532E as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F800B17A2FA64BEBA751423EA81301AE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友……"

    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我该……怎么做……才……怎么做才好……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "被、被那么说……好难受……"

    show rs_image_2E15079D93F042638344B24315ECF18B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "总之友先去保健室休息，我……找他们抱怨几句。"

    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不……不、不行，不能去。做了那种事的话，忍就会……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "就算是玩笑……{w=1}{color=#C0C0C0}有些话{/color}{w=1.5}{color=#808080}也是不能说的。{/color}"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1E452D70E5C547059D37DC526E22F054 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_297D12A37B1F462D8B77493FEF02B193 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.5

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我去了。"

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    window hide

    pause 1.5

    if sys_music_current_file != "sound/BGM/My precious time - piano.ogg":
        play music "sound/BGM/My precious time - piano.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time - piano.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_2BD0E40E817E44B28F8F0279FD7035C3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 0.8

    show rs_image_533AAAC44B2D41CB82225B285E277639 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6EBDB8D5A1AD4DF082F5B765D83DE7CD as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at center_top zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    show rs_image_06FBA0115C924EB89765D7CAFA0D532E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1FB04C4573E84E4DAF670EB9FD7BD6C6 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_2E15079D93F042638344B24315ECF18B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    show rs_image_AD98FF52060B467081E8E309526CF300 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1E452D70E5C547059D37DC526E22F054 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 0.8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_422CEAA0768946AF8E1A713B2CB845CF as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    show rs_image_06FBA0115C924EB89765D7CAFA0D532E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F800B17A2FA64BEBA751423EA81301AE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E4EBFCBF8642432D983EFD32ED4B980B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 1.2

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    # Gallery unlock: images/CG/Prelife-memory/Prelife-memory 4.png
    $ zorder_rs_image_7C1396F883A044398410DB50945F5D1D = -100
    show rs_image_7C1396F883A044398410DB50945F5D1D as rs_image_7C1396F883A044398410DB50945F5D1D zorder zorder_rs_image_7C1396F883A044398410DB50945F5D1D onlayer master
    hide rs_image_7C1396F883A044398410DB50945F5D1D

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_7C1396F883A044398410DB50945F5D1D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_DEF4707300154D00B22225E4F8282BA7

    pause 0.5

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你……你们闹完了没！！给我知耻！"

    rs_character_06E99199BFCE4C93B1F3942F0090429B "切……走了。"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "嗯嗯。"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "哦。"

    window hide

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_A2F5530406854E5098F52F72EE26DA66

    window show

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_2E3CEC31B39D4B77A97E2C2B10BD534E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哈……哈……"

    show rs_image_F800B17A2FA64BEBA751423EA81301AE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……{w}原来……{w=0.4}是这样的心情。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶……"

    show rs_image_81CF27D906FA4867BCAEC4C85AAC1840 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……果然，不作出改变的话是不行的。"

    show rs_image_06FBA0115C924EB89765D7CAFA0D532E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "改变……。"

    window hide

    pause 0.5

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 3

    stop music fadeout 3
    $ sys_music_current_file = ""

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    pause 2.5


    if judge_lm_condition([]):
        jump block_00003911

    return

label block_00003911:
    # Node: 00003911 (久遠回憶 2)
    $ set_window("チャット画面")
    window show

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Type 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Type 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Type 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#800080}flower 你好呀♪今天学校也辛苦了哦！┌(┌＾o＾)┐{/color}{w}\n{color=#F9CE1D}YUU 辛苦了。{/color}{w}\n{color=#800080}flower 今天也累坏了(´・ω・｀)\n啊啊——现在的班里好想要一个关系好的啊——( ｣´0｀)\n还要等暑假也太远了……｣{/color}{w}\n{color=#F9CE1D}YUU 你那边也是吗，我这边也……{/color}{w}\n{color=#800080}flower 真的假的，双方都不好过呐——(´・ω・｀)\n不过我这只是个人问题，这么说有点不合适不过(^q^)\n你那边怎么了？？{/color}{w}\n{color=#F9CE1D}YUU 有点……呜呜(T ^ T){/color}{w}\n{color=#800080}flower 来谈谈(｀・ω・´){/color}"

    window hide

    pause 0.8

    window show

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Type 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Type 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Type 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#800080}flower 这很麻烦啊(´；ω；｀){/color}{w}\n{color=#F9CE1D}YUU 能听我说真是太好了，轻松了一点……{/color}{w}\n{color=#800080}flower 没事没事～\n我也是有点担心的呐～最近总觉得你有些沮丧。\n不过说起来真是些不知轻重的人（｀Δ´）\n简直不敢相信！{/color}{w}\n{color=#F9CE1D}YUU 谢谢(>_<)\n不过，作为我唯一的同伴的那个孩子\n说了“不改变不行”这样的话……{/color}{w}\n{color=#800080}flower 不改变不行……嗯嗯，\n确实是呐。我也是，你也是，\n也许必须要做点什么才好。{/color}{w}\n{color=#F9CE1D}YUU 可就算这么说(>_<){/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#800080}flower 本来还想多说点的，必须要去给店里帮忙了！{/color}{w}\n{color=#F9CE1D}YUU 好的！一直麻烦你了。下次再见！{/color}{w}\n{color=#800080}flower 哦！(｀・ω・´)\n接下来怎么做下次一起想想(｀・ω・´)\n下次见！{/color}"

    window hide

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    pause 0.8

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DB5AB8A1EA534F3F81A68748DB089DF3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 0.5

    window show

    if sys_music_current_file != "sound/BGM/My precious time of now - piano.ogg":
        play music "sound/BGM/My precious time of now - piano.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time of now - piano.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "改变……行动……怎么做才好……"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Bell 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Bell 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Bell 2.ogg"

    extend "叮"

    show rs_image_39BA5B8CF114437EB5FCE26D91B9FAD5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……来了。"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_1FDBD6D1D5174051A58C39DDF42F0F8C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友，是我。"

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    show rs_image_1FDBD6D1D5174051A58C39DDF42F0F8C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_1503A55409E04E4282A40803C56C9FEC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "晚上好。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_39BA5B8CF114437EB5FCE26D91B9FAD5 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "晚上好，怎么了——？"

    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不，没什么特别的……。{w}\n{nw}"
    show rs_image_7E08762184A342409082DE4098B70327 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……{w=0.4}{nw}"
    show rs_image_1503A55409E04E4282A40803C56C9FEC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "又在玩电脑了。"

    show rs_image_5B9CC9E962834DFAA482CD64983036AE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没……没什么关系嘛。我做什么都和忍无关……"

    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯……是啊，确实是。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"

    show rs_image_297D12A37B1F462D8B77493FEF02B193 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "梅雨季能快点过去就好了呐。你很不喜欢下雨的。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……"

    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"
    show rs_image_EF29254D67B448F48CD5987CB3746ED7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "我啊，想要学一些什么，想要转换心情。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "所以，今年夏天可能不怎么有时间玩了……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……欸。“转换心情”，加油哦……"

    show rs_image_297D12A37B1F462D8B77493FEF02B193 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……“转换心情”的意思是，换一个新的心情继续努力。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是这样……"

    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……{w=0.5}{nw}"
    show rs_image_297D12A37B1F462D8B77493FEF02B193 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "友也做点什么转换一下心情如何？{w}\n看，比如钢琴，最近不是都没在弹吗？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……不过，没关系的，又不有趣。"

    show rs_image_1503A55409E04E4282A40803C56C9FEC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "为什么？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "为什么……{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_D66809B07DBB47B58D9A2808822498AA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7CFC2D3570394463AE9EB2953AC6BE86 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那种事你早就知道了！"

    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊……嗯，是呢……{w=0.5}抱歉。{w=0.3}{nw}"
    show rs_image_10B254E7FCA4400BB4718D5FF0E43860 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend ""

    show rs_image_06FBA0115C924EB89765D7CAFA0D532E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……今天的晚饭，要怎么办？来我家？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……不，我自己做………"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哦……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    window hide

    pause 1.5

    $ set_window("チャット画面")
    window show

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Type 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Type 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Type 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#F9CE1D}……\n……\n……\nYUU 所以，难得的暑假，我也想转换心情重新开始。{/color}{w}\n{color=#800080}flower 转换心情重新开始，\n好奇怪的词（；￣ェ￣）\n不过这样没关系吗？不告诉双亲和老师？{/color}{w}\n{color=#F9CE1D}YUU 没事……大概(^_^;)\n毕竟，除此之外也没有方法了。\n否则以后会一直被这样说的(Ｔ＿Ｔ){/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#800080}flower 是嘛～嗯，这样啊。\n嘛，我认为只要想做就可以去做哦(｡･ ω<)\n真的失败的话，就等失败的时候再考虑！{/color}"

    if sys_effect_current_file != "sound/Effect Sound/Type 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Type 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Type 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#F9CE1D}YUU 啊——啊，等新学期来时不好好谢谢他的话……{/color}{w}\n{color=#800080}flower 嗯嗯？谁？{/color}{w}\n{color=#F9CE1D}YUU 朋友哦！(>_<)\n受到照顾了嘛……{/color}{w}\n{color=#800080}flower 是嘛是嘛。一直都备受关照嘛……(´-ω-`)\n能向好的方向转变就好了呐♪{/color}{w}\n{color=#F9CE1D}YUU 嗯！{/color}"

    window hide

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    pause 0.8

    $ set_window("イベントモード")
    pause 0.5

    window show

    stop music fadeout 2
    $ sys_music_current_file = ""

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "再也不会……让你们说出那样的话了……"

    window hide

    pause 3

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_D66809B07DBB47B58D9A2808822498AA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……友……？{w}你的头发……是……？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_FD01F3E88C664E1B84ED75FA573BF2E1 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈……我也想改变什么哦。怎么样？合适吗……？"

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_music_current_file != "sound/BGM/My precious time.ogg":
        play music "sound/BGM/My precious time.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time.ogg"

    pause 0.7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……{w}不{w=0.2}敢{w=0.2}相{w=0.2}信{w=0.2}…{w=0.2}…{w=0.2}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？"

    window hide

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    # Gallery unlock: images/CG/Prelife-memory/Prelife-memory 5.png
    $ zorder_rs_image_AC590944081A4E0C9EC81899E9209C85 = -100
    show rs_image_AC590944081A4E0C9EC81899E9209C85 as rs_image_AC590944081A4E0C9EC81899E9209C85 zorder zorder_rs_image_AC590944081A4E0C9EC81899E9209C85 onlayer master
    hide rs_image_AC590944081A4E0C9EC81899E9209C85

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_AC590944081A4E0C9EC81899E9209C85 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.5

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "居然会染成那样！简直就和逆濑一样！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "为什么！？要像那样成为不良！？\n为什么！？友也想成为他们那样的人！？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不、不是的！我只是……{w=0.2}我只是想转换心情……！"

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "怎么不是了，不就是想要加入他们，\n不就是想要成为他们的一员么！？"

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我之前对你说的才不是这个意思！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不……等等……听我解释……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不良什么的最差劲了！我从心底里……\n{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    # Gallery unlock: images/CG/Prelife-memory/Prelife-memory 5.png
    $ zorder_rs_image_AC590944081A4E0C9EC81899E9209C85 = -100
    show rs_image_AC590944081A4E0C9EC81899E9209C85 as rs_image_AC590944081A4E0C9EC81899E9209C85 zorder zorder_rs_image_AC590944081A4E0C9EC81899E9209C85 onlayer master
    hide rs_image_AC590944081A4E0C9EC81899E9209C85

    show rs_image_AC590944081A4E0C9EC81899E9209C85 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    extend "{color=#AA0055}鄙视他们！！{/color}我才不会输给你这种人！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我走了，快要开始练习了。\n{w=1}我……{w}我不会再把友当朋友了。"

    window hide

    pause 0.5

    # Gallery unlock: images/CG/Prelife-memory/Prelife-memory 6.png
    $ zorder_rs_image_F7C5F4C539224DA08E60CF859D14D0B7 = -100
    show rs_image_F7C5F4C539224DA08E60CF859D14D0B7 as rs_image_F7C5F4C539224DA08E60CF859D14D0B7 zorder zorder_rs_image_F7C5F4C539224DA08E60CF859D14D0B7 onlayer master
    hide rs_image_F7C5F4C539224DA08E60CF859D14D0B7

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_F7C5F4C539224DA08E60CF859D14D0B7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_354DFEA941CB402F9AA73F6072D895B3

    pause 0.5

    window show

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "等……等等……不……我、我……为什么连忍都……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎么……会是……这……呜……不……呜……{w}\n{nw}"
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    extend "呜哇啊啊啊啊啊啊啊啊啊啊啊啊啊！！！！"

    window hide

    pause 0.8

    show center_title (_("全都错了，一定从最开始什么都错了……")) as center_title zorder 1000
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 3.5

    show center_title (_("那个时候，如果能一笑了之……\n那个时候，如果能试着融入当时的气氛……")) as center_title zorder 1000
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 5

    show center_title (_("就一定不会有这样的……")) as center_title zorder 1000
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 2.5

    hide center_title
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    window hide

    $ set_window("イベントモード")
    pause 3.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_47F13A8A6643413691290FE8226AE77C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    if sys_music_current_file != "sound/BGM/My precious time - slowly.ogg":
        play music "sound/BGM/My precious time - slowly.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time - slowly.ogg"

    pause 0.6

    window show

    pause 0.3

    rs_character_70D192FC6EC641EB9F15466FD277C78A "早上好，忍酱。天气变暖和了呐。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "啊啦，今天一个人？友酱呢？"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不知道……"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "啊啦……是吗……"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "说起来，之前看到有个金发的孩子走进了忍酱住的公寓，\n是有那样的孩子对不对？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "真是的，小小年纪就学坏了。\n把头发染成那德行，真想看看他们父母长什么样。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "忍酱可绝对不能变成那样哦！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……当然。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "也告诉友酱要小心哦。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    window hide

    pause 0.7

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_52A4FB95B188448396BFCDB678787F82 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_DB13F96B3ED24A30A4BC2818B33F6208 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "果然还是……不去上学了……"

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window hide

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E4EBFCBF8642432D983EFD32ED4B980B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    window show

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "早啊，绫濑酱～♪今天也很可爱呐"
    if sys_effect2_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_E4EBFCBF8642432D983EFD32ED4B980B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    extend "……呜哇！？"
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_881AD062F59342BC8ACF7BD08BA526C2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这是最后忠告，不要加“酱”了。"

    rs_character_EEA3F27AEC2B46E082EB2D2B190F32C5 "好……好吓人～……"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "你这不讲道理的家伙！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_881AD062F59342BC8ACF7BD08BA526C2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哈？"

    rs_character_F9A5472F1C134BB28526F3F596DD3783 "唔……"

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    show rs_image_93274A5024EC4DB48BC9078403E617D2 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at left_top zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_06E99199BFCE4C93B1F3942F0090429B "停下，别惹我们。否则会让你吃不了兜着走的。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    window hide

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_52A4FB95B188448396BFCDB678787F82 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    if sys_effect_current_file != "sound/Effect Sound/Type 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Type 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Type 1.ogg"

    pause 0.8

    show rs_image_B444FDE4EF1A43E5A2345A44A71061D5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 0.8

    window show

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_373D1DEFBDED426F9EA9055A42E13627 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "果然不在……这个时间，大家都去上学了。"

    show rs_image_0285159DADE74D2C81EB978C7868CCAB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊……说不定之前知道的聊天室里会有人……"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_B97A3992A1D24282B85B44E0C876F034 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_3B6B863A23084F9EA6BFCF3703A3D9F7

    pause 0.6

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "总之试试也好（；￣ェ￣）{w}\n但其实说过很多遍了，我并不推荐。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "那边年龄层有点太高了……(｡-_-｡){w}\n{color=#FF8080}http://st～～～～{/color}"

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_354DFEA941CB402F9AA73F6072D895B3

    stop music fadeout 1
    $ sys_music_current_file = ""

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Type 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Type 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Type 1.ogg"

    pause 2

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{w=0.3}你{w=0.5}好。"

    window hide

    pause 3

    stop effect fadeout 0.4
    $ sys_effect_current_file = ""

    if sys_effect3_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_47F13A8A6643413691290FE8226AE77C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 0.5

    window show

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F800B17A2FA64BEBA751423EA81301AE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    show rs_image_9431D76633F74814B919EB09BC8959B3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊……你好。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "……下午好，忍酱。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "…………最近一直一个人呐，友酱不会是生病了？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……嗯。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "这样……也许是冷战……{w}\n嗯。这种事情不想多说的，抱歉。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "没关系……"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "啊，对了对了，说起来啊。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "之前说起的那个金发的孩子，\n你们去学校后他好像从公寓里出来了。"

    show rs_image_1503A55409E04E4282A40803C56C9FEC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哦……{w=0.3}经常看到？"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "是呐，最近经常看到，那个金发还是很引人注意的。"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "连学校也不好好去，真是恶劣。{w}\n肯定是地痞无赖的孩子。{w=0.2}{nw}"
    show rs_image_D66809B07DBB47B58D9A2808822498AA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend ""

    show rs_image_81CF27D906FA4867BCAEC4C85AAC1840 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……那个是……"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "啊啦？怎么了？"

    show rs_image_F800B17A2FA64BEBA751423EA81301AE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……没什么。"

    stop effect3 fadeout 1
    $ sys_effect3_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    window hide

    pause 1

    if sys_effect3_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A58F18DC23404B0FABA813677A0C68F9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.7

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_6B7494753B654BB1B96759DFC910974D as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，不好……"

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 1

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 = 300
    show rs_image_AD98FF52060B467081E8E309526CF300 as tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 at right_top zorder zorder_tag_2E1D5DC8F2184C56BA3702E2A2AB70E9 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 1.4

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_2E1D5DC8F2184C56BA3702E2A2AB70E9
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_D370CF33D37B4618AEC0EFED26094DBC as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    pause 0.7

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_D370CF33D37B4618AEC0EFED26094DBC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_DC039D54F9D346AEB7704BE8E71E9665 "嗯？认识的人？"

    show rs_image_373D1DEFBDED426F9EA9055A42E13627 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……同班的。不过，没关系的，不会暴露的。"

    rs_character_DC039D54F9D346AEB7704BE8E71E9665 "是嘛。不过如果真的遇到了，说是父亲就好了哦？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那个人知道我家是母子家庭。"

    rs_character_DC039D54F9D346AEB7704BE8E71E9665 "这就不行了啊。"
    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    extend "不过，那孩子也很可爱呐。\n和{color=#F9CE1D}优{/color}一样，是金发呢。"

    show rs_image_DB13F96B3ED24A30A4BC2818B33F6208 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……只有那家伙我不想和他比较。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_DC039D54F9D346AEB7704BE8E71E9665 "哦，吃醋了？没关系！不管怎么说优都是最可爱的哦。"

    show rs_image_35BC7AA517BD4D7FBDBA70627A2C11FB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不……不是。不是那个意思……"

    stop effect3 fadeout 2.5
    $ sys_effect3_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    rs_character_DC039D54F9D346AEB7704BE8E71E9665 "优……今天会比平时更厉害哦。\n准备了更多会让优舒服的东西哦。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊……唔……{w=1.5}{color=#C0C0C0}嗯{/color}{w=1}{color=#C0C0C0}，好……{/color}"

    window hide

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    if sys_music_current_file != "sound/BGM/My precious time.ogg":
        play music "sound/BGM/My precious time.ogg" loop
        $ sys_music_current_file = "sound/BGM/My precious time.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_52A4FB95B188448396BFCDB678787F82 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    if sys_effect2_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open door 1.ogg"

    pause 0.8

    show rs_image_F8080354DC2B48FEBAE5605900B5200A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    pause 0.8

    show rs_image_B444FDE4EF1A43E5A2345A44A71061D5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_2E15079D93F042638344B24315ECF18B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    window show

    pause 0.4

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "（也许我从一开始就误解了……）"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Type 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Type 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Type 2.ogg"

    show rs_image_B444FDE4EF1A43E5A2345A44A71061D5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 3

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    window show

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_81CF27D906FA4867BCAEC4C85AAC1840 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……！……果然，这都是我的错。友才不会和那些家伙……！"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    window hide

    $ set_window("チャット画面")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#800080}flower 请问……在不在～？？（；￣ェ￣）{/color}"

    window hide

    $ set_window("イベントモード")
    window show

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_B444FDE4EF1A43E5A2345A44A71061D5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D66809B07DBB47B58D9A2808822498AA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "谁啊……这是。"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    window hide

    $ set_window("チャット画面")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#F9CE1D}YUU 你好。{/color}{w}\n{color=#800080}flower 啊，在啊～(*ﾟ∀ﾟ*)\n太好了，我很担心的哦。\n刚才我看到聊天室上面的公告了哦～(;´д｀){/color}{w}\n{color=#800080}你正在交谈的那个人，好像是做网路一次性援交的，\n千万不要继续交谈了！！{/color}{w}\n{color=#800080}网站已经因为这个闹起来了，\n总之没事就好～(￣◇￣;){/color}"

    window hide

    $ set_window("イベントモード")
    window show

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_B444FDE4EF1A43E5A2345A44A71061D5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_D66809B07DBB47B58D9A2808822498AA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "诶，这是什么……？网路……？"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    window hide

    $ set_window("チャット画面")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#F9CE1D}YUU 抱歉，我是这个叫做“YUU”的人的朋友。{/color}{w}\n{color=#800080}flower 欸(°д°){/color}{w}\n{color=#F9CE1D}YUU 不好意思，请详细说说刚才的事。\n就是说，我的朋友遇到危险了？{/color}{w}\n{color=#800080}flower 那个……总之，我就直说了。\n你的朋友在聊天室和某个有性犯罪前科的人……{/color}{w}\n{nw}"
    stop music fadeout 3
    $ sys_music_current_file = ""

    extend "{color=#800080}……\n……\n……{/color}"

    window hide

    $ set_window("イベントモード")
    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_52A4FB95B188448396BFCDB678787F82 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.2

    show rs_image_5013EC64CA634A9E9754EF6FE927CCD2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.2

    show rs_image_78D7BAB745054155A67D88CE45047FD7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.2

    show rs_image_E4EBFCBF8642432D983EFD32ED4B980B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.6

    show rs_image_47F13A8A6643413691290FE8226AE77C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    window show

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_2E15079D93F042638344B24315ECF18B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友！友！？在的话回答我！？"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_47F13A8A6643413691290FE8226AE77C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_70D192FC6EC641EB9F15466FD277C78A "忍酱，怎么了？这么慌。"

    show rs_image_F800B17A2FA64BEBA751423EA81301AE as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "中岛阿姨！友！那个金发的孩子在什么地方！？"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "金发的男孩子？那个孩子的话，上午朝车站走过去了。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "非常感谢！！"

    rs_character_70D192FC6EC641EB9F15466FD277C78A "等、等等！那个孩子和友什么关系？"

    if sys_effect3_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "{size=24}他就是森海友！！！{/size}"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_70D192FC6EC641EB9F15466FD277C78A "欸欸欸欸！？！？"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    window hide

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A58F18DC23404B0FABA813677A0C68F9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.6

    window show

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_DC039D54F9D346AEB7704BE8E71E9665 "来，上车♪"

    rs_character_DC039D54F9D346AEB7704BE8E71E9665 "今天要去远一点的地方，和往常一样找一家好的酒店♪"

    rs_character_DC039D54F9D346AEB7704BE8E71E9665 "肯定也会让优觉得舒服的♪"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_35BC7AA517BD4D7FBDBA70627A2C11FB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶，这、这个我还是第一次听说……"

    rs_character_DC039D54F9D346AEB7704BE8E71E9665 "当然了～太早吐露的话不就没那么高兴了嘛？\n既然如此，当然要保密。"

    show rs_image_373D1DEFBDED426F9EA9055A42E13627 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可……这么着急的话，先让我准备……"

    rs_character_DC039D54F9D346AEB7704BE8E71E9665 "没关系，快点上车。"

    show rs_image_DB13F96B3ED24A30A4BC2818B33F6208 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……可是……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_2E3CEC31B39D4B77A97E2C2B10BD534E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友！！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_6B7494753B654BB1B96759DFC910974D as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍！！？"

    rs_character_DC039D54F9D346AEB7704BE8E71E9665 "你、你谁啊！？小姐姐就请先一边去……"

    if sys_effect_current_file != "sound/Effect Sound/Battle 4.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 4.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 4.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我是……{w=0.5}{size=32}男人啊啊啊！！！{/size}"

    window hide

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if sys_effect2_current_file != "sound/Effect Sound/Battle 5.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_4D8F1D6A70C24A34A3E6C37B69619470 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    if sys_effect_current_file != "sound/Effect Sound/Battle 5.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_E04DFA4059EE40D18051F1CAA5223C75 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    if sys_effect2_current_file != "sound/Effect Sound/Battle 5.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_51451FBF94C8444AA5696178E72CE210 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Battle 6.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 6.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 6.ogg"

    show rs_image_46726D80EC7B4D48AD2EFED4CDD37F1C as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 1.5

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.4

    window show

    if sys_effect_current_file != "sound/Effect Sound/Hit 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DC039D54F9D346AEB7704BE8E71E9665 "呜哇！！"

    if sys_effect2_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Fall down 1.ogg"

    show rs_image_A58F18DC23404B0FABA813677A0C68F9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    pause 0.4

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_D370CF33D37B4618AEC0EFED26094DBC as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍……为、为什么……？"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_2E3CEC31B39D4B77A97E2C2B10BD534E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "问了你电脑里的那个朋友，说是友遇到了危险。"

    show rs_image_DB13F96B3ED24A30A4BC2818B33F6208 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "因为……忍已经讨厌我了……那我还有什么……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_2E15079D93F042638344B24315ECF18B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "没有这回事！！！\n我们绝对会一直在一起！！就那点事不会分开的！！"

    show rs_image_81CF27D906FA4867BCAEC4C85AAC1840 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我明明这么了解友，却仅仅因为外表而逃开，真的很对不起！{w}\n让友孤独一人……抱歉！！"

    show rs_image_373D1DEFBDED426F9EA9055A42E13627 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍……我们、还能……{w=1}做朋友……？"

    pause 0.1

    show rs_image_297D12A37B1F462D8B77493FEF02B193 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "毋庸置疑！以后就由我来守护友！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "就像今天这样，真的发生什么的话，友的身边，我一定会时常伴随。"

    show rs_image_D370CF33D37B4618AEC0EFED26094DBC as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍……"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    # Gallery unlock: images/CG/Prelife-memory/Prelife-memory 7.png
    $ zorder_rs_image_E05FE25C588740B4A48960064ACFC99B = -100
    show rs_image_E05FE25C588740B4A48960064ACFC99B as rs_image_E05FE25C588740B4A48960064ACFC99B zorder zorder_rs_image_E05FE25C588740B4A48960064ACFC99B onlayer master
    hide rs_image_E05FE25C588740B4A48960064ACFC99B

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_E05FE25C588740B4A48960064ACFC99B as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_222BBB56F7BA4025B3E942F40786CBC9

    pause 0.5

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍～！！{w}\n我再也没有必要、再也不会像今天这样做了！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "只要忍在，绝对不会寂寞的～！！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "友……！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍！！"

    window hide

    pause 1

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 0.8

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_A58F18DC23404B0FABA813677A0C68F9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_297D12A37B1F462D8B77493FEF02B193 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.5

    window show

    pause 0.3

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那……回家了，友，趁这个大叔还没起来。{w}\n中岛阿姨也很担心你的。"

    window hide

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_78D7BAB745054155A67D88CE45047FD7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_0285159DADE74D2C81EB978C7868CCAB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_297D12A37B1F462D8B77493FEF02B193 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……说起来，最近没和由实阿姨打过招呼呐。{w}\n{nw}"
    show rs_image_373D1DEFBDED426F9EA9055A42E13627 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "这个发色肯定会吓一跳的。"

    show rs_image_C28E1FB4E07A4A46A8C0108E4FB0E11D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "会吃惊但也不用那么担心。友就是友，挺直脊背就可以了。"

    show rs_image_FD01F3E88C664E1B84ED75FA573BF2E1 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……！{w=0.4}{nw}"
    show rs_image_A622B9FF12254675ABE89C40A4E124A5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "嗯，说得对！"

    show rs_image_F95D78AB70A24C2EA6510C7D02BE40E8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "说起来，忍，刚才好厉害呐。最近开始学的东西是空手道？"

    show rs_image_EF29254D67B448F48CD5987CB3746ED7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯。{w}……因为憧憬《东斗神拳》。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_A622B9FF12254675ABE89C40A4E124A5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好厉害——！！那是不是身上也全都是肌肉呢！？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "运动会的时候肯定很引人注目的！好期待哦～♪\n{nw}"
    show rs_image_D66809B07DBB47B58D9A2808822498AA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "！{w=0.4}{nw}"
    show rs_image_297D12A37B1F462D8B77493FEF02B193 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……不会那样的。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "再说了，等到修学旅行的时候，\n反倒会是友更受注目哦？就因为你那脑袋。"

    window hide

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 3.5

    $ set_window("チャット画面")
    window show

    if sys_effect_current_file != "sound/Effect Sound/Type 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Type 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Type 1.ogg"

    if sys_music_current_file != "sound/BGM/The end of touch.ogg":
        play music "sound/BGM/The end of touch.ogg" loop
        $ sys_music_current_file = "sound/BGM/The end of touch.ogg"

    pause 0.5

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#F9CE1D}……\n……\n……\nYUU 综上所述，已经不需要了。{/color}{w}\n{color=#800080}flower 是嘛——(´；ω；｀)\n能无事结束真是太好了。\n你真的有一位很棒的朋友呐。{/color}{w}\n{color=#F9CE1D}YUU O(∩_∩)O♪令我自豪的朋友哦♪{/color}{w}\n{color=#800080}flower 不错嘛不错嘛～！我也一定要在中学成功出道，\n获得越来越多的朋友哦・゜・(ノД`)・゜・{/color}{w}\n{color=#F9CE1D}YUU 嗯！啊，稍等。{/color}"

    window hide

    stop effect fadeout 0.5
    $ sys_effect_current_file = ""

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_DB5AB8A1EA534F3F81A68748DB089DF3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.4

    window show

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_A622B9FF12254675ABE89C40A4E124A5 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍～！有什么想对flower君说的话吗～？"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_7E08762184A342409082DE4098B70327 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我家的友蒙受你们照顾了——就这么说。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_35BC7AA517BD4D7FBDBA70627A2C11FB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "你是家长啊！什么嘛，那个……"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    $ set_window("チャット画面")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#F9CE1D}YUU 朋友说“我家的友蒙受你们照顾了”这样的( ´△｀){/color}{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    extend "{color=#800080}flower 他是家长啊ヾ(´・ω・｀){/color}"

    window hide

    $ set_window("イベントモード")
    window show

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_DB5AB8A1EA534F3F81A68748DB089DF3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_A622B9FF12254675ABE89C40A4E124A5 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1503A55409E04E4282A40803C56C9FEC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊哈哈♪说了同样的话呐——！"

    show rs_image_297D12A37B1F462D8B77493FEF02B193 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "感觉会是和友很相似的孩子呢。\n两人如果真的相遇的话，肯定会成为好朋友的。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "我也这么觉得哦——"

    show rs_image_2BD29A41939B4CF6BC5B8378F39DCC86 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好了，既然再见也说了，{w}\n{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "忍！买东西去！！"

    show rs_image_7E08762184A342409082DE4098B70327 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "现在？太晚了。要是没东西可吃就来我家。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_A622B9FF12254675ABE89C40A4E124A5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "今天是纪念日！！{w}\n{nw}"
    show rs_image_D66809B07DBB47B58D9A2808822498AA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "我和忍重归于好的纪念日！！"

    show rs_image_EF29254D67B448F48CD5987CB3746ED7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "所以我要做很多好吃的东西，好好款待忍哦♪"

    show rs_image_297D12A37B1F462D8B77493FEF02B193 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "明白了，那我也来帮忙。"

    show rs_image_2BD29A41939B4CF6BC5B8378F39DCC86 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！拜托了♪那么走了！"

    window hide

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    show rs_image_1FDBD6D1D5174051A58C39DDF42F0F8C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    pause 3

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_8C818451D3534586ADE16DBAE08932F5

    pause 2

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，说起来是今天呐！"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_BA68039D702C4EA2A6CF95AF1F2E9D2E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "纪念日。"

    show rs_image_0F46590E67454A75B03975CF59479626 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦，不愧是忍！好好记着呐！"

    show rs_image_7780BD482A234B81970D2A4B4EE70A97 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……毕竟发生了很多事。"

    show rs_image_3F2B220CD95B4BC6AAD59B3FE6C7DF0B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是呐，也明白了忍的饭究竟做得多么糟。"

    show rs_image_4837F6B6AF604F54BF6339BCB1FFAFEA as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不……不用你管。"

    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "逆濑后来很快就又转校了。{w}\n{nw}"
    show rs_image_8A80B90628C143D1B3A53C71240BBE2D as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "虽说那些事才刚刚开始，但因为那家伙不在也就没有下文了。"

    show rs_image_3F2B220CD95B4BC6AAD59B3FE6C7DF0B as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……不过啊，正因为有了那些事才会有现在的自己。\n这么想的话会不会轻松一点呢……"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_3F533DA3CF494DEBA1146743852331E9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不，是不是有点思维发散过头了？"

    show rs_image_C66A56F89C43490FBD87D2164FFD98A5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "没什么不好，那种思考方式。{w}……友，差不多该走了。"

    show rs_image_8DB9EBBA116648CAAA85C0A0F67B04D2 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶？出门？去什么地方？"

    if sys_music_current_file != "sound/Piano/sti_gymno_01_pi.ogg":
        play music "sound/Piano/sti_gymno_01_pi.ogg" loop
        $ sys_music_current_file = "sound/Piano/sti_gymno_01_pi.ogg"

    show rs_image_04B589B0BDD948F4BB727589A05C0593 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不是纪念日么？我以为友想要好好招待我才特地一起放学过来的呢。"

    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……嗯♪当然！买东西去了！"

    show rs_image_C66A56F89C43490FBD87D2164FFD98A5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯。"

    window hide

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    # Original value is 400, but will bliock scb_flag_title_end, so I change it to 0 and reset that after call
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    call scb_flag_title_end(1, _("「久远回忆」"), "rs_image_EAA2AFC1658347D38884AD39C0C5F1B7", True) from _call_scb_flag_title_end_12

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400

    if judge_lm_condition([]):
        jump block_00003913

    return

label block_00003913:
    # Node: 00003913 (Phase: 0)
    $ C1S5Phase = 0
    if Chapter <> 1:
        $ del C1S5Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_00003915
    if judge_lm_condition([]):
        jump block_00003912

    return

label block_00003915:
    # Node: 00003915 ()

    return

label block_00003912:
    # Node: 00003912 (FINISH)
    $ C1S5 = True
    $ TalkShinobuF5After = True
    $ F5Check1 = False

    if judge_lm_condition([]):
        jump block_0000391F

    return

label block_0000391F:
    # Node: 0000391F (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_15

    if judge_lm_condition([]):
        jump block_00003915

    return

