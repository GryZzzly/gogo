label veronica_button_dialogue:
    call expression game.dialog_select("veronica_dialogue_pre") from _call_expression_1400
    menu:
        "Vegetable Stock" if M_okita.is_state(S_okita_get_ingredients):
            call expression game.dialog_select("veronica_dialogue_vegatable_stock") from _call_expression_1401
            $ M_okita.set("talked with veronica", True)

        "Bug spray?" if quest10 in quest_list and not infestation_done:
            call expression game.dialog_select("veronica_dialogue_bug_spray") from _call_expression_1402
            menu:
                "Large wings.":
                    call expression game.dialog_select("veronica_dialogue_bug_spray_large_wings") from _call_expression_1403
                "Pincers on back.":

                    call expression game.dialog_select("veronica_dialogue_bug_spray_pincers") from _call_expression_1404
                "White spots.":

                    call expression game.dialog_select("veronica_dialogue_bug_spray_white_spots") from _call_expression_1405
        "I'm fine.":

            call expression game.dialog_select("veronica_dialogue_leave") from _call_expression_1406

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
