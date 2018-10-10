label beth_dialogue:
    call expression game.dialog_select("beth_dialogue_pre") from _call_expression_1510
    menu:
        "I don't know." if not M_mia.is_set("buy donuts"):
            call expression game.dialog_select("beth_dialogue_do_not_know") from _call_expression_1511

        "<>I want donuts! (50$)" if not player.has_money(50) and M_mia.is_set("buy donuts"):
            $ pass

        "I want donuts! (50$)" if player.has_money(50) and M_mia.is_set("buy donuts"):
            call expression game.dialog_select("beth_dialogue_want_donuts") from _call_expression_1512
            call screen donut_minigame
        "No, thanks.":

            call expression game.dialog_select("beth_dialogue_leave") from _call_expression_1513

    hide player
    hide xtra
    hide beth
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
