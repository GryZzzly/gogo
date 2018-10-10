default first_revealing = True

label home_kitchen_dialogue:
    $ player.go_to(L_home_kitchen)
    if not game.timer.is_dark():
        if game.timer.is_morning() and sister.over(sis_telescope01) and not sister.known(sis_breakfast):
            call expression game.dialog_select("kitchen_sis_telescope_1") from _call_expression_1119

            $ sister.add_event(sis_breakfast)
            $ game.main()

        elif M_mom.is_state(S_mom_start):
            call expression game.dialog_select("kitchen_mom_start") from _call_expression_1120
            call screen deb_name_input
            if deb_char_name.strip() == "":
                $ deb_char_name = "Debbie"
            $ config.replay_scope["deb_char_name"] = deb_char_name
            $ persistent.deb_char_name = deb_char_name
            $ deb = Character("[deb_char_name]", color="#ff6df0")
            $ M_mom.trigger(T_mom_breakfast)
            $ game.unlock_ui()
            $ L_map.unlock()
            $ game.main()

        elif M_mom.is_state(S_mom_dinner) and player.location.is_here(M_mom):
            call expression game.dialog_select("kitchen_mom_dinner") from _call_expression_1121
            $ M_mom.trigger(T_mom_dinner_help)

            jump home_livingroom_dialogue

        elif M_mom.is_state(S_mom_dinner_fish) and player.has_item("seatrout"):
            call expression game.dialog_select("kitchen_mom_dinner_fish") from _call_expression_1122
            $ player.remove_item("seatrout")
            $ M_mom.trigger(T_mom_dinner_fish_caught)
            $ game.timer.tick(2)

            $ player.go_to(L_home_entrance)

    if M_mom.is_state(S_mom_debt_call):
        call expression game.dialog_select("kitchen_mom_debt_call") from _call_expression_1123
        $ M_mom.trigger(T_mom_debt_help)

        $ game.main()

    elif M_mom.is_state(S_mom_diane_visit) and game.timer.is_evening():
        call expression game.dialog_select("kitchen_mom_diane_visit") from _call_expression_1124
        $ M_mom.trigger(T_mom_diane_chat)
        $ game.timer.tick()
        jump home_entrance
    $ game.main()

label mom_kissing_practice:
    call expression game.dialog_select("kitchen_mom_kissing_practice") from _call_expression_1125
    $ M_mom.trigger(T_mom_kiss)
    $ game.timer.tick()
    $ game.main()

label dishes_dialogue:
    call expression game.dialog_select("kitchen_mom_dishes") from _call_expression_1126
    menu:
        "Let me help.":
            call expression game.dialog_select("kitchen_mom_dishes_yes") from _call_expression_1127
            $ game.timer.tick()
            $ M_mom.trigger(T_mom_washed_dishes)
        "Nevermind.":

            call expression game.dialog_select("kitchen_mom_dishes_no") from _call_expression_1128
    $ M_mom.set("chores", False)
    $ game.main()

label sis_breakfast_force:
    call expression game.dialog_select("kitchen_sis_breakfast_force") from _call_expression_1129
    $ game.main()

label sis_breakfast_force_mom:
    call expression game.dialog_select("kitchen_sis_breakfast_force_mom") from _call_expression_1130
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
