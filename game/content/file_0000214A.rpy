# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 0000214A (Soundtrack)

init python:
    class SoundtrackPlayer(Action):
        def __init__(self, target_album, target_index, sound_list, playing_info_name):
            self.target_album = target_album
            self.target_index = target_index
            self.sound_list = sound_list
            self.playing_info_name = playing_info_name
        def __call__(self):
            if not (self.get_sensitive() and self.playing_info_name in globals()):
                return
            if self.get_selected():
                return
            renpy.music.stop('soundtrack', 0.2)
            renpy.music.play(self.sound_list[self.target_album]["item"][self.target_index]["path"], 'soundtrack', True)
            globals()[self.playing_info_name] = (self.target_album, self.target_index, renpy.music.get_duration('music'))
            renpy.restart_interaction()
        def get_sensitive(self):
            return self.target_album != None and self.target_index != None
        def get_selected(self):
            if not self.playing_info_name in globals():
                return False
            return self.target_album == globals()[self.playing_info_name][0] and self.target_index == globals()[self.playing_info_name][1]

label soundtrack_prepare:
    show black zorder -100
    with Dissolve(0.5)

    jump block_0000214B

    return

label block_0000214B:
    # Node: 0000214B ()
    $ soundtract_current_album = 4
    $ soundtrack_current_index = 0
    $ soundtrack_playing = (4, 0, 196.04898)
    $ set_place_title(False)

    jump block_0000214C

    return

label block_0000214C:
    # Node: 0000214C (Prepare)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_747C986A971D4B81833D573429A46067
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window hide

    stop music fadeout 2
    $ sys_music_current_file = ""

    $ zorder_tag_747C986A971D4B81833D573429A46067 = 0
    show rs_image_6AA1AE8F26894397B7B7A489DEA85104 as tag_747C986A971D4B81833D573429A46067 at center_bottom zorder zorder_tag_747C986A971D4B81833D573429A46067 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    show rs_image_F64E3FF4BF7646D49B8E5DDD6B6B6E38 as tag_747C986A971D4B81833D573429A46067 zorder zorder_tag_747C986A971D4B81833D573429A46067 onlayer master
    with rs_effect_CDE613D22E9248719DB7B0AA90B2723F

    pause 1

    show rs_image_2F188FD479C04C6B8D3D474C29A22CA4 as tag_747C986A971D4B81833D573429A46067 zorder zorder_tag_747C986A971D4B81833D573429A46067 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    play soundtrack "sound/Piano/sti_gymno_01_pi.ogg" loop

    jump block_00003CA1

    return

