# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003EA0 (FLAG: 學園怪談)

label block_00003EA1:
    # Node: 00003EA1 ()

    if judge_lm_condition([]):
        jump block_00003EA8

    return

label block_00003EA8:
    # Node: 00003EA8 (Phase: 99)
    if Not(VarExists("C3S5Phase")):
        $ C3S5Phase = 0
    $ C3S5Phase = 99

    if judge_lm_condition([]):
        jump block_00003EA3

    return

label block_00003EA3:
    # Node: 00003EA3 (F5 START)
    call scb_flag_title(3, _("「学园怪谈」")) from _call_scb_flag_title_11

    if judge_lm_condition([]):
        jump block_00003EA6

    return

label block_00003EA6:
    # Node: 00003EA6 (學園怪談 1)
    $ set_window("イベントモード")
    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 2

    show rs_image_A37C8EF97F3840A491FC4D8F8FC7F280 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 1.5

    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 1.6

    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2.5

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 2.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 3.ogg"

    show rs_image_6F41BEB29B0744ED8F25360004E87AB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    pause 2

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 2.ogg"

    show rs_image_104D8871C298423C8D21AE9E1802FF43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show rs_image_BCAC5076DD214C629BDF5B88F585E30E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 2.ogg"

    show rs_image_802FEF2577C54DDA8193A6CA90A73DA7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_6F41BEB29B0744ED8F25360004E87AB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Thunder 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Thunder 1.ogg"

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 200
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    if sys_music_current_file != "sound/BGM/Monster 1.ogg":
        play music "sound/BGM/Monster 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Monster 1.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}终于自由了啊啊啊啊！！！{/size}"

    window hide

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_A7EEAA961C214874BEBADA168E79984E = 300
    show rs_image_BF15F042F4A241789DDE485A5CD928DE as tag_A7EEAA961C214874BEBADA168E79984E at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A7EEAA961C214874BEBADA168E79984E onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 300
    show rs_image_562CBE7FE74549F0894E5ADA22F9A4DA as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 1

    hide tag_A7EEAA961C214874BEBADA168E79984E
    hide tag_82C54ADE966440F7B34C83D13555B813
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 300
    show rs_image_757537DAAA5F421595F24FFD01860C20 as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.5

    window show

    rs_character_E8A540AA00B04A0D9E7C365A0C741280 "令人怀念的校舍啊，我们在此聚集……终于回来了，御咲学园！！！"

    show rs_image_052F34847F0D47A8B9559273E4FAA7C6 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "被关在那种黑暗狭小的箱子里，无趣，无趣，还不如死了舒服。"

    show rs_image_9B664D5A09A14B7D83F83FD0EEE7A1F0 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "但那也是遥不可及的愿望……\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_757537DAAA5F421595F24FFD01860C20 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "要说为什么的话，我们已经死了！"

    show rs_image_562CBE7FE74549F0894E5ADA22F9A4DA as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "可是！！多亏不知某个笨蛋解开了封印，我们终于重获自由了！！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_757537DAAA5F421595F24FFD01860C20 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "伙伴！！！接下来怎么做！？怎么做！？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_F92377E933F7492EB64FE63A7C4764D3 "当然是一扫这股犹豫了。那么，什么时候开始？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_A7EEAA961C214874BEBADA168E79984E = 300
    show rs_image_BF15F042F4A241789DDE485A5CD928DE as tag_A7EEAA961C214874BEBADA168E79984E at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A7EEAA961C214874BEBADA168E79984E onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_0DB98FCA95C84A20810A95417C182A61 "………"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_A672631E2B514DA2B6388CDF6C0BD900 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "你！！这里应该说“现在就做！”才对！真是的，没兴致～"

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "他因为封印较弱比我们早几天出来，已经不会为此等小事感动了嘛。\n真羡慕。"

    show rs_image_757537DAAA5F421595F24FFD01860C20 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "那也只是早一晚！！你就好好看清自己把猎物给我们。"

    show rs_image_175B061199E04D9EB2CB6F9FA9279C56 as tag_A7EEAA961C214874BEBADA168E79984E zorder zorder_tag_A7EEAA961C214874BEBADA168E79984E onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D21FC549273B4A1ABB90AEF39DEAD87B "……无所谓，我的目标只有那孩子……"

    window hide

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_A7EEAA961C214874BEBADA168E79984E
    hide tag_82C54ADE966440F7B34C83D13555B813
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 300
    show rs_image_A672631E2B514DA2B6388CDF6C0BD900 as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_757537DAAA5F421595F24FFD01860C20 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_079949A107134E47B24110C78D2FA0CF "集合，同志们！再次取回我们应得的荣光！\n想在朝思暮想的乐园里快活吗！！！"

    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}哦哦哦哦哦哦！！！！{/size}"

    window hide

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_C1F0041794544D71B07C91EE20FC49B6 = 300
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_C1F0041794544D71B07C91EE20FC49B6 at left_top zorder zorder_tag_C1F0041794544D71B07C91EE20FC49B6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.05

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_A9C25AA9ADF244498299ED6338BC9B6A = 300
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_A9C25AA9ADF244498299ED6338BC9B6A at Transform(xpos=450, yalign=0.0) zorder zorder_tag_A9C25AA9ADF244498299ED6338BC9B6A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.05

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_9A2F0FC4EAF04544A204C360327C8E59 = 300
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_9A2F0FC4EAF04544A204C360327C8E59 at center_top zorder zorder_tag_9A2F0FC4EAF04544A204C360327C8E59 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.05

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_8849E9F5C5E044E3AAACB5D6D7EF2CE8 = 300
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_8849E9F5C5E044E3AAACB5D6D7EF2CE8 at Transform(xpos=-150, yalign=0.0) zorder zorder_tag_8849E9F5C5E044E3AAACB5D6D7EF2CE8 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.05

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_2C45FF10AF2D49B9A109BA34FD33D1F4 = 300
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_2C45FF10AF2D49B9A109BA34FD33D1F4 at Transform(xpos=300, yalign=0.0) zorder zorder_tag_2C45FF10AF2D49B9A109BA34FD33D1F4 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Thunder 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Thunder 1.ogg"

    $ zorder_tag_A7EEAA961C214874BEBADA168E79984E = 400
    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 400
    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 400
    show rs_image_BF15F042F4A241789DDE485A5CD928DE as tag_A7EEAA961C214874BEBADA168E79984E at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A7EEAA961C214874BEBADA168E79984E onlayer master
    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    show rs_image_562CBE7FE74549F0894E5ADA22F9A4DA as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    pause 2.5

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_A7EEAA961C214874BEBADA168E79984E
    hide tag_82C54ADE966440F7B34C83D13555B813
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C1F0041794544D71B07C91EE20FC49B6
    hide tag_A9C25AA9ADF244498299ED6338BC9B6A
    hide tag_9A2F0FC4EAF04544A204C360327C8E59
    hide tag_8849E9F5C5E044E3AAACB5D6D7EF2CE8
    hide tag_2C45FF10AF2D49B9A109BA34FD33D1F4
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_222BBB56F7BA4025B3E942F40786CBC9

    pause 2.5

    $ set_window("イベントモード")
    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 200
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_7B7735414BAC45BC9703868C4B37F398 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 1.5

    $ zorder_tag_061CD0864C4E48C0B3AA935440B7C90D = 300
    show rs_image_07D0476A77F848D38DFD798A8124FBC5 as tag_061CD0864C4E48C0B3AA935440B7C90D at center_top zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    show rs_image_F1F4BA1BDF4D4BD6820C5BB46EF814E4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_3CDBB93600FA40048DE19330047E1350 as tag_061CD0864C4E48C0B3AA935440B7C90D zorder zorder_tag_061CD0864C4E48C0B3AA935440B7C90D onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "唔？突然怎么这么困……"

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_061CD0864C4E48C0B3AA935440B7C90D
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "呼……呼……"

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7B7735414BAC45BC9703868C4B37F398 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "老、老师！？"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_music_current_file != "sound/BGM/Monster 2.ogg":
        play music "sound/BGM/Monster 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Monster 2.ogg"

    show rs_image_104D8871C298423C8D21AE9E1802FF43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "老师，发生什么了！？{w}\n欸！？二班的老师也！！{w}\n其他职员也睡倒了！"

    show rs_image_D095424890D94026B037A118F37E6038 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_FDC8C79E099A4B27B54A26982B59E98A

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "小卖部的大妈也！！{w}\n坏了！所有大人都睡了！！这是怎么了！？{w}\n出事了！！赶快出去叫人！！"

    window hide

    pause 0.3

    show rs_image_7B7735414BAC45BC9703868C4B37F398 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_B4378AE67E6A4B08A37DF8E3C2E65B17 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "什、什么？手机没信号了！"

    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    show rs_image_7B5C5A077F444A129B34E79C86B664D1 as tag_724406A84D7141298EFF0D864FAE1534 at left_top zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "我也是……混蛋……到底怎么回事？"

    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_C9A169B5FECE487BAE71B3017B79B0B4 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "总总总总总之冷静！！冷冷冷冷静下来！！"
    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    show rs_image_498A037484774EF3BE2C6B545543CBD3 as tag_61A891D6A6D047DC93695DA12E13CC75 at right_top zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "处理这种场合太难了所以不用勉强自己哦，班长。"

    window hide

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open window 1.ogg"

    pause 0.9

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C197AB750EF8424887D8CF5ECCE7226B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友、友啾，还好吗！？！？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9071DE7B7E5343C897D93F24F8DF7BAF as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "翼君，什么时候来的！？\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_293AA514A24E4A44BB395EC06789F57B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    extend "呜哇啊啊啊救救我——！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_B62939FE188646B19F924D8B074E376A as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "大、大家不好了！！看外面！！"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_CA32B3074CBF4DB08BA59AE12141A4F7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这是……校门外空无一物……"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_889F2AF205E140788BE374915197CA80 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "简直就像只有学园本身被移动到了异空间一样……\n这难道是梦？"

    window hide

    pause 0.5

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_8B5421D67E1C439BA9A47142DAC6188F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_53FEBB64B5034493AD43F17831AA22EB as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_A39671BE6D8246F5ACCB45CA04C8C3D1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "这是怎么了！！到底发生什么了！？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我怎么知道！总之回校舍！在外面我们也可能会被怎么样的！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_12C16002CB7242BA9D0C2BD3BC6B40C2 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_5A3ACD55ABCB481BA6B043DB3F263AB5 as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_E3F6ADD43DE44A428E1224756613C694 "开什么玩笑——！怎么能这么灰溜溜地逃回去！我来打头！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    show rs_image_3B561EDD5FE14AB3949693F15E6C2035 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "笨蛋啊你！那才是最危险的！！我绝对不会让你去的！！"

    window hide

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_486F70F1E27D43BC868FA3ADA0B574BE as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_802FEF2577C54DDA8193A6CA90A73DA7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嗯？什么人啊这些大叔，学校里有来着？\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_4C30DC76D6504BB48138EAD5DBDD5345 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "好像很庄重地抱着个箱子呢。"

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_B7338300611E44679D3661334AC876A9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不知道，很可疑，我也不认识。怎么说，这个人，穿的挺奇怪的……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    show rs_image_7DB1B9742B564B6884BA6E90FD7CD17B as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "不是和尚吗？"
    show rs_image_A05DD3DEFDEC4CBFBF1137EFA3D79309 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那个，难道……\n这家伙就是引起这一系列事情的原因？？"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_12C16002CB7242BA9D0C2BD3BC6B40C2 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "什么！？给我起来大叔！！\n"
    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Hit 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Hit 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Hit 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "起来了！！做点什么啊——！！"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_D648DEFEBFB849EDABEC0C42208FB02C as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_609B18A24DC64637943B3F2C0430365E as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "已经可以了！别管这个大叔了赶紧回去比较好！！"

    show rs_image_12C16002CB7242BA9D0C2BD3BC6B40C2 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "绝不！这个时间这个地点出现这样一个人不觉得奇怪吗！\n这家伙绝对就是关键！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_4C30DC76D6504BB48138EAD5DBDD5345 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "比如那个箱子里有重要道具……"

    stop music fadeout 2
    $ sys_music_current_file = ""

    window hide

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    show rs_image_93E7311915BC403AAFABACFA29A7DDB1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_DEC2F822DD03433CB37D42439376833B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_98508F03C2B54E6595F99F669212CD79 as tag_0999797A178545CBA5F244F41BBA50B1 at center_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_A39671BE6D8246F5ACCB45CA04C8C3D1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_B558281038CC4E8AA65F932D844CC6FD as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_A05DD3DEFDEC4CBFBF1137EFA3D79309 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_710A38AC94C841779DB701B5AC1010FD "！？\n"
    if sys_music2_current_file != "sound/Effect Sound/Cut the wind 1.ogg":
        play music2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "木、木木木木村、背后！！！"

    pause 0.4

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A at center_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_802FEF2577C54DDA8193A6CA90A73DA7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_3BC0411E559D49E38A86F531E7DC85FF

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸？"

    window hide

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_C1F0041794544D71B07C91EE20FC49B6 = 200
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_C1F0041794544D71B07C91EE20FC49B6 at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_C1F0041794544D71B07C91EE20FC49B6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_A9C25AA9ADF244498299ED6338BC9B6A = 200
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_A9C25AA9ADF244498299ED6338BC9B6A at Transform(xpos=450, yalign=0.0) zorder zorder_tag_A9C25AA9ADF244498299ED6338BC9B6A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.3

    window show

    if sys_music_current_file != "sound/BGM/Battle.ogg":
        play music "sound/BGM/Battle.ogg" loop
        $ sys_music_current_file = "sound/BGM/Battle.ogg"

    rs_character_597D0FE9F56B4929893DA8F9F1B0A666 "你很聪明呐～不过，错了一半。重要的不是里面，而是箱子本身。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    show rs_image_F22822BF03BF404AA4D836728AC17B45 as tag_2C4A74BADF6540698EF3E9A300893D1A zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "唔、唔哇啊啊啊啊啊！？！？这些是什么！！！\n走开！！走——开——！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_C1F0041794544D71B07C91EE20FC49B6
    hide tag_A9C25AA9ADF244498299ED6338BC9B6A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_7EDD11CE231F458AB1243CE1B9165B7F

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C1F0041794544D71B07C91EE20FC49B6 = 300
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_C1F0041794544D71B07C91EE20FC49B6 at center_top zorder zorder_tag_C1F0041794544D71B07C91EE20FC49B6 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_597D0FE9F56B4929893DA8F9F1B0A666 "万岁——首先拿下一个。"

    hide tag_C1F0041794544D71B07C91EE20FC49B6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_5A3ACD55ABCB481BA6B043DB3F263AB5 as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_AE2879D336AC4FEF9997D54F17B41E88

    rs_character_710A38AC94C841779DB701B5AC1010FD "木、木村！！"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_C2D928E50B6A4036912698848DAC99D0 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "混蛋！！你这家伙！！\n不许对我的木村出手！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C1F0041794544D71B07C91EE20FC49B6 = 200
    show rs_image_5A3ACD55ABCB481BA6B043DB3F263AB5 as tag_0999797A178545CBA5F244F41BBA50B1 zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_C1F0041794544D71B07C91EE20FC49B6 at Transform(xpos=450, yalign=0.0) zorder zorder_tag_C1F0041794544D71B07C91EE20FC49B6 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_DA3AA75F12294B2E94D171462BCE03A2 "那我就收下这个了。真幸运～是可爱系的呐。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_C1F0041794544D71B07C91EE20FC49B6
    hide tag_A9C25AA9ADF244498299ED6338BC9B6A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_7EDD11CE231F458AB1243CE1B9165B7F

    pause 0.3

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_53FEBB64B5034493AD43F17831AA22EB as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_E54A2DFBC85F4C20B96B216AE6D076B7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "这些怪物是什么！？"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C1F0041794544D71B07C91EE20FC49B6 = 200
    $ zorder_tag_A9C25AA9ADF244498299ED6338BC9B6A = 200
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_C1F0041794544D71B07C91EE20FC49B6 at right_top zorder zorder_tag_C1F0041794544D71B07C91EE20FC49B6 onlayer master
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_A9C25AA9ADF244498299ED6338BC9B6A at left_top zorder zorder_tag_A9C25AA9ADF244498299ED6338BC9B6A onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_597D0FE9F56B4929893DA8F9F1B0A666 "还要回收箱子，先回去一下～"

    rs_character_DA3AA75F12294B2E94D171462BCE03A2 "就这么做～要用箱子给大家带来笑容。"

    hide tag_C1F0041794544D71B07C91EE20FC49B6
    hide tag_A9C25AA9ADF244498299ED6338BC9B6A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_6F41BEB29B0744ED8F25360004E87AB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_C1F0041794544D71B07C91EE20FC49B6
    hide tag_A9C25AA9ADF244498299ED6338BC9B6A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7DAD4CE5E17E4F44BB8A78EA7CC54328 "{size=32}唔、唔哇啊啊啊！！？{/size}"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "伊藤！木村！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "坏了、坏了坏了坏了……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_802FEF2577C54DDA8193A6CA90A73DA7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_E54A2DFBC85F4C20B96B216AE6D076B7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "笨蛋猫山！！别吓昏过去啊——！"
    show rs_image_EFDEEDA02727406390376B91A7A8F75D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "添麻烦！！"

    pause 0.4

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    show rs_image_93E7311915BC403AAFABACFA29A7DDB1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……嗯？{w}{w=0.4}{nw}"
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    extend "你们在那干什么！"

    window hide

    pause 2.5

    $ set_window("イベントモード")
    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_AA86FA56504D468ABD431166D03DCF2B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BE44B9B57DE34031B0F7EB596C4CDC5E

    pause 1.2

    show rs_image_EB60C595EE234D36811D5503DC18D49A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.9

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_C1F0041794544D71B07C91EE20FC49B6 = 200
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_C1F0041794544D71B07C91EE20FC49B6 at left_top zorder zorder_tag_C1F0041794544D71B07C91EE20FC49B6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    if sys_music_current_file != "sound/BGM/Monster 1.ogg":
        play music "sound/BGM/Monster 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Monster 1.ogg"

    rs_character_597D0FE9F56B4929893DA8F9F1B0A666 "两位追加～"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_A9C25AA9ADF244498299ED6338BC9B6A = 200
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_A9C25AA9ADF244498299ED6338BC9B6A at right_top zorder zorder_tag_A9C25AA9ADF244498299ED6338BC9B6A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_DA3AA75F12294B2E94D171462BCE03A2 "箱子也好好回收了哦～"

    hide tag_C1F0041794544D71B07C91EE20FC49B6
    hide tag_A9C25AA9ADF244498299ED6338BC9B6A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 = 200
    show rs_image_F640D24E91BC44AB8E0808AF82ED2885 as tag_346FE7CD97BB4FB18CB50E78275F4E23 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_346FE7CD97BB4FB18CB50E78275F4E23 onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    rs_character_EA9AA88E88D84B559B925363E2931756 "好，打赌是我赢了！果然伊藤和木村也被抓过来了呐。"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_1A71CDD16705479CADC0B5AE6CAF3F69 as tag_CC4336DE74164173AC47C2C317367F10 at center_top zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "啊啊！还以为会赚到午饭钱的……你们再拿出点毅力啊！！"

    show rs_image_04BBD0AABA25450B9004531DD4019381 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "算了，就靠取材排解！"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_9C6025197AA6408B855470BD6875E779 as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "小岛君，这可是大事件，好好拍！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_DCBDF256A1E242E78A25910AE27C0954 = 300
    show rs_image_8A8399081EA34489AD19EAD1C673B291 as tag_DCBDF256A1E242E78A25910AE27C0954 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_DCBDF256A1E242E78A25910AE27C0954 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "部长，这种毫无魄力的心灵照片还不如直接合成来得好。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 300
    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 300
    show rs_image_FF2DDA4385D843F1B0AD95DA89A1A9F2 as tag_2C4A74BADF6540698EF3E9A300893D1A at right_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    show rs_image_A05DD3DEFDEC4CBFBF1137EFA3D79309 as tag_0999797A178545CBA5F244F41BBA50B1 at left_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_710A38AC94C841779DB701B5AC1010FD "诶？意外很和平的样子……？"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "一、一般会这样享受现状吗！？"

    window hide

    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 at left_top zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "同志们辛苦了。这下就安稳了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 300
    show rs_image_757537DAAA5F421595F24FFD01860C20 as tag_3FA60293C6724C72B5FECC927A2B7804 at right_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_079949A107134E47B24110C78D2FA0CF "啊啊！我们的时代终于来临了！！\n存在于独立时空间的御咲学园，正可谓是乐园！"

    show rs_image_053F79D99A65415485F5458CD87E3325 as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "在这里少年们永远不会长大。\n因为原本的世界里时间并未前进，也就不会有救援。"

    show rs_image_4D9B5CDCB00648DAB664199B1CA9D163 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "别用那种自私自利的语气说。这里对少年们也是乐园。"

    show rs_image_757537DAAA5F421595F24FFD01860C20 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "做出一个没有麻烦的大人，没有作业，\n可以按照自己所想随意生活游玩的世界如何！"

    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "既然如此，各种各样的设施就很必要了。同志们也要辛勤工作了呐。"

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "要在外面玩的话，就必须要进一步扩大支配范围到御咲学园之外……"

    show rs_image_562CBE7FE74549F0894E5ADA22F9A4DA as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "不错！不错！渐渐把世界变成少年们的乐园！！"

    hide tag_82C54ADE966440F7B34C83D13555B813
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 300
    show rs_image_4D9B5CDCB00648DAB664199B1CA9D163 as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_079949A107134E47B24110C78D2FA0CF "那个令人生畏的箱子一定要藏到绝对不会被发现的地方！"

    hide tag_82C54ADE966440F7B34C83D13555B813
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_A7EEAA961C214874BEBADA168E79984E = 300
    show rs_image_175B061199E04D9EB2CB6F9FA9279C56 as tag_A7EEAA961C214874BEBADA168E79984E at center_top zorder zorder_tag_A7EEAA961C214874BEBADA168E79984E onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    rs_character_D21FC549273B4A1ABB90AEF39DEAD87B "明白……藏起来……"

    hide tag_A7EEAA961C214874BEBADA168E79984E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 at center_top zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "本该直接在此破坏的，不过箱子里还残留着我们的一部分力量。"

    show rs_image_9CB24AF1FF544F0F9A754DA0E9105FBB as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "不过，这里也并不存在知道封印我们的方法的大人，无须担心。"

    hide tag_82C54ADE966440F7B34C83D13555B813
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 300
    show rs_image_757537DAAA5F421595F24FFD01860C20 as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "要快哦～！真想快点取回力量！！快点征服世界～！！"

    hide tag_82C54ADE966440F7B34C83D13555B813
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show rs_image_6F41BEB29B0744ED8F25360004E87AB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_079949A107134E47B24110C78D2FA0CF "算了，毕竟迟早都会是我们的完全胜利嘛！！！唔哈哈哈！！"

    window hide

    pause 1

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_038A3EB7489F4B51B2A1AD7FBC2E0808

    pause 2.5

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_7B7735414BAC45BC9703868C4B37F398 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.8

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_FE681BB78F1F4D339A2566A5D9707982 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "前去侦查的加藤和松田也失去了联络……怎么办？绫濑，我们去不去？"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_CA32B3074CBF4DB08BA59AE12141A4F7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "是啊，在这里等着也毫无用处，为了亲眼确认也只能去了。"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_A51FC16534344AB291AA801BC1DAFEA2 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那、那么，友君，慎酱，还有一之濑君，请跟着他们两个走。\n应该不分开的话会更安全。"

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}请等一下！{/size}"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.7

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_022781101FD04002AB8C506EED9156F2 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦呀？你应该是，"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_E21ACD1443A4402AA37E7CE200FF6D4C as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_A7D458B112A543F691F4223B8946B813 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_BAB1EF8BB1E8402E9731FA917EC2849D as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=430, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.3

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg"

    extend "三酱的弟弟君！\n为什么来这里？"

    show rs_image_BFC4A160DFDF465C82BD02885E29367D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊……前辈是……{color=#008080}之前{/color}多谢关照……{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_70926DEB0D12407EA1DE34641A6A633B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_486F70F1E27D43BC868FA3ADA0B574BE as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_17BD4756EE4547C7999FB0FE558D991B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "什么啊，你们也平安活下来了啊。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_FF4A588462534B15B9D5F444704F26BB as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇，技安！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_332D35DF942A4E11AF6CD9B932EC0FD0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "平、平安活下来是什么意思？"

    show rs_image_53FEBB64B5034493AD43F17831AA22EB as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔唔唔……伊藤和木村……被怪物带走了……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_B62939FE188646B19F924D8B074E376A as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "怎、怎么会！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_4BA562125E914D049B3A68EC3F0DB8A1 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "唔，三酱抖得这么厉害明明很可爱的……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_A2E7C1AAED834AD7861668C6EE330F80 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_075F12352E04495CB718DBEB1B7D807C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "乖乖。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_CA32B3074CBF4DB08BA59AE12141A4F7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "怪物……？\n"
    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "还有……没见过你呢，你是？"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_C040277FC7FE48E19FB154ABD798FD6D as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "啊，你、你好，初次见面。我叫做榊雪绪……"

    show rs_image_F03237FB10EB44FDB0C2E3F6C4B4F5D2 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗的朋友，同样是小学六年级。请多多关照～……"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_FE681BB78F1F4D339A2566A5D9707982 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "可是，两个小学生为何会出现在这里……？"

    window hide

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_ABB2A951B8D345A092CC374396221386 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_E1B79FB8843B4F1DA81DDFFFF2F5ED7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5BF57DBE5ED14CE2AFADF67B50D75DA7 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "善。汝之疑问吾均会解答。"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_A39671BE6D8246F5ACCB45CA04C8C3D1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=600, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_B558281038CC4E8AA65F932D844CC6FD as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=340, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_229EB6C626CB4AD79FA6063567685C64 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-240, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_9241757E0E3A46D8A082C1EF9568D9F4 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=20, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=450, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=100, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_6536F8ADBA294923ABCC248AEAB17528 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=200, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_7C7F47B899A04C1E9877716E2B4CC7B5 "{size=36}！？{/size}"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_76A6FDF06765424DBC1E2AE1C0D1ADA1 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_3B4C660F421B4BE392BB540B580F0339 "这孩子最近性格总是会变来变去……吓到你们了很抱歉……"

    show rs_image_12FA5E6A33CF436D8BF3D03325E739EE as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "但好像对这次事件知道些什么，还请听一下……"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_7AD635BC32424CDEABF54354F991383F as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "现今，此处已于时空间独立。无从外出，时光停滞。"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "此乃汝云“怪物”……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    extend "即{color=#FF0000}恶灵{/color}之过。"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B62939FE188646B19F924D8B074E376A as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_BA79E21F6467495A849CFF33257777BB as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3A18AD188C0145CF8D8F0303DB763749 "恶、恶灵！！？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_02AF4E98AE404A37BBF5189D1BD66AE6 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=450, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=90, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-120, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍、忍！"

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_038AF5F78DF84D199A7553B24E2CBDAA as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=280, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥！"

    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_CBC100753B6747F2AFD4D87363DBBCAA "乖乖。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_293AA514A24E4A44BB395EC06789F57B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-120, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "（只、只有我是一个人……）"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_00C537252F144BC5A27190CF382A7D50 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_B2054D14604A408CAF74D842FA9CF92A as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_D46359E31BB0468CA6B3E9997C1C2BBC as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=90, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……放心。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_83DC2938B261446EA7DA8E7BEDD8F68F as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "独事无力，遂群居而行。何等卑劣。"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "根除且易，然为使学园重归旧处，需重施封印。"

    show rs_image_7AD635BC32424CDEABF54354F991383F as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "尚闻仍有知之之人，然此皆孩童，无从期待。"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_17BD4756EE4547C7999FB0FE558D991B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_022781101FD04002AB8C506EED9156F2 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我、我知道你们很难相信，但这是真的！我可是亲眼看到了那些怪物……唔。"

    show rs_image_3CA5C53D5B5F4402ABE043400BD0BCE1 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "然后，你们是来救我们的吗？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_1FF74BBF0900427C9BF73296B4E8EE28 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "非也。本欲与猫山四朗共迎三朗归，偶然卷入。"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "直言，吾不欲于此等闲事劳烦，却不得友人谅。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_A7D458B112A543F691F4223B8946B813 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_7AD635BC32424CDEABF54354F991383F as tag_4233D225ED0D43968B3A0D890F587FEB at right_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "欸，可是，你刚才还说不封印怪物就没法解决的。"

    show rs_image_83DC2938B261446EA7DA8E7BEDD8F68F as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "此乃汝等现状。吾可自由来往。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_FE681BB78F1F4D339A2566A5D9707982 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "原来如此……看来榊被常人无法理解的力量寄宿了。记得是叫“灵感”。"

    show rs_image_C94C15F70ECD4CCBBA838E6B1352ED84 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "不错。子言极是。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_741DD1CD8B8948359D329B0A50F15E14 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "言他之，子甚似恼怒。"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "若有欲为之事，吾可相助。后请献上汝之身……"

    show rs_image_4D5E70DCADBB4F2CA52AB49DED72D7C5 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_B0AE196FCA0347DEACA52C0CB36FB8EE as tag_4233D225ED0D43968B3A0D890F587FEB at right_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    pause 0.3

    rs_character_7009C1117C004F51829614A203C67DE7 "最、最后那个不听也可以的～！总之就是这里也只有现在是安全的～"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "就是说不管怎样还是要突入作战时间了吧！好，那边两个班长！带头！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BA79E21F6467495A849CFF33257777BB as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_1A4E2C97F9B346CDB2866AA35E205783 "诶诶诶诶诶！"

    window hide

    pause 0.7

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1.8

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_F1F4BA1BDF4D4BD6820C5BB46EF814E4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_FFC620A1302E417EBD9CB71C6CDE9274

    pause 0.8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_9071DE7B7E5343C897D93F24F8DF7BAF as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那个……根据榊君的说明，解决方法是……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "打倒怪物，封印他们……"

    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没有具体的方案根本不明白！怪物能打倒！？封印又该怎么封印！？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_D7279DBAD79D48199C2509989B89EA00 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_7B7735414BAC45BC9703868C4B37F398 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "封印……？"
    show rs_image_E54A2DFBC85F4C20B96B216AE6D076B7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊！\n难道是那个可疑大叔拿着的{color=#FFFF00}箱子{/color}！"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_609B18A24DC64637943B3F2C0430365E as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "绝对就是！要不那些怪物就没必要特地找回去了！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_8AD2DDD7544B43C4A6A69B2DAC1465E5 as tag_4233D225ED0D43968B3A0D890F587FEB at right_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "那个箱子现在在什么地方？"

    show rs_image_B276F958003A43A59D0E1DAFE5CCAA4E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "被怪物带走了，现在不知道……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_A51FC16534344AB291AA801BC1DAFEA2 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "说、说起来，被带走是被带到那里去了呐……"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "如果这个学园整个被从时空中分离开来了的话，\n根本没必要特意带去什么地方……唔。"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_FE681BB78F1F4D339A2566A5D9707982 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "学校内能集中所有学生的地方……而且还不是校庭，那样的话就只有一个了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_2155B7020F8F4BDE8F91FA487FF49C6A as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "那事不宜迟，去营救大家了！决不允许那些家伙继续肆意妄为了！"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_022781101FD04002AB8C506EED9156F2 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那就是说要和怪物战斗了？可是要怎么做才能攻击到他们？"
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_C94C15F70ECD4CCBBA838E6B1352ED84 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "无须担心。吾之力将伴随汝等。"

    window hide

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_E1B79FB8843B4F1DA81DDFFFF2F5ED7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_332D35DF942A4E11AF6CD9B932EC0FD0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.3

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_E1B79FB8843B4F1DA81DDFFFF2F5ED7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E21ACD1443A4402AA37E7CE200FF6D4C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_FE681BB78F1F4D339A2566A5D9707982 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_48394E3397A94AD090308D24BFC677E3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    pause 0.3

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_E1B79FB8843B4F1DA81DDFFFF2F5ED7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_93E7311915BC403AAFABACFA29A7DDB1 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_DEC2F822DD03433CB37D42439376833B as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3DE6DC5E51F14E4F86F96E18DE4838E6 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.3

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_5BF57DBE5ED14CE2AFADF67B50D75DA7 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "如此，汝等身体，以及道具，方可有效。"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_7C30D306B01C4984A6C86B48D0A0FD27 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哦哦……！寄宿在拳头里的特别的力量……！！"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍的兴致好高。"

    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "呵呵呵……燃起来了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这样一来怪物也并不恐怖了。不过只能凑巧看见的那种还是有些不舒服。"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "就像我之前给你看的{color=#008080}照片{/color}那样的？{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_737FF30685D64FC5AE26E9E0A8C50014 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_C8509382B1E34741B9130C4CA5DE55D6 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "对对！那真的很恐怖啊……"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_78AAFDF80423489CB9D3E414C6D0A594 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "话题先回来，那个箱子在哪？在他们的要塞不成？"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就让忍他们把怪物打得落花流水，直接逼问不就好了？"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_4E2835E547304DD1A4EE59EDDEA933C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "唔，对于已死的家伙有恐怖这种说法吗？不管怎么威胁都问不出来的吧？"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_C98211B62EA04A368AA5021885891661 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那劝诱如何？这可是问出秘密的最好手段哦～♪"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_50D82C35F258450C9BFE07520E310720 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "劝诱……你有那种毅力么？对方可是怪物哦？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_B7002004B9C945ABA305FBBF878A4362 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不要小看玩弄无数男性于掌中的花乃汤的看板少年・慎酱！"

    show rs_image_0600CCA9D8E5458687C3A5F9EE6CB6C5 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……"
    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "（不满中～）"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_A7D458B112A543F691F4223B8946B813 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_8AD2DDD7544B43C4A6A69B2DAC1465E5 as tag_4233D225ED0D43968B3A0D890F587FEB at right_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_3B4C660F421B4BE392BB540B580F0339 "那个……就算找到了箱子，该怎么封印？"

    show rs_image_2D9DBFACED644B2882B38D7E4606CBF6 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "说的对，要是有对妖怪之类的东西很了解的人就好了。"

    show rs_image_BFC4A160DFDF465C82BD02885E29367D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "图书室会不会有这方面的书呢！？毕、毕竟是中学。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_B276F958003A43A59D0E1DAFE5CCAA4E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "不——这可说不准……算了，调查调查也没什么不好。"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "感觉渐渐找到谈话的方向了呐！好——的！那么各自出动！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_9071DE7B7E5343C897D93F24F8DF7BAF as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_F1F4BA1BDF4D4BD6820C5BB46EF814E4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "现、现在开始为大家分组。{w}\n①救援组②回收组③调查组。"

    show rs_image_10320EED82DD4A1ABC66033DB3E2750B as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "{color=#00FFFF}救援组{/color}请打倒怪物，救出所有被困的人。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "{color=#00FFFF}回收组{/color}请从怪物那里打听到箱子的所在之处，然后回收它。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "{color=#00FFFF}调查组{/color}请详细查找相关的封印方法。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_104D8871C298423C8D21AE9E1802FF43 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好、好——！大家一起加油，夺回御咲学园的和平——！！"

    window hide

    pause 1

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_1C3AC3BC102640A98B0B848A29849370

    pause 3


    if judge_lm_condition([]):
        jump block_00003EA4

    return

label block_00003EA4:
    # Node: 00003EA4 (學園怪談 2)
    $ set_window("イベントモード")

    show left_title (_("救援组")) as left_title
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 2

    hide left_title
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_51451FBF94C8444AA5696178E72CE210 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    show rs_image_6942001DFE4B4C088A665365008EB0AF as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_music_current_file != "sound/BGM/Flurry 2.ogg":
        play music "sound/BGM/Flurry 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 2.ogg"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "呀！！！"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_4D8F1D6A70C24A34A3E6C37B69619470 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    $ zorder_tag_A366FE92B81D404585614E7D29CFAD20 = 300
    show rs_image_808C1269C48143C38C3000CB647CB3BF as tag_A366FE92B81D404585614E7D29CFAD20 at center_bottom zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    show rs_image_6942001DFE4B4C088A665365008EB0AF as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哈！！！"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_8CD556F98525469D9B60EF719D590FB8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    $ zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 = 400
    show rs_image_ABB55DB1211049EFB8F17F920B8EE8F2 as tag_DD234F3A788F4BD5954C8F12B53FB442 at center_bottom zorder zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 onlayer master
    show rs_image_808C1269C48143C38C3000CB647CB3BF as tag_A366FE92B81D404585614E7D29CFAD20 zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    show rs_image_6942001DFE4B4C088A665365008EB0AF as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯！！！"

    window hide

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_A366FE92B81D404585614E7D29CFAD20
    hide tag_DD234F3A788F4BD5954C8F12B53FB442
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    $ zorder_tag_C1F0041794544D71B07C91EE20FC49B6 = 300
    $ zorder_tag_A9C25AA9ADF244498299ED6338BC9B6A = 300
    $ zorder_tag_9A2F0FC4EAF04544A204C360327C8E59 = 300
    $ zorder_tag_8849E9F5C5E044E3AAACB5D6D7EF2CE8 = 300
    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_C1F0041794544D71B07C91EE20FC49B6 at Transform(xpos=-120, yalign=0.0) zorder zorder_tag_C1F0041794544D71B07C91EE20FC49B6 onlayer master
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_A9C25AA9ADF244498299ED6338BC9B6A at Transform(xpos=280, yalign=0.0) zorder zorder_tag_A9C25AA9ADF244498299ED6338BC9B6A onlayer master
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_9A2F0FC4EAF04544A204C360327C8E59 at Transform(xpos=450, yalign=0.0) zorder zorder_tag_9A2F0FC4EAF04544A204C360327C8E59 onlayer master
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_8849E9F5C5E044E3AAACB5D6D7EF2CE8 at Transform(xpos=90, yalign=0.0) zorder zorder_tag_8849E9F5C5E044E3AAACB5D6D7EF2CE8 onlayer master
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_595DE88542AA4928A9E91FC52D64D9F1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    window show

    rs_character_975302EA219B4E37980C3617E75594B6 "被打败了～……"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_C1F0041794544D71B07C91EE20FC49B6
    hide tag_A9C25AA9ADF244498299ED6338BC9B6A
    hide tag_9A2F0FC4EAF04544A204C360327C8E59
    hide tag_8849E9F5C5E044E3AAACB5D6D7EF2CE8
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 6.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 6.ogg"

    show rs_image_9F8EA032E81344E3B32B192681064721 as tag_5DC444A6262A4FCE9BF63B4338E21A74 zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_D966548D39864E42A031D80097F6944B as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_621923550F3B42DEAC63D2D352B2183B as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_5739B888853E4BCE83F4B5FFEC74A1C2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.4

    window show

    rs_character_9C406D37B5D94F7A82F160CA06D06626 "{size=32}谁也行放马过来！！！{/size}"

    window hide

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_293AA514A24E4A44BB395EC06789F57B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……我为什么会在这个组……？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我们看上去好像强过头，敌人都逃了。"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_B550C4E9D1DB474BBEDD133EA85FDFC5 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "任务是歼灭他们……不全都打倒是不行的。"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_02ECE9B805B742C6B558DFD2FD5D2608 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "为了那个令对方稍微大意一点也是必要的。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 2.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_293AA514A24E4A44BB395EC06789F57B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊……原来……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F9B0C2D0E2D84D6D85BC37C697E5F928 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "好，那就再来一次刚才的。翼君拜托你了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_CDE407350E4A49AC8933C6D199FE9A13 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "诶诶，又来！？我还没做好心理准备。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_B8B80AD906F346B398AAC78CE2B095A3 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "没关系！翼君的话一定能做到的！"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "相信自己。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_83253C644D7341D899A80F5E86570559 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_293AA514A24E4A44BB395EC06789F57B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "等这些结束后，作为奖励给你友的照片。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9071DE7B7E5343C897D93F24F8DF7BAF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我干！！"

    window hide

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    show rs_image_148B282ED1E44EDCB7EE910F714866A9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_C197AB750EF8424887D8CF5ECCE7226B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    window show

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜哇～～和大家走散了～好害怕～谁来救救我～～！！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_C1F0041794544D71B07C91EE20FC49B6 = 300
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_C1F0041794544D71B07C91EE20FC49B6 at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_C1F0041794544D71B07C91EE20FC49B6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_A9C25AA9ADF244498299ED6338BC9B6A = 300
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_A9C25AA9ADF244498299ED6338BC9B6A at Transform(xpos=410, yalign=0.0) zorder zorder_tag_A9C25AA9ADF244498299ED6338BC9B6A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_9A2F0FC4EAF04544A204C360327C8E59 = 300
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_9A2F0FC4EAF04544A204C360327C8E59 at center_top zorder zorder_tag_9A2F0FC4EAF04544A204C360327C8E59 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.3

    rs_character_27D85922B12540459DC156B3E8B254FA "发现落单的男孩子！"

    rs_character_103390581EEB458CB17C8FD22138296C "不要害怕，我们马上就把你带到朋友那里哦。"

    rs_character_B894A92E3C044747B068C05173C9695E "来来，过来过来。"

    window hide

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_D966548D39864E42A031D80097F6944B as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-90, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_621923550F3B42DEAC63D2D352B2183B as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_5739B888853E4BCE83F4B5FFEC74A1C2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 6.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 6.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_46726D80EC7B4D48AD2EFED4CDD37F1C as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.4

    window show

    rs_character_975302EA219B4E37980C3617E75594B6 "{size=28}唔啊！！{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_C1F0041794544D71B07C91EE20FC49B6
    hide tag_A9C25AA9ADF244498299ED6338BC9B6A
    hide tag_9A2F0FC4EAF04544A204C360327C8E59
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.7

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.6

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_93384CF7101E46B99C76C26B616C4A01 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这种作战……罪恶感好重。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_83253C644D7341D899A80F5E86570559 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不需同情敌人。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_9D80F5870F2249459239D301CED743C6 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "毕竟要先找到对方。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_2155B7020F8F4BDE8F91FA487FF49C6A as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "就以这个步调继续！接下来是大家应该在的体育馆的方向。"

    show rs_image_7C30D306B01C4984A6C86B48D0A0FD27 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "翼君，期待你继续活跃了哦。"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "会有很多奖励的。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E8DD9768D82A468CA794353ED73907AD as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我会尽全力的！我会加油的！！我会不断前进的！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 0.9

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_9241757E0E3A46D8A082C1EF9568D9F4 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "嗯……？等等，大家！那里有人！"
    show rs_image_A51FC16534344AB291AA801BC1DAFEA2 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "那个人是……"

    window hide

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.9

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Bell 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Bell 1.ogg"

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_595DE88542AA4928A9E91FC52D64D9F1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_DB0BD4A5526E46CCA60D1A469CF4D475 as tag_3482C372784E44A89E382266A93F2B14 at left_top zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 0.5

    window show

    rs_character_C223850065F6443080205D1F61C04C98 "你们好呀。"

    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_7C30D306B01C4984A6C86B48D0A0FD27 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_12471979B7D1437085FB86AB6EEB1E51 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "原来还有没事的人……不要担心，已经安全了。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "请和我们一起行动，我们能保护好你。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_BD5D4967AAB3422CB365C33860DE9016 as tag_3482C372784E44A89E382266A93F2B14 at center_top zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C223850065F6443080205D1F61C04C98 "谢谢，不过，我可以自己行动的。\n虽说和你们不太一样，我也还是很强的哦。"

    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_DB0BD4A5526E46CCA60D1A469CF4D475 as tag_3482C372784E44A89E382266A93F2B14 at left_top zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C223850065F6443080205D1F61C04C98 "那个……你，过来一下可以吗？"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_B2054D14604A408CAF74D842FA9CF92A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸……嗯，好的。"

    show rs_image_C4B36F704BDC4BB295B684E3F4796279 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "给你这个。"

    show rs_image_332D35DF942A4E11AF6CD9B932EC0FD0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "这是……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Bell 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Bell 1.ogg"

    extend "{color=#FFFF00}符、符咒{/color}！？"

    show rs_image_BD5D4967AAB3422CB365C33860DE9016 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "嗯，蕴含有打败恶灵的力量哦。我带着也毫无用处，给你了。"

    show rs_image_DB0BD4A5526E46CCA60D1A469CF4D475 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "你们已经很强大了，如果出现更强的敌人，就请使用这张。"

    show rs_image_93384CF7101E46B99C76C26B616C4A01 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "非、非常感谢。"

    hide tag_3482C372784E44A89E382266A93F2B14
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_4B8BD646B04149A38936E9329ADBBC5D as tag_3482C372784E44A89E382266A93F2B14 at center_top zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "那么，四位请加油了。大家都在体育馆等着呐。"

    window hide

    pause 0.6

    hide tag_3482C372784E44A89E382266A93F2B14
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    pause 2

    $ set_window("イベントモード")

    show left_title (_("回收组")) as left_title
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 2

    hide left_title
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_music_current_file != "sound/BGM/Flurry 2.ogg":
        play music "sound/BGM/Flurry 2.ogg" loop fadein 2
        $ sys_music_current_file = "sound/BGM/Flurry 2.ogg"

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_D095424890D94026B037A118F37E6038 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_C1F0041794544D71B07C91EE20FC49B6 = 200
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_C1F0041794544D71B07C91EE20FC49B6 at center_top zorder zorder_tag_C1F0041794544D71B07C91EE20FC49B6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_C0A385790CEC4BE8855720DC852E147D "男孩子们～在吗～？不要藏了出来～"

    window hide

    hide tag_C1F0041794544D71B07C91EE20FC49B6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_5FD9A8D43C244230B1ACD57E410985E4 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_29B059D0AECE4F3FBF86EE5DA29B17DF as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "来了来了！好……三酱，友亲，就按计划的来！"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_2A528A20757145A78087B876421EFAF4 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "了解！唔～好紧张！"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_B558281038CC4E8AA65F932D844CC6FD as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你、你们真的要干！？失败了可就没下文了啊……"

    show rs_image_AD906DE4351649D4A088A775E16D4592 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "没关系，实在不行用刚才拿到的{color=#FFFF00}符咒{/color}想点法子就是了♪♪"
    show rs_image_3CCC6DE5C5ED405DB1BBB15ECA3CDD44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不过啊，刚才那个人，一直单人行动真的没问题嘛。"

    show rs_image_F615F0D0DA0141DBA1401F94D0D8B1F8 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好像有什么原因的样子，我们也不好说什么。\n再说了，要是真的发生什么，救援组也会去帮忙的！"

    show rs_image_EB8AFE0130874B6E925058521DB5C8AB as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "上啊三酱！这种事情门面是很重要的，拜托慎重对待了。"

    show rs_image_23970544C9224BB4B785B8FB367471BC as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……明白。我相信你。\n既然是奥村想出来的方案，一定能行！"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_7B9421782EFE49138E5AADFCD59A037D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_075F12352E04495CB718DBEB1B7D807C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_9538619ECD0849688D07CEC63FB8B083 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "咻——咻——♪"

    window hide

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_D095424890D94026B037A118F37E6038 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 0.7

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_602B12F1C445477F861182BD846DB0BD as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦，那边的小兄弟！执勤辛苦了～"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_C1F0041794544D71B07C91EE20FC49B6 = 200
    show rs_image_619F9CAF828B4C79A9F49F01EDB4F32B as tag_C1F0041794544D71B07C91EE20FC49B6 at left_top zorder zorder_tag_C1F0041794544D71B07C91EE20FC49B6 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_C0A385790CEC4BE8855720DC852E147D "啊～终于肯出来了～不想让我辛苦的话早点出来不就好了嘛～"

    show rs_image_0AE8CF84C8F94EF9BEE8D1640F087EC3 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不要在意不要在意。\n现在就先别管工作了，偶尔休息休息也是很重要的哦～？"

    show rs_image_0406E6E479AB41E795AD161873DE523C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "占用点时间怎么样？不不，请务必，说几句话也好！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_C0A385790CEC4BE8855720DC852E147D "哦、哦。"

    show rs_image_16C788753D5540129E52560144B1F91A as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "客官是做什么的呐？\n欸，在当妖怪啊！那可真是不得了，压力肯定很大。"

    show rs_image_05869A4FEB35497BB941E279D075CC45 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我们有超适合你的好地方哦。咋样？有兴趣不？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_C0A385790CEC4BE8855720DC852E147D "欸……有点。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好来了——！那么！客人一位——！！"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C1F0041794544D71B07C91EE20FC49B6
    with rs_effect_A4DEE961526445FC8CF90E5B29704349

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    # Gallery unlock: images/CG/The-inbelieveble-of-school/The-inbelieveble-of-school 2.png
    $ zorder_rs_image_B5CABC467ECD46948E0B1292E589A60D = -100
    show rs_image_B5CABC467ECD46948E0B1292E589A60D as rs_image_B5CABC467ECD46948E0B1292E589A60D zorder zorder_rs_image_B5CABC467ECD46948E0B1292E589A60D onlayer master
    hide rs_image_B5CABC467ECD46948E0B1292E589A60D

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 200
    show rs_image_B5CABC467ECD46948E0B1292E589A60D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_2A62662A9A9C44A1A266E7BB1BDCA6A0

    pause 0.9

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_C49E8447151A496692350FA6779E4154 "{size=28}{color=#FF80FF}欢迎光临♪{/color}{/size}"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这两位是本店最棒的哦，左边是友亲，右边是小慎。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "快快，来给客官打个招呼！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    rs_character_C49E8447151A496692350FA6779E4154 "{size=28}{color=#FF80FF}官人好呀♪请多多关照了。{/color}{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_C0A385790CEC4BE8855720DC852E147D "欸、欸。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "客官请慢用～"

    # Gallery unlock: images/CG/The-inbelieveble-of-school/The-inbelieveble-of-school 2-1.png
    $ zorder_rs_image_344471F6EC6A4D92B3E3A4F9A0C4F5E8 = -100
    show rs_image_344471F6EC6A4D92B3E3A4F9A0C4F5E8 as rs_image_344471F6EC6A4D92B3E3A4F9A0C4F5E8 zorder zorder_rs_image_344471F6EC6A4D92B3E3A4F9A0C4F5E8 onlayer master
    hide rs_image_344471F6EC6A4D92B3E3A4F9A0C4F5E8

    show rs_image_344471F6EC6A4D92B3E3A4F9A0C4F5E8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "贵人难道是第一次来这种地方？看起来好紧张呐～"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "放松放松，"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    extend "就由我们来消・除・紧・张♪"

    window hide

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Scene changing 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Scene changing 2.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_57F79897CE2D49FC8E9CC05EC4072D27

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 200
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "还有这种事啊～！妖怪的世界也好辛苦呐。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "对这么努力的妖怪先生我们会送上特别服务哦～♪"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊，不过，在那之前，我想打听一件事可以吗？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_C0A385790CEC4BE8855720DC852E147D "没问题没问题，什么都行。都谈到这儿了，秘密什么的早就都没了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀——！说是什么都行哦！慎酱！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好高兴——！不过果然这……感觉意有所指呐。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_C0A385790CEC4BE8855720DC852E147D "相信我！一定会回应你们的期待的！说，想问的是什么？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "其实……"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    pause 0.3

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 2.5

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_D095424890D94026B037A118F37E6038 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_BC6A664B6C584BBCA2E4BAC991994F6A

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_40923DB023424478AE9514379D78E8B7 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "完毕！情报收集成功！{color=#00FFFF}箱子就在屋顶上{/color}！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_2B24914707CC4FF38461FD9B7BB09975 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "干得漂亮你们两个！！事不宜迟快去！"

    window hide

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    pause 0.3

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_148B282ED1E44EDCB7EE910F714866A9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_39829274F0594DCC89A2EF09B108ED2E as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_29B059D0AECE4F3FBF86EE5DA29B17DF as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "话说回来你们就这么顺利脱身了啊。怎么骗过去的？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_4BBDCD83023642F6923D76BE102A1BB9 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_9538619ECD0849688D07CEC63FB8B083 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{color=#FF80FF}“我们要先去洗个澡请等等哦”{/color}这样的♪"

    window hide

    show rs_image_B558281038CC4E8AA65F932D844CC6FD as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.8

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_216D0346FF6C46758111C49C47CD49B1

    pause 0.5

    stop music fadeout 5
    $ sys_music_current_file = ""

    pause 1.5

    $ set_window("イベントモード")
    
    show left_title (_("调查组")) as left_title
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 2

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    hide left_title
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_FF7C34936A8D4217BC2F765AF4D7D8C8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 1

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_2D9DBFACED644B2882B38D7E4606CBF6 as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_A7D458B112A543F691F4223B8946B813 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_4E2835E547304DD1A4EE59EDDEA933C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "校长室里真的会有记载{color=#00FFFF}封印恶灵的方法{/color}的书吗？"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.2

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_DB0BD4A5526E46CCA60D1A469CF4D475 as tag_3482C372784E44A89E382266A93F2B14 at center_top zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C223850065F6443080205D1F61C04C98 "可能。\n刚才给你们的符咒也是从校长那里拿到的，他肯定对这类事情很明白。"

    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_DB0BD4A5526E46CCA60D1A469CF4D475 as tag_3482C372784E44A89E382266A93F2B14 at left_top zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    show rs_image_76A6FDF06765424DBC1E2AE1C0D1ADA1 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "原来如此……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_890FBC4A7D5344C091041A7DCE93EA3E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不对，居然会给学生符咒，\n这个校长是想做什么！？"

    show rs_image_6C6AB7F5377C4CE7869A802109670AE0 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "太奇怪了！……难道说是被校长欺负了……"

    show rs_image_BD5D4967AAB3422CB365C33860DE9016 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "哈哈，不，不是那样的请放心。那个人可是发誓保护整个学园的。"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_4E2835E547304DD1A4EE59EDDEA933C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_8AD2DDD7544B43C4A6A69B2DAC1465E5 as tag_4233D225ED0D43968B3A0D890F587FEB at right_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_7009C1117C004F51829614A203C67DE7 "作哉前辈，一直不说话呢，怎么回事？"

    show rs_image_B276F958003A43A59D0E1DAFE5CCAA4E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "诶？啊，不……没什么……"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_DB0BD4A5526E46CCA60D1A469CF4D475 as tag_3482C372784E44A89E382266A93F2B14 at right_top zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C223850065F6443080205D1F61C04C98 "在担心校舍里狗狗的事情吗？应该是你在照顾吧。"

    show rs_image_93E7311915BC403AAFABACFA29A7DDB1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嗯。"

    show rs_image_BD5D4967AAB3422CB365C33860DE9016 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "那孩子和其他大人一样都睡过去了，所以不用担心。"

    show rs_image_C4B36F704BDC4BB295B684E3F4796279 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C223850065F6443080205D1F61C04C98 "动物很敏感的，\n事件还没有发生时它就已经好好藏起来然后睡过去了。放心。"

    show rs_image_D4AF6091BD0341CFBF561C2744F3FD83 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "真、真的！？太好了……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_4B8BD646B04149A38936E9329ADBBC5D as tag_3482C372784E44A89E382266A93F2B14 at center_top zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C223850065F6443080205D1F61C04C98 "那么接下来就请你们好好努力了。再见。"

    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_E62168EC90B7417CB5F5DD87BA487392 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_7009C1117C004F51829614A203C67DE7 "那个……请等一下。你难道是……"

    $ zorder_tag_3482C372784E44A89E382266A93F2B14 = 300
    show rs_image_756F57F2C6974C2B9E435BA505465356 as tag_3482C372784E44A89E382266A93F2B14 at right_top zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C223850065F6443080205D1F61C04C98 "哈哈——请保密。"
    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    show rs_image_DB0BD4A5526E46CCA60D1A469CF4D475 as tag_3482C372784E44A89E382266A93F2B14 zorder zorder_tag_3482C372784E44A89E382266A93F2B14 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "……你也要做好心理准备。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_3482C372784E44A89E382266A93F2B14
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.3

    show rs_image_BAB1EF8BB1E8402E9731FA917EC2849D as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_7009C1117C004F51829614A203C67DE7 "诶？"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_BAB1EF8BB1E8402E9731FA917EC2849D as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 0.7

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_BAB1EF8BB1E8402E9731FA917EC2849D as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_25B4CA5E7DB54A70B991383AB9E2522F as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_D4AF6091BD0341CFBF561C2744F3FD83 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "好！那就开始找书。这时候就别管什么校长室了，翻个底朝天！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_7C2E9E7F5F0D47D1BF49B03E25F8C320 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哇～！一想到能做平时不能做的事就有些小激动呐！"

    window hide

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 at center_top zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "这可不行啊。那种无礼的事可不能做。"

    hide tag_82C54ADE966440F7B34C83D13555B813
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E62168EC90B7417CB5F5DD87BA487392 as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_D14C1328F4484EBE997C5CE2D0C119BD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_E54A2DFBC85F4C20B96B216AE6D076B7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "！？你是！！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "出、出现了！！"

    rs_character_7009C1117C004F51829614A203C67DE7 "这只妖怪……"
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Thunder 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Thunder 1.ogg"

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 at center_top zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    extend "和其他妖怪等级不一样！{nw}"
    if sys_music_current_file != "sound/BGM/Final battle.ogg":
        play music "sound/BGM/Final battle.ogg" loop
        $ sys_music_current_file = "sound/BGM/Final battle.ogg"

    extend ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_AB6DB43EEF134D37A5FCF4185693D36B as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "哦呀？这还真是……不小心把作为这所学园的学生来说尚小的朋友卷进来了呐。"

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "不过非常可爱，非常可“口”……请务必光临我们的乐园。"

    hide tag_82C54ADE966440F7B34C83D13555B813
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 400
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_EAC123C74DA14C4DA194C5F35E8A772D as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_36CE26546DFB496C998891D769988B5D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_AD087A5E71C5437FB7CB2C447B5E97BD as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "混蛋……什么乐园！绝不会让你动他们一根汗毛的！！"

    show rs_image_890FBC4A7D5344C091041A7DCE93EA3E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "前、前辈不要勉强了！这种等级前辈一个人是敌不过的！"

    show rs_image_486F70F1E27D43BC868FA3ADA0B574BE as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "说什么呢，不是好好从雪绪那里拿到力量了嘛。\n肯定能行，刚才那家伙也这么说了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_30B3B1D90FB849C3B3D248154907D000 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7009C1117C004F51829614A203C67DE7 "（对了，九尾，交换！处理掉这只怪物！！）"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『…………。』"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 400
    show rs_image_B0AE196FCA0347DEACA52C0CB36FB8EE as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "（九尾？呐，九尾！！）"

    window hide

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.5

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_C0AC7060D45F43C8A44ABBEE4810EF9B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "这种家伙得赶紧干掉，今天还没和小翼出去散步呢！"

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 at left_top zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "哦……"

    window hide

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_82C54ADE966440F7B34C83D13555B813
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_6F41BEB29B0744ED8F25360004E87AB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_A7EEAA961C214874BEBADA168E79984E = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BF15F042F4A241789DDE485A5CD928DE as tag_A7EEAA961C214874BEBADA168E79984E at center_top zorder zorder_tag_A7EEAA961C214874BEBADA168E79984E onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_D21FC549273B4A1ABB90AEF39DEAD87B "……"

    hide tag_A7EEAA961C214874BEBADA168E79984E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_609B18A24DC64637943B3F2C0430365E as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_52BE5F9300564226BA402BC7C43E0B3A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "就是那个！那家伙拿着的箱子！那就是我说的箱子！"

    show rs_image_8DFCEBB60ED1479B8679685FD7E31FFB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可、可是，从刚才就一直……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A7EEAA961C214874BEBADA168E79984E = 300
    show rs_image_BF15F042F4A241789DDE485A5CD928DE as tag_A7EEAA961C214874BEBADA168E79984E at center_top zorder zorder_tag_A7EEAA961C214874BEBADA168E79984E onlayer master
    show rs_image_6F41BEB29B0744ED8F25360004E87AB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D21FC549273B4A1ABB90AEF39DEAD87B "慎太郎……又、见面了……这次一定要、让你满足……"

    hide tag_A7EEAA961C214874BEBADA168E79984E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_282C9F7BE25049678AA10F7136B6FC9E as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_52BE5F9300564226BA402BC7C43E0B3A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那个，呃……？请问阁下是……？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "一直都在念叨慎酱……到底为什么呐？发生什么了？"

    show rs_image_0600CCA9D8E5458687C3A5F9EE6CB6C5 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你……该不会想跟我说和妖怪都做过？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_C43CDCE2089F485094F071FBC81A3038 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "怎怎怎怎么可能——！"

    show rs_image_FD381C6412CC4FE7A52F90CB708C2E44 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可、可是，很明显目标只有慎酱。根本就对我们毫不关心……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    show rs_image_A95041BF36BD457E9EEEC67FBC46A672 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "难道是被慎酱玩弄苦不堪言自杀后……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Duang 1.ogg"

    show rs_image_B4378AE67E6A4B08A37DF8E3C2E65B17 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "别说那么可怕的话！！我不觉得自己有那么鬼畜。"

    show rs_image_17BD4756EE4547C7999FB0FE558D991B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "一般加害者都是意识不到自己的罪过的。"

    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "真的假的——我什么时候和那种人玩过来着？！"

    show rs_image_A3D6CADEDC674400B7CD24D81BE7CC16 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "唔～明明已经长过很多次记性了，一旦交出身体，后面就会有相当多麻烦事。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_4E199F4B91FA4890953552A1AF55627D as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你还真是对那些事老这么马虎！！只限今天给我把所有事干净处理掉！！！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_3D554AE725A4498287A90C6C9BCBB679 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "唔……上就上谁怕谁。猛男慎太郎，上了……"

    pause 0.3

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A7EEAA961C214874BEBADA168E79984E = 300
    show rs_image_BF15F042F4A241789DDE485A5CD928DE as tag_A7EEAA961C214874BEBADA168E79984E at center_top zorder zorder_tag_A7EEAA961C214874BEBADA168E79984E onlayer master
    show rs_image_6F41BEB29B0744ED8F25360004E87AB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D21FC549273B4A1ABB90AEF39DEAD87B "慎太郎……慎太郎……"

    hide tag_A7EEAA961C214874BEBADA168E79984E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_A3D6CADEDC674400B7CD24D81BE7CC16 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_52BE5F9300564226BA402BC7C43E0B3A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "对不起，关于你和我之间究竟发生过什么，说实话我已经记不起来了。"

    show rs_image_4BA562125E914D049B3A68EC3F0DB8A1 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "但正因是我，想必做了让你很难受的事。"

    show rs_image_3CA5C53D5B5F4402ABE043400BD0BCE1 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不过，我现在已经有了重要的人。不论其他人再怎么引诱，我都不会动摇了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D554AE725A4498287A90C6C9BCBB679 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "所以，就请……忘了我！！找个好人嫁了吧！！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_0600CCA9D8E5458687C3A5F9EE6CB6C5 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_15C167A596C24CA5ABBDDF10433FFF71

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哇——简直就像花心男的分手现场——"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "作为我的恋人真是太差劲了。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A7EEAA961C214874BEBADA168E79984E = 300
    show rs_image_BF15F042F4A241789DDE485A5CD928DE as tag_A7EEAA961C214874BEBADA168E79984E at center_top zorder zorder_tag_A7EEAA961C214874BEBADA168E79984E onlayer master
    show rs_image_6F41BEB29B0744ED8F25360004E87AB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D21FC549273B4A1ABB90AEF39DEAD87B "…………"

    hide tag_A7EEAA961C214874BEBADA168E79984E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_A3D6CADEDC674400B7CD24D81BE7CC16 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_52BE5F9300564226BA402BC7C43E0B3A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "怎样？所以请不要做这种事了，把箱子交给我们好不好。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A7EEAA961C214874BEBADA168E79984E = 300
    show rs_image_BF15F042F4A241789DDE485A5CD928DE as tag_A7EEAA961C214874BEBADA168E79984E at center_top zorder zorder_tag_A7EEAA961C214874BEBADA168E79984E onlayer master
    show rs_image_6F41BEB29B0744ED8F25360004E87AB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D21FC549273B4A1ABB90AEF39DEAD87B "……那就"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    extend "和我做……"

    hide tag_A7EEAA961C214874BEBADA168E79984E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_609B18A24DC64637943B3F2C0430365E as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_C9A169B5FECE487BAE71B3017B79B0B4 as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_52BE5F9300564226BA402BC7C43E0B3A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈！？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这混蛋……！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A7EEAA961C214874BEBADA168E79984E = 300
    show rs_image_175B061199E04D9EB2CB6F9FA9279C56 as tag_A7EEAA961C214874BEBADA168E79984E at center_top zorder zorder_tag_A7EEAA961C214874BEBADA168E79984E onlayer master
    show rs_image_6F41BEB29B0744ED8F25360004E87AB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D21FC549273B4A1ABB90AEF39DEAD87B "只要和我做，就给你们……"

    hide tag_A7EEAA961C214874BEBADA168E79984E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_F1BC27BCAA724436A6E40C4DD41F6CDD as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_FF4A588462534B15B9D5F444704F26BB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_52BE5F9300564226BA402BC7C43E0B3A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "世上也有这种人呢。三酱……？"

    show rs_image_50D82C35F258450C9BFE07520E310720 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这些家伙思维早就腐朽了，我们就算讲道理也他们听不进去。"

    show rs_image_4ADA38AD8AC240F48211FBA4F8807972 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就是说已经……"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_A3D6CADEDC674400B7CD24D81BE7CC16 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我、我明白了……如果靠这副身体能帮到大家的话，我也会很欣慰的。"

    window hide

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_4BA562125E914D049B3A68EC3F0DB8A1 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_A7EEAA961C214874BEBADA168E79984E = 300
    show rs_image_175B061199E04D9EB2CB6F9FA9279C56 as tag_A7EEAA961C214874BEBADA168E79984E at right_top zorder zorder_tag_A7EEAA961C214874BEBADA168E79984E onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.7

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Search 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Search 1.ogg"

    pause 0.9

    window show

    rs_character_D21FC549273B4A1ABB90AEF39DEAD87B "……（吞口水）"

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    # Gallery unlock: images/CG/The-inbelieveble-of-school/The-inbelieveble-of-school 3.png
    $ zorder_rs_image_4253E3A8DC4C43E586A3DDBA53A4A6AF = -100
    show rs_image_4253E3A8DC4C43E586A3DDBA53A4A6AF as rs_image_4253E3A8DC4C43E586A3DDBA53A4A6AF zorder zorder_rs_image_4253E3A8DC4C43E586A3DDBA53A4A6AF onlayer master
    hide rs_image_4253E3A8DC4C43E586A3DDBA53A4A6AF

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_4253E3A8DC4C43E586A3DDBA53A4A6AF as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_28F784D09B6C4DC7923149F266748707 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "趁大意之时强行突破了——！！上了白痴呆毛！"

    window hide

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    hide tag_A7EEAA961C214874BEBADA168E79984E
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_3844B6CC2B84472FBFD019B9A7A05016

    pause 1

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "抓住了——！！慎酱，趁现在！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "一发完事！！！"

    rs_character_D21FC549273B4A1ABB90AEF39DEAD87B "你们……！放开！慎太郎……慎太郎……！！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……谢谢你那么中意我。可是……！不行就是不行！！"

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 2.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "{size=28}来世！！继续加油吧！！！{/size}"

    window hide

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Bell 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Bell 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 3.ogg"

    $ zorder_tag_A7EEAA961C214874BEBADA168E79984E = 300
    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_13E25CE20F2E49BBABB9895D06E9CB96 as tag_A7EEAA961C214874BEBADA168E79984E at center_top zorder zorder_tag_A7EEAA961C214874BEBADA168E79984E onlayer master
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_52BE5F9300564226BA402BC7C43E0B3A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A66B9E9678E74FA481DCD625BCC55869

    window show

    rs_character_D21FC549273B4A1ABB90AEF39DEAD87B "唔啊啊啊啊啊啊……啊啊啊啊……"

    window hide

    pause 0.5

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Finger Snap 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    hide tag_A7EEAA961C214874BEBADA168E79984E
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 1.5

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_23970544C9224BB4B785B8FB367471BC as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_4BA562125E914D049B3A68EC3F0DB8A1 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_FF06A916FD6F481293533497D0DA6110 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "太好了！干掉了！"

    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "任务完成！！做到了呐，慎酱！！"

    show rs_image_A3D6CADEDC674400B7CD24D81BE7CC16 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯……"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_23970544C9224BB4B785B8FB367471BC as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_4BA562125E914D049B3A68EC3F0DB8A1 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "奥村……既然已经和我交往，这样的结果便是无可奈何。\n"
    show rs_image_05869A4FEB35497BB941E279D075CC45 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不是你的错，不要失落。"
    show rs_image_A2E7C1AAED834AD7861668C6EE330F80 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "三酱……谢谢。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔——我也在好不好——不要擅自进入两人世界啊——"

    window hide

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1.4

    $ set_window("イベントモード")
    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_BCAC5076DD214C629BDF5B88F585E30E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_BDC291B5081C42168C8A1886FB5FACD3 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_9D80F5870F2249459239D301CED743C6 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.4

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "一路平推到这里了。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "那事不宜迟赶快救出大家！"

    show rs_image_FE681BB78F1F4D339A2566A5D9707982 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "……不，在那之前应该至少还得打一场。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_293AA514A24E4A44BB395EC06789F57B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=500, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "大、大家要加油哦。我就在一旁好好支援……"

    window hide

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_9F9D06EDAE09497BA369F17610C49EF8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    pause 1.2

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Thunder 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Thunder 1.ogg"

    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 300
    show rs_image_757537DAAA5F421595F24FFD01860C20 as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    window show

    rs_character_079949A107134E47B24110C78D2FA0CF "吼——哈！你们终于来了！！真是好好关照我的部下们了！"

    show rs_image_562CBE7FE74549F0894E5ADA22F9A4DA as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "可是遗憾，这种恶劣的孩子我们的乐园里不需要！\n现在就送你们上路，做好准备！"

    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_BCAC5076DD214C629BDF5B88F585E30E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_A5766C99781F455DA534AE7F92F38CA4 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_5739B888853E4BCE83F4B5FFEC74A1C2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_621923550F3B42DEAC63D2D352B2183B as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "来了！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 300
    show rs_image_9F9D06EDAE09497BA369F17610C49EF8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_562CBE7FE74549F0894E5ADA22F9A4DA as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "上"
    show rs_image_A672631E2B514DA2B6388CDF6C0BD900 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……之前，“送你们上路”这句话先撤回。\n稍微受点伤也就老实了吧！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_757537DAAA5F421595F24FFD01860C20 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "后会好好调教你们，让你们陷于快感，复试合格后，重新成为我们的伙伴！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_D966548D39864E42A031D80097F6944B as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_621923550F3B42DEAC63D2D352B2183B as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "还想手下留情？别小看人了"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不要小看我每天和哥哥一起锻炼出来的毅力！"

    show rs_image_562CBE7FE74549F0894E5ADA22F9A4DA as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "哦……真会说。不错，我最喜欢对这种自以为是的人出手了。"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 100
    show rs_image_6DBEF4C3CA3942C490BB486CFC040195 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "别废话了，赶紧打。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_8CD556F98525469D9B60EF719D590FB8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    show rs_image_D3DEB10466FE4B59B22508F112B7DC57 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "唔哦！？"

    show rs_image_504AC66EBE6F443DA669461609923D2C as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "只有我才能给空快感！！"
    
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_51451FBF94C8444AA5696178E72CE210 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_4CE0B471CB9A4894AEAB218AE895C0CF as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_D3DEB10466FE4B59B22508F112B7DC57 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "呃！"

    show rs_image_63B7FCD9DF38442BA0683EF60F550969 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "看，就这点能耐根本不足以当对手！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_052F34847F0D47A8B9559273E4FAA7C6 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    show rs_image_4D8F1D6A70C24A34A3E6C37B69619470 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_D9A3137B80B14CE785B79C9B543E0786 as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_D3DEB10466FE4B59B22508F112B7DC57 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "?！！"

    window hide

    pause 0.5

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_A366FE92B81D404585614E7D29CFAD20
    hide tag_DD234F3A788F4BD5954C8F12B53FB442
    with rs_effect_2604FEB26CCC4082BC90CCE4B5300A9E

    pause 0.7

    window show

    rs_character_079949A107134E47B24110C78D2FA0CF "这些家伙是怎么回事……和其他人根本水准不同……\n再说为何这些人能打到我！？"

    show rs_image_4D9B5CDCB00648DAB664199B1CA9D163 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "算了，反正这种攻击也不痛不痒。但也不能一直处于劣势……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_A672631E2B514DA2B6388CDF6C0BD900 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "……哦呀？"
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_293AA514A24E4A44BB395EC06789F57B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=500, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_BCAC5076DD214C629BDF5B88F585E30E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    extend "那边不藏着个看上去超弱的嘛！！"

    show rs_image_BA79E21F6467495A849CFF33257777BB as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "噫！？哇、哇啊啊啊！！"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_D8F88F968B9E4B3CBEED302C0FA2B323 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_9F9D06EDAE09497BA369F17610C49EF8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "一之濑君！！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 200
    show rs_image_293AA514A24E4A44BB395EC06789F57B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=250, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_562CBE7FE74549F0894E5ADA22F9A4DA as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_15C167A596C24CA5ABBDDF10433FFF71

    rs_character_079949A107134E47B24110C78D2FA0CF "抓～到～你～了。你们是这孩子的朋友对不？"

    rs_character_079949A107134E47B24110C78D2FA0CF "不想让朋友受伤的话，就快点屈服听从我的命令～"

    hide tag_3FA60293C6724C72B5FECC927A2B7804
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_2155B7020F8F4BDE8F91FA487FF49C6A as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_BF3FF6B64ED742E38A1DC78DBAC48031 as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "卑鄙！！这样也算男人？！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 200
    show rs_image_CDE407350E4A49AC8933C6D199FE9A13 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=250, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_757537DAAA5F421595F24FFD01860C20 as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "本来就不是哦～我和你们一样是男孩子哦！\n啊，多么美妙，这里除了男孩子别无其他。"

    show rs_image_562CBE7FE74549F0894E5ADA22F9A4DA as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "好了，听我号令，成为同伴。"

    window hide

    hide tag_3FA60293C6724C72B5FECC927A2B7804
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_B3256942BF0C4567BBE53ABE31023DE2 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_9D80F5870F2249459239D301CED743C6 as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1

    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_864148A734BC4812B08CBBF3D01B3978 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "只有男孩子……啊。那这个乐园里没有女孩子了？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 200
    show rs_image_A2534044EF094540BC82F97E1E03D950 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=250, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_562CBE7FE74549F0894E5ADA22F9A4DA as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "当然！本就是杂物，一经发现即刻排除！！"

    hide tag_3FA60293C6724C72B5FECC927A2B7804
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_5EEBBCC1A1DD424FA293CA4EA0C6C4C6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "就是说……不论如何，我都不可能是同伴了呢。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_229EB6C626CB4AD79FA6063567685C64 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_9241757E0E3A46D8A082C1EF9568D9F4 as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_71FE39D448264F1B86FB7E3459E84840 "！？"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_02AF4E98AE404A37BBF5189D1BD66AE6 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_CB70B28808D840B5A51436CA4E858F49 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "{size=14}……哦！{/size}"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_B3256942BF0C4567BBE53ABE31023DE2 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_5EEBBCC1A1DD424FA293CA4EA0C6C4C6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_B62939FE188646B19F924D8B074E376A as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不要那么说嘛，忍{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#FF80FF}酱{/color}！！"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_C8509382B1E34741B9130C4CA5DE55D6 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……啊。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_A9272CFB7442404397033A5CA243E723 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空！不要暴露绫濑的秘密！"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "会不能再和{color=#FF80FF}她{/color}一起的哦！？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 200
    show rs_image_6536F8ADBA294923ABCC248AEAB17528 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=250, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_4D9B5CDCB00648DAB664199B1CA9D163 as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_A9C92E63BBCE424D87EBFD571BAB26DE "欸。诶？？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_4683860EE22143EDB1980090E250F53A as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_864148A734BC4812B08CBBF3D01B3978 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_C8509382B1E34741B9130C4CA5DE55D6 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "谢谢你们。可这样下去就太对不起一之濑君了。"

    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "因为，本来被抓的应该是我。我……其实是"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/God 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/God 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_140B552F50584401971F8DF480089BE0

    extend "{size=32}{color=#FF80FF}女孩子{/color}{/size}{size=32}！！{/size}"

    window hide

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 200
    show rs_image_BA79E21F6467495A849CFF33257777BB as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_9B664D5A09A14B7D83F83FD0EEE7A1F0 as tag_3FA60293C6724C72B5FECC927A2B7804 at left_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 2.ogg"

    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cat 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cat 2.ogg"

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Brakes 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Brakes 1.ogg"

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Battle 6.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Battle 6.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_46726D80EC7B4D48AD2EFED4CDD37F1C as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.6

    window show

    rs_character_A9C92E63BBCE424D87EBFD571BAB26DE "{size=32}诶诶诶诶！！！？？？{/size}"

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_9F9D06EDAE09497BA369F17610C49EF8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_864148A734BC4812B08CBBF3D01B3978 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_DCD8B79F49964D74AC066FB7F605BC72

    pause 0.4

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "本来校长对我说女孩子也可以，靠走后门入学了，没想到现在会这样……"

    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "最喜欢男孩子的妖怪先生应该不会伤害一之濑君的。"

    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那样的话人质就没有意义了。妖怪先生自己应该是最清楚的。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 200
    show rs_image_BA79E21F6467495A849CFF33257777BB as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_052F34847F0D47A8B9559273E4FAA7C6 as tag_3FA60293C6724C72B5FECC927A2B7804 at left_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "唔……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "既然如此我来当人质。一之濑君一直被这么抓着太可怜了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 200
    show rs_image_293AA514A24E4A44BB395EC06789F57B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_4D9B5CDCB00648DAB664199B1CA9D163 as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不不、不要在意我～！我的战斗力根本比不上绫濑君……酱！"

    show rs_image_A672631E2B514DA2B6388CDF6C0BD900 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "既、既然如此你们三个赶快投降！只要照做我就放了他！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_83253C644D7341D899A80F5E86570559 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "请不要误会，这只是我的个人意愿，他们还是会继续战斗的……"

    show rs_image_03C1A439835A4147A5447DAA1669CA0C as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "而且，对妖怪先生来说，对手能简单地屈服不是更有趣吗？"

    show rs_image_4D9B5CDCB00648DAB664199B1CA9D163 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "……你还挺聪明。好，我也能得到好用的人质，不是坏事。"

    rs_character_079949A107134E47B24110C78D2FA0CF "好，交换。"

    show rs_image_541BC7417880499BB6151B8C86902E0A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "谢谢。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 200
    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_4D9B5CDCB00648DAB664199B1CA9D163 as tag_3FA60293C6724C72B5FECC927A2B7804 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.6

    show rs_image_C533295FFF704695B54B98B9893D98B9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "绫、绫濑同学……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 200
    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_4D9B5CDCB00648DAB664199B1CA9D163 as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_079949A107134E47B24110C78D2FA0CF "快过来。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=250, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我明白。"

    window hide

    pause 0.6

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_5739B888853E4BCE83F4B5FFEC74A1C2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 3.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_8CD556F98525469D9B60EF719D590FB8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    show rs_image_ABB55DB1211049EFB8F17F920B8EE8F2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    window show

    rs_character_079949A107134E47B24110C78D2FA0CF "唔！？为、为何……你、你算计我！？"

    rs_character_079949A107134E47B24110C78D2FA0CF "卑鄙小人！！这也算男人？！"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "……啊，并不是……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不，我就是。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_A9C92E63BBCE424D87EBFD571BAB26DE "诶？诶？？"

    if sys_music2_current_file != "sound/Effect Sound/Cut the wind 1.ogg":
        play music2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_A5766C99781F455DA534AE7F92F38CA4 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "愚蠢！绫濑可是顶天立地的男子汉！！"

    if sys_music2_current_file != "sound/Effect Sound/Cut the wind 1.ogg":
        play music2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_621923550F3B42DEAC63D2D352B2183B as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "说是要做出男孩子的乐园什么的，目光短浅！！"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_6942001DFE4B4C088A665365008EB0AF as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_808C1269C48143C38C3000CB647CB3BF as tag_073D4E2B5E224963B025F95C92ED797A at center_bottom zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_4D8F1D6A70C24A34A3E6C37B69619470 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_E04DFA4059EE40D18051F1CAA5223C75 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_51451FBF94C8444AA5696178E72CE210 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.5

    show rs_image_052F34847F0D47A8B9559273E4FAA7C6 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_A366FE92B81D404585614E7D29CFAD20
    hide tag_DD234F3A788F4BD5954C8F12B53FB442
    with rs_effect_062874A7535D428098A6E643E4778255

    pause 0.8

    window show

    rs_character_079949A107134E47B24110C78D2FA0CF "！！你们这群家伙有什么资格骂我卑鄙……！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_4D9B5CDCB00648DAB664199B1CA9D163 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_AC46DBAAAEE24C10AECA19E0EDA27051

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "孩子们的三观尚未成熟，用大人的话说就是仍存在讲不通道理的残酷一面。"

    window hide

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_9B664D5A09A14B7D83F83FD0EEE7A1F0 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    show rs_image_6DBEF4C3CA3942C490BB486CFC040195 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    pause 0.5

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Boom 1.ogg"

    # Gallery unlock: images/CG/The-inbelieveble-of-school/The-inbelieveble-of-school 1.png
    $ zorder_rs_image_1AB3B872D6C54A87BBE10747A2C3FDAD = -100
    show rs_image_1AB3B872D6C54A87BBE10747A2C3FDAD as rs_image_1AB3B872D6C54A87BBE10747A2C3FDAD zorder zorder_rs_image_1AB3B872D6C54A87BBE10747A2C3FDAD onlayer master
    hide rs_image_1AB3B872D6C54A87BBE10747A2C3FDAD

    # Gallery unlock: images/CG/The-inbelieveble-of-school/The-inbelieveble-of-school 1-1.png
    $ zorder_rs_image_21F6C31513A34EA8A8B2E622273CDD7F = -100
    show rs_image_21F6C31513A34EA8A8B2E622273CDD7F as rs_image_21F6C31513A34EA8A8B2E622273CDD7F zorder zorder_rs_image_21F6C31513A34EA8A8B2E622273CDD7F onlayer master
    hide rs_image_21F6C31513A34EA8A8B2E622273CDD7F

    $ zorder_tag_A366FE92B81D404585614E7D29CFAD20 = 0
    $ zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 = 100
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_1AB3B872D6C54A87BBE10747A2C3FDAD as tag_A366FE92B81D404585614E7D29CFAD20 at center_bottom zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    show rs_image_21F6C31513A34EA8A8B2E622273CDD7F as tag_DD234F3A788F4BD5954C8F12B53FB442 at center_bottom zorder zorder_tag_DD234F3A788F4BD5954C8F12B53FB442 onlayer master
    show rs_image_FA71A79D75754B70A790643847D4F2C5 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 1

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_A366FE92B81D404585614E7D29CFAD20
    hide tag_DD234F3A788F4BD5954C8F12B53FB442
    with rs_effect_DCD8B79F49964D74AC066FB7F605BC72

    pause 0.5

    show rs_image_052F34847F0D47A8B9559273E4FAA7C6 as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_079949A107134E47B24110C78D2FA0CF "唔——！"
    show rs_image_562CBE7FE74549F0894E5ADA22F9A4DA as tag_3FA60293C6724C72B5FECC927A2B7804 zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "不过，那种攻击毫无意义！！\n我和那边的杂鱼们是不同的！！"

    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_BCAC5076DD214C629BDF5B88F585E30E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_889F2AF205E140788BE374915197CA80 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_CA32B3074CBF4DB08BA59AE12141A4F7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_B62939FE188646B19F924D8B074E376A as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "呼……应该已经给予大量伤害了，为何完全无效！？"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "居然会有这么顽强的妖怪……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "没有什么必杀的底牌的话……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_C533295FFF704695B54B98B9893D98B9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=500, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "（底牌……"
    stop music fadeout 1
    $ sys_music_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Bell 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Bell 1.ogg"

    show rs_image_332D35DF942A4E11AF6CD9B932EC0FD0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    extend "底牌！？）"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 300
    show rs_image_9F9D06EDAE09497BA369F17610C49EF8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_562CBE7FE74549F0894E5ADA22F9A4DA as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_079949A107134E47B24110C78D2FA0CF "既然你们是那种想法，沟通就不需要了！\n人质还是要这边这个超弱的来当！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_2155B7020F8F4BDE8F91FA487FF49C6A as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_7DC581F0926C46E1B9B46277F2729C93 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "糟了！！"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "快逃，一之濑！"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_C197AB750EF8424887D8CF5ECCE7226B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_BCAC5076DD214C629BDF5B88F585E30E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我、我也是能……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_79A20385C6FE4DBBA5012549CF15BF35 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    if sys_music_current_file != "sound/BGM/Final battle.ogg":
        play music "sound/BGM/Final battle.ogg" loop
        $ sys_music_current_file = "sound/BGM/Final battle.ogg"

    extend "看招！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Bell 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Bell 1.ogg"

    # Gallery unlock: images/CG/The-inbelieveble-of-school/The-inbelieveble-of-school 4-1.png
    $ zorder_rs_image_9C292825A57E4A5E85C7B9686E18FC48 = -100
    show rs_image_9C292825A57E4A5E85C7B9686E18FC48 as rs_image_9C292825A57E4A5E85C7B9686E18FC48 zorder zorder_rs_image_9C292825A57E4A5E85C7B9686E18FC48 onlayer master
    hide rs_image_9C292825A57E4A5E85C7B9686E18FC48

    show rs_image_9C292825A57E4A5E85C7B9686E18FC48 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    rs_character_079949A107134E47B24110C78D2FA0CF "{size=28}唔啊啊啊啊啊啊！！！！{/size}"

    window hide

    pause 0.6

    $ zorder_tag_3FA60293C6724C72B5FECC927A2B7804 = 300
    show rs_image_9F9D06EDAE09497BA369F17610C49EF8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_9B664D5A09A14B7D83F83FD0EEE7A1F0 as tag_3FA60293C6724C72B5FECC927A2B7804 at center_top zorder zorder_tag_3FA60293C6724C72B5FECC927A2B7804 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_3FA60293C6724C72B5FECC927A2B7804
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 1.4

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 300
    show rs_image_229EB6C626CB4AD79FA6063567685C64 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_9241757E0E3A46D8A082C1EF9568D9F4 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欸……怎么了？妖怪消失了……"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "这是……{color=#FFFF00}符咒{/color}？一之濑用的？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_C18E9E3152D24005B446B9C4987139A3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "哈……哈……之前从常磐前辈那里得到的。绫、绫濑君说起“底牌”时突然想到……"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "原来这样……不管怎么说帮大忙了。打倒了最强的那个呢。"

    show rs_image_9071DE7B7E5343C897D93F24F8DF7BAF as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那……那赶快救出大家！"

    window hide

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1.4

    $ set_window("イベントモード")
    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_FF7C34936A8D4217BC2F765AF4D7D8C8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.9

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_AD087A5E71C5437FB7CB2C447B5E97BD as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你这家伙！！无耻！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 at left_top zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "呵呵，弱点是你自己暴露出来的，为何要怨我？要怨也怨自己的愚蠢。"

    window hide

    show rs_image_AB6DB43EEF134D37A5FCF4185693D36B as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_E54A2DFBC85F4C20B96B216AE6D076B7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_E04DFA4059EE40D18051F1CAA5223C75 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_82C54ADE966440F7B34C83D13555B813
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_E28C2DB578FC4F31B06A10BB926E6BE4 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "唔！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_36CE26546DFB496C998891D769988B5D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_3B4C660F421B4BE392BB540B580F0339 "穗海前辈！！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 at left_top zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "哦呀，已经结束了？我还是很喜欢强势的孩子的，再多玩一会也好呀。"

    hide tag_82C54ADE966440F7B34C83D13555B813
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_EFDEEDA02727406390376B91A7A8F75D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你这下贱混蛋……！就如你所愿……！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_AD087A5E71C5437FB7CB2C447B5E97BD as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 at left_top zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.3

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    show rs_image_A39671BE6D8246F5ACCB45CA04C8C3D1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_4CBCF132AF8F49E38C726D5800545B50 as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "哦。"

    show rs_image_E28C2DB578FC4F31B06A10BB926E6BE4 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "！！"

    show rs_image_FBB5A2065F074D4BA71B4BEDF4970C32 as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "多少次都是一样的。你是无法下手攻击这个样子的我的！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "你的力量之源正是你所重视的一切。但反过来说，那也是你的弱点。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_36CE26546DFB496C998891D769988B5D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "住、住手！！不、不许欺负前辈了！！"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_82C54ADE966440F7B34C83D13555B813
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_9CB24AF1FF544F0F9A754DA0E9105FBB as tag_82C54ADE966440F7B34C83D13555B813 at center_top zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "那就和我们一起成为乐园的一部分。拒绝的话，也只会重复现在的一切。"

    hide tag_82C54ADE966440F7B34C83D13555B813
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_A7D458B112A543F691F4223B8946B813 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_C0AC7060D45F43C8A44ABBEE4810EF9B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "开什么玩笑！你们所谓的乐园对小翼来说就是地狱！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_9CB24AF1FF544F0F9A754DA0E9105FBB as tag_82C54ADE966440F7B34C83D13555B813 at center_top zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "那与我无关。"
    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "对了，这个{color=#FFFF00}符咒{/color}也撕掉好了。"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Bell 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Bell 1.ogg"

    hide tag_82C54ADE966440F7B34C83D13555B813
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Break 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.9

    $ zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 = 100
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_4177AE20CFD04B4C908EB1979945B817 as tag_5DC444A6262A4FCE9BF63B4338E21A74 at center_bottom zorder zorder_tag_5DC444A6262A4FCE9BF63B4338E21A74 onlayer master
    show rs_image_FF7C34936A8D4217BC2F765AF4D7D8C8 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_890FBC4A7D5344C091041A7DCE93EA3E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at left_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_EFDEEDA02727406390376B91A7A8F75D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "唔、混蛋……"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊……"
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_E62168EC90B7417CB5F5DD87BA487392 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_36CE26546DFB496C998891D769988B5D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    extend "阿雪！这样下去穗海前辈就！"

    show rs_image_ABB2A951B8D345A092CC374396221386 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "我明白！可是……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_AD087A5E71C5437FB7CB2C447B5E97BD as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "这、这次一定！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_0021272C60ED4B518AF2F86B9C5284DB as tag_82C54ADE966440F7B34C83D13555B813 at left_top zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "没用的。"

    window hide

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_82C54ADE966440F7B34C83D13555B813 at center_bottom zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "唔，这次是猫……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "然后……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "兔、兔子……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "继续……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈……！小熊猫……！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Monster 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Monster 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "你很喜欢动物嘛。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 200
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_1DC349F94DE94D6FACCF6AD451DDAE8E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "好厉害——袋熊！矮矮的毛茸茸的！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_82C54ADE966440F7B34C83D13555B813
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_3B4C660F421B4BE392BB540B580F0339 "前辈守备范围真广……话说原来猫也可以。\n"
    show rs_image_7C2E9E7F5F0D47D1BF49B03E25F8C320 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "这下看到希望了呢。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_D14C1328F4484EBE997C5CE2D0C119BD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "不对不是说这个的时候！！"
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_ABB2A951B8D345A092CC374396221386 as tag_4233D225ED0D43968B3A0D890F587FEB at left_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_36CE26546DFB496C998891D769988B5D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "阿雪！！做点什么啊！"

    show rs_image_890FBC4A7D5344C091041A7DCE93EA3E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "我不想继续看到前辈被玩弄了！！"

    show rs_image_B0AE196FCA0347DEACA52C0CB36FB8EE as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "我明白，我明白可是……！"

    pause 0.4

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_EAC123C74DA14C4DA194C5F35E8A772D as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_7009C1117C004F51829614A203C67DE7 "（呐九尾！为什么从刚才开始一直无视我！！）"

    show rs_image_30B3B1D90FB849C3B3D248154907D000 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "（这样下去大家都会被关在这里的！）"

    show rs_image_ABB2A951B8D345A092CC374396221386 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "（因为自己能逃出去就要见死不救！？我绝对不要这样！！）"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『……。』"

    show rs_image_EAC123C74DA14C4DA194C5F35E8A772D as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "（如果对大家见死不救……"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    show rs_image_30B3B1D90FB849C3B3D248154907D000 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    extend "我就再也不和九尾一起{color=#00FFFF}冒险{/color}了！！！）"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『……{w}……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_E62168EC90B7417CB5F5DD87BA487392 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "殊途同归。』"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_7009C1117C004F51829614A203C67DE7 "（欸？）"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 2.ogg"

    show rs_image_E1B79FB8843B4F1DA81DDFFFF2F5ED7F as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『可。此乃汝之选择，了解。雪绪，汝可退下。』"

    window hide

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Eye shine 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Eye shine 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BB04FBA8C4C5435A8473CC98753BFDB8 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    pause 0.4

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_341BF4851D844BF3BF882BEBE64621EE

    pause 1.4

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_71B99D519BF84409A5FC0F4A37BA0FED as tag_82C54ADE966440F7B34C83D13555B813 at center_top zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "！？"

    hide tag_82C54ADE966440F7B34C83D13555B813
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    show rs_image_C94C15F70ECD4CCBBA838E6B1352ED84 as tag_4233D225ED0D43968B3A0D890F587FEB at center_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "黄口小儿，何等嚣张。呵，勿需震惊……呼呼呼。"
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_82C54ADE966440F7B34C83D13555B813
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_82C54ADE966440F7B34C83D13555B813 = 300
    show rs_image_83DC2938B261446EA7DA8E7BEDD8F68F as tag_4233D225ED0D43968B3A0D890F587FEB at right_top zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_053F79D99A65415485F5458CD87E3325 as tag_82C54ADE966440F7B34C83D13555B813 at left_top zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "你、你这是怎么回事。突然就开口说话了，还这么高高在上……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_F49153AE549043A4A0CE9729749CB94B as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "！？{w}这股气息……难道是，"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    extend "{b}九尾！？{/b}"

    show rs_image_71B99D519BF84409A5FC0F4A37BA0FED as tag_82C54ADE966440F7B34C83D13555B813 zorder zorder_tag_82C54ADE966440F7B34C83D13555B813 onlayer master
    show rs_image_5BF57DBE5ED14CE2AFADF67B50D75DA7 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "可于吾前卖弄身姿，实乃汝之辞世好礼。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_82C54ADE966440F7B34C83D13555B813
    with rs_effect_D89D56EB440E4694B833F77134864B90

    extend "滚，"
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D89D56EB440E4694B833F77134864B90

    extend "雑鱼。"

    window hide

    pause 1

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Battle 6.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Battle 6.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Battle 6.ogg"

    # Gallery unlock: images/CG/The-inbelieveble-of-school/The-inbelieveble-of-school 5.png
    $ zorder_rs_image_E3E0C745F8D941F395EB7D2B8486A4E6 = -100
    show rs_image_E3E0C745F8D941F395EB7D2B8486A4E6 as rs_image_E3E0C745F8D941F395EB7D2B8486A4E6 zorder zorder_rs_image_E3E0C745F8D941F395EB7D2B8486A4E6 onlayer master
    hide rs_image_E3E0C745F8D941F395EB7D2B8486A4E6

    show rs_image_E3E0C745F8D941F395EB7D2B8486A4E6 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_44331B79D1D84C7EAA35F0480004721A

    pause 1

    window show

    rs_character_0B5C629539F940FA8A7FD26DD368F847 "唔啊啊啊啊！！！"

    window hide

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.8

    # Gallery unlock: images/CG/The-inbelieveble-of-school/The-inbelieveble-of-school 5-1.png
    $ zorder_rs_image_E1907497859B4E81BC4C4AEAC7E61C43 = -100
    show rs_image_E1907497859B4E81BC4C4AEAC7E61C43 as rs_image_E1907497859B4E81BC4C4AEAC7E61C43 zorder zorder_rs_image_E1907497859B4E81BC4C4AEAC7E61C43 onlayer master
    hide rs_image_E1907497859B4E81BC4C4AEAC7E61C43

    show rs_image_E1907497859B4E81BC4C4AEAC7E61C43 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.4

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "雪、雪绪……不错嘛。最近听说变得灵敏了是真的呢。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "久等了！！觉醒版阿雪！真是的～还想着什么时候该来了。"

    window hide

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 2.ogg"

    # Gallery unlock: images/CG/The-inbelieveble-of-school/The-inbelieveble-of-school 5-2.png
    $ zorder_rs_image_7469B14A83B44907A5986CD48A25A5EC = -100
    show rs_image_7469B14A83B44907A5986CD48A25A5EC as rs_image_7469B14A83B44907A5986CD48A25A5EC zorder zorder_rs_image_7469B14A83B44907A5986CD48A25A5EC onlayer master
    hide rs_image_7469B14A83B44907A5986CD48A25A5EC

    show rs_image_7469B14A83B44907A5986CD48A25A5EC as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.75

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "欸、欸……"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "好了，终于可以继续寻找封印方法了。"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "啊，前辈请先在那边休息一下。剩下的我们会做的！来，阿雪？"

    rs_character_7009C1117C004F51829614A203C67DE7 "欸～我也在努力退治妖怪。什么都没做的只有四朗一个人哦～"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "什、什么——！！？"

    window hide

    pause 0.5

    hide tag_5DC444A6262A4FCE9BF63B4338E21A74
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_1AB0074A0ABB40A7B797779771DF877D
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.8

    window show

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "『……』"

    window hide

    pause 1

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 4

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_6F41BEB29B0744ED8F25360004E87AB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D7A016DFACC54185AD0F3CB8B772E4CD

    if sys_music_current_file != "sound/BGM/The end of touch.ogg":
        play music "sound/BGM/The end of touch.ogg" loop
        $ sys_music_current_file = "sound/BGM/The end of touch.ogg"

    pause 1.3

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_BAB1EF8BB1E8402E9731FA917EC2849D as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_3DE6DC5E51F14E4F86F96E18DE4838E6 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_93E7311915BC403AAFABACFA29A7DDB1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_52BE5F9300564226BA402BC7C43E0B3A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.4

    window show

    show rs_image_A7D458B112A543F691F4223B8946B813 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "左边那部分是不是画得大一些会比较好呐。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_C0AC7060D45F43C8A44ABBEE4810EF9B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "木村——！！左边那块画大点！！"

    window hide

    pause 0.5

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_495084C2B20148F89AF8F281ECF662F2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 1.4

    show rs_image_8B5421D67E1C439BA9A47142DAC6188F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.8

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_2C4A74BADF6540698EF3E9A300893D1A = 200
    show rs_image_E8124A11D49145D0AE386AB993200B49 as tag_2C4A74BADF6540698EF3E9A300893D1A at left_top zorder zorder_tag_2C4A74BADF6540698EF3E9A300893D1A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "这种幻想风格的魔法阵真的有用？"

    $ zorder_tag_0999797A178545CBA5F244F41BBA50B1 = 200
    show rs_image_77E1742540E140CF92D387CBC6BD319A as tag_0999797A178545CBA5F244F41BBA50B1 at right_top zorder zorder_tag_0999797A178545CBA5F244F41BBA50B1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_710A38AC94C841779DB701B5AC1010FD "这种情况下也只能相信了。封印恶灵什么的，就像童话故事一样。"

    hide tag_2C4A74BADF6540698EF3E9A300893D1A
    hide tag_0999797A178545CBA5F244F41BBA50B1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_61A891D6A6D047DC93695DA12E13CC75 = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_724406A84D7141298EFF0D864FAE1534 = 300
    show rs_image_3DE36583042D4EF283177E16D538DDFC as tag_61A891D6A6D047DC93695DA12E13CC75 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4DBEB4DFB776458C84C13F7A2269B2D1 as tag_724406A84D7141298EFF0D864FAE1534 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "画完魔法阵后大家都站到圈内——！！\n谁还有事——？！除了技安大家都在～！？"

    show rs_image_F7E9A07B0B694A66B00B3ACEA65FE20D as tag_61A891D6A6D047DC93695DA12E13CC75 zorder zorder_tag_61A891D6A6D047DC93695DA12E13CC75 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "从头点一遍名怎么样？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_C968F326D97A4C939B195190FB16CD71 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，说得对呐！还有这一招！"

    show rs_image_8FFD17943DFD449881D8513C0F30D13E as tag_724406A84D7141298EFF0D864FAE1534 zorder zorder_tag_724406A84D7141298EFF0D864FAE1534 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "真是的，班长还是老样子……"

    window hide

    pause 0.5

    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    $ set_place_title(_("校庭"))
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D54164DAF02E4D8EA2D2F176E0318E76 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00003EA7

    return

label block_00003EA7:
    # Node: 00003EA7 (Playground)
    $ sys_lm_menu_item = [{"pos": (250, 280),"image": "images/Chapter 3/Menu/F5/Okajima-senior+Sato.png","hover": "images/Chapter 3/Menu/F5/Okajima-senior+Sato hover.png","name": "吹奏楽部"}, {"pos": (344, 296),"image": "images/Chapter 3/Menu/F5/Okajima+Kojima.png","hover": "images/Chapter 3/Menu/F5/Okajima+Kojima hover.png","name": "新聞部"}, {"pos": (472, 288),"image": "images/Chapter 3/Menu/F5/Nakayama-senior+Izumi.png","hover": "images/Chapter 3/Menu/F5/Nakayama-senior+Izumi hover.png","name": "バレー部"}, {"pos": (571, 296),"image": "images/Chapter 3/Menu/F5/Tsuki-Sora.png","hover": "images/Chapter 3/Menu/F5/Tsuki-Sora hover.png","name": "双子"}, {"pos": (105, 307),"image": "images/Chapter 3/Menu/F5/Shinobu+Nakayama+Kiyo.png","hover": "images/Chapter 3/Menu/F5/Shinobu+Nakayama+Kiyo hover.png","name": "しのぶ"}, {"pos": (672, 310),"image": "images/Chapter 3/Menu/F5/Itou+Kimura.png","hover": "images/Chapter 3/Menu/F5/Itou+Kimura hover.png","name": "伊藤木村"}, {"pos": (243, 352),"image": "images/Chapter 3/Menu/F5/Saburo+Shintaro.png","hover": "images/Chapter 3/Menu/F5/Saburo+Shintaro hover.png","name": "三朗慎太郎"}, {"pos": (416, 365),"image": "images/Chapter 3/Menu/F5/Tsubasa.png","hover": "images/Chapter 3/Menu/F5/Tsubasa hover.png","name": "つばさ"}, {"pos": (530, 362),"image": "images/Chapter 3/Menu/F5/Katou+Matsuta.png","hover": "images/Chapter 3/Menu/F5/Katou+Matsuta hover.png","name": "松田加藤"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_612
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"つばさ\"" }]):
        jump block_00003EAE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"三朗慎太郎\"" }]):
        jump block_00003EB0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"吹奏楽部\"" }]):
        jump block_00003EAD
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"新聞部\"" }]):
        jump block_00003EB2
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"バレー部\"" }]):
        jump block_00003EB1
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"伊藤木村\"" }]):
        jump block_00003EAC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"松田加藤\"" }]):
        jump block_00003EAF
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"しのぶ\"" }]):
        jump block_00003FDE
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"双子\"" }]):
        jump block_00003FDD
    jump block_00003EA9

    return

