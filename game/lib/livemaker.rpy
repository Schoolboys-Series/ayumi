# LiveMaker compatible library ©2017 GILESFVK ËKITES

define config.layers = [ 'master', 'transient', 'screens', 'overlay' ]

init -1 python:
    import random
    import copy
    # Volume stack
    volume_stack = {
        "music": [],
        "music2": [],
        "effect": [],
        "effect2": [],
        "effect3": [],
        "effect4": []
    }
    # Register extra channel to support LiveMaker
    renpy.music.register_channel("music2", "music", True, True, True)
    renpy.music.register_channel("effect", "sfx", False, True, True)
    renpy.music.register_channel("effect2", "sfx", False, True, True)
    renpy.music.register_channel("effect3", "sfx", False, True, True)
    renpy.music.register_channel("effect4", "sfx", False, True, True)
    renpy.music.register_channel("menu_effect", "sfx", False, True, True)
    renpy.music.register_channel("movie_main", loop=False, movie=True)
    renpy.music.register_channel("soundtrack", loop=True, movie=False)
    # Basic Messagebox data to support LiveMaker
    dialogue_stylesheet = {}
    dialogue_ctc = {}
    dialogue_show_actions = {}
    dialogue_stylesheet["(標準)"] = Style(style.default)
    dialogue_stylesheet["(標準)"].size = 22
    dialogue_stylesheet["(標準)"].color = "#000000"
    dialogue_stylesheet["(標準)"].outlines = [(absolute(1), "#FFFFFF", absolute(0), absolute(0))]
    dialogue_stylesheet["(標準)"].area = (175, 425, 620, 170)
    dialogue_stylesheet["(標準)"].padding = (20, 14, 20, 19)
    dialogue_stylesheet["(標準)"].background = Image("gui/window_ayumi.png", xalign=0, yalign=0)
    dialogue_ctc["(標準)"] = (754, 556)
    dialogue_show_actions["(標準)"] = False

    dialogue_stylesheet["イベントモード"] = Style(style.default)
    dialogue_stylesheet["イベントモード"].size = 22
    dialogue_stylesheet["イベントモード"].color = "#FFFFFF"
    dialogue_stylesheet["イベントモード"].outlines = [(absolute(1), "#000000", absolute(0), absolute(0))]
    dialogue_stylesheet["イベントモード"].area = (0, 300, 800, 300)
    dialogue_stylesheet["イベントモード"].padding = (20, 130, 10, 15)
    dialogue_stylesheet["イベントモード"].background = Image("gui/window_event.png", xalign=0.5, yalign=1.0)
    dialogue_ctc["イベントモード"] = (764, 566)
    dialogue_show_actions["イベントモード"] = True

    dialogue_stylesheet["チャット"] = Style(style.default)
    dialogue_stylesheet["チャット"].size = 22
    dialogue_stylesheet["チャット"].color = "#000000"
    dialogue_stylesheet["チャット"].outlines = [(absolute(1), "#FFFFFF", absolute(0), absolute(0))]
    dialogue_stylesheet["チャット"].area = (250, 50, 510, 104)
    dialogue_stylesheet["チャット"].padding = (72, 10, 10, 14)
    dialogue_stylesheet["チャット"].background = Image("gui/window_alert.png", xalign=0.0, yalign=0.0)
    dialogue_ctc["チャット"] = (754, 195)
    dialogue_show_actions["チャット"] = True

    dialogue_stylesheet["体育祭、音楽祭"] = Style(style.default)
    dialogue_stylesheet["体育祭、音楽祭"].size = 22
    dialogue_stylesheet["体育祭、音楽祭"].color = "#000000"
    dialogue_stylesheet["体育祭、音楽祭"].outlines = [(absolute(1), "#FFFFFF", absolute(0), absolute(0))]
    dialogue_stylesheet["体育祭、音楽祭"].area = (135, 240, 530, 120)
    dialogue_stylesheet["体育祭、音楽祭"].padding = (20, 10, 20, 10)
    dialogue_stylesheet["体育祭、音楽祭"].background = Image("gui/window_center.png", xalign=0.5, yalign=0.5)
    dialogue_ctc["体育祭、音楽祭"] = (635, 329)
    dialogue_show_actions["体育祭、音楽祭"] = False

    dialogue_stylesheet["チャット画面"] = Style(style.default)
    dialogue_stylesheet["チャット画面"].size = 22
    dialogue_stylesheet["チャット画面"].color = "#000000"
    dialogue_stylesheet["チャット画面"].outlines = [(absolute(1), "#FFFFFF", absolute(0), absolute(0))]
    dialogue_stylesheet["チャット画面"].area = (0, 0, 800, 600)
    dialogue_stylesheet["チャット画面"].padding = (127, 103, 15, 105)
    dialogue_stylesheet["チャット画面"].background = Image("gui/window_channel.png", xalign=1.0, yalign=0.0)
    dialogue_ctc["チャット画面"] = (755, 460)
    dialogue_show_actions["チャット画面"] = False

    dialogue_stylesheet["カルタ"] = Style(style.default)
    dialogue_stylesheet["カルタ"].size = 30
    dialogue_stylesheet["カルタ"].color = "#000000"
    dialogue_stylesheet["カルタ"].outlines = [(absolute(1), "#FFFFFF", absolute(0), absolute(0))]
    dialogue_stylesheet["カルタ"].area = (38, 9, 582, 103)
    dialogue_stylesheet["カルタ"].padding = (10, 0, 0, 0)
    dialogue_stylesheet["カルタ"].background = Image("gui/window_empty.png", xalign=0, yalign=0)
    dialogue_ctc["カルタ"] = (580, 70)
    dialogue_show_actions["カルタ"] = False

    # set_window("<Messagebox's name from LiveMaker project>")
    def set_window(name=None):
        if "current_window" in globals() and name == None:
            name = globals()["current_window"]
        elif name != None:
            globals()["current_window"] = name
        else:
            globals()["current_window"] = name = "イベントモード"
        print "Set windows to : %s" % (name)
        style.window = copy.deepcopy(dialogue_stylesheet[name])
        if style.exists("say_dialogue"):
            style.say_dialogue.color = dialogue_stylesheet[name].color
            style.say_dialogue.size = dialogue_stylesheet[name].size
        if style.exists("ctc"):
            style.ctc.pos = dialogue_ctc[name]
        globals()["sys_dialogue_show_actions"] = dialogue_show_actions[name]
        style.rebuild()

    # Action support for set_window(name)
    class SetWindow(Action):
        def __init__(self, name=""):
            self.name = name
        def __call__(self):
            set_window(self.name)

    def get_volume(channel):
        return renpy.audio.audio.get_channel(channel).context.secondary_volume

    def record_volume(channel):
        globals()["volume_stack"][channel].append(get_volume(channel))

    def reverse_volume(channel, fade=0):
        stack = globals()["volume_stack"][channel]
        if len(stack) == 0:
            return
        original_volume = stack.pop()
        renpy.music.set_volume(original_volume, fade, channel)
    
    #LiveMaker compatible function: condition calculator
    def judge_lm_condition(code):
        final_result = False
        total_length = len(code)
        if total_length == 0:
            return True
        i = 0
        if code[0]["scope"] > 0:
            scope_offset = code[0]["scope"]
            while i < total_length:
                code[i]["scope"] = code[i]["scope"] - scope_offset
                i += 1
        i = 0
        current_scope = 0
        while i < total_length:
            content = code[i]["content"]
            scope = code[i]["scope"]
            if scope == current_scope:
                if content != "":
                    final_result = final_result or eval(content)
                else:
                    final_result = final_result or True
            else:
                if content != "":
                    final_result = final_result and eval(content)
                else:
                    final_result = final_result and True
            current_scope = scope
            if final_result and i < total_length - 1 and code[i + 1]["scope"] <= current_scope:
                return True
            if not final_result:
                i += 1
                while i < total_length and code[i]["scope"] > current_scope:
                    i += 1
                continue
            i += 1
        return final_result
    
    def lm_input(caption, prompt, placeholder = []):
        renpy.show_screen("lm_input_caption", caption=caption)
        result = [None] * len(prompt)
        for index, request in enumerate(prompt):
            if placeholder != None and index < len(placeholder):
                result[index] = renpy.input(request, placeholder[index])
            else:
                result[index] = renpy.input(request)
            renpy.pause(0.2, hard=True)
        renpy.hide_screen("lm_input_caption");
        return result

    # Customized pip-like operator support
    class Infix:
        def __init__(self, function):
            self.function = function
        def __ror__(self, other):
            return Infix(lambda x, self=self, other=other: self.function(other, x))
        def __or__(self, other):
            return self.function(other)
        def __rlshift__(self, other):
            return Infix(lambda x, self=self, other=other: self.function(other, x))
        def __rshift__(self, other):
            return self.function(other)
        def __call__(self, value1, value2):
            return self.function(value1, value2)

    # LiveMaker compatible operator: string combine
    str_combine = Infix(lambda x,y: str(x) + str(y))

    def FillMem(target, content):
        if isinstance(target, list):
            for i in range(len(target)):
                if isinstance(target[i], list):
                    FillMem(target[i], content)
                else:
                    target[i] = content
        else:
            target[i] = content

    def OpenUrl(url):
        target = OpenURL(url);
        target.__call__()

    def Max(a, b):
        return max(a, b)

    def Min(a, b):
        return min(a, b)

    def Random(limit):
        return renpy.random.randint(0, limit - 1)

    def VarExists(name):
        return name in globals() and name != None

    def Not(condition):
        return not condition

    def AddArray(source, item):
        source.append(item)
    
    def StringToArray(source):
        return soruce.split("\n")

    def AddDelimiter(spliter, source):
        if (source == "" or source == None):
            return source
        else:
            return source + spliter

