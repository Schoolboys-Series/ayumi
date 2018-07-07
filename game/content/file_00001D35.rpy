# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 00001D35 (CP3 Daytime Misaki 慎太郎月空)

label block_00001D36:
    # Node: 00001D36 (開始)
    $ F3TalkAfterMainCharacterFinish = False
    $ CharacterRandom = 0
    $ SelectedCharacter = 0
    $ IsCharacterAccepted = False
    $ CurrentCharacterAccepted = False
    $ TalkKobaMinaF3 = False
    $ TalkSaburoF3 = False
    $ TalkSakuyaF3 = False
    $ TalkMatsutaF3 = False
    $ TalkSatouF3 = False
    $ TalkShiroYukiF3 = False
    $ TalkTomoF3 = False
    $ TalkKatouF3 = False
    $ TalkItouKimuraF3 = False
    $ TalkIzumiF3 = False
    $ TalkTsubasachanF3 = False
    $ TalkYuuhiF3 = False
    $ TalkNoriF3 = False
    $ TalkShinoTsubaF3 = False
    $ TalkKojimaOkajimaF3 = False

    jump block_000041FD

    return

label block_000041FD:
    # Node: 000041FD (Prepare)
    $ IsCharacterAccepted = [False] * 19
    $ Items = [
        { "name": _("花乃汤优惠券"), "count": 10, "description": _("去了就能修养身心。\n在一部分人中很有名的“花乃汤”的优惠券。") },
        { "name": _("Madchen Cafe优惠券"), "count": 10, "description": _("据说能体验到非常愉悦之感的咖啡店。") },
        { "name": _("天玉寺游乐园情侣票"), "count": 1, "description": _("动物园的双人票。\n也包括游乐园部分，约会的绝佳地点！") },
        { "name": _("拉面自助券"), "count": 1, "description": _("运动部的御用拉面店“电拉”的自助券。\n根据心情和态度店主有时会提供额外服务。") },
        { "name": _("《见习魔法师的任务》第一卷"), "count": 1, "description": _("某奇幻漫画的第一卷。\n主人公似乎被玩了各种PLAY。") },
        { "name": _("《见习魔法师的任务》最新卷"), "count": 1, "description": _("某奇幻漫画的最新一卷。\n主人公还是被各种PLAY中。") },
        { "name": _("眼镜布"), "count": 1, "description": _("当戴眼镜的人遭受天降至灾时\n牺牲自己另其重见光明的……布。") },
        { "name": _("关西观光杂志"), "count": 1, "description": _("当旅行计划能按照读书时所想的\n一模一样发展时会有不错的成就感。") },
        { "name": _("怀旧玩具合集"), "count": 1, "description": _("以前流行的玩具和游戏。\n对现在的孩子来说没准很新奇。") },
        { "name": _("流行玩具合集"), "count": 1, "description": _("街头巷尾流行的玩具。\n不过基本都需要在室内玩。") },
        { "name": _("高档狗食"), "count": 1, "description": _("加了满满肉质的狗食。\n对正在成长的狗狗超级合适。") },
        { "name": _("电动按摩器"), "count": -1, "description": _("电动按摩器。\n一举征服所有男孩子的利器。") },
        { "name": _("穗海作哉照片集"), "count": -1, "description": _("小岛的作哉偷拍集。\n如果有委托他也可以去拍别人。") },
        { "name": _("可爱动物照片集"), "count": -1, "description": _("小岛的可爱动物照片集。\n这些软软的姿态肯定能征服所有人！") },
        { "name": _("优美风景照片集"), "count": -1, "description": _("小岛的风景照片集。\n据说有助于成为浪漫的大人。") }
    ]

    jump block_00001D39

    return

label block_00001D39:
    # Node: 00001D39 (Misaki)
    if sys_music_current_file != "sound/BGM/Drum.ogg":
        play music "sound/BGM/Drum.ogg" loop
        $ sys_music_current_file = "sound/BGM/Drum.ogg"

    $ set_window("(標準)")
    stop music2 fadeout 0.2
    $ sys_music2_current_file = ""

    stop effect fadeout 0.2
    $ sys_effect_current_file = ""

    stop effect2 fadeout 0.2
    $ sys_effect2_current_file = ""

    $ set_place_title(False)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_99488938252D4BC2B7FA91D436D9159B
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ sys_ayumi_global_map_character = "tsuki_sora_shintaro"
    $ sys_ayumi_global_map_time = "daytime"

    if judge_lm_condition([{ "scope": 0, "content": "TalkSatouF3 * TalkMatsutaF3 * TalkSakuyaF3 * TalkSaburoF3 * TalkItouKimuraF3 * TalkKobaMinaF3 * TalkShiroYukiF3 * TalkKojimaOkajimaF3 * TalkShinoTsubaF3 <> 0" },{ "scope": 1, "content": "F3TalkAfterMainCharacterFinish == False" }]):
        jump block_00001DBE
    if judge_lm_condition([]):
        jump block_000041E3

    return

label block_00001DBE:
    # Node: 00001DBE (Step 2)
    pause 0.3

    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "嗯嗯♪这样就有很多人了！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "差不多这些人应该可以了？\n也很担心抬山车的大叔们的腰。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『如果没有更多可以招募的人，\n请点按{/color}{color=#FF00FF}“放弃目标”{/color}{color=#0080FF}按钮。』{/color}"

    window hide

    jump block_000031A6

    return

label block_000031A6:
    # Node: 000031A6 (T ++)
    $ F3TalkAfterMainCharacterFinish = True

    jump block_000041E3

    return

label block_000041E3:
    # Node: 000041E3 (Indicator)

    if judge_lm_condition([{ "scope": 0, "content": "TalkSatouF3 * TalkMatsutaF3 * TalkSakuyaF3 * TalkSaburoF3 * TalkItouKimuraF3 * TalkKobaMinaF3 * TalkShiroYukiF3 * TalkKojimaOkajimaF3 * TalkShinoTsubaF3 <> 0" }]):
        jump block_000031A3
    if judge_lm_condition([]):
        jump block_00001D3A

    return

label block_000031A3:
    # Node: 000031A3 (Misaki XCTA)
    if TalkNoriF3 == True and TalkYuuhiF3 == True and TalkTsubasachanF3 == True:
        $ del sys_ayumi_global_map_time
        $ del sys_ayumi_global_map_character
        jump block_000041F6

    call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character , "misaki", False, True, talk_label="block_00001D37", target_label="block_00001D38", break_confirm_title=(_("不需要更多参加者了？"),_("已经可以了"),_("还不够还不够还不够！"))) from _call_scb_global_map_82
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲学園\"" }]):
        jump block_00001D3D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"住宅街\"" }]):
        jump block_00001D3B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"公園\"" }]):
        jump block_00001D3E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"商店街\"" }]):
        jump block_00001D42
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲駅\"" }]):
        jump block_00001D60
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"昼休み不可\"" }]):
        jump block_000031A3
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00001D37
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00001D38
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄\"" }]):
        jump block_000031A0
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00003284

    return

label block_00001D3A:
    # Node: 00001D3A (Misaki XCTX)
    call scb_global_map(sys_ayumi_global_map_time, sys_ayumi_global_map_character, "misaki", False, False, talk_label="block_00001D37", target_label="block_00001D38", break_confirm_title=(_("不需要更多参加者了？"),_("已经可以了"),_("还不够还不够还不够！"))) from _call_scb_global_map_83
    $ del sys_ayumi_global_map_time
    $ del sys_ayumi_global_map_character

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲学園\"" }]):
        jump block_00001D3D
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"住宅街\"" }]):
        jump block_00001D3B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"商店街\"" }]):
        jump block_00001D42
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"公園\"" }]):
        jump block_00001D3E
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"御咲駅\"" }]):
        jump block_00001D60
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"昼休み不可\"" }]):
        jump block_00001D3A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"会話\"" }]):
        jump block_00001D37
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標確認\"" }]):
        jump block_00001D38
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"目標破棄不可\"" }]):
        jump block_00001D3A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"キャラクター\"" }]):
        jump block_00003284

    return

label block_00001D3D:
    # Node: 00001D3D (Misaki school)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("校门"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A99E3DECBAEF415DB7F99A84949EA0D7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkTomoF3 == False" }]):
        jump block_00001DCA
    if judge_lm_condition([]):
        jump block_00001D3C

    return

label block_00001DCA:
    # Node: 00001DCA (友)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_D0B3E32873F949DCA6C6D14851A1C27F as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呀吼——！今年也来参加祭典了哦！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_8B21F2EE5CAB4BA180475578DB7D237A as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "……今年是不是孩子们有些少？"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦哦——我的好友！{w}\n对啊～这里面有很深的原因的……\n{w=0.6}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Surprise 1.ogg"

    extend "{size=14}{/size}{size=16}……如此如此这般那般。{/size}"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AD37822A8D354BE2B52A438D983BDA93 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "欸——发生了这种事啊……\n我也是为了那身衣服去的哦。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_4C60252282D24EBEB3C772CC733637A2 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "自从那天明白了被裤装紧缚的感觉，\n便再也忘不了了。"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "真是的，友君……{w}能高兴当然很好，\n要是真的变成那样马上就会被发现的，\n一定要注意哦。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D220109FD0344CBB9F4E6657BDE95A4F as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊……是。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_739A9D89C79F4587BFC3289C4DD5DD97 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "一定要注意。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "等等！为什么这时候哥哥要说话的！"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "总之，作为参加的报酬要赠送礼品呐！"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_03F645A815E340E186C979234DEEA63E as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "太好了——！不过我什么都好哦——♪"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}友{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003149

    return

