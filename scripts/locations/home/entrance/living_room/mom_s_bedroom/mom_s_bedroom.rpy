label mom_bedroom_screen:
    $ player.go_to(L_home_mombedroom)
    $ game.main()

label mom_bedroom:
    $ player.go_to(L_home_mombedroom)
    if M_mom.is_state(S_mom_spy) and not game.timer.is_dark():
        call expression game.dialog_select("mom_spy") from _call_expression_707
        $ M_mom.trigger(T_mom_caught_spying)
        $ persistent.cookie_jar["Debbie"]["unlocked"] = True
        $ persistent.cookie_jar["Debbie"]["gallery"]["01_unlocked"] = True
        $ game.timer.tick()

    elif M_mom.is_state(S_mom_panties_masturbation_again):
        call expression game.dialog_select("moms_bedroom_mom_panties_masturbation_again") from _call_expression_708

    elif M_mom.is_state(S_mom_sleepover_wakeup):
        call expression game.dialog_select("moms_bedroom_mom_sleepover_makeup") from _call_expression_709
        $ M_mom.trigger(T_mom_sleepover_morning)
        $ player.go_to(L_home_livingroom)

    elif M_mom.is_state(S_mom_dinner_outfit):
        call expression game.dialog_select("moms_bedroom_mom_dinner_outfit") from _call_expression_710
        $ M_mom.trigger(T_mom_dinner_outfit_check)

        menu:
            "Ask {b}[deb_name]{/b}.":
                call expression game.dialog_select("moms_bedroom_mom_dinner_outfit_ask") from _call_expression_711
            "Just leave.":

                $ pass

        jump expression game.dialog_select("home_livingroom_dialogue")

    elif M_mom.is_state(S_mom_midnight_swim_after):
        $ player.go_to(L_home_livingroom)
        call expression game.dialog_select("moms_bedroom_mom_midnight_swim_after") from _call_expression_712

    elif game.timer.is_dark():
        call expression game.dialog_select("moms_bedroom_night") from _call_expression_713

    elif not M_mom.is_set("fetch lotion") and not M_mom.is_set("sleep together"):
        call expression game.dialog_select("moms_bedroom_mom_is_set_lotion") from _call_expression_714
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
