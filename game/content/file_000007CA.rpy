# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 000007CA (野球拳)

label block_000007CB:
    # Node: 000007CB ()

    if judge_lm_condition([]):
        jump block_00004259

    return

label block_00004259:
    # Node: 00004259 (Disable save)

    if judge_lm_condition([]):
        jump block_00003B52

    return

label block_00003B52:
    # Node: 00003B52 (PREPARE)
    $ YKKAllyLife = 3
    $ YKKEnemyLife = 3
    $ YKKIsWinner = False
    $ YKKEnemyChoice = 0
    $ YKKSkipCreateCG = False
    if Not(VarExists("YKKMustWin")):
        $ YKKMustWin = False

    if judge_lm_condition([]):
        jump block_00003B54

    return

label block_00003B54:
    # Node: 00003B54 (UPDATE)
    if YKKAllyLife == 0:
        $ YKKIsWinner = False
    elif YKKEnemyLife == 0:
        $ YKKIsWinner = True
    else:
        $ renpy.hide("AllyLifePoint")
        $ renpy.hide("EnemyLifePoint")
        $ renpy.show(YKKAllyLifePoint[3 - YKKAllyLife], at_list=[Transform(xpos=0, ypos=300)], what=renpy.easy.displayable(YKKAllyLifePoint[3 - YKKAllyLife]), tag="AllyLifePoint", zorder=300)
        $ renpy.show(YKKEnemyLifePoint[3 - YKKEnemyLife], at_list=[Transform(xpos=0, ypos=0)], what=renpy.easy.displayable(YKKEnemyLifePoint[3 - YKKEnemyLife]), tag="EnemyLifePoint", zorder=300)
        if YKKSkipCreateCG == True:
            $ YKKSkipCreateCG = False
        else:
            # Gallery support
            $ renpy.show(YKKCGList[3 - YKKEnemyLife], at_list=[Transform(xpos=0, ypos=0)], what=renpy.easy.displayable(YKKCGList[3 - YKKEnemyLife]), tag=YKKCGList[3 - YKKEnemyLife], zorder=-100)
            $ renpy.hide(YKKCGList[3 - YKKEnemyLife])

            $ renpy.show(YKKCGList[3 - YKKEnemyLife], at_list=[Transform(xpos=0, ypos=0)], what=renpy.easy.displayable(YKKCGList[3 - YKKEnemyLife]), tag="CG" |str_combine| YKKEnemyLife, zorder=YKKEnemyLife * 10)
        if YKKEnemyLife == 3:
            hide CG1
            hide CG2
            with rs_effect_CAE7E1A8F1B9452F9A07D2E1DAAE9E40
        elif YKKEnemyLife == 2:
            hide CG1
            hide CG3
            with rs_effect_CAE7E1A8F1B9452F9A07D2E1DAAE9E40
        elif YKKEnemyLife == 1:
            hide CG2
            hide CG3
            with rs_effect_CAE7E1A8F1B9452F9A07D2E1DAAE9E40
        $ YKKEnemyChoice = Random(3)

    if judge_lm_condition([{ "scope": 0, "content": "YKKAllyLife == 0" },{ "scope": 0, "content": "YKKEnemyLife == 0" }]):
        jump block_00003B57
    if judge_lm_condition([]):
        jump block_00003B59

    return

label block_00003B57:
    # Node: 00003B57 (CLEAR)
    $ del YKKAllyLife
    $ del YKKEnemyLife
    $ del YKKEnemyChoice
    $ del YKKSkipCreateCG

    hide CG1
    hide CG2
    hide CG3
    hide tag_445345A84BCD459E8C2AC2BA7651355B
    hide tag_93E1ED3B9EFB461486972450D09B1393
    hide tag_98EEC70DEB344EA5BDB430BB03A0BBE7
    hide AllyLifePoint
    hide EnemyLifePoint

    if judge_lm_condition([]):
        jump block_0000425A

    return

label block_0000425A:
    # Node: 0000425A (Enable save)

    if judge_lm_condition([]):
        jump block_00003B56

    return

label block_00003B56:
    # Node: 00003B56 ()

    return