label block_00003149:
    # Node: 00003149 (T ++)
    $ TalkTomoF3 = True
    $ SelectedCharacter = 1

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_00001D68:
    # Node: 00001D68 (Selector)
    image danjiri_panel_title = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#C2185B",
        size=30,
        outlines=[(absolute(2), "#FFFFFF", absolute(0), absolute(0))])

    $ zorder_tag_C699A99FC13844B8A9D3F6E818A6F3D0 = 300
    show rs_image_3EBA93AFB8A84CBC812AF787D69AC4F4 as tag_C699A99FC13844B8A9D3F6E818A6F3D0 at center_bottom zorder zorder_tag_C699A99FC13844B8A9D3F6E818A6F3D0 onlayer master
    show danjiri_panel_title (_("所有物品")) at Transform(xpos=200,ypos=66) as danjiri_panel_title zorder 400 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if judge_lm_condition([]):
        jump block_000041FE

    return

screen danjiri_selector():
    $ ItemX = 0
    $ ItemY = 0
    $ i = 0
    for i in range(15):
        $ ItemX = 167 + Min(Max(i - 7, 0), 1) * 310
        $ ItemY = 131 + (i % 8) * 39
        if Items[i]["count"] == -1:
            pass
        elif Items[i]["count"] == 0:
            text Items[i]["name"] xpos ItemX ypos ItemY:
                style "danjiri_selector_item_text_empty"
        else:
            textbutton Items[i]["name"]:
                text_style "danjiri_selector_item_text"
                xpos ItemX
                ypos ItemY
                action [Hide("danjiri_detail"), Show("danjiri_detail", item=Items[i], index=i)]
        $ ItemX = 425 + Min(Max(i - 7, 0), 1) * 310
        $ ItemY = 131 + (i % 8) * 39
        if Items[i]["count"] == -1:
            pass
        else:
            text "x" + str(Items[i]["count"]) xpos ItemX ypos ItemY:
                style "danjiri_selector_item_text"

screen danjiri_detail(item, index):
    add "images/Selection/Danjiri/Preview.png" xpos 151 ypos 465
    add "images/Selection/Danjiri/Confirm.png" xpos 438 ypos 58
    text item["description"] style "danjiri_preview_text" xpos 161 ypos 485
    textbutton _("确定"):
        text_style "danjiri_detail_comfirm_button"
        xpos 455
        ypos 60
        action Return({ "name": item["name"], "index": index })
style danjiri_preview_text:
    font "font/zcool-happy-ayumi-extended.ttf"
    color "#FFFFFF"
    size 22
    outlines [(absolute(1), "#000000", absolute(0), absolute(0))]
style danjiri_selector_item_text:
    font "font/zcool-happy-ayumi-extended.ttf"
    color "#FFFFFF"
    size 18
    outlines [(absolute(1), "#FF98C6", absolute(0), absolute(0))]
    hover_color "#FF98C6"
    hover_outlines [(absolute(1), "#FFFFFF", absolute(0), absolute(0))]
style danjiri_selector_item_text_empty is danjiri_selector_item_text:
    color "#AAAAAA"
    outlines [(absolute(1), "#FFFFFF", absolute(0), absolute(0))]
    hover_color "#AAAAAA"
    hover_outlines [(absolute(1), "#FFFFFF", absolute(0), absolute(0))]
style danjiri_detail_comfirm_button:
    font "font/zcool-happy-ayumi-extended.ttf"
    size 30
    color "#C2185B"
    outlines [(absolute(3), "#FFFFFF", absolute(0), absolute(0))]
    hover_color "#FFFFFF"
    hover_outlines [(absolute(3), "#C2185B", absolute(0), absolute(0))]

label block_000041FE:
    # Node: 000041FE (Selector)
    image danjiri_panel_item = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#FFFFFF",
        size=18,
        outlines=[(absolute(1), "#FFFFFF", absolute(0), absolute(0))])
    image danjiri_panel_item_empty = ParameterizedText(
        font="font/zcool-happy-ayumi-extended.ttf",
        color="#FFFFFF",
        size=18,
        outlines=[(absolute(1), "#FFFFFF", absolute(0), absolute(0))])

    call screen danjiri_selector()
    $ _lm_selected_index = _return["index"]
    $ _lm_selected_value = _return["name"]

    hide screen danjiri_detail
    
    jump block_00004200

    return

label block_00004200:
    # Node: 00004200 (Updator)
    if SelectedCharacter == 1:
        $ CurrentCharacterAccepted = True
    elif SelectedCharacter == 2:
        if _lm_selected_index == 12 or _lm_selected_index == 11 or _lm_selected_index == 9:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 3:
        if _lm_selected_index == 7 or _lm_selected_index == 11 or _lm_selected_index == 14:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 5:
        if _lm_selected_index == 3 or _lm_selected_index == 11:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 6:
        if _lm_selected_index == 0 or _lm_selected_index == 1 or _lm_selected_index == 2 or _lm_selected_index == 11 or _lm_selected_index == 13:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 7:
        if _lm_selected_index == 0 or _lm_selected_index == 1 or _lm_selected_index == 2 or _lm_selected_index == 3 or _lm_selected_index == 11:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 8:
        if _lm_selected_index == 0 or _lm_selected_index == 1 or _lm_selected_index == 11 or _lm_selected_index == 13:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 9:
        if _lm_selected_index == 10 or _lm_selected_index == 12:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 10:
        if _lm_selected_index == 8 or _lm_selected_index == 11:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 11:
        if _lm_selected_index == 4 or _lm_selected_index == 11:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 12:
        if _lm_selected_index == 5 or _lm_selected_index == 11:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 13:
        if IsCharacterAccepted[17] == True and (_lm_selected_index == 4 or _lm_selected_index == 11 or _lm_selected_index == 13):
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 14 or SelectedCharacter == 15:
        $ CurrentCharacterAccepted = True
    elif SelectedCharacter == 16:
        if _lm_selected_index == 2 or _lm_selected_index == 11 or _lm_selected_index == 12 or _lm_selected_index == 14:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 17:
        if _lm_selected_index == 0 or _lm_selected_index == 1 or _lm_selected_index == 11:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 18:
        if _lm_selected_index == 0 or _lm_selected_index == 1 or _lm_selected_index == 2 or _lm_selected_index == 11 or _lm_selected_index == 13:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    elif SelectedCharacter == 19:
        if _lm_selected_index == 6 or _lm_selected_index == 1 or _lm_selected_index == 14:
            $ CurrentCharacterAccepted = True
        else:
            $ CurrentCharacterAccepted = False
    $ Items[_lm_selected_index]["count"] -= 1
    if CurrentCharacterAccepted == True:
        $ IsCharacterAccepted[SelectedCharacter - 1] = True

    if judge_lm_condition([]):
        jump block_00004221

    return

label block_00004221:
    # Node: 00004221 (CLEAR)
    hide tag_C699A99FC13844B8A9D3F6E818A6F3D0
    hide danjiri_panel_title
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    jump block_00004201

    return

label block_00004201:
    # Node: 00004201 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 1" }]):
        jump block_00001DCF
    if judge_lm_condition([]):
        jump block_00004203

    return

label block_00001DCF:
    # Node: 00001DCF (友 A)
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_4BF61371B4EA4299B4F80BBEDE40F3BF as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『友很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『友将会参加花车祭。』{/color}"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "啊，对了！要靠送东西找人参加的话，我有一个好东西哦！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "对那些怎么也不想穿的人，只要有这个就没问题了！"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "……不管是什么样的男孩子也能一击必杀♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "这、这是……！呼呼呼♪友亲，真是个坏孩子呐～"

    rs_character_D45A9D2E09284CA0B5A11E1BF07A3CA2 "呵呵呵♪"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『礼物表中添加了“电动按摩器”一个。』{/color}"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_0000314A

    return

label block_0000314A:
    # Node: 0000314A (Accept)
    $ Items[11]["count"] = 1

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_00004202:
    # Node: 00004202 (TO: Misaki)

    if judge_lm_condition([]):
        jump block_000041E7

    return

label block_000041E7:
    # Node: 000041E7 (TO: Misaki)

    if judge_lm_condition([]):
        jump block_000041E5

    return

label block_000041E5:
    # Node: 000041E5 (TO: Misaki)

    if judge_lm_condition([]):
        jump block_000041E4

    return

label block_000041E4:
    # Node: 000041E4 (TO: Misaki)

    if judge_lm_condition([]):
        jump block_000041E6

    return

label block_000041E6:
    # Node: 000041E6 (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001D39

    return

label block_00004203:
    # Node: 00004203 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 2" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DE2
    if judge_lm_condition([]):
        jump block_00004204

    return

