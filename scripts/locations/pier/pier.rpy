label pier_dialogue:
    $ player.go_to(L_pier)
    $ playSound(audio.a_pier, 1.0)
    if L_pier.first_visit:
        call expression game.dialog_select("pier_first_visit") from _call_expression_1721
        $ L_pier.visited()
    $ game.main()

label pier_board:
    if pier_board_first:
        call expression game.dialog_select("pier_board_first_visit") from _call_expression_1722
        $ pier_board_first = False
    scene expression game.timer.image("pier_board{}")
    pause
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