label block_00003B59:
    # Node: 00003B59 (Hint)
    hide tag_445345A84BCD459E8C2AC2BA7651355B
    hide tag_93E1ED3B9EFB461486972450D09B1393
    hide tag_98EEC70DEB344EA5BDB430BB03A0BBE7
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ renpy.pause(2, hard=True)

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_445345A84BCD459E8C2AC2BA7651355B = 200
    show rs_image_3FDAF1D21ADF42CB88D0E1036D606D54 as tag_445345A84BCD459E8C2AC2BA7651355B at center_bottom zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_FD68A346D7D44E428AFB4158847AC3EE

    pause 1.2

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_86F3BBBA9EB74881AC89CD8328868CD6 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_582B28E0E2DD42FA964BF576F8F12DBD as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_BABCD5D2E5A54EBD81AEB01B3A0580F7

    pause 0.5

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Yoo 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Yoo 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Yoo 1.ogg"

    show rs_image_B3EE009F700A45B3977802B904CFE952 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_3A4BA4C12CE946B5B47CA31B0DB6CAC2


    if judge_lm_condition([]):
        jump block_00003B53

    return

label block_00003B53:
    # Node: 00003B53 (選擇)
    $ sys_lm_menu_item = [{"pos": (80, 220),"image": "images/Games/Yakyuken/CHOICE/Rock.png","hover": "images/Games/Yakyuken/CHOICE/Rock hover.png","name": "Rock"}, {"pos": (290, 220),"image": "images/Games/Yakyuken/CHOICE/Scissors.png","hover": "images/Games/Yakyuken/CHOICE/Scissors hover.png","name": "Scissors"}, {"pos": (512, 220),"image": "images/Games/Yakyuken/CHOICE/Paper.png","hover": "images/Games/Yakyuken/CHOICE/Paper hover.png","name": "Paper"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, -0.001) from _call_lm_menu_426
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Scissors\"" },{ "scope": 1, "content": "YKKEnemyChoice == 2" },{ "scope": 1, "content": "YKKAllyLife == 1" },{ "scope": 2, "content": "YKKMustWin == True" }]):
        jump block_00003B60
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Rock\"" },{ "scope": 1, "content": "YKKEnemyChoice == 1" },{ "scope": 1, "content": "YKKAllyLife == 1" },{ "scope": 2, "content": "YKKMustWin == True" }]):
        jump block_00003B5E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Paper\"" },{ "scope": 1, "content": "YKKEnemyChoice == 0" },{ "scope": 1, "content": "YKKAllyLife == 1" },{ "scope": 2, "content": "YKKMustWin == True" }]):
        jump block_00003B61
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Scissors\"" },{ "scope": 1, "content": "YKKEnemyChoice == 1" }]):
        jump block_00003B5F
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Rock\"" },{ "scope": 1, "content": "YKKEnemyChoice == 0" }]):
        jump block_00003B5B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Paper\"" },{ "scope": 1, "content": "YKKEnemyChoice == 2" }]):
        jump block_00003B63
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Scissors\"" },{ "scope": 1, "content": "YKKEnemyChoice == 0" }]):
        jump block_00003B5C
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Rock\"" },{ "scope": 1, "content": "YKKEnemyChoice == 2" }]):
        jump block_00003B5D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"Paper\"" },{ "scope": 1, "content": "YKKEnemyChoice == 1" }]):
        jump block_00003B62

    return

label block_00003B60:
    # Node: 00003B60 (S - P)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_9453C611A6E44C138BAD374653AB1038 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    $ zorder_tag_93E1ED3B9EFB461486972450D09B1393 = 300
    show rs_image_26D8970A553148548DEBB169BD8083D9 as tag_93E1ED3B9EFB461486972450D09B1393 at Transform(xpos=128, ypos=220) zorder zorder_tag_93E1ED3B9EFB461486972450D09B1393 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    $ zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 = 300
    show rs_image_71E6425D726744D28CC59B4689BB52E3 as tag_98EEC70DEB344EA5BDB430BB03A0BBE7 at Transform(xpos=464, ypos=220) zorder zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B64

    return