label block_00001DE2:
    # Node: 00001DE2 (四朗 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_4D47049BB3064A929802A548D8ECC0C7 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『四朗很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『四朗将会参加花车祭。』{/color}"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "这、这真的没关系吗，会不会散开……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "（{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shoot 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shoot 1.ogg"

    extend "拍照{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Shoot 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Shoot 1.ogg"

    extend "拍照{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shoot 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shoot 1.ogg"

    extend "拍照{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Shoot 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Shoot 1.ogg"

    extend "拍照）"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}雪绪{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003152

    return

label block_00003152:
    # Node: 00003152 (Next)
    $ SelectedCharacter = 3

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_00004204:
    # Node: 00004204 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 2" }]):
        jump block_00001DE4
    if judge_lm_condition([]):
        jump block_00004206

    return

label block_00001DE4:
    # Node: 00001DE4 (四朗 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_1DC349F94DE94D6FACCF6AD451DDAE8E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『四朗不喜欢这个礼物，{/color}{w}{color=#00FFFF}并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『四朗至少会参加花车祭。』{/color}"

    rs_character_3B4C660F421B4BE392BB540B580F0339 "抱、抱歉，有些羞耻……"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_1DC349F94DE94D6FACCF6AD451DDAE8E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}雪绪{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003152

    return

label block_00004206:
    # Node: 00004206 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 3" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DE3
    if judge_lm_condition([]):
        jump block_00004205

    return

label block_00001DE3:
    # Node: 00001DE3 (雪緒 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_621A8D65BB0F4D3183FAB72AEE159692 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『雪绪很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『雪绪将会参加花车祭。』{/color}"

    rs_character_7009C1117C004F51829614A203C67DE7 "哦！比想像中的要好活动呐。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "（{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shoot 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shoot 1.ogg"

    extend "拍照{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Shoot 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Shoot 1.ogg"

    extend "拍照{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Shoot 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Shoot 1.ogg"

    extend "拍照{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Shoot 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Shoot 1.ogg"

    extend "拍照）"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00003153

    return

label block_00003153:
    # Node: 00003153 (Accept)

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_00004205:
    # Node: 00004205 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 3" }]):
        jump block_00001DE5
    if judge_lm_condition([]):
        jump block_00004207

    return

label block_00001DE5:
    # Node: 00001DE5 (雪緒 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_ABB2A951B8D345A092CC374396221386 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『雪绪不喜欢这个礼物，{/color}{w}{color=#00FFFF}并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『雪绪至少会参加花车祭。』{/color}"

    rs_character_7009C1117C004F51829614A203C67DE7 "果、果然还是不要穿了～……"

    window hide

    pause 0.7

    $ set_place_title("")
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7


    if judge_lm_condition([]):
        jump block_00003153

    return

label block_00004207:
    # Node: 00004207 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 5" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DEA
    if judge_lm_condition([]):
        jump block_00004208

    return

label block_00001DEA:
    # Node: 00001DEA (加藤 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_6064ADF1530C4CCCA775A14A4D889261 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『准太很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『准太将会参加花车祭。』{/color}"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "为了抹除心灵创伤我要再试一次！好！说干就干！"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦，大总统——♪"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00003155

    return

label block_00003155:
    # Node: 00003155 (Accept)

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_00004208:
    # Node: 00004208 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 5" }]):
        jump block_00001DEB
    if judge_lm_condition([]):
        jump block_00004209

    return

label block_00001DEB:
    # Node: 00001DEB (加藤 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_80C0E1DD873C4A0BB5F458CC590DE6E3 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『准太不喜欢这个礼物，{/color}{w}{color=#00FFFF}并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『准太至少会参加花车祭。』{/color}"

    rs_character_81D16F74A3C44B8982DB528D7D934850 "对不住，要像小时候那样疯不太现实……"

    window hide

    pause 0.7

    $ set_place_title("")
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7


    if judge_lm_condition([]):
        jump block_00003155

    return

label block_00004209:
    # Node: 00004209 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 6" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DF6
    if judge_lm_condition([]):
        jump block_0000420A

    return

label block_00001DF6:
    # Node: 00001DF6 (伊藤 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_1EC4013E35934B06A08FC6C3A749C6DB as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『圭很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『圭将会参加花车祭。』{/color}"

    rs_character_710A38AC94C841779DB701B5AC1010FD "嘛，偶尔也可以。"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}树{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003159

    return

label block_00003159:
    # Node: 00003159 (Next)
    $ SelectedCharacter = 7

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_0000420A:
    # Node: 0000420A (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 6" }]):
        jump block_00001DF7
    if judge_lm_condition([]):
        jump block_0000420B

    return

label block_00001DF7:
    # Node: 00001DF7 (伊藤 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_4EF6420177F64116B91BCBDDBDFEA52F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『圭不喜欢这个礼物，并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『圭至少会参加花车祭。』{/color}"

    rs_character_710A38AC94C841779DB701B5AC1010FD "我可没有……穿这个的勇气。"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}树{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003159

    return

label block_0000420B:
    # Node: 0000420B (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 7" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DF5
    if judge_lm_condition([]):
        jump block_0000420C

    return

label block_00001DF5:
    # Node: 00001DF5 (木村 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_78FD4FAFB4BA4B10BB6641EAE4ABC05E as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『树很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『树将会参加花车祭。』{/color}"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "好——！热闹起来——♪"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00003169

    return

label block_00003169:
    # Node: 00003169 (Accept)

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_0000420C:
    # Node: 0000420C (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 7" }]):
        jump block_00001DF4
    if judge_lm_condition([]):
        jump block_0000420D

    return

label block_00001DF4:
    # Node: 00001DF4 (木村 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_E8124A11D49145D0AE386AB993200B49 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『树不喜欢这个礼物，并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『树至少会参加花车祭。』{/color}"

    rs_character_E3F6ADD43DE44A428E1224756613C694 "呀，抱歉，现在这样就很有意思了。"

    window hide

    $ set_place_title("")
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91


    if judge_lm_condition([]):
        jump block_00003169

    return

label block_0000420D:
    # Node: 0000420D (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 8" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DED
    if judge_lm_condition([]):
        jump block_0000420E

    return

label block_00001DED:
    # Node: 00001DED (泉 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_AC23CE3BCF1A4DF6A8E789348F1A5AD0 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『翔很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『翔将会参加花车祭。』{/color}"

    rs_character_8D9249CA1389416BAF6A122851E276D0 "……。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "很合适哦！泉君。"

    rs_character_8D9249CA1389416BAF6A122851E276D0 "啊、哈哈，谢谢。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_8D9249CA1389416BAF6A122851E276D0 "（太好了……能看到的地方已经消下去了。\n要是不小心被看到了的话本想说是虫子叮咬蒙混过去的……）"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00003156

    return

label block_00003156:
    # Node: 00003156 (Accept)

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_0000420E:
    # Node: 0000420E (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 8" }]):
        jump block_00001DEE
    if judge_lm_condition([]):
        jump block_0000420F

    return

label block_00001DEE:
    # Node: 00001DEE (泉 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_801DE23A647744BCBFCB3A3097F1FE5E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『翔不喜欢这个礼物，并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『翔至少会参加花车祭。』{/color}"

    rs_character_8D9249CA1389416BAF6A122851E276D0 "抱、抱歉！说起来社团那边还有事……\n果然这次就先算了。"

    window hide

    pause 0.7

    $ set_place_title("")
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7


    if judge_lm_condition([]):
        jump block_00003156

    return

label block_0000420F:
    # Node: 0000420F (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 9" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DFF
    if judge_lm_condition([]):
        jump block_00004210

    return

label block_00001DFF:
    # Node: 00001DFF (小翼 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_66A069D2D1C644CAA34C2B06C2DCFC02 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『小翼很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『小翼将会参加花车祭。』{/color}"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哇——！我最喜欢和大家一起玩了——♪"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_0000315C

    return

label block_0000315C:
    # Node: 0000315C (Accept)

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_00004210:
    # Node: 00004210 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 9" }]):
        jump block_00001E00
    if judge_lm_condition([]):
        jump block_00004211

    return

label block_00001E00:
    # Node: 00001E00 (小翼 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_FACB6036013341EC894B878C7D2A109E as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『小翼不喜欢这个礼物，并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『小翼至少会参加花车祭。』{/color}"

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "这种东西不要啦！"

    window hide

    pause 0.7

    $ set_place_title("")
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7


    if judge_lm_condition([]):
        jump block_0000315C

    return

label block_00004211:
    # Node: 00004211 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 10" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DD7
    if judge_lm_condition([]):
        jump block_00004212

    return

label block_00001DD7:
    # Node: 00001DD7 (小林+南 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 500
    show rs_image_BF8B12E0E3F64C4DB962886DA0418594 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『小林和南很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『小林和南将会参加花车祭。』{/color}"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "哇——谢谢！我会好好珍惜的！"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "好——！今天要好好玩哦！"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_0000314E

    return

label block_0000314E:
    # Node: 0000314E (Accept)

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_00004212:
    # Node: 00004212 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 10" }]):
        jump block_00001DD8
    if judge_lm_condition([]):
        jump block_00004213

    return

label block_00001DD8:
    # Node: 00001DD8 (小林+南 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 400
    $ zorder_tag_063DF7E916A1424E84C7F9FED562D399 = 400
    show rs_image_892A36737DA046ACB115A2CF21689897 as tag_3C7A06FF4945452D859E685A41EEAAD5 at right_top zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    show rs_image_9F0EFB315BA5436EAF7727A13F09D748 as tag_063DF7E916A1424E84C7F9FED562D399 at left_top zorder zorder_tag_063DF7E916A1424E84C7F9FED562D399 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『小林和南不喜欢这个礼物，并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『小林和南至少会参加花车祭。』{/color}"

    rs_character_EA79386263E543A88D4DC03B8BD44485 "欸——好微妙～我不想要这个。"

    rs_character_9A978AAD07624C598B6179F23F51FB2D "我也是——"

    window hide

    pause 0.7

    $ set_place_title("")
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    hide tag_063DF7E916A1424E84C7F9FED562D399
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_0000314E

    return

label block_00004213:
    # Node: 00004213 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 11" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DFD
    if judge_lm_condition([]):
        jump block_00004214

    return

label block_00001DFD:
    # Node: 00001DFD (夕阳 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_DD79DA9A4E6A4C108DD05B8CA9B6CC65 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『夕阳很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『夕阳将会参加花车祭。』{/color}"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "为了正义献出自己的力量！"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_0000315B

    return

label block_0000315B:
    # Node: 0000315B (Accept)

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_00004214:
    # Node: 00004214 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 11" }]):
        jump block_00001DFC
    if judge_lm_condition([]):
        jump block_00004215

    return

label block_00001DFC:
    # Node: 00001DFC (夕阳 B)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_3FDCD7E4D59945F684522C8731382ECB as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『夕阳不喜欢这个礼物，并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『夕阳至少会参加花车祭。』{/color}"

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "唔、唔……抱歉，这次就……下次一定会的……"

    window hide

    pause 0.7

    $ set_place_title("")
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7


    if judge_lm_condition([]):
        jump block_0000315B

    return

label block_00004215:
    # Node: 00004215 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 12" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00003639
    if judge_lm_condition([]):
        jump block_00004216

    return

label block_00003639:
    # Node: 00003639 (朔 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_AD7BE6F755074C26AD756987A78EE83D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『朔很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『朔将会参加花车祭。』{/color}"

    rs_character_62324AD297554FE987C680452CEE232E "呵呵……能参加这样的祭典，对我来说也是好事。"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_0000363B

    return

label block_0000363B:
    # Node: 0000363B (Accept)

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_00004216:
    # Node: 00004216 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 12" }]):
        jump block_0000363A
    if judge_lm_condition([]):
        jump block_00004217

    return

label block_0000363A:
    # Node: 0000363A (朔 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_F33F4D4959B947DB9755DD0A59FB7942 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『朔不喜欢这个礼物，并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『朔至少会参加花车祭。』{/color}"

    rs_character_62324AD297554FE987C680452CEE232E "先不说参不参加，那种装束是和我八字不合的。\n太轻看我的身体了。"

    window hide

    pause 0.7

    $ set_place_title("")
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7


    if judge_lm_condition([]):
        jump block_0000363B

    return

label block_00004217:
    # Node: 00004217 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 13" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DFA
    if judge_lm_condition([]):
        jump block_00004218

    return

label block_00001DFA:
    # Node: 00001DFA (作哉 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_C23F899501AA42BFB8C966C48C9C1B70 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『作哉很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『作哉将会参加花车祭。』{/color}"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "哈！谁是贫弱的身体啊，不要小看篮球部。"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_0000315A

    return

label block_0000315A:
    # Node: 0000315A (Accept)

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_00004218:
    # Node: 00004218 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 13" }]):
        jump block_00001DF9
    if judge_lm_condition([]):
        jump block_00004219

    return

label block_00001DF9:
    # Node: 00001DF9 (作哉 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_5DACBAF38D6E4FE29C08A12B0FEB8C4A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『作哉不喜欢这个礼物，并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『作哉至少会参加花车祭。』{/color}"

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "谁会穿那种不知羞耻的东西。"

    window hide

    pause 0.7

    $ set_place_title("")
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7


    if judge_lm_condition([]):
        jump block_0000315A

    return

label block_00004219:
    # Node: 00004219 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 14" }]):
        jump block_00001DD5
    if judge_lm_condition([]):
        jump block_0000421A

    return

label block_00001DD5:
    # Node: 00001DD5 (小島 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_C5136717F28A4645A6BEEAEDCDF73816 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『正很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『正将会参加花车祭。』{/color}"

    rs_character_53FF68C192E3494AB005C1909579AFFB "欸——这次还有礼物呐。"

    rs_character_53FF68C192E3494AB005C1909579AFFB "……可以的话这个请拿去用，肯定会有想要的人的。"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『礼物表中添加了“可爱动物照片集”“优美风景照片集”各一份。』{/color}"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}直弥{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_0000314C

    return

label block_0000314C:
    # Node: 0000314C (Next)
    $ SelectedCharacter = 15
    $ Items[12]["count"] = 1
    $ Items[13]["count"] = 1
    $ Items[14]["count"] = 1

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_0000421A:
    # Node: 0000421A (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 15" }]):
        jump block_00001DDC
    if judge_lm_condition([]):
        jump block_0000421B

    return

label block_00001DDC:
    # Node: 00001DDC (岡島 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_7A0E218B5D4F4736B6C12C019B3EA826 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『直弥很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『直弥将会参加花车祭。』{/color}"

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "唔嗯！果然不穿成这样根本融入不进祭典啊！"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7


    if judge_lm_condition([]):
        jump block_0000314D

    return

label block_0000314D:
    # Node: 0000314D (Accept)

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_0000421B:
    # Node: 0000421B (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 16" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DE6
    if judge_lm_condition([]):
        jump block_0000421C

    return

label block_00001DE6:
    # Node: 00001DE6 (松田 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_B496C0103C82409F8A8F7FE3D02FED32 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『健治很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『健治将会参加花车祭。』{/color}"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "……拿你们没辙。我也来助一臂之力。"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "……不过话说回来这个穿起来意外还可以，有点改观了。"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00003154

    return

label block_00003154:
    # Node: 00003154 (Accept)

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_0000421C:
    # Node: 0000421C (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 16" }]):
        jump block_00001DE8
    if judge_lm_condition([]):
        jump block_0000421D

    return

label block_00001DE8:
    # Node: 00001DE8 (松田 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_56D6B709C8B5416A99FE10E21A364469 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『健治不喜欢这个礼物，并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『健治至少会参加花车祭。』{/color}"

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "抱歉，这种装束还是太羞耻了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "松田……你怎么还对这件事……！！"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "等、等一下哥哥！每个人都是不一样的！是不是？"

    window hide

    pause 0.7

    $ set_place_title("")
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7


    if judge_lm_condition([]):
        jump block_00003154

    return

label block_0000421D:
    # Node: 0000421D (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 17" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DDA
    if judge_lm_condition([]):
        jump block_0000421E

    return

label block_00001DDA:
    # Node: 00001DDA (忍 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_EB4B7F573DEC435BAD4F87970774788D as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『忍很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『忍将会参加花车祭。』{/color}"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "嘛，也算拿到好东西了。……不过，果然这身衣服太羞耻了。"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "因为在成长期，今天就已经觉得很紧了，\n明年也许就穿不了了。"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哈哈——说不准呐……"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}翼{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003160

    return

label block_00003160:
    # Node: 00003160 (Next)
    $ SelectedCharacter = 18

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_0000421E:
    # Node: 0000421E (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 17" }]):
        jump block_00001DDD
    if judge_lm_condition([]):
        jump block_0000421F

    return

label block_00001DDD:
    # Node: 00001DDD (忍 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『忍不喜欢这个礼物，并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『忍至少会参加花车祭。』{/color}"

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "唔……抱歉，今年还是……"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_CCE9211F1D544B1B9A81636F5959A677 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}翼{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003160

    return

label block_0000421F:
    # Node: 0000421F (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 18" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DDB
    if judge_lm_condition([]):
        jump block_00004220

    return

label block_00001DDB:
    # Node: 00001DDB (翼 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_FF6A5863BD354799A493F6068A1CEEC9 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『翼很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『翼将会参加花车祭。』{/color}"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "唔、唔——很不好意思——这是叫做“裤”？好、好紧……"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "因为身怀“巨物”嘛，唔呼呼呼♪"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00003150

    return

label block_00003150:
    # Node: 00003150 (Accept)

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_00004220:
    # Node: 00004220 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 18" }]):
        jump block_00001DDE
    if judge_lm_condition([]):
        jump block_00004222

    return

label block_00001DDE:
    # Node: 00001DDE (翼 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『翼不喜欢这个礼物，并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『翼至少会参加花车祭。』{/color}"

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "抱、抱歉，果然还是太羞耻了……"

    window hide

    pause 0.7

    $ set_place_title("")
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7


    if judge_lm_condition([]):
        jump block_00003150

    return

label block_00004222:
    # Node: 00004222 (TO: Character)

    if judge_lm_condition([{ "scope": 0, "content": "SelectedCharacter == 19" },{ "scope": 1, "content": "CurrentCharacterAccepted == True" }]):
        jump block_00001DF0
    if judge_lm_condition([]):
        jump block_00004223

    return

label block_00001DF0:
    # Node: 00001DF0 (佐藤 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_25DE12CC31C44F17AF7CB633FC89865C as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『光很喜欢这个礼物，{/color}{w}{color=#00FFFF}将会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『光将会参加花车祭。』{/color}"

    rs_character_EA9AA88E88D84B559B925363E2931756 "唔呀——果然这太羞耻了。不过，大家也都穿着，算了。"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00003157

    return

label block_00003157:
    # Node: 00003157 (Accept)

    if judge_lm_condition([]):
        jump block_00004202

    return

label block_00004223:
    # Node: 00004223 (TO: Character)

    if judge_lm_condition([]):
        jump block_00001DEF

    return

label block_00001DEF:
    # Node: 00001DEF (佐藤 R)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Wrong 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Wrong 1.ogg"

    $ set_place_title("")
    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 100
    show rs_image_85CA87C0E2714547A2E11A25B260A42F as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    show rs_image_FE8CE49E54AF48F48BC132D0E2289CDA as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.6

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 400
    show rs_image_6EB06386B3BF438184595D042608116A as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_top zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    pause 0.8

    $ set_window("イベントモード")
    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『光不喜欢这个礼物，并不会试穿服装。』{/color}"

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『光至少会参加花车祭。』{/color}"

    rs_character_EA9AA88E88D84B559B925363E2931756 "对不起，这再怎么说有点太勉强了……"

    window hide

    pause 0.7

    $ set_place_title("")
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")
    pause 0.7


    if judge_lm_condition([]):
        jump block_00003157

    return

label block_00001D3C:
    # Node: 00001D3C (Misaki school)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_353
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000041E5

    return

label block_00001D3B:
    # Node: 00001D3B (Residential street)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("住宅街"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D7154940FF02439388BA1F87BDD543E3 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkTomoF3 == False" }]):
        jump block_00001DCA
    if judge_lm_condition([{ "scope": 0, "content": "TalkKatouF3 == False" },{ "scope": 1, "content": "CharacterRandom < 6" }]):
        jump block_00001DE9
    if judge_lm_condition([{ "scope": 0, "content": "TalkItouKimuraF3 == False" },{ "scope": 1, "content": "CharacterRandom < 6" }]):
        jump block_00001DF2
    if judge_lm_condition([{ "scope": 0, "content": "TalkShiroYukiF3 == False" },{ "scope": 1, "content": "CharacterRandom < 6" }]):
        jump block_00001DE1
    if judge_lm_condition([]):
        jump block_00001D3F

    return

label block_00001DE9:
    # Node: 00001DE9 (加藤)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_C5C9A2538FCB4FCB827FE1BBFE20727F as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_81D16F74A3C44B8982DB528D7D934850 "不错嘛！哈哈，真怀念呐。\n最后一次参加应该是小5的时候了。"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦——加藤君你好呀——！\n怎么样？回归童心再来一次？"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_21A5A72FBBD8459A863B99B859A0013F as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "不——确实很想不过有次祭典途中衣服散开了，\n已经变成心灵创伤了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "什么！！居然这样——！？\n这种重要情报为何我的资料库里会没有！？"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_581796CAD76B4C929577B4C1D581EF10 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_81D16F74A3C44B8982DB528D7D934850 "啊——没被你知道其实挺好。\n"
    show rs_image_36E75A5BA4504559920E625E0462334C as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "不过那些大人笑得太厉害了，\n真的超羞耻的……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "好想看看加藤酱的好地方呐♪{w}\n嘛，别那么说了今年也以\n一气走光的气势来吧！"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}准太{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003165

    return

label block_00003165:
    # Node: 00003165 (T ++)
    $ TalkKatouF3 = True
    $ SelectedCharacter = 5

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_00001DF2:
    # Node: 00001DF2 (伊藤+木村)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_48D8C5CECCB84B739099EE1FBE060B20 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_E3F6ADD43DE44A428E1224756613C694 "哦——！不错不错！\n感受到祭典的热闹了——！\n我也要参……"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_EB52490B1A0A4E33BC3D00AD5EFD78E1 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "等等，我明白你的心情，\n但今天的训练强度本来就很高，\n赶快回家休息去。"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_4271CF98C3494E2FA007048FB141D469 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "欸——！才没那回事。\n错过这种有意思的活动对精神打击才更大哦。"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_6AC542E194714D3B9139FB8ED959EF70 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "唔……\n{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_E191791210724EEA9502E62AF8CDEDD5 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "但你就会穿成那样哦，行吗？"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_1990EB79915C41699DBA3A20A151B949 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_E3F6ADD43DE44A428E1224756613C694 "啊……是呐。但还是想去——\n{w=0.55}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_48D8C5CECCB84B739099EE1FBE060B20 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "伊藤酱好像也不是纯粹担心的样子。"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Pa 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Pa 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_75C2B184DB504C6B8E9957384EEB59E5 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_710A38AC94C841779DB701B5AC1010FD "什么意思！！！"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}圭{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003168

    return

label block_00003168:
    # Node: 00003168 (T ++)
    $ TalkItouKimuraF3 = True
    $ SelectedCharacter = 6

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_00001DE1:
    # Node: 00001DE1 (四朗+雪緒)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_AEF29DAA216E47B98629F2356997D217 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_7009C1117C004F51829614A203C67DE7 "哇——好厉害，好大的山车呐——"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_CE2AA99006A14FB68F9A5BA7EB0C8B29 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_3B4C660F421B4BE392BB540B580F0339 "扛着它的叔叔们也很厉害，\n"
    show rs_image_8BCAEF624622485E87EDCA1DB4125701 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "不过乘在上面好像也很有意思呐！"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "愿意参加的话，就可以乘在上面了哦。\n如何？要不要一起来享受祭典？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Kirakira 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Kirakira 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 300
    show rs_image_3687A9321C7B4D138F77BAB93AE5187A as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "呼呼，可爱的小学生们的姿态……\n只是想想就忍不住了～"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_41A84CEAB4B9488D918E907B63CC8E1A as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_3B4C660F421B4BE392BB540B580F0339 "……"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_415D182241854807A3375D2199A1DA38 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_7009C1117C004F51829614A203C67DE7 "……"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}四朗{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003162

    return

label block_00003162:
    # Node: 00003162 (T ++)
    $ TalkShiroYukiF3 = True
    $ SelectedCharacter = 2

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_00001D3F:
    # Node: 00001D3F (Residential street)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (552, 288),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (696, 360),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "隠し"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_354
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000041E5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001D48
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"隠し\"" }]):
        jump block_00001D4C

    return

