label dewitt_button_dialogue:
    if M_dewitt.is_state(S_dewitt_talent_show_help):
        call expression game.dialog_select("music_classroom_dewitt_talent_show_help") from _call_expression_1723
        $ M_dewitt.trigger(T_dewitt_mc_talent_show_help)

    elif M_dewitt.is_state(S_dewitt_return_flute):
        call expression game.dialog_select("music_classroom_dewitt_return_flute") from _call_expression_1724
        $ M_dewitt.trigger(T_dewitt_flute_practice)
        $ game.timer.tick()

    elif M_dewitt.is_state(S_dewitt_talent_get):
        call expression game.dialog_select("music_classroom_dewitt_talent_get") from _call_expression_1725
        $ M_dewitt.trigger(T_dewitt_talent_show_excitement)

    elif M_dewitt.is_state(S_dewitt_eve_meet_up):
        call expression game.dialog_select("dewitt_dialogue_dewitt_eve_meet_up") from _call_expression_1726

    elif M_dewitt.is_state(S_dewitt_science_adhesive):
        call expression game.dialog_select("dewitt_dialogue_dewitt_science_adhesive") from _call_expression_1727

    elif M_dewitt.is_state(S_dewitt_school_sneak_mission_help):
        call expression game.dialog_select("dewitt_dialogue_dewitt_school_sneak_mission_help") from _call_expression_1728

    elif M_dewitt.is_state(S_dewitt_office_night_visit_delay):
        call expression game.dialog_select("dewitt_dialogue_dewitt_office_night_visit_delay") from _call_expression_1729

    elif M_dewitt.is_state(S_dewitt_office_night_visit):
        call expression game.dialog_select("dewitt_dialogue_dewitt_office_night_visit") from _call_expression_1730

    elif M_dewitt.is_state(S_dewitt_end):
        call expression game.dialog_select("dewitt_dialogue_dewitt_end") from _call_expression_1731
    else:

        call expression game.dialog_select("dewitt_dialogue_intro") from _call_expression_1732
        menu:
            "Flute." if M_dewitt.between_states(S_dewitt_find_flute, S_dewitt_make_new_flute):
                if M_dewitt.is_state([S_dewitt_find_flute, S_dewitt_judith_locker_search]):
                    call expression game.dialog_select("dewitt_dialogue_dewitt_find_flute") from _call_expression_1733
                else:

                    call expression game.dialog_select("dewitt_dialogue_dewitt_make_new_flute") from _call_expression_1734

            "Talent Show." if M_dewitt.between_states(S_dewitt_talent_show_ask_annie, S_dewitt_kevin_give_guitar):
                call expression game.dialog_select("dewitt_dialogue_talent_show_help") from _call_expression_1735
            "Not really.":

                call expression game.dialog_select("dewitt_dialogue_leave") from _call_expression_1736
    hide dewitt
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
