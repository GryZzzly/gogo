label kevin_button_dialogue:
    scene cafeteria_b
    if M_ross.is_state(S_ross_find_magazines) and not M_ross.get("magazine kevin"):
        call expression game.dialog_select("kevin_dialogue_ross_find_magazines") from _call_expression_1969
        call expression "player_ross_magazines_{}_left".format(M_ross.get("magazines remaining")) from _call_expression_1970
        $ M_ross.set("magazine kevin", True)

    elif M_ross.is_state(S_ross_ask_model):
        call expression game.dialog_select("kevin_dialogue_ross_ask_model") from _call_expression_1971
    else:

        call expression game.dialog_select("kevin_dialogue_intro") from _call_expression_1972
        if erik.completed(erik_favor_2):
            call expression game.dialog_select("kevin_dialogue_erik_favor_2_completed") from _call_expression_1973
        kev "Anything you wanted to talk about?"
        show kevin 23
        menu:
            "Guitar." if M_dewitt.is_state(S_dewitt_kevin_give_guitar):
                call expression game.dialog_select("kevin_dialogue_dewitt_kevin_give_guitar") from _call_expression_1974
                $ player.remove_item("guitar")
                if M_dewitt.is_set("talent ask eve"):
                    $ M_dewitt.trigger(T_dewitt_find_last_talent)
                else:
                    $ M_dewitt.trigger(T_dewitt_give_fender_guitar)

            "Talent Show." if M_dewitt.between_states(S_dewitt_talent_show_ask, S_dewitt_replace_guitar) or M_dewitt.is_set("talent helping eve"):
                if M_dewitt.is_set("talent helping eve"):
                    call expression game.dialog_select("dewitt_talent_show_helping_eve") from _call_expression_1975

                elif M_dewitt.is_state([S_dewitt_talent_show_ask, S_dewitt_talent_show_ask_kevin]):
                    call expression game.dialog_select("kevin_dialogue_talent_show_help") from _call_expression_1976
                    $ M_dewitt.trigger(T_dewitt_kevins_agreement)

                elif M_dewitt.is_state(S_dewitt_replace_guitar):
                    call expression game.dialog_select("kevin_dialogue_talent_show_replace_guitar") from _call_expression_1977
                else:

                    call expression game.dialog_select("kevin_dialogue_talent_show") from _call_expression_1978

            "Adhesive." if M_dewitt.is_state(S_dewitt_science_adhesive):
                call expression game.dialog_select("kevin_dialogue_dewitt_science_adhesive") from _call_expression_1979
            "Nothing":

                call expression game.dialog_select("kevin_dialogue_leave") from _call_expression_1980

    hide kevin
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