label block_00003EA9:
    # Node: 00003EA9 (Confirm)

    if judge_lm_condition([]):
        jump block_00003EAA

    return

label block_00003EAA:
    # Node: 00003EAA (選擇)
    call scb_selector(_("已经确认完毕了？"), [{"name":"はい", "content":_("可以了")}, {"name":"いいえ", "content":_("再等一会")}]) from _call_scb_selector_69

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"はい\"" }]):
        jump block_00003EAB
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"いいえ\"" }]):
        jump block_00003EA7

    return

label block_00003EAB:
    # Node: 00003EAB (學園怪談 3)
    $ set_window("イベントモード")
    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_8B5421D67E1C439BA9A47142DAC6188F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_BD3488C0DB4E4D3A90DE1A07FF4B6C4D as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "技安！！这边准备好了！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_BAB1EF8BB1E8402E9731FA917EC2849D as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_3DE6DC5E51F14E4F86F96E18DE4838E6 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_486F70F1E27D43BC868FA3ADA0B574BE as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_52BE5F9300564226BA402BC7C43E0B3A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "明白了！"
    show rs_image_D4AF6091BD0341CFBF561C2744F3FD83 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "走吧，四朗，雪绪。"

    window hide

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    pause 0.2

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_BAB1EF8BB1E8402E9731FA917EC2849D as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_76A6FDF06765424DBC1E2AE1C0D1ADA1 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_D4AF6091BD0341CFBF561C2744F3FD83 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_148B282ED1E44EDCB7EE910F714866A9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "终于能回到原来的世界了啊～……太好了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_311C0DF0CF504684BAB1C36398430D4D as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "前辈！回去后请和我们打篮球哦！"

    show rs_image_AA7BE8B3E89D43F6AC40550A8222044B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哦！雪绪也来。{w=0.2}{nw}"
    show rs_image_F03237FB10EB44FDB0C2E3F6C4B4F5D2 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    window hide

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.2

    $ zorder_tag_4233D225ED0D43968B3A0D890F587FEB = 300
    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_BAB1EF8BB1E8402E9731FA917EC2849D as tag_4233D225ED0D43968B3A0D890F587FEB at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    show rs_image_7C2E9E7F5F0D47D1BF49B03E25F8C320 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    show rs_image_D4AF6091BD0341CFBF561C2744F3FD83 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_B056783A418145BFAACBDB79DAF4C3BE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_3B4C660F421B4BE392BB540B580F0339 "阿雪最近运动神经突然好了，打篮球也很厉害，吓到我了呐～！"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "欸～这样啊！今天也很厉害呐。是在远足部学到什么了吗？"

    show rs_image_2A8CFCB3518F4B1B8CF01BE489B15614 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "哈哈。也许是那样的。说不定能打败前辈哦。"

    show rs_image_AA7BE8B3E89D43F6AC40550A8222044B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈，真敢说。不要小看每天都在社团锻炼的中学生啊～！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D14C1328F4484EBE997C5CE2D0C119BD as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "前辈怎么可能输给阿雪——！！别指着鼻子上天狐狸！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_B276F958003A43A59D0E1DAFE5CCAA4E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_E7C9E0A49A974D4A82B0A5F8DEFB0F38 as tag_4233D225ED0D43968B3A0D890F587FEB zorder zorder_tag_4233D225ED0D43968B3A0D890F587FEB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    rs_character_7009C1117C004F51829614A203C67DE7 "四朗，给我记住。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_890FBC4A7D5344C091041A7DCE93EA3E as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "噫！？"

    window hide

    pause 0.3

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 1.4

    if sys_music2_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wind 1.ogg"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 2.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_E6F828E052D84D4B9313602BBCD368CC as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 1.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_495084C2B20148F89AF8F281ECF662F2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.6

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "大家，都集中起来了吗～？{w}要开始了哦！一、二！"

    pause 0.3

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    extend "{size=20}{color=#FFFF00}Revertere ad locum tuum! Ianuae Magicae!!!{/color}{/size}"

    window hide

    pause 0.4

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Battle 4.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Battle 4.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Battle 4.ogg"

    show rs_image_E52474D2D3FC418AAD7B6C04AF6F88C1 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_44331B79D1D84C7EAA35F0480004721A

    pause 1

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……嗯！！？阿、阿雪……你身上冒出黄色的烟了……"

    rs_character_7009C1117C004F51829614A203C67DE7 "欸！？{w}九、九尾！？？呐，九尾！九尾！！"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "阿雪怎么了？“九尾”是什么？"

    rs_character_7009C1117C004F51829614A203C67DE7 "骗人的……九尾竟然也会被……"
    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Bell 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Bell 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Bell 1.ogg"

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    extend "九尾！九尾——！！！"

    window hide

    pause 1

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_8201690CF6F7483EBE67068B89A27AD0

    pause 1

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_8B5421D67E1C439BA9A47142DAC6188F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_12C4530B167A41AE9A198E0A1C7198EA

    pause 1

    # Gallery unlock: images/CG/The-inbelieveble-of-school/The-inbelieveble-of-school 6.png
    $ zorder_rs_image_45E6DC2D2D414F33A0305654A6FC0BE9 = -100
    show rs_image_45E6DC2D2D414F33A0305654A6FC0BE9 as rs_image_45E6DC2D2D414F33A0305654A6FC0BE9 zorder zorder_rs_image_45E6DC2D2D414F33A0305654A6FC0BE9 onlayer master
    hide rs_image_45E6DC2D2D414F33A0305654A6FC0BE9

    show rs_image_45E6DC2D2D414F33A0305654A6FC0BE9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 0.8

    window show

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "……"

    rs_character_C223850065F6443080205D1F61C04C98 "分别前没能告诉他？比起“封印”这种掩饰用的词汇，\n直接告诉他这就是{color=#FFFF00}驱灵仪式{/color}会更好吧。"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "虽无执着，仍乃小童。告之遂不免多事。"

    rs_character_C223850065F6443080205D1F61C04C98 "是嘛。那我也需要回到原来的地方了。好久没能进入校舍，真的很开心呐。"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "缚于地者常遇难事。若论封于无人来访之山谷，吾亦相同。"

    rs_character_C223850065F6443080205D1F61C04C98 "我至少还能亲眼看到大家的日常，山里就太无趣了呐。"

    rs_character_6C344A6C39F6479282A6BD884E3F8F11 "非人者亦有。然与汝相伴仅在须臾，实乃羡慕。"

    rs_character_C223850065F6443080205D1F61C04C98 "不要那么想嘛。{w}\n肯定很快就会重新迎来这样的时光的。保持这种想法也不坏哦？"

    window hide

    pause 1

    show rs_image_6F41BEB29B0744ED8F25360004E87AB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 2.5

    hide tag_4233D225ED0D43968B3A0D890F587FEB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    stop music fadeout 2.5
    $ sys_music_current_file = ""

    pause 4


    if judge_lm_condition([]):
        jump block_00003EBE

    return

