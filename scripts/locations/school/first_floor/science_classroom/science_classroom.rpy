label science_classroom_dialogue:
    $ player.go_to(L_school_scienceclassroom)
    call pa_announcement from _call_pa_announcement_10
    if M_okita.is_state(S_okita_start) and not game.timer.is_dark():
        call expression game.dialog_select("science_classroom_first_visit") from _call_expression_1480
        pause 0.5
        call expression game.dialog_select("science_classroom_cutscene") from _call_expression_1481
        pause 0.5
        call expression game.dialog_select("science_classroom_after_cutscene") from _call_expression_1482
        $ M_okita.trigger(T_okita_intro)
        $ game.timer.tick()
        if game.timer.is_dark():
            $ player.go_to(L_map)
            $ game.main()

    elif M_okita.is_state(S_okita_has_items):
        $ player.remove_item("labcoat")
        $ player.remove_item("blueprints")
        $ player.remove_item("goggles")
        call expression game.dialog_select("science_classroom_okita_has_items") from _call_expression_1483
        $ M_okita.trigger(T_okita_foam_misshap)
        $ player.go_to(L_map)
        $ game.main()

    elif M_dewitt.is_state(S_dewitt_science_adhesive):
        call expression game.dialog_select("science_classroom_dewitt_science_adhesive") from _call_expression_1484
        $ player.go_to(L_map)
        $ player.get_item("sticky_tape")
        $ M_dewitt.trigger(T_dewitt_sticky_tape_get)

    elif M_mia.is_state(S_mia_return_favor):
        call expression game.dialog_select("science_classroom_mia_return_favor") from _call_expression_1485
        $ M_mia.trigger(T_mia_night_invite)

    elif M_mia.is_state(S_mia_strip_aftermath) and M_mia.is_set('story delay'):
        call expression game.dialog_select("science_classroom_mia_strip_aftermath") from _call_expression_1486
        $ M_mia.trigger(T_mia_grounded)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
