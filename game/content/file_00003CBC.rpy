# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00003CBC (END OF SEMESTER)

label block_00003CBD:
    # Node: 00003CBD ()
    $ SYSReviewChapter = 0
    $ E_TalkTentacleACave = 0
    $ E_TalkTentacleBCave = 0
    $ E_TalkKojimaSatouEvent = False
    $ E_IsCaveFirstArrive = True
    $ E_TalkSakase = -1
    $ E_TalkKaiEvent = False
    $ E_TAG_C3AllowTriggleSukimotoTalk = False
    $ E_TAG_TalkOkajimaInitNumber = 0
    $ E_TAG_StudyCount = 0
    $ E_TalkShintaroNoteComplete = True
    $ E_NativeMusicAvailable = False

    if judge_lm_condition([]):
        jump block_00003FB4

    return

label block_00003FB4:
    # Node: 00003FB4 (Chapter: EOS)
    $ Chapter = 4
    $ END = True
    $ E_TAG_C3AllowTriggleSukimotoTalk = EOSAllowTriggleSukimotoTalk
    $ E_TAG_TalkOkajimaInitNumber = EOSTalkOkajimaInitNumber
    $ E_TAG_StudyCount = EOSStudyCount
    $ del EOSStudyCount
    $ del EOSTalkOkajimaInitNumber
    $ del EOSAllowTriggleSukimotoTalk

    if judge_lm_condition([]):
        jump block_00003F34

    return

label block_00003F34:
    # Node: 00003F34 (Daytime)
    call block_0000405D from _call_block_0000405D

    return

