# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003F3D (Final score)

label block_00003F3E:
    # Node: 00003F3E ()

    if judge_lm_condition([]):
        jump block_00003F40

    return

label block_00003F40:
    # Node: 00003F40 (Background)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_0BDB8A4A05BB44ED81AE140BE96066BD
    with rs_effect_BE47ECCC0D6944BC919AF538D960F5EA

    pause 1.5

    if sys_music_current_file != "sound/Piano/sti_gymno_01_pi.ogg":
        play music "sound/Piano/sti_gymno_01_pi.ogg" loop
        $ sys_music_current_file = "sound/Piano/sti_gymno_01_pi.ogg"

    $ zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 = 0
    show rs_image_128A19B2910148BD876660D835380008 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 at center_bottom zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_2B3B849B552243179409B8411C157783

    pause 3

    if sys_effect_current_file != "sound/Effect Sound/Paper 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Paper 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Paper 1.ogg"

    show rs_image_17BE90256FA34F51AC4CF030C593146A as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_57CE8EBF60D542D08516CF92F41A556F

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003F85

    return

label block_00003F85:
    # Node: 00003F85 (Calculate)
    $ TargetImageX = 0
    $ TargetImageY = 0
    $ Score = 0
    $ ChapterScore = 0
    $ Score = C1S4 + C1S5
    $ TargetImageX = 473 + (2 - Score) * 42
    $ TargetImageY = 131
    $ renpy.show("images/Score/Circle.png", at_list=[Transform(xpos=TargetImageX, ypos=TargetImageY)], what=renpy.easy.displayable("images/Score/Circle.png"), tag="C1StoryScore", zorder=1000)
    $ renpy.music.play("sound/Effect Sound/Attack 1.ogg", "effect")
    pause 0.5
    $ ChapterScore = Score
    $ Score = Max(C1QTsubasa + C1QNewsclub + C1QKimuraConference + CXQSabuImechen + CXQTsukiTest + C1QMatsuta + CXQShinoQuestion + C1QSabuShin - 6, 0)
    $ TargetImageX = 473 + (2 - Score) * 42
    $ TargetImageY = 172
    $ renpy.show("images/Score/Circle.png", at_list=[Transform(xpos=TargetImageX, ypos=TargetImageY)], what=renpy.easy.displayable("images/Score/Circle.png"), tag="C1QuestScore", zorder=1000)
    $ renpy.music.stop("effect", 0.2)
    $ renpy.music.play("sound/Effect Sound/Attack 1.ogg", "effect")
    pause 0.5
    $ ChapterScore = ChapterScore + Score
    $ Score = C0SShinobu + C1SSabuShin
    $ TargetImageX = 473 + (2 - Score) * 42
    $ TargetImageY = 215
    $ renpy.show("images/Score/Circle.png", at_list=[Transform(xpos=TargetImageX, ypos=TargetImageY)], what=renpy.easy.displayable("images/Score/Circle.png"), tag="C1SubeventScore", zorder=1000)
    $ renpy.music.stop("effect", 0.2)
    $ renpy.music.play("sound/Effect Sound/Attack 1.ogg", "effect")
    pause 0.5
    $ ChapterScore = ChapterScore + Score
    if ChapterScore == 6:
        $ renpy.show("images/Score/Best.png", at_list=[Transform(xpos=591, ypos=124)], what=renpy.easy.displayable("images/Score/Best.png"), tag="C1Score", zorder=1000)
    elif ChapterScore > 3:
        $ renpy.show("images/Score/Good.png", at_list=[Transform(xpos=591, ypos=124)], what=renpy.easy.displayable("images/Score/Good.png"), tag="C1Score", zorder=1000)
    else:
        $ renpy.show("images/Score/Fine.png", at_list=[Transform(xpos=591, ypos=124)], what=renpy.easy.displayable("images/Score/Fine.png"), tag="C1Score", zorder=1000)
    $ renpy.music.stop("effect", 0.2)
    $ renpy.music.play("sound/Effect Sound/Attack 1.ogg", "effect")
    pause 1
    $ Score = Max(C2S4 + C2S5 + C2S6 - 1, 0)
    $ TargetImageX = 473 + (2 - Score) * 42
    $ TargetImageY = 257
    $ renpy.show("images/Score/Circle.png", at_list=[Transform(xpos=TargetImageX, ypos=TargetImageY)], what=renpy.easy.displayable("images/Score/Circle.png"), tag="C2StoryScore", zorder=1000)
    $ renpy.music.stop("effect", 0.2)
    $ renpy.music.play("sound/Effect Sound/Attack 1.ogg", "effect")
    pause 0.5
    $ ChapterScore = Score
    $ Score = Max(CXQKaruta + C2QYuuhi + C2QKimuraConference + C2QSora + C2QSakuya +C2QNewsclub - 4, 0)
    $ TargetImageX = 473 + (2 - Score) * 42
    $ TargetImageY = 299
    $ renpy.show("images/Score/Circle.png", at_list=[Transform(xpos=TargetImageX, ypos=TargetImageY)], what=renpy.easy.displayable("images/Score/Circle.png"), tag="C2QuestScore", zorder=1000)
    $ renpy.music.stop("effect", 0.2)
    $ renpy.music.play("sound/Effect Sound/Attack 1.ogg", "effect")
    pause 0.5
    $ ChapterScore = ChapterScore + Score
    $ Score = C2SYuuhi + C2SNori
    $ TargetImageX = 473 + (2 - Score) * 42
    $ TargetImageY = 340
    $ renpy.show("images/Score/Circle.png", at_list=[Transform(xpos=TargetImageX, ypos=TargetImageY)], what=renpy.easy.displayable("images/Score/Circle.png"), tag="C2SubeventScore", zorder=1000)
    $ renpy.music.stop("effect", 0.2)
    $ renpy.music.play("sound/Effect Sound/Attack 1.ogg", "effect")
    pause 0.5
    $ ChapterScore = ChapterScore + Score
    if ChapterScore == 6:
        $ renpy.show("images/Score/Best.png", at_list=[Transform(xpos=591, ypos=249)], what=renpy.easy.displayable("images/Score/Best.png"), tag="C2Score", zorder=1000)
    elif ChapterScore > 3:
        $ renpy.show("images/Score/Good.png", at_list=[Transform(xpos=591, ypos=249)], what=renpy.easy.displayable("images/Score/Good.png"), tag="C2Score", zorder=1000)
    else:
        $ renpy.show("images/Score/Fine.png", at_list=[Transform(xpos=591, ypos=249)], what=renpy.easy.displayable("images/Score/Fine.png"), tag="C2Score", zorder=1000)
    $ renpy.music.stop("effect", 0.2)
    $ renpy.music.play("sound/Effect Sound/Attack 1.ogg", "effect")
    pause 1
    $ Score = Max(C3S4 + C3S5 + C3S6 - 1, 0)
    $ TargetImageX = 473 + (2 - Score) * 42
    $ TargetImageY = 382
    $ renpy.show("images/Score/Circle.png", at_list=[Transform(xpos=TargetImageX, ypos=TargetImageY)], what=renpy.easy.displayable("images/Score/Circle.png"), tag="C3StoryScore", zorder=1000)
    $ renpy.music.stop("effect", 0.2)
    $ renpy.music.play("sound/Effect Sound/Attack 1.ogg", "effect")
    # WARNING: Ignore condition of wait TRUE
    pause 0.5
    $ ChapterScore = Score
    $ Score = Max(C3QShiro + C3QKimuraConference + C3QNakayama + C3QYakyuken + C3QSakuyaWalk1 +C3QSakuyaWalk2 + C3QNewsclub - 5, 0)
    $ TargetImageX = 473 + (2 - Score) * 42
    $ TargetImageY = 424
    $ renpy.show("images/Score/Circle.png", at_list=[Transform(xpos=TargetImageX, ypos=TargetImageY)], what=renpy.easy.displayable("images/Score/Circle.png"), tag="C3QuestScore", zorder=1000)
    $ renpy.music.stop("effect", 0.2)
    $ renpy.music.play("sound/Effect Sound/Attack 1.ogg", "effect")
    pause 0.5
    $ ChapterScore = ChapterScore + Score
    $ Score = Max(C3SSabuShin + C3SPark + C3SShiroYuki +C3SYukiToki + C3SPhoto - 3, 0)
    $ TargetImageX = 473 + (2 - Score) * 42
    $ TargetImageY = 467
    $ renpy.show("images/Score/Circle.png", at_list=[Transform(xpos=TargetImageX, ypos=TargetImageY)], what=renpy.easy.displayable("images/Score/Circle.png"), tag="C3SubeventScore", zorder=1000)
    $ renpy.music.stop("effect", 0.2)
    $ renpy.music.play("sound/Effect Sound/Attack 1.ogg", "effect")
    pause 0.5
    $ ChapterScore = ChapterScore + Score
    if ChapterScore == 6:
        $ renpy.show("images/Score/Best.png", at_list=[Transform(xpos=591, ypos=376)], what=renpy.easy.displayable("images/Score/Best.png"), tag="C3Score", zorder=1000)
    elif ChapterScore > 3:
        $ renpy.show("images/Score/Good.png", at_list=[Transform(xpos=591, ypos=376)], what=renpy.easy.displayable("images/Score/Good.png"), tag="C3Score", zorder=1000)
    else:
        $ renpy.show("images/Score/Fine.png", at_list=[Transform(xpos=591, ypos=376)], what=renpy.easy.displayable("images/Score/Fine.png"), tag="C3Score", zorder=1000)
    $ renpy.music.stop("effect", 0.2)
    $ renpy.music.play("sound/Effect Sound/Attack 1.ogg", "effect")
    pause 1
    $ del TargetImageX
    $ del TargetImageY
    $ del Score
    $ del ChapterScore

    if judge_lm_condition([]):
        jump block_00003F82

    return

label block_00003F82:
    # Node: 00003F82 (CLEAR)
    if sys_effect_current_file != "sound/Effect Sound/Kirakira 1.ogg" or True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_DDEA0DFE1E9C413E81B40E334B3E1659 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_21F1EA2277F74660BEB3B56A8ACEAE1A

    pause 0.5

    pause

    stop music fadeout 3
    $ sys_music_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    hide C1Score
    hide C1StoryScore
    hide C1QuestScore
    hide C1SubeventScore
    hide C2Score
    hide C2StoryScore
    hide C2QuestScore
    hide C2SubeventScore
    hide C3Score
    hide C3StoryScore
    hide C3QuestScore
    hide C3SubeventScore
    with rs_effect_F4E162020AD741B2A2A1C91F35FC43D9

    pause 1.5


    if judge_lm_condition([]):
        jump block_00003F84

    return

label block_00003F84:
    # Node: 00003F84 ()

    return

