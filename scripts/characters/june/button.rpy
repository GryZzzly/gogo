label june_dialogue:
    if M_bissette.is_state(S_bissette_fix_printer):
        if M_bissette.is_set("printer fix fail"):
            call expression game.dialog_select("june_dialogue_bissette_fix_printer_repeat") from _call_expression_788
        else:

            call expression game.dialog_select("june_dialogue_bissette_fix_printer_first") from _call_expression_789

        if player.stats.str() < 2:
            call expression game.dialog_select("june_dialogue_bissette_fix_printer_fail") from _call_expression_790
            $ M_bissette.trigger(T_bissette_june_printer_error)
        else:

            call expression game.dialog_select("june_dialogue_bissette_fix_printer_pass") from _call_expression_791
            $ M_bissette.trigger(T_bissette_june_scan_pages)
        $ game.main()

    elif M_okita.is_state(S_okita_faptic_engine):
        call expression game.dialog_select("june_dialogue_okita_faptic_engine") from _call_expression_792
        $ M_okita.trigger(T_okita_faptic_get_controller)

    elif M_okita.is_state(S_okita_get_controller_info):
        call expression game.dialog_select("june_dialogue_okita_get_controller_info") from _call_expression_793

    elif M_okita.is_state(S_okita_get_controller) and player.has_item("controller"):
        call expression game.dialog_select("june_dialogue_okita_has_controller") from _call_expression_794
        $ player.remove_item("controller")
        $ player.get_item("faptic_engine")
        $ game.main()
    else:

        scene school_computer_b
        if June.completed(june_mc_help):
            call expression game.dialog_select("june_dialogue_mc_intro") from _call_expression_795
        else:

            call expression game.dialog_select("june_dialogue_intro") from _call_expression_796
        menu:
            "Lenses." if M_okita.is_state(S_okita_get_bifocal_lenses):
                call expression game.dialog_select("june_dialogue_okita_get_bifocal_lenses") from _call_expression_797

            "Model." if M_ross.is_state(S_ross_ask_model):
                call expression game.dialog_select("june_dialogue_ross_ask_model") from _call_expression_798

            "Hang out." if June.completed(june_mc_help) and not june_hang_out:
                call expression game.dialog_select("june_dialogue_hang_out") from _call_expression_799
                if not June.known(june_mc_help_2):
                    $ June.add_event(june_mc_help_2)
                    $ M_june.place(place = L_home_bedroom, condition = "june_hang_out")
                    $ M_june.force(tod = 2)
                $ june_hang_out = True

            "Cosplay." if June.started(june_cosplay) and not player.has_item("orcette_cosplay"):
                call expression game.dialog_select("june_dialogue_cosplay_no_costume") from _call_expression_800

            "Cosplay." if June.started(june_cosplay) and player.has_item("orcette_cosplay"):
                call expression game.dialog_select("june_dialogue_cosplay_has_costume") from _call_expression_801
                $ june_hang_out = True
                $ player.remove_item("orcette_cosplay")
                $ june_cosplay.finish()

            "Ask about class." if June.completed(june_intro) and (not June.known(june_erik_help) and not June.known(june_mc_help)):
                if not June.known(june_intro_2):
                    $ June.add_event(june_intro_2)
                $ june_intro_2.finish()
                call expression game.dialog_select("june_dialogue_ask_about_class") from _call_expression_802
                $ config.skipping = None
                show popup_warning at truecenter with dissolve
                $ renpy.pause(3, hard=True)
                pause
                hide popup_warning with dissolve
                menu june_route_split:
                    "My friend {b}Erik{/b}!":
                        hide screen save
                        call expression game.dialog_select("june_dialogue_erik_help") from _call_expression_803
                        $ June.add_event(june_erik_help)
                    "I'll play!":

                        hide screen save
                        call expression game.dialog_select("june_dialogue_mc_help") from _call_expression_804
                        $ June.add_event(june_mc_help)
                    "Save Menu.":

                        show screen save
                        pause
                        hide screen save
                        call expression game.dialog_select("june_route_split") from _call_expression_805
            "Nothing.":

                call expression game.dialog_select("june_dialogue_leave") from _call_expression_806
    hide june
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
