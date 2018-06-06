init -2 python:
    def run_hotfixes():
        hotfix_1()
        hotfix_2()

    def hotfix_1():
        if not "sys_effect3_current_file" in globals():
            globals()["sys_effect3_current_file"] = ""
        if not "sys_effect4_current_file" in globals():
            globals()["sys_effect4_current_file"] = ""
    
    def hotfix_2():
        if sys_current_place_title != False and renpy.get_screen("scb_quick_menu") == None and renpy.get_screen("menu") == None:
            renpy.show_screen("scb_quick_menu", _layer="screens", _tag="scb_quick_menu")
            renpy.with_statement(Dissolve(0.2))
