label dexter_court_dialogue:
    scene expression player.location.background_blur
    if M_roxxy.get("roxxy relationship") == 0:
        call expression game.dialog_select("button_dexter_intro_beginning") from _call_expression_1514
        $ game.main()
    else:
        if M_roxxy.get("roxxy relationship") == 5:
            call expression game.dialog_select("button_dexter_intro_final") from _call_expression_1515
        else:
            call expression game.dialog_select("button_dexter_intro") from _call_expression_1516
        menu:
            "Talent Show." if M_dewitt.is_set("talent ask dexter"):
                if M_dewitt.is_set("talent helping kevin"):
                    call expression game.dialog_select("dewitt_talent_show_helping_kevin") from _call_expression_1517

                elif M_dewitt.is_set("talent helping eve"):
                    call expression game.dialog_select("dewitt_talent_show_helping_eve") from _call_expression_1518
                else:

                    call expression game.dialog_select("button_dexter_talent_show") from _call_expression_1519
                    $ M_dewitt.set("talent ask dexter", False)

            "Challenge." if player.location == L_basketball_court:
                call expression game.dialog_select("button_dexter_challenge") from _call_expression_1520
                $ M_dexter.trigger(T_dex_challenge)

            "Push-ups." if M_roxxy.is_state(S_roxxy_do_pushups_intro, S_roxxy_do_pushups):
                if M_roxxy.is_state(S_roxxy_do_pushups):
                    call expression game.dialog_select("dexter_button_pushups") from _call_expression_1521
                    call screen pushups_minigame
                else:
                    call expression game.dialog_select("dexter_button_pushups_rematch") from _call_expression_1522
                    call screen pushups_minigame

            "Library Book." if M_bissette.between_states(S_bissette_jane_return_books, [S_bissette_got_eriks_martinez_books, S_bissette_got_martinez_eriks_books]) and not M_bissette.is_set("dexters book search"):
                call expression game.dialog_select("button_dexter_library_book") from _call_expression_1523
            "Still playing basketball":

                if M_roxxy.get("roxxy relationship") == 5:
                    call expression game.dialog_select("button_dexter_basketball_final") from _call_expression_1524
                else:
                    call expression game.dialog_select("button_dexter_basketball") from _call_expression_1525
            "Behaving yourself?" if M_roxxy.get("roxxy relationship")==5:
                call expression game.dialog_select("button_dexter_behaving_yourself") from _call_expression_1526

            "Run along now." if M_roxxy.get("roxxy relationship")==5:
                call expression game.dialog_select("button_dexter_run_along") from _call_expression_1527

            "Whatever." if M_roxxy.get("roxxy relationship") < 5:
                call expression game.dialog_select("button_dexter_whatever") from _call_expression_1528
    hide dexter
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
