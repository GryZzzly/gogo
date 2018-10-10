label kim_button_dialogue:
    scene expression L_dealership.background_blur
    call expression game.dialog_select("kim_button_dialogue_intro") from _call_expression_1698
    menu kim_button_menu:
        "Is that you on the sign?":
            call expression game.dialog_select("kim_button_dialogue_sign") from _call_expression_1699
        "Nice button":
            call expression game.dialog_select("kim_button_dialogue_button") from _call_expression_1700
        "I'm just browsing":
            call expression game.dialog_select("kim_button_dialogue_browsing") from _call_expression_1701
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
