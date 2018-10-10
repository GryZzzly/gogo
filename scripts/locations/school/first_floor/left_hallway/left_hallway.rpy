label left_hall_dialogue:
    $ player.go_to(L_school_lefthallway)
    call pa_announcement from _call_pa_announcement_9
    if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg") and not game.timer.is_dark():
        $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)

    if not game.timer.is_dark():
        if M_judith.is_state(S_judith_start):
            call expression game.dialog_select("left_hallway_judith_changing") from _call_expression_1363
            $ M_judith.trigger(T_judith_changed)

        elif M_roxxy.is_state(S_roxxy_lockerroom_event):
            call expression game.dialog_select("left_hallway_roxxy_lockerroom_event") from _call_expression_1364

            $ M_roxxy.set("left hallway lock", True)

        elif M_roxxy.is_state(S_roxxy_shower_event) and not M_roxxy.get("get erik clothes"):
            call expression game.dialog_select("left_hallway_roxxy_shower_event") from _call_expression_1365

            $ M_roxxy.set("get erik clothes", True)

        elif M_judith.is_state(S_judith_latina_bashing):
            call expression game.dialog_select("left_hallway_latinos_bashing") from _call_expression_1366
            $ M_judith.trigger(T_judith_latina_bashed)

        elif M_judith.is_state(S_judith_in_girls_bathroom):
            call expression game.dialog_select("left_hallway_judith_missing") from _call_expression_1367

        elif M_bissette.get_state() in [S_bissette_jane_return_books, S_bissette_got_dexters_book,
                                        S_bissette_got_dexters_eriks_books, S_bissette_got_eriks_book,
                                        S_bissette_got_eriks_dexters_books
                                       ] and not M_bissette.is_set("martinez book search"):
            call expression game.dialog_select("left_hallway_martinez_book_search") from _call_expression_1368
            $ M_bissette.set("martinez book search", True)
    else:



        if quest11 in quest_list and quest11 not in completed_quests and not left_hall_cult_seen:
            call expression game.dialog_select("left_hallway_cult_discovery") from _call_expression_1369
            $ left_hall_cult_seen = True

        elif M_dewitt.is_state(S_dewitt_school_sneak_mission):
            call expression game.dialog_select("left_hallway_school_sneak_mission") from _call_expression_1370
            $ M_dewitt.trigger(T_dewitt_school_sneak_in)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
