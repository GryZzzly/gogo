label office_dialogue:
    $ player.go_to(L_school_smithoffice)
    if quest09_1 == True and quest09 not in completed_quests:
        call expression game.dialog_select("principals_office_delivery_invoice") from _call_expression_92

    elif M_dewitt.is_state([S_dewitt_paint_trail, S_dewitt_check_up]):
        call expression game.dialog_select("principals_office_dewitt_paint_trail") from _call_expression_93
        $ player.go_to(L_school_floor3)
        $ M_dewitt.trigger(T_dewitt_clue_dead_end)

    elif M_dewitt.is_state(S_dewitt_smith_office_trap):
        call expression game.dialog_select("principals_office_dewitt_smith_office_trap") from _call_expression_94
        $ player.remove_item("sticky_tape")
        $ player.go_to(L_map)

        $ game.timer.tick()
        $ M_dewitt.trigger(T_dewitt_trap_set)

    elif M_dewitt.is_state(S_dewitt_trap_check_up):
        call expression game.dialog_select("principals_office_dewitt_trap_check_up") from _call_expression_95
        $ player.go_to(L_school_floor3)
        $ M_dewitt.trigger(T_dewitt_trap_check_ok)

    elif M_dewitt.is_state(S_dewitt_office_night_visit_delay):
        call expression game.dialog_select("principals_office_dewitt_office_night_visit_delay") from _call_expression_96
        $ player.go_to(L_school_floor3)

    elif M_okita.is_state(S_okita_get_keycode) and game.timer.is_morning():
        call expression game.dialog_select("principals_office_okita_get_keycode_morning") from _call_expression_97
        $ player.go_to(L_school_floor3)
        $ game.main()

    elif M_okita.is_state(S_okita_get_keycode) and game.timer.is_afternoon():
        call expression game.dialog_select("principals_office_okita_get_keycode_afternoon") from _call_expression_98

    elif M_okita.is_state(S_okita_get_ingredients) and game.timer.is_morning():
        call expression game.dialog_select("principals_office_okita_get_ingredients_morning") from _call_expression_99
        $ player.go_to(L_school_floor3)
        $ game.main()

    elif M_latinas.is_state(S_latinas_caught):
        call expression game.dialog_select("principals_office_annie_trouble") from _call_expression_100
        $ persistent.cookie_jar["Annie"]["unlocked"] = True
        $ persistent.cookie_jar["Annie"]["gallery"]["01_unlocked"] = True
        $ M_latinas.trigger(T_latinas_annie_trouble)

    elif M_smith.is_state([S_smith_intro, S_smith_go_to_locker]):
        $ pass

    elif player.location.is_here(M_smith):
        if game.timer.is_dark():
            call expression game.dialog_select("principals_office_no_entry_night") from _call_expression_101
        else:
            call expression game.dialog_select("principals_office_no_entry") from _call_expression_102
        $ player.go_to(L_school_floor3)
        $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
