# Pre-defined colors
image black = Solid("#000000")
image white = Solid("#FFFFFF")
image color_primary = Solid("#00B3C7")

init python:
    # import time 会在6.X最后一个版本导致无法存档。7.X未知。
    # Help function
    def split(arr, size):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr = arr[size:]
        arrs.append(arr)
        return arrs
    # Gallery
    gallery_list = [
        (_("序章"), [
            "8311E1236AED463A9358E6303D1D2F5C",
            "84E3A40E55C74C5C9B705CF5E3FE58A1",
            "87A38905C919455BB6D35DB596394AC9",
            "691F32B0298245DE8278009B3F9589BE",
            "03C9EB10B8D14965A3E4A9225ACC9C39"
        ]),
        (_("第一章"), [
            "D8229CDD6C214636928DC6C6FCFCA4FB",
            "9ACE399648824FD884F39266417CDDBD",
            "1C9982B11CB6440DBBEE2B161A425C30",
            "5BAF87FE15234238AB0865FE6CEABB74",
            "18A77FEE59614E49AA0660833A369388",
            "83F732F048574A3294F4B648F4D0DFC8",
            "EAE467ED476446099F36A59024BEB550",
            "1DF1A98336DB4A81BE40028C743F7DF8",
            "DF4B118410C548ADBD1EA7899F30BCCF",
            "2F3A55DB5E7D426AA2695C5D1B97A040",
            "361696A1939D46CEBF91C8115642936C",
            "BB15BC7CC853407495EB41EE25D1EFAD",
            "A1E7CA7F049F49908469DC30E836FCEF",
            "2B9BE937603E4E96969F3C4CE130A6F5",
            "689A15BAED4D45EAA7879993C605248F",
            "18084E9C14F5421BBBB3CA4F07A82DC8",
            "CCAF353B743A4E13A7A43D3F8AF8D694",
            "287157BDD64B4E528AFF869F71BDA5A9",
            "68F095DA988D4FBD93381898FF8260F4",
            "85CAF3695FEF4F89962FCAB11752108F",
            "7B83AD9CA240425EA3A9E06C0D24BF7B",
            "B4FB83ADF72E4DEDA77384FEB0F94E44",
            "9363768CD32C4FE78E30EB697E142B70",
            "D704FBCAA179433EB76BAC3007A3C241",
            "5E80ED9C3E1F4920A274B420F13A4D82",
            "C7F946EF0FB14A6A9ED6F7A9D18C5E2B",
            "A222B7CC30A245E0AB1F1A5B1FC13CC5",
            "BB4914B9F99F4B449F1BD45034C67186",
            "A438304BAD244787B1FCBDEB053ED1B2",
            "ADFD6891D3AF42CA8301DDC64AE2F5D7",
            "0F106B8E35274818A2D1764D5EC4CEFF",
            "CEDACC94A9174ACEBB28422618EB83AD",
            "709A0F8E88FC4927B3F2872F13C17FA7",
            "D9D9BBF18FFA4E278F5E7FF9A7D00AF2",
            "7C1396F883A044398410DB50945F5D1D",
            "AC590944081A4E0C9EC81899E9209C85",
            "F7C5F4C539224DA08E60CF859D14D0B7",
            "E05FE25C588740B4A48960064ACFC99B",
            "DE8A835C2AC6467EB4456D8DEFA396B3",
            "267F041B536640EA86097324E1BF5809",
            "1A1E430526B94BB68A38F9C6A6CE9B8C",
            "8A9A9C995593446F8C7F1623E032EB67",
            "D9FF8323B07F4CB09838C9DC0E934C20",
            "B4E4E5696DB74835907C35BB91F9BD19",
            "85BB53EF8F764B8998C0F67FF475E7E5"
        ]),
        (_("第二章"), [
            "C5CDC0061BA04DD3AD28D4ABCC1A8876",
            "0FD0B77AE6184E9E8876D49DA2E6D501",
            "38144AA40B6D4C3B8F05376BD7FBBF73",
            "1AF095ACDA634CDB97AA0E1F9C729EAB",
            "A591B65F951C4384B441DD43899ACCFB",
            "84F29D2D29E0455A8600FFB3594BAF7F",
            "0E19376156254FCF92845E2C1706AA05",
            "9593E8C30A6D41789E064CE4E2E05E2E",
            "DE58EA8B26934BF59A0AABA095CABDBB",
            "E132C3CC6E324B62A79DA01BE75B90C8",
            "6A16110F14C64AA89B2FAD22D32413C7",
            "821554C146A04ADF85F552B16E7C73A1",
            "03FE1F27E00741CCAF415509C1FF7783",
            "ECECD9655F024DD9ABD97ABDC960DC82",
            "4D6DF38872224876B0346DDC8236880E",
            "B6A08DC7BC7B43CA9586AF3377BA9930",
            "3D4DEC86BCC44FEC9C0353067818153E",
            "10467CBD22854ED498CC690F9E3ABF68",
            "772ED68CBCDA4539B968C3D37984A791",
            "849CEB1C756A40EC9091CD060431DA06",
            "7D1E6CD76A3F4377B4251D3865FE5B7C",
            "9CFDDCA65C8A45049A67D61DA2BEBB7B",
            "335BF89B88F641B8B8DB66BE58875FEA",
            "A3F0B5B71ACF44378505551EAB95D2D5",
            "61A27D51005E46C3BB478FEE8106B863",
            "1C2DDB742E8E4804A215E5C68FF7CBFE",
            "CAB89628D892438290F5EEAEE6FDA3AE",
            "E4328112D39C4B68A1C267CCCE49C938",
            "C514C7B43BB94588B7E6F6DE0405902C",
            "17EE1054E0774C6E887A51B6D6F9809F",
            "B23B20310413456B97F5A62F21EB8231",
            "1DB63445D5FA4A8F90EE59842CB17587",
            "63D04BFE31F74541BAC4E3BE874F04D4",
            "01A535C9B5DB4CB99B85DD6BAC669F41",
            "4BE6749A7DEF47B28C893ED7AEE021E1",
            "63048BA95B7241CCA1206E32EEB5617C",
            "E8909DD316534842888A95088CBFE945",
            "B5626DFE23C0455A8A9CD7A2A8AA44A0",
            "5CF2995690BF4C87A419E7A4AD05A94D",
            "3BA596B22A77484494505809CFB86D73",
            "2B2468BBF68040D7AA817B022CDE842D",
            "986D6DD667574B1D83ECEA3AF755AFA3",
            "52CC474C78C944CABB132D3C2D0EA6A8",
            "C533C9DBA54D4CAFAD4F08DA43EB9A55",
            "9C54D280900F4385BDFF754A33B420AF",
            "3B43238981B5446E810F4A35352A9D94",
            "E99D8EE889324E538179D61E6C5B1FC7",
            "D5131E3A10814E4FB5007D75587FC94C",
            "AB1B0D4593B3493595C05D2634542B0F",
            "99E537CF1D264E8A9DC364659ADA92B3",
            "6416585972644DE1BFEFE64812811D22",
            "95153E5DF032453584ADEE5B712511FC",
            "7069267F64E54B868A5050EEF9D93A3B",
            "B370E5346ABB47548DAE9D421086387D",
            "9799A75AC32E46DBB98AC1FC4E281CC9",
            "8D8A506E039845CD89579B536CAB6E35",
            "6C20080978734302A13DBD9F5C977D8A",
            "9E2ECBA71A44401F9A87C7DF41500965",
            "ACC7BF001A154359B4A9C008A8F9B628",
            "3D10951C06114AB5A589638B31BA9888",
            "96F52A116B95488881F36C7B55C08BD0",
            "B6DB788D29BB4DFCBACCD696EA1D68EC"
        ]),
        (_("第三章和学期末"), [
            "F8ABD783506148DE8982E63A2D047172",
            "C8A84981806B4A4DB2B6D92C97AE2032",
            "AD7961BC76E643599E9C50754D2B16E3",
            "B254F70E32264E79AF406C3492347538",
            "8C10B311F1B241F380A70CA461F73E5E",
            "6074209F6E654F3580E90BD8FE1A21C8",
            "2D24925D8776427E806125699BD065DE",
            "0BF98EB1ECCB4B0E884CBC033AC9F50E",
            "E34446EB077F4A6EA9497B9B9B0733FE",
            "08883BD8FCE34314B854783E9E919F7A",
            "26575D16067F4A9DA889C346CBB487A8",
            "54C31AC2FA71447087DF924311BF70EC",
            "6BDC463AF3034115B872FE8114549896",
            "9C8D732DF7E24E7F953E682C4348EA0A",
            "A53B45F08CC449B5B3975CB5C5C64EF0",
            "63D435C006354C2BA34CDE707A2F5EB7",
            "8F1E01956CF44C7A87C37EDFB685642E",
            "7E57D7A3B6704964B8907157D0B72E75",
            "97433B7ED6534086BEE73738CC688FD8",
            "A43CCBE3B95A40109DF2A73F21CB816A",
            "8C98F73227E949DAA5A09717C8CF0B1E",
            "78B0CFBCE4A74EB9819E36549647B400",
            "CD0D0A6DE097468A89BF35159754AED4",
            "8DBB09A70C0A416DAE3322BBA30B3080",
            "F01836A52D714D4AB57BB88A94C85343",
            "1280E1FE84AF4802A866EF6180931523",
            "6D983F1C2CBA4EB8AE6EE83BDA57FCC1",
            "1AB3B872D6C54A87BBE10747A2C3FDAD",
            "21F6C31513A34EA8A8B2E622273CDD7F",
            "B5CABC467ECD46948E0B1292E589A60D",
            "344471F6EC6A4D92B3E3A4F9A0C4F5E8",
            "4253E3A8DC4C43E586A3DDBA53A4A6AF",
            "9C292825A57E4A5E85C7B9686E18FC48",
            "E3E0C745F8D941F395EB7D2B8486A4E6",
            "E1907497859B4E81BC4C4AEAC7E61C43",
            "7469B14A83B44907A5986CD48A25A5EC",
            "45E6DC2D2D414F33A0305654A6FC0BE9",
            "48B08BE8EC9F4E278E32DF739320F0D9",
            "61D8FFFC34E4460B9E6EAB78BB0388BC",
            "111AB42F949B4430BA74B6ADE590935E",
            "4C2D5276FCBB40F0B0DEB04A3E2EC3B5",
            "4D24DED204CD42949FB326EEF358987F",
            "03063425963043719D0E021E3257FDBB",
            "44D20D14619C4C49BA2A44119906A340",
            "4D66E39D4F0541B297D6075145C4D09A",
            "67BB6AD80CAE4374A5BE1811B7D7D1D5",
            "9B3BE1450BA84524B154AAD914462F24",
            "29E9A807D6B148168EEACEB2EA7D0A5E",
            "41428618BA4343D9B122066AD821CA68",
            "8FD417243BAF49B6840F3190C65AA4E5",
            "4C236CF15FAB471C978461AE1AFB0117",
            "C57B8F2A70644733BB36E8DA3C8F5B9A",
            "82C2A7F9AB474FB6AA0C71F77E91070C",
            "793A50EA5F1D4DD095383254ED6D5645",
            "11538F8AB5634131B83013199E04FF74",
            "692431208FC84C2BBC4BFB384C5535E2",
            "3B270FDC9BBD4F209FD7C52684B74402",
            "C95DA2C7DAF24261815104970FA26629",
            "9AB5FF9008204534A8731A5EAC18119E",
            "BB04FC5B2E1E42B7B836B5E2E24DAB6A",
            "D8781686D9AC4CE7B6A0E90C3986C44F"
        ]),
        (_("野球拳"), [
            "C93E3A8AE8DA46FA8F4E3883F10E4A0A",
            "C8CDD0393EE8457FAB6E6746ACFC16B4",
            "C66C10E625D1487C81DE82A7A6963CE1",
            "05A1F8B8E2FC4BF48EEB4DCDD2746CEC",
            "C1CF19D2F51147BEA158A4A080C53E8E",
            "82FBA261F8B743E2B7905761A51E8130",
            "8FE737664EDE4EC7B0E8209B406F0C83",
            "8914D7D41D88433BA466B30E72553022",
            "F07581615155432B859CC7C4EA5BB50A",
            "77ADCB3F3FFE4790ACF1CFA1B370D10E",
            "E9A663366FCD424F80AA4C9F0F50B783",
            "F232B64B26E9462499506723A75A2478",
            "F0B942BCF3F345D994A483AC7B298635",
            "7807C68AFE0D45CA9679A08B5635D87F",
            "9F56029B7C3B4A9A846CEBD0C4ABA9F6",
            "66A4E0F049264A14B7EC2B8586906585",
            "4FFF4D5081EF48C48C56351B30912D0D",
            "45595CAD90274C6792ED17A5D287AC73",
            "2ADB5978CA224AD0BEA156342BF3B5F0",
            "723D3AF7D5734BC090560585CEA18788",
            "AB78B916A99943F290C5E252F0284D9D",
            "557C98C111E1428CA41D02A69E29F441",
            "3EF7CB15BDBB46C7AF82217340EF373E",
            "A5A554C6B21A43F2A81B32E021B450ED",
            "8CCEE6A27E144B12B85D173D15807073",
            "E67627BC64024DDDB7016189C04834C4",
            "84D27BCD9A7D4F1FB7C4FE3B768FE94A",
            "DE11F75619AE4D088BE99CB4C2F9194D",
            "1588B519213A4B2192BA12D75A93925E",
            "A4A48A6A524F416482A347C3E239F9E5"
        ])
    ]
    gallery = AdvancedGallery()
    gallery.transition = Dissolve(0.3)
    persistent.gallery_total_count = 0
    for i, chapter in enumerate(gallery_list):
        for picture in chapter[1]:
            gallery.button("rs_image_" + picture)
            gallery.unlock_image("rs_image_" + picture)
            persistent.gallery_total_count += 1
    persistent.gallery_page = gallery_list[0][0]

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language
style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False
style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True
style gui_text:
    properties gui.text_properties("interface")
