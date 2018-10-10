label ross_button_dialogue:
    if M_ross.is_state(S_ross_grab_clay):
        call expression game.dialog_select("button_ross_grab_clay") from _call_expression_2050

    elif M_ross.is_state(S_ross_find_partner):
        call expression game.dialog_select("button_ross_find_partner") from _call_expression_2051
        $ M_ross.trigger(T_ross_find_partner)

    elif M_ross.is_state(S_ross_ask_mia_partner):
        call expression game.dialog_select("button_ross_ask_mia_partner") from _call_expression_2052

    elif M_ross.is_state(S_ross_mia_is_partner):
        call expression game.dialog_select("button_ross_mia_is_partner") from _call_expression_2053
        $ M_ross.trigger(T_ross_find_art_pad)

    elif M_ross.is_state([S_ross_find_art_pad, S_ross_find_eve_backpack, S_ross_get_eve_drawing]):
        if player.has_item("art_pad"):
            call expression game.dialog_select("button_ross_found_art_pad") from _call_expression_2054
            $ M_ross.trigger(T_ross_mia_drawn)
            $ player.remove_item("art_pad")
            $ game.timer.tick()
        else:

            call expression game.dialog_select("button_ross_find_art_pad") from _call_expression_2055

    elif M_ross.is_state(S_ross_collage):
        call expression game.dialog_select("button_ross_collage") from _call_expression_2056
        $ M_ross.trigger(T_ross_find_magazines)
        $ player.remove_item("magazines")

    elif M_ross.is_state(S_ross_find_magazines):
        call expression game.dialog_select("button_ross_find_magazines") from _call_expression_2057

    elif M_ross.is_state(S_ross_make_collage):
        call expression game.dialog_select("button_ross_make_collage") from _call_expression_2058
        $ game.timer.tick()
        $ M_ross.trigger(T_ross_made_collage)

    elif M_ross.is_state(S_ross_need_easels):
        call expression game.dialog_select("button_ross_need_easels") from _call_expression_2059
        $ M_ross.trigger(T_ross_find_easels)

    elif M_ross.is_state(S_ross_get_easels):
        if not player.has_item("easels"):
            call expression game.dialog_select("button_ross_get_easels") from _call_expression_2060
        else:

            call expression game.dialog_select("button_ross_has_easels") from _call_expression_2061
            $ M_ross.trigger(T_ross_has_easels)
            $ player.remove_item("easels")

    elif M_ross.is_state(S_ross_ask_model):
        call expression game.dialog_select("button_ross_ask_model") from _call_expression_2062

    elif M_ross.is_state(S_ross_found_model):
        call expression game.dialog_select("button_ross_found_model") from _call_expression_2063
        $ persistent.cookie_jar["Ross"]["unlocked"] = True
        $ persistent.cookie_jar["Ross"]["gallery"]["01_unlocked"] = True
        $ game.timer.tick()
        $ M_ross.trigger(T_ross_paint_for_smith)

    elif M_ross.is_state(S_ross_need_linens):
        call expression game.dialog_select("button_ross_need_linens") from _call_expression_2064
        $ M_ross.trigger(T_ross_find_linens)

    elif M_ross.is_state(S_ross_get_linens):
        if player.has_item("linens"):
            call expression game.dialog_select("button_ross_has_linens") from _call_expression_2065
            $ M_ross.trigger(T_ross_find_paint)
            $ player.remove_item("linens")
        else:

            call expression game.dialog_select("button_ross_get_linens") from _call_expression_2066

    elif M_ross.is_state(S_ross_get_paint):
        call expression game.dialog_select("button_ross_get_paint_grace_reminder") from _call_expression_2067

    elif M_ross.is_state(S_ross_get_paint_grace):
        if player.has_item("paint"):
            call expression game.dialog_select("button_ross_get_paint_grace") from _call_expression_2068
            call screen art_minigame
        else:

            call expression game.dialog_select("button_ross_get_paint_grace_reminder") from _call_expression_2069

    elif M_ross.is_state(S_ross_waiting_for_contest):
        call expression game.dialog_select("button_ross_waiting_for_contest") from _call_expression_2070

    elif M_ross.is_state(S_ross_contest):
        call expression game.dialog_select("button_ross_contest") from _call_expression_2071
        $ M_ross.trigger(T_ross_contest_over)

    elif M_ross.is_state(S_ross_paint_with_body):
        call expression game.dialog_select("button_ross_paint_with_body") from _call_expression_2072

    elif M_ross.is_state(S_ross_end):
        call expression game.dialog_select("button_ross_end_intro") from _call_expression_2073
        menu:
            "Yes.":
                call expression game.dialog_select("button_ross_end_intro") from _call_expression_2074
            "No.":

                call expression game.dialog_select("button_ross_end_intro") from _call_expression_2075
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
