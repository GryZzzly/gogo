label dewitt_button_dialogue_lounge:
    call expression game.dialog_select("dewitt_dialogue_lounge_intro") from _call_expression_1452

    if player.has_required_int(5):
        call expression game.dialog_select("dewitt_dialogue_lounge_stat_pass") from _call_expression_1453
        call expression "player_ross_magazines_{}_left".format(M_ross.get("magazines remaining")) from _call_expression_1454
        $ M_ross.set("magazine dewitt", True)
    else:

        call expression game.dialog_select("dewitt_dialogue_lounge_stat_fail") from _call_expression_1455
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
