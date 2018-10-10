label dewitt_office_button_dialogue:
    if M_dewitt.is_state([S_dewitt_eve_meet_up, S_dewitt_erik_get_beer, S_dewitt_clean_graffiti]):
        call expression game.dialog_select("dewitt_dialogue_office_dewitt_eve_meet_up") from _call_expression_1636

    elif M_dewitt.is_state(S_dewitt_end) and game.timer.is_dark():
        call expression game.dialog_select("dewitt_dialogue_office_dewitt_end_intro") from _call_expression_1637
        menu:
            "Dance.":
                call expression game.dialog_select("dewitt_dialogue_office_dewitt_end_dance") from _call_expression_1638
                jump expression game.dialog_select("dewitt_twerk_loop")
            "BJ.":

                call expression game.dialog_select("dewitt_dialogue_office_dewitt_end_bj") from _call_expression_1639
                jump expression game.dialog_select("dewitt_bj_loop")
            "Right to it.":

                jump expression game.dialog_select("dewitt_dialogue_office_dewitt_end_sex")
    else:

        call expression game.dialog_select("dewitt_dialogue_office_intro") from _call_expression_1640
        menu:
            "Private flute lessons." if M_dewitt.is_state(S_dewitt_end):
                call expression game.dialog_select("dewitt_dialogue_office_flute_lessons") from _call_expression_1641
            "Nothing.":

                call expression game.dialog_select("dewitt_dialogue_office_leave") from _call_expression_1642
    hide player
    hide dewitt
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