label block_00001D48:
    # Node: 00001D48 (Residential street turning)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("住宅街路口"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A4E74E94E7C549809795CEBC732E6326 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkIzumiF3 == False" },{ "scope": 1, "content": "CharacterRandom < 6" }]):
        jump block_00001DEC
    if judge_lm_condition([{ "scope": 0, "content": "TalkItouKimuraF3 == False" },{ "scope": 1, "content": "CharacterRandom < 6" }]):
        jump block_00001DF2
    if judge_lm_condition([{ "scope": 0, "content": "TalkSaburoF3 == False" },{ "scope": 1, "content": "CharacterRandom < 6" }]):
        jump block_00001DDF
    if judge_lm_condition([]):
        jump block_000041E8

    return

label block_00001DEC:
    # Node: 00001DEC (泉)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_D668AB5BCE7641D598E5B719952F1E93 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_8D9249CA1389416BAF6A122851E276D0 "大家好。"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "泉君，你好！今年也来了呐。"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4CAFD25A1F5E4405A36AFD06AA87C091 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "嗯，听说今年遇到了很多挫折，\n我也想出一点力。"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "非常感谢。那请等我们准备一下泉君的衣服。"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D668AB5BCE7641D598E5B719952F1E93 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "嗯！{w=0.5}{nw}"
    show rs_image_A886E64725024E519334B46B47F7F928 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_5345B1A31CF144EC8F0B037DDCA0098B as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_3F09116E1F944952A143A708C140C6CA

    extend "……啊。"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_8D9249CA1389416BAF6A122851E276D0 "（麻烦了……之前那个{color=#FF80C0}痕迹{/color}说不定还留着……！）"

    show rs_image_6B3637450A254E26B3FE58D8EA24C639 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_8D9249CA1389416BAF6A122851E276D0 "（但现在也已经无法拒绝了……唔～竟然会这样……）"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}翔{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003166

    return

label block_00003166:
    # Node: 00003166 (T ++)
    $ TalkIzumiF3 = True
    $ SelectedCharacter = 8

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_00001DDF:
    # Node: 00001DDF (三朗)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 100
    show rs_image_B03B1B1EC5AC453EB98AC746686F6888 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "啊。"

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Cute 2.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 2.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "！！三酱！！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Finger Snap 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Finger Snap 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 200
    show rs_image_107F1D49D8E64904B63165A87DBFC26D as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_B4AB96B624DF4D2BB93266F16432FC2B

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "（来了！我的大本命！！\n不论{color=#FF00FF}做{/color}什么也要给他穿上这身衣服！）"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "（不过三酱肯定没兴趣的，\n至今为止从没参加过……\n唔唔……该怎么劝诱才好……！！）"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.6

    show rs_image_AB9B8E3D29CB454EA7EC6ED6E91C1CE1 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "我……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_DDDF386FF986455881E1B5DFB8EF2A24 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "今年……！\n"
    show rs_image_A8D996B64FF040029332404479DE8B96 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    pause 0.5

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_D8FC82CE48DA49309979B5A946A61B41 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "也让我参加！\n我……一直憧憬着这种硬汉的装束！！"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦！？"

    show rs_image_739A9D89C79F4587BFC3289C4DD5DD97 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "有眼光。那事不宜迟，尽快准备。\n首先是参加的礼物……"

    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A87485B3188F45C3A93B127A275967EE as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不需要！\n男人的浪漫不需要那种无聊的东西！"

    show rs_image_308DA681610949B78940D81D228A0172 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "不错啊，你们很不错啊。\n果然硬汉就是要这样——！"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window hide


    if judge_lm_condition([]):
        jump block_00001DE0

    return

label block_00001DE0:
    # Node: 00001DE0 (三朗 A)
    hide tag_BAEBA6F1B5AF40CC8B58E3426AC4477D
    hide tag_4D170217F16A4E7D9E3FEC718E139E17
    hide tag_B3BE0891BF2243B9B6E1AE2D4D61212D
    hide tag_230C5376F77E47F58C3F00942800353C
    hide tag_4E92252689C340DFA01D24DFEB7ECFEB
    hide tag_38E8277F6FD744099478DE7747B78253
    hide tag_79B16A8482EF44139BE652D8A6F16A94
    hide tag_0A1E2428FC2A4704817E80A27CFB9A88
    hide tag_F8E16E957AFF4D5682017D8E2EB4D29B
    hide tag_441F8CC9B8604F38915DDD0AAA6C4DA1
    hide tag_B01D021C81F043EC8329194DB0E5351C
    hide tag_DA8EDFF280524E4C8C2E742D1256578E
    hide tag_F9F10AFF06E94489AE06618A8EBD1C5B
    hide tag_D391C9C3898B48ADB0CD222A31E677E6
    hide tag_C9FFDEC01995483ABB9B28C31B71164B
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    hide tag_FCBC2A38F3BA491496BE2151B261AF48
    $ set_place_title("")
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 0.7

    $ set_window("イベントモード")
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Look! 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Look! 1.ogg"

    $ zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB = 400
    show rs_image_55BB38FA7D68431DBB9995586DA18004 as tag_3C0D2D9BB95B42AAA768FE8D105219CB at center_bottom zorder zorder_tag_3C0D2D9BB95B42AAA768FE8D105219CB onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause 1.4

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#00FFFF}『三朗将会参加花车祭。』{/color}"

    rs_character_078F0CD6ADB94AD5AA5BE8FF07BBC085 "咋样！合适不？\n今年终于能如愿好好玩了——！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "啊哇哇，三酱不要那么大胆地给我看后面——！！\n太没防备了！我、我要开动了哦！？"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Stupid 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "（直男特有的毫不自觉啊。\n不论如何我也必须从那些魔鬼手中誓死守护他……）"

    window hide

    pause 0.7

    hide tag_3C0D2D9BB95B42AAA768FE8D105219CB
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_ECFB5B509A334A868686B3435242BF90
    $ set_place_title("")
    with rs_effect_6B3CF87FF75645B9A45FBB353620EE91

    $ set_window("(標準)")

    if judge_lm_condition([]):
        jump block_00003151

    return

label block_00003151:
    # Node: 00003151 (T ++)
    $ TalkSaburoF3 = True
    $ IsCharacterAccepted[3] = True

    if judge_lm_condition([]):
        jump block_000041E7

    return

label block_000041E8:
    # Node: 000041E8 (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001D49

    return

label block_00001D49:
    # Node: 00001D49 (Residential street turning)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (120, 320),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "花乃湯"}, {"pos": (512, 320),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "神社"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_355
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"花乃湯\"" }]):
        jump block_00001D52
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"神社\"" }]):
        jump block_00001D50
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001D3B

    return

