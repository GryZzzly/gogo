label ronda_button_dialogue:
    call expression game.dialog_select("ronda_dialogue_intro") from _call_expression_2145
    menu:
        "Talent Show." if M_dewitt.is_set("talent ask ronda"):
            if M_dewitt.is_set("talent helping kevin"):
                call expression game.dialog_select("dewitt_talent_show_helping_kevin") from _call_expression_2146

            elif M_dewitt.is_set("talent helping eve"):
                call expression game.dialog_select("dewitt_talent_show_helping_eve") from _call_expression_2147
            else:

                call expression game.dialog_select("ronda_dialogue_talent_show_help") from _call_expression_2148
                $ M_dewitt.set("talent ask ronda", False)

        "Model" if M_ross.is_state(S_ross_ask_model):
            call expression game.dialog_select("ronda_dialogue_model_help") from _call_expression_2149
        "Leave.":

            call expression game.dialog_select("ronda_dialogue_leave") from _call_expression_2150
    hide player
    hide ronda
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
