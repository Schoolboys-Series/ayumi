init -1000 python:
    persistent.gallery_page = ""

    class CurrentGalleryPage(Action):
        def __init__(self, page=""):
            self.page = page
        def __call__(self):
            if not self.get_sensitive():
                return
            persistent.gallery_page = self.page
            renpy.restart_interaction()
        def get_sensitive(self):
            return self.page
        def get_selected(self):
            return self.page == persistent.gallery_page

    class AdvancedGallery(Gallery):
        def __init__(self):
            Gallery.__init__(self)
        def IsUnlocked(self, name):
            if name not in self.buttons:
                raise Exception("{0!r} is not a button defined in this gallery.".format(name))
            b = self.buttons[name]
            return b.check_unlock()
