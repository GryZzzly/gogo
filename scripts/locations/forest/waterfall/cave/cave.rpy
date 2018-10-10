label cave_dialogue:
    $ player.go_to(L_cave)
    if M_okita.is_state(S_okita_get_ingredients):
        call expression game.dialog_select("cave_okita_get_ingredients") from _call_expression_715
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
