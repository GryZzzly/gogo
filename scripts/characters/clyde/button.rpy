label clyde_button_dialogue:
    scene expression player.location.background_blur
    if M_roxxy.is_state(S_roxxy_meeting_clyde) and game.timer.is_dark():
        call expression game.dialog_select("button_clyde_roxxy_meeting_buyer_dark") from _call_expression_510
        $ M_roxxy.trigger(T_roxxy_meet_buyer)
        $ game.sleep_lock = True
        $ player.go_to(L_park)
        $ game.main()

    elif M_roxxy.finished_state(S_roxxy_picnic_done) and not M_clyde.get("cletus"):
        $ M_clyde.set("cletus", True)
        call expression game.dialog_select("button_clyde_cletus_introduce") from _call_expression_511
        $ game.main()
    else:
        if not M_roxxy.finished_state(S_roxxy_missing_outfit_delay):
            call expression game.dialog_select("button_clyde_intro_0") from _call_expression_512
        elif M_roxxy.between_states(S_roxxy_missing_outfit_delay, S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_clyde_intro_1") from _call_expression_513
        else:
            call expression game.dialog_select("button_cletus_intro") from _call_expression_514
        menu:
            "Crystal in Prison." if M_roxxy.is_state(S_roxxy_get_evidence):
                call expression game.dialog_select("button_clyde_roxxy_get_evidence_intro") from _call_expression_515
                menu:
                    "What about {b}Roxxy{/b}?":
                        if player.has_required_chr(7):
                            call expression game.dialog_select("button_clyde_roxxy_get_evidence_about_roxxy_pass") from _call_expression_516
                            $ M_roxxy.trigger(T_roxxy_sell_meth)
                        else:
                            call expression game.dialog_select("button_clyde_roxxy_get_evidence_about_roxxy_fail") from _call_expression_517
                        $ game.main()
                    "Nevermind.":
                        call expression game.dialog_select("button_clyde_roxxy_get_evidence_nevermind") from _call_expression_518

            "Selling the Meth" if M_roxxy.is_state(S_roxxy_selling_meth_ask_roxxy):
                call expression game.dialog_select("button_clyde_roxxy_selling_meth_ask_roxxy") from _call_expression_519

            "Selling the Meth" if M_roxxy.is_state(S_roxxy_selling_meth):
                call expression game.dialog_select("button_clyde_roxxy_selling_meth") from _call_expression_520
                $ M_roxxy.trigger(T_roxxy_meet_clyde)

            "Selling the Meth" if M_roxxy.is_state(S_roxxy_meeting_clyde):
                call expression game.dialog_select("button_clyde_roxxy_meeting_buyer") from _call_expression_521

            "Wanna hit the range?" if M_roxxy.finished_state(S_roxxy_beat_clyde) and L_trailer_tractor.is_here(M_clyde):
                jump shooting_range_dialogue

            "Fine, how are you?" if not M_clyde.get("cletus"):
                call expression game.dialog_select("button_clyde_how_are_you") from _call_expression_522

            "Where are you from?" if not M_clyde.get("cletus"):
                call expression game.dialog_select("button_clyde_where_are_you_from") from _call_expression_523

            "This is ridiculous, I know you're {b}Clyde{/b}!" if M_clyde.get("cletus"):
                call expression game.dialog_select("button_clyde_know_youre_clyde") from _call_expression_524

            "What's going on in there?" if L_trailer_shack.is_here(M_clyde) and not L_trailer_shack_interior.locked:
                call expression game.dialog_select("button_clyde_whats_going_on") from _call_expression_525

            "Nice tractor" if L_trailer_tractor.is_here(M_clyde):
                call expression game.dialog_select("button_clyde_nice_tractor") from _call_expression_526

            "See ya, {b}Clyde{/b}" if not M_clyde.get("cletus"):
                call expression game.dialog_select("button_clyde_see_ya") from _call_expression_527
                $ game.main()

            "Nevermind." if M_clyde.get("cletus"):
                call expression game.dialog_select("button_clyde_nevermind") from _call_expression_528
                $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