transform left_top:
    xpos 0.0 xanchor 0.0 ypos 0.0 yanchor 0.0
transform left_center:
    xpos 0.0 xanchor 0.0 ypos 0.5 yanchor 0.5
transform left_bottom:
    xpos 0.0 xanchor 0.0 ypos 1.0 yanchor 1.0
transform center_top:
    xpos 0.5 xanchor 0.5 ypos 0.0 yanchor 0.0
transform center_center:
    xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
transform center_bottom:
    xpos 0.5 xanchor 0.5 ypos 1.0 yanchor 1.0
transform right_top:
    xpos 1.0 xanchor 1.0 ypos 0.0 yanchor 0.0
transform right_center:
    xpos 1.0 xanchor 1.0 ypos 0.5 yanchor 0.5
transform right_bottom:
    xpos 1.0 xanchor 1.0 ypos 1.0 yanchor 1.0

## LiveMaker Compatible Menu ###################################################
##
## This screen is a compatible screen to show LiveMaker's menu.
##
## item.pos = (x, y)
## item.image = <Image>
## item.hover = <Image>
## item.preview = (x, y, Image)
## item.name = <String>
## item.condition = <Code>
## sound.hover = <Sound>
## sound.click = <Sound>

label lm_menu(item, sound, time_limit, fadein_time=0, fadeout_time=0):
    call screen lm_menu_screen(item, sound, time_limit, fadein_time, fadeout_time)
    $ _lm_selected_value = _return["name"]
    $ _lm_selected_index = _return["index"]
    return