label block_00003EBE:
    # Node: 00003EBE (梅咲 square)
    $ set_window("(標準)")
    if sys_music_current_file != "sound/Effect Sound/Train 2.ogg":
        play music "sound/Effect Sound/Train 2.ogg" noloop
        $ sys_music_current_file = "sound/Effect Sound/Train 2.ogg"

    pause 1.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ set_place_title(_("梅咲广场"))
    pause 0.5

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_678F3087B5E446BD927B68119C790EE5 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_202D019D0CEB444FB06F28FE932B89CB as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003EBF

    return

label block_00003EBF:
    # Node: 00003EBF (梅咲 square)
    $ sys_lm_menu_item = [{"pos": (368, 256),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "バス"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_613
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"バス\"" }]):
        jump block_00003EB9

    return

label block_00003EB9:
    # Node: 00003EB9 (Bus)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Bus 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Bus 2.ogg"

    $ set_place_title("")
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Bus 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Bus 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_3479A228A574419BB05D0C16C7A56E23 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 2.5

    show rs_image_22B28283E0ED4E5E951B048169A5F12E as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    pause 2

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    stop music fadeout 2
    $ sys_music_current_file = ""

    stop effect fadeout 2
    $ sys_effect_current_file = ""

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003EBC

    return

label block_00003EBC:
    # Node: 00003EBC (Mountain 1)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ set_place_title(_("道路"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wave 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_678F3087B5E446BD927B68119C790EE5 as tag_ECFB5B509A334A868686B3435242BF90 at center_bottom zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_87068767729842AF903679E9A80C638C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003EB6

    return

