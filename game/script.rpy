label splashscreen:
    play music "sound/BGM/Start scene.ogg"
    show black
    image lmc_0000238E_background = "images/Start Scene/Background.png"
    show lmc_0000238E_background
    image lmc_0000238E_logo = "images/Start Scene/Pre-load movie/Logo.png"
    show lmc_0000238E_logo:
        alpha 0.0
        linear 4.5 alpha 1.0
        linear 4.5 alpha 0.0
        pause 19.0
        repeat
    pause 1.0
    image lmc_0000238E_click_waiting = ParameterizedText(
        font="font/source-hans-sans-medium.ttc",
        color="#068AFC",
        xalign=0.5,
        yalign=0.6,
        size=40,
        outlines=[(absolute(6), "#FFFFFF00", absolute(0), absolute(0)),
                  (absolute(4), "#FFFFFF44", absolute(0), absolute(0)),
                  (absolute(2), "#FFFFFF88", absolute(0), absolute(0))])
    show lmc_0000238E_click_waiting (_("点击开始")) zorder 100:
        alpha 0.0
        linear 1.0 alpha 1.0
        pause 1.0
        linear 1.0 alpha 0.0
        repeat
    image lmc_0000238E_Tomo = "images/Start Scene/Pre-load movie/Tomo.png"
    show lmc_0000238E_Tomo:
        alpha 0.0
        pause 6.0
        linear 1.0 alpha 1.0
        pause 2.0
        linear 1.0 alpha 0.0
        pause 18.0
        repeat
    image lmc_0000238E_Shinobu = "images/Start Scene/Pre-load movie/Shinobu.png"
    show lmc_0000238E_Shinobu:
        alpha 0.0
        pause 8.4
        linear 1.0 alpha 1.0
        pause 2.0
        linear 1.0 alpha 0.0
        pause 15.6
        repeat
    image lmc_0000238E_Tsubasa = "images/Start Scene/Pre-load movie/Tsubasa.png"
    show lmc_0000238E_Tsubasa:
        alpha 0.0
        pause 13.2
        linear 1.0 alpha 1.0
        pause 2.0
        linear 1.0 alpha 0.0
        pause 10.8
        repeat
    image lmc_0000238E_Sakuya = "images/Start Scene/Pre-load movie/Sakuya.png"
    show lmc_0000238E_Sakuya:
        alpha 0.0
        pause 14.6
        linear 1.0 alpha 1.0
        pause 2.0
        linear 1.0 alpha 0.0
        pause 9.4
        repeat
    image lmc_0000238E_Akamine = "images/Start Scene/Pre-load movie/Tsuki-Sora.png"
    show lmc_0000238E_Akamine:
        alpha 0.0
        pause 19.0
        linear 1.0 alpha 1.0
        pause 2.0
        linear 1.0 alpha 0.0
        pause 5.0
        repeat
    image lmc_0000238E_Shintaro = "images/Start Scene/Pre-load movie/Shintaro.png"
    show lmc_0000238E_Shintaro:
        alpha 0.0
        pause 23.0
        linear 1.0 alpha 1.0
        pause 2.0
        linear 1.0 alpha 0.0
        pause 1.0
        repeat
    image lmc_0000238E_Saburo = "images/Start Scene/Pre-load movie/Saburo.png"
    show lmc_0000238E_Saburo:
        alpha 0.0
        pause 23.7
        linear 1.0 alpha 1.0
        pause 2.0
        linear 1.0 alpha 0.0
        pause 0.3
        repeat
    pause
    hide lmc_0000238E_logo
    hide lmc_0000238E_click_waiting
    hide lmc_0000238E_Tomo
    hide lmc_0000238E_Shinobu
    hide lmc_0000238E_Tsubasa
    hide lmc_0000238E_Sakuya
    hide lmc_0000238E_Akamine
    hide lmc_0000238E_Shintaro
    hide lmc_0000238E_Saburo
    with Dissolve(0.5)

    return

label start:
    $ _skipping = True
    $ _dismiss_pause = True
    $ sys_music_current_file = ""
    $ sys_music2_current_file = ""
    $ sys_effect_current_file = ""
    $ sys_effect2_current_file = ""
    $ sys_effect3_current_file = ""
    $ sys_effect4_current_file = ""
    $ set_window("イベントモード")

    stop music fadeout 1.0
    
    show black zorder -100
    with Dissolve(0.5)

    image center_title = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#000000",
        xalign=0.5,
        yalign=0.5,
        size=30,
        text_align=0.5,
        outlines=[(absolute(2), "#FFFFFF", absolute(0), absolute(0))])

    image center_title_white = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#FFFFFF",
        xalign=0.5,
        yalign=0.5,
        size=30,
        text_align=0.5,
        outlines=[(absolute(2), "#000000", absolute(0), absolute(0))])

    image left_title = ParameterizedText(
        font="font/source-hans-sans-heavy.ttc",
        color="#000000",
        xalign=0.1,
        yalign=0.9,
        size=30,
        text_align=0.5,
        outlines=[(absolute(2), "#FFFFFF", absolute(0), absolute(0))])

    $ C1S1 = C1S2 = C1S3 = C1S4 = C1S5 = C2S1 = C2S2 = C2S3 = C2S4 = C2S5 = C2S6 = C3S1 = C3S2 = C3S3 = C3S4 = C3S5 = C3S6 = True

    call screen shintarou_notebook

    jump block_00003985

    return
