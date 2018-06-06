# Note: Basic win score = ceil(sum(ceil(sum(character[i]) / 3) for i in range(4)) / 4)

init python:
    def celemony_piece_dragged(drags, drop):
        piece_index = int(drags[0].drag_name[6:]);
        if piece_index in store.group_piece_status:
            store.group_piece_status[store.group_piece_status.index(piece_index)] = -1
        if drop:
            group_index = int(drop.drag_name[12:]);
            if (store.group_piece_status[group_index] > -1):
                return False
            store.pieces[piece_index]["x"] = drop.x
            store.pieces[piece_index]["y"] = drop.y
            store.group_piece_status[group_index] = piece_index
        else:
            store.pieces[piece_index]["x"] = drags[0].x
            store.pieces[piece_index]["y"] = drags[0].y
        return True

label celemony(groups, score_table):
    python:
        pieces = [
            { "x": 0, "y": 0, "id": "Itou" },
            { "x": 0, "y": 0, "id": "Izumi" },
            { "x": 0, "y": 0, "id": "Katou" },
            { "x": 0, "y": 0, "id": "Kimura" },
            { "x": 0, "y": 0, "id": "Kojima" },
            { "x": 0, "y": 0, "id": "Matsuda" },
            { "x": 0, "y": 0, "id": "Okajima" },
            { "x": 0, "y": 0, "id": "Saburou" },
            { "x": 0, "y": 0, "id": "Sakuya" },
            { "x": 0, "y": 0, "id": "Satou" },
            { "x": 0, "y": 0, "id": "Shinobu" },
            { "x": 0, "y": 0, "id": "Shintarou" },
            { "x": 0, "y": 0, "id": "Sora" },
            { "x": 0, "y": 0, "id": "Tomo" },
            { "x": 0, "y": 0, "id": "Tsubasa" },
            { "x": 0, "y": 0, "id": "Tsuki" },
        ]
        group_piece_status = [-1] * 16
        for i in range(16):
            pieces[i]["x"] = renpy.random.randint(0, 640)
            pieces[i]["y"] = renpy.random.randint(412, 510)
label celemony_selector_tag:
    call screen celemony_selector(groups, pieces)
    if _return == "Finished":
        python:
            final_status = [[], [], [], []]
            for index, character in enumerate(group_piece_status):
                final_status[groups[index]["id"]].append(pieces[character]["id"])
        call celemony_calculator from _call_celemony_calculator
        $ del final_score
        $ del celemony_actions
        return _return
    else:
        jump celemony_selector_tag

screen celemony_selector(groups, pieces):
    draggroup:
        for index, group in enumerate(groups):
            drag:
                drag_name "placeholder_" + str(index)
                child group["image"]
                draggable False
                xpos group["x"] ypos group["y"]
        for index, piece in enumerate(pieces):
            drag:
                drag_name "piece_" + str(index)
                child "images/Celemony/Avatar/" + piece["id"] + ".png"
                droppable False
                dragged celemony_piece_dragged
                xpos piece["x"] ypos piece["y"]
    if not -1 in store.group_piece_status:
        textbutton _("出赛"):
            style "celemony_selector_accept_button"
            action Return("Finished")

style celemony_selector_accept_button:
    xalign 0.5
    ypos 480
style celemony_selector_accept_button_text:
    size 60
    color "#222222"
    hover_color "#FAFAFA"
    font "font/source-hans-sans-medium.ttc"
    outlines [(absolute(2), "#FAFAFAFF", absolute(0), absolute(0)),
              (absolute(4), "#FAFAFAAA", absolute(0), absolute(0)),
              (absolute(6), "#FAFAFA66", absolute(0), absolute(0)),
              (absolute(8), "#FAFAFA00", absolute(0), absolute(0))]
    hover_outlines [(absolute(2), "#222222FF", absolute(0), absolute(0)),
                    (absolute(4), "#222222AA", absolute(0), absolute(0)),
                    (absolute(6), "#22222266", absolute(0), absolute(0)),
                    (absolute(8), "#22222200", absolute(0), absolute(0))]