style button:
    properties gui.button_properties("button")
style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
style prompt_text is gui_text:
    properties gui.text_properties("prompt")
style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################

## Gallery screen ##############################################################
##
## Gallery is a screen that provide function for player to view all available
## CGs if they had already viewed the CG in game.

screen gallery():
    tag menu

    add "gui/gallery_background.png"
    frame:
        style "gallery_frame"
        area (0, 75, 800, 450)
        has viewport:
            mousewheel True
            draggable True
            side_yfill True

        use gallery_content(persistent.gallery_page)
    hbox:
        style_prefix "gallery_chapter"
        $ persistent.gallery_available_count = 0
        for i, chapter in enumerate(gallery_list):
            textbutton chapter[0] action CurrentGalleryPage(chapter[0])
            for picture in chapter[1]:
                if gallery.IsUnlocked("rs_image_" + picture):
                    $ persistent.gallery_available_count += 1
    textbutton _("返回"):
        style "gallery_button_return"
        action Return()
    text ("%d / %d" % (persistent.gallery_available_count, persistent.gallery_total_count)):
        style "gallery_button_count"

style gallery_chapter_hbox:
    xalign 0.5
    ypos 550
style gallery_chapter_button_text:
    color "#FFFFFF"
    outlines [(absolute(6), "#FF808000", absolute(0), absolute(0)),
              (absolute(4), "#FF808088", absolute(0), absolute(0)),
              (absolute(2), "#FF8080FF", absolute(0), absolute(0))]
    selected_color "#FF8080"
    selected_outlines [(absolute(6), "#FFFFFF00", absolute(0), absolute(0)),
                       (absolute(4), "#FFFFFF88", absolute(0), absolute(0)),
                       (absolute(2), "#FFFFFFFF", absolute(0), absolute(0))]
    hover_color "#FF8080"
    hover_outlines [(absolute(6), "#FFFFFF00", absolute(0), absolute(0)),
                    (absolute(4), "#FFFFFF88", absolute(0), absolute(0)),
                    (absolute(2), "#FFFFFFFF", absolute(0), absolute(0))]
