label tatiana_dialogue:
    call expression game.dialog_select("tatiana_dialogue_pre") from _call_expression_196
    menu tatiana_options:
        "You seem familiar.":
            call expression game.dialog_select("tatiana_dialogue_familiar") from _call_expression_197
            jump expression game.dialog_select("tatiana_options")
        "Any suggestions?":

            call expression game.dialog_select("tatiana_dialogue_suggestions") from _call_expression_198
            jump expression game.dialog_select("tatiana_options")
        "I found what I need.":

            call expression game.dialog_select("tatiana_dialogue_leave") from _call_expression_199

    hide tatia
    hide player
    hide xtra
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
