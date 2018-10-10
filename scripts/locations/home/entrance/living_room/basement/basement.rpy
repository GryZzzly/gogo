label home_basement_dialogue:
    $ player.go_to(L_home_basement)
    if M_mom.is_state(S_mom_wash_clothes):
        call expression game.dialog_select("basement_mom_wash_clothes") from _call_expression_507
        $ M_mom.trigger(T_mom_clean_clothes)
        $ player.go_to(L_home_bedroom)

        $ game.timer.tick()

    elif M_mom.is_state(S_mom_close_valve):
        call expression game.dialog_select("basement_mom_close_valve") from _call_expression_508

    elif M_mom.is_state(S_mom_lotion_adventure) and M_mom.is_set("retrieved lotion"):
        jump expression game.dialog_select("mom_lotion_fun")

    elif M_mom.is_state(S_mom_give_laundry):
        call expression game.dialog_select("basement_mom_give_laundry") from _call_expression_509
        jump expression game.dialog_select("basement_mom_sex")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
