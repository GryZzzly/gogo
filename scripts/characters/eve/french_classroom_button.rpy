label eve_classroom_dialogue:
    scene classroom
    if M_eve.is_state(S_eve_intro):
        call expression game.dialog_select("eve_classroom_dialogue_eve_intro") from _call_expression_770
        $ L_park.unlock()
        $ M_eve.trigger(T_eve_park_hangout)
    else:

        call expression game.dialog_select("eve_classroom_dialogue_intro") from _call_expression_771
        menu eve_dialogue_options:
            "Talent Show." if M_dewitt.is_state([S_dewitt_talent_show_ask, S_dewitt_talent_show_ask_eve]) or M_dewitt.is_set("talent helping kevin"):
                if M_dewitt.is_set("talent helping kevin"):
                    call expression game.dialog_select("dewitt_talent_show_helping_kevin") from _call_expression_772
                else:

                    call expression game.dialog_select("eve_classroom_dialogue_talent_show_help") from _call_expression_773
                    $ M_dewitt.trigger(T_dewitt_eves_agreement)

            "Adhesive." if M_dewitt.is_state(S_dewitt_science_adhesive):
                call expression game.dialog_select("eve_classroom_dialogue_adehsive") from _call_expression_774
            "{b}Miss Bissette's{/b} reward.":

                call expression game.dialog_select("eve_classroom_dialogue_bissettes_reward") from _call_expression_775
                call expression game.dialog_select("eve_dialogue_options") from _call_expression_776
            "Hang out.":

                call expression game.dialog_select("eve_classroom_dialogue_hang_out") from _call_expression_777
                call expression game.dialog_select("eve_dialogue_options") from _call_expression_778
            "Nothing.":

                call expression game.dialog_select("eve_classroom_dialogue_leave") from _call_expression_779
    hide evedesk with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
