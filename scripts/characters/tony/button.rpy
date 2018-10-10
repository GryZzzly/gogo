label tony_dialogue:
    call expression game.dialog_select("tony_dialogue_pre") from _call_expression_647
    if not M_tony.is_set("deliver") and player.transport_level > 0:
        call expression game.dialog_select("tony_dialogue_deliver_pizzas_first") from _call_expression_648
        $ M_tony.set("deliver", True)

    elif M_tony.is_set("deliver"):
        call expression game.dialog_select("tony_dialogue_deliver_pizzas_repeat") from _call_expression_649
    else:
        call expression game.dialog_select("tony_dialogue_default") from _call_expression_650

    hide player
    hide tony
    hide maria
    with dissolve
    hide xtra
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
