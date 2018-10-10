label chad_button_dialogue:
    if M_ross.is_state(S_ross_get_eve_drawing) and not player.has_item("art_pad"):
        if not M_ross.get("talked with chad"):
            call expression game.dialog_select("button_chad_get_eve_drawing_first") from _call_expression_1934
            $ M_ross.set("talked with chad", True)

        elif not player.has_item("eve_drawing"):
            call expression game.dialog_select("button_chad_get_eve_drawing") from _call_expression_1935

        elif player.has_item("eve_drawing"):
            call expression game.dialog_select("button_chad_get_eve_drawing_completed") from _call_expression_1936
            $ player.remove_item("eve_drawing")
            $ player.get_item("art_pad")
    else:
        call expression game.dialog_select("button_chad_generic") from _call_expression_1937
        menu:
            "Nothing":
                call expression game.dialog_select("button_chad_nothing") from _call_expression_1938
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
