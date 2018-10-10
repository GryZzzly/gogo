label judith_button_dialogue:
    if M_judith.is_state(S_judith_start):
        call expression game.dialog_select("judith_dialogue_start") from _call_expression_1086
    else:

        if player.location == L_school_lefthallway:
            call expression game.dialog_select("judith_dialogue_left_hallway_intro") from _call_expression_1087

        elif player.location == L_school_artclassroom:
            call expression game.dialog_select("judith_dialogue_art_classroom_intro") from _call_expression_1088
        menu:
            "Bathroom Fun" if not M_judith.is_set("sex sequence locked"):
                call expression game.dialog_select("judith_dialogue_bathroom_fun") from _call_expression_1089
                $ M_judith.set("in bathroom", True)
                $ M_judith.place(place = L_school_stall)
                $ M_judith.force(tod = [0,1])
                $ L_school_girlsroom.unlock()

            "Dictionary" if not M_bissette.is_set("judith return dictionary"):
                call expression game.dialog_select("judith_dialogue_dictionary_return") from _call_expression_1090
                $ M_bissette.set("judith return dictionary", True)

            "Dictionary" if M_bissette.is_state(S_bissette_find_full_dictionary):
                call expression game.dialog_select("judith_dialogue_bissette_find_full_dictionary") from _call_expression_1091
                $ M_bissette.trigger(T_bissette_judith_borrow_dictionary)

            "Flute." if M_dewitt.is_state([S_dewitt_find_flute, S_dewitt_judith_locker_search]):
                call expression game.dialog_select("judith_dialogue_dewitt_find_flute") from _call_expression_1092
                $ M_dewitt.trigger(T_dewitt_judith_flute)

            "Talent Show." if M_dewitt.is_set("talent ask judith"):
                if M_dewitt.is_set("talent helping kevin"):
                    call expression game.dialog_select("dewitt_talent_show_helping_kevin") from _call_expression_1093

                elif M_dewitt.is_set("talent helping eve"):
                    call expression game.dialog_select("dewitt_talent_show_helping_eve") from _call_expression_1094
                else:

                    call expression game.dialog_select("judith_dialogue_talent_show_help") from _call_expression_1095
                    $ M_dewitt.set("talent ask judith", False)

            "Glasses." if M_okita.is_state(S_okita_get_bifocal_lenses):
                call expression game.dialog_select("judith_dialogue_okita_get_bifocal_lenses") from _call_expression_1096
                $ M_okita.trigger(T_okita_take_picture_judith)

            "Picture." if M_okita.is_state(S_okita_take_picture_judith):
                call expression game.dialog_select("judith_dialogue_okita_take_picture_judith") from _call_expression_1097

            "Model." if M_ross.is_state(S_ross_ask_model):
                call expression game.dialog_select("judith_dialogue_ross_ask_model") from _call_expression_1098
                $ M_ross.trigger(T_ross_find_model)
            "Leave.":


                if player.location == L_school_lefthallway:
                    call expression game.dialog_select("judith_dialogue_left_hallway_leave") from _call_expression_1099

                elif player.location == L_school_artclassroom:
                    call expression game.dialog_select("judith_dialogue_art_classroom_leave") from _call_expression_1100
    hide judith
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
