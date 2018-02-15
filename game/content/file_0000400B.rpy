# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 0000400B (FLAG: 正義的教訓)

label block_0000400C:
    # Node: 0000400C ()

    if judge_lm_condition([]):
        jump block_0000400E

    return

label block_0000400E:
    # Node: 0000400E (Phase: 99)
    if Not(VarExists("C3S2Phase")):
        $ C3S2Phase = 0
    $ C3S2Phase = 99

    if judge_lm_condition([]):
        jump block_0000400D

    return

label block_0000400D:
    # Node: 0000400D (F2 START)
    call scb_flag_title(3, _("「正义的教训」")) from _call_scb_flag_title_13

    if judge_lm_condition([]):
        jump block_0000400F

    return

label block_0000400F:
    # Node: 0000400F (正義的教訓 1)
    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F3D233F763D6421EBDC0A1616D4F0D6F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    if sys_music2_current_file != "sound/Effect Sound/Tick tock 1.ogg":
        play music2 "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    pause 0.8

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_3CCC6DE5C5ED405DB1BBB15ECA3CDD44 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯……"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_54984C82CD7C4D86A32BA7AFE5015CD1 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那个……"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_4BA562125E914D049B3A68EC3F0DB8A1 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼姆～"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_02AF4E98AE404A37BBF5189D1BD66AE6 as tag_81DF0CF91B224EAAA16B0366711BA01F at center_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "唔……"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_CB70B28808D840B5A51436CA4E858F49 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "唔～……"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_78AAFDF80423489CB9D3E414C6D0A594 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊～……"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_4E2835E547304DD1A4EE59EDDEA933C3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……{w=0.55}{nw}"
    stop music2 fadeout 0.8
    $ sys_music2_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_DEC2F822DD03433CB37D42439376833B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_7F843C6F478A4CA391089291EB2F56A3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    extend "你，说到底为什么要我们做？"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 400
    show rs_image_776A3EC98A3846ECA9A049472752C15A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可是……滑子老师他。"

    window hide

    pause 0.8

    show rs_image_23E95FF3D12540FB88BD74983BE7800E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_856822D0F30B4AF0AE8688F27D9CE9B2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    pause 0.6

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_B08F170752C74A09BC000D1CF77FA609 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "之前在公民馆的那次小钢琴部的演奏评价非常好。"

    show rs_image_87A4A951CCF94134BEC8CCB7D574B6E1 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "所以，这次在公民馆的聚会的演出，可以也去试试吗？"

    show rs_image_9BAD09B7F4DE47339C69A165D80E6844 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D9F0C257FF534E79ADF7FDFE3653E326 "不过，这次的规模比上次大得多，你们也要加一些人手，尽量热闹些。"

    window hide

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    show rs_image_7F843C6F478A4CA391089291EB2F56A3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_F3D233F763D6421EBDC0A1616D4F0D6F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    pause 0.5

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "根本等于什么都没说啊，为什么给你的麻烦事非得我们来做？"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "可是，被说了只要和当初顺利做完御咲祭时\n担任实行委员同样的阵容就可以了嘛～！"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_17BD4756EE4547C7999FB0FE558D991B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "所以就没确认我们的想法直接接受了，真是自作主张。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_C0AC7060D45F43C8A44ABBEE4810EF9B as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "就是就是，把我们卷进来也很麻烦的。"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_8D9EAB710DF84DAAA58AA16DC9ADFC74 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "可是，小翼酱的事情也麻烦过老师……"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_B276F958003A43A59D0E1DAFE5CCAA4E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "唔……确实……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_02AF4E98AE404A37BBF5189D1BD66AE6 as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "但是，根本想不出好的方案。"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_E21ACD1443A4402AA37E7CE200FF6D4C as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "大家一起跳个脱衣舞不就行了？"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_30CFC5FBE4104C718C904D0C834E6E9A as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不要，客人会直接晕过去的。"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……既然在这里不管怎么样都想不出来，去外面散散步如何？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_FF4A588462534B15B9D5F444704F26BB as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "等下——！那只是忍待不下去了想找个地方去玩对不对？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "真是的，认真做啦——！呵——呵——什么都不会的忍——呵！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_1D259A10CEC9474D9310090F507D010A as tag_81DF0CF91B224EAAA16B0366711BA01F at left_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "确实有理，适当活动一下身体能促进血液循环，思维也会顺畅。"

    show rs_image_BDC291B5081C42168C8A1886FB5FACD3 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "绫濑是想说那样做或许能想出有用的方案来吧。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_27FF4633286B4DF59BF4C1A761DDF98E as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，是这样，只是交流问题啊，什么都不会的忍——"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 at left_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BEF582EB5C1541099B31FB6D3CD3509F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好痛。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_93E7311915BC403AAFABACFA29A7DDB1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_F0AF18EA5ED94E6B9426EA7B01961357 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那就边走边想好了♪偶尔这样做做也没什么不好嘛。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "是呐，好像很有趣的样子。\n"
    show rs_image_E3D2D87C0D4C4A54B7016B01E2AC7D10 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "作哉君也请整理一下心情不要生气了哦？"

    show rs_image_7F843C6F478A4CA391089291EB2F56A3 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊、嗯。"
    show rs_image_00C537252F144BC5A27190CF382A7D50 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "{size=16}……其实也并没怎么生气。{/size}"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_A39671BE6D8246F5ACCB45CA04C8C3D1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_0AE8CF84C8F94EF9BEE8D1640F087EC3 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_34E241C96D16409BBECDFE411E12F665 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "欸——其实你们俩想独处？？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "原——来如此原——来如此！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_C507E18213D34AE4A482BBE2CE5D35AD as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "你们两个去耳鼻喉科挂个号怎么样？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_B2054D14604A408CAF74D842FA9CF92A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_C989D2B8472147EBAAC08D14FF060BEC as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=430, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "能流利交流了呐，一之濑君。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_2B8CA379875246C784AD29CB254874FC as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯，也和我说说话，一之濑。"

    show rs_image_3C4C246AAFC1459DBB1711584019784D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "好、好的！哈哈……"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_A579F650612D4CA18E2B222221DBF547 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊～我也要我也要～！翼君本来就是我的～！！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_8C106322A86B43E599BD9F3A2962F305 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸！！我、我的是指……"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "一之濑君，过来，我这里是最安全的。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_5B75C21196E6494E82DFA6A82B22212D as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_602B12F1C445477F861182BD846DB0BD as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦～一之濑挺受欢迎嘛～这下前途不明了某人也很麻烦了呐～"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "一边去。"

    window hide

    pause 0.9

    stop music fadeout 2
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_5AF726F3D86C4FD7BCCD53EEA33689F0

    pause 2.5

    $ set_window("イベントモード")
    if sys_effect_current_file != "sound/Effect Sound/Swallow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Swallow 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    if sys_music2_current_file != "sound/Effect Sound/Clamorous 1.ogg":
        play music2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    pause 2

    stop effect fadeout 2
    $ sys_effect_current_file = ""

    show rs_image_D5FE65484D524DF0ACA6C31DC2F622E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_9A04F9951A5942729EEA1C44C5227BDB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.4

    if sys_music_current_file != "sound/BGM/Chapter 1.ogg":
        play music "sound/BGM/Chapter 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Chapter 1.ogg"

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那～么，都已经到商店街了，想到好方案的人请举手！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.2

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=36}……{/size}"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_C9A169B5FECE487BAE71B3017B79B0B4 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没有！？为什么！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_31DC2C2F7D164AA2B6F4DCFBBBFB98BB as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_62A567EC8E0B4E0F9C806140172361E5 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀～今天天气真好呐。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "真的好啊～这种日子能一起散步还不错吧？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_D4AF6091BD0341CFBF561C2744F3FD83 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_1CDBF9A281F54418A7363E36408C7DD5 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "空，那应该是你喜欢的店。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哇，真的！呐呐作哉君，下次也……"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_F0AF18EA5ED94E6B9426EA7B01961357 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_2098D50DC921476DADED454076F2DA7D as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "月君不论实际还是看上去都很帅气呐。路过的行人也都在看。"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "笨、笨蛋，别戏弄我……"

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_60082BB1D9BF487E8D6719ABAD43D64E as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "大家～好好干啦～虽然我也没想法～"

    show rs_image_F56E1443445D4250ADC9107746BB4E98 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呜～要是有什么突发事件就好了。引起恐慌的话肯定能想到什么的。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_F746E3C6B8844B0BA4CB845795AF8A1F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_56FBF946ACED4A5BB4E2382EC4EB180C as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "都说道这个程度了忍同学就做点什么嘛。"

    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……嗯？"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_3F5AF2DAC6F94773B04A709D2558F647 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.8

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    stop music2 fadeout 2
    $ sys_music2_current_file = ""

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_5287952871AA4DBE8AEEF83638377748 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_022781101FD04002AB8C506EED9156F2 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那就试着仰望星空如何～？今天的天气好像也没好到能看到什么呐～"

    stop music fadeout 1
    $ sys_music_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_CA32B3074CBF4DB08BA59AE12141A4F7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……！！看那个！"

    window hide

    pause 0.5

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_64BB3E5A165344B0851F77909A33471E as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_8C5B9D09E3154FABA2E732547E9321D0

    pause 0.6

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "啊？那是……{w}{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_A366FE92B81D404585614E7D29CFAD20 = 400
    show rs_image_78BC0881956C42EB89271A1A1108A59A as tag_A366FE92B81D404585614E7D29CFAD20 at center_bottom zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    extend "……诶？"

    if sys_music_current_file != "sound/BGM/Stage of HERO.ogg":
        play music "sound/BGM/Stage of HERO.ogg" loop
        $ sys_music_current_file = "sound/BGM/Stage of HERO.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那、那是什么！？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_B6CBAF4A67C24194A4344656E0351CB2 as tag_A366FE92B81D404585614E7D29CFAD20 zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "请、请好好看看天空！！"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_0A971CC1A0ED4474ADB47E07493BDF7A as tag_A366FE92B81D404585614E7D29CFAD20 zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "鸟！？"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "飞机！！？"

    if sys_effect2_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Drum 1.ogg"

    # Gallery unlock: images/CG/Precept-of-justice/Precept-of-justice 1-5.png
    $ zorder_rs_image_08883BD8FCE34314B854783E9E919F7A = -100
    show rs_image_08883BD8FCE34314B854783E9E919F7A as rs_image_08883BD8FCE34314B854783E9E919F7A zorder zorder_rs_image_08883BD8FCE34314B854783E9E919F7A onlayer master
    hide rs_image_08883BD8FCE34314B854783E9E919F7A

    show rs_image_08883BD8FCE34314B854783E9E919F7A as tag_A366FE92B81D404585614E7D29CFAD20 zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不，那是……！！"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    # Gallery unlock: images/CG/Precept-of-justice/Precept-of-justice 1-1.png
    $ zorder_rs_image_E34446EB077F4A6EA9497B9B9B0733FE = -100
    show rs_image_E34446EB077F4A6EA9497B9B9B0733FE as rs_image_E34446EB077F4A6EA9497B9B9B0733FE zorder zorder_rs_image_E34446EB077F4A6EA9497B9B9B0733FE onlayer master
    hide rs_image_E34446EB077F4A6EA9497B9B9B0733FE

    show rs_image_E34446EB077F4A6EA9497B9B9B0733FE as tag_A366FE92B81D404585614E7D29CFAD20 zorder zorder_tag_A366FE92B81D404585614E7D29CFAD20 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=36}{color=#0000FF}超人！！！{/color}{/size}"

    window hide

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 1

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_A366FE92B81D404585614E7D29CFAD20
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.6

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_0600CCA9D8E5458687C3A5F9EE6CB6C5 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那根本不是飞，只是从一栋楼跳到别的……"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_B4378AE67E6A4B08A37DF8E3C2E65B17 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那也很奇怪了！三酱不要这么冷静地分析！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_D8F88F968B9E4B3CBEED302C0FA2B323 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_16CAEBBCC6FD449194FCB8B9AE6A986E as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "追上去！查明真相！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "了、了解！！可、可是到底去什么地方了！？"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "分组搜索好了。那样会比较好找，行动起来也方便。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "明白了。那等下再见！"

    window hide

    pause 0.6

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A4E74E94E7C549809795CEBC732E6326 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    pause 0.5

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_C18E9E3152D24005B446B9C4987139A3 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_F9B0C2D0E2D84D6D85BC37C697E5F928 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "到底去什么地方了！？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不、不清楚……完全找不到了。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "说起来，这个人员组合真少见呐。"

    show rs_image_F886D313ADF24EF0827EE545DCDFF7F0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "没有说明的余裕乘势就变成这个样子了。其他组想必也是这样的。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_7C30D306B01C4984A6C86B48D0A0FD27 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这种突发事件肯定能成为好点子的，一定要找出来。"

    show rs_image_D7BB1A8267AE4353950D17F94CE6C389 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "是这么说，不过其实是因为好奇心吧～？小忍果然也是男孩子呐。"

    window hide

    pause 0.8

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_306C7487DB45469D8D387C96B770D327

    pause 1.5


    if judge_lm_condition([]):
        jump block_00004010

    return

label block_00004010:
    # Node: 00004010 (CP3 Daytime Misaki 忍翼慎太郎)
    call block_00001CFB from _call_block_00001CFB

    if judge_lm_condition([]):
        jump block_000041C8

    return

label block_000041C8:
    # Node: 000041C8 (正義的教訓 2)
    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("迷之地点"))
    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_CD2EEFA824144E4EA57A4C040DABF455 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7D781D05099A4C93AF6B1D005359F3E9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    pause 0.3

    show rs_image_37DD260DB3B64875AFF0FBF4F01BD3E9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊！发现足迹了。这是……确实有呐。"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_CD2EEFA824144E4EA57A4C040DABF455 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A7B77D634FDA4F01AB6ED891600EEDD6 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "为什么能肯定这就是超人先生的！？"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_F4E4588DC479409680603E0DBD6B5E84 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "继续深究会很危险的，还是快点回去好～"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_15B6E6A6404F4C88A018646854D18096 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "中二病模式的小忍可是谁都无法阻止的。"

    show rs_image_A4DA559591184F10AEF1EEE2F25374D4 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "话是这么说，不能让小忍一个人去，但把翼亲留下也很危险。"

    show rs_image_71C15FD598FF4136BA22D65F7B888767 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "这里也只能我们跟着去了？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_0DF7CB7945524EF69DA7FA90D0FEB010 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_bottom zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜呜……说的也对。一发生什么的话绫濑君也一定能做什么的。"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_37DD260DB3B64875AFF0FBF4F01BD3E9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，放心，绝对会保护你们的，然后，绝对会干掉敌人的。"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    show rs_image_CD2EEFA824144E4EA57A4C040DABF455 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_F4E4588DC479409680603E0DBD6B5E84 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "出、出现了，这个节奏……到底要和什么战斗啊，真是的。"

    hide tag_724406A84D7141298EFF0D864FAE1534
    hide tag_2D6D26BC65EB40CCB22A2D540F9DE0E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    $ set_place_title(_("迷之地点"))
    pause 1

    stop effect2 fadeout 2
    $ sys_effect2_current_file = ""

    $ set_place_title("")
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_038A3EB7489F4B51B2A1AD7FBC2E0808

    pause 2

    $ set_window("イベントモード")
    if sys_music_current_file != "sound/BGM/Something comical 1.ogg":
        play music "sound/BGM/Something comical 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something comical 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C84270558B44454A2A6E8B66021E559 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_04EAB054667D4258ACFBBEA80EB6992F

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_C533295FFF704695B54B98B9893D98B9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_E21ACD1443A4402AA37E7CE200FF6D4C as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.2

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "说起来这里还有这么一片森林呐。\n"
    show rs_image_A3D6CADEDC674400B7CD24D81BE7CC16 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……总觉得有些气氛不对。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_6536F8ADBA294923ABCC248AEAB17528 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那、那那那是什么意思！？"

    show rs_image_D7BB1A8267AE4353950D17F94CE6C389 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不……怎么说呢～\n"
    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    extend "直白地讲，要出来了。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_E3D2D87C0D4C4A54B7016B01E2AC7D10 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，厕所的话可以先在那边的草丛里……"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    show rs_image_3D554AE725A4498287A90C6C9BCBB679 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不对——！！\n"
    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_6536F8ADBA294923ABCC248AEAB17528 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_4BBDCD83023642F6923D76BE102A1BB9 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    extend "说不定刚才的足迹其实是幽灵为了诱导我们……"

    if sys_effect2_current_file != "sound/Effect Sound/Duang 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Duang 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Duang 1.ogg"

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BA79E21F6467495A849CFF33257777BB as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_CDE407350E4A49AC8933C6D199FE9A13 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "噫呀呀呀呀！请、请不要说下去了——！！！"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_C98211B62EA04A368AA5021885891661 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "唔呵呵，叫得不错嘛♪"

    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不过没关系，这种超现实的话题……\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_B4A2258019834560B2658037BA91A812 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "啊，刚才还真有。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_A8EF2219CD9444569B9735243B55701F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "就是啊～！人能在空中飞什么的，幽灵也一定……"

    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "不、不至于吧～这个和那个是两回事～"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C4A4D54F058543A7828D7E40F7A5666F as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "没有什么幽灵♪幽灵都是骗人的♪都是睡迷糊的人看错的♪"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E8DD9768D82A468CA794353ED73907AD as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不过就算是这样，就算是这样，我们也♪……"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C0BD1F4E52FF496AA98961E053D79050 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_B4970C64BAAB484EA5A4C3E6C931521C "{size=32}好可怕～！！{/size}"

    window hide

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F9B0C2D0E2D84D6D85BC37C697E5F928 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 0.3

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯！？刚才……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_6536F8ADBA294923ABCC248AEAB17528 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "怎、怎么了……？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "有、有声音……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    stop music fadeout 1
    $ sys_music_current_file = ""

    show rs_image_D8F88F968B9E4B3CBEED302C0FA2B323 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你们先安静。\n"
    show rs_image_5739B888853E4BCE83F4B5FFEC74A1C2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "那边，有什么东西。"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_293AA514A24E4A44BB395EC06789F57B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_B4378AE67E6A4B08A37DF8E3C2E65B17 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    rs_character_B4970C64BAAB484EA5A4C3E6C931521C "{size=14}噫——！！！{/size}"

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_28F784D09B6C4DC7923149F266748707 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "卧倒！！"

    rs_character_B4970C64BAAB484EA5A4C3E6C931521C "是！！"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Battle 6.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 6.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 6.ogg"

    $ zorder_tag_66DB760C0228479AB543CB442FD4CD4E = 200
    show rs_image_7103FCF0405049A2A9636492EB968B3F as tag_66DB760C0228479AB543CB442FD4CD4E at center_top zorder zorder_tag_66DB760C0228479AB543CB442FD4CD4E onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if sys_music_current_file != "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg":
        play music "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg" loop
        $ sys_music_current_file = "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_DFC7EAA2966B4B62848D367D9579AFA0

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "{size=36}哦哦哦！！！{/size}"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_5739B888853E4BCE83F4B5FFEC74A1C2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Hit 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 3.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA71A79D75754B70A790643847D4F2C5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哈！！！"

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "噫！？\n"
    $ zorder_tag_66DB760C0228479AB543CB442FD4CD4E = 200
    show rs_image_C463A4717ED94299B8E9300E43B7A45F as tag_66DB760C0228479AB543CB442FD4CD4E at center_top zorder zorder_tag_66DB760C0228479AB543CB442FD4CD4E onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    extend "……呃～……"

    if sys_effect2_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_66DB760C0228479AB543CB442FD4CD4E
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 0.5

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_7DC581F0926C46E1B9B46277F2729C93 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这是什么东西？熊……类似的。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_BA79E21F6467495A849CFF33257777BB as tag_C389451CCE5A4CEAB24DEF9A7C02635D at left_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_C43CDCE2089F485094F071FBC81A3038 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "噫呀——！！比幽灵还可怕的东西出现了！！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "对啊！！完全忘记大自然的恐怖了！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_66DB760C0228479AB543CB442FD4CD4E = 100
    show rs_image_A8EF2219CD9444569B9735243B55701F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_69ED399C69E74B6BACE72BFAE0862603 as tag_66DB760C0228479AB543CB442FD4CD4E at Transform(xpos=-150, yalign=0.0) zorder zorder_tag_66DB760C0228479AB543CB442FD4CD4E onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_4C6E1175AEE0459B894D9CA5F8B20658 = 100
    show rs_image_B4378AE67E6A4B08A37DF8E3C2E65B17 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_7354908CD2ED469180084AE15C3932F1 as tag_4C6E1175AEE0459B894D9CA5F8B20658 at Transform(xpos=460, yalign=0.0) zorder zorder_tag_4C6E1175AEE0459B894D9CA5F8B20658 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_52B9C216A69D4C1294D69027AA9BBA09 = 100
    show rs_image_CA32B3074CBF4DB08BA59AE12141A4F7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_93A607A2064640039904CA3E4A160122 as tag_52B9C216A69D4C1294D69027AA9BBA09 at center_top zorder zorder_tag_52B9C216A69D4C1294D69027AA9BBA09 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……不好，被包围了……"

    if sys_effect2_current_file != "sound/Effect Sound/Wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_D6ADB3B2DBE647DC91A820FFA6D351E3 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_3E50473C6BE74F0694DCDB246EF2B19A

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "唔哇！唔呼唔呼！"

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "噫哦……噫哦……"

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "困……困……"

    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_CDE407350E4A49AC8933C6D199FE9A13 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_B4A2258019834560B2658037BA91A812 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D6BC962AE17948D893E50BE9B4670973

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "噫！不要过来！！我不好吃的！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我觉得自己很好吃不过能不吃就最好了～～～！！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_7C30D306B01C4984A6C86B48D0A0FD27 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "确认敌人，巨大熊三只，比起物理攻击还是魔法更有效。"

    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    show rs_image_C533295FFF704695B54B98B9893D98B9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_52B9C216A69D4C1294D69027AA9BBA09 zorder zorder_tag_52B9C216A69D4C1294D69027AA9BBA09 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "援助就拜托两位了！对方的弱点应该是火系。"

    show rs_image_52820B68402A48B88D6C1517EC79E403 as tag_52B9C216A69D4C1294D69027AA9BBA09 zorder zorder_tag_52B9C216A69D4C1294D69027AA9BBA09 onlayer master
    show rs_image_F9B0C2D0E2D84D6D85BC37C697E5F928 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "慎太郎不要在意MP尽可能输出！！翼君就负责回复HP！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_BA79E21F6467495A849CFF33257777BB as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_B4A2258019834560B2658037BA91A812 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_93A607A2064640039904CA3E4A160122 as tag_52B9C216A69D4C1294D69027AA9BBA09 zorder zorder_tag_52B9C216A69D4C1294D69027AA9BBA09 onlayer master
    with rs_effect_D89D56EB440E4694B833F77134864B90

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "你到底想让我做什么！？我只是花乃汤所属的普通慎酱啊！？"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "对呀！！这种时候还开什么玩笑！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "要是我靠唱歌真的能回复生命的话肯定会做的但是……！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_5EEBBCC1A1DD424FA293CA4EA0C6C4C6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔……果然这就是现实，能战斗的只有我一个……"

    window hide

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_5739B888853E4BCE83F4B5FFEC74A1C2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Battle 4.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 4.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 4.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_6DBEF4C3CA3942C490BB486CFC040195 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_9F8EA032E81344E3B32B192681064721 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    pause 0.4

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "既然如此……解除限制！全力上了！！"

    window hide

    pause 0.6

    show rs_image_5B5DF4DA677D4CD28DD1FC1DF3F476C9 as tag_52B9C216A69D4C1294D69027AA9BBA09 zorder zorder_tag_52B9C216A69D4C1294D69027AA9BBA09 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    if sys_effect_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_4C6E1175AEE0459B894D9CA5F8B20658
    hide tag_66DB760C0228479AB543CB442FD4CD4E
    with rs_effect_EA806967665045E388F41C134DBDE988

    pause 1

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "哦哦哦！！"

    if sys_effect_current_file != "sound/Effect Sound/Hit 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 2.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哈！！！"

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "呜！？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "呜哈！！！"

    if sys_effect_current_file != "sound/Effect Sound/Hit 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哈！{w=0.2}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Hit 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Hit 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Hit 3.ogg"

    extend "吼！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "呜呜！！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "加、加油哦绫濑君……！\n"
    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    # Gallery unlock: images/CG/Precept-of-justice/Precept-of-justice 2-1.png
    $ zorder_rs_image_26575D16067F4A9DA889C346CBB487A8 = -100
    show rs_image_26575D16067F4A9DA889C346CBB487A8 as rs_image_26575D16067F4A9DA889C346CBB487A8 zorder zorder_rs_image_26575D16067F4A9DA889C346CBB487A8 onlayer master
    hide rs_image_26575D16067F4A9DA889C346CBB487A8

    show rs_image_26575D16067F4A9DA889C346CBB487A8 as tag_52B9C216A69D4C1294D69027AA9BBA09 zorder zorder_tag_52B9C216A69D4C1294D69027AA9BBA09 onlayer master
    with rs_effect_F1D853AA1431437BBF572B63AF1E4944

    extend "……嗯？呜哇！！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "翼亲？！"

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "呜哇啊啊！！好大的触手！被吸盘……救、救救我！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "一之濑君！！"

    window hide

    stop music fadeout 2
    $ sys_music_current_file = ""

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_A463E4342E4C4913B00CFE87127016A2 as tag_52B9C216A69D4C1294D69027AA9BBA09 zorder zorder_tag_52B9C216A69D4C1294D69027AA9BBA09 onlayer master
    with rs_effect_53B376EDDA024633A3328E405F058927

    pause 0.3

    window show

    rs_character_9EDF48057FB84D428D56198A69E2880E "集中于眼前的战斗！！"

    rs_character_C473A7F2C0A44A78A0300ED989EA3752 "诶？"

    window hide

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_52B9C216A69D4C1294D69027AA9BBA09
    with rs_effect_A4443243EC4043A8B5E78595C25D3327

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 200
    show rs_image_E59E6F1DC5AA4840AB7DC104AB5CA1EC as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at center_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    if sys_music_current_file != "sound/BGM/Stage of HERO.ogg":
        play music "sound/BGM/Stage of HERO.ogg" loop
        $ sys_music_current_file = "sound/BGM/Stage of HERO.ogg"

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Beam 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Beam 1.ogg" loop
        $ sys_effect_current_file = "sound/Effect Sound/Beam 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A354D565142F4203AABA29F37DA989A2 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    pause 0.4

    window show

    rs_character_9EDF48057FB84D428D56198A69E2880E "{size=36}{color=#00FFFF}GYMNO BEAM！！！{/color}{/size}"

    stop effect fadeout 1
    $ sys_effect_current_file = ""

    rs_character_EED793CA73BD4B74986CA4112F0DBABA "{size=36}呜！！{/size}"

    window hide

    pause 0.5

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 0.6

    show rs_image_DFE7656E88C947F3914B1BDB28FDCEBD as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3

    window show

    rs_character_9EDF48057FB84D428D56198A69E2880E "好！那边的小个子也要战斗哦！！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_DFE7656E88C947F3914B1BDB28FDCEBD as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    show rs_image_7DC581F0926C46E1B9B46277F2729C93 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "刚、刚才的是……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_80D8EF0BD0844464A179A184B542D31B as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "等下再解释！！那些家伙又来了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ zorder_tag_66DB760C0228479AB543CB442FD4CD4E = 300
    show rs_image_93A607A2064640039904CA3E4A160122 as tag_66DB760C0228479AB543CB442FD4CD4E at Transform(xpos=-100, yalign=0.0) zorder zorder_tag_66DB760C0228479AB543CB442FD4CD4E onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "呜啊啊啊！呜啊啊啊！"

    if sys_effect_current_file != "sound/Effect Sound/Drum 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Drum 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Drum 1.ogg"

    $ zorder_tag_4C6E1175AEE0459B894D9CA5F8B20658 = 300
    show rs_image_93A607A2064640039904CA3E4A160122 as tag_4C6E1175AEE0459B894D9CA5F8B20658 at Transform(xpos=350, yalign=0.0) zorder zorder_tag_4C6E1175AEE0459B894D9CA5F8B20658 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "唔！！"

    hide tag_66DB760C0228479AB543CB442FD4CD4E
    hide tag_4C6E1175AEE0459B894D9CA5F8B20658
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_DFE7656E88C947F3914B1BDB28FDCEBD as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    show rs_image_7DC581F0926C46E1B9B46277F2729C93 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_9EDF48057FB84D428D56198A69E2880E "听好了，前卫是你，我是后卫。愉快合作打倒它们！！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯、嗯！慎太郎，接下来会很混乱找个地方藏起来！！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B4378AE67E6A4B08A37DF8E3C2E65B17 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-120, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_AE2879D336AC4FEF9997D54F17B41E88

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "马上！你不说我也会去的！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_E59E6F1DC5AA4840AB7DC104AB5CA1EC as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    show rs_image_5739B888853E4BCE83F4B5FFEC74A1C2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9EDF48057FB84D428D56198A69E2880E "好了，上吧！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯！"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    # Gallery unlock: images/CG/Precept-of-justice/Precept-of-justice 3.png
    $ zorder_rs_image_54C31AC2FA71447087DF924311BF70EC = -100
    show rs_image_54C31AC2FA71447087DF924311BF70EC as rs_image_54C31AC2FA71447087DF924311BF70EC zorder zorder_rs_image_54C31AC2FA71447087DF924311BF70EC onlayer master
    hide rs_image_54C31AC2FA71447087DF924311BF70EC

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    show rs_image_54C31AC2FA71447087DF924311BF70EC as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EA806967665045E388F41C134DBDE988

    pause 0.8

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "哈！{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "呼！！{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "吼！！！"

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "呜"

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "姆"

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "噫"

    rs_character_9EDF48057FB84D428D56198A69E2880E "{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "BEAM！{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "BEAM！！{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "BEAM！！！"

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "噫"

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "呜噫"

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    rs_character_9EE015BA31314B149F5FA89B44759AA4 "姆"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……简直就是碾压……"

    window hide

    pause 0.8

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_B2DBE7CD3A504BD39A635232397DF931

    pause 2

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C84270558B44454A2A6E8B66021E559 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 0.6

    if sys_music_current_file != "sound/BGM/Something comical 1.ogg":
        play music "sound/BGM/Something comical 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something comical 1.ogg"

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 200
    show rs_image_2A2BEF79FCD844B490D59AD7A154C949 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_9EDF48057FB84D428D56198A69E2880E "呼，只有这种程度嘛。"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "非常感谢，帮大忙了。"

    show rs_image_DFE7656E88C947F3914B1BDB28FDCEBD as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9EDF48057FB84D428D56198A69E2880E "助人为乐就是我的义务。"

    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那么……果然你就是在楼顶跳来跳去的那位超人了？"

    show rs_image_E8F84349B64C4AE4A712B8B3F1D3A38E as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9EDF48057FB84D428D56198A69E2880E "啊～被看到了啊。就是说你们还特地追着我过来了？"

    show rs_image_A30E40C909B540CAA5B7C56736A22C28 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯……非常在意所以……\n"
    show rs_image_63589B9FEDCC4B28BC5D20C27E07C476 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不过英雄的真面目是必须被保密的呐。"

    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "在这之上还添了很多麻烦……抱歉。"

    show rs_image_DFE7656E88C947F3914B1BDB28FDCEBD as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9EDF48057FB84D428D56198A69E2880E "不不，很久没有和武斗派组队了还是很高兴的。\n"
    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_1626534B504446319B30BAF22C4EC025 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "最近的那个伙伴是专修魔法的，只有我能上前线。"

    show rs_image_7C30D306B01C4984A6C86B48D0A0FD27 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸～果然一般都是要为这颗星球的和平不断战斗的呐！！然后……"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_D7BB1A8267AE4353950D17F94CE6C389 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "那个～兴头上抱歉打扰不过，我们的翼公主还被抓走着呢……"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊，还有这么回事！\n"
    show rs_image_7DC581F0926C46E1B9B46277F2729C93 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "那个，我的朋友被……！"

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 200
    show rs_image_E8F84349B64C4AE4A712B8B3F1D3A38E as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9EDF48057FB84D428D56198A69E2880E "嗯，没关系，那位朋友已经在安全的地方避难了。"

    show rs_image_3E4C3CC93D2B4A9689B330A728C1C5AC as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "什、什么时候……不愧是英雄。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_4BBDCD83023642F6923D76BE102A1BB9 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "就是说很从容～？既然如此！！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 200
    show rs_image_4BBDCD83023642F6923D76BE102A1BB9 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_F0E8ECEB4D184568965014D5479E0737 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at right_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_9EDF48057FB84D428D56198A69E2880E "哇！？"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    # Gallery unlock: images/CG/Precept-of-justice/Precept-of-justice 4-2.png
    $ zorder_rs_image_A53B45F08CC449B5B3975CB5C5C64EF0 = -100
    show rs_image_A53B45F08CC449B5B3975CB5C5C64EF0 as rs_image_A53B45F08CC449B5B3975CB5C5C64EF0 zorder zorder_rs_image_A53B45F08CC449B5B3975CB5C5C64EF0 onlayer master
    hide rs_image_A53B45F08CC449B5B3975CB5C5C64EF0

    # Gallery unlock: images/CG/Precept-of-justice/Precept-of-justice 4-1.png
    $ zorder_rs_image_9C8D732DF7E24E7F953E682C4348EA0A = -100
    show rs_image_9C8D732DF7E24E7F953E682C4348EA0A as rs_image_9C8D732DF7E24E7F953E682C4348EA0A zorder zorder_rs_image_9C8D732DF7E24E7F953E682C4348EA0A onlayer master
    hide rs_image_9C8D732DF7E24E7F953E682C4348EA0A

    # Gallery unlock: images/CG/Precept-of-justice/Precept-of-justice 4.png
    $ zorder_rs_image_6BDC463AF3034115B872FE8114549896 = -100
    show rs_image_6BDC463AF3034115B872FE8114549896 as rs_image_6BDC463AF3034115B872FE8114549896 zorder zorder_rs_image_6BDC463AF3034115B872FE8114549896 onlayer master
    hide rs_image_6BDC463AF3034115B872FE8114549896

    $ zorder_tag_03723FC929AD4F0BA44259F7A076ADFD = 200
    $ zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD = 200
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_A53B45F08CC449B5B3975CB5C5C64EF0 as tag_03723FC929AD4F0BA44259F7A076ADFD at center_bottom zorder zorder_tag_03723FC929AD4F0BA44259F7A076ADFD onlayer master
    show rs_image_9C8D732DF7E24E7F953E682C4348EA0A as tag_0BDB8A4A05BB44ED81AE140BE96066BD at center_bottom zorder zorder_tag_0BDB8A4A05BB44ED81AE140BE96066BD onlayer master
    show rs_image_6BDC463AF3034115B872FE8114549896 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.9

    hide tag_0BDB8A4A05BB44ED81AE140BE96066BD
    hide tag_03723FC929AD4F0BA44259F7A076ADFD
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "你那个全身紧身衣，再让我好好看看嘛～"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "慎太郎！对正义的英雄太失礼了！"

    rs_character_9EDF48057FB84D428D56198A69E2880E "没、没、没关系。看看也不会少什么……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "欸——！那摸一下好不好！？呐呐让我摸摸嘛！？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "慎、慎太郎！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "话是这么说，小忍不是也对这件套装的材料很感兴趣吗？"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "这、这当然……"

    rs_character_9EDF48057FB84D428D56198A69E2880E "欸……和解了？嘛、算了，如你们所愿好了～"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀太好了！！那就不客气了！"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "失礼了。\n"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_7D01705A898341B492157D7AAE403B84 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    extend "……啊，比想像中的要薄呐。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "那个射线果然是英雄本身的能力，\n腕上似乎也没什么机关……"

    rs_character_57471360F48A413AB843A4E46D8C5541 "哈……啊……"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呀～真色呐……{w}不对，真帅气啊～快忍不住了～"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "裤子下面也有套装……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    rs_character_57471360F48A413AB843A4E46D8C5541 "等、等等，那边就不要……！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "再来一点嘛！！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "再多等一下……！"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "{color=#FF80C0}啊、啊……{/color}{nw}"
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_03723FC929AD4F0BA44259F7A076ADFD
    hide tag_0BDB8A4A05BB44ED81AE140BE96066BD
    with rs_effect_BAF3BF757577455980E802743F48D2F9

    extend ""

    window hide

    pause 2.5

    if sys_effect_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C84270558B44454A2A6E8B66021E559 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A58FA4D4F3DA4D62A421C5FCE76AA975

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Grass 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Grass 1.ogg"

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 200
    show rs_image_BCFB20456B6D43D6BC37C1D09AC7CB23 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_45B18A7E92D1470D8D1D06CD4730A1A1

    pause 0.5

    window show

    rs_character_9EDF48057FB84D428D56198A69E2880E "唔唔……看，你们的朋友在那边。"

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_F886D313ADF24EF0827EE545DCDFF7F0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "啊，绫濑君！奥村君！"

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_7DC581F0926C46E1B9B46277F2729C93 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "一之濑君！没事太好了！"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_A3E496DCEC7C4B75B1FF286D5EB3B496 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "本以为敌人只有那些毛茸茸的东西的，\n没想到居然会有巨大章鱼，真是太早下结论了～"

    show rs_image_F8376985E40140D4B85FF898F2E3F997 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "抱歉让你有了不好的回忆，明明说了要保护好的……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_5739B888853E4BCE83F4B5FFEC74A1C2 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "总之！那个章鱼也是怪物！？我去端了！！"

    show rs_image_93384CF7101E46B99C76C26B616C4A01 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那个……是……"

    stop music fadeout 5
    $ sys_music_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_B7002004B9C945ABA305FBBF878A4362 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "抓走我们的偶像可是重罪！去讨回公道小忍！"

    show rs_image_C533295FFF704695B54B98B9893D98B9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不，那个……所以说……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 200
    show rs_image_4F5C0A33D5614FA5BA5F63955E1180D4 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_9EDF48057FB84D428D56198A69E2880E "……"

    show rs_image_E8F84349B64C4AE4A712B8B3F1D3A38E as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_music2_current_file != "sound/BGM/To the future.ogg":
        play music2 "sound/BGM/To the future.ogg" loop
        $ sys_music2_current_file = "sound/BGM/To the future.ogg"

    rs_character_9EDF48057FB84D428D56198A69E2880E "那个章鱼的问题就交给我。不能让你们受伤。"

    show rs_image_DFE7656E88C947F3914B1BDB28FDCEBD as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "好了，这样就解决了，接下来就是离开森林了。"

    rs_character_9EDF48057FB84D428D56198A69E2880E "能打倒那么多魔物，应该不用太担心。"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_8FD1C2C6B9644301A434EC2DEE203B7F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……{w=0.5}{nw}"
    show rs_image_CF91581F91144E3C8277BC47DCBFC1F0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "我明白了。\n出去的路还记得，我们应该没问题的。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不能继续占用英雄的时间了。"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "麻烦你了啊。今天这段经历，这个感觉，绝对不会忘的！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_C533295FFF704695B54B98B9893D98B9 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "非常感谢……"

    show rs_image_DFE7656E88C947F3914B1BDB28FDCEBD as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_9EDF48057FB84D428D56198A69E2880E "嗯，那再见了。"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.7

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_4206BF0F2582432A8C2017FD937CB719 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那个，两位，有些话……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_E21ACD1443A4402AA37E7CE200FF6D4C as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C473A7F2C0A44A78A0300ED989EA3752 "？"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 1

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_A3D6CADEDC674400B7CD24D81BE7CC16 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_E04CCE237E8A462395C684CE40271A7A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_4C84270558B44454A2A6E8B66021E559 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.5

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "原来来是这样……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "这就有些对不起英雄君了。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_8D9EAB710DF84DAAA58AA16DC9ADFC74 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "嗯，很大的章鱼先生救了我。他一定是英雄的同伴……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_F9B0C2D0E2D84D6D85BC37C697E5F928 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "我要去道歉！明明被帮了这么多，还做出那种无礼的事……"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "我也去，就这么回去心里也不是滋味。"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_9071DE7B7E5343C897D93F24F8DF7BAF as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我也……那时候什么都没能说出来……这次要好好道谢。"

    window hide

    pause 0.7

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_B2054D14604A408CAF74D842FA9CF92A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_F6EC1BB1B1FF458CA64DC5A2BE557F78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_F8CB9EADFCAB4568A7D220AE1588A2E8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_4C84270558B44454A2A6E8B66021E559 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_F9DBAF1EE9EF4C7F828153AA794ECB5E

    pause 1.3

    show rs_image_0D67630697184B64BC76C377B00318F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "啊，在那边，听到声音了。"

    show rs_image_E21ACD1443A4402AA37E7CE200FF6D4C as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "真的，那边就是刚才的章鱼先生和……"

    show rs_image_3C4C246AAFC1459DBB1711584019784D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "那是救了我的章鱼先生！"

    window hide

    pause 0.7

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_B312A23449C84B4BB886D98AB7635507

    pause 2

    if sys_music_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music_current_file = "sound/Effect Sound/Wave 1.ogg"

    # Gallery unlock: images/CG/Precept-of-justice/Precept-of-justice 5.png
    $ zorder_rs_image_63D435C006354C2BA34CDE707A2F5EB7 = -100
    show rs_image_63D435C006354C2BA34CDE707A2F5EB7 as rs_image_63D435C006354C2BA34CDE707A2F5EB7 zorder zorder_rs_image_63D435C006354C2BA34CDE707A2F5EB7 onlayer master
    hide rs_image_63D435C006354C2BA34CDE707A2F5EB7

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_63D435C006354C2BA34CDE707A2F5EB7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D15EE2E27FB94685820AB97CA85D859F

    pause 1.5

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "……{w}现在好像不是去打扰的时候……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯嗯。"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "诶……为什么？"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "翼亲，现在不要去。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "可、可是，不去道歉的话……"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "应该那么做但……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊，既然如此，我带着笔和纸哦。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "干得好慎太郎！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "……啊，是这样。"

    window hide

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_AB948B0D45304509BAF5756D84F2B057

    pause 0.7

    # Gallery unlock: images/CG/Precept-of-justice/Precept-of-justice 5-1.png
    $ zorder_rs_image_8F1E01956CF44C7A87C37EDFB685642E = -100
    show rs_image_8F1E01956CF44C7A87C37EDFB685642E as rs_image_8F1E01956CF44C7A87C37EDFB685642E zorder zorder_rs_image_8F1E01956CF44C7A87C37EDFB685642E onlayer master
    hide rs_image_8F1E01956CF44C7A87C37EDFB685642E

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_8F1E01956CF44C7A87C37EDFB685642E as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 0.8

    window show

    rs_character_9EDF48057FB84D428D56198A69E2880E "嗯？纸？\n"
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.5

    extend "………"

    rs_character_3BBAA8C5C08941A6826287E4FAEAD42E "怎么了？守。"

    rs_character_57471360F48A413AB843A4E46D8C5541 "嗯，{w}果然，{w=0.8}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    extend "{color=#FFFF00}做了好事心情会很好！{/color}"

    window hide

    pause 1.5

    stop music2 fadeout 3
    $ sys_music2_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9AE31F3F53874BC98B8F6A7881FF50D3

    pause 5


    if judge_lm_condition([]):
        jump block_000041C4

    return

label block_000041C4:
    # Node: 000041C4 (正義的教訓 3)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F2217CE71C3849B9A0B1401B9AB2019C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_673B577A4E15407397C9C9B62906A309

    pause 1.5

    if sys_effect_current_file != "sound/Effect Sound/Switch 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Switch 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Switch 2.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 300
    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_5D43F2001123473FAF26C63FF5A36044 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 400
    show rs_image_2486E9AC1518402DA6CBAA06B85610C8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    window show

    rs_character_5AC24F70672E42179BCA906D6BF3849F "大、大家——！下午好——！是翼哥哥哦——！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_983D3ABC05A64E488B0C017601C96E4D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_B7D632B215DC48F886E24A21F27A219A "首先要元气满满地打招呼哦——！\n一、二，大——家——好～！！"

    rs_character_9B222CDB150149259BF774B73B26BF52 "……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_1BF70E7C1E054ED9AA4E4E9D14725C2F as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_B7D632B215DC48F886E24A21F27A219A "开、开玩笑的，抱歉失礼了……"

    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_B7D632B215DC48F886E24A21F27A219A "为什么要这样打招呼呢，\n当然是今天要演的剧码是{color=#FF0000}英雄故事{/color}！"

    show rs_image_9D4ED68CEC2D4E5BA0296B4CA2A90847 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_B7D632B215DC48F886E24A21F27A219A "小时候，大家都憧憬过的，梦想的存在……\n"
    show rs_image_0BD950ADC14245578BC5105060EF0E00 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "已经长大的大家也请回归童心好好享受！"

    show rs_image_15A2B3B975314AA1B94A1058C95E9FB0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B7D632B215DC48F886E24A21F27A219A "标题是{color=#FF0000}《Ultimate Man》{/color}！{w}那么开始了！！"

    window hide

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 1

    show rs_image_2D9493A55DC8485C824DF0F885B3D4FC as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    pause 4

    show rs_image_9C124BC2EA23427D804F5C004D21DF06 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.4

    if sys_effect2_current_file != "sound/Effect Sound/Thunder 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Thunder 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Thunder 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_E6AFB5423C9947A58B503412BB75E357 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    if sys_music_current_file != "sound/BGM/Drama.ogg":
        play music "sound/BGM/Drama.ogg" loop
        $ sys_music_current_file = "sound/BGM/Drama.ogg"

    window show

    rs_character_C4EC42614BFC49C4AA6B36B07765CEAC "亲爱的！亲爱的！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C925BB388DA34301AF033B05CCA35073 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_778AC52A4FD141E38A16785F72F29EFE as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_5F4F62C57989466EA541092868A7F473 "父亲大人！"

    rs_character_CEEF74930DCE4838B40554F6F032BB6D "父亲～！！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_9B222CDB150149259BF774B73B26BF52 "{color=#C0C0C0}？？？（黑人问号）……{/color}"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_792AF3E314934B62AEEA04F5B3C86285 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_8A11E465FF654D8F813A7292784648E8 "听好了，你们必须要为父报仇。{w}\n为此必须要打倒威胁和平的我们的敌人……"

    rs_character_8A11E465FF654D8F813A7292784648E8 "必须要消灭{color=#8080FF}乌贼乌贼星人{/color}！！！！\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "赌上{color=#FF0000}Ultiman{/color}一族的名誉！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_9C4A096078AC4865815C37EB2372FC1B as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_CCEB3276FE42480B9F0D6D4E0AEDB6D9 "我明白了，妈妈！！我们毕竟是有着守护世界和平的力量的！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_3694C9C08ECF4C04B386D995A0A0F230 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_104194B4514C43EDACB2FBE0139785AC "要成为比父亲更加更加强大的英雄，一定要拯救世界！！"

    rs_character_104194B4514C43EDACB2FBE0139785AC "绝不会让乌贼乌贼星人之流夺取这颗星球！！"

    show rs_image_57A69621F1D74FC6B4F065FC592FCAC7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8A11E465FF654D8F813A7292784648E8 "很好，我会期待的。{w}不过……"

    show rs_image_792AF3E314934B62AEEA04F5B3C86285 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8A11E465FF654D8F813A7292784648E8 "那孩子好慢。只是买个东西究竟要多久……"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 400
    show rs_image_5D43F2001123473FAF26C63FF5A36044 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    show rs_image_2486E9AC1518402DA6CBAA06B85610C8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_B7D632B215DC48F886E24A21F27A219A "大家！作为主角的英雄终于登场了哦！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_983D3ABC05A64E488B0C017601C96E4D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_B7D632B215DC48F886E24A21F27A219A "大家一起来欢呼！"
    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    extend "一、二！{color=#FF0000}Ultimate Man！！{/color}"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_9B222CDB150149259BF774B73B26BF52 "ul、ultimate man……"

    window hide

    pause 0.3

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Eye shine 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Eye shine 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Eye shine 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_07883B464A8E44059F33DB50D82BCA1D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.9

    show rs_image_B39E11A4362B45DDB6F8F0B644CF1D36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_65B13C186816400F9E3478FC93161EE2 "……我回来了，母亲大人，还有，哥哥们。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_21F080E325C94AE69523468BCB8F1795 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_B39E11A4362B45DDB6F8F0B644CF1D36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    rs_character_8A11E465FF654D8F813A7292784648E8 "太慢了！！真是的！！到底去什么地方闲晃了！？"

    show rs_image_792AF3E314934B62AEEA04F5B3C86285 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8A11E465FF654D8F813A7292784648E8 "那么，做饭的材料买到了没？？"

    show rs_image_D02EFDA626A044D0A5B626EA2ABAACF9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "这、这个……土豆卖完了……"

    show rs_image_21F080E325C94AE69523468BCB8F1795 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8A11E465FF654D8F813A7292784648E8 "……你什么都干不好！行了，你可以休息了"

    show rs_image_57A69621F1D74FC6B4F065FC592FCAC7 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8A11E465FF654D8F813A7292784648E8 "你妈我自己去！你就留下来看家！"

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "是的……母亲大人。"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.9

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_D02EFDA626A044D0A5B626EA2ABAACF9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_9C4A096078AC4865815C37EB2372FC1B as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    show rs_image_3694C9C08ECF4C04B386D995A0A0F230 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_CCEB3276FE42480B9F0D6D4E0AEDB6D9 "你还真是没用！"

    rs_character_104194B4514C43EDACB2FBE0139785AC "到现在还麻烦母亲！真是Ultiman一族的耻辱！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_CCEB3276FE42480B9F0D6D4E0AEDB6D9 "你这种在家里老老实实看书写字就行了！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_104194B4514C43EDACB2FBE0139785AC "乌贼乌贼星人就由我们来打倒，明白了吗。"

    show rs_image_B39E11A4362B45DDB6F8F0B644CF1D36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "我明白了，哥哥大人……"

    show rs_image_98561AA9F19949BC932EB3BEEBB1E7E7 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_CCEB3276FE42480B9F0D6D4E0AEDB6D9 "走！"

    show rs_image_9A7250E3EA3449329B06DE7ECF8CAE8C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_104194B4514C43EDACB2FBE0139785AC "嗯！"

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.7

    show rs_image_D02EFDA626A044D0A5B626EA2ABAACF9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "……"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 400
    show rs_image_5D43F2001123473FAF26C63FF5A36044 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    show rs_image_17B63D85141F4D91A903BDDBAA7EA884 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_B7D632B215DC48F886E24A21F27A219A "啊，好可怜的Ultimate Man。"

    rs_character_B7D632B215DC48F886E24A21F27A219A "因为母亲和哥哥的缘故，作为英雄也无法战斗。"

    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B7D632B215DC48F886E24A21F27A219A "不过，就算是这样的Ultimate Man，某一天，也迎来了机会。"

    window hide

    pause 0.4

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_2925F20029814B29BE7B230E5B76ED86 "呀——！乌贼乌贼星人！谁来救救我们——！"

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_D1AB248F7F634CDBB48A2D3A92CFF03F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "不好了！外面有谁在呼救！"
    show rs_image_B39E11A4362B45DDB6F8F0B644CF1D36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "可现在家里只有我。"

    show rs_image_07883B464A8E44059F33DB50D82BCA1D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "我、我必须去！"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "现在就去！！"
    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    extend "哈！！"

    rs_character_2925F20029814B29BE7B230E5B76ED86 "哇！是Ultimate Man！来救我们了！"

    rs_character_2925F20029814B29BE7B230E5B76ED86 "乌贼乌贼星人算什么，打扁它们！"

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_07883B464A8E44059F33DB50D82BCA1D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_5347402CC2724A2BAD6DFA4C3193FA8E

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "觉、做好觉悟～乌贼乌贼星人！\n"
    show rs_image_B39E11A4362B45DDB6F8F0B644CF1D36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "算是我是一族里最弱小的……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_07883B464A8E44059F33DB50D82BCA1D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "这样的我也寄宿着正义的力量！绝对不会输给你这种家伙！！"

    window hide

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_76AF34D70BF845CB9284A08A28F7BE3D as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_B3C7073FD076476C856ACCC134A30A64

    pause 0.4

    window show

    rs_character_1DC2D3936AC3424E97131914161D1CF1 "不知好歹的小子！看我做了你！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_76AF34D70BF845CB9284A08A28F7BE3D as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_07883B464A8E44059F33DB50D82BCA1D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "哈！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    show rs_image_EDC3452D5A9942C2A29872DCC6E91A6E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "哇！被——打——败——了……"

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.7

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_D1AB248F7F634CDBB48A2D3A92CFF03F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "太好了！太好了！第一次胜利！我也能击退乌贼乌贼星人了！"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "唔……"

    show rs_image_B39E11A4362B45DDB6F8F0B644CF1D36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "不过，真可悲呐……我听到的那些恶质的传闻到底是真是假。"

    show rs_image_10AF58709C614B95B1819EED5FB8B4D8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "只听信传闻而不能亲眼确认也很迷茫，这次就亲自看看。"

    show rs_image_638AA4DC09BB4CA8A27AAE747E157F9B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "请帮忙把这个乌贼乌贼星人移动到其他安全的地方。{w}呼。"

    window hide

    pause 0.3

    if sys_music2_current_file != "sound/Effect Sound/Walk 1.ogg":
        play music2 "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_FFC620A1302E417EBD9CB71C6CDE9274

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 2

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_937347463B844868AA4519AAB0889E21 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_B39E11A4362B45DDB6F8F0B644CF1D36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "为什么，要救我的说。"

    show rs_image_68199263B23E4EB68FFE2CB1F677A4C0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "我并没亲眼见到你做坏事，只是因为你在那里，就擅自这么认定了。"

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "然后便开始了攻击。真的很对不起。"

    show rs_image_48421AD9C9AF4EDAA9F7466A007E1A95 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "我们在你们眼里就是坏人，攻击也是无可奈何的说。"

    show rs_image_638AA4DC09BB4CA8A27AAE747E157F9B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "你会攻击我或者其他人吗？"

    show rs_image_E1DF2702814A4B1EACE992290C0B6A0D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "还……从没做过的说。"

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "我们讨厌争斗的说，我们只是喜欢散步的快乐的乌贼的说。"

    show rs_image_10AF58709C614B95B1819EED5FB8B4D8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "那我就不会把你当做坏人。而且，因为这样就开始攻击也不对。"

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "就算过去你的同胞攻击过人类，那也与你无关。"

    show rs_image_B39E11A4362B45DDB6F8F0B644CF1D36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "所以，是一眼便把你定性为坏人的我不好。\n"
    show rs_image_937347463B844868AA4519AAB0889E21 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "抱歉，身体还好吗？"

    show rs_image_BA3FE361CF524C029339B830E6EB71E8 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "你是个好人的说，我还是第一次遇到你这样的人的说。"

    show rs_image_F43BD18A617C49799A20916E9BDF72C1 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "可以的话……我想和你好好相处的说。我想和你做朋友的说。"

    show rs_image_10AF58709C614B95B1819EED5FB8B4D8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "真的？我们可以成为朋友吗？"

    show rs_image_BA3FE361CF524C029339B830E6EB71E8 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "当然了的说！请多指教的说！"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 400
    show rs_image_5D43F2001123473FAF26C63FF5A36044 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_B7D632B215DC48F886E24A21F27A219A "就这样，两人之间诞生了友情的萌芽。"

    rs_character_B7D632B215DC48F886E24A21F27A219A "两人经常背着母亲和兄弟的目光一起外出，一起游玩。"

    show rs_image_9D4ED68CEC2D4E5BA0296B4CA2A90847 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B7D632B215DC48F886E24A21F27A219A "但是，这种快乐的日子是不会永远持续下去的。"

    window hide

    pause 0.3

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_21F080E325C94AE69523468BCB8F1795 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_8A11E465FF654D8F813A7292784648E8 "嗯？有奇怪的味道。你们在那边站好！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_989F509905E64B179B0F6123E256F90C as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_CCEB3276FE42480B9F0D6D4E0AEDB6D9 "不是我。"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_C9F3447ECA5B4C70ACB11853F96C2125 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_104194B4514C43EDACB2FBE0139785AC "也不是我。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_D02EFDA626A044D0A5B626EA2ABAACF9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "唔……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_21F080E325C94AE69523468BCB8F1795 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8A11E465FF654D8F813A7292784648E8 "你！！你身上有乌贼的气味！！"

    show rs_image_A5FE8C164D1D420C9534C9F7A849311E as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8A11E465FF654D8F813A7292784648E8 "难道说！你偷偷溜出家门去干什么见不得人的勾当了！？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_9C4A096078AC4865815C37EB2372FC1B as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_CCEB3276FE42480B9F0D6D4E0AEDB6D9 "妈妈，听我说！我听到了一个传闻。"

    show rs_image_792AF3E314934B62AEEA04F5B3C86285 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8A11E465FF654D8F813A7292784648E8 "什么？详细说说。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_9A7250E3EA3449329B06DE7ECF8CAE8C as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_104194B4514C43EDACB2FBE0139785AC "我也知道！据说有人看到了乌贼乌贼星人和人类一起关系很好的样子！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_C9F3447ECA5B4C70ACB11853F96C2125 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_D02EFDA626A044D0A5B626EA2ABAACF9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_989F509905E64B179B0F6123E256F90C as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_CCEB3276FE42480B9F0D6D4E0AEDB6D9 "难道说，指的就是这家伙不成？？"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_499742D6A86840128DDBE1B0D9E0BB65 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at center_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8A11E465FF654D8F813A7292784648E8 "什么！！！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9295663F0C2C4F39AFABBD57A66F68EC as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8A11E465FF654D8F813A7292784648E8 "你！！你觉得作为Ultiman一族的一员这种事可能被原谅吗！？"

    rs_character_8A11E465FF654D8F813A7292784648E8 "你想给殉职的父亲脸上抹黑！？"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_D1AB248F7F634CDBB48A2D3A92CFF03F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at right_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "母亲大人，不是这样的，这是！"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_21F080E325C94AE69523468BCB8F1795 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8A11E465FF654D8F813A7292784648E8 "闭嘴！你这样的家伙不是我们家的孩子！！"

    rs_character_8A11E465FF654D8F813A7292784648E8 "不知廉耻！！出去！"

    show rs_image_D02EFDA626A044D0A5B626EA2ABAACF9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "……"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    rs_character_B7D632B215DC48F886E24A21F27A219A "Ultimate Hero被逐出了家门。{w}\n没有归宿，没有目标，只是在机械地前行……"

    window hide

    pause 0.3

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_D02EFDA626A044D0A5B626EA2ABAACF9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "（抽泣）……"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_BFC824A4F0E34951A0C31A4CFCCF7B81 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "怎么了的说？发生什么了的说？？"

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "我被逐出家门了，没有地方可以去了。"

    show rs_image_E1DF2702814A4B1EACE992290C0B6A0D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "真可怜。\n"
    show rs_image_BA3FE361CF524C029339B830E6EB71E8 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "既然这样，来我们、我们乌贼乌贼星人的住处好不好。"

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "我家也在那里，就住在那里。"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_10AF58709C614B95B1819EED5FB8B4D8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "真的！？谢谢！乌贼乌贼星人。"

    window hide

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.4

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    window show

    rs_character_B7D632B215DC48F886E24A21F27A219A "就这样两人同居了。{w}不过，世界上的事情不是这么简单的。"

    rs_character_B7D632B215DC48F886E24A21F27A219A "在那边也有各种各样的困难在等待着。"

    window hide

    pause 0.3

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_638AA4DC09BB4CA8A27AAE747E157F9B as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    window show

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "抱歉，请给我一个土豆。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_10E8D072A8DF4FF98FCF4B707B4C5D05 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_1DAD4C7807EA40A48E26D338ED51E752 "我们这里不卖人类的商品的说！！"

    show rs_image_D02EFDA626A044D0A5B626EA2ABAACF9 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "唔……不管怎么找也没有。这下子根本做不了好吃的饭……"

    window hide

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    stop music fadeout 3
    $ sys_music_current_file = ""

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 400
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1.2

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_BFC824A4F0E34951A0C31A4CFCCF7B81 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "我回来了～哦呀？没有开灯的说？"

    show rs_image_BA3FE361CF524C029339B830E6EB71E8 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "好了好了，肚子饿了的说，今天的晚饭是什么的说……"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_B39E11A4362B45DDB6F8F0B644CF1D36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_48421AD9C9AF4EDAA9F7466A007E1A95 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "哇！？怎么了的说！？"

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.4

    if sys_music_current_file != "sound/BGM/Drama.ogg":
        play music "sound/BGM/Drama.ogg" loop
        $ sys_music_current_file = "sound/BGM/Drama.ogg"

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "（抽泣）我果然不能住在这里。"

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "果然人类和乌贼是不可能的，一定存在差别的。这是肯定的。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_EDC3452D5A9942C2A29872DCC6E91A6E as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "才没有那种事的说！！绝对不能这么气馁的说。"

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "因为，不是别人正是你自己，跨越了那道壁垒不是嘛。"

    show rs_image_76AF34D70BF845CB9284A08A28F7BE3D as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "好好交流的话肯定其他乌贼也能理解的！好，我去和大家说！！"

    show rs_image_68199263B23E4EB68FFE2CB1F677A4C0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "乌贼乌贼星人……"

    show rs_image_937347463B844868AA4519AAB0889E21 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "我去了的说。"

    window hide

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 400
    show rs_image_5D43F2001123473FAF26C63FF5A36044 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_B7D632B215DC48F886E24A21F27A219A "乌贼乌贼星人的奋力劝说令其他乌贼相信了这种可能性。"

    show rs_image_15A2B3B975314AA1B94A1058C95E9FB0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B7D632B215DC48F886E24A21F27A219A "就这样，随着这个想法开始传达出去，两人的日常再度归于和平。"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.8

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_10AF58709C614B95B1819EED5FB8B4D8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_92BA738ECC554DD68424281B020F4A98 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    window show

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "拜乌贼乌贼星人所赐，我现在非常幸福，每天都那么快乐。"

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "你教会了我们无比重要的事情。争斗一定不久之后就会平息的说。"

    show rs_image_F43BD18A617C49799A20916E9BDF72C1 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_10AF58709C614B95B1819EED5FB8B4D8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "乌贼乌贼星人……"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    rs_character_CCEB3276FE42480B9F0D6D4E0AEDB6D9 "原来在这里！！愚蠢的弟弟！"

    rs_character_104194B4514C43EDACB2FBE0139785AC "今天必须要把你带回去！！"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3694C9C08ECF4C04B386D995A0A0F230 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_9C4A096078AC4865815C37EB2372FC1B as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.9

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_10E8D072A8DF4FF98FCF4B707B4C5D05 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "哥哥大人！？"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_C925BB388DA34301AF033B05CCA35073 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_104194B4514C43EDACB2FBE0139785AC "都怪你和乌贼乌贼星人这么近，我们！母亲也！！"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_98561AA9F19949BC932EB3BEEBB1E7E7 as tag_073D4E2B5E224963B025F95C92ED797A at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_CCEB3276FE42480B9F0D6D4E0AEDB6D9 "传闻越来越广，Ultimate Man一族已经颜面扫地，\n妈妈揽下了所有罪过，最后含冤离去。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_9A7250E3EA3449329B06DE7ECF8CAE8C as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_9C4A096078AC4865815C37EB2372FC1B as tag_073D4E2B5E224963B025F95C92ED797A at left_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_CCEB3276FE42480B9F0D6D4E0AEDB6D9 "混蛋！！可恶的乌贼乌贼星人！！我们要报一族的仇恨！！"

    rs_character_104194B4514C43EDACB2FBE0139785AC "一定要宰了你！！以正义之名！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_68199263B23E4EB68FFE2CB1F677A4C0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "等等！！不要！"

    window hide

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 0.8

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    window show

    rs_character_B7D632B215DC48F886E24A21F27A219A "战斗的结果，是同归于尽。双方全都倒下了。"

    window hide

    pause 0.5

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_EDC3452D5A9942C2A29872DCC6E91A6E as tag_A77E36FB70FF4F60B12060B2747E46D1 at center_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_F3A62EC81C5F4C45A38223D03BAC35AE "唔哇……！！"

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_8B0CAF9FBBF548B2AE945D0D140CBDDA

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_B39E11A4362B45DDB6F8F0B644CF1D36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    window show

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "乌贼乌贼星人！"

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_778AC52A4FD141E38A16785F72F29EFE as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_CCEB3276FE42480B9F0D6D4E0AEDB6D9 "哈哈……终于解决掉这家伙了，这下子妈妈也能安息了……"

    show rs_image_10E8D072A8DF4FF98FCF4B707B4C5D05 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "诶！？为什么说……？"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_3694C9C08ECF4C04B386D995A0A0F230 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=430, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_104194B4514C43EDACB2FBE0139785AC "母亲和我们都无法原谅把你拐走的这家伙。"

    show rs_image_98561AA9F19949BC932EB3BEEBB1E7E7 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_CCEB3276FE42480B9F0D6D4E0AEDB6D9 "你对我们最重要了。我们一开始只是想让你出去冷静一下，\n过几分钟就会把你找回去的。"

    show rs_image_9A7250E3EA3449329B06DE7ECF8CAE8C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_104194B4514C43EDACB2FBE0139785AC "可是，却被这家伙夺走了。不过现在，就能从乌贼混蛋手里救回来了。"

    show rs_image_BF774FD732DA4372BE35878A2F3CD2C3 as tag_073D4E2B5E224963B025F95C92ED797A zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_CCEB3276FE42480B9F0D6D4E0AEDB6D9 "让一族最弱的你守在家里是我们唯一能想到的能保护好你的方法。\n不过接下来你就要一……个人生活了。"

    show rs_image_D15801E88DF345DBBD7F8335FDF28DB6 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_104194B4514C43EDACB2FBE0139785AC "没能一直好好保护你对不起。我不会说再见的，胆小鬼，要加油……啊……"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_446CB9E7B6074C7F87730DF5D4AF793D

    pause 0.7

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_B39E11A4362B45DDB6F8F0B644CF1D36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "怎么会……怎么会这样……\n"
    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    extend "呜哇啊啊啊啊啊！！！"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_1DAD4C7807EA40A48E26D338ED51E752 "怎么了！！在闹什么！！"

    rs_character_1DAD4C7807EA40A48E26D338ED51E752 "混蛋！！可恶的人类！！对我们的同胞做了什么！！"

    rs_character_1DAD4C7807EA40A48E26D338ED51E752 "果然人类都是骗子！！既然这样干脆灭了他们！！"

    pause 0.3

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 400
    show rs_image_5D43F2001123473FAF26C63FF5A36044 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    show rs_image_9D4ED68CEC2D4E5BA0296B4CA2A90847 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_B7D632B215DC48F886E24A21F27A219A "悲剧终于迎来了起点。"

    rs_character_B7D632B215DC48F886E24A21F27A219A "双方的争斗愈演愈烈，世界向着毁灭的道路一步步滑下。"

    window hide

    pause 0.3

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.8

    show rs_image_B92B887E08834FC5A17F09C47C396C17 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_C8D0380A6B3B4071BD17EE2CFA40D67E

    pause 1

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_B39E11A4362B45DDB6F8F0B644CF1D36 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    window show

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "已经……无所谓了。什么都……死活都无所谓了。"

    pause 0.4

    if sys_effect_current_file != "sound/Effect Sound/Finger Snap 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 2.ogg"

    show rs_image_E68D7CEBF22344F0B43187D36C2B71B6 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    rs_character_9EDF48057FB84D428D56198A69E2880E "孩子啊……"

    show rs_image_10E8D072A8DF4FF98FCF4B707B4C5D05 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "诶……这个声音是……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.4

    if sys_effect2_current_file != "sound/Effect Sound/Finger Snap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    show rs_image_7CBDD0664EB44F05A512AB8E30444417 as tag_81DF0CF91B224EAAA16B0366711BA01F at right_top zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_E105874A5CD740D285F7ACB5031E97EB

    rs_character_D4327E518BA046DF9D26429DB75D6477 "好久不见啊，我的孩子。已经忘了我了吗。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_D1AB248F7F634CDBB48A2D3A92CFF03F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "父亲大人！！怎么可能忘记！！我一直都记得！"

    show rs_image_249AD614447348FC9211D112E3DA7672 as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_FC24FA7704C34AA19E782D403AB120CA "不，你已经忘了。你现在，不仅是我，连你自己都已经迷失了。"

    show rs_image_3EF810DF1BBA46FB910DD986A761F8FD as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_FC24FA7704C34AA19E782D403AB120CA "我的孩子啊，你是Ultiman一族的一员……你是拯救世界的英雄！！"

    show rs_image_7E8094E3B0244C59B26D036A4F6D26A8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "英雄……我这样的……"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    show rs_image_10E8D072A8DF4FF98FCF4B707B4C5D05 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_3CE8AB3CEF264256B7E0BD2304BE562C as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    rs_character_FC24FA7704C34AA19E782D403AB120CA "再好好想想，你究竟是什么人！！\n你是我的孩子，你是现在仅存的唯一的英雄！！！"

    pause 0.4

    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    with rs_effect_1C428704E5E24078848D388A31B861CE

    pause 0.9

    show rs_image_7E8094E3B0244C59B26D036A4F6D26A8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 1.4

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_07883B464A8E44059F33DB50D82BCA1D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "是啊……我是英雄！！我要拯救世界！！！"

    window hide

    pause 0.7

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.7

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 400
    show rs_image_5D43F2001123473FAF26C63FF5A36044 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    show rs_image_8A626993E4D845D382910F0B900F3F2B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_B7D632B215DC48F886E24A21F27A219A "终于，Ultimate Hero出动了！{w}同时，最大的困难也浮现了！"

    show rs_image_9F9E3AB5982941C7A3FF42BB60F86B4D as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_B7D632B215DC48F886E24A21F27A219A "这颗星球，突然成为了某巨大陨石的目标。{w}\n就像是，争斗突然变得微不足道，重归寂静……"

    window hide

    pause 0.3

    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    show rs_image_B92B887E08834FC5A17F09C47C396C17 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.7

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "完蛋了！！\n"
    if sys_effect2_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "世界要毁灭了！！\n"
    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "已经没戏了！！"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_11F618502DA34C33A4D83F14BE1EA04F as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_66C39315E2E44A2AB7009268529FCA34 "隆隆隆隆！！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_07883B464A8E44059F33DB50D82BCA1D as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_64306473DF684E3FAFE0CF654B017265

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "这个世界要由我拯救！！\n"
    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "看招！！！！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect3_current_file != "sound/Effect Sound/Battle 6.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Battle 6.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Battle 6.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_93830EF9BFE74D7F9502C7940A23AFC1 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9430B522B96F4776A6267883EBC70B80

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    show rs_image_3DB3E4837FF142F5BA8FE801C602667F as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_52F8AA25B7AF40D584EAB249FAFE9B0C "呜哇……"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    window hide

    pause 1

    show rs_image_9C124BC2EA23427D804F5C004D21DF06 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_C8D0380A6B3B4071BD17EE2CFA40D67E

    pause 0.8

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_14FEF7C178554444A31252FD66ED09D6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    window show

    rs_character_B1BD18743BEC4D0F8D7522E76D84FA51 "拯救人类和乌贼乌贼星人……这就是我的使命……"

    show rs_image_10AF58709C614B95B1819EED5FB8B4D8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_0EEF5B963A544F2DBEA6C89B48BDD52F

    pause 0.7

    rs_character_2925F20029814B29BE7B230E5B76ED86 "他救了这个世界……"

    rs_character_1DAD4C7807EA40A48E26D338ED51E752 "已经不是争斗的时候了，下次一定要由我们亲手保护这个世界！！"

    window hide

    pause 0.7

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.5

    $ zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 400
    show rs_image_5D43F2001123473FAF26C63FF5A36044 as tag_241AF4B67B0B4452B97B2944C6D13AFE at center_bottom zorder zorder_tag_241AF4B67B0B4452B97B2944C6D13AFE onlayer master
    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    rs_character_B7D632B215DC48F886E24A21F27A219A "就这样，以自己的性命为代价，Ultimate Hero令世界重归和平。"

    show rs_image_15A2B3B975314AA1B94A1058C95E9FB0 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_B7D632B215DC48F886E24A21F27A219A "故事，也就到此为止了。"

    window hide

    pause 0.8

    if sys_effect2_current_file != "sound/Effect Sound/Clap 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clap 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Clap 1.ogg"

    stop music fadeout 4
    $ sys_music_current_file = ""

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_241AF4B67B0B4452B97B2944C6D13AFE
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_04460297D37A447D8CE6298460DB7159

    pause 5

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.5


    if judge_lm_condition([]):
        jump block_000041C3

    return

label block_000041C3:
    # Node: 000041C3 (正義的教訓 4)
    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_D0A2F3892CC04807B56A93B9E691BA42 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.9

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 400
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_0B30A99001644A018C47ABCD41C30F9A as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_2486E9AC1518402DA6CBAA06B85610C8 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at center_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_EA4ACE3D61BB4E55AC643AD05DFE8DD0 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_music_current_file != "sound/BGM/The hope.ogg":
        play music "sound/BGM/The hope.ogg" loop
        $ sys_music_current_file = "sound/BGM/The hope.ogg"

    pause 0.4

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "大家辛苦了～！呀，干得不错嘛！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "一开始有意见的客人们最后也投入故事的世界中了呐，太好了。"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "嘛，你的话一次也没出错不是挺好吗？虽说好几次差点。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_A2C536146FD94F36A1473E7F475A8AA9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "说起来，你那个老妈演得是在太那个了，我可是好不容易忍住不笑的。"

    $ zorder_tag_81DF0CF91B224EAAA16B0366711BA01F = 200
    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_B7DA8760D1894ADDAD4A804423AB38E0 as tag_81DF0CF91B224EAAA16B0366711BA01F at Transform(xpos=430, yalign=0.0) zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    show rs_image_49D4F7003E234005BC5B86C34093DEFD as tag_073D4E2B5E224963B025F95C92ED797A at center_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哥哥，最后那个父亲角色的演出非常勇猛、非常帅气哦。"

    show rs_image_F89A04A6DC494AEF9DDB0A6A99F3D02A as tag_81DF0CF91B224EAAA16B0366711BA01F zorder zorder_tag_81DF0CF91B224EAAA16B0366711BA01F onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "是、是吗。我只有那个时候才能出场，感情投入过多了。"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_81DF0CF91B224EAAA16B0366711BA01F
    hide tag_073D4E2B5E224963B025F95C92ED797A
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 200
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C9A169B5FECE487BAE71B3017B79B0B4 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_58CAC53C853A4ECC97CAB3038D1CAAF0 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "让我演陨石实在是太过分了——！为什么打得那么重！！"

    show rs_image_3F5AF2DAC6F94773B04A709D2558F647 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "忍！！！剧本上写了下手轻点了！！"

    show rs_image_2D2761902CAE44EC807DF631A55BE304 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "其实轻了，只是有些估计错误，所以就变成那样了，抱歉。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_073D4E2B5E224963B025F95C92ED797A = 200
    show rs_image_1CDBF9A281F54418A7363E36408C7DD5 as tag_073D4E2B5E224963B025F95C92ED797A at right_top zorder zorder_tag_073D4E2B5E224963B025F95C92ED797A onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "没什么不好嘛，很感人，而且友君也很好笑。"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_06FD3372A1FE4B4FB675F0FFE43B7CB3 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "说起来，忍同学～是不是对剧本投入太多感情了呢？"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_073D4E2B5E224963B025F95C92ED797A
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_7D2835EC10DE4438B9BBE9F8CE5454F5 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at left_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔、嗯……好不容易有那种体验，至少能在现实中稍微用一下……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_17B63D85141F4D91A903BDDBAA7EA884 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "说是那么说可……最后太悲情了！为什么就不能是Happy Ending呢。"

    show rs_image_AA6ADB52F38D4A07AB46270DE3FB9136 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "不，其实是这种剧情更容易吸引观众……"

    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_FF491F5A6126442898B268B47C1758E6 as tag_A77E36FB70FF4F60B12060B2747E46D1 at right_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "作为原型的两位要是看到这场演出会不会生气呐～"

    show rs_image_0C866D450EF342189ED1497939E81294 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯……那样的话又要去道歉了……"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.7

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 200
    show rs_image_4935FCE98EC6419797D5AA3F5048A873 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at left_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_222ACAAE90984841BA57DEA7ED06FB8F

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "……嗯？"
    show rs_image_ACA8F5A4D2D2420B8A44020F7AFB23F0 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "什么啊，这张纸，\n“给写出这个剧本的人”……？"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 200
    show rs_image_61DF088BB68345749E26C196F82492B4 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at right_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "也就是给绫濑的。"
    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_602B12F1C445477F861182BD846DB0BD as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "粉丝来信哦～！"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 200
    show rs_image_1382C936693A4354B456F9C02B592547 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "欸？就那种演出……？\n"
    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    show rs_image_AA6ADB52F38D4A07AB46270DE3FB9136 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    extend "……{w=0.9}{nw}"
    show rs_image_57981D44BEC64E6E999A769D75A0EC1A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "这是……"
    show rs_image_2D2761902CAE44EC807DF631A55BE304 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "慎太郎、一之濑君。"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 200
    show rs_image_12E394DC341C4685AB17E83FEED856C9 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯？"

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 200
    show rs_image_A20D31D533CF44CDA4A7F67CEC353CDE as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "什么？"

    window hide

    show rs_image_E683F1ECE3314055A6535AFF3A0F039A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.7

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.4

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "看样子没必要道歉了。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "也就是说……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "这是……"

    show rs_image_FFF48C5CEE674CE0B2C0548153234BA2 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_E081FEE75EE3497E8DAFEBD9F1C48BA4 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_4A9AC5BBBA6D44F5B5DCB7EEF0B9EAB6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.4

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嗯，就是那样。"

    window hide

    pause 0.8

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_07BACEE3C1C64F1DAD61CD240DF0C2E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 = 200
    $ zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD = 200
    show rs_image_F4C733D956094DDB90D3AE4E82A63BAA as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 at left_top zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    show rs_image_4B64C623E7064EDA84B3D0A997F99470 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD at right_top zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.4

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "呜～真是很棒的剧情啊，守……"

    rs_character_57471360F48A413AB843A4E46D8C5541 "太、太大惊小怪了，你到底要多么感性？\n"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_3E667A569CC54E86B612A79E21C9EC9E as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "还是说只是个笨蛋？"

    if sys_music2_current_file != "sound/Effect Sound/Stupid 1.ogg":
        play music2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_B7004DEEA80C41CC8F336C87E7A09F2E as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "不用你管——！（抽泣）……你才是从头到尾都很高兴不是嘛。"

    show rs_image_309B0F3F61544BA188E845B4B474794B as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_57471360F48A413AB843A4E46D8C5541 "那、那是……嘛，能被那么理解确实很高兴……"

    show rs_image_BEE780ABA64C4D7ABB8972D17BDCBFAB as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "理解？嗯？怎么回事？"

    show rs_image_C9B3C83238F74DF0BD84400376826860 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "啊，对了，还没给夕阳介绍过呐。"

    show rs_image_07F2639BB0524AEBB4F93F1989365243 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "（抽泣）……对，就算立场不同但只要心灵相通，也能在一起呐。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_15C5A93E72CC49F7B52D2031A6D69DEE as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "好！！我有一天也一定要和那家伙！"

    show rs_image_AAAEA4F6F87F4C9E9D2EA46DBB711AED as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "说得好，夕阳，到底要止步不前维持单相思到什么时候。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_3E667A569CC54E86B612A79E21C9EC9E as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "早点交往，一起来双重约会。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_18B1A67E5BA849D9AF4BB1601B6AF6CC as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "诶！？就是说，你是，有恋人的！？"

    show rs_image_34FE71D3EB71405D8A5DEB69161B5815 as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_57471360F48A413AB843A4E46D8C5541 "之前不是说过了嘛，\n你身边就有{color=#008080}比你谈着更特殊的恋爱{/color}的人哦。{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_08A60BE855F842738514E4884FEB1529 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_F4C733D956094DDB90D3AE4E82A63BAA as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_57471360F48A413AB843A4E46D8C5541 "……以后会介绍给你的。"

    show rs_image_6445A86DD28745F0AD0938A8193610F2 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔、唔唔……那、那个啊，{w}果然有恋人就会很高兴吗？"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_3E667A569CC54E86B612A79E21C9EC9E as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "嗯，当然很高兴。早上也是，白天也是，{w}\n{w=0.3}{nw}"
    if sys_effect2_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Waoh 1.ogg"

    show rs_image_270A2307D9DC40C0AD9EA0A56F2A07BF as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "晚上……会更加高兴♪"

    if sys_effect2_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_7D2BA1257986495BA7EE1CE21AF449F6 as tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD zorder zorder_tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔——！！好羡慕——！！！我以后也要……一定会！！！"

    show rs_image_3E667A569CC54E86B612A79E21C9EC9E as tag_FD7EEC63649F4ABB88B3E11A041AF5A6 zorder zorder_tag_FD7EEC63649F4ABB88B3E11A041AF5A6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_57471360F48A413AB843A4E46D8C5541 "哈哈，加油，官能的魔术师君♪"

    window hide

    pause 0.3

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_B63B16D4A65544238C7A16A52E11B6FA as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D3FB05FA0D1C41DFBA547183F8C41662

    window show

    pause 0.4

    rs_character_57471360F48A413AB843A4E46D8C5541 "（我也从你们充满着正义感的心情里获得动力了哦，谢谢你们！）"

    rs_character_57471360F48A413AB843A4E46D8C5541 "（果然，"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "做了好事心情也会好呐！）"

    window hide

    pause 1

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_A45595F91B474CC9A0810932B96DD8EC
    hide tag_E99970E1386B453DAF81C3AE2C72BE8E
    hide tag_FD7EEC63649F4ABB88B3E11A041AF5A6
    hide tag_C0A07765EA8A4A8D8CCADC4F9E5B43AD
    with rs_effect_B6D2CFDC1CB5407EACD7FBC1D100D198

    call scb_flag_title_end(3, _("「正义的教训」")) from _call_scb_flag_title_end_15

    if judge_lm_condition([]):
        jump block_000041C7

    return

label block_000041C7:
    # Node: 000041C7 (Phase: 0)
    $ C3S2Phase = 0
    if Chapter <> 3:
        $ del C3S2Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_000041CA
    if judge_lm_condition([]):
        jump block_000041C6

    return

label block_000041CA:
    # Node: 000041CA ()

    return

label block_000041C6:
    # Node: 000041C6 (FINISH)
    $ C3S2 = True
    $ TalkShinobuF2After = True
    if ((C1SG2 == False) or (C2SG2 == False)) and (C3S1 == True) and (C3S3 == True):
        $ SYSBreakCurrentChapter = True

    if judge_lm_condition([]):
        jump block_000041CB

    return

label block_000041CB:
    # Node: 000041CB (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_18

    if judge_lm_condition([]):
        jump block_000041C5

    return

label block_000041C5:
    # Node: 000041C5 (FLAG FINISH)
    $ set_window("(標準)")
    pause 1.5

    if sys_music2_current_file != "sound/BGM/Flag finished.ogg":
        play music2 "sound/BGM/Flag finished.ogg" noloop
        $ sys_music2_current_file = "sound/BGM/Flag finished.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『事件{/color}{color=#0000FF}“正义的教训”{/color}{color=#0080FF}成功结束。』{/color}"

    window hide


    if judge_lm_condition([{ "scope": 0, "content": "VarExists(\"SYSBreakCurrentChapter\") == True" }]):
        jump block_000041CA
    if judge_lm_condition([]):
        jump block_000041E1

    return

label block_000041E1:
    # Node: 000041E1 (RESET)
    pause 4

    if sys_music2_current_file != "sound/Effect Sound/Class bell 1.ogg":
        play music2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_music2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_89A4DFB7FA4E44A4B67B5A6F55BE2CDA

    pause 1.5


    if judge_lm_condition([]):
        jump block_000041CA

    return