label block_00003EB6:
    # Node: 00003EB6 (Mountain 1)
    $ sys_lm_menu_item = [{"pos": (552, 304),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_614
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00003EBD

    return

label block_00003EBD:
    # Node: 00003EBD (Mountain 2)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ set_place_title(_("道路"))
    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    if sys_music_current_file != "sound/Effect Sound/Wind 1.ogg":
        play music "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_music_current_file = "sound/Effect Sound/Wind 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.8

    show rs_image_678F3087B5E446BD927B68119C790EE5 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3BFB9DEF4B0B4342AB76E8147EDAA875 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3


    if judge_lm_condition([]):
        jump block_00003EB7

    return

label block_00003EB7:
    # Node: 00003EB7 (Mountain 2)
    $ sys_lm_menu_item = [{"pos": (104, 272),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_615
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00003EBC
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00003EB8

    return

label block_00003EB8:
    # Node: 00003EB8 (學園怪談 4)
    $ set_window("イベントモード")
    stop music fadeout 2
    $ sys_music_current_file = ""

    $ set_place_title("")
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_8EC5717E792241CB9E9610819A6E1D46

    pause 2

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "真是的，突然就消失不见，吓死我了。"

    window hide

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_007FC3B89CCB4F35BDB06265267D8401 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 1.5

    show center_title_white (_("我来接你了哦\n九尾")) as center_title_white zorder 1000
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 4

    hide center_title_white
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg"

    pause 0.8

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_DCEBC7527B8F4B4EA0FF44E692174034

    call scb_flag_title_end(3, _("「学园怪谈」")) from _call_scb_flag_title_end_13

    if judge_lm_condition([]):
        jump block_00003EB3

    return

label block_00003EB3:
    # Node: 00003EB3 (Phase: 0)
    $ C3S5Phase = 0
    if Chapter <> 3:
        $ del C3S5Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_00003FE0
    if judge_lm_condition([]):
        jump block_00003EB5

    return

label block_00003FE0:
    # Node: 00003FE0 ()

    return

label block_00003EB5:
    # Node: 00003EB5 (FINISH)
    $ C3S5 = True

    if judge_lm_condition([]):
        jump block_00003FDF

    return

label block_00003FDF:
    # Node: 00003FDF (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_16

    if judge_lm_condition([]):
        jump block_00003FE0

    return

label block_00003EAE:
    # Node: 00003EAE (翼)
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_58B570C730E34F7D910E94E19D4A143A as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_E5980AB1AA3E484A93A2EBD2139A77FE as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "做到了呐，友君！是我们的胜利哦。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "YEAH——！翼君好像帮了救援组大忙吧！在那群人里也是很厉害了呐！！"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_93C0B7E63B614E9386D2D63EAAD23E8F as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不，我只是投了一张纸过去……\n"
    show rs_image_F1C99A939B8C442CB1E7D64CE94323DC as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "这都是多亏了友君哦！"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸？我在回收组……"

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5949B5B78A4A498996EECB708FE12ECF as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不，友君{w=0.3}{size=14}{color=#808080}（照片）{/color}{/size}一直都在我身边哦。"

    show rs_image_3D1658550AAD4B23B72B22E477CAE581 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "？？"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))

    if judge_lm_condition([]):
        jump block_00003EA7

    return

label block_00003EB0:
    # Node: 00003EB0 (慎太郎+三朗)
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_5B9AE6B31C384E64B73544A0EE33EDF7 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_4BDA99B276AF4FA1ABCDFD02FF3B31F5 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈～还以为会咋样，\n什么都没发生真是太好了。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_A4DA559591184F10AEF1EEE2F25374D4 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "是啊～逐渐意识到放纵性欲也是大罪了。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_AB9B8E3D29CB454EA7EC6ED6E91C1CE1 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "就是！下次要是我再发现你在干那种事，\n就要好好调教了！"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_BCF76F402DDE4A5C8E1B927886F977C2 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "没关系！我可是很专一的。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_82231ADF123047EF98DEC3113C52C10A as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊……不过，有点想被三酱调教呐～！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_0F2FF68508D6483F9A130D2B025269C2 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呐——呐——！除了花心还有什么能被调教？？"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_E9F999F5EAC440AD9842EDCF163482BE as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "说什么话……\n"
    show rs_image_DDB8C95C32944AE58D2742027CC2A3D6 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "直说的话差不多的范围内都可以忍的。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_1B7780F87FED40AF88DC6B5A69C34B8B as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不是说那个～！唔～……"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))

    if judge_lm_condition([]):
        jump block_00003EA7

    return

label block_00003EAD:
    # Node: 00003EAD (佐藤+岡島前輩)
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_2E24765C23544B69A9391DC51FE38194 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_EBC00E6C111C45A6830591C1B1D82AC6 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "这样就解决了呐，前辈♪ \n没能逃过考试请不要在意！"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_8E0E40AFC8B7460ABD959470C7074805 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_193BCCFE681D42C8993A47A884FF2200 "呵，\n我本来就是重点升学班，根本没有逃的打算。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_2E1F43EA232A44689196EAB6C6746E38 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "是这样吗！"
    show rs_image_EBC00E6C111C45A6830591C1B1D82AC6 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……哈哈。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_1FBDFA89EBEF425E9105994CA2ED47F1 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_193BCCFE681D42C8993A47A884FF2200 "有意见？"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_E9DA1A925CE140459A40C853C70AA406 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EA9AA88E88D84B559B925363E2931756 "并没有哦。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))

    if judge_lm_condition([]):
        jump block_00003EA7

    return

label block_00003EB2:
    # Node: 00003EB2 (岡島+小島)
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_6EACDBA5EB7B44D7A7699633252E6B7E as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_BB675405870B497F958414550471B4BF as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "这次的事件我们新闻部会有详细报导的。\n敬请期待明天的报纸！"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_9F29F130587546EBA5C8BD952A84E3CF as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "毕竟也是出现了真正的幽灵呐。\n本来还以为能拍到更加有冲击力的照片的，\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_1654C244584349A6B0811665076020BD as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    extend "真扫兴。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))

    if judge_lm_condition([]):
        jump block_00003EA7

    return