label block_00001D52:
    # Node: 00001D52 (花乃湯)
    stop music2 fadeout 0.2
    $ sys_music2_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("花乃汤"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_BB828FFB3AED43E6BB07C3169278015F as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkIzumiF3 == 0" },{ "scope": 1, "content": "CharacterRandom < 6" }]):
        jump block_00001DEC
    if judge_lm_condition([{ "scope": 0, "content": "TalkSaburoF3 == False" },{ "scope": 1, "content": "CharacterRandom < 6" }]):
        jump block_00001DDF
    if judge_lm_condition([]):
        jump block_000041EA

    return

label block_000041EA:
    # Node: 000041EA (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001D53

    return

label block_00001D53:
    # Node: 00001D53 (花乃湯)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (392, 352),"image": "images/MOVING/ACTIONS/Focusing 2.png","hover": "images/MOVING/ACTIONS/Focusing 2 hover.png","name": "ポスター"}, {"pos": (80, 280),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_356
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001D48
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001D5D

    return

label block_00001D5D:
    # Node: 00001D5D (River)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("河边"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    if sys_music2_current_file != "sound/Effect Sound/Wave 1.ogg":
        play music2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_music2_current_file = "sound/Effect Sound/Wave 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_788AB1D278244B129D0C9F9230156AD7 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkSakuyaF3 == False" },{ "scope": 1, "content": "CharacterRandom < 6" }]):
        jump block_00001DF8
    if judge_lm_condition([]):
        jump block_000041EB

    return

