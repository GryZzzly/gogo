label girl_lockerroom_dialogue:
    $ player.go_to(L_school_girlsroom)
    call pa_announcement from _call_pa_announcement_7
    if M_roxxy.is_state(S_roxxy_lockerroom_event):
        call expression game.dialog_select("girls_lockerroom_roxxy_lockerroom_event") from _call_expression_1069
        $ M_roxxy.trigger(T_roxxy_argument)

        $ player.go_to(L_school_lefthallway)
        $ game.main()
    elif M_judith.is_state(S_judith_in_girls_bathroom):
        call expression game.dialog_select("girls_lockerroom_judith_in_girls_bathroom") from _call_expression_1070
    $ game.main()

label judith_toilet:
    if M_judith.get("in bathroom"):
        if M_judith.get("sex sequence locked"):
            call expression game.dialog_select("girls_lockerroom_judith_toilet_first_intro") from _call_expression_1071
            menu:
                "You're not ugly!":
                    call expression game.dialog_select("girls_lockerroom_judith_toilet_first_not_ugly") from _call_expression_1072
                    menu:
                        "Ok.":
                            call expression game.dialog_select("girls_lockerroom_judith_toilet_first_ok") from _call_expression_1073
                            menu:
                                "Sure.":
                                    call expression game.dialog_select("girls_lockerroom_judith_toilet_first_sure") from _call_expression_1074
                                    menu:
                                        "Yes.":
                                            $ M_judith.trigger(T_judith_comfort_her)
                                            $ M_judith.set("sex sequence locked", False)
                                            call expression game.dialog_select("girls_lockerroom_judith_toilet_first_yes") from _call_expression_1075
                                            $ M_judith.set("in bathroom", False)
                                            $ M_judith.unforce()
                                        "We should stop.":

                                            call expression game.dialog_select("girls_lockerroom_judith_toilet_first_should_stop") from _call_expression_1076
                                "I can't.":

                                    call expression game.dialog_select("girls_lockerroom_judith_toilet_first_cant") from _call_expression_1077
                        "We should leave.":

                            call expression game.dialog_select("girls_lockerroom_judith_toilet_should_leave") from _call_expression_1078
                "I know...":

                    call expression game.dialog_select("girls_lockerroom_judith_toilet_first_ugly") from _call_expression_1079
            hide player
            hide judith
            with dissolve
            jump expression game.dialog_select("left_hall_dialogue")
        else:

            call expression game.dialog_select("judith_toilet_replay") from _call_expression_1080
    else:
        call expression game.dialog_select("girls_lockerroom_judith_toilet_not_here") from _call_expression_1081
    jump expression game.dialog_select("girl_lockerroom_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
