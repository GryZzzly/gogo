label roxxy_button_showers_dialogue:
    if M_roxxy.is_state(S_roxxy_check_on_roxxy):
        call expression game.dialog_select("button_roxxy_showers_check_on_roxxy") from _call_expression_1433
        $ M_roxxy.trigger(T_roxxy_go_to_cabin)
    elif M_roxxy.is_state(S_roxxy_in_cabin):
        call expression game.dialog_select("button_roxxy_showers_in_cabin") from _call_expression_1434
    elif M_roxxy.is_state(S_roxxy_get_new_bikini):
        call expression game.dialog_select("button_roxxy_showers_get_new_bikini") from _call_expression_1435
    elif M_roxxy.is_state(S_roxxy_get_oil) and player.has_item("massage_oil"):
        call expression game.dialog_select("button_roxxy_showers_get_oil") from _call_expression_1436
    elif M_roxxy.is_state(S_roxxy_get_oil) and not player.has_item("massage_oil"):
        call expression game.dialog_select("button_roxxy_showers_no_oil") from _call_expression_1437
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
