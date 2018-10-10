label home_entrance:
    $ player.go_to(L_home_entrance)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if erik.started(erik_bullying):
        call expression game.dialog_select("entrance_erik_bullying") from _call_expression_538
        $ erik_bullying.finish()


    elif M_mia.is_state(S_mia_angelicas_impatience):
        call expression game.dialog_select("entrance_mia_angelicas_impatience") from _call_expression_539
        $ M_mia.trigger(T_angelica_house_visit)


    elif M_mia.is_state(S_mia_angelicas_home_visit):
        call expression game.dialog_select("entrance_mia_angelicas_home_visit") from _call_expression_540
        $ M_mia.trigger(T_angelica_requires_whip)


    elif M_mia.is_state(S_mia_angelicas_final_home_visit):
        call expression game.dialog_select("entrance_mia_angelicas_final_home_visit") from _call_expression_541
        $ M_mia.trigger(T_angelica_strapon_request)


    elif M_mom.is_state(S_mom_overheard):
        call expression game.dialog_select("entrance_mom_overheard") from _call_expression_542
        $ M_mom.trigger(T_mom_check)


    elif M_mom.is_state(S_mom_lawn_help) and not game.timer.is_dark():
        call expression game.dialog_select("entrance_mom_lawn_help") from _call_expression_543
        $ M_mom.trigger(T_mom_help_mow)

    elif M_mom.is_state(S_mom_clothes_dirty):
        call expression game.dialog_select("entrance_mom_clothes_dirty") from _call_expression_544
        $ M_mom.trigger(T_mom_sis_bitch)

    elif M_mom.is_state(S_mom_debt_collectors):
        $ playMusic("<loop 73.5>audio/music_villain.ogg", 1.0)
        call expression game.dialog_select("entrance_mom_debt_collectors") from _call_expression_545
        $ M_mom.trigger(T_mom_bad_guys)


    elif M_mom.is_state(S_mom_pipe_help) and game.timer.is_morning():
        call expression game.dialog_select("entrance_mom_pipe_help") from _call_expression_546
        $ M_mom.trigger(T_mom_broken_pipe)


    elif M_mom.is_state(S_mom_movie_night) and game.timer.is_evening():
        call expression game.dialog_select("entrance_mom_movie_night") from _call_expression_547
        $ M_mom.trigger(T_mom_movie_invite)


    elif M_mom.is_state(S_mom_hang_out) and not game.timer.is_dark():
        call expression game.dialog_select("entrance_mom_hang_out") from _call_expression_548
        menu:
            "Yes.":
                call expression game.dialog_select("entrance_mom_hang_out_yes") from _call_expression_549
                $ M_mom.trigger(T_mom_hang_out_accept)
            "No.":


                call expression game.dialog_select("entrance_mom_hang_out_no") from _call_expression_550
                $ M_mom.trigger(T_mom_hang_out_refuse)
        hide debbie
        hide player
        with dissolve

    elif M_mom.is_state(S_mom_spy) and not game.timer.is_dark():
        call expression game.dialog_select("entrance_mom_spy") from _call_expression_551

    elif M_mom.is_state(S_mom_kissing_practice) and not game.timer.is_dark():
        call expression game.dialog_select("entrance_mom_kissing_practice") from _call_expression_552

    elif M_mom.is_state(S_mom_car_broken) and game.timer.is_morning():
        call expression game.dialog_select("entrance_mom_car_broken") from _call_expression_553
        $ M_mom.trigger(T_mom_car_help)

    elif M_mom.is_state(S_mom_panties_masturbation_again) and not game.timer.is_dark():
        if L_home_basement.is_here(M_mom):
            $ temp = "Basement"
        else:
            $ temp = "Kitchen"
        call expression game.dialog_select("entrance_mom_panties_masturbation_again") from _call_expression_554

    elif M_mom.is_state(S_mom_diane_visit) and game.timer.is_evening():
        call expression game.dialog_select("entrance_mom_diane_visit") from _call_expression_555

    elif M_mom.is_state(S_mom_midnight_search):
        jump mom_midnight_swim

    elif sister.started(sis_couch01) and game.timer.is_evening():
        call expression game.dialog_select("entrance_sis_couch_1") from _call_expression_556

    elif sister.started(sis_couch02) and game.timer.is_evening():
        call expression game.dialog_select("entrance_sis_couch_2") from _call_expression_557

    elif sister.started(sis_couch03) and game.timer.is_evening() and (not M_mom.is_state(S_mom_sleepover) or not L_home_livingroom.is_here(M_mom)):
        call expression game.dialog_select("entrance_sis_couch_3") from _call_expression_558
        jump home_livingroom_dialogue

    elif M_bissette.is_state(S_bissette_roxxy_jenny_mentoring) and game.timer.is_afternoon():
        if not M_roxxy.get("roxxy trailer sex"):
            call expression game.dialog_select("entrance_bissette_roxxy_jenny_mentoring") from _call_expression_559
        else:
            call expression game.dialog_select("entrance_bissette_roxxy_jenny_mentoring_sex") from _call_expression_560

        $ M_bissette.trigger(T_bissette_roxxy_jenny_hangout)
    $ game.main()

label vacuum_dialogue:
    call expression game.dialog_select("entrance_mom_vacuum") from _call_expression_561
    menu:
        "Let me help.":
            call expression game.dialog_select("entrance_mom_vacuum_yes") from _call_expression_562
            $ game.timer.tick()
            $ M_mom.trigger(T_mom_vacuumed)
        "It's too loud.":
            call expression game.dialog_select("entrance_mom_vacuum_no") from _call_expression_563
    $ M_mom.set("chores", False)
    $ game.main()

label erik_bullying_3:
    $ player.go_to(L_home_entrance)
    call expression game.dialog_select("entrance_erik_bullying_3") from _call_expression_564
    $ erik.add_event(erik_bullying_3)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