style gallery_frame is empty
style gallery_button_return:
    xpos 700
    ypos 10
style gallery_button_count:
    size 30
    ypos 15
    xpos 10
    color "#FFFFFF"
    font "font/zcool-happy-ayumi-extended.ttf"
style gallery_button_return_text:
    size 30
    color "#FFFFFF"
    font "font/zcool-happy-ayumi-extended.ttf"
    outlines [(absolute(10), "#FF808000", absolute(0), absolute(0)),
              (absolute(8), "#FF808044", absolute(0), absolute(0)),
              (absolute(6), "#FF808088", absolute(0), absolute(0)),
              (absolute(4), "#FF8080BB", absolute(0), absolute(0)),
              (absolute(2), "#FF8080FF", absolute(0), absolute(0))]

    hover_color "#FF8080"
    hover_outlines [(absolute(10), "#FFFFFF00", absolute(0), absolute(0)),
                    (absolute(8), "#FFFFFF44", absolute(0), absolute(0)),
                    (absolute(6), "#FFFFFF88", absolute(0), absolute(0)),
                    (absolute(4), "#FFFFFFBB", absolute(0), absolute(0)),
                    (absolute(2), "#FFFFFFFF", absolute(0), absolute(0))]

screen gallery_content(target_chapter):
    vpgrid:
        cols 5
        draggable True
        mousewheel True
        scrollbars None
        style_prefix "gallery_content_hbox"
        for i, chapter in enumerate(gallery_list):
            if chapter[0] == target_chapter:
                for picture in chapter[1]:
                    if gallery.IsUnlocked("rs_image_" + picture):
                        button:
                            style "gallery_content_hbox_button"
                            add "rs_image_" + picture size (130, 97)
                            action gallery.Action("rs_image_" + picture)
                    else:
                        imagebutton:
                            idle Solid(gui.idle_small_color)
                            style "gallery_content_hbox_button"