label celemony_calculator:
    python:
        final_score = [0] * 4
        celemony_actions = []
        for index, characters in enumerate(final_status):
            for character in characters:
                score = score_table["base"][character][index]
                final_score[index] += score
                celemony_actions.append({
                    "type": "base",
                    "character": character,
                    "event": index,
                    "score": score
                })
            for extra in score_table["extra"]:
                if (len(extra["condition"][0]) == 0 or index in extra["condition"][0]) and set(extra["condition"][1]).issubset(set(characters)):
                    random_offset = renpy.random.random()
                    offset = next((x for x in extra["range"] if x["rate"][0] <= random_offset and x["rate"][1] > random_offset), 0)
                    final_score[index] += offset["value"]
                    celemony_actions.append({
                        "type": "extra",
                        "character": extra["condition"][1],
                        "event": index,
                        "score": offset["value"],
                        "description": offset["description"] if "description" in offset else ""
                    })
                    del random_offset
        del final_status

    return { "score": final_score, "actions": celemony_actions }

label convert_celemony_detail(data, events):
    python:
        events = [{ "index": i, "name": e } for i, e in enumerate(events)]
        for index, event in enumerate(events):
            dataset = [x for x in data["actions"] if x["event"] == event["index"]]
            events[index] = {
                "score": data["score"][index],
                "name": events[index]["name"],
                "base": [x for x in dataset if x["type"] == "base"],
                "extra": [x for x in dataset if x["type"] == "extra"]
            }

    return events

screen celemony_detail(events):
    add "gui/celemony_detail.png"
    frame:
        style "celemony_detail_frame"
        has viewport:
            mousewheel "change"
            draggable True
            side_yfill True
        vbox:
            style "celemony_detail_frame_viewarea"
            null height 10
            text _("慎酱的比赛日志") style "celemony_detail_text"
            null height 10
            for index, event in enumerate(events):
                text event["name"] style "celemony_detail_event_title"
                python:
                    y_size = len(events) / 4.0
                    if y_size > int(y_size):
                        y_size += 1
                vpgrid:
                    style "celemony_detail_frame_viewarea"
                    ysize y_size * 90
                    cols 4
                    for character in event["base"]:
                        fixed:
                            style "celemony_detail_character_box"
                            add "images/Celemony/Avatar/" + character["character"] + ".png"
                            if character["character"] in ["Satou", "Okajima", "Itou", "Kimura", "Kojima", "Saburou", "Sakuya", "Tsubasa"]:
                                text str(character["score"]) style "celemony_detail_character_score_blue"
                            else:
                                text str(character["score"]) style "celemony_detail_character_score"
                if len([x for x in event["extra"] if x["description"] != ""]) == 0:
                    text _("一切照常进行") style "celemony_detail_text"
                else:
                    for extra in [x for x in event["extra"] if x["description"] != ""]:
                        text __(extra["description"]) + (" (%s)" % (extra["score"] if extra["score"] < 0 else "+%d" % extra["score"])) style "celemony_detail_text"
                null height 10
                text __("结果：%d分（%s）") % (event["score"], __("成功") if event["succeed"] else __("失败")) style "celemony_detail_text"
                null height 20
            textbutton _("继续") style "celemony_detail_next_button" action Return()
            null height 20

style celemony_detail_frame is default:
    area (70, 0, 680, 600)
style celemony_detail_frame_viewarea:
    xsize 700
style celemony_detail_text:
    font "font/zcool-happy-ayumi-extended.ttf"
style celemony_detail_event_title is celemony_detail_text:
    xalign 0.5
    size 34
style celemony_detail_next_button:
    xalign 0.9
style celemony_detail_next_button_text is celemony_detail_text:
    size 28
    color "#C1718E"
    outlines [(absolute(3), "#FFFFFFFF", absolute(0), absolute(0))]
    hover_color "#FFFFFF"
    hover_outlines [(absolute(3), "#C1718EFF", absolute(0), absolute(0))]
style celemony_detail_character_box is default:
    xsize 158
    ysize 90
style celemony_detail_character_score is celemony_detail_text:
    xpos 140
    ypos 55
    size 28
    color "#FFFFFF"
    outlines [(absolute(6), "#FF6702FF", absolute(0), absolute(0))]
style celemony_detail_character_score_blue is celemony_detail_character_score:
    outlines [(absolute(6), "#01B0FEFF", absolute(0), absolute(0))]