label block_00001DF8:
    # Node: 00001DF8 (作哉)
    pause 0.3

    stop music2 fadeout 1
    $ sys_music2_current_file = ""

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_573C19B20D334CB2A4B5E6AE92FDD27C as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "唔啊——你们穿的真强。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "什么什么？作酱也想穿？\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    extend "那就没的可选了～！客人一位～♪"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_CCB1A633889F460283C1F1F6FA453156 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "我没说过！跟笨蛋似的。回去了回去了。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Attack 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Attack 1.ogg"

    show rs_image_739A9D89C79F4587BFC3289C4DD5DD97 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "啊，原来如此。\n这种衣服像你这样贫弱的男人是穿不了的，\n有自知之明不错。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_04B0D298A2E94847A99BC62C2036C12B as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_22EB590C07AA48DDB7C3C251878D3BE5 "说什么你这混蛋……！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Flee 1.ogg"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "算、算了！作哉君也不要在意外表了，\n只是参加一下如何？"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "其他也有很多人会参加的。"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}作哉{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_0000316A

    return

label block_0000316A:
    # Node: 0000316A (T ++)
    $ TalkSakuyaF3 = True
    $ SelectedCharacter = 13

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_000041EB:
    # Node: 000041EB (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001D5E

    return

label block_00001D5E:
    # Node: 00001D5E (River)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_357
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001D52

    return

label block_00001D50:
    # Node: 00001D50 (Jinja)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("神社"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_65FB514C0D3B40558703DF2D35F42E17 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000041EF

    return

label block_000041EF:
    # Node: 000041EF (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001D51

    return

label block_00001D51:
    # Node: 00001D51 (Jinja)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_358
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001D48

    return

label block_00001D4C:
    # Node: 00001D4C (Square)
    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    $ reverse_volume("music", 1)

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("广场"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3B5A1C5EC3AA4BC08F04842878E1A1F0 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([]):
        jump block_000041F0

    return

label block_000041F0:
    # Node: 000041F0 (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001D4D

    return

label block_00001D4D:
    # Node: 00001D4D (Square)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (624, 248),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "泉の公園"}, {"pos": (120, 328),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "？？？"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_359
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"泉の公園\"" }]):
        jump block_00001D5A
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001D3B
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"？？？\"" }]):
        jump block_00001D4E

    return

label block_00001D5A:
    # Node: 00001D5A (Spring water park)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
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

    $ set_place_title(_("泉水公园"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wave 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_4C85C2BFFE134BFDADEC528506A90841 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkNoriF3 == False" },{ "scope": 1, "content": "CharacterRandom < 2" },{ "scope": 2, "content": "TalkSatouF3 * TalkMatsutaF3 * TalkSakuyaF3 * TalkSaburoF3 * TalkItouKimuraF3 * TalkKobaMinaF3 * TalkShiroYukiF3 * TalkKojimaOkajimaF3 * TalkShinoTsubaF3 <> 0" }]):
        jump block_00003638
    if judge_lm_condition([]):
        jump block_000041F2

    return

label block_00003638:
    # Node: 00003638 (朔)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_38E2853E83D641CFA189A9FC46AB7AD5 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_62324AD297554FE987C680452CEE232E "那边的各位。"

    show rs_image_739A9D89C79F4587BFC3289C4DD5DD97 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯？什么，希望参加祭典？"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "哇——！非常感谢。"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_092C4F890A874DA69A95FA3407A3732D as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "不，感觉有什么很有趣的味道。\n"
    show rs_image_25144F0AB6BB4BA784922991F30A5E47 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "看来某人存在那方面的经验呐，对这种装束。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "欸！？"

    show rs_image_739A9D89C79F4587BFC3289C4DD5DD97 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "唔，果然还是没能抑制住……{w}\n其实看到空这种样子，\n时不时就会想到{color=#FF00FF}那些事情{/color}……"

    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_38E2853E83D641CFA189A9FC46AB7AD5 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_62324AD297554FE987C680452CEE232E "能详细听听吗？\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_092C4F890A874DA69A95FA3407A3732D as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "现在这个样子也无法好好工作，\n我会给出好的提案。"

    show rs_image_739A9D89C79F4587BFC3289C4DD5DD97 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "是吗，那么……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 2.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "给我等等！\n在那之前不是应该先问能不能参加祭典吗！"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Stupid 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Stupid 1.ogg"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "真、真是的！不要擅自改变我的话题！"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}朔{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003637

    return

label block_00003637:
    # Node: 00003637 (T ++)
    $ TalkNoriF3 = True
    $ SelectedCharacter = 12

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_000041F2:
    # Node: 000041F2 (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001D5B

    return

label block_00001D5B:
    # Node: 00001D5B (Spring water park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_360
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001D4C

    return

label block_00001D4E:
    # Node: 00001D4E (Forest)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    $ record_volume("music")
    $ renpy.music.set_volume(0, 1, "music")

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("迷之地点"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wind 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wind 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7D781D05099A4C93AF6B1D005359F3E9 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkYuuhiF3 == False" },{ "scope": 1, "content": "CharacterRandom < 2" },{ "scope": 2, "content": "TalkSatouF3 * TalkMatsutaF3 * TalkSakuyaF3 * TalkSaburoF3 * TalkItouKimuraF3 * TalkKobaMinaF3 * TalkShiroYukiF3 * TalkKojimaOkajimaF3 * TalkShinoTsubaF3 <> 0" }]):
        jump block_00001DFB
    if judge_lm_condition([]):
        jump block_000041F1

    return

label block_00001DFB:
    # Node: 00001DFB (夕阳)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    $ reverse_volume("music")

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_0D6E2942C5A242B69D56894DDC96458A as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "哇啊！？吓我一跳！\n"
    show rs_image_9E2385E3E158453DB920D015F353CDAD as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "你、你们在这里干什么？\n而且这种莫名其妙的装扮是……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦哦——！这里也有少年出没！\n呀～边边角角都要看看呐。"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "这个叫做花车祭哦，\n大家一起搬运这个像是山车的很大的神轿，\n给大家带来活力哦。"

    show rs_image_AECC81DFE5584CBB81CAE2DD767DD5B7 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "欸——听起来很有意思。\n好像也能维持镇上的和平。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/As you wish 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/As you wish 1.ogg"

    show rs_image_5B44187C64DC4A32AAA681294DBBA8A6 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EFC67D522B5F4615BFAE716D87F58204 "既然如此就请也让我帮忙！"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}夕阳{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_0000316C

    return

label block_0000316C:
    # Node: 0000316C (T ++)
    $ TalkYuuhiF3 = True
    $ SelectedCharacter = 11

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_000041F1:
    # Node: 000041F1 (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001D4F

    return

label block_00001D4F:
    # Node: 00001D4F (Forest)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_361
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001D4C

    return

label block_00001D3E:
    # Node: 00001D3E (Park)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("公园"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_AC1A95BA21694004A67885C809E98CFF as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkTomoF3 == False" }]):
        jump block_00001DCA
    if judge_lm_condition([{ "scope": 0, "content": "TalkKobaMinaF3 == False" }]):
        jump block_00001DD6
    if judge_lm_condition([]):
        jump block_000041EC

    return

label block_00001DD6:
    # Node: 00001DD6 (小林+南)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 2.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 2.ogg"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_0DD616D8E2914FC2859CDB40FCB50F1A as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_EA79386263E543A88D4DC03B8BD44485 "啊！花车来了——！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_1CDB21F0CE5D4659A6BA9E03A4285F77 as tag_3C7A06FF4945452D859E685A41EEAAD5 zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "好棒的祭典！！"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_645DF0E195CF42798B8F728CE5EAEEE2 as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    rs_character_9A978AAD07624C598B6179F23F51FB2D "好棒的祭典哦！！"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦——年轻人真有气势。\n嗯嗯！有你们两个这样的孩子在\n祭典也能好好举行了。"

    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 = 300
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1FF2B98C6C1E44809702A907624A30EB as tag_3C7A06FF4945452D859E685A41EEAAD5 at center_bottom zorder zorder_tag_3C7A06FF4945452D859E685A41EEAAD5 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA79386263E543A88D4DC03B8BD44485 "啊，对了，呐——呐——空哥，{w}\n以前{color=#008080}插到你身体里{/color}对不起，\n有些用力太大了——{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Decision 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Decision 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 400
    show rs_image_73C341486AC740399EEDF1F7DB84E570 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend ""

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flash 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flash 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C2EBD607711F4DB78A9DBF2C9798A9E5 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_739A9D89C79F4587BFC3289C4DD5DD97 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_1B5FF639D1044BDDAEE2A66FB32F2CF7

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "！？！？"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "不、不是的！不是那个意思！"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    hide tag_3C7A06FF4945452D859E685A41EEAAD5
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}小林{/color}{color=#0080FF}和{/color}{color=#FF00FF}南{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_0000315F

    return

label block_0000315F:
    # Node: 0000315F (T ++)
    $ TalkKobaMinaF3 = True
    $ SelectedCharacter = 10

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_000041EC:
    # Node: 000041EC (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001D40

    return

label block_00001D40:
    # Node: 00001D40 (Park)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (696, 200),"image": "images/MOVING/ACTIONS/Hidden.png","hover": "images/MOVING/ACTIONS/Hidden hover.png","name": "隠し"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_362
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000041E5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"隠し\"" }]):
        jump block_00001DA9

    return