style gallery_content_hbox_vpgrid:
    xminimum 800
    xpos 0
style gallery_content_hbox_button:
    maximum (150, 117)
    minimum (150, 117)
    margin (30, 10, 30, 10)
style gallery_content_hbox_image_button:
    maximum (150, 117)
    minimum (150, 117)
    margin (30, 10, 30, 10)

## Click to continue screen ####################################################
##
## The click to continue scrren is used to display an indicator to the player to
## tell them that they can click the screen to go to next part of dialog or
## just continue the game.
##
## https://www.renpy.org/doc/html/screen_special.html#ctc-click-to-continue

screen ctc():
    zorder 100

    image anim.Filmstrip("gui/next_indicator.png", (31, 29), (2, 1), 0.3, style="ctc")

style ctc:
    pos (0, 0)
    anchor (0, 0)

## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        style "window"

        if who is not None:
            window:
                style "namebox"
                text who id "who"
        text what id "what"
        if "sys_dialogue_show_actions" in globals() and globals()["sys_dialogue_show_actions"] == True:
            hbox:
                style "say_actions"
                imagebutton:
                    idle "gui/menu_button.png"
                    hover "gui/menu_button hover.png"
                    action ShowMenu("save")

style window is default
style namebox is default
style namebox_label is say_label
style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding
style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
style say_actions:
    xalign 1.0
    yalign 0.05
    spacing 15

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    frame:
        style "input_conatiner"
        vbox:
            xalign 0.5
            yalign 0.5
            text prompt style "input_prompt"
            input id "input"

style input_conatiner is default:
    xalign 0.5
    xsize 371
    ysize 156
    ypos 300
    background Image("gui/frame.png")
style input_conatiner:
    variant "small"
    ypos 50
style input_prompt is default:
    xalign 0.5
style input:
    xalign 0.5
    size 30

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i action Return(i)

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text
style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5
    spacing gui.choice_spacing
style choice_button is default:
    properties gui.button_properties("choice_button")
style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

image main_bg_movie = Movie(channel="movie_main", play="movie/main_bg.mpg", size=(800, 600))

