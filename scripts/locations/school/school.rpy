label school_mia_study_reminder:
    scene expression "backgrounds/location_school_day_blur.jpg"
    show player 4
    with dissolve
    player_name "( Hmm, now that I've caught up in French class, {b}I can help Mia with her studies{/b}. )"
    show player 1
    player_name "( {b}I should talk to her about it{/b}! )"
    return

label school_dialogue:
    $ player.go_to(L_school_hall)
    if erik.started(erik_intro):
        call expression game.dialog_select("school_erik_intro_started") from _call_expression_994
        $ L_map.lock()
        $ M_mia.trigger(T_all_school_entrance)

    elif M_bissette.finished_state(S_bissette_study) and not M_mia.get("reminded study") and not game.timer.is_dark():
        call expression game.dialog_select("school_mia_study_reminder") from _call_expression_995
        $ M_mia.set("reminded study", True)

    if M_dewitt.is_state(S_dewitt_school_sneak_mission) and game.timer.is_dark():
        call expression game.dialog_select("school_dewitt_school_sneak_mission") from _call_expression_996

        $ game.main()

    if not game.timer.is_weekend():
        if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg") and not game.timer.is_dark():
            $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)

        if M_roxxy.is_state(S_roxxy_shower_event) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_shower_event") from _call_expression_997

        elif M_roxxy.is_state(S_roxxy_intense_gymercise) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_intense_gymercise") from _call_expression_998


        elif M_bissette.is_state(S_bissette_challenge) and not game.timer.is_dark():
            call expression game.dialog_select("school_bissette_challenge") from _call_expression_999
            $ M_bissette.trigger(T_bissette_challenge_thoughts)

            $ game.timer.tick()
            jump map_dialogue

        elif M_mia.is_state(S_mia_glasses_favor) and not game.timer.is_dark():
            call expression game.dialog_select("school_mia_glasses_favor") from _call_expression_1000
            $ player.get_item("aviators")
            $ M_mia.trigger(T_mia_gives_glasses)

        elif erik.started(erik_bullying_2) and not game.ui_locked and not game.timer.is_dark():
            call expression game.dialog_select("school_erik_bullying_2_started") from _call_expression_1001
            if player.stats.dex() >= 4:
                call expression game.dialog_select("school_erik_bullying_2_started_dex_pass") from _call_expression_1002
                jump expression game.dialog_select("erik_bullying_2")
            else:
                call expression game.dialog_select("school_erik_bullying_2_started_dex_fail") from _call_expression_1003

        elif erik.started(erik_intro) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_intro_started") from _call_expression_1004
            $ erik_intro.finish()
            $ M_smith.trigger(T_smith_intro)
            $ M_roxxy.trigger(T_roxxy_teachers_berating)


        elif M_dewitt.is_state(S_dewitt_talent_show_ask_annie) and not game.timer.is_dark():
            call expression game.dialog_select("school_hallway_dewitt_talent_show_ask_annie") from _call_expression_1005

            $ M_dewitt.trigger(T_dewitt_annies_refusal)

        elif M_dewitt.is_state(S_dewitt_pre_talent_show_chat) and not game.timer.is_dark():
            call expression game.dialog_select("school_dewitt_pre_talent_show_chat") from _call_expression_1006

            $ M_dewitt.trigger(T_dewitt_double_check_trap)

        elif M_smith.is_state(S_smith_unlocked_locker) and not game.timer.is_dark():
            call expression game.dialog_select("school_hallway_smith_unlocked_locker") from _call_expression_1007
            $ M_smith.trigger(T_smith_go_to_athletics)

        elif M_roxxy.is_state(S_roxxy_dexter_argument) and not M_roxxy.get("dexter argument got information") and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_dexter_argument") from _call_expression_1008
            $ M_roxxy.set("dexter argument got information", True)
            $ player.go_to(L_map)
            $ game.main()

        elif M_roxxy.is_state(S_roxxy_dexter_confront) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_dexter_confront") from _call_expression_1009
            $ M_roxxy.trigger(T_roxxy_do_assignment)

        elif M_roxxy.is_state(S_roxxy_assignment) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_assignment") from _call_expression_1010
            $ M_roxxy.trigger(T_roxxy_study_at_roxxy)

        elif M_roxxy.is_state(S_roxxy_missing_outfit) and game.timer.is_morning():
            call expression game.dialog_select("school_roxxy_missing_outfit") from _call_expression_1011
            $ M_roxxy.trigger(T_roxxy_find_cheerleader_outfit)
            $ player.go_to(L_map)
            $ game.main()

        elif M_roxxy.is_state(S_roxxy_return_to_school) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_return_to_school") from _call_expression_1012
            $ M_roxxy.trigger(T_roxxy_returned_to_school)
            $ player.go_to(L_map)
            $ game.main()

        elif M_roxxy.is_state(S_roxxy_trailer_park_trouble) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_trailer_park_trouble") from _call_expression_1013
            $ player.go_to(L_map)
            $ M_roxxy.trigger(T_roxxy_home_foreclosed)
            $ game.main()

        elif M_roxxy.is_state(S_roxxy_selling_meth_ask_roxxy) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_selling_meth_ask_roxxy") from _call_expression_1014
            $ player.go_to(L_map)
            $ M_roxxy.trigger(T_roxxy_meth_asked_roxxy)
            $ game.main()

        elif M_roxxy.is_state(S_roxxy_shut_down_lab) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_shut_down_lab") from _call_expression_1015
            $ M_roxxy.trigger(T_roxxy_failing_exams)

        elif M_roxxy.is_state(S_roxxy_give_exams) and not game.timer.is_dark():
            label roxxy_locker_rub_hscene_replay:
                call expression game.dialog_select("school_roxxy_give_exams") from _call_expression_1016
            $ renpy.end_replay()
            $ persistent.cookie_jar["Roxxy"]["unlocked"] = True
            $ persistent.cookie_jar["Roxxy"]["gallery"]["03_unlocked"] = True
            $ M_roxxy.trigger(T_roxxy_gave_exams)

        elif M_roxxy.is_state(S_roxxy_dexter_flirt) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_dexter_flirt") from _call_expression_1017
            $ M_roxxy.trigger(T_roxxy_help_dewitt)

        elif M_roxxy.is_state(S_roxxy_do_pushups_intro) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_do_pushups_intro") from _call_expression_1018
            $ M_roxxy.trigger(T_roxxy_dexter_challenge_pushups)
            call screen pushups_minigame

        elif M_roxxy.is_state(S_roxxy_trailer_park_romance) and game.timer.is_morning():
            call expression game.dialog_select("school_roxxy_trailer_park_romance_intro") from _call_expression_1019
            menu:
                "Not right now.":
                    call expression game.dialog_select("school_roxxy_trailer_park_romance_no") from _call_expression_1020
                "I can come":

                    call expression game.dialog_select("school_roxxy_trailer_park_romance_yes") from _call_expression_1021
                    $ M_roxxy.trigger(T_roxxy_accepted_picnic)

        elif M_roxxy.is_state(S_roxxy_dexter_basketball) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_dexter_basketball") from _call_expression_1022
            $ M_roxxy.trigger(T_roxxy_basket_challenged)
            $ M_roxxy.set("basketball unlocked", True)
            jump basketball_minigame_prepare

        elif M_roxxy.is_state(S_roxxy_fight_dexter) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_fight_dexter") from _call_expression_1023
            menu:
                "No.":
                    show player 10 with dissolve
                    player_name "No, this is life or death... I should really prepare more."
                    $ player.go_to(L_map)
                    $ game.main()
                "Yes.":

                    show player 12 with dissolve
                    player_name "No more running..."
                    player_name "It's time to put {b}Dexter{/b} down for good!"
                    jump dexter_fight_minigame_prepare
            hide player with dissolve

        elif M_roxxy.get("roxxy trailer sex") >= 2 and not M_roxxy.get("roxxy locker sex") and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_locker_sex") from _call_expression_1024
            call expression game.dialog_select("roxxy_locker_sex_loop_pre") from _call_expression_1025
            jump expression game.dialog_select("roxxy_locker_sex_loop")
        call pa_announcement from _call_pa_announcement_6

    elif not M_dewitt.is_state(S_dewitt_school_sneak_mission) and not game.timer.is_dark():
        $ player.go_to(L_map)
        if not game.timer.is_dark():
            if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
                $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
        else:

            if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
                $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
        call expression game.dialog_select("school_weekend_lock") from _call_expression_1026
    $ game.main()

label school_locker:
    $ player.go_to(L_school_locker_MC)
    if M_smith.is_state(S_smith_go_to_locker):
        call expression game.dialog_select("school_locker_smith_go_to_locker") from _call_expression_1027
        $ M_smith.trigger(T_smith_unlocked_locker)

    elif M_roxxy.is_set("meet for locker sex") and not game.timer.is_dark():
        label roxxy_locker_fuck_hscene_replay:
            call expression game.dialog_select("school_roxxy_locker_sex_repeat") from _call_expression_1028
        call expression game.dialog_select("roxxy_locker_sex_loop_pre") from _call_expression_1029
        jump expression game.dialog_select("roxxy_locker_sex_loop")
    $ player.location.call_screen(False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
