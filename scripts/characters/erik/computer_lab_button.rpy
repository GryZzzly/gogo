label erik_dialogue:
    call expression game.dialog_select("erik_dialogue_intro") from _call_expression_504
    menu:
        "Lenses." if M_okita.is_state(S_okita_get_bifocal_lenses):
            call expression game.dialog_select("erik_dialogue_okita_get_bifocal_lenses") from _call_expression_505
        "Nothing":

            call expression game.dialog_select("erik_dialogue_leave") from _call_expression_506
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
