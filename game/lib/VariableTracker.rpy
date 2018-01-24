init python:
    class VariableTracker(Action):
        def __init__(self, init_value="", record_variable_name=""):
            self.init_value = init_value
            self.record_variable_name = record_variable_name
        def __call__(self):
            if not (self.get_sensitive() and self.record_variable_name in globals()):
                return
            globals()[self.record_variable_name] = self.init_value
            renpy.restart_interaction()
        def get_sensitive(self):
            return self.init_value != None
        def get_selected(self):
            if not self.record_variable_name in globals():
                return False
            return self.init_value == globals()[self.record_variable_name]