label block_00003CA1:
    # Node: 00003CA1 (GenerateList)
    $ sound_list = [{
        "name": _("背景曲"),
        "item": [
            { "name": _("日常 1"), "path": "sound/BGM/Daily 1.ogg" },
            { "name": _("日常 2"), "path": "sound/BGM/Daily 2.ogg" },
            { "name": _("手足无措 1"), "path": "sound/BGM/Flurry 1.ogg" },
            { "name": _("手足无措 2"), "path": "sound/BGM/Flurry 2.ogg" },
            { "name": _("平和 1"), "path": "sound/BGM/Guitar 1.ogg" },
            { "name": _("平和 2"), "path": "sound/BGM/Guitar 2.ogg" },
            { "name": _("奇怪的酒店 1"), "path": "sound/BGM/Hotel 1.ogg" },
            { "name": _("奇怪的酒店 2"), "path": "sound/BGM/Hotel 2.ogg" },
            { "name": _("奇怪的酒店 3"), "path": "sound/BGM/Hotel 3.ogg" },
            { "name": _("见鬼了 1"), "path": "sound/BGM/Monster 1.ogg" },
            { "name": _("见鬼了 2"), "path": "sound/BGM/Monster 2.ogg" },
            { "name": _("朔的洞窟"), "path": "sound/BGM/Nori cave.ogg" },
            { "name": _("无语的想法"), "path": "sound/BGM/Strange idea.ogg" },
            { "name": _("友的房间"), "path": "sound/BGM/Tomo's room.ogg" }
        ]
    }, {
        "name": _("背景曲2"),
        "item": [
            { "name": _("平和的午后"), "path": "sound/BGM/Afternoon.ogg" },
            { "name": _("敌人来袭"), "path": "sound/BGM/Battle.ogg" },
            { "name": _("最终决战"), "path": "sound/BGM/Final battle.ogg" },
            { "name": _("重重疑点"), "path": "sound/BGM/Solve the case.ogg" },
            { "name": _("意料之外的展开"), "path": "sound/BGM/Something comical 1.ogg" },
            { "name": _("微妙的气氛"), "path": "sound/BGM/Something strange 1.ogg" },
            { "name": _("暴风骤雨之前"), "path": "sound/BGM/Something will happen.ogg" },
            { "name": _("感动的始末"), "path": "sound/BGM/The end of touch.ogg" },
            { "name": _("追逐希望"), "path": "sound/BGM/The hope.ogg" },
            { "name": _("面向未来"), "path": "sound/BGM/To the future.ogg" },
            { "name": _("过去的宝物"), "path": "sound/BGM/My precious time - piano.ogg" },
            { "name": _("过去的宝物……"), "path": "sound/BGM/My precious time.ogg" },
            { "name": _("珍重的时光"), "path": "sound/BGM/My precious time - slowly.ogg" },
            { "name": _("久远回忆"), "path": "sound/BGM/The past precious.ogg" },
            { "name": _("面向未来之前"), "path": "sound/BGM/My precious time of now.ogg" },
            { "name": _("无比珍贵的现在"), "path": "sound/BGM/My precious time of now - piano.ogg" }
        ]
    }, {
        "name": _("背景曲3"),
        "item": [
            { "name": _("Don't be afraid!!"), "path": "sound/BGM/Theme/Schoolboys Theme - Dont be afraid!!.ogg" },
            { "name": _("Don't be afraid!! （伴奏）"), "path": "sound/BGM/Theme/Schoolboys Theme - Dont be afraid!! (Instrument).ogg" },
            { "name": _("愛を賭けて"), "path": "sound/BGM/Theme/Schoolboys Theme - Bet of Love.ogg" },
            { "name": _("第一章节"), "path": "sound/BGM/Chapter 1.ogg" },
            { "name": _("第二章节"), "path": "sound/BGM/Chapter 2.ogg" },
            { "name": _("第三章节"), "path": "sound/BGM/Chapter 3.ogg" },
            { "name": _("Csikos Post"), "path": "sound/BGM/Celemony.ogg" },
            { "name": _("Vltava"), "path": "sound/BGM/Slowly time.ogg" },
            { "name": _("赤峰兄弟的训练"), "path": "sound/BGM/Series - Akamine brothers.ogg" },
            { "name": _("起点"), "path": "sound/BGM/Start scene.ogg" },
            { "name": _("充满朝气的夕阳下"), "path": "sound/BGM/Lively twilight.ogg" },
            { "name": _("英雄登场"), "path": "sound/BGM/Stage of HERO.ogg" },
            { "name": _("英雄末路"), "path": "sound/BGM/Drama.ogg" },
            { "name": _("御咲花车祭！"), "path": "sound/BGM/Drum.ogg" },
            { "name": _("漫才开始"), "path": "sound/BGM/Manzai.ogg" },
            { "name": _("天使与恶魔"), "path": "sound/BGM/Angel and Demon.ogg" },
            { "name": _("Ailurus fulgens"), "path": "sound/BGM/Ailurus fulgens.ogg" },
            { "name": _("寂静之夜"), "path": "sound/BGM/Night.ogg" },
            { "name": _("宝物~卒業の春~"), "path": "sound/BGM/Treasure-Spring-of-Graduate.ogg" }
        ]
    }, {
        "name": _("主题曲"),
        "item": [
            { "name": _("森海友 1"), "path": "sound/BGM/Theme/Schoolboys Theme - Tomo 1.ogg" },
            { "name": _("森海友 2"), "path": "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg" },
            { "name": _("森海友 3"), "path": "sound/BGM/Theme/Schoolboys Theme - Tomo 3.ogg" },
            { "name": _("一之濑翼"), "path": "sound/BGM/Theme/Schoolboys Theme - Tsubasa.ogg" },
            { "name": _("赤峰兄弟 1"), "path": "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 1.ogg" },
            { "name": _("赤峰兄弟 2"), "path": "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg" },
            { "name": _("赤峰兄弟 3"), "path": "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 3.ogg" },
            { "name": _("奥村慎太郎"), "path": "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg" },
            { "name": _("猫山三朗"), "path": "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg" },
            { "name": _("友和忍"), "path": "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg" },
            { "name": _("作哉与翼"), "path": "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg" },
            { "name": _("木村与伊藤"), "path": "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg" },
            { "name": _("九尾 1"), "path": "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg" },
            { "name": _("九尾 2"), "path": "sound/BGM/Theme/Schoolboys Theme - Kyubi 2.ogg" },
            { "name": _("九尾 3"), "path": "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg" },
            { "name": _("朔"), "path": "sound/BGM/Theme/Schoolboys Theme - Nori.ogg" },

        ]
    }, {
        "name": _("钢琴曲"),
        "item": [
            { "name": _("Gymnopédie"), "path": "sound/Piano/sti_gymno_01_pi.ogg" },
            { "name": _("La campanella"), "path": "sound/Piano/rst_lacam_pi.ogg" },
            { "name": _("Le Tombeau de Couperin"), "path": "sound/Piano/rvl_prelude_pi.ogg" },
            { "name": _("Sonata Pathétique"), "path": "sound/Piano/btb_hisou_2_pi.ogg" },
            { "name": _("Heroic Symphony"), "path": "sound/Piano/hero.ogg" }
        ]
    }]

    jump block_00003CA0

    return