label block_00003B64:
    # Node: 00003B64 (Win)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 2.ogg"

    $ zorder_tag_62B301F7D3B54E57A3E8F7E6E0E8B145 = 500
    show rs_image_99E5D61DF982413DA7EBF936D43DC9FA as tag_62B301F7D3B54E57A3E8F7E6E0E8B145 at center_top zorder zorder_tag_62B301F7D3B54E57A3E8F7E6E0E8B145 onlayer master
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    hide tag_62B301F7D3B54E57A3E8F7E6E0E8B145
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00003B6D

    return

label block_00003B6D:
    # Node: 00003B6D (Win)
    $ YKKEnemyLife = YKKEnemyLife - 1

    if judge_lm_condition([]):
        jump block_00003B68

    return

label block_00003B68:
    # Node: 00003B68 (TO: Update)

    if judge_lm_condition([]):
        jump block_00003B69

    return

label block_00003B69:
    # Node: 00003B69 (TO: Update)

    if judge_lm_condition([]):
        jump block_00003B54

    return

label block_00003B5E:
    # Node: 00003B5E (R - S)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_9453C611A6E44C138BAD374653AB1038 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    $ zorder_tag_93E1ED3B9EFB461486972450D09B1393 = 300
    show rs_image_29F1CF10388847AC865DE47D926EB220 as tag_93E1ED3B9EFB461486972450D09B1393 at Transform(xpos=128, ypos=220) zorder zorder_tag_93E1ED3B9EFB461486972450D09B1393 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    $ zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 = 300
    show rs_image_26D8970A553148548DEBB169BD8083D9 as tag_98EEC70DEB344EA5BDB430BB03A0BBE7 at Transform(xpos=464, ypos=220) zorder zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B64

    return

label block_00003B61:
    # Node: 00003B61 (P - R)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_9453C611A6E44C138BAD374653AB1038 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    $ zorder_tag_93E1ED3B9EFB461486972450D09B1393 = 300
    show rs_image_71E6425D726744D28CC59B4689BB52E3 as tag_93E1ED3B9EFB461486972450D09B1393 at Transform(xpos=128, ypos=220) zorder zorder_tag_93E1ED3B9EFB461486972450D09B1393 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    $ zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 = 300
    show rs_image_29F1CF10388847AC865DE47D926EB220 as tag_98EEC70DEB344EA5BDB430BB03A0BBE7 at Transform(xpos=464, ypos=220) zorder zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B64

    return

label block_00003B5F:
    # Node: 00003B5F (S - S)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_9453C611A6E44C138BAD374653AB1038 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    $ zorder_tag_93E1ED3B9EFB461486972450D09B1393 = 300
    show rs_image_26D8970A553148548DEBB169BD8083D9 as tag_93E1ED3B9EFB461486972450D09B1393 at Transform(xpos=128, ypos=220) zorder zorder_tag_93E1ED3B9EFB461486972450D09B1393 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    $ zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 = 300
    show rs_image_26D8970A553148548DEBB169BD8083D9 as tag_98EEC70DEB344EA5BDB430BB03A0BBE7 at Transform(xpos=464, ypos=220) zorder zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B66

    return

label block_00003B66:
    # Node: 00003B66 (Deuce)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Dorky 1.ogg"


    if judge_lm_condition([]):
        jump block_00003B6F

    return

label block_00003B6F:
    # Node: 00003B6F (Deuce)
    $ YKKSkipCreateCG = True

    if judge_lm_condition([]):
        jump block_00003B68

    return

label block_00003B5B:
    # Node: 00003B5B (R - R)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_9453C611A6E44C138BAD374653AB1038 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    $ zorder_tag_93E1ED3B9EFB461486972450D09B1393 = 300
    show rs_image_29F1CF10388847AC865DE47D926EB220 as tag_93E1ED3B9EFB461486972450D09B1393 at Transform(xpos=128, ypos=220) zorder zorder_tag_93E1ED3B9EFB461486972450D09B1393 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    $ zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 = 300
    show rs_image_29F1CF10388847AC865DE47D926EB220 as tag_98EEC70DEB344EA5BDB430BB03A0BBE7 at Transform(xpos=464, ypos=220) zorder zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B66

    return

