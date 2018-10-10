label bedroom_dialogue:
    $ player.go_to(L_home_bedroom)
    if not M_player.is_set("just wokeup"):
        if M_mom.is_state(S_mom_mrsj_visit) and not game.timer.is_dark():
            jump expression game.dialog_select("home_front")

        elif M_mom.is_state(S_mom_car_fixed):
            jump expression game.dialog_select("home_front")

        elif M_mom.is_state(S_mom_bad_guys_revisit) and not game.timer.is_dark():
            jump expression game.dialog_select("home_front")

        elif M_mom.is_state(S_mom_diane_visit) and game.timer.is_evening():
            jump expression game.dialog_select("home_entrance")

    if erik.completed(erik_bullying_2) and not erik.known(erik_bullying_3):
        jump expression game.dialog_select("erik_bullying_3")

    if M_player.is_state(S_player_start) and M_player.is_set("just wokeup"):
        call expression game.dialog_select("bedroom_mc_start_just_wokeup") from _call_expression_310

    elif game.timer.is_morning() and not game.timer.is_weekend() and M_player.is_set("just wokeup"):
        call expression game.dialog_select("bedroom_mc_weekday_just_wokeup") from _call_expression_311

    elif game.timer.is_morning() and game.timer.is_weekend() and M_player.is_set("just wokeup"):
        call expression game.dialog_select("bedroom_mc_weekend_just_wokeup") from _call_expression_312

    if game.timer.game_day() >= event_wait_till and not erik.known(erik_bullying):
        call expression game.dialog_select("bedroom_erik_bullying") from _call_expression_313

        $ erik.add_event(erik_bullying)
        $ M_erik.place(place = L_erikhouse_erikroom)
        $ M_erik.force()

    elif M_mia.is_state(S_mia_tattoo_help) and M_mia.is_set('story delay'):
        call expression game.dialog_select("bedroom_mia_tattoo_help") from _call_expression_314
        $ M_mia.trigger(T_mia_tattoo_start)

    elif M_mia.is_state(S_mia_strip_aftermath):
        call expression game.dialog_select("bedroom_mia_strip_aftermath_grounded") from _call_expression_315
        $ M_mia.trigger(T_mia_grounded)

    elif M_mia.is_state(S_mia_concerning_visit):
        call expression game.dialog_select("bedroom_mia_concerning_visit") from _call_expression_316

    elif M_mia.is_state(S_mia_urgent_message):
        call expression game.dialog_select("bedroom_mia_urgent_message") from _call_expression_317

        $ player.receive_message("mia02")

    elif M_mia.is_state(S_mia_angelicas_impatience):
        call expression game.dialog_select("bedroom_mia_angelicas_impatience") from _call_expression_318


    elif M_mia.is_state(S_mia_angelicas_home_visit):
        call expression game.dialog_select("bedroom_mia_angelicas_home_visit") from _call_expression_319


    elif M_mia.is_state(S_mia_angelicas_final_home_visit):
        call expression game.dialog_select("bedroom_mia_angelicas_final_home_visit") from _call_expression_320


    if M_mom.is_state(S_mom_overheard) and game.timer.is_dark():
        call expression game.dialog_select("bedroom_mom_overheard") from _call_expression_321
        $ M_mom.trigger(T_mom_check)


    elif M_mom.is_state(S_mom_doorbell):
        call expression game.dialog_select("bedroom_mom_doorbell") from _call_expression_322
        $ M_mom.trigger(T_mom_check_door)


    elif M_mom.is_state(S_mom_movie_afterthoughts):
        call expression game.dialog_select("bedroom_mom_movie_afterthoughts") from _call_expression_323
        $ M_mom.trigger(T_mom_movie_night_finish)

    elif M_mom.is_state(S_mom_movie_afterthoughts_two):
        call expression game.dialog_select("bedroom_mom_afterthoughts_two") from _call_expression_324
        $ M_mom.trigger(T_mom_movie_night_finish)

    elif M_mom.is_state(S_mom_note) and game.timer.is_dark():
        call expression game.dialog_select("bedroom_mom_note") from _call_expression_325

    elif M_mom.is_state(S_mom_note) and M_player.is_set("just wokeup"):
        call expression game.dialog_select("bedroom_mom_note_just_wokeup") from _call_expression_326
        $ M_player.set("just wokeup", False)


    if M_bissette.is_state(S_bissette_french_food_assignment):
        call expression game.dialog_select("bedroom_bissette_french_food_assignment") from _call_expression_327

    elif M_bissette.is_state(S_bissette_roxxy_jenny_mentoring) and game.timer.is_afternoon():
        call expression game.dialog_select("bedroom_bissette_roxxy_jenny_mentoring") from _call_expression_328

    if M_dewitt.is_state(S_dewitt_make_replacement_guitar) and player.has_item("paint") and player.has_item("wood_pile"):
        call expression game.dialog_select("bedroom_dewitt_make_replacement_guitar") from _call_expression_329

    if not game.timer.is_dark():
        if M_player.is_set("just wokeup"):
            call expression game.dialog_select("player_just_wokeup") from _call_expression_330

    elif game.timer.is_evening():
        if sister.started(sis_couch01):
            call expression game.dialog_select("bedroom_sis_couch_1") from _call_expression_331

        elif sister.started(sis_couch03):
            call expression game.dialog_select("bedroom_sis_couch_3") from _call_expression_332
    $ game.main()