label block_00003EB1:
    # Node: 00003EB1 (泉+中山前輩)
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_4CAFD25A1F5E4405A36AFD06AA87C091 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_D668AB5BCE7641D598E5B719952F1E93 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "拜森海君和大家所赐得救了，真的非常感谢！"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_1833E5B4BC8B4238A9B2FD7651F6CFBC as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A751683772E84A83B9CDA0EADC2D57CE "我们三年级本该好好处理的，\n没能派上用场对不起了。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_9AF02379E9534E1FB204413A9C8F2675 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "真的呐，\n前辈“没有考试不是也挺好的嘛”这样说着，\n根本派不上用场。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_2A15D6142AA44DF38FF1D4D9F93E6F99 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A751683772E84A83B9CDA0EADC2D57CE "啊哈，哈哈哈……"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))

    if judge_lm_condition([]):
        jump block_00003EA7

    return

label block_00003EAC:
    # Node: 00003EAC (木村+伊藤)
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_770FBE957C624A43B0FADE9DB660E0E2 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_48D8C5CECCB84B739099EE1FBE060B20 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "伊藤君居然会说\n“不许对我的木村出手”这样的话，\n很帅气呐☆"

    show rs_image_E12C9158C45243C89FC121E481091022 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呵呵！\n我什么时候成伊藤的东西了？？\n几点几分几秒地球转第几圈的时候？"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_EB52490B1A0A4E33BC3D00AD5EFD78E1 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "幼稚！！就因为你被妖怪抓走了一时情急而已！"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_48D8C5CECCB84B739099EE1FBE060B20 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊～好勇敢呐。\n感觉伊藤酱不在我身边就活不下去了呐～！"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_6AC542E194714D3B9139FB8ED959EF70 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "我不在你肯定不行！{w}一开始你被{nw}"
    show rs_image_54727816761343868F8C820927DCC7C6 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "妖怪抓走的时候，\n气血上脑一下子就看不见周围的情况了……"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_692C028CA3784566A15437BC68BB11B1 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "算了算了不要那么紧张嘛！\n反正我会永远和你在一起，\n安心下来不就能看清周围了嘛？"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_84ECEC41D074460088D334B076B5152D as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "欸……"
    show rs_image_D8C14DC952DD4951B9533E31594D0F9F as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，嗯，交给我。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))

    if judge_lm_condition([]):
        jump block_00003EA7

    return

