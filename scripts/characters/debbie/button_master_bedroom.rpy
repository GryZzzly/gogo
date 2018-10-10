label mom_dialogue_button_room:
    call expression game.dialog_select("debbie_dialogue_master_room_pre") from _call_expression_2083
    jump expression game.dialog_select("debbie_dialogue_master_room_options")

    label debbie_dialogue_master_room_after_kiss:
        call expression game.dialog_select("debbie_dialogue_master_room_after_kiss_dialogue") from _call_expression_2084
    menu debbie_dialogue_master_room_options:
        "Kiss.":
            call expression game.dialog_select("debbie_dialogue_master_room_kiss") from _call_expression_2085
            jump expression game.dialog_select("debbie_dialogue_master_room_after_kiss")
        "Shower.":

            call expression game.dialog_select("debbie_dialogue_master_room_shower") from _call_expression_2086
            jump expression game.dialog_select("mom_shower_question")
        "Have sex.":

            label sex_mom_bed_intro_3:
                if randomizer() <= 50:
                    call expression game.dialog_select("debbie_dialogue_master_room_sex_random_true") from _call_expression_2087
                else:

                    call expression game.dialog_select("debbie_dialogue_master_room_sex_random_false") from _call_expression_2088
                call expression game.dialog_select("debbie_dialogue_master_room_sex_after") from _call_expression_2089
            jump expression game.dialog_select("mom_sex")

        "Laundry." if M_mom.is_set("basement sex"):
            call expression game.dialog_select("debbie_dialogue_master_room_laundry_sex") from _call_expression_2090
            jump expression game.dialog_select("basement_mom_sex")

        "Watch a Movie." if not M_mom.is_set("movie night"):
            call expression game.dialog_select("debbie_dialogue_master_room_watch_movie") from _call_expression_2091
            $ M_mom.set("movie night", True)
        "Nevermind.":

            call expression game.dialog_select("debbie_dialogue_master_room_leave") from _call_expression_2092
    hide player
    hide debbie
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
