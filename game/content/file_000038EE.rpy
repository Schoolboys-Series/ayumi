# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 000038EE (SYSTEM UPDATE)

label block_000038EF:
    $ C1SG1 = C1S1 and C1S2 and C1S3
    $ C1SG2 = C1S4 and C1S5
    $ C2SG1 = C2S1 and C2S2 and C2S3
    $ C2SG2 = C2S4 and C2S5 and C2S6
    $ C3SG1 = C3S1 and C3S2 and C3S3
    $ C3SG2 = C3S4 and C3S5 and C3S6
    $ persistent.SystemStoryCache[0] = persistent.SystemStoryCache[0] or C1S1
    $ persistent.SystemStoryCache[1] = persistent.SystemStoryCache[1] or C1S2
    $ persistent.SystemStoryCache[2] = persistent.SystemStoryCache[2] or C1S3
    $ persistent.SystemStoryCache[3] = persistent.SystemStoryCache[3] or C1S4
    $ persistent.SystemStoryCache[4] = persistent.SystemStoryCache[4] or C1S5
    $ persistent.SystemStoryCache[5] = persistent.SystemStoryCache[5] or C2S1
    $ persistent.SystemStoryCache[6] = persistent.SystemStoryCache[6] or C2S2
    $ persistent.SystemStoryCache[7] = persistent.SystemStoryCache[7] or C2S3
    $ persistent.SystemStoryCache[8] = persistent.SystemStoryCache[8] or C2S4
    $ persistent.SystemStoryCache[9] = persistent.SystemStoryCache[9] or C2S5
    $ persistent.SystemStoryCache[10] = persistent.SystemStoryCache[10] or C2S6
    $ persistent.SystemStoryCache[11] = persistent.SystemStoryCache[11] or C3S1
    $ persistent.SystemStoryCache[12] = persistent.SystemStoryCache[12] or C3S2
    $ persistent.SystemStoryCache[13] = persistent.SystemStoryCache[13] or C3S3
    $ persistent.SystemStoryCache[14] = persistent.SystemStoryCache[14] or C3S4
    $ persistent.SystemStoryCache[15] = persistent.SystemStoryCache[15] or C3S5
    $ persistent.SystemStoryCache[16] = persistent.SystemStoryCache[16] or C3S6
    if VarExists("C3ShowLastWarning"):
        if (((C3S1 + C3S2 + C2S3) == 2) and ((C1SG2 == False) or (C2SG2 == False))) or ((C3S4 + C3S5 + C3S6) == 2):
            $ C3ShowLastWarning = True
        else:
            $ C3ShowLastWarning = False

    return
