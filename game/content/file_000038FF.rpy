# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 000038FF (FLAG: 尋求刺激-解)

label block_00003900:
    # Node: 00003900 ()

    if judge_lm_condition([]):
        jump block_00003901

    return

label block_00003901:
    # Node: 00003901 (Phase: 99)
    if Not(VarExists("C1S3Phase")):
        $ C1S3Phase = 0
    $ C1S3Phase = 99

    if judge_lm_condition([]):
        jump block_0000397D

    return

label block_0000397D:
    # Node: 0000397D (F3 START)
    call scb_flag_title(1, _("「寻求刺激·解」")) from _call_scb_flag_title_8

    if judge_lm_condition([]):
        jump block_00003902

    return

label block_00003902:
    # Node: 00003902 (尋求刺激-解)
    if sys_effect_current_file != "sound/Effect Sound/Attention 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attention 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attention 1.ogg"

    pause 0.5

    window show

    pause 0.3

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『本故事包含大量的那种剧情\n和见光死的梗（无车），\n请注意莫要翻车。』{/color}"

    pause 0.3

    window hide

    pause 1.5

    $ set_window("イベントモード")
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4647E66D4861417FB077A035A142C3DA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_B8418F379EFF48E39A2ABA6AFFA9DE51

    if sys_music_current_file != "sound/Effect Sound/Tick tock 1.ogg":
        play music "sound/Effect Sound/Tick tock 1.ogg" loop
        $ sys_music_current_file = "sound/Effect Sound/Tick tock 1.ogg"

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open window 1.ogg"

    show rs_image_4647E66D4861417FB077A035A142C3DA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.4

    window show

    rs_character_D9C0860668FF43478EC0A1AA6DC14569 "欢迎光临～"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_0F46590E67454A75B03975CF59479626 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "～♪"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Paper 1.ogg"

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    pause 1.5

    if sys_effect2_current_file != "sound/Effect Sound/Open window 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Open window 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Open window 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4647E66D4861417FB077A035A142C3DA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_222FAD08179342858A781E0AC89B59C1

    pause 0.3

    rs_character_D9C0860668FF43478EC0A1AA6DC14569 "欢迎光临～"

    if sys_effect_current_file != "sound/Effect Sound/Walk 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_E01C5428E6854C2CB75FE50409B66A56 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "～♪"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    pause 0.5

    if sys_effect2_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Paper 1.ogg"

    pause 0.5

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    pause 1

    window hide

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4647E66D4861417FB077A035A142C3DA as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5B01D199AADA45BA90961FBE87B54477

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_8CE08F208261448AB0AB50BEE127AB04 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DC5C15404DD64F10A204D7B27BE6A06D as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    if sys_music_current_file != "sound/Effect Sound/Ding 1.ogg":
        play music "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_music_current_file = "sound/Effect Sound/Ding 1.ogg"

    rs_character_6E72D7A6692D4D3C87490600E5B2F5CC "……呼。"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_81339CBB1684406EB266897AD5F0330B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哇！？白痴呆毛！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8DB9EBBA116648CAAA85C0A0F67B04D2 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦！猫君！！完全没注意到呐——"

    if sys_music_current_file != "sound/BGM/Something will happen.ogg":
        play music "sound/BGM/Something will happen.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something will happen.ogg"

    show rs_image_00D0008B11054042A14DAD5B35850FA9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈哈，我也是我也是。{w}总之惯例地……"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    # Gallery unlock: images/CG/Pluck hair/Pluck hair 2.png
    $ zorder_rs_image_DE8A835C2AC6467EB4456D8DEFA396B3 = -100
    show rs_image_DE8A835C2AC6467EB4456D8DEFA396B3 as rs_image_DE8A835C2AC6467EB4456D8DEFA396B3 zorder zorder_rs_image_DE8A835C2AC6467EB4456D8DEFA396B3 onlayer master
    hide rs_image_DE8A835C2AC6467EB4456D8DEFA396B3

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_DE8A835C2AC6467EB4456D8DEFA396B3 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好呀～"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，嗯，好。"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那个，不要每次都这样了！"

    show rs_image_E01C5428E6854C2CB75FE50409B66A56 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "有何不可有何不可！不就是个肌肤相亲么♪"

    show rs_image_C0489618AF3A47C089B8F4BA43A59A66 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "对了你在看什么书？\n"
    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_81339CBB1684406EB266897AD5F0330B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "噫！！{color=#3A00C4}同{/color}……果真你也是那一边儿的么……"

    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "猫君呐～？"

    if sys_effect_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_39A751328FDE46FAB3026BEC1F2E6B1C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哦！这可真是一对不错的胸啊♪真棒啊～真棒呐～"

    show rs_image_375D6778444E478BBE6E5FCB29DBAEE8 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "诶，你啊，女人也行么？"

    show rs_image_11E9CB4CF92548E88CF101664A977D06 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！我所有都喜欢哦！\n{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    extend "只要舒服的话怎么都可以哦。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_0098B8AFE80F44A6AACB698DF38498AC as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "你……超乎想象得下流。"

    show rs_image_8CE08F208261448AB0AB50BEE127AB04 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "与性别无关，人是要看内在的。"

    show rs_image_093624408E4A49609F348CA15F58D0F1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "那，你所谓的“内在”是？"

    if sys_effect_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    show rs_image_11E9CB4CF92548E88CF101664A977D06 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_3CD1D1BAAA614EC5B716922FC26E97B9

    show rs_image_11E9CB4CF92548E88CF101664A977D06 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{size=32}只要舒服怎么都行！{/size}"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_1209D298FCAF4E62993FA6F9C54C9FCE as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "碧池太郎。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 3.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_D268FC41B6614D8EAEFECC7472B34419 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊——开玩笑的！说笑的～！"

    show rs_image_A55DE444AA7F4312A71EDB37C476BD22 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我要是也能像你这么单纯就好了呢……"

    show rs_image_C0489618AF3A47C089B8F4BA43A59A66 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嘛咋都行了，怎样，找到了没？今晚的点心？"

    show rs_image_8CE08F208261448AB0AB50BEE127AB04 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！已经全都记住了！！要早点回去嗡嗡嗡哦～"

    show rs_image_0098B8AFE80F44A6AACB698DF38498AC as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嗡嗡嗡？"

    show rs_image_8F24F3F0856A427BBFD119767177B781 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼呼。我可是活在未来的男人。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "一切都交给机器。看，就是用这个。"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Look! 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_8210A3BC79A247A5AAEF4BB7CC5EF5C9 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.5

    window show

    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "出、出现了！传说中的电动按摩器！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "传、传说中？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我们年级可都知道的！你整天拿着这么个玩意儿上学。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸～我这么有名啊。哈哈，有些不好意思呐……"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不，给我知耻一些。不过我还是第一次看到实物呢。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "嘛～确实，AV这东西用起来效果也很不错。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不过男性真的能用么……？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸那是什么我也要看！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "电摩的乐趣在于不用自己动手，\n被机械强制交代出来的感觉可是无法忍耐的哦～"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦……{w=0.5}……呐，开个电源试试。"
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_65D8765D75A74E43AE3A0FB9E9D2BBFB as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没有插座的话用不了的～\n再说了，在公共场合这么做有点……"

    show rs_image_375D6778444E478BBE6E5FCB29DBAEE8 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊，这样，嗯……\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_338FF3739E7848C2944283BC7DDB8ED9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "嗯，就这么干！！白痴呆毛，过来！"

    show rs_image_8DB9EBBA116648CAAA85C0A0F67B04D2 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "诶！？{w}等、等等～！"

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    stop music fadeout 0.5
    $ sys_music_current_file = ""

    pause 1.5

    window hide

    if sys_music_current_file != "sound/BGM/Flurry 1.ogg":
        play music "sound/BGM/Flurry 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_092C46B7A72E4AFEB49017870F0978E6 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 0.5

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 0
    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "原来是想到卡拉OK了呐，猫君。"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_E01C5428E6854C2CB75FE50409B66A56 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "反正这边也有插座，开开又咋了嘛！{w}来来，请，请♪"

    show rs_image_0F46590E67454A75B03975CF59479626 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼～♪那就开始～！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_8210A3BC79A247A5AAEF4BB7CC5EF5C9 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "见识振动的美妙之处！！{w}开关・开！！"

    if sys_effect2_current_file != "sound/Effect Sound/Switch 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Switch 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Switch 1.ogg"

    show rs_image_5B4DF841D0A4426483B871872CD92671 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    show rs_image_5B4DF841D0A4426483B871872CD92671 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    if sys_effect3_current_file != "sound/Effect Sound/Vibration 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Vibration 2.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Vibration 2.ogg"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}wwwwwwwwwwwwww！{/size}"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦哦哦哦！\n声音还挺大的嘛，过来这边儿真是对了。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不过啊，振动真强。……呜哇！太强了根本不敢动。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是不～来，猫君也拿着。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "请务必试试哦，正确的用法。"

    window hide

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    # Gallery unlock: images/CG/Seeking-for-stimulation-finally/Seeking-for-stimulation-finally 1.png
    $ zorder_rs_image_18084E9C14F5421BBBB3CA4F07A82DC8 = -100
    show rs_image_18084E9C14F5421BBBB3CA4F07A82DC8 as rs_image_18084E9C14F5421BBBB3CA4F07A82DC8 zorder zorder_rs_image_18084E9C14F5421BBBB3CA4F07A82DC8 onlayer master
    hide rs_image_18084E9C14F5421BBBB3CA4F07A82DC8

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_18084E9C14F5421BBBB3CA4F07A82DC8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_7F932474FD4A465598E0CFBE32B9CD09

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "真、真的…？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "之前不是一直都有兴趣嘛～？\n来，新世界的大门就要在眼前！！快！快！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔、哦。不、不疼？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不会痛的！不过，也许对太敏感的人\n刺激有些强过头了也说不定，至少我这么觉得。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "来来来，快放到那里去～"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔……呃……嗯……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "还有十厘米！五厘米！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈……哈……！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "只剩一点！！"

    stop effect3 fadeout 0.1
    $ sys_effect3_current_file = ""

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……果然还是算了。"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    window show

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_092C46B7A72E4AFEB49017870F0978E6 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    show rs_image_342469B7E318428586C1F76696312BCB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{size=28}……哈啊！？！？{/size}"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5BA6C9344B034374A99A57D20E3BC928 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我还没变态到在别人面前干好么！！"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_DC5C15404DD64F10A204D7B27BE6A06D as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_29378D72FCF54EF98AE11A4369F35631 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "综上，白痴呆毛酱☆今天，借我用用呗☆？"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不、不行不行不行！！\n我今晚也绝对不能缺了这孩子啊！"

    show rs_image_65D8765D75A74E43AE3A0FB9E9D2BBFB as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "没什么不好嘛～传闻中你不是有两根的嘛？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "只是一天一根不在也没事儿嘛！\n拜托了！就是这样！！"

    show rs_image_0ED26038CAA342189E25F288497A2342 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "唔……好。只有一天哦。作为交换，不要弄坏了～"

    if sys_effect_current_file != "sound/Effect Sound/As you wish 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_00D0008B11054042A14DAD5B35850FA9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "好咧～～！！谢了，谢了啊白痴呆毛！！\n天使！你真是天使！！"

    show rs_image_8F24F3F0856A427BBFD119767177B781 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呵呵～那刚才骂人碧池太郎的话可以收回了吧！"

    show rs_image_9248578025B04D709276B881AD82AAC4 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "没问题没问题！那就让我好好试试～♪"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    window hide

    pause 0.8

    if sys_effect3_current_file != "sound/Effect Sound/Vibration 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Vibration 2.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Vibration 2.ogg"

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}wwwwwwwwwwww！！{/size}"

    window hide

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_03F9D423C98243D893E52202A359B740 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_4C49CB282F514E7FB8F3E76FFD229A96 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "什么声音……"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window hide

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_97FB2B4DF012465D98F4737FED39C2E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈、哈……唔！"

    window hide

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    if sys_effect_current_file != "sound/Effect Sound/Waoh 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Waoh 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Waoh 1.ogg"

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "这……不妙……？！\n腰、腰要震碎了！"
    if sys_effect2_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    extend "{color=#FF80C0}啊……不好……！{/color}"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window hide

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_03F9D423C98243D893E52202A359B740 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    window show

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_E47A96C261964823A2932F1C8BFCF258 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "好烦啊！那人又想做什么。"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window hide

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_97FB2B4DF012465D98F4737FED39C2E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{color=#FF80C0}不……不行……继续的话……！{/color}"

    if sys_effect_current_file != "sound/Effect Sound/Open door 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Open door 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Open door 1.ogg"

    show rs_image_97FB2B4DF012465D98F4737FED39C2E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_5EB601DCA8974E1A8C893840BF4F8D12

    if sys_effect2_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dash 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_BA8F587A9CFC4AC38660F10FCCA9BD0C as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at center_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "哥哥烦死了！在做……"
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 = 300
    show rs_image_B18CEC27CB7E4BE28F0FEA52EFCE8F50 as tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 at right_top zorder zorder_tag_8E7A1CAFAF9A498EA9AED7966C7C96F6 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "！！？"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_D6F534AD425748419CA9A9C429E16985 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Ding 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Ding 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Ding 2.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_8E7A1CAFAF9A498EA9AED7966C7C96F6
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    stop music fadeout 0.6
    $ sys_music_current_file = ""

    pause 2.5

    stop effect fadeout 0.6
    $ sys_effect_current_file = ""

    pause 1.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_7F267802C71245A99F2D8889E4793792 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    if sys_music_current_file != "sound/BGM/Daily 2.ogg":
        play music "sound/BGM/Daily 2.ogg" loop
        $ sys_music_current_file = "sound/BGM/Daily 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_3F533DA3CF494DEBA1146743852331E9 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window show

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这样啊～没能做到最后，真遗憾。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "果然那个还是太明显了。家里有人的话就不能用了。"

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_39191B79962D46378B6EE9303930F2C8 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_093624408E4A49609F348CA15F58D0F1 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不过啊，真的……感觉超赞啊。那真的会中毒呐。"

    show rs_image_28A01C08CFC245F2B5B451B8E36AF5EB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "猫君，眼光不错嘛。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不会再“自力更生”了对不？反正也只会减少手腕的使用寿命。"

    show rs_image_3F382299D2C54FA49DC81E2AA4CDAC91 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "是啊，我以后也试着用用道具好了。"

    show rs_image_D3A9686A301549F6B739A77497C158B9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "是～呐～是呐！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，只是听听就觉得终于喜欢上震动了呐。\n好的，我也要快点回去嗡嗡一下了！"

    show rs_image_375D6778444E478BBE6E5FCB29DBAEE8 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "欸，你昨天没做？家里不是还有一根来着么？"

    show rs_image_952D06E912C54776B1C4F5BB577DFB95 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那个。现在故障了～{w}\n所以昨天只好找{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Notice 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Notice 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Notice 1.ogg"

    extend "{color=#00FFFF}咕噜咕噜君{/color}将就了一下。"

    show rs_image_A55DE444AA7F4312A71EDB37C476BD22 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{color=#FFFFFF}咕{/color}……？那又是什么，听着像什么派系似的。{w}\n那也是很不错的东西？"

    show rs_image_8CE08F208261448AB0AB50BEE127AB04 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嘛，肯定不如电摩好。不过也是很不错的实力派哦～"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C745E931F5C24881B3C5FC0BF517931B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "老、老司机教教我！！\n我可从昨天开始就一直是剑拔弩张的状态的！"

    if sys_effect_current_file != "sound/Effect Sound/Surprise 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5BA6C9344B034374A99A57D20E3BC928 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "但事已至此，就想干脆不用手了！"

    show rs_image_28A01C08CFC245F2B5B451B8E36AF5EB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "好～呀……作为顺利了解了电摩好处的同伴，\n这次就破例教教你！"

    show rs_image_99B6023D52BE4DE3B83DA6CA21A146C8 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "放学后……说起来猫君有社团活动呐，\n那就晚上七点在东边的公园可以吗？"

    show rs_image_375D6778444E478BBE6E5FCB29DBAEE8 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "公园？要在外面？"

    show rs_image_11E9CB4CF92548E88CF101664A977D06 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "当然了交给我！"

    if sys_effect_current_file != "sound/Effect Sound/God 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/God 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/God 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_81339CBB1684406EB266897AD5F0330B as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_1DEF9484682F4FA3BF644B40652AE3AB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "一定会指引猫君到达快乐的彼岸的，放心即可。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_65D8765D75A74E43AE3A0FB9E9D2BBFB as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦，师父！！拜托了！！"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    stop music fadeout 1
    $ sys_music_current_file = ""

    window hide

    pause 1.5

    if sys_effect3_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F080DC78D9E041C8851F42F8A37F4FC3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 1

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_F7780BBB76424F93AD294371903C514C as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "咕噜咕……是……滑梯！？"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "正是如此！\n这次介绍给三朗前辈的快乐源泉，正是眼前的道具！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不，请别胡闹了师父，会喜欢这种东西的只有小学生。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "话～说～回～来～如果爬上去，脸朝下，\n把{color=#FF80C0}那里紧贴着{/color}滑下去的话……！"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    extend "{size=32}～～～～～～～……{/size}"

    window hide

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F080DC78D9E041C8851F42F8A37F4FC3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_A6B4348D830149E99506A5D175DCF690 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "很、很不错的哦……嘛嘛，就当是上个当去试试！"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_81339CBB1684406EB266897AD5F0330B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哦、哦……脸朝下贴上去……"

    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.3

    window hide

    if sys_music_current_file != "sound/BGM/Flurry 1.ogg":
        play music "sound/BGM/Flurry 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 1.ogg"

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    # Gallery unlock: images/CG/Seeking-for-stimulation-finally/Seeking-for-stimulation-finally 2.png
    $ zorder_rs_image_CCAF353B743A4E13A7A43D3F8AF8D694 = -100
    show rs_image_CCAF353B743A4E13A7A43D3F8AF8D694 as rs_image_CCAF353B743A4E13A7A43D3F8AF8D694 zorder zorder_rs_image_CCAF353B743A4E13A7A43D3F8AF8D694 onlayer master
    hide rs_image_CCAF353B743A4E13A7A43D3F8AF8D694

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_CCAF353B743A4E13A7A43D3F8AF8D694 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_FF4D3C8D6CBC4BA09B73C83E06D18F76

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}～～～～～～～……{/size}"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{color=#FF80C0}啊啊啊啊啊……！！{/color}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不错！？很舒服！？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "正如师父所说非常棒……啊。可是滑梯太短了根本就……"

    if sys_effect3_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Pa 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那就多来几次！！"

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不可气馁！自古有德之人方可力究此致！\n来，快感的门扉，现在即将打开！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈……啊……！再一次！！"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    if sys_effect2_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    # Gallery unlock: images/CG/Seeking-for-stimulation-finally/Seeking-for-stimulation-finally 2.png
    $ zorder_rs_image_CCAF353B743A4E13A7A43D3F8AF8D694 = -100
    show rs_image_CCAF353B743A4E13A7A43D3F8AF8D694 as rs_image_CCAF353B743A4E13A7A43D3F8AF8D694 zorder zorder_rs_image_CCAF353B743A4E13A7A43D3F8AF8D694 onlayer master
    hide rs_image_CCAF353B743A4E13A7A43D3F8AF8D694

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_CCAF353B743A4E13A7A43D3F8AF8D694 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_B9863F4A69BE4E1CBF54DB1F5F378A5D

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{size=32}～～～～～～～……{/size}"

    pause 0.3

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{color=#FF80C0}啊啊啊啊！{/color}"

    if sys_effect2_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "叫得挺不错的嘛！！只要再来一次！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "下次，就是最后的……！"

    window hide

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F080DC78D9E041C8851F42F8A37F4FC3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_40EF2E724ABB420CA128496A39011B0E

    window show

    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_52116B1449D74170802914AF1BEA06D1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_C2EBA78177DC4C19BB09CDE7382841A8 as tag_A469B787E7E7466FA1613F380A4CBF41 at left_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "干什么呢，你们。"

    if sys_effect_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_342469B7E318428586C1F76696312BCB as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_985C4F51753342B8B4DE84538D870AD5 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_6E72D7A6692D4D3C87490600E5B2F5CC "！？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    show rs_image_CAE9E92D7F644421A40585EE4A43F483 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at Transform(xpos=430, yalign=0.0) zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "猫山，在社团活动时老发呆就算了，为什么会和这家伙半夜乱窜啊。"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_376CA53D8BF64CE497CF774B53A38857 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "技、技安！！{color=#008080}又来{/color}打扰我们的好事了！{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Decision 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_F647A346C17043E4AA06DD4621FE0DFF = 400
    show rs_image_328F7611A01F4113B7ED85246E2C68E1 as tag_F647A346C17043E4AA06DD4621FE0DFF at center_bottom zorder zorder_tag_F647A346C17043E4AA06DD4621FE0DFF onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_F647A346C17043E4AA06DD4621FE0DFF
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "\n猫君！！撤退！！先撤退！！"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_C745E931F5C24881B3C5FC0BF517931B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at Transform(xpos=-60, yalign=0.0) zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "师、师父等等……！我、我……只差一点就……！"

    if sys_effect_current_file != "sound/Effect Sound/God 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/God 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/God 1.ogg"

    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_C745E931F5C24881B3C5FC0BF517931B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_2F76ABC32FFF461B9C1A6AA99B10BAAF as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "只有跨越试炼方可更强！！加油！！这里只能暂且忍耐！"

    show rs_image_5BA6C9344B034374A99A57D20E3BC928 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "混、混蛋！！穗海！给我记住！！"

    if sys_effect_current_file != "sound/Effect Sound/Dash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dash 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_DA851BDF3E0F4030931776C0C57D440D

    stop music fadeout 1
    $ sys_music_current_file = ""

    window hide

    pause 0.8

    if sys_effect3_current_file != "sound/Effect Sound/Night insect 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Night insect 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Night insect 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_F080DC78D9E041C8851F42F8A37F4FC3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.4

    window show

    $ zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D = 300
    $ zorder_tag_A469B787E7E7466FA1613F380A4CBF41 = 300
    show rs_image_52116B1449D74170802914AF1BEA06D1 as tag_F533D76D6EDF4AB39ECAAB90D8F4723D at right_top zorder zorder_tag_F533D76D6EDF4AB39ECAAB90D8F4723D onlayer master
    show rs_image_4CBCF132AF8F49E38C726D5800545B50 as tag_A469B787E7E7466FA1613F380A4CBF41 at left_top zorder zorder_tag_A469B787E7E7466FA1613F380A4CBF41 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.3

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "奇怪的一群人。小翼，你怎么看。"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "汪～"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A469B787E7E7466FA1613F380A4CBF41
    hide tag_F533D76D6EDF4AB39ECAAB90D8F4723D
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    window hide

    pause 0.5

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_C6E646A376EB4D6687DFAAD949959131 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    pause 0.4

    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    if sys_music_current_file != "sound/BGM/Something strange 1.ogg":
        play music "sound/BGM/Something strange 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Something strange 1.ogg"

    window show

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_8A80B90628C143D1B3A53C71240BBE2D as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊哈哈，又是没到最后……不要在意。"

    if sys_effect_current_file != "sound/Effect Sound/Frustrated 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Frustrated 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Frustrated 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C745E931F5C24881B3C5FC0BF517931B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "唔、呜呜呜。可是啊，那确实太费事了，\n被打断也是很可能的。"

    show rs_image_A48E3C15AF6146FA91F9AD97CAF30F5C as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不会被别人打扰，不会明明能做却做不了的……\n类似的好选择有么？"

    if sys_effect_current_file != "sound/Effect Sound/God 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/God 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/God 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1DEF9484682F4FA3BF644B40652AE3AB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯～既然如此……"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_8DB9EBBA116648CAAA85C0A0F67B04D2 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊！对了！\n{w=0.5}{nw}"
    if sys_effect_current_file != "sound/Effect Sound/God 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/God 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/God 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1DEF9484682F4FA3BF644B40652AE3AB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    extend "三朗君，你的愿望，或许能实现哦！！"

    show rs_image_65D8765D75A74E43AE3A0FB9E9D2BBFB as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "真的吗，师父！！"

    show rs_image_2F76ABC32FFF461B9C1A6AA99B10BAAF as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "嗯！！本周末就会带你到能实现愿望的地方。"

    show rs_image_5BA6C9344B034374A99A57D20E3BC928 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "只要去了！这次，我也……！"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_943958ACE1594083BA9B66D14E70D431 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……话说啊，这么想做的话，\n不用这样忍着直接在家里做不就好了？"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_AE31149E5F7F4DC79066D77A5F625EC2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不可！！现如今已经知晓了更进一步的快感，\n自然再也无法回到过去了！"

    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5BA6C9344B034374A99A57D20E3BC928 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "师父，请带领我到达快乐的彼岸！！"

    if sys_effect_current_file != "sound/Effect Sound/God 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/God 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/God 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_2F76ABC32FFF461B9C1A6AA99B10BAAF as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "交给老夫！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    window hide

    pause 2

    if sys_effect3_current_file != "sound/Effect Sound/Clamorous 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect3_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_CA940727708D47E681656A6519179F7A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_52D170452B914F45964BC41A297FB8DC

    pause 0.8

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_4FBC7EAAD8924B8F9F4C8AA7F184C12B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    pause 0.4

    window show

    pause 0.3

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "师父！！这种露出度高的地方真令人期待呐！{w}\n那么，所谓的那个在何处呢！？"

    if sys_effect_current_file != "sound/Effect Sound/God 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/God 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/God 1.ogg"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_B05A19575A2A4710BF2D13CC4BBBFB78 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_5B3055FA9C02431C98B0AFFF187DD6BE as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼呼，不用急，不会错过的。"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_450C067FF4354880AB47DDBA92043DAD as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "拜托了！！对青春期来说点到为止就和禁止挊同样残酷啊！"

    show rs_image_5B3055FA9C02431C98B0AFFF187DD6BE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "有道理……"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_8E8244857F1745E2B43802443EDCDE11 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "总之先到泳池里！好了好了猫君，这边哦！"

    show rs_image_8B256A0B92C5469491ED77A36C787C85 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "诶，要下水？我……不会游泳……"

    if sys_effect_current_file != "sound/Effect Sound/God 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/God 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/God 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_5B3055FA9C02431C98B0AFFF187DD6BE as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "这种程度就要放弃……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "你小子，还以为有点毅力的，是我高看了。"

    if sys_effect_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_450C067FF4354880AB47DDBA92043DAD as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "呜呜，明白了！我做！一定会回应师父的期待的！！"

    if sys_effect_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……去了！！"

    show rs_image_CA940727708D47E681656A6519179F7A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    if sys_effect_current_file != "sound/Effect Sound/Dive 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dive 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dive 1.ogg"

    pause 0.4

    rs_character_A82533A004F246E9ABF29675BC420B77 "那边，很危险的，别跳。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_242595F448274BE08CADD1467C9F10E9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_3A2C5578C29A46D498C5C917B2567EB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "抱、抱歉……"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_10E5ED57321C4CE98174684B86DA4E58 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "哈哈～被骂了呐！看，来这边！接下来就由我来带领！"

    show rs_image_27C2722A9AF9404EB32E2F19E4FFB086 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "师、师父真的可以么。再怎么说也太勉强了，\n要是还和之前一样的我可不会满足哦？"

    show rs_image_CAED8D007ADB4080B35E9102A92BE7E6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "没事没事，这次的将会和电摩一般舒服哦。"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_BAFDE86844DA4F7D80E970CE99530F55 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……好，这里！{w}快看！墙壁上有进水孔对不对？"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "确、确实是，哇，水压挺大的。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "到这里还能理解呐。试着活用至今为止的经验自己试试。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……（吞口水）{w}把那里，冲着……"

    window hide

    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_FAE04D9AEB58490C92EEB463378364AF

    pause 0.8

    if sys_music_current_file != "sound/BGM/Flurry 1.ogg":
        play music "sound/BGM/Flurry 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Flurry 1.ogg"

    if sys_effect_current_file != "sound/Effect Sound/Boom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 2.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_EA6D39ADD59940DAA9CC6909087E7935 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_DEF4707300154D00B22225E4F8282BA7

    pause 0.2

    if sys_effect2_current_file != "sound/Effect Sound/Boom 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 2.ogg"

    # Gallery unlock: images/CG/Seeking-for-stimulation-finally/Seeking-for-stimulation-finally 4.png
    $ zorder_rs_image_287157BDD64B4E528AFF869F71BDA5A9 = -100
    show rs_image_287157BDD64B4E528AFF869F71BDA5A9 as rs_image_287157BDD64B4E528AFF869F71BDA5A9 zorder zorder_rs_image_287157BDD64B4E528AFF869F71BDA5A9 onlayer master
    hide rs_image_287157BDD64B4E528AFF869F71BDA5A9

    show rs_image_287157BDD64B4E528AFF869F71BDA5A9 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    pause 0.4

    window show

    pause 0.3

    if sys_effect2_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈哦哦！！？{w}\n厉、厉害！！无意中甚至想要逃开！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼呼呼，这里就不会轻易被别人发现了。这次就好好体验一番！"

    if sys_effect2_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{color=#FF80C0}哈啊、啊啊啊！！{/color}\n"
    if sys_effect_current_file != "sound/Effect Sound/Surprise 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "……嗯？可这里是泳池内啊。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "如果在这里做了，那其他人……"

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "怎、怎么了！快点继续！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "师父，很抱歉……我、我……我……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "行了！！别废话！！既然如此只好强行上了！！"

    if sys_effect_current_file != "sound/Effect Sound/Cut the wind 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide

    pause 0.2

    if sys_effect_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_2EBE16894A8644B99EE70E291DA31DA1 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_DEF4707300154D00B22225E4F8282BA7

    pause 0.2

    if sys_effect2_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Boom 1.ogg"

    # Gallery unlock: images/CG/Seeking-for-stimulation-finally/Seeking-for-stimulation-finally 6.png
    $ zorder_rs_image_68F095DA988D4FBD93381898FF8260F4 = -100
    show rs_image_68F095DA988D4FBD93381898FF8260F4 as rs_image_68F095DA988D4FBD93381898FF8260F4 zorder zorder_rs_image_68F095DA988D4FBD93381898FF8260F4 onlayer master
    hide rs_image_68F095DA988D4FBD93381898FF8260F4

    show rs_image_68F095DA988D4FBD93381898FF8260F4 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_6AF713EEDC664B669DFA76C7954DF0B7

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊呜！！不、不要！！不要推！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "师父快住手！n啊……啊啊要出来了！！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "为了冲刺快乐的终点多少有点牺牲是在所难免的！\n去吧！！"

    if sys_effect_current_file != "sound/Effect Sound/Flee 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=32}不、不行！！！{/size}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呃！？"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_3A2C5578C29A46D498C5C917B2567EB5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 0.6

    stop music fadeout 0.5
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    if sys_effect_current_file != "sound/Effect Sound/Dive 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dive 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dive 1.ogg"

    pause 0.4

    window show

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_242595F448274BE08CADD1467C9F10E9 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "哈……哈……\n"
    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    show rs_image_450C067FF4354880AB47DDBA92043DAD as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "我、我做不到……！！"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_58383924290F4D839989B44C5389C00F as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{w=0.4}猫君这么坚持就只好放弃了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "不过我已经没什么新点子了。\n{w=0.5}{nw}"
    show rs_image_2279C734BC2A40AAB4EECE2B8CDF9EF6 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "所以后面要怎么做，要一起来考虑了。"

    show rs_image_4FEA6F1568C64D2882B9DA14716E7869 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "白痴呆毛……"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.5

    if sys_music_current_file != "sound/BGM/The end of touch.ogg":
        play music "sound/BGM/The end of touch.ogg" loop
        $ sys_music_current_file = "sound/BGM/The end of touch.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_2279C734BC2A40AAB4EECE2B8CDF9EF6 as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_52AC15E153DE4B9F9274366127CFBD0D

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我很喜欢猫君努力的样子哦。\n一定会让一直不懈努力的猫君高兴的。"

    show rs_image_CA662822A7184AD2B572BBCF7BA9CF38 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "至今为止一直在失败，下次一定会成功的！\n不只我一个，而是和猫君合作！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_577B6B1ACE9B48BAAAE5FB9EB32B6984 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "师父……\n"
    show rs_image_9F5B97FCC06442B7A0F5C2891E985C72 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    extend "嗯！我一定会永远忠于师父的！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_5558577FCB4F4A43A84362ED9AD414E8

    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_CBC57413FCC2493CBDBC3CBDAD915207 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_577B6B1ACE9B48BAAAE5FB9EB32B6984 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_2279C734BC2A40AAB4EECE2B8CDF9EF6 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "猫君！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "师父！！"

    window hide

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_716026AC591942AABE5EC2E0AEA78A89 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_4E3CA8A40DAB42339BCDA438574F62BF

    pause 1.4

    stop music fadeout 0.5
    $ sys_music_current_file = ""

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    window show

    rs_character_A82533A004F246E9ABF29675BC420B77 "那边那边，别在泳池内玩不纯同性交往——"

    window hide

    pause 2

    show rs_image_AAFB84FD7F9749899F3613AE8FC5801F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_995A246CCA8349168AE1D97DE29F1026

    pause 0.6

    if sys_effect_current_file != "sound/Effect Sound/God 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/God 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/God 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1DEF9484682F4FA3BF644B40652AE3AB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window show

    if sys_music_current_file != "sound/BGM/Final battle.ogg":
        play music "sound/BGM/Final battle.ogg" loop
        $ sys_music_current_file = "sound/BGM/Final battle.ogg"

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "委身于成人话题，追逐于无上愉悦，这就是，森海教的精髓……\n"
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Stupid 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_81339CBB1684406EB266897AD5F0330B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_952D06E912C54776B1C4F5BB577DFB95 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "呜……咳咳！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "师、师父！怎么了！？身体不……"

    show rs_image_2F76ABC32FFF461B9C1A6AA99B10BAAF as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "猫君，明明你在禁欲，\n作为师父的我要是不做以身作则就说不过去了啊。"

    if sys_effect_current_file != "sound/Effect Sound/Strike 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_952D06E912C54776B1C4F5BB577DFB95 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可、无论如何还是做不到……"

    show rs_image_5BA6C9344B034374A99A57D20E3BC928 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不要说胡话了！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "一直都依赖于强烈刺激的师父，\n比起我禁欲的冲击可要大不知道多少……！"

    show rs_image_1DEF9484682F4FA3BF644B40652AE3AB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呼，偶尔乱来一下也没关系，\n心里有些……这种心情多少年没有过了呐。"

    show rs_image_D2A450B39A1A4C46BBF15CFA6979230F as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊！师、师父！！那边有爬杆！！\n如何，能成为带给我们快乐的道具没错的！！"

    if sys_effect_current_file != "sound/Effect Sound/Attack 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_2F76ABC32FFF461B9C1A6AA99B10BAAF as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "可笑！！那种程度只是小学生罢了……早已落伍了！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "我们追求的是更进一步的刺激。思考思考再思考！{w}\n找到能让我们满足的，打开新世界大门的钥匙……！"

    show rs_image_DD145F71E82D45D8ABD7B31C13B66822 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "如机械般无情而强烈地给予快感的道具……{w}\n比起手还是振动更……比起用嘴……"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "……！！"
    if sys_effect_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_DDDDF17EE72F454EB800117B2622B8DB as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "{size=32}……吸尘器！！{/size}"

    if sys_effect_current_file != "sound/Effect Sound/Eye shine 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Eye shine 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Eye shine 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_86826E9F4C2F4B9D8906A085B9944D8C as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "就是那个！！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_9B79BC7F460B4E06BA4FDB458B5423C1

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_352F0413ECA142A5AF6C4B4881200B55 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_86500D05C8934AE7B4E71CC1D50E5D36 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_86C6DB3C38A946C09D75722DCD2AE27B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "等等等等！！！"

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "在这之上不会放你们不管的！！"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Pa 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_376CA53D8BF64CE497CF774B53A38857 as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AE31149E5F7F4DC79066D77A5F625EC2 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "什么人！？"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_2435C20FAF91447F8FFD9A7E62F34984 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    show rs_image_55AA9D3ECD6A49F888891037C386D65A as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "两位醒醒！继续追求更强的刺激只会更危险的！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "就是那样！人是要从心爱的人那里得到治愈，进一步获得快乐的！！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "只是想着毫无感情的机器追寻什么的，肯定是不对的！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_376CA53D8BF64CE497CF774B53A38857 as tag_ECFB5B509A334A868686B3435242BF90 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5BA6C9344B034374A99A57D20E3BC928 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "混蛋！不要阻碍我们梦想！！"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "比起你们当然是师父说的更对！！"

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_F5A88DE19235425A81D30DF2D7E4C7CD as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "三酱！那样不行的！！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "如果，今后，你喜欢上了什么人，\n你还能把对方当做当做人看待吗？"

    show rs_image_0098B8AFE80F44A6AACB698DF38498AC as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_2435C20FAF91447F8FFD9A7E62F34984 as tag_A77E36FB70FF4F60B12060B2747E46D1 zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "被道具摧毁殆尽的你的心灵，真的不会把人当做道具吗？"

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    show rs_image_DEB70960E8944B33903B14177D8DC211 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at Transform(xpos=-80, yalign=0.0) zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "面对如此悲伤的未来，你们觉得这样真的好吗！"

    show rs_image_1209D298FCAF4E62993FA6F9C54C9FCE as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "可……我……已经明白了，{w}\n比起手，道具更能治愈我的身体……。"

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_8FC7B994836E4084B027C2E8010AD725 as tag_A77E36FB70FF4F60B12060B2747E46D1 at Transform(xpos=430, yalign=0.0) zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "三酱……"

    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect3_current_file != "sound/Effect Sound/Impact 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Impact 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Impact 2.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_1DEF9484682F4FA3BF644B40652AE3AB as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_9EB6D16F01EC4823B16A7F9817B2E3F1

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "森海教的教义！"

    if sys_effect_current_file != "sound/Effect Sound/God 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/God 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/God 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{color=#FF0000}『人心难测因而善变，道具无心始得永恒』{/color}！！"

    show rs_image_F4E69F65605A49BCA7659DDD9B7624D5 as tag_C389451CCE5A4CEAB24DEF9A7C02635D zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "友君……"

    if sys_effect_current_file != "sound/Effect Sound/Shock 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shock 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shock 1.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_DD145F71E82D45D8ABD7B31C13B66822 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    show rs_image_86826E9F4C2F4B9D8906A085B9944D8C as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    rs_character_6E72D7A6692D4D3C87490600E5B2F5CC "我们，将会一冲到底！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Flash 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_158D8E25C4414ECF868A62B83D40B99B as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_70FB35FDEFFD4B18BB947374E9B061CE as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "怎么可能放你们自由！！！"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "一定要阻止你们！！！"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if sys_effect_current_file != "sound/Effect Sound/Impact 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Impact 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_342469B7E318428586C1F76696312BCB as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5BA6C9344B034374A99A57D20E3BC928 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "{size=28}哇！！！{/size}"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "{size=28}一边儿去！！！！{/size}"

    window hide

    if sys_effect_current_file != "sound/Effect Sound/Battle 5.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_4B4EB0D4FDE241748E5136DAFE0D484E as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_8676A882850344248D70E3A3623F329F as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_319DADD51F7C413586B41BFF2D47BF78 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
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

    if sys_effect_current_file != "sound/Effect Sound/Battle 5.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 5.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 5.ogg"

    show rs_image_8CD556F98525469D9B60EF719D590FB8 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 0.7

    if sys_effect2_current_file != "sound/Effect Sound/Battle 4.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Battle 4.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Battle 4.ogg"

    show rs_image_85F7088A138E4CFBB807EF1708A34C58 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 2

    if sys_effect_current_file != "sound/Effect Sound/Battle 6.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Battle 6.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Battle 6.ogg"

    show rs_image_46726D80EC7B4D48AD2EFED4CDD37F1C as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 1.5

    stop music fadeout 1.5
    $ sys_music_current_file = ""

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "唔……为何……"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "你们为什么要做到如此地步……"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_EEDE17A0523340C4B70747B46FC7D04C as tag_ECFB5B509A334A868686B3435242BF90 at right_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_DD145F71E82D45D8ABD7B31C13B66822 as tag_25C83DBF35814073B3DF9FF7BCEF75AC at left_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "是男人大家都明白……"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "那就是，我们正在……"

    if sys_effect_current_file != "sound/Effect Sound/Boom 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Boom 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Boom 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_FA6744B680C1471EA7A25CCABF08CF1D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_342469B7E318428586C1F76696312BCB as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5BA6C9344B034374A99A57D20E3BC928 as tag_25C83DBF35814073B3DF9FF7BCEF75AC zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    show rs_image_E548BB1B00F44A74AC84AD6D6E56E79B as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_6E72D7A6692D4D3C87490600E5B2F5CC "{size=32}禁欲啊！！！{/size}"

    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D = 300
    $ zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 = 300
    show rs_image_9C9BE421F7E44A6E9376D93AB2B16371 as tag_C389451CCE5A4CEAB24DEF9A7C02635D at right_top zorder zorder_tag_C389451CCE5A4CEAB24DEF9A7C02635D onlayer master
    show rs_image_ECBA0CF7876045D4AE8665A90CDBF4B6 as tag_A77E36FB70FF4F60B12060B2747E46D1 at left_top zorder zorder_tag_A77E36FB70FF4F60B12060B2747E46D1 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "……这下赢不了了啊。"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "我们已经无可奈何……只能交给他们两位了。"

    if sys_effect_current_file != "sound/Effect Sound/Fall down 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Fall down 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Fall down 1.ogg"

    window hide

    hide tag_A77E36FB70FF4F60B12060B2747E46D1
    hide tag_C389451CCE5A4CEAB24DEF9A7C02635D
    with rs_effect_B69EB6ADE2444C579F00655EAB4DA398

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 2

    if sys_effect2_current_file != "sound/Effect Sound/Class bell 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Class bell 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Class bell 1.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_4C71379AA46D4F159457BCFC688DAA5B as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_EB196AC2DFAF48139C3B5EFA0E52D271

    pause 1.5

    show rs_image_BD4CC76442FF4F6D834FAEC84EA37886 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 1

    show rs_image_ACAD2F42E01A4E09BF4171AA359A9577 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_C6D091EC70524F8D9DD215C9591866E0

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_ECFB5B509A334A868686B3435242BF90 = 300
    show rs_image_CC130F44963D4D48998ABB3BDE7E7BBE as tag_ECFB5B509A334A868686B3435242BF90 at center_top zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊！！"

    window hide

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_9C551C4C1CCA4C6FAF29D7A15E237645 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_4D65017A9CA34C6DA13680DEAE104604

    window show

    if sys_effect_current_file != "sound/Effect Sound/Inspiration 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC = 300
    show rs_image_81339CBB1684406EB266897AD5F0330B as tag_25C83DBF35814073B3DF9FF7BCEF75AC at center_top zorder zorder_tag_25C83DBF35814073B3DF9FF7BCEF75AC onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "咦！？"

    window hide

    pause 0.5

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_25C83DBF35814073B3DF9FF7BCEF75AC
    with rs_effect_845492A87CCD4D7690839A0715D9C7C1

    pause 2

    if sys_effect3_current_file != "sound/Effect Sound/Crow 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Crow 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Crow 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 0
    show rs_image_A6EB165FEA4F43D98FA0D7F5088E39A4 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_top zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 1.7

    if sys_music_current_file != "sound/BGM/Guitar 1.ogg":
        play music "sound/BGM/Guitar 1.ogg" loop
        $ sys_music_current_file = "sound/BGM/Guitar 1.ogg"

    show rs_image_1C0C4120492547BCA9CB3657FA718354 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_338B12F993214B9CA45CE53965EE33E0

    pause 0.4

    window show

    pause 0.3

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……{w}这种事，不要继续了。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "是啊，肯定错了。"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "合作很短不过，我很高兴哦，猫君。"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我也是，谢谢给我如此宝贵的体验。"

    window hide

    pause 0.5

    show rs_image_30C1CE12A1AA4F868F908494973F3622 as tag_3C0D2D9BB95B42AAA768FE8D105219CB zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_1445BCCB339E41F196B5E8B4A0176595

    pause 0.3

    if sys_effect3_current_file != "sound/Effect Sound/Ding 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Ding 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Ding 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_12F01B9753A54FD2BD71827106B781A3 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_3A5CCA7A88F54C8F83FC86A3A7514EF1 "呜……"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{nw}"
    if sys_effect_current_file != "sound/Effect Sound/Crow 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Crow 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Crow 2.ogg"

    extend "笨蛋——\n"
    if sys_effect2_current_file != "sound/Effect Sound/Crow 2.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Crow 2.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Crow 2.ogg"

    extend "笨蛋——"

    stop effect3 fadeout 0.5
    $ sys_effect3_current_file = ""

    window hide

    pause 1

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    # Gallery unlock: images/CG/Seeking-for-stimulation-finally/Seeking-for-stimulation-finally 7.png
    $ zorder_rs_image_85CAF3695FEF4F89962FCAB11752108F = -100
    show rs_image_85CAF3695FEF4F89962FCAB11752108F as rs_image_85CAF3695FEF4F89962FCAB11752108F zorder zorder_rs_image_85CAF3695FEF4F89962FCAB11752108F onlayer master
    hide rs_image_85CAF3695FEF4F89962FCAB11752108F

    # Previously Mr. Kiriya show CG behind end image to unlock gallery, so I think I should keep zorder change
    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0

    call scb_flag_title_end(1, _("「寻求刺激·解」")) from _call_scb_flag_title_end_10

    if judge_lm_condition([]):
        jump block_00003905

    return

label block_00003905:
    # Node: 00003905 (Phase: 0)
    $ C1S3Phase = 0
    if Chapter <> 1:
        $ del C1S3Phase

    if judge_lm_condition([{ "scope": 0, "content": "SYSTheaterState > 0" }]):
        jump block_00003906
    if judge_lm_condition([]):
        jump block_00003903

    return

label block_00003906:
    # Node: 00003906 ()

    return

label block_00003903:
    # Node: 00003903 (FINISH)
    $ C1S3 = True
    $ TalkShintaroF3After = True

    if judge_lm_condition([]):
        jump block_0000391E

    return

label block_0000391E:
    # Node: 0000391E (SYSTEM UPDATE)
    call block_000038EF from _call_block_000038EF_11

    if judge_lm_condition([]):
        jump block_00003906

    return