label block_00001DA9:
    # Node: 00001DA9 (Park hill)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("公园内山"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A924E6FB7A0740108CE21D8D0C0FC8D2 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkTsubasachanF3 == False" },{ "scope": 1, "content": "CharacterRandom < 3" },{ "scope": 2, "content": "TalkSatouF3 * TalkMatsutaF3 * TalkSakuyaF3 * TalkSaburoF3 * TalkItouKimuraF3 * TalkKobaMinaF3 * TalkShiroYukiF3 * TalkKojimaOkajimaF3 * TalkShinoTsubaF3 <> 0" }]):
        jump block_00001DFE
    if judge_lm_condition([]):
        jump block_000041ED

    return

label block_00001DFE:
    # Node: 00001DFE (小翼)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Cute 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Cute 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_79EEC8AD62B24332A4A9362795A61DC8 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_87ED686ED78C4AB6909895FBBBE8A60B "哇哦！有好多人类——！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 3.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 3.ogg"

    show rs_image_E7FB89F14D554B59971676B5C3A3F54D as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    extend "呐——呐——！在做什么呐——？\n和我玩——！一起玩——！"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哇！？干什么这孩子！\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Dorky 1.ogg"

    extend "不要，那里是……\n不、不行……！"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}小翼{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_0000316B

    return

label block_0000316B:
    # Node: 0000316B (T ++)
    $ TalkTsubasachanF3 = True
    $ SelectedCharacter = 9

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_000041ED:
    # Node: 000041ED (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001DA8

    return

label block_00001DA8:
    # Node: 00001DA8 (Park Hill)
    $ sys_lm_menu_item = [{"pos": (216, 88),"image": "images/MOVING/ACTIONS/Moving 2.png","hover": "images/MOVING/ACTIONS/Moving 2 hover.png","name": "移動する"}, {"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_363
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001DA7
    if judge_lm_condition([]):
        jump block_00001D3E

    return

label block_00001DA7:
    # Node: 00001DA7 (Park Hill Lake)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Grass 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Grass 1.ogg"

    stop effect2 fadeout 0.5
    $ sys_effect2_current_file = ""

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("公园湖边"))
    pause 0.4

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Wave 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Wave 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_7639E4BE73E34BBD9D978953E896CF0C as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_D40B37AD6AF94EE0AFF8CB0762377A91

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkTsubasachanF3 == False" },{ "scope": 1, "content": "CharacterRandom < 3" },{ "scope": 2, "content": "TalkSatouF3 * TalkMatsutaF3 * TalkSakuyaF3 * TalkSaburoF3 * TalkItouKimuraF3 * TalkKobaMinaF3 * TalkShiroYukiF3 * TalkKojimaOkajimaF3 * TalkShinoTsubaF3 <> 0" }]):
        jump block_00001DFE
    if judge_lm_condition([]):
        jump block_000041EE

    return

label block_000041EE:
    # Node: 000041EE (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001DA6

    return

label block_00001DA6:
    # Node: 00001DA6 (Park Hill Lake)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_364
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001DA9

    return

label block_00001D42:
    # Node: 00001D42 (Shopping street)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("商店街"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_5F022B91486841699EAC5FE3BDC0F5CE as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkTomoF3 == False" }]):
        jump block_00001DCA
    if judge_lm_condition([{ "scope": 0, "content": "TalkKojimaOkajimaF3 == False" }]):
        jump block_00001DD4
    if judge_lm_condition([]):
        jump block_000041F3

    return

label block_00001DD4:
    # Node: 00001DD4 (小島+岡島)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Inspiration 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Inspiration 1.ogg"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_6EACDBA5EB7B44D7A7699633252E6B7E as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "呀，各位！今年也到这个时候了呐。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_4DE7491D04004FC5BE18A0FEB043C1BF as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "按照惯例，请让我们也参加。"

    show rs_image_739A9D89C79F4587BFC3289C4DD5DD97 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "非常感谢二位。今年也要弄得热热闹闹的哦。"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "新闻部的报纸上也会刊载这次活动吗？\n我很期待哦。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_DF83E8681DAD43B1BF6C0CF0E3555C11 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "嗯！那赶快把衣服给我。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_A3D0E6087D6B4C4DA8B5F544E1F3B782 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "啊——……{w=0.5}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_1654C244584349A6B0811665076020BD as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "真的要穿？部长。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_AF867A4937BD47B085C2FBD0F564E665 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "嗯？当然了。\n不换上正式服装御咲花车祭可是不算开始的。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_1654C244584349A6B0811665076020BD as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_53FF68C192E3494AB005C1909579AFFB "……是吗。\n{w=0.55}{nw}"
    show rs_image_9F29F130587546EBA5C8BD952A84E3CF as tag_CC4336DE74164173AC47C2C317367F10 zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……要小心啊，部长。"

    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_CC4336DE74164173AC47C2C317367F10 = 300
    show rs_image_07383DF7F5A94166BAD98FE0E71F4768 as tag_CC4336DE74164173AC47C2C317367F10 at center_bottom zorder zorder_tag_CC4336DE74164173AC47C2C317367F10 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_41A906D279CA4677A6A2ED8CBE544459 "？"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    hide tag_CC4336DE74164173AC47C2C317367F10
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}正{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_0000315D

    return

label block_0000315D:
    # Node: 0000315D (T ++)
    $ TalkKojimaOkajimaF3 = True
    $ SelectedCharacter = 14

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_000041F3:
    # Node: 000041F3 (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001D43

    return

label block_00001D43:
    # Node: 00001D43 (Shopping street)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}, {"pos": (104, 256),"image": "images/MOVING/ACTIONS/Moving.png","hover": "images/MOVING/ACTIONS/Moving hover.png","name": "移動する"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_365
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000041E5
    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動する\"" }]):
        jump block_00001D4A

    return

label block_00001D4A:
    # Node: 00001D4A (Shopping street inside)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("商店街内"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Clamorous 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Clamorous 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_D5FE65484D524DF0ACA6C31DC2F622E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkMatsutaF3 == False" },{ "scope": 1, "content": "CharacterRandom < 6" }]):
        jump block_00001DE7
    if judge_lm_condition([{ "scope": 0, "content": "TalkKatouF3 == False" },{ "scope": 1, "content": "CharacterRandom < 6" }]):
        jump block_00001DE9
    if judge_lm_condition([{ "scope": 0, "content": "TalkItouKimuraF3 == False" },{ "scope": 1, "content": "CharacterRandom < 6" }]):
        jump block_00001DF2
    if judge_lm_condition([]):
        jump block_000041F4

    return

