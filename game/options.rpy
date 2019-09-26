## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("SCHOOLBOYS! 步")

## The version of the game.

define config.version = "2.3.1092.0"

# 2.3.XXXX.X
# XXXX: 0100    0100    0100
#       场景修订 游戏修订 逻辑修订
# X: 子修订版本，一般为0

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "Gymno.Schoolboys.Ayumi"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.hw_video = False

## Enabled sound debugging
define config.debug_sound = True

# define config.allow_skipping = False

define config.after_load_callbacks = [
    set_window
]

## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "sound/BGM/Start scene.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = Dissolve(0.5)
define config.exit_transition = Dissolve(0.5)


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = Dissolve(0.5)


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "hide"

## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)

## disabled rollback because user occur unexpected operation
define config.rollback_enabled = False


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 160


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15

## Control the window mode. If True, the game boots on fullscreen mode.
## To hide iOS's status bar, preferences.fullscreen is True only iOS.

## default preferences.fullscreen = False


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "Gymno.Schoolboys.Ayumi.Savedata"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None) # Backup file
    build.classify('**.psd', None) # Photoshop file
    build.classify('**.ai', None)  # Illustrator file
    build.classify('**.fcp', None) # FontCreator file
    build.classify('README.md', None) # Readme file
    build.classify('Steamwork/**', None) # Steam file
    build.classify('CONTRIBUTING.md', None) # GitHub file
    build.classify('LICENSE', None) # GitHub file
    build.classify('**/thumbs.db', None) # Thumbnail file
    build.classify('**/.**', None) # Hidden file
    build.classify('raw/**', None) # Raw file
    build.classify('**/#**', None)
    build.classify('game/saves/**', None)
    build.classify('game/images/**.png', 'archive')
    build.classify('game/sound/**.ogg', 'archive')
    build.classify('game/tl/**/**.png', 'archive')
    build.classify('game/tl/**/**.ogg', 'archive')

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

define build.google_play_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnOJyab6W7Vv9X/2jM0yKPK9CxEZkoaL6MMI/vR188nj7R5wiP+kBBAJ+LiJ2+mKRmOPedLBIwUeNM3M5ffm9755bnUONSPEfo+hoMYhbL3/HiVZBh0IaCJ0QrXJj8bba6UckYNtNjzhQU4fUVftbW8p+qAZy7IjOfiak5DlhHF7jLvI8mwRv7iyhNGppeTPyACSKkF+UDiu/CUNxl2OkFL8ds2rIg3LLqfOxiprkzkWefvyW2lsrkfP03tncO+wqZRiX343GvFLCDIMrlabtjFGU+4j1BUCM/+a8GAjtpp1hFynRgWUB+RT+srX2CPHP5HfNE0zQ+cIHhXbJ66ng1QIDAQAB"
define build.google_play_salt = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