screen main_menu():
    tag menu
    add "main_bg_movie" at Transform(xalign=0.5, yalign=0.5)
    python:
        last_saved_game_list = sorted(renpy.list_saved_games('\d+'), key=lambda x: x[3])
        if len(last_saved_game_list) == 0:
            last_saved_game = None
        else:
            last_saved_game = last_saved_game_list[-1]
            last_saved_game_name = last_saved_game[0].split("-")
            last_saved_game = (
                last_saved_game_name[0], # file name
                last_saved_game_name[1], # page name
                last_saved_game[2], # image
                "" #time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(last_saved_game[3]))  # time
            )
            print last_saved_game
            del last_saved_game_name
        del last_saved_game_list
    style_prefix "main_menu"
    add "color_primary" at main_menu_intro_animation_background
    add "gui/menu/line.png" at main_menu_intro_animation_line(340, 90, 0.27)
    add "gui/menu/banner.png" at main_menu_intro_animation_line(290, 130, 0.27)
    add "gui/menu/logo.png" at main_menu_intro_animation_logo
    add "gui/menu/1.png" at main_menu_intro_animation_title(0, 0.2)
    add "gui/menu/2.png" at main_menu_intro_animation_title(60, 0.25)
    add "gui/menu/3.png" at main_menu_intro_animation_title(110, 0.3)
    add "gui/menu/4.png" at main_menu_intro_animation_title(170, 0.35)
    add "gui/menu/5.png" at main_menu_intro_animation_title(230, 0.4)
    add "gui/menu/3.png" at main_menu_intro_animation_title(290, 0.45)
    add "gui/menu/6.png" at main_menu_intro_animation_title(350, 0.5)
    add "gui/menu/7.png" at main_menu_intro_animation_title(410, 0.55)
    if last_saved_game != None:
        frame at main_menu_save_lot:
            style "main_menu_save_lot"
            vbox:
                xpos 180
                ypos 10
                text _("最近的存档") style "main_menu_save_lot_text"
                text last_saved_game[3] style "main_menu_save_lot_text"
                textbutton _("从这里继续") style "main_menu_save_lot_button" action FileLoad(last_saved_game[1], confirm=False, page=last_saved_game[0])
            imagebutton:
                idle last_saved_game[2]
                xpos 0
                ypos 0
                action FileLoad(last_saved_game[1], confirm=False, page=last_saved_game[0])
            add "gui/menu/save_cover.png" xpos 0 ypos 0 zoom 0.4
    frame at main_menu_sidebar:
        style "main_menu_sidebar"
        add "color_primary"
    vbox at main_menu_left_action_panel:
        style "main_menu_left_action_panel"
        style_prefix "main_menu_left_action_panel"
        textbutton _("新的故事") action Start()
        textbutton _("回到日常") action ShowMenu("load")
        textbutton _("关于本作") action ShowMenu("about")
        textbutton _("系统设置") action ShowMenu("preferences")
        textbutton _("帮助文档") action ShowMenu("help")
        if renpy.variant("pc"):
            textbutton _("退出游戏") action Quit(confirm=False)
    vbox at main_menu_right_action_panel:
        style "main_menu_right_action_panel"
        style_prefix "main_menu_right_action_panel"
        hbox:
            textbutton _("事件画廊"):
                style "main_menu_right_action_panel_text_button"
                action ShowMenu("gallery")
            imagebutton at main_menu_right_action_panel_image_button:
                idle "gui/menu/gallery.png"
                hover "gui/menu/gallery hover.png"
                action ShowMenu("gallery")
        hbox:
            if persistent.SYSMusicAvailable:
                textbutton _("音乐鉴赏"):
                    style "main_menu_right_action_panel_text_button"
                    action Start("soundtrack_prepare")
                imagebutton at main_menu_right_action_panel_image_button:
                    idle "gui/menu/music.png"
                    hover "gui/menu/music hover.png"
                    action Start("soundtrack_prepare")
            else:
                text _("音乐鉴赏") style "main_menu_right_action_panel_text_muted"
                imagebutton at main_menu_right_action_panel_image_button:
                    idle "gui/menu/music muted.png"
        hbox:
            if persistent.SystemStoryCache[17]:
                textbutton _("场景回想"):
                    style "main_menu_right_action_panel_text_button"
                    action Start("theater_prepare")
                imagebutton at main_menu_right_action_panel_image_button:
                    idle "gui/menu/theater.png"
                    hover "gui/menu/theater hover.png"
                    action Start("theater_prepare")
            else:
                text _("场景回想") style "main_menu_right_action_panel_text_muted"
                imagebutton at main_menu_right_action_panel_image_button:
                    idle "gui/menu/theater muted.png"
    text "© 2016 - 2018\n  Kiriya·Kasasagi/2eme Gymnopédie\n  Lundarl Gholoi/GILESFVK ËKITES\n  Version [config.version!t]" at main_menu_text

transform main_menu_intro_animation_background:
    xalign 0.5
    yalign 0.5
    xpos 1600
    ypos 1200
    zoom 2.5
    rotate 45
    parallel:
        pause 0.7
        easein_back 0.3 zoom 1
    parallel:
        easein 1.0 xpos -200 ypos -200
transform main_menu_intro_animation_title(x_pos, delay_time):
    xpos 80 + x_pos
    ypos 80
    xanchor 0.5
    yanchor 0.5
    zoom 0
    rotate -1
    pause 0.8 + delay_time
    parallel:
        easein_back 0.4 zoom 0.3
transform main_menu_intro_animation_line(x_pos, y_pos, zoom_level):
    zoom 0
    xanchor 0.5
    yanchor 0.5
    xpos x_pos
    ypos y_pos
    pause 1.2
    parallel:
        easein_back 0.4 zoom zoom_level
transform main_menu_intro_animation_logo:
    xanchor 0.5
    yanchor 0.5
    zoom 0.25
    ypos 90
    xpos 1000
    pause 1.4
    easein 1.0 xpos 600 rotate -360
transform main_menu_sidebar:
    alpha 0
    pause 1.8
    easein 0.3 alpha 1
transform main_menu_left_action_panel:
    alpha 0
    xpos 40
    pause 1.8
    easein 0.3 alpha 1 xpos 60
transform main_menu_right_action_panel:
    alpha 0
    xanchor 1.0
    xpos 800
    pause 1.8
    easein 0.3 alpha 1 xpos 780
transform main_menu_right_action_panel_image_button:
    zoom 0.5
transform main_menu_text:
    alpha 0
    pause 1.8
    easein 0.3 alpha 1
transform main_menu_save_lot:
    alpha 0
    xpos 250
    ypos 200
    pause 2.1
    easein 0.3 alpha 1
style main_menu_save_lot is default
style main_menu_sidebar is default:
    area (750, 0, 50, 600)
