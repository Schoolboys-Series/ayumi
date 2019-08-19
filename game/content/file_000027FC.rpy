# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 000027FC (慎太郎筆記)

screen shintarou_notebook:
    fixed at shintarou_notebook_screen:
        default current_page = 1
        default current_character = None
        add "images/Shintaro-notebook/Background.png"
        $ character_list = filter(lambda x: x["id"] in [
            "Tomo", "Shinobu", "Shintarou", "Tsuki", "Sora", "Tsubasa", "Sakuya", "Saburou", "Shirou", "Yukio",
            "Tsubasa-chan", "Nameko", "Itou", "Kimura", "Katou", "Matsuda", "Izumi",
            "Satou", "Okajima", "Kojima"], character_full_info)
        if C3S1 == True:
            $ character_list.extend(filter(lambda x: x["id"] in ["Kiyo", "Nakayama", "Okajima-senior", "Nakayama-senior"], character_full_info))
        if Chapter > 1:
            $ character_list.extend(filter(lambda x: x["id"] in ["Yuuhi", "Nori", "Mamoru"], character_full_info))
        if C2S6 == True:
            $ character_list.extend(filter(lambda x: x["id"] in ["Kai", "Tentacle-earthworm", "Tentacle-starfish", "Tour-guide"], character_full_info))
        if C3S5 == True:
            $ character_list.extend(filter(lambda x: x["id"] in ["MonsterA", "MonsterB", "MonsterC"], character_full_info))
        if C2S6 == True or C3S5 == True:
            $ character_list.extend(filter(lambda x: x["id"]  == "Dark lesser", character_full_info))
        $ character_list.extend(filter(lambda x: x["id"]  == "Tokiwa", character_full_info))
        if C1S4 == True:
            $ character_list.extend(filter(lambda x: x["id"]  == "Tsubasa-chan (Human)", character_full_info))
        if C1S4 == True or Chapter > 1:
            $ character_list.extend(filter(lambda x: x["id"]  in ["Kobayashi", "Minami", "Sugimoto", "Rikuta", "Shougintoki"], character_full_info))
        if C3S1 == True:
            $ character_list.extend(filter(lambda x: x["id"]  == "Shouhei", character_full_info))
        if C2S5 == True:
            $ character_list.extend(filter(lambda x: x["id"]  == "Kyuubi", character_full_info))
        if C1SG1 and C1SG2 and C2SG1 and C2SG2 and C3SG1 and C3SG2:
            $ character_list.extend(filter(lambda x: x["id"]  in ["Sakase", "Be--", "He--"], character_full_info))
        frame:
            style "shintarou_notebook_character_list"
            has viewport:
                mousewheel "change"
                draggable True
                side_yfill True
            vbox:
                null height 20
                for character in character_list:
                    textbutton character["name"]:
                        xpos 30
                        style "shintarou_notebook_character_name"
                        action [Play("menu_effect", "sound/Effect Sound/Paper 1.ogg"), SetScreenVariable("current_character", character)]
                null height 20
        if current_character != None:
            $ y_pos = 44
            for i in range(1, 3):
                if current_page == i:
                    add "images/Shintaro-notebook/bage opened.png" xpos 714 ypos y_pos
                    text str(i):
                        xpos 727
                        ypos y_pos + 20
                        style "shintarou_notebook_page_text_active"
                else:
                    add "images/Shintaro-notebook/bage.png" xpos 714 ypos y_pos
                    textbutton str(i):
                        xpos 727
                        ypos y_pos + 20
                        style "shintarou_notebook_page_text"
                        action [Play("menu_effect", "sound/Effect Sound/Paper 1.ogg"), SetScreenVariable("current_page", i)]
                $ y_pos += 108
            $ del y_pos
            if current_page == 1:
                use shintarou_notebook_content(find_chatracter_version(current_character))
            elif current_page == 2:
                use shintarou_notebook_content2(find_chatracter_version(current_character))
        textbutton "×" style "shintarou_notebook_close_button" action [Pause(0.3), Return()]

screen shintarou_notebook_content(character):
    add ("images/Shintaro-notebook/Content/" + character["id"] + ".png") xpos -51
    text character["name"] at Transform(xpos=260, ypos=23) style "shintarou_notebook_content_name"
    $ shintarou_notebook_content_param = ""
    if "age" in character:
        $ shintarou_notebook_content_param += __("年龄：") + __(character["age"]) + "\n"
    if "height" in character:
        $ shintarou_notebook_content_param += __("身高：") + __(character["height"]) + "\n"
    if "weight" in character:
        $ shintarou_notebook_content_param += __("体重：") + __(character["weight"]) + "\n"
    if "birthdate" in character:
        $ shintarou_notebook_content_param += __("生日：") + __(character["birthdate"]) + "\n"
    if "blood" in character:
        $ shintarou_notebook_content_param += __("血型：") + __(character["blood"]) + "\n"
    if "club" in character:
        $ shintarou_notebook_content_param += __("所属：") + __(character["club"]) + "\n"
    if "pants" in character:
        $ shintarou_notebook_content_param += __("内裤类型：") + __(character["pants"]) + "\n"
    text shintarou_notebook_content_param at Transform(xpos=240, ypos=98) style "shintarou_notebook_content_content"
    $ del shintarou_notebook_content_param
    text character["description"] at Transform(xpos=240, ypos=332) style "shintarou_notebook_content_content"
    for addon in character["addons"]:
        text addon["content"] at addon["transform"] style "shintarou_notebook_content_addon"

