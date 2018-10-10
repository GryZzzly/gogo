label angelica_dialogue:
    if M_ross.is_state(S_ross_get_linens) and not player.has_item("linens"):
        call expression game.dialog_select("angelica_dialogue_ross_get_linens_pre") from _call_expression_640
        menu:
            "Linens":
                call expression game.dialog_select("angelica_dialogue_ross_get_linens") from _call_expression_641
                $ player.get_item("linens")

    elif M_mia.is_set("helen dialogue change"):
        call expression game.dialog_select("angelica_dialogue_change_pre") from _call_expression_642
        menu:
            "Talk.":
                call expression game.dialog_select("angelica_dialogue_change_talk") from _call_expression_643
            "Graveyard.":

                call expression game.dialog_select("angelica_dialogue_change_graveyard") from _call_expression_644
            "Nevermind.":

                call expression game.dialog_select("angelica_dialogue_change_leave") from _call_expression_645
    else:

        call expression game.dialog_select("angelica_dialogue_pre") from _call_expression_646
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