label block_00003B63:
    # Node: 00003B63 (P - P)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_9453C611A6E44C138BAD374653AB1038 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    $ zorder_tag_93E1ED3B9EFB461486972450D09B1393 = 300
    show rs_image_71E6425D726744D28CC59B4689BB52E3 as tag_93E1ED3B9EFB461486972450D09B1393 at Transform(xpos=128, ypos=220) zorder zorder_tag_93E1ED3B9EFB461486972450D09B1393 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    $ zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 = 300
    show rs_image_71E6425D726744D28CC59B4689BB52E3 as tag_98EEC70DEB344EA5BDB430BB03A0BBE7 at Transform(xpos=464, ypos=220) zorder zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B66

    return

label block_00003B5C:
    # Node: 00003B5C (S - R)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_9453C611A6E44C138BAD374653AB1038 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    $ zorder_tag_93E1ED3B9EFB461486972450D09B1393 = 300
    show rs_image_26D8970A553148548DEBB169BD8083D9 as tag_93E1ED3B9EFB461486972450D09B1393 at Transform(xpos=128, ypos=220) zorder zorder_tag_93E1ED3B9EFB461486972450D09B1393 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    $ zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 = 300
    show rs_image_29F1CF10388847AC865DE47D926EB220 as tag_98EEC70DEB344EA5BDB430BB03A0BBE7 at Transform(xpos=464, ypos=220) zorder zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B65

    return

label block_00003B65:
    # Node: 00003B65 (Lose)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Hit 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Hit 2.ogg"

    $ zorder_tag_62B301F7D3B54E57A3E8F7E6E0E8B145 = 500
    show rs_image_CC84F7B6DC29475CAD8E4D7FA82F6356 as tag_62B301F7D3B54E57A3E8F7E6E0E8B145 at center_bottom zorder zorder_tag_62B301F7D3B54E57A3E8F7E6E0E8B145 onlayer master
    with rs_effect_66AB5DA1801D4C12AA109F014A7EDBDF

    hide tag_62B301F7D3B54E57A3E8F7E6E0E8B145
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    if judge_lm_condition([]):
        jump block_00003B6E

    return

label block_00003B6E:
    # Node: 00003B6E (Lose)
    $ YKKAllyLife = YKKAllyLife - 1
    $ YKKSkipCreateCG = True

    if judge_lm_condition([]):
        jump block_00003B68

    return

label block_00003B5D:
    # Node: 00003B5D (R - P)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_9453C611A6E44C138BAD374653AB1038 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    $ zorder_tag_93E1ED3B9EFB461486972450D09B1393 = 300
    show rs_image_29F1CF10388847AC865DE47D926EB220 as tag_93E1ED3B9EFB461486972450D09B1393 at Transform(xpos=128, ypos=220) zorder zorder_tag_93E1ED3B9EFB461486972450D09B1393 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    $ zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 = 300
    show rs_image_71E6425D726744D28CC59B4689BB52E3 as tag_98EEC70DEB344EA5BDB430BB03A0BBE7 at Transform(xpos=464, ypos=220) zorder zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B65

    return

label block_00003B62:
    # Node: 00003B62 (P - S)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Impact 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Impact 1.ogg"

    show rs_image_9453C611A6E44C138BAD374653AB1038 as tag_445345A84BCD459E8C2AC2BA7651355B zorder zorder_tag_445345A84BCD459E8C2AC2BA7651355B onlayer master
    with rs_effect_70C20BBBD5964F65A50568CD34CCD88B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Break 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Break 1.ogg"

    $ zorder_tag_93E1ED3B9EFB461486972450D09B1393 = 300
    show rs_image_71E6425D726744D28CC59B4689BB52E3 as tag_93E1ED3B9EFB461486972450D09B1393 at Transform(xpos=128, ypos=220) zorder zorder_tag_93E1ED3B9EFB461486972450D09B1393 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    $ zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 = 300
    show rs_image_26D8970A553148548DEBB169BD8083D9 as tag_98EEC70DEB344EA5BDB430BB03A0BBE7 at Transform(xpos=464, ypos=220) zorder zorder_tag_98EEC70DEB344EA5BDB430BB03A0BBE7 onlayer master
    with rs_effect_475D3B5F4D4C431BBD1999CAD3E3CD83

    pause 0.5


    if judge_lm_condition([]):
        jump block_00003B65

    return

