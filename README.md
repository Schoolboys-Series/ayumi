# SCHOOLBOYS! AYUMI Source code repository

![Version](https://img.shields.io/badge/Version-2.3.0562.0-green.svg?style=flat-square)
![RenPy](https://img.shields.io/badge/RenPy-7.2.2.491-green.svg?style=flat-square)

This repository contains all source codes of SCHOOLBOYS! AYUMI, which is a Ren'Py game. Resources (images, sounds, and movies) are not included in this place because they are under other license.

## Modification for Ren'Py

Because it is an issue on showing image that ratio on w/h is different than screen in gallery will cause problem, a change was made to solve this problem in Ren'Py engine file common/00gallery.rpy:

```patch
@@ -566,14 +566,30 @@ init -1500:
     #     The number of images attached to the current button.
     # gallery
     #     The image gallery object.
+    python:
+        def image_size(source):
+            source_renderer = renpy.render(source, 800, 600, 0, 0)
+            size = source_renderer.get_size()
+            del source_renderer
+            return size
+        
+        def image_contain_scale_level(source, area_width, area_height):
+            image_width, image_height = image_size(source)
+            scale_x = image_width / area_width
+            scale_y = image_height / area_height
+            scale_level = 1.0 / (scale_x if scale_x > scale_y else scale_y)
+            del scale_x, scale_y, image_width, image_height
+            return scale_level
+
     screen _gallery:
+        add Solid("#000000")
 
         if locked:
             add "#000"
             text _("Image [index] of [count] locked.") align (0.5, 0.5)
         else:
             for d in displayables:
-                add d
+                add d zoom image_contain_scale_level(d, config.screen_width, config.screen_height)
 
         if gallery.slideshow:
             timer gallery.slideshow_delay action Return("next") repeat True

```