label mom_button_dialogue:
    if M_mom.is_state(S_mom_relaxing):
        call expression game.dialog_select("debbie_dialogue_mom_relaxing") from _call_expression_423
        $ game.main()

    elif M_mom.is_set("sleep together") and not M_mom.is_set("revealing") and player.location == L_home_kitchen:
        call expression game.dialog_select("debbie_dialogue_mom_not_revealing_kitchen") from _call_expression_424
        $ M_mom.set("revealing", True)
        $ M_mom.set("panties available", True)
        jump expression game.dialog_select("debbie_dialogue_options")

    scene expression player.location.background_blur

    if M_mom.is_set("fetch lotion") and not M_mom.is_set("retrieved lotion"):
        call expression game.dialog_select("debbie_dialogue_mom_fetch_lotion") from _call_expression_425

    elif M_mom.is_set("fetch lotion") and M_mom.is_set("retrieved lotion"):
        jump expression game.dialog_select("mom_lotion_fun")

    elif M_mom.is_state(S_mom_car_condition):
        call expression game.dialog_select("debbie_dialogue_mom_car_condition") from _call_expression_426
        $ M_mom.trigger(T_mom_deliver_car_news)
    else:

        if M_mom.is_set("revealing") and player.location == L_home_kitchen:
            call expression game.dialog_select("debbie_dialogue_mom_revealing_kitchen_pre") from _call_expression_427
            menu:
                "Feel Ass":
                    if M_mom.is_set("sex available"):
                        label mom_kitchen_replay:
                            call expression game.dialog_select("debbie_dialogue_mom_revealing_feel_ass_sex_pre") from _call_expression_428
                        $ M_mom.set("sex speed", .175)
                        call expression game.dialog_select("debbie_dialogue_mom_revealing_feel_ass_sex_after") from _call_expression_429
                        jump expression game.dialog_select("mom_kitchen_fuck_loop")
                    else:

                        call expression game.dialog_select("debbie_dialogue_mom_revealing_feel_ass_no_sex") from _call_expression_430
                        jump expression game.dialog_select("debbie_dialogue_options")
                "Talk":

                    call expression game.dialog_select("debbie_dialogue_mom_revealing_talk") from _call_expression_431
                    jump expression game.dialog_select("debbie_dialogue_options")

        if M_mom.is_set("revealing"):
            call expression game.dialog_select("debbie_dialogue_mom_revealing") from _call_expression_432
        else:

            call expression game.dialog_select("debbie_dialogue_mom_not_revealing") from _call_expression_433
        menu debbie_dialogue_options:
            "Ask about {b}Dad{/b}." if M_mom.is_set("dad question"):
                $ M_mom.set("dad question", False)
                call expression game.dialog_select("debbie_dialogue_ask_about_dad") from _call_expression_434
                jump expression game.dialog_select("debbie_dialogue_options")

            "Ask about money problems." if M_mom.is_set("money question"):
                $ M_mom.set("money question", False)
                call expression game.dialog_select("debbie_dialogue_ask_about_money_problems") from _call_expression_435
                jump expression game.dialog_select("debbie_dialogue_options")

            "Ask about the men in suits." if M_mom.is_set("bad guys question"):
                $ M_mom.set("bad guys question", False)
                call expression game.dialog_select("debbie_dialogue_ask_about_men_in_suits") from _call_expression_436
                jump expression game.dialog_select("debbie_dialogue_options")

            "Paint." if M_dewitt.is_state([S_dewitt_ask_deb_paint, S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint]):
                call expression game.dialog_select("debbie_dialogue_paint") from _call_expression_437
                $ M_dewitt.trigger(T_dewitt_diane_find_paint)
            "Help {b}[deb_name]{/b} around the house.":

                if M_mom.is_state([S_mom_fill_mower, S_mom_mow_lawn]):
                    call expression game.dialog_select("debbie_dialogue_help_mow_lawn") from _call_expression_438
                    $ game.main()

                elif M_mom.between_states(S_mom_sis_check, S_mom_fix_pipe):
                    call expression game.dialog_select("debbie_dialogue_help_fix_broken_pipe") from _call_expression_439

                elif M_mom.between_states(S_mom_vacuum_help, S_mom_laundry_help):
                    call expression game.dialog_select("debbie_dialogue_help_chores_pre") from _call_expression_440
                    if M_mom.is_state(S_mom_laundry_help) and M_mom.is_set("chores"):
                        call expression game.dialog_select("debbie_dialogue_help_chores_later") from _call_expression_441
                    else:
                        call expression game.dialog_select("debbie_dialogue_help_chores_tomorrow") from _call_expression_442
                    call expression game.dialog_select("debbie_dialogue_help_chores_after") from _call_expression_443

                elif M_mom.is_state(S_mom_check_car):
                    call expression game.dialog_select("debbie_dialogue_help_check_car") from _call_expression_444

                elif M_mom.is_state(S_mom_fix_car):
                    call expression game.dialog_select("debbie_dialogue_help_fix_car") from _call_expression_445
                else:

                    call expression game.dialog_select("debbie_dialogue_help_nothing") from _call_expression_446
                show player 1
                jump expression game.dialog_select("debbie_dialogue_options")

            "Apply lotion." if M_mom.is_set("lotion fun"):
                if M_mom.is_set("sex available") and player.location == L_home_kitchen:
                    call expression game.dialog_select("debbie_dialogue_lotion_fun_had_sex") from _call_expression_447
                else:

                    call expression game.dialog_select("debbie_dialogue_lotion_fun") from _call_expression_448
                call expression game.dialog_select("debbie_dialogue_lotion_fun_after") from _call_expression_449
                $ M_mom.set("fetch lotion", True)


            "Shopping" if M_mom.is_state(S_mom_hang_out_return) and player.location == L_home_kitchen:
                call expression game.dialog_select("debbie_dialogue_shopping") from _call_expression_450
                $ M_mom.trigger(T_mom_hang_out_accept)

            "Shower." if M_mom.is_set("sex available"):
                if player.location == L_home_basement:
                    call expression game.dialog_select("debbie_dialogue_shower_basement") from _call_expression_451

                elif player.location == L_home_kitchen:
                    call expression game.dialog_select("debbie_dialogue_shower_kitchen") from _call_expression_452
                jump expression game.dialog_select("mom_shower_question")

            "Sex in your room." if M_mom.is_set("sex available"):
                if player.location == L_home_basement:
                    call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_basement") from _call_expression_453

                elif player.location == L_home_kitchen:
                    call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_kitchen") from _call_expression_454
                call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_after") from _call_expression_455
                jump expression game.dialog_select("mom_sex")

            "Sex in my room." if M_mom.is_set("sex available") and not M_mom.is_set("room sneak"):
                call expression game.dialog_select("debbie_dialogue_sex_in_my_room") from _call_expression_456
                $ M_mom.set("room sneak", True)

            "Hang out in the car." if M_mom.is_set("sex available"):
                call expression game.dialog_select("debbie_dialogue_sex_in_car") from _call_expression_457
                jump expression game.dialog_select("debbie_car_sex")

            "Watch a Movie." if M_mom.is_set("sex available") and not M_mom.is_set("movie night"):
                call expression game.dialog_select("debbie_dialogue_watch_movie") from _call_expression_458
                $ M_mom.set("movie night", True)

            "Laundry." if M_mom.is_set("basement sex"):
                if player.location == L_home_basement:
                    label mom_basement_replay:
                        if not store._in_replay == None:
                            if randomizer() < 50:
                                jump expression game.dialog_select("basement_mom_sex")
                    call expression game.dialog_select("debbie_dialogue_laundry_sex_basement") from _call_expression_459
                    if not M_mom.is_state(S_mom_give_laundry) and randomizer() <= 50:
                        $ mom_basement_rand = True
                        call expression game.dialog_select("debbie_dialogue_laundry_sex_basement_random_true") from _call_expression_460
                    else:

                        $ mom_basement_rand = False
                        call expression game.dialog_select("debbie_dialogue_laundry_sex_basement_random_false") from _call_expression_461
                    $ M_mom.set("sex speed", .4)
                    $ player.go_to(L_home_basement)
                    $ cum = False
                    $ anim_toggle = False
                    $ xray = False
                    jump expression game.dialog_select("basement_mom_sex_loop")

                elif player.location == L_home_kitchen:
                    call expression game.dialog_select("debbie_dialogue_laundry_sex_kitchen") from _call_expression_462
                    jump expression game.dialog_select("basement_mom_sex")

            "Kissing" if M_mom.is_state(S_mom_kissing_practice) and player.location == L_home_kitchen:
                call expression game.dialog_select("debbie_dialogue_kiss") from _call_expression_463
                menu:
                    "Can you teach me?":
                        call expression game.dialog_select("debbie_dialogue_kiss_teach") from _call_expression_464
                        if player.stats.chr() >= 5:
                            jump expression game.dialog_select("mom_kissing_practice")
                        else:

                            call expression game.dialog_select("debbie_dialogue_kiss_teach_stat_fail") from _call_expression_465
                    "Nothing":

                        call expression game.dialog_select("debbie_dialogue_kiss_leave") from _call_expression_466

            "Practice Kissing" if M_mom.is_set("practice kissing") and player.location == L_home_kitchen:
                call expression game.dialog_select("debbie_dialogue_kiss_practice") from _call_expression_467
                $ game.timer.tick()
            "Nevermind.":

                call expression game.dialog_select("debbie_dialogue_leave") from _call_expression_468
    hide player
    hide debbie
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
