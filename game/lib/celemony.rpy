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
        for index, characters in enumerate(final_status):
            for character in characters:
                final_score[index] += score_table["base"][character][index]
            for extra in score_table["extra"]:
                if (len(extra["condition"][0]) == 0 or index in extra["condition"][0]) and set(extra["condition"][1]).issubset(set(characters)):
                    random_offset = renpy.random.random()
                    final_score[index] += next((x for x in extra["range"] if x["rate"][0] <= random_offset and x["rate"][1] > random_offset), 0)["value"]
                    del random_offset
        del final_status

    return final_score