label block_00003EAF:
    # Node: 00003EAF (松田+加藤)
    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_CF9552A127F84B139910618B1FE71819 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_36E75A5BA4504559920E625E0462334C as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "要是那些妖怪说的是真的，\n维持现状不是也很好吗？\n不是说要给我们制造乐园吗？"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_F74587AF3C5D4336B5497ADD0EDFD9BA as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "你啊——不是对我们好就是好。"

    show rs_image_36FA043A9D13453B8E531655A8BDDE10 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "那会是一个大人一直在睡，没有任何猫狗动物的世界。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_1DB6078B9236425482D8C50AB190159F as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "嗯……说的也是。成不了大人就太无聊了，\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_720C0D06E4A146109B2FB898D5464241 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "大人不在也很无聊呐。"

    show rs_image_CF9552A127F84B139910618B1FE71819 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "说起来你喜欢动物？第一次听说。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_3D04A5D178044F04B357189727365274 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "欸，不……\n我只是觉得肯定会有见不到动物会很寂寞的人。"

    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 = 300
    show rs_image_CF9552A127F84B139910618B1FE71819 as tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 at center_bottom zorder zorder_tag_2D6D26BC65EB40CCB22A2D540F9DE0E3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_81D16F74A3C44B8982DB528D7D934850 "嗯——"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))

    if judge_lm_condition([]):
        jump block_00003EA7

    return

