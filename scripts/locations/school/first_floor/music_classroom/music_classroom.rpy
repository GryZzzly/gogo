label music_classroom_dialogue:
    $ player.go_to(L_school_musicclassroom)
    call pa_announcement from _call_pa_announcement_8
    if player.location.is_here(M_dewitt):
        if M_dewitt.is_state(S_dewitt_intro):
            call expression game.dialog_select("music_classroom_dewitt_intro") from _call_expression_1259
            $ M_dewitt.trigger(T_dewitt_mc_welcome_back)
            $ game.timer.tick()

        elif M_dewitt.is_state(S_dewitt_smith_berating):
            call expression game.dialog_select("music_classroom_dewitt_smith_berating") from _call_expression_1260
            $ M_dewitt.trigger(T_dewitt_mc_overhear)

        elif M_dewitt.is_state(S_dewitt_talent_show_progress):
            call expression game.dialog_select("music_classroom_dewitt_talent_show_progress") from _call_expression_1261

            $ M_dewitt.trigger(T_dewitt_talent_hunt)

        elif M_dewitt.is_state(S_dewitt_music_sheets):
            call expression game.dialog_select("music_classroom_dewitt_music_sheets") from _call_expression_1262

            $ M_dewitt.trigger(T_dewitt_auditorium_problem)

        elif M_dewitt.is_state(S_dewitt_check_up):
            call expression game.dialog_select("music_classroom_dewitt_check_up") from _call_expression_1263

            $ player.go_to(L_school_hall)
            $ M_dewitt.trigger(T_dewitt_crying)

        elif M_dewitt.is_state(S_dewitt_find_dewitt):
            call expression game.dialog_select("music_classroom_dewitt_find_dewitt") from _call_expression_1264
            $ M_dewitt.trigger(T_dewitt_fetch_dewitt)

        elif M_dewitt.is_state(S_dewitt_talent_show_practice):
            call expression game.dialog_select("music_classroom_dewitt_talent_show_practice") from _call_expression_1265
            $ game.timer.tick()
            $ M_dewitt.trigger(T_dewitt_smith_payback_plan)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