screen lm_menu_screen(items, sound, time_limit, fadein_time, fadeout_time):
    frame at lm_menu_show_hide(fadein_time, fadeout_time):
        style "lm_menu_frame"
        for i, item in enumerate(items):
            if (not "condition" in item) or judge_lm_condition(item["condition"]):
                if not "type" in item or item["type"] == "imagebutton":
                    imagebutton:
                        anchor (0, 0)
                        pos item["pos"]
                        idle item["image"]
                        hover item["hover"]
                        if "click" in sound:
                            action [Hide("lm_menu_preview"), Play("menu_effect", sound["click"]), Return({ "name": item["name"], "index": i })]
                        else:
                            action [Hide("lm_menu_preview"), Return({ "name": item["name"], "index": i })]
                        if "preview" in item and (len(item["preview"]) == 3):
                            if "hover" in sound:
                                hovered [Play("menu_effect", sound["hover"]), Show("lm_menu_preview", x=item["preview"][0], y=item["preview"][1], target=item["preview"][2])]
                            else:
                                hovered Show("lm_menu_preview", x=item["preview"][0], y=item["preview"][1], target=item["preview"][2])
                            unhovered Hide("lm_menu_preview")
                        else:
                            if "hover" in sound:
                                hovered Play("menu_effect", sound["hover"])
                elif item["type"] == "textbutton":
                    textbutton item["text"]:
                        anchor (0, 0)
                        pos item["pos"]
                        if "style" in item:
                            text_style item["style"]
                        else:
                            text_style "lm_menu_textbutton_normal"
                        if "click" in sound:
                            action [Hide("lm_menu_preview"), Play("menu_effect", sound["click"]), Return({ "name": item["name"], "index": i })]
                        else:
                            action [Hide("lm_menu_preview"), Return({ "name": item["name"], "index": i })]
                        if "preview" in item and (len(item["preview"]) == 3):
                            if "hover" in sound:
                                hovered [Play("menu_effect", sound["hover"]), Show("lm_menu_preview", x=item["preview"][0], y=item["preview"][1], target=item["preview"][2])]
                            else:
                                hovered Show("lm_menu_preview", x=item["preview"][0], y=item["preview"][1], target=item["preview"][2])
                            unhovered Hide("lm_menu_preview")
                        else:
                            if "hover" in sound:
                                hovered Play("menu_effect", sound["hover"])
        if time_limit and time_limit > 0:
            timer time_limit action Return({ "name": "", "index": -1 })
        