style main_menu_text is gui_text:
    ypos 500
    xpos 60
    size 10
    color "#00B3C7"
    font "font/source-hans-sans-medium.ttc"
style main_menu_save_lot_text:
    size 16
    color "#00B3C7"
    font "font/zcool-happy-ayumi-extended.ttf"
style main_menu_save_lot_button:
    top_margin 20
style main_menu_save_lot_button_text:
    size 24
    color "#00B3C7"
    hover_color "#04C9FF"
style main_menu_left_action_panel:
    ypos 180
    spacing 15
style main_menu_left_action_panel_button is gui_button:
    xalign 0
style main_menu_left_action_panel_button_text is gui_button_text:
    size 26
    color "#95F7FF"
    outlines [(absolute(4), "#068AFC00", absolute(0), absolute(0)),
              (absolute(3), "#068AFC88", absolute(0), absolute(0)),
              (absolute(2), "#068AFCFF", absolute(0), absolute(0))]
    hover_color "#FBE28C"
    hover_outlines [(absolute(4), "#FFFFFF00", absolute(0), absolute(0)),
                    (absolute(3), "#FFFFFF88", absolute(0), absolute(0)),
                    (absolute(2), "#FFFFFFFF", absolute(0), absolute(0))]
style main_menu_right_action_panel:
    ypos 350
    spacing 15
style main_menu_right_action_panel_hbox:
    xalign 1.0
style main_menu_right_action_panel_text is gui_button_text:
    size 26
    xalign 1.0
    color "#00B3C7"
style main_menu_right_action_panel_text_muted is gui_button_text:
    size 26
    xalign 1.0
    color "#636363"
style main_menu_right_action_panel_text_button:
    yalign 0.5
style main_menu_right_action_panel_text_button_text is gui_button_text:
    size 26
    xalign 1.0
    color "#00B3C7"
    hover_color "#068AFC"
## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):
    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"
                pass
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial 1.0
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        side_yfill True
                        transclude
                else:
                    transclude
    vbox:
        style_prefix "game_menu_vbox"
        xalign 40
        yalign 0.5
        spacing gui.navigation_spacing
        if not main_menu:
            if _in_replay:
                textbutton _("结束回放") action EndReplay(confirm=True)
            textbutton _("历史记录") action ShowMenu("history")
            textbutton _("保存进度") action ShowMenu("save")
            textbutton _("时间回溯") action ShowMenu("load")
            textbutton _("系统设置") action ShowMenu("preferences")
            if renpy.variant("pc"):
                textbutton _("帮助文档") action ShowMenu("help")
                textbutton _("退出游戏") action Quit(confirm=not main_menu)
            textbutton _("回到主界面") action MainMenu()
    if main_menu:
        textbutton _("返回"):
            style "return_button"
            action Return()
    else:
        textbutton _("继续游戏"):
            style "return_button"
            action Return()
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
    label title
    add "gui/logo.png" xpos 610 ypos 9 zoom 0.2

style game_menu_outer_frame:
    bottom_padding 40
    top_padding 50
    background "gui/game_menu.png"
style game_menu_navigation_frame is empty
style game_menu_navigation_frame:
    xsize 120
    yfill True
style game_menu_content_frame:
    left_margin 40
    right_margin 10
    top_margin 10
style game_menu_scrollbar is gui_vscrollbar
style game_menu_label:
    xpos 10
    ypos 20
    ysize 120
style game_menu_label_text:
    size 30
    color "#FFFFFF"
style game_menu_vbox_button_text:
    xpos 10
    color "#222222"
    hover_color "#FFFFFF"
    hover_outlines [(absolute(1), "#222222", absolute(0), absolute(0))]
style return_button:
    ypos 500
