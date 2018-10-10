label roxxy_classroom_dialogue:
    scene french_class_c
    if M_roxxy.is_state(S_roxxy_get_evidence):
        call expression game.dialog_select("button_roxxy_get_evidence") from _call_expression_1988
        $ game.main()

    elif M_roxxy.is_state(S_roxxy_lolipop_for_lolipop, S_roxxy_lolipop_just_once):
        if player.has_item("roxxy_homework"):
            if M_roxxy.is_state(S_roxxy_lolipop_for_lolipop):
                call expression game.dialog_select("button_roxxy_lolipop_for_lolipop") from _call_expression_1989
            elif M_roxxy.is_state(S_roxxy_lolipop_just_once):
                call expression game.dialog_select("button_roxxy_lolipop_just_once") from _call_expression_1990
            call expression game.dialog_select("button_roxxy_lolipop_cutscene") from _call_expression_1991
            $ player.remove_item("roxxy_homework")
            $ game.timer.tick()

            $ M_roxxy.trigger(T_roxxy_confrontation)
            $ player.go_to(L_school_hall)
            $ game.main()
        else:
            call expression game.dialog_select("button_roxxy_get_homework_locker") from _call_expression_1992

    elif M_bissette.is_state(S_bissette_roxxy_exam_convince):
        if not M_roxxy.get("roxxy trailer sex"):
            call expression game.dialog_select("roxxy_dialogue_exam_convince") from _call_expression_1993
        else:
            call expression game.dialog_select("roxxy_dialogue_exam_convince_roxxy_sex") from _call_expression_1994
        $ M_bissette.trigger(T_bissette_roxxy_deal)

    elif M_bissette.is_state(S_bissette_roxxy_pom_poms):
        if not M_roxxy.get("roxxy trailer sex"):
            call expression game.dialog_select("roxxy_dialogue_pom_poms") from _call_expression_1995
        else:
            call expression game.dialog_select("roxxy_dialogue_pom_poms_sex") from _call_expression_1996

    elif M_bissette.is_state(S_bissette_roxxy_pom_poms_deal):
        if not M_roxxy.get("roxxy trailer sex"):
            call expression game.dialog_select("roxxy_dialogue_pom_poms_deal") from _call_expression_1997
        else:
            call expression game.dialog_select("roxxy_dialogue_pom_poms_deal_sex") from _call_expression_1998
        $ M_bissette.trigger(T_bissette_roxxy_deal)
        $ player.remove_item("pompoms")

    elif M_bissette.is_state([S_bissette_roxxy_cheerleader_deal, S_bissette_jenny_mentoring_payment]):
        if not M_roxxy.get("roxxy trailer sex"):
            call expression game.dialog_select("roxxy_dialogue_cheerleader_deal") from _call_expression_1999
        else:
            call expression game.dialog_select("roxxy_dialogue_cheerleader_deal_sex") from _call_expression_2000

    elif M_bissette.is_state(S_bissette_roxxy_deal_confirmation):
        if not M_roxxy.get("roxxy trailer sex"):
            call expression game.dialog_select("roxxy_dialogue_deal_confirmation") from _call_expression_2001
        else:
            call expression game.dialog_select("roxxy_dialogue_deal_confirmation_sex") from _call_expression_2002
        $ M_bissette.trigger(T_bissette_roxxy_meet_inform)

    elif M_roxxy.is_state(S_roxxy_get_fake_id):
        if M_roxxy.get("talked to roxxy id"):
            call expression game.dialog_select("button_roxxy_get_fake_id") from _call_expression_2003
        else:
            call expression game.dialog_select("button_roxxy_get_fake_id_first") from _call_expression_2004
            $ M_roxxy.set("talked to roxxy id", True)

    elif M_roxxy.is_state(S_roxxy_fake_id_ask_terry):
        call expression game.dialog_select("button_roxxy_fake_id_ask_terry") from _call_expression_2005
        $ M_roxxy.set("take roxxy mall", True)
        $ player.go_to(L_map)
        $ game.main()

    elif M_roxxy.is_state(S_roxxy_fake_id_get_picture):
        call expression game.dialog_select("button_roxxy_fake_id_get_picture") from _call_expression_2006
    else:

        if M_roxxy.get("roxxy relationship") == 0:
            call expression game.dialog_select("french_roxxy_dialogue_relationship_0") from _call_expression_2007
            $ game.main()
        call expression game.dialog_select("french_roxxy_dialogue_relationship_{}".format(M_roxxy.get("roxxy relationship"))) from _call_expression_2008
        menu:
            "Model." if M_ross.is_state(S_ross_ask_model):
                call expression game.dialog_select("roxxy_dialogue_ask_model") from _call_expression_2009

            "Talent Show." if M_dewitt.is_set("talent ask roxxy"):
                if M_dewitt.is_set("talent helping kevin"):
                    call expression game.dialog_select("dewitt_talent_show_helping_kevin") from _call_expression_2010

                elif M_dewitt.is_set("talent helping eve"):
                    call expression game.dialog_select("dewitt_talent_show_helping_eve") from _call_expression_2011
                else:

                    call expression game.dialog_select("roxxy_dialogue_talent_show_help") from _call_expression_2012
                    $ M_dewitt.set("talent ask roxxy", False)

            "How's everything going?" if M_roxxy.is_state(S_roxxy_hows_it_going):
                call expression game.dialog_select("button_roxxy_hows_it_going") from _call_expression_2013
                $ M_roxxy.trigger(T_roxxy_chat_with_becca_missy)

            "How's it going?" if not M_roxxy.is_state(S_roxxy_hows_it_going) and M_roxxy.get("roxxy relationship") in (1,2):
                call expression game.dialog_select("button_roxxy_hows_it_going_relationship_{}".format(M_roxxy.get("roxxy relationship"))) from _call_expression_2014

            "Exams." if M_roxxy.is_state(S_roxxy_sneak_into_smith):
                call expression game.dialog_select("button_roxxy_sneak_into_smith") from _call_expression_2015

            "Drinks." if M_roxxy.is_state(S_roxxy_need_booze):
                if M_roxxy.get("talked to roxxy booze"):
                    call expression game.dialog_select("button_roxxy_need_booze") from _call_expression_2016
                else:
                    call expression game.dialog_select("button_roxxy_need_booze_first") from _call_expression_2017
                    $ M_roxxy.set("talked to roxxy booze", True)

            "Any word from {b}Clyde{/b}?" if M_roxxy.get("roxxy relationship") not in (3,4) and M_roxxy.finished_state(S_roxxy_shut_down_lab):
                call expression game.dialog_select("button_roxxy_french_whats_up_clyde_relationship_2") from _call_expression_2018

            "What's up with {b}Clyde{/b}?" if M_roxxy.get("roxxy relationship") in (3,4):
                call expression game.dialog_select("button_roxxy_french_whats_up_clyde_relationship_{}".format(M_roxxy.get("roxxy relationship"))) from _call_expression_2019

            "Meet me at my locker." if M_roxxy.get("roxxy locker sex") and not M_roxxy.is_set("meet for locker sex"):
                call expression game.dialog_select("button_roxxy_meet_me_at_my_locker") from _call_expression_2020
                $ M_roxxy.set("meet for locker sex", True)

            "I'll see you tonight" if M_roxxy.get("roxxy relationship") == 4:
                call expression game.dialog_select("button_roxxy_ill_see_you_tonight") from _call_expression_2021

            "Nothing." if M_roxxy.get("roxxy relationship")<=2:
                call expression game.dialog_select("french_roxxy_dialogue_leave_relationship_{}".format(M_roxxy.get("roxxy relationship"))) from _call_expression_2022

            "I'll be fine." if M_roxxy.get("roxxy relationship")==3:
                call expression game.dialog_select("french_roxxy_dialogue_leave_relationship_{}".format(M_roxxy.get("roxxy relationship"))) from _call_expression_2023

            "I should go." if M_roxxy.get("roxxy relationship")==4:
                call expression game.dialog_select("french_roxxy_dialogue_leave_relationship_{}".format(M_roxxy.get("roxxy relationship"))) from _call_expression_2024
    hide roxxy
    hide player
    with dissolve
    $ game.main()

