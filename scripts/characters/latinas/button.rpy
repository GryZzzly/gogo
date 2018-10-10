label latinas_button_dialogue:
    scene location_school_lockershowers_closeup
    if M_latinas.is_state(S_latinas_start) and game.timer.game_day() >= 1:
        call expression game.dialog_select("latinas_dialogue_shower") from _call_expression_1949
        $ persistent.cookie_jar["Latina Twins"]["unlocked"] = True
        $ persistent.cookie_jar["Latina Twins"]["gallery"]["01_unlocked"] = True
        $ M_latinas.trigger(T_latinas_showers)
        call expression game.dialog_select("office_dialogue") from _call_expression_1950
    else:

        call expression game.dialog_select("latinas_dialogue_leave") from _call_expression_1951
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