style return_button_text is game_menu_vbox_button_text


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
    tag menu
    use game_menu(_("关于本作"), scroll="viewport"):
        style_prefix "about"

        vbox:
            label "[config.name!t]"
            text _("版本 [config.version!t]\n")
            text _("这是一个由2eme Gymnopédie使用LiveMaker制作、GILESFVK ËKITES使用Ren\'py移植的游戏。游戏的LiveMaker日文版本可以在{a=http://2emegymnopedie.blog77.fc2.com/blog-entry-502.html}此处（需翻墙）{/s}得到。")
            text _("本软件的源代码可在PC发行版中找到（不含资源文件）。")
            text _("由于没有来自2eme Gymnopédie的使用条款，因此使用者必须遵守来自GILESFVK ËKITES的相关条款：")
            text _("")
            text _("{size=+5}GILESFVK ËKITES 最终用户许可协议{/size}")
            text _("{b}{size=-5}请认真阅读本协议，其表示你与GILESFVK ËKITES（或同人社团GILESFVK ËKITES，以下简称EKIFVK）在使用后者提供的服务时所需要遵守的协议，适用范围包括软件、服务、游戏、音像影像文字制品、同人创作与支持，一定情况可能包括相关媒体、宣传或任何来自后者的产品及附属材料（上述所有范围以下简称为服务）。一旦你开始使用本协议所指向的服务并在任何位置选择“我已阅读并同意上述协议”（如果服务为游戏，则此标志变更为开始游玩游戏后，不包括游戏主界面），即表明你同意接受本协议的各项条款并将会遵守它们所提出的约定。如果你不同意本协议，请不要继续使用本协议所指向的服务。{/size}{/b}")
            text _("1. 约定和所有权")
            text _("    你是使用服务的主体。")
            text _("    EKIFVK是提供服务的主体，也是本协议的制定方，拥有本协议及其指向的服务的最终解释权。")
            text _("    EKIFVK拥有本协议及其指向的服务的全部所有权，你在同意本协议并没有违反本协议的期间拥有服务的使用权。")
            text _("")
            text _("2. 你可以使用服务在不违反你所在的国家和地区的法律法规的前提下任意开展非营利性活动。盈利性活动则取决于服务本身是否允许这么做。")
            text _("    补充条款：本游戏不支持你这么做。")
            text _("")
            text _("3. 当服务可以被理解为一种软件或软件服务时，你不能对其进行反向工程、反编译和反汇编，除非这样的行为获得了EKIFVK的认可。但是，如果它们是开源软件，你可以直接要求EKIFVK提供源代码，并在不违反对应的开源协议的情况下任意使用。")
            text _("")
            text _("4. 如果你未能遵守本协议，则那个时点你将失去使用服务的权利，同时本协议终止，你使用服务创造且仍旧留存于服务中的任何数据或其他形式的物品、信息视为被你放弃所有权，EKIFVK可决定接收这部分内容或销毁它们或不予处理。")
            text _("")
            text _("5. 如果本协议中任何一条被你所在国家和地区的法律系统证明为无效，则那个条目对你立即失效，不过其他条目的效力仍旧存在。")
            text _("")
            text _("6. 本协议的内容可能在未来会改变，届时你将会以醒目的方式收到通知并决定是否继续使用协议指向的服务。如果你决定继续，则你接受新的协议，本协议失效；如果你决定放弃，则按照第四条处理。")
            text _("")
            text _("7. 本协议自2017年9月18日起生效。")
            text _("")
            text _("")
            text _("关于 站酷(ZCOOL)字体")
            text _("站酷(ZCOOL)字体是由{a=http://www.zcool.com.cn/}站酷{/a}制作并发行的字体，本游戏中使用的是GILESFVK ËKITES在其基础上针对SCHOOLBOYS!系列定制的特殊版本。")
            text _("")
            text _("关于 思源黑体")
            text _("思源黑体是由{a=https://www.adobe.com/}Adobe{/a}与{a=https://www.google.com}Google{/a}制作并发行的字体，遵循{a=https://www.apache.org/licenses/LICENSE-2.0}Apache 2.0{/a}许可证授权。")
            text _("")
            text _("关于Ren'Py游戏引擎")
            text _("{a=https://www.renpy.org/}Ren'Py{/a}是一个使用python编写的开源游戏引擎，本游戏使用了其的[renpy.version_only]版，以下是它的许可协议：")
            text _("")
            text _("[renpy.license!t]")

style about_label is gui_label
style about_label_text is gui_label_text
style about_text:
    font "font/source-hans-sans-medium.ttc"
style about_text is gui_text
style about_label_text:
    size gui.label_text_size

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():
    tag menu
    use file_slots(_("保存进度"))


screen load():
    tag menu
    use file_slots(_("时间回溯"))


screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动保存"), quick=_("快读保存"))

    use game_menu(title):
        fixed:
            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True
            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value
            grid 3 2:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(6):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%Y年%m月%d日\n%H:%M:%S"), empty=_("没有记录")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)
            ## Buttons to access other pages.
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious()
                if config.has_autosave:
                    textbutton _("{#auto_page}自动") action FilePage("auto")
                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()

style page_button is gui_button
style page_button:
    properties gui.button_properties("page_button")
style page_button_text is gui_button_text
style page_button_text:
    properties gui.button_text_properties("page_button")
style slot_button is gui_button
style slot_button:
    properties gui.button_properties("slot_button")
style slot_button_text is gui_button_text
style slot_button_text:
    properties gui.button_text_properties("slot_button")
style slot_time_text is slot_button_text
style slot_time_text:
    yoffset 5
style slot_name_text is slot_button_text
style page_label is gui_label
style page_label:
    xalign 0.5
    yalign 0
    ypadding 10