label roxxy_third_floor_dialogue:
    if M_roxxy.is_state(S_roxxy_teachers_event):
        call expression game.dialog_select("button_roxxy_intro") from _call_expression_2025
        $ M_roxxy.trigger(T_roxxy_locker_room)
    $ game.main()

label roxxy_trailer_button_dialogue:
    scene expression player.location.background_blur
    if M_roxxy.get("roxxy relationship") == 0:
        call expression game.dialog_select("home_roxxy_dialogue_relationship_0") from _call_expression_2026
        $ game.main()
    call expression game.dialog_select("home_roxxy_dialogue_relationship_{}".format(M_roxxy.get("roxxy relationship"))) from _call_expression_2027
    menu:
        "Wanna hang out?" if M_roxxy.get("roxxy relationship") == 1:
            call expression game.dialog_select("button_roxxy_home_hang_out") from _call_expression_2028

        "Any word from {b}Clyde{/b}?" if M_roxxy.get("roxxy relationship") == 2:
            call expression game.dialog_select("button_roxxy_french_whats_up_clyde_relationship_{}".format(M_roxxy.get("roxxy relationship"))) from _call_expression_2029

        "How's it going?" if M_roxxy.get("roxxy relationship") == 2:
            call expression game.dialog_select("button_roxxy_home_hows_it_going") from _call_expression_2030

        "What's up with {b}Clyde{/b}?" if M_roxxy.get("roxxy relationship") in (3,4):
            call expression game.dialog_select("button_roxxy_french_whats_up_clyde_relationship_{}".format(M_roxxy.get("roxxy relationship"))) from _call_expression_2031

        "Hang out." if M_roxxy.is_state(S_roxxy_end) and game.timer.is_dark():
            if not M_roxxy.get("roxxy trailer sex"):
                call expression game.dialog_select("button_roxxy_trailer_bed_sex_first") from _call_expression_2032
            else:
                label roxxy_bedroom_fuck_hscene_replay:
                    call expression game.dialog_select("button_roxxy_trailer_bed_sex_repeat") from _call_expression_2033
            $ anim_toggle = True
            $ M_roxxy.set("sex speed", .09)
            call expression game.dialog_select("button_roxxy_trailer_bed_sex_loop_pre") from _call_expression_2034
            jump expression game.dialog_select("button_roxxy_trailer_bed_sex_loop")

        "Nothing." if M_roxxy.get("roxxy relationship") <= 3:
            call expression game.dialog_select("home_roxxy_dialogue_leave_relationship_{}".format(M_roxxy.get("roxxy relationship"))) from _call_expression_2035

        "I should go." if M_roxxy.get("roxxy relationship") == 4:
            call expression game.dialog_select("home_roxxy_dialogue_leave_relationship_{}".format(M_roxxy.get("roxxy relationship"))) from _call_expression_2036
    $ game.main()

