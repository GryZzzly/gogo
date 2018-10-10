label smiths_frontyard_dialogue:
    $ player.go_to(L_smith_front)
    if M_roxxy.is_state(S_roxxy_sneak_into_smith) and not player.location.is_visited and game.timer.is_dark():
        $ player.location.visited()
        call expression game.dialog_select("smith_frontyard_sneaking") from _call_expression_485
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