label block_00003FDE:
    # Node: 00003FDE (忍+中山+清)
    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    show rs_image_2E8641A2B5174EDB9F6B23CA9431F488 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at center_bottom zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_11105D5FDDBE4455A6758D4C0CA54D7F as tag_988AD5B87A6D42E59078E032C7FA7EB1 zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D34F60C882F0425E93252349E8C3BC8D "绫濑前辈！\n没能拜见前辈面对妖怪英勇战斗的身姿真是遗憾！！"

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    show rs_image_1AD02FE68F6D4BDAB1AFC4AE07A4FB53 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at center_bottom zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "也不是那么夸张的事。\n也有拿不出手的地方……没看到正好。"

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    show rs_image_22CBAD93D7934D48A52EE3B4A81002B8 as tag_988AD5B87A6D42E59078E032C7FA7EB1 at center_bottom zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_08DBDA5028CF47989118DFA6DF0E1507 "欸～？？反倒更在意了～！！\n这件事以后还请详细说说哦！"

    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 = 300
    show rs_image_0CAC11E265C142FCB91DA75E12E5C69E as tag_988AD5B87A6D42E59078E032C7FA7EB1 at center_bottom zorder zorder_tag_988AD5B87A6D42E59078E032C7FA7EB1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……下次再说。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    hide tag_988AD5B87A6D42E59078E032C7FA7EB1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))

    if judge_lm_condition([]):
        jump block_00003EA7

    return

