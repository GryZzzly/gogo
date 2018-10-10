label dianebedroom_dialogue:
    $ player.go_to(L_diane_bedroom)
    if aunt.started(aunt_drunken_splur):
        call expression game.dialog_select("dianes_bedroom_diane_drunken_splur_started") from _call_expression_2181
    $ game.main()

label diane_bedroom_dialogue:
    if aunt.known(aunt_drunken_splur) and not aunt.over(aunt_drunken_splur):
        call expression game.dialog_select("dianes_dialogue_diane_drunken_splur_known") from _call_expression_2182

        $ aunt_drunken_splur.finish()

    elif aunt.known(aunt_mouse_attack) and not aunt.over(aunt_mouse_attack):
        call expression game.dialog_select("dianes_dialogue_diane_mouse_attack_known") from _call_expression_2183

        $ aunt_mouse_attack.finish()
        $ aunt.complete_events(aunt_mouse_attack)
        call expression game.dialog_select("dianelobby_dialogue") from _call_expression_2184
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
