label assembly_hall_dialogue:
    $ player.go_to(L_school_assemblyhall)
    call pa_announcement from _call_pa_announcement
    if M_dewitt.is_state(S_dewitt_graffiti_mess):
        call expression game.dialog_select("assembly_hall_dewitt_graffit_mess") from _call_expression_168
        $ M_dewitt.trigger(T_dewitt_bandit_clue)

    elif M_dewitt.is_state(S_dewitt_clean_graffiti) and player.has_item("beer"):
        call expression game.dialog_select("assembly_hall_dewitt_clean_graffit") from _call_expression_169

        $ M_dewitt.trigger(T_dewitt_fixed_auditorium)
        $ player.remove_item("beer")

    elif M_dewitt.is_state(S_dewitt_show_auditorium):
        call expression game.dialog_select("assembly_hall_dewitt_show_auditorium") from _call_expression_170
        $ game.timer.tick(2)
        $ M_dewitt.trigger(T_dewitt_talent_show_uncancelled)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
