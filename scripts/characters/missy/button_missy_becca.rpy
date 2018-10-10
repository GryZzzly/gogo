label missy_becca_button_dialogue:
    scene expression player.location.background_blur
    if M_roxxy.is_state(S_roxxy_chat_with_becca_missy):
        call expression game.dialog_select("button_missy_becca_chat_with_becca_missy") from _call_expression_477
        $ M_roxxy.trigger(T_roxxy_get_goldenschwagger)
    elif M_roxxy.is_state(S_roxxy_spin_bottle):
        if player.has_item("goldschwagger"):
            show player 5f with dissolve
            player_name "( I shouldn't bother them anymore. )"
            player_name "( I'll see them {b}Saturday afternoon at the beach{/b}. )"
            hide player with dissolve
        else:
            show player 5f with dissolve
            player_name "( I shouldn't bother them anymore. )"
            player_name "( I need to speak with {b}Captain Terry{/b} about this {b}GoldSchwagger{/b} stuff. )"
            hide player with dissolve
        $ game.main()
    else:
        if M_roxxy.between_states(S_roxxy_ask_exam_copy_delay, S_roxxy_invite_to_bikini_contest):
            call expression game.dialog_select("button_missy_becca_intro_rox11") from _call_expression_478
        elif not M_roxxy.finished_state(S_roxxy_ask_exam_copy_delay):
            call expression game.dialog_select("button_missy_becca_intro_0_1") from _call_expression_479
            $ game.main()
        else:
            call expression game.dialog_select("button_missy_becca_intro") from _call_expression_480
        menu:
            "You girls look nice." if M_roxxy.between_states(S_roxxy_ask_exam_copy_delay, S_roxxy_invite_to_bikini_contest):
                call expression game.dialog_select("button_missy_becca_look_nice") from _call_expression_481
            "I just wanted to say hi." if M_roxxy.between_states(S_roxxy_ask_exam_copy_delay, S_roxxy_invite_to_bikini_contest):
                call expression game.dialog_select("button_missy_becca_leave_rox11") from _call_expression_482
            "You both look beautiful today" if M_roxxy.finished_state(S_roxxy_invite_to_bikini_contest):
                call expression game.dialog_select("button_missy_becca_look_beautiful") from _call_expression_483
            "I'll see you around." if M_roxxy.finished_state(S_roxxy_invite_to_bikini_contest):
                call expression game.dialog_select("button_missy_becca_leave") from _call_expression_484
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