label sleeping:
    if M_mom.is_state([S_mom_movie_night, S_mom_movie_night_two]):
        call expression game.dialog_select("bedroom_sleeping_debbie_movie_night") from _call_expression_333
        $ game.timer.tick(2)

        $ game.main()

    elif M_mom.is_state(S_mom_sleepover):
        call expression game.dialog_select("bedroom_sleeping_debbie_sleepover") from _call_expression_334
        $ game.main()

    elif M_mom.is_set("room sneak"):
        jump expression game.dialog_select("bedroom_debbie_sleepover")

    if erik.over(erik_breastfeeding_2) and not erik.over(erik_thief):
        if erik.in_progress(erik_thief):
            $ erik_thief.unfinish()


        elif randomizer() > 66:
            if not erik.known(erik_thief):
                $ erik.add_event(erik_thief)
            call expression game.dialog_select("bedroom_sleeping_erik_thief_pre") from _call_expression_335
            menu:
                "Use the telescope.":
                    call expression game.dialog_select("bedroom_sleeping_erik_thief_use_telescope") from _call_expression_336
                    $ game.timer.tick(3)
                    $ erik_thief.finish()

                    scene black with fade
                    jump expression game.dialog_select("erik_house_dialogue")
                "Go back to sleep.":

                    call expression game.dialog_select("bedroom_sleeping_erik_thief_sleep") from _call_expression_337

    elif erik.started(erik_bullying_3):
        call expression game.dialog_select("bedroom_sleeping_erik_bullying_3_started") from _call_expression_338
        $ erik_bullying_3.finish()
        $ M_erik.place(place = L_erikhouse_basement)
        $ M_erik.force()

    elif M_dewitt.is_state(S_dewitt_eve_karaoke):
        call expression game.dialog_select("bedroom_sleeping_dewitt_eve_karaoke") from _call_expression_339
        $ game.main()

    elif M_dewitt.is_state(S_dewitt_school_sneak_mission):
        call expression game.dialog_select("bedroom_sleeping_dewitt_school_sneak_mission") from _call_expression_340
        $ game.main()

    elif M_mia.is_state(S_mia_midnight_call):
        call expression game.dialog_select("bedroom_sleeping_mia_midnight_call") from _call_expression_341

        $ game.timer.tick(3)
        $ player.receive_message("mia01")
        $ game.main()

    elif M_mom.is_state(S_mom_solo_dream):
        call expression game.dialog_select("bedroom_sleeping_debbie_solo_dream") from _call_expression_342
        $ M_mom.trigger(T_mom_dream)

    elif M_mom.is_state(S_mom_night_visit):
        call expression game.dialog_select("bedroom_sleeping_debbie_night_visit") from _call_expression_343
        $ M_mom.trigger(T_mom_midnight_fun)

    elif M_mom.is_state(S_mom_night_visit_two):
        call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_two") from _call_expression_344
        $ persistent.cookie_jar["Debbie"]["unlocked"] = True
        $ persistent.cookie_jar["Debbie"]["gallery"]["03_unlocked"] = True
        $ M_mom.trigger(T_mom_midnight_fun)

    elif M_mom.is_state(S_mom_midnight_noises):
        call expression game.dialog_select("bedroom_sleeping_debbie_midnight_noises") from _call_expression_345
        $ M_mom.trigger(T_mom_midnight_wakeup)
        $ game.timer.tick(3)

        $ game.main()

    elif M_mom.is_state(S_mom_night_visit_three):
        label mom_mc_sexvisit:
            call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three") from _call_expression_346
        $ keep_going = 0
        $ M_mom.set("change angle", False)
        call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_loop") from _call_expression_347
    else:

        show expression game.timer.image("bedroom{}")

    if M_player.is_set("pet cat"):
        scene location_home_bedroom_sleeping3 with fade
    else:
        scene location_home_bedroom_sleeping with fade
    show unlock11 at truecenter with dissolve
    $ renpy.pause()
    $ Sleep()
    hide unlock11
    hide bedroom
    hide bedroom_broken
    hide bedroom_night
    hide bedroom_broken_night
    scene black with fade
    hide sleeping with fade

    if M_mom.is_state(S_mom_smith_dream):
        call expression game.dialog_select("bedroom_sleeping_debbie_smith_dream") from _call_expression_348
        $ M_mom.trigger(T_mom_dream)
    jump expression game.dialog_select("bedroom_dialogue")

label jerking_off_dialogue:
    scene expression game.timer.image("bedroom{}")
    menu:
        "Jerk off.":
            $ A_solo_pleasure.unlock()
            menu:
                "{b}[deb_name]{/b}." if M_player.is_set("jerk mom"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_debbie") from _call_expression_349
                    scene black with fade
                    $ game.timer.tick()

                "Mia." if M_player.is_set("jerk mia"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_mia") from _call_expression_350
                    scene black with fade
                    $ game.timer.tick()

                "Roxxy" if M_player.is_set("jerk roxxy"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_roxxy") from _call_expression_351
                    scene black with fade
                    $ game.timer.tick()
                "Leave.":

                    $ pass
        "Leave.":

            $ pass
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