label block_00003FDD:
    # Node: 00003FDD (月+空)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_39FACE09B65F4041BD879856B3BBC96C as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    show rs_image_7C65D1B95CC44571A3E775F933CCD3C2 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "空，真亏你能毫不退缩地和妖怪勇敢地战斗，\n了不起。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_0128BB8EAA3541469E1CD433C1215308 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "因为哥哥在所以才能这么安心哦。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_E17ECF4F68EC48AC8426F360F5F88888 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯。不过，\n每晚的练习究竟能不能锻炼精神力呢……\n"

    show rs_image_EC91B7B847884CDABC396D355234FECA as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "今后也要继续锻炼下去！"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 300
    show rs_image_9069EF4B68784EE3AB5F780E3D49186E as tag_81DF0CF91B224EAAA16B0366711BA01F at center_bottom zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_61A891D6A6D047DC93695DA12E13CC75
    hide tag_0999797A178545CBA5F244F41BBA50B1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_2F2406ABFD334A9FAFFFD526F608E209
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_346FE7CD97BB4FB18CB50E78275F4E23
    hide tag_CC4336DE74164173AC47C2C317367F10
    hide tag_DCBDF256A1E242E78A25910AE27C0954
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    show rs_image_7131112E86B24D6A9BE667868088D590 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("校庭"))

    if judge_lm_condition([]):
        jump block_00003EA7

    return

