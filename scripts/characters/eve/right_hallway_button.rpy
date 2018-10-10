label right_hall_eve_button:
    call expression game.dialog_select("button_eve_intro") from _call_expression_578
    menu:
        "Talent Show." if M_dewitt.is_state([S_dewitt_talent_show_ask, S_dewitt_talent_show_ask_eve]) or M_dewitt.is_set("talent helping kevin"):
            if M_dewitt.is_set("talent helping kevin"):
                call expression game.dialog_select("dewitt_talent_show_helping_kevin") from _call_expression_579
            else:

                call expression game.dialog_select("button_eve_talent_show_help") from _call_expression_580
                $ M_dewitt.trigger(T_dewitt_eves_agreement)

        "Art Pad." if M_ross.is_state(S_ross_find_art_pad):
            call expression game.dialog_select("button_eve_ross_find_art_pad") from _call_expression_581
            $ M_ross.trigger(T_ross_find_eve_backpack)

        "Backpack." if M_ross.is_state(S_ross_find_eve_backpack):
            if player.has_item("eve_backpack"):
                call expression game.dialog_select("button_eve_ross_find_eve_backpack_have_backpack") from _call_expression_582
                $ player.remove_item("eve_backpack")
                $ M_ross.trigger(T_ross_got_eve_backpack)
            else:

                call expression game.dialog_select("button_eve_ross_find_eve_backpack_no_backpack") from _call_expression_583

        "Drawing." if M_ross.is_state(S_ross_get_eve_drawing):
            call expression game.dialog_select("button_eve_ross_get_eve_drawing") from _call_expression_584

        "Model." if M_ross.is_state(S_ross_ask_model):
            call expression game.dialog_select("button_eve_ask_model") from _call_expression_585

        "Paint." if M_ross.is_state(S_ross_get_paint):
            call expression game.dialog_select("button_eve_ross_get_paint") from _call_expression_586
            $ L_tattooparlor.unlock()
            $ M_ross.trigger(T_ross_talk_to_grace)

        "Paint." if M_ross.is_state(S_ross_get_paint_grace):
            call expression game.dialog_select("button_eve_ross_get_paint_grace") from _call_expression_587
        "Nothing.":

            $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