screen shintarou_notebook_content2(character):
    add ("images/Shintaro-notebook/Background/" + character["id"] + ".png") xpos -51
    text _("主要出场记录") at Transform(xpos=230, ypos=5) style "shintarou_notebook_content_content"
    text character["name"] at Transform(xpos=260, ypos=30) style "shintarou_notebook_content_name"
    default has_record = False
    frame:
        style "shintarou_notebook_content2_container"
        has viewport:
            mousewheel "change"
            draggable True
            side_yfill True
        vbox:
            for chapter in character["appearances"]:
                if len(chapter) > 0:
                    null height 10
                    for story in chapter:
                        $ has_record = True
                        if eval(story + " == True"):
                            text "√ " + __(scene_var_description[story]) style "shintarou_notebook_content2_achieved"
                        else:
                            text "… " + __(scene_var_description[story]) style "shintarou_notebook_content2_unfinished"
            if has_record == False:
                text _("没有记录") style "shintarou_notebook_content2_unfinished"
            null height 20

transform shintarou_notebook_screen:
    on show:
        alpha 0
        ypos 100
        easein 0.3 ypos 0 alpha 1
    on hide:
        easeout 0.3 ypos 100 alpha 0
style shintarou_notebook_close_button:
    xanchor 1.0
    yanchor 1.0
    xpos 790
    ypos 590
    font "font/source-hans-sans-heavy.ttc"
style shintarou_notebook_close_button_text:
    size 40
    color "#808080"
    hover_color "#000000"
    outlines [(absolute(1), "#222222FF", absolute(0), absolute(0)),
              (absolute(2), "#222222CC", absolute(0), absolute(0)),
              (absolute(3), "#22222288", absolute(0), absolute(0)),
              (absolute(4), "#22222244", absolute(0), absolute(0)),
              (absolute(5), "#22222200", absolute(0), absolute(0))]
style shintarou_notebook_page_text_active:
    size 36
    color "#459F91"
style shintarou_notebook_page_text_text:
    size 36
    color "#000000"
    hover_color "#459F91"
style shintarou_notebook_character_list is default
style shintarou_notebook_character_name:
    ymargin 10
style shintarou_notebook_character_name_text:
    size 24
    color "#000000"
    hover_color "#459F91"
    selected_color "#459F91"
    font "font/zcool-happy-ayumi-extended.ttf"
style shintarou_notebook_content_name:
    font "font/zcool-happy-ayumi-extended.ttf"
    color "#000000"
    size 60
    outlines [(absolute(1), "#FFFFFFFF", absolute(0), absolute(0)),
              (absolute(2), "#FFFFFFCC", absolute(0), absolute(0)),
              (absolute(3), "#FFFFFF88", absolute(0), absolute(0)),
              (absolute(4), "#FFFFFF44", absolute(0), absolute(0)),
              (absolute(5), "#FFFFFF00", absolute(0), absolute(0))]
style shintarou_notebook_content_content:
    font "font/zcool-happy-ayumi-extended.ttf"
    color "#000000"
    size 20
    line_spacing 11
    outlines [(absolute(1), "#FFFFFFFF", absolute(0), absolute(0)),
              (absolute(2), "#FFFFFFCC", absolute(0), absolute(0)),
              (absolute(3), "#FFFFFF88", absolute(0), absolute(0)),
              (absolute(4), "#FFFFFF44", absolute(0), absolute(0)),
              (absolute(5), "#FFFFFF00", absolute(0), absolute(0))]
style shintarou_notebook_content_addon:
    font "font/zcool-happy-ayumi-extended.ttf"
    color "#FF0000"
    size 18
    outlines [(absolute(1), "#FFFFFFFF", absolute(0), absolute(0)),
              (absolute(2), "#FFFFFFCC", absolute(0), absolute(0)),
              (absolute(3), "#FFFFFF88", absolute(0), absolute(0)),
              (absolute(4), "#FFFFFF44", absolute(0), absolute(0)),
              (absolute(5), "#FFFFFF00", absolute(0), absolute(0))]
style shintarou_notebook_content2_container is default:
    ysize 500
    xpos 240
    ypos 100
style shintarou_notebook_content2_achieved:
    size 18
    color "#459F91"
    font "font/zcool-happy-ayumi-extended.ttf"
style shintarou_notebook_content2_unfinished:
    size 18
    color "#808080"
    font "font/zcool-happy-ayumi-extended.ttf"
