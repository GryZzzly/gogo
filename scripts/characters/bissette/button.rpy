label bissette_button_dialogue:
    scene french_class_c
    if M_bissette.is_set("meet in office"):
        call expression game.dialog_select("bissette_dialogue_meet_in_office") from _call_expression_6

    elif M_bissette.is_state(S_bissette_check_dictionary):
        call expression game.dialog_select("bissette_dialogue_check_dictionary") from _call_expression_7
        $ M_bissette.trigger(T_bissette_missing_pages)
    else:

        call expression game.dialog_select("bissette_dialogue_intro") from _call_expression_8
        menu:
            "Food Assignment." if M_bissette.between_states(S_bissette_find_food_book, S_bissette_french_food_assignment):
                call expression game.dialog_select("bissette_dialogue_food_assignment_intro") from _call_expression_9
                if not M_bissette.is_state(S_bissette_french_food_assignment):
                    call expression game.dialog_select("bissette_dialogue_food_assignment_prepare_assignment") from _call_expression_10
                else:

                    call expression game.dialog_select("bissette_dialogue_food_assignment_do_assignment") from _call_expression_11

            "Poem Assignment." if M_bissette.between_states(S_bissette_find_poem_reference_book, S_bissette_print_poem_assignment):
                if M_bissette.between_states(S_bissette_find_poem_reference_book, S_bissette_do_poem_assignment):
                    call expression game.dialog_select("bissette_dialogue_poem_assignment_intro") from _call_expression_12
                    if M_bissette.is_state(S_bissette_do_poem_assignment):
                        call expression game.dialog_select("bissette_dialogue_poem_assignment_do_assignment") from _call_expression_13
                else:

                    call expression game.dialog_select("bissette_dialogue_poem_assignment_print_assignment") from _call_expression_14

            "Private Tutoring." if M_bissette.is_state(S_bissette_end) and not M_bissette.is_set("night visit"):
                call expression game.dialog_select("bissette_dialogue_private_tutoring") from _call_expression_15
                $ M_bissette.set("night visit", True)

            "Tutoring." if M_bissette.between_states(S_bissette_tutoring, S_bissette_fix_printer):
                if M_bissette.is_state(S_bissette_tutoring):
                    call expression game.dialog_select("bissette_dialogue_tutoring") from _call_expression_16
                    $ M_bissette.trigger(T_bissette_require_dictionary)

                elif M_bissette.is_state([S_bissette_find_dictionary, S_bissette_get_dictionary]):
                    call expression game.dialog_select("bissette_dialogue_get_dictionary") from _call_expression_17
                else:

                    call expression game.dialog_select("bissette_dialogue_replace_missing_pages") from _call_expression_18
            "Chat.":

                call expression game.dialog_select("bissette_dialogue_chat") from _call_expression_19
            "Not really.":

                call expression game.dialog_select("bissette_dialogue_leave") from _call_expression_20

    hide player
    hide teacher
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