label block_00003CA0:
    # Node: 00003CA0 (Update)
    call screen soundtrack(sound_list)

    jump block_00003C95

    return

screen soundtrack(sound_list):
    frame:
        style "soundtrack_frame"
        area (5, 60, 230, 530)
        has viewport:
            mousewheel "change"
            draggable True
            side_yfill True

        use soundtrack_content(sound_list, soundtract_current_album, soundtrack_playing)
    hbox:
        style "soundtrack_album"
        for i, album in enumerate(sound_list):
            textbutton album["name"]:
                text_style "soundtrack_album_button_text"
                action VariableTracker(i, "soundtract_current_album")
    text "♫ " + __(sound_list[soundtrack_playing[0]]["name"]) + " - " + __(sound_list[soundtrack_playing[0]]["item"][soundtrack_playing[1]]["name"]):
        style "soundtrack_status_text"
    textbutton _("返回"):
        xpos 700
        ypos 10
        text_style "soundtrack_album_button_text"
        action Return("")

screen soundtrack_content(sound_list, album_index, track_info):
    vbox:
        for i, soundtrack in enumerate(sound_list[album_index]["item"]):
            textbutton sound_list[album_index]["item"][i]["name"]:
                style "soundtrack_content_item"
                action SoundtrackPlayer(album_index, i, sound_list, "soundtrack_playing")

style soundtrack_status_intro:
    xpos 258
    ypos 450
    size 18
    color "#FFFFFF"
style soundtrack_status_text:
    xpos 425
    ypos 71
    size 16
    color "#FFFFFF"
style soundtrack_frame is default
style soundtrack_album:
    xpos 16
    ypos 10
style soundtrack_album_button_text:
    color "#FFFFFF"
    font "font/zcool-happy-ayumi-extended.ttf"
    outlines [(absolute(6), "#2D6BA500", absolute(0), absolute(0)),
              (absolute(4), "#2D6BA588", absolute(0), absolute(0)),
              (absolute(2), "#2D6BA5FF", absolute(0), absolute(0))]
    selected_color "#2D6BA5"
    selected_outlines [(absolute(6), "#FFFFFF00", absolute(0), absolute(0)),
                       (absolute(4), "#FFFFFF88", absolute(0), absolute(0)),
                       (absolute(2), "#FFFFFFFF", absolute(0), absolute(0))]
    hover_color "#2D6BA5"
    hover_outlines [(absolute(6), "#FFFFFF00", absolute(0), absolute(0)),
                    (absolute(4), "#FFFFFF88", absolute(0), absolute(0)),
                    (absolute(2), "#FFFFFFFF", absolute(0), absolute(0))]
style soundtrack_content_item:
    ymargin 5
style soundtrack_content_item_text:
    color "#2D6BA5"
    font "font/source-hans-sans-medium.ttc"
    size 16
    outlines [(absolute(6), "#FFFFFF00", absolute(0), absolute(0)),
              (absolute(4), "#FFFFFF88", absolute(0), absolute(0)),
              (absolute(2), "#FFFFFFFF", absolute(0), absolute(0))]
    selected_color "#FFFFFF"
    selected_outlines [(absolute(6), "#2D6BA500", absolute(0), absolute(0)),
                       (absolute(4), "#2D6BA588", absolute(0), absolute(0)),
                       (absolute(2), "#2D6BA5FF", absolute(0), absolute(0))]
    hover_color "#FFFFFF"
    hover_outlines [(absolute(6), "#2D6BA500", absolute(0), absolute(0)),
                    (absolute(4), "#2D6BA588", absolute(0), absolute(0)),
                    (absolute(2), "#2D6BA5FF", absolute(0), absolute(0))]

transform soundtrack_progressbar(duration):
    xpos 413
    ypos 66
    parallel:
        xzoom 0.0
        linear duration xzoom 1.0
        repeat

label block_00003C95:
    # Node: 00003C95 (CLEAR)
    hide tag_747C986A971D4B81833D573429A46067
    hide tag_E6300DB69D254C278710366E7D300298
    hide tag_C6F01EC8F88A4AB093352F6D3F68197C
    hide tag_30A510E5705C4015819C44CDD628028A
    hide tag_7E30B19D592346FAA1C3C3A0E82D602F
    hide tag_83794CD575404B2B99772C15549BE0B7
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    stop soundtrack fadeout 0.5
    $ sys_music_current_file = ""

    jump block_00003C96

    return

label block_00003C96:
    # Node: 00003C96 ()
    $ del soundtract_current_album
    $ del soundtrack_current_index

    return
