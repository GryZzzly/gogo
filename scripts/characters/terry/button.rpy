label terry_button_dialogue:
    $ playMusic(audio.m_pier)
    scene expression game.timer.image("pier_closeup{}")
    if M_terry.is_state(S_terry_start):
        call expression game.dialog_select("terry_dialogue_terry_start") from _call_expression_1182
        $ M_terry.trigger(T_terry_intro)

    elif M_terry.is_state(S_terry_nemesis):
        call expression game.dialog_select("terry_dialogue_terry_nemesis") from _call_expression_1183
        $ M_terry.trigger(T_terry_tigger)

    elif M_terry.is_state(S_terry_retire) and player.has_item("tigger"):
        call expression game.dialog_select("terry_dialogue_terry_retire") from _call_expression_1184
        $ M_terry.trigger(T_terry_overjoyed_swim)
        $ M_aqua.trigger(T_aqua_test_pass)
        $ player.remove_item("tigger")
        $ player.go_to(L_map)

    elif M_terry.is_state(S_terry_tigger_sign):
        call expression game.dialog_select("terry_dialogue_terry_tigger_sign") from _call_expression_1185
        $ M_terry.trigger(T_terry_hang_tigger)
    else:

        call expression game.dialog_select("terry_dialogue_intro") from _call_expression_1186
        menu:
            "Buy some fish ($100)":
                call expression game.dialog_select("terry_dialogue_buy_fish") from _call_expression_1187
                menu:
                    "Seatrout":
                        $ fish = "Seatrout"
                        call expression game.dialog_select("terry_dialogue_buy_fish_buy") from _call_expression_1188
                    "Snapper":

                        $ fish = "Snapper"
                        call expression game.dialog_select("terry_dialogue_buy_fish_buy") from _call_expression_1189
                    "Mackerel":

                        $ fish = "Mackerel"
                        call expression game.dialog_select("terry_dialogue_buy_fish_buy") from _call_expression_1190
                    "Nevermind":

                        call expression game.dialog_select("terry_dialogue_buy_fish_nevermind") from _call_expression_1191

            "Sell some fish (80$)" if player.has_item("seatrout", "snapper", "mackerel"):
                call expression game.dialog_select("terry_dialogue_sell_fish") from _call_expression_1192
                menu:
                    "Seatrout" if player.has_item("seatrout"):
                        $ fish = "Seatrout"
                        call expression game.dialog_select("terry_dialogue_sell_fish_sell") from _call_expression_1193

                    "Snapper" if player.has_item("snapper"):
                        $ fish = "Snapper"
                        call expression game.dialog_select("terry_dialogue_sell_fish_sell") from _call_expression_1194

                    "Mackerel" if player.has_item("mackerel"):
                        $ fish = "Mackerel"
                        call expression game.dialog_select("terry_dialogue_sell_fish_sell") from _call_expression_1195
                    "Nevermind":

                        call expression game.dialog_select("terry_dialogue_sell_fish_nevermind") from _call_expression_1196
            "Buy a drink (5$)":

                call expression game.dialog_select("terry_dialogue_buy_drink_pre") from _call_expression_1197
                menu:
                    "Buy a shot.":
                        call expression game.dialog_select("terry_dialogue_buy_drink") from _call_expression_1198
                    "I’ll pass.":

                        call expression game.dialog_select("terry_dialogue_buy_drink_pass") from _call_expression_1199
            "Go fishing":

                call expression game.dialog_select("terry_dialogue_fishing") from _call_expression_1200
                $ M_terry.set("bait talk", True)

            "Bait" if M_terry.is_set("bait talk"):
                call expression game.dialog_select("terry_dialogue_fishing_bait") from _call_expression_1201

            "What's your secret?" if M_terry.is_state(S_terry_secret):
                call expression game.dialog_select("terry_dialogue_secret") from _call_expression_1202
                $ M_terry.trigger(T_terry_secret_lure)
                $ M_aqua.trigger(T_aqua_special_lure)

            "About that lure..." if M_terry.is_state([S_terry_lure, S_terry_trade]) and not M_aqua.is_state(S_aqua_trade):
                call expression game.dialog_select("terry_dialogue_lure") from _call_expression_1203

            "Golden Compass." if M_aqua.is_state(S_aqua_trade) and M_terry.is_state(S_terry_trade):
                call expression game.dialog_select("terry_dialogue_golden_compass") from _call_expression_1204
                $ player.remove_item("golden_compass")
                $ player.get_item("special_lure")
                $ M_terry.trigger(T_terry_lure_trade)
                $ M_aqua.trigger(T_terry_lure_trade)

            "Retire." if M_terry.is_state([S_terry_bored, S_terry_retire]) and M_aqua.is_state(S_aqua_valor_test):
                call expression game.dialog_select("terry_dialogue_retire") from _call_expression_1205
                $ M_terry.trigger(T_terry_retire)

            "Fake ID" if M_roxxy.get("talked to roxxy id") and M_roxxy.is_state(S_roxxy_get_fake_id, S_roxxy_fake_id_get_picture):
                if M_roxxy.is_state(S_roxxy_get_fake_id):
                    call expression game.dialog_select("terry_dialogue_fake_id") from _call_expression_1206
                    $ M_roxxy.trigger(T_roxxy_ask_terry)

                elif M_roxxy.is_state(S_roxxy_fake_id_get_picture) and player.has_item("roxxy_picture"):
                    if M_roxxy.get("talked to terry"):
                        call expression game.dialog_select("terry_dialogue_fake_id_picture_repeat") from _call_expression_1207
                    else:

                        call expression game.dialog_select("terry_dialogue_fake_id_picture_first") from _call_expression_1208
                        $ M_roxxy.set("talked to terry", True)
                    menu:
                        "Yes" if player.has_money(400):
                            $ player.spend_money(400)
                            call expression game.dialog_select("terry_dialogue_fake_id_yes") from _call_expression_1209
                            menu:
                                "Becca.":
                                    call expression game.dialog_select("terry_dialogue_fake_id_yes_becca") from _call_expression_1210
                                "Missy.":

                                    call expression game.dialog_select("terry_dialogue_fake_id_yes_missy") from _call_expression_1211
                            $ game.timer.tick(2)
                            $ M_player.set("jerk roxxy", True)
                            $ M_roxxy.trigger(T_roxxy_give_id)
                        "No":

                            call expression game.dialog_select("terry_dialogue_fake_id_no") from _call_expression_1212

            "GoldSchwagger" if M_roxxy.is_state(S_roxxy_spin_bottle) and not player.has_item("goldschwagger"):
                call expression game.dialog_select("terry_dialogue_goldschwagger") from _call_expression_1213
                $ player.get_item("goldschwagger")
            "Leave":

                $ pass

    $ playMusic()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
