label erik_button_dialogue:
    if M_bissette.get_state() in [S_bissette_jane_return_books, S_bissette_got_dexters_book,
                                  S_bissette_got_dexters_martinez_books, S_bissette_got_martinez_book,
                                  S_bissette_got_martinez_dexters_books
                                 ] and not M_bissette.is_set("eriks book search"):
        if player.location == L_erikhouse_basement:
            scene location_erik_basement01_closeup

        elif player.location == L_erikhouse_erikroom:
            scene expression game.timer.image("eriks_room{}_c")

        elif player.location == L_school_cafeteria:
            scene expression game.timer.image("backgrounds/location_school_cafeteria{}_blur.jpg")

        elif player.location == L_school_scienceclassroom:
            scene expression game.timer.image("backgrounds/location_school_science{}_blur.jpg")
        call erik_book_return from _call_erik_book_return
        $ M_bissette.set("eriks book search", True)
        $ game.main()

    if not erik.known(erik_card_hunt) and player.location == L_erikhouse_basement:
        call expression game.dialog_select("erik_card_hunt") from _call_expression_1284
        $ erik.add_event(erik_card_hunt)
        $ M_erik.unforce()
        $ game.main()

    if erik.over(erik_crown_card) and not erik.known(erik_orcette) and player.location == L_erikhouse_basement:
        jump erik_orcette

    if player.location.is_here(M_june):
        scene expression "backgrounds/location_erik_house_bedroom_bed_june_day.jpg" with hpunch
        player_name "!!!"
        $ player.go_to(L_erikhouse_entrance)
        $ erik_funky = True
        jump erik_funky_block

    if player.location == L_erikhouse_basement:
        scene location_erik_basement01_closeup

    elif player.location == L_erikhouse_erikroom:
        if erik.started(erik_gf):
            scene expression game.timer.image("erik_house_bedroom{}_b")
            show player 14
            with dissolve
            player_name "He looks so happy now."
            show player 17
            player_name "I should go tell {b}Mrs. Johnson{/b} the good news!"
            hide player with dissolve
            $ game.main()

        elif erik.in_progress(erik_gf_stolen):
            scene expression game.timer.image("erik_house_bedroom{}_b")
            show player 10
            with dissolve
            player_name "He's probably not in the best mood right now..."
            player_name "I'll talk to him tomorrow."
            hide player with dissolve
            $ game.main()
        scene expression game.timer.image("eriks_room{}_c")

    elif player.location == L_school_scienceclassroom:
        scene school_science_c02

    elif player.location == L_school_cafeteria:
        scene expression game.timer.image("backgrounds/location_school_cafeteria{}_blur.jpg")

    show erik 1 at right
    if player.location == L_school_scienceclassroom:
        show erikl 1f at right
    show player 2 at left
    with dissolve
    player_name "Hey {b}Erik{/b}!"
    show player 1 at left
    show erik 5 at right
    eri "Hey {b}[firstname]{/b}! What's up?"
    label erik_talk:
        menu:
            "Master Blaster." if M_okita.is_state(S_okita_get_controller_info):
                call expression game.dialog_select("button_erik_master_blaster") from _call_expression_1285
                $ M_okita.trigger(T_okita_got_master_blaster_info)

            "Master Blaster." if M_okita.is_state(S_okita_get_controller):
                call expression game.dialog_select("button_erik_master_blaster_again") from _call_expression_1286

            "Flute." if M_dewitt.is_state(S_dewitt_make_new_flute):
                call expression game.dialog_select("button_erik_make_flute") from _call_expression_1287

            "Talent Show." if M_dewitt.is_set("talent ask erik"):
                if M_dewitt.is_set("talent helping kevin"):
                    call expression game.dialog_select("dewitt_talent_show_helping_kevin") from _call_expression_1288

                elif M_dewitt.is_set("talent helping eve"):
                    call expression game.dialog_select("dewitt_talent_show_helping_eve") from _call_expression_1289
                else:

                    call expression game.dialog_select("button_erik_talent_show") from _call_expression_1290
                    $ M_dewitt.set("talent ask erik", False)

            "Guitar." if M_dewitt.is_state([S_dewitt_erik_borrow_guitar, S_dewitt_garage_find_paint, S_dewitt_ask_deb_paint, S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint, S_dewitt_make_replacement_guitar]):
                if M_dewitt.is_state(S_dewitt_erik_borrow_guitar):
                    call expression game.dialog_select("button_erik_borrow_guitar") from _call_expression_1291
                    if shed_unlocked:
                        $ M_dewitt.trigger(T_dewitt_eriks_agreement_shed)
                    else:
                        $ M_dewitt.trigger(T_dewitt_eriks_agreement_no_shed)
                else:

                    call expression game.dialog_select("button_erik_make_guitar") from _call_expression_1292
                    if shed_unlocked:
                        $ M_dewitt.trigger(T_dewitt_eriks_agreement_shed)
                    else:
                        $ M_dewitt.trigger(T_dewitt_eriks_agreement_no_shed)

            "Beer." if M_dewitt.is_state([S_dewitt_erik_get_beer, S_dewitt_clean_graffiti]):
                call expression game.dialog_select("button_erik_ask_beer") from _call_expression_1293
                $ M_dewitt.trigger(T_dewitt_erik_deal)

            "Drinks for {b}Roxxy{/b}" if M_roxxy.get("talked to roxxy booze"):
                call expression game.dialog_select("button_erik_talked_to_roxxy_booze") from _call_expression_1294
                $ M_roxxy.trigger(T_roxxy_get_beer)

            "Need your help." if M_dewitt.is_state(S_dewitt_school_sneak_mission_help):
                call expression game.dialog_select("button_erik_school_sneak_mission_help") from _call_expression_1295
                $ M_dewitt.trigger(T_dewitt_erik_deal)

            "Model." if M_ross.is_state(S_ross_ask_model):
                call expression game.dialog_select("button_erik_ask_model") from _call_expression_1296

            "Cards." if erik.started(erik_card_hunt):
                call expression game.dialog_select("erik_cards") from _call_expression_1297

            "Cock Crown of Thorns." if erik.started(erik_crown_card):
                jump erik_crown_card

            "The package." if erik.started(erik_orcette) or erik.started(erik_orcette_2):
                jump erik_package

            "VR Headset." if erik.started(erik_vr):
                jump erik_vr_game

            "Library Book." if M_bissette.is_set("eriks book search"):
                call erik_book_return from _call_erik_book_return_1

            "Sex education." if mrsj.started(mrsj_sex_ed):
                call expression game.dialog_select("button_erik_sex_ed") from _call_expression_1298

            "Girlfriend." if June.completed(june_erik_help) and not erik.known(erik_gf):
                call expression game.dialog_select("button_erik_girlfriend") from _call_expression_1299
                $ erik.add_event(erik_gf)

            "Girlfriend." if June.completed(june_mc_help) and not erik.known(erik_gf_stolen):
                call expression game.dialog_select("button_erik_girlfriend_stolen") from _call_expression_1300
                $ erik.add_event(erik_gf_stolen)
                $ erik_gf_stolen.finish()

            "Girlfriend." if June.completed(june_intro) and not June.known(june_intro_2):
                call expression game.dialog_select("button_erik_girlfriend_intro") from _call_expression_1301
                $ June.add_event(june_intro_2)
                jump erik_talk

            "Message from {b}Mr. Johnson{/b}." if erik.started(erik_father_forgive):
                call expression game.dialog_select("button_erik_message_from_dad") from _call_expression_1302
                $ erik_father_forgive.finish()

            "{b}Mrs. Johnson{/b}." if erik.over(erik_breastfeeding_2) and not erik.completed(erik_path_split):
                if mrsj.completed(mrsj_poker_night_2) and not erik.known(erik_path_split):
                    call expression game.dialog_select("button_erik_mrsj_poker_lost") from _call_expression_1303
                    $ erik.add_event(erik_path_split)
                    jump erik_talk

                elif erik.started(erik_path_split):
                    call expression game.dialog_select("button_erik_path_split") from _call_expression_1304
                    jump erik_talk
                else:

                    call expression game.dialog_select("button_erik_breastfeeding_in_person") from _call_expression_1305

            "I have the game!" if erik.completed(erik_favor) and player.has_item("game") and not erik.known(erik_favor_2):
                call expression game.dialog_select("button_erik_favor_completed") from _call_expression_1306
                $ player.remove_item("game")
                $ erik.add_event(erik_favor_2)
                jump erik_talk

            "I need a favor." if erik.started(erik_favor):
                call expression game.dialog_select("button_erik_ask_favor") from _call_expression_1307
                $ erik_favor.finish()
                jump erik_talk
            "Where's {b}Mrs. Johnson{/b}?":

                call expression game.dialog_select("button_erik_where_is_mrsj") from _call_expression_1308
            "Not much.":

                call expression game.dialog_select("button_erik_not_much") from _call_expression_1309

            "I need help." if False:
                call expression game.dialog_select("button_erik_webcam_help") from _call_expression_1310
                $ M_erik.set("webcam help", True)
    hide erikl
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
