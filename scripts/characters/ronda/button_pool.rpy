label ronda_pool_button_dialogue:
    scene location_pool_closeup2
    if not M_cassie.get("had sex"):
        call expression game.dialog_select("ronda_pool_dialogue_pre_cassie_fun") from _call_expression_1833
    else:

        call expression game.dialog_select("ronda_pool_dialogue_after_cassie_fun") from _call_expression_1834

    hide player
    hide ronda
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
