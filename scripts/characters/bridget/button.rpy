label coach_button_dialogue:
    if player.location == L_school_bridgetoffice:
        call expression game.dialog_select("coach_bridget_dialogue_office_intro") from _call_expression_1984

    elif player.location == L_school_track:
        call expression game.dialog_select("coach_bridget_dialogue_courtyard_intro") from _call_expression_1985
    menu:
        "Where do I train?":
            call expression game.dialog_select("coach_bridget_dialogue_training_advice") from _call_expression_1986
        "Nothing.":

            call expression game.dialog_select("coach_bridget_dialogue_leave") from _call_expression_1987
    hide coach
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