style page_label_text is gui_label_text
style page_label_text:
    layout "subtitle"
    hover_color gui.hover_color

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    tag menu

    use game_menu(_("系统设置"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                vbox:
                    style_prefix "check"
                    label _("自动略过")
                    textbutton _("没读过的文本") action Preference("skip", "toggle")
                    textbutton _("选项分歧文本") action Preference("after choices", "toggle")
                    textbutton _("所有加的特技") action InvertSelected(Preference("transitions", "toggle"))
                vbox:
                    style_prefix "radio"
                    label _("语言")
                    textbutton "简体中文" action Language(None) text_style "language_sc_button"
                    textbutton "日本語" action Language("japanese") text_style "language_ja_button"

            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    label _("文字显示速度")
                    bar value Preference("text speed")
                vbox:
                    if config.has_music:
                        label _("音乐音量")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("音效音量")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)

style language_sc_button is radio_button_text:
    font "font/zcool-happy-ayumi-extended.ttf"
style language_ja_button is radio_button_text:
    font "font/honyaji-re.ttf"
style pref_label is gui_label
style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2
style pref_label_text is gui_label_text
style pref_label_text:
    yalign 1.0
style pref_vbox is vbox
style pref_vbox:
    xsize 225
style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"
style radio_button_text is gui_button_text
style radio_button_text:
    properties gui.button_text_properties("radio_button")
style radio_vbox is pref_vbox
style radio_vbox:
    spacing gui.pref_button_spacing
style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
style check_button_text is gui_button_text
style check_button_text:
    properties gui.button_text_properties("check_button")
style check_vbox is pref_vbox
style check_vbox:
    spacing gui.pref_button_spacing
style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_slider:
    xalign 0.5
style slider_button is gui_button
style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10
style slider_button_text is gui_button_text
style slider_button_text:
    properties gui.button_text_properties("slider_button")
style slider_pref_vbox is pref_vbox
style slider_vbox:
    xsize 600

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    tag menu
    predict False

    use game_menu(_("历史记录"), scroll=("vpgrid" if gui.history_height else "viewport")):
        style_prefix "history"
        for h in _history_list:
            window:
                has fixed:
                    yfit True
                if h.who:
                    label h.who:
                        style "history_name"
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                text h.what
        if not _history_list:
            label _("暂无记录。")

style history_window is empty
style history_window:
    xfill True
    ysize gui.history_height
style history_name is gui_label
style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
style history_name_text is gui_label_text
style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
style history_text is gui_text
style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
style history_label is gui_label
style history_label:
    xfill True
style history_label_text is gui_label_text
style history_label_text:
    xalign 0.5

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():
    tag menu
    default device = "keyboard"

    use game_menu(_("帮助文档"), scroll="viewport"):
        style_prefix "help"
        vbox:
            spacing 15
            hbox:
                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")
                textbutton _("手柄") action SetScreenVariable("device", "gamepad")
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

screen keyboard_help():
    hbox:
        label _("回车")
        text _("用来确定并提交你的操作，同时也可以用来继续阅读下一句")
    hbox:
        label _("空格")
        text _("用来确定你的操作，不过不会提交")
    hbox:
        label _("四个箭头")
        text _("当做比较难用的鼠标好了")
    hbox:
        label _("ESC")
        text _("进入系统菜单")
    hbox:
        label _("Ctrl")
        text _("按下这个键的期间你会处在快进模式")
    hbox:
        label _("Tab")
        text _("开关快进模式")
    hbox:
        label _("Page Up")
        text _("回到上一句，很适合点得太快漏下句子的情况")
    hbox:
        label _("Page Down")
        text _("回到下一句，仅当你现在看的不是最新一句时才管用")
    hbox:
        label "H"
        text _("隐藏所有能隐藏的东西，除了CG和立绘")
    hbox:
        label "S"
        text _("快速截图")

screen mouse_help():
    hbox:
        label _("左键")
        text _("可以用来点东西，点什么就是什么")
    hbox:
        label _("中键")
        text _("隐藏所有能隐藏的东西，除了CG和立绘")
    hbox:
        label _("右键")
        text _("进入系统菜单")
    hbox:
        label _("滚轮")
        text _("在最近看过的句子中来回切，不会一不小心滚到没看过的句子里去，放心就好")

screen gamepad_help():
    hbox:
        label _("RT/A")
        text _("相当于鼠标左键点击")
    hbox:
        label _("LT/LB")
        text _("回到上一句，很适合点得太快漏下句子的情况")
    hbox:
        label _("RB")
        text _("回到下一句台词，前提是看过")
    hbox:
        label _("D-Pad/摇杆")
        text _("当鼠标用")
    hbox:
        label _("START/GUIDE")
        text _("进入系统菜单")
    hbox:
        label _("Y")
        text _("隐藏所有能隐藏的东西，除了CG和立绘")
    textbutton _("手柄校准") action GamepadCalibrate()

style help_button is gui_button
style help_button:
    properties gui.button_properties("help_button")
    xmargin 8
style help_button_text is gui_button_text
style help_button_text:
    properties gui.button_text_properties("help_button")
style help_label is gui_label
style help_label:
    xsize 150
    right_padding 20
style help_label_text is gui_label_text
style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0
style help_text is gui_text


################################################################################
## Additional screens
################################################################################

## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("是") action yes_action
                textbutton _("否") action no_action
    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign 0.5
    yalign 0.5
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
style confirm_button is gui_medium_button
style confirm_button:
    properties gui.button_properties("confirm_button")
style confirm_button_text is gui_medium_button_text
style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 6
            text _("正在快进")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is empty
style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding
style skip_text is gui_text
style skip_text:
    size gui.notify_text_size
style skip_triangle is skip_text
style skip_triangle:
    font "font/zcool-happy-ayumi-extended.ttf"

## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text message
    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_frame:
    ypos gui.notify_ypos
    xalign 0.5
    background Solid("#FFFFFF88")
    padding gui.notify_frame_borders.padding
style notify_text is gui_text
style notify_text:
    properties gui.text_properties("notify")

## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            spacing gui.nvl_spacing
        if gui.nvl_height:
            vpgrid:
                cols 1
                yinitial 1.0
                use nvl_dialogue(dialogue)
        else:
            use nvl_dialogue(dialogue)
        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id
            fixed:
                yfit gui.nvl_height is None
                if d.who is not None:
                    text d.who:
                        id d.who_id
                text d.what:
                    id d.what_id

define config.nvl_list_length = 6

style nvl_window is default
style nvl_window:
    xfill True
    yfill True
    background "gui/nvl.png"
    padding gui.nvl_borders.padding
style nvl_entry is default
style nvl_entry:
    xfill True
    ysize gui.nvl_height
style nvl_label is say_label
style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign
style nvl_dialogue is say_dialogue
style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
style nvl_button is button
style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign
style nvl_button_text is button_text
style nvl_button_text:
    properties gui.button_text_properties("nvl_button")
style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
