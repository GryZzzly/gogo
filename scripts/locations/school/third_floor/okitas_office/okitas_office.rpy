label okita_office_dialogue:
    $ player.go_to(L_school_okitaoffice)
    if game.timer.is_night():
        call expression game.dialog_select("bissette_office_night_lock") from _call_expression_1939
        $ player.go_to(L_school_floor3)

    if M_okita.is_state(S_okita_enter_office) and not game.timer.is_dark():
        call expression game.dialog_select("okitas_office_enter_office") from _call_expression_1940
        $ M_okita.trigger(T_okita_entered_office)

    elif M_okita.is_state(S_okita_enter_office) and game.timer.is_dark():
        call expression game.dialog_select("okitas_office_blocked_entrance") from _call_expression_1941
        $ player.go_to(L_school_floor3)
        $ game.main()

    elif M_okita.is_state(S_okita_get_items_from_office):

        if player.has_item("blueprints") and player.has_item("labcoat") and player.has_item("goggles"):
            call expression game.dialog_select("okitas_office_okita_got_all_items") from _call_expression_1942

            $ M_okita.trigger(T_okita_got_items)

    elif M_okita.is_state(S_okita_xray_perving):
        call expression game.dialog_select("okitas_office_okita_xray_perving") from _call_expression_1943
        $ M_okita.trigger(T_okita_xray_perving_aftermath)

        $ game.timer.tick(2)
        $ player.go_to(L_map)
        $ game.main()

    elif M_okita.is_state(S_okita_belt_assembled):
        call expression game.dialog_select("okitas_office_okita_belt_assembled") from _call_expression_1944
        $ M_okita.trigger(T_okita_belt_assembled_aftermath)

        $ game.timer.tick(2)
        $ player.go_to(L_map)
        $ game.main()

    elif M_okita.is_state(S_okita_extract_cum) and game.timer.is_evening():
        call expression game.dialog_select("okitas_office_extract_cum") from _call_expression_1945
        $ M_okita.trigger(T_okita_extracted_cum)
        call expression game.dialog_select("okitas_office_start_brewing") from _call_expression_1946
        call screen science_minigame

    elif M_okita.is_state(S_okita_start_mixing) and game.timer.is_evening():
        call expression game.dialog_select("okitas_office_start_brewing_again") from _call_expression_1947
        call screen science_minigame

    elif M_okita.is_state(S_okita_is_hypersexual) and game.timer.is_evening():
        call expression game.dialog_select("okitas_office_okita_is_hypersexual") from _call_expression_1948
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