label roxxy_beach_button_dialogue:
    scene expression game.timer.image("backgrounds/location_beach_water{}_blur.jpg")
    if M_roxxy.get("roxxy relationship") == 0:
        call expression game.dialog_select("beach_roxxy_dialogue_relationship_0") from _call_expression_2037
        $ game.main()
    if M_roxxy.finished_state(S_roxxy_spin_bottle):
        call expression game.dialog_select("button_roxxy_beach_intro") from _call_expression_2038
    else:
        call expression game.dialog_select("beach_roxxy_dialogue_relationship_{}".format(M_roxxy.get("roxxy relationship"))) from _call_expression_2039
    menu:
        "I'll play" if M_roxxy.finished_state(S_roxxy_spin_bottle):
            call expression game.dialog_select("button_roxxy_beach_spin_bottle") from _call_expression_2040
            if M_roxxy.get("roxxy beach sex") or M_becca.get("becca beach sex") or M_missy.get("missy beach sex") or M_player.get("mc beach sex"):
                call expression game.dialog_select("button_roxxy_beach_spin_bottle_sex_repeat") from _call_expression_2041
            $ M_player.set("beach bottle spins", 0)
            call screen spin_bottle_minigame

        "How about a massage?" if M_roxxy.finished_state(S_roxxy_get_oil):
            call expression game.dialog_select("roxxy_beach_button_massage") from _call_expression_2042
            $ M_roxxy.set("massage", True)

        "Nah, not tonight." if M_roxxy.finished_state(S_roxxy_spin_bottle):
            call expression game.dialog_select("button_roxxy_beach_leave") from _call_expression_2043

        "Nothing." if not M_roxxy.finished_state(S_roxxy_spin_bottle):
            call expression game.dialog_select("button_roxxy_beach_leave_before_spin_bottle") from _call_expression_2044
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