label block_00001DE7:
    # Node: 00001DE7 (松田)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_36FA043A9D13453B8E531655A8BDDE10 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "哦，花车祭啊。\n说起来也确实到时候了。"

    show rs_image_739A9D89C79F4587BFC3289C4DD5DD97 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "松田，你要不要也参加？\n记得去年你没参加对不？"

    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_ED1123A4A4404155ABBDBFA9983E6A38 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "啊——毕竟和社团冲突了。\n今天只是结束得早，也不是不能参加……"

    show rs_image_739A9D89C79F4587BFC3289C4DD5DD97 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "是嘛，感谢参与。\n那么松田穿起来比较合适的是……"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cut the wind 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cut the wind 1.ogg"

    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_3D04A5D178044F04B357189727365274 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "等等。"

    show rs_image_739A9D89C79F4587BFC3289C4DD5DD97 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "嗯？怎么了。"

    show rs_image_DA1C695151FE4CC4867C8C5414A47182 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_8044151835FD439999F1BE883381A5CC as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_0DB1F59F51E4429DBACC2B1352D3B7F3 "那个啊……不管怎么说要穿那个就有点……"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}健治{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003164

    return

label block_00003164:
    # Node: 00003164 (T ++)
    $ TalkMatsutaF3 = True
    $ SelectedCharacter = 16

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_000041F4:
    # Node: 000041F4 (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001D4B

    return

label block_00001D4B:
    # Node: 00001D4B (Shopping street inside)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_366
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_00001D42

    return

label block_00001D60:
    # Node: 00001D60 (御咲站)
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Walk 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Walk 1.ogg"

    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_74F4CAF2F88C4ADDA6E82D260E573C5B
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    $ set_place_title(_("御咲站"))
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Swallow 1.ogg" loop
        $ sys_effect2_current_file = "sound/Effect Sound/Swallow 1.ogg"

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_07BACEE3C1C64F1DAD61CD240DF0C2E5 as tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 zorder zorder_tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    pause 0.3


    if judge_lm_condition([{ "scope": 0, "content": "TalkTomoF3 == False" }]):
        jump block_00001DCA
    if judge_lm_condition([{ "scope": 0, "content": "TalkShinoTsubaF3 == False" }]):
        jump block_00001DD9
    if judge_lm_condition([{ "scope": 0, "content": "TalkSatouF3 == False" },{ "scope": 1, "content": "CharacterRandom < 6" }]):
        jump block_00001DF1
    if judge_lm_condition([]):
        jump block_000041F5

    return

label block_00001DD9:
    # Node: 00001DD9 (忍+翼)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_09D0AFA678734FA2930394DBEB002EF7 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_448920BBD02549838978B8525156A8E8

    window show

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "你们好——"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_3FF5037A502D4C24A92D108FA6E56C70 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "大、大家好。\n"
    show rs_image_93C0B7E63B614E9386D2D63EAAD23E8F as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "那个……大家都穿得很有趣呐。"

    show rs_image_C0F9D8B5A9384E3AA89C0CB8EB04DBC9 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "哦！翼亲和小忍！\n呀——这还真是稀奇的组合。"

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Cute 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Cute 1.ogg"

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "难道说，两位终于从\n喜欢那个黄发人形自走炮渐渐地……"

    if "sys_effect3_current_file" in globals() and sys_effect3_current_file != "sound/Effect Sound/Dorky 1.ogg" or True: # Hotfix: Ignore multiplay defenser for voice sound
        play effect3 "sound/Effect Sound/Dorky 1.ogg" noloop
        $ sys_effect3_current_file = "sound/Effect Sound/Dorky 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    show rs_image_C4ACCC5C4B794F3287B64EDAF6379084 as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_A7B77D634FDA4F01AB6ED891600EEDD6 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "不、不是的……！"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_52B5BCA8CBE443D4BB4698E2E1D83A45 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_D93E396B7ADB48CBAE13F206958FC08B "可能，最近我们关系很好的。"

    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Flee 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Flee 1.ogg"

    $ zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 = 100
    $ zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 = 300
    show rs_image_27968C670E8B4CAE8EDAACBE167BD25E as tag_26CE4420E4BF43ADBA4E35F2A9784E98 at center_bottom zorder zorder_tag_26CE4420E4BF43ADBA4E35F2A9784E98 onlayer master
    show rs_image_55B57643DE144DC0BBCAE4A0FA38D0A8 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 at center_bottom zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    hide tag_26CE4420E4BF43ADBA4E35F2A9784E98
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_C2CBBFE577DA4C4095B176A23C6C89D1 "欸——！！\n{w=0.55}{nw}"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    show rs_image_F4E4588DC479409680603E0DBD6B5E84 as tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 zorder zorder_tag_9D0001B69AD04AE9A8D1DE7AF344E0A3 onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "……啊，不！我很荣幸！"

    show rs_image_739A9D89C79F4587BFC3289C4DD5DD97 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "奥村，快说正事。"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "就是啊，翼君可是第一次看花车祭呢。"

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "如何？要不要一起参加？\n现在还有礼物附送哦！"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    hide tag_9D0001B69AD04AE9A8D1DE7AF344E0A3
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}忍{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003161

    return

label block_00003161:
    # Node: 00003161 (T ++)
    $ TalkShinoTsubaF3 = True
    $ SelectedCharacter = 17

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_00001DF1:
    # Node: 00001DF1 (佐藤)
    pause 0.3

    stop effect2 fadeout 1
    $ sys_effect2_current_file = ""

    pause 0.7

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect2 "sound/Effect Sound/Strike 1.ogg" noloop
        $ sys_effect2_current_file = "sound/Effect Sound/Strike 1.ogg"

    $ zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE = 300
    show rs_image_2E1F43EA232A44689196EAB6C6746E38 as tag_C3CCF1D5899F4E609345C51A82FBFFAE at center_bottom zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_B70215F4C83E407D8C2CA682FB6965D7

    window show

    rs_character_EA9AA88E88D84B559B925363E2931756 "哦——在学校已经听过传闻了，\n果然很大张旗鼓呐。"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "你好，佐藤君。\n佐藤君不是御咲出生的，\n这应该是第一次见到。"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_E9DA1A925CE140459A40C853C70AA406 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "是的。而且去年也因为社团活动没能去看。\n不过，看起来比想像中还要有趣呐。\n"
    if True: # Hotfix: Ignore multiplay defenser for effect sound
        play effect "sound/Effect Sound/Surprise 1.ogg" noloop
        $ sys_effect_current_file = "sound/Effect Sound/Surprise 1.ogg"

    show rs_image_F454E39E17AB417EAFAD03FC09D7C631 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "……{w=0.4}{size=20}（四处张望）{/size}"

    show rs_image_1100577F1808415DBCDF7EAD33DE321E as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_4CFD8855F77C4A9085B6B9BFABDD845A "……？在找谁？"

    show rs_image_788D1F2A4B204EF8B9A2DD8678C84171 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    show rs_image_1E6988844B884E2B88D92837EA789B61 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    rs_character_EA9AA88E88D84B559B925363E2931756 "不、没什么！什么都没有。\n{w=0.55}{nw}"
    show rs_image_0ED56A8EA704458D9455AFBC4C60221F as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_04F714FDB0E541E4813BA7A0A833CD54

    extend "{size=16}……{/size}也对，不可能在呐{size=16}……{/size}\n"
    show rs_image_2E24765C23544B69A9391DC51FE38194 as tag_C3CCF1D5899F4E609345C51A82FBFFAE zorder zorder_tag_C3CCF1D5899F4E609345C51A82FBFFAE onlayer master
    with rs_effect_A56BC4024D7642E48310911FC9A1EB4B

    extend "怎么做好呢，我要不要也参加呐。"

    hide tag_C3CCF1D5899F4E609345C51A82FBFFAE
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    show rs_image_B7B371E9C25B4882BF62B4D3040FFB76 as tag_ECFB5B509A334A868686B3435242BF90 zorder zorder_tag_ECFB5B509A334A868686B3435242BF90 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『选一个给{/color}{color=#FF00FF}光{/color}{color=#0080FF}的礼物。』{/color}"

    window hide


    if judge_lm_condition([]):
        jump block_00003167

    return

label block_00003167:
    # Node: 00003167 (T ++)
    $ TalkSatouF3 = True
    $ SelectedCharacter = 19

    if judge_lm_condition([]):
        jump block_00001D68

    return

label block_000041F5:
    # Node: 000041F5 (Random)
    $ CharacterRandom = Random(10)

    if judge_lm_condition([]):
        jump block_00001D62

    return

label block_00001D62:
    # Node: 00001D62 (御咲站)
    $ sys_lm_menu_item = [{"pos": (648, 496),"image": "images/MOVING/ACTIONS/Back.png","hover": "images/MOVING/ACTIONS/Back hover.png","name": "移動"}]
    $ sys_lm_menu_sound = {"hover": "sound/Effect Sound/System - choose.ogg", "click": "sound/Effect Sound/System - click.ogg"}
    call lm_menu(sys_lm_menu_item, sys_lm_menu_sound, 0, 0.2, 0.2) from _call_lm_menu_367
    $ del sys_lm_menu_item
    $ del sys_lm_menu_sound

    if judge_lm_condition([{ "scope": 0, "content": "_lm_selected_value == \"移動\"" }]):
        jump block_000041E5

    return

label block_00001D37:
    # Node: 00001D37 (Conversation)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_A733FAAD276D4713B00D1C40A5D6F696 "事到如今才问不过，\n宣传用的“YO-I-SA-SHYA”\n到底是什么意思？"

    rs_character_BE51324BF3994D6DAC0D39E0AF888D1E "据说来自“不错的祭典”这句话。"

    window hide

    $ set_window("(標準)")

    return

label block_00001D38:
    # Node: 00001D38 (Target)
    $ set_window("チャット")
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    window show

    rs_character_DB399286619A4AAB9D7D1A2D286772C8 "{color=#0080FF}『用奖品交换他们穿上祭典用装束\n然后请他们参加祭典。』{/color}"

    window hide

    $ set_window("(標準)")

    return

label block_00003284:
    # Node: 00003284 (Character)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_521EB228B90943B3A2B33F87C47D3A0E
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    pause

    hide tag_ED234D4517E14A4EB0C635E1C4B85E12
    hide tag_E12C07C263114A53A918CA2B2E9A063D
    with rs_effect_351A8A667ECF419EB1A052B06E597A01


    return

label block_000031A0:
    # Node: 000031A0 (Stop)
    hide tag_CCB6D21AA43D4C57B10D3D14A711E963
    hide tag_88D3209FDD1D4A2E8369A5A61DF50852
    hide tag_D28A7A2F6DE040DFB581C0284900AF2B
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    jump block_000041F6

    return

label block_000041F6:
    # Node: 000041F6 ()
    $ del F3TalkAfterMainCharacterFinish
    $ del CharacterRandom
    $ del SelectedCharacter
    $ del Items
    $ del IsCharacterAccepted
    $ del CurrentCharacterAccepted
    $ del TalkKobaMinaF3
    $ del TalkSaburoF3
    $ del TalkSakuyaF3
    $ del TalkMatsutaF3
    $ del TalkSatouF3
    $ del TalkShiroYukiF3
    $ del TalkTomoF3
    $ del TalkKatouF3
    $ del TalkItouKimuraF3
    $ del TalkIzumiF3
    $ del TalkTsubasachanF3
    $ del TalkYuuhiF3
    $ del TalkNoriF3
    $ del TalkShinoTsubaF3
    $ del TalkKojimaOkajimaF3

    return