screen lm_menu_preview(x, y, target):
    add target pos (x, y)

style lm_menu_textbutton_normal:
    color "#000000"
    size 24
    outlines [(absolute(2), "#FFFFFF", absolute(0), absolute(0))]
    hover_color "#FFFFFF"
    hover_outlines [(absolute(2), "#000000", absolute(0), absolute(0))]
style lm_menu_frame is default
transform lm_menu_show_hide(show_time, hide_time):
    on show:
        alpha 0.0
        linear show_time alpha 1.0
    on hide:
        alpha 1.0
        linear hide_time alpha 0.0

## Background for input caption
screen lm_input_caption(caption):
    tag lm_input_caption

    add "gui/input_caption.png" pos (135, 474)
    text caption:
        style "lm_input_caption_hint"

style lm_input_caption_hint:
    xalign 0.5
    yanchor 0.5
    ypos 517
    font "font/zcool-happy-ayumi-extended.ttf"

## LiveMaker Compatible Choice #################################################
##
## This screen is a compatible screen to show LiveMaker's choice.
##
## sound.hover = <Sound>
## sound.click = <Sound>

label lm_choice(items, sound, time_limit):
    call screen lm_choice_screen(items, sound, time_limit)
    $ _lm_selected_value = _return

    return _lm_selected_value

screen lm_choice_screen(items, sound, time_limit):
    style_prefix "choice"
    vbox:
        for item in items:
            textbutton item:
                if "click" in sound:
                    action [Play("menu_effect", sound["click"]), Return(item)]
                else:
                    action Return(item)
                if "hover" in sound:
                    hovered Play("menu_effect", sound["hover"])
    if time_limit and time_limit > 0:
        timer time_limit action Return("")
