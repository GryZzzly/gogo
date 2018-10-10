label sis_bedroom_dialogue:
    $ player.go_to(L_home_sisbedroom)




    scene expression game.timer.image("backgrounds/location_home_jennybedroom{}.jpg")
    if not game.timer.is_dark():
        if sis_bedroom_count == 0:
            call expression game.dialog_select("sis_bedroom_sis_not_in_room") from _call_expression_2115
            $ M_jenny.place(place = L_NULL)
            $ M_jenny.force(tod = [0,1])

        elif M_bissette.is_state(S_bissette_roxxy_jenny_spying):
            call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying") from _call_expression_2116
            $ M_bissette.trigger(T_bissette_roxxy_jenny_spied)

            $ game.timer.tick()
            $ player.go_to(L_home_hallway)

        elif sister.started(sis_hallway02) and sister.over(sis_telescope02):
            call expression game.dialog_select("sis_bedroom_sis_hallway_2_started") from _call_expression_2117
            jump expression game.dialog_select("hallway_dialogue")

        elif sis_bedroom_count == 1 and not sis_panties_trade and look_for_panties:

            $ M_jenny.unforce()
            call expression game.dialog_select("sis_bedroom_sis_caught_stealing_panties") from _call_expression_2118
            $ bedtable01_count = 1
            if player.has_money(100):
                menu:
                    "Here's $100.":
                        $ player.spend_money(100)
                        $ player.get_item("panties")
                        $ sis_panty01.finish()
                        $ completed_quests.append(quest07)
                        $ sis_panties_bought = True
                        $ sis_bedroom_count = 2
                        $ sis_panties_trade = True
                        call expression game.dialog_select("sis_bedroom_sis_caught_stealing_panties_buy_panties") from _call_expression_2119
                        jump expression game.dialog_select("hallway_dialogue")
                    "I don't need it.":

                        call expression game.dialog_select("sis_bedroom_sis_caught_stealing_panties_do_not_buy_panties") from _call_expression_2120
                        jump expression game.dialog_select("hallway_dialogue")
            else:

                menu:
                    "I don't have enough.":
                        call expression game.dialog_select("sis_bedroom_sis_caught_stealing_panties_cant_buy_panties") from _call_expression_2121
                        jump expression game.dialog_select("hallway_dialogue")

        elif sister.started(sis_final):
            call expression game.dialog_select("sis_bedroom_sis_final_started") from _call_expression_2122
            $ sis_final.finish()

            jump expression game.dialog_select("hallway_dialogue")

        elif M_bissette.is_state(S_bissette_roxxy_cheerleader_deal):
            call expression game.dialog_select("jennys_bedroom_bissette_roxxy_cheerleader_deal") from _call_expression_2123
            $ M_bissette.trigger(T_bissette_jenny_deal)
        else:

            $ game.main()

    elif game.timer.is_dark() and not in_sis_room:
        call expression game.dialog_select("sis_bedroom_sis_sleeping") from _call_expression_2124
    $ in_sis_room = False
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
