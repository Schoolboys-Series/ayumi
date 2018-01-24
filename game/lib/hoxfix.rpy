init -2 python:
    def run_hotfixes():
        hotfix_1()

    def hotfix_1():
        if not "sys_effect3_current_file" in globals():
            print "Hotfix: define sys_effect3_current_file"
            globals()["sys_effect3_current_file"] = ""
        if not "sys_effect4_current_file" in globals():
            print "Hotfix: define sys_effect4_current_file"
            globals()["sys_effect4_current_file"] = ""
