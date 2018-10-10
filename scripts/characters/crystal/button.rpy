label roxmom_dialogue:
    scene expression game.timer.image("trailer_interior_c{}")
    if M_crystal.is_state(S_crystal_start):
        $ M_crystal.trigger(T_crystal_intro)

    if M_roxxy.is_state(S_roxxy_picnic_done):
        call expression game.dialog_select("button_crystal_roxxy_go_to_picnic") from _call_expression_1536
    else:
        if M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
            if game.timer.is_dark():
                call expression game.dialog_select("button_crystal_rox8_11_evening") from _call_expression_1537
            else:
                call expression game.dialog_select("button_crystal_rox8_11_day") from _call_expression_1538
        elif M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
            if game.timer.is_dark():
                call expression game.dialog_select("button_crystal_final_evening") from _call_expression_1539
            else:
                call expression game.dialog_select("button_crystal_final_day") from _call_expression_1540
        else:
            call expression game.dialog_select("button_crystal_preamble") from _call_expression_1541
    show crystal 1
    menu roxmom_dialogue_repeat:
        "Where's {b}Roxxy{/b}?" if not game.timer.is_dark():
            if M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
                call expression game.dialog_select("button_crystal_roxxy_rox8_rox11") from _call_expression_1542
            elif M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
                call expression game.dialog_select("button_crystal_roxxy_final") from _call_expression_1543
            else:
                call expression game.dialog_select("button_crystal_roxxy") from _call_expression_1544
            jump expression game.dialog_select("roxmom_dialogue_repeat")

        "So you're {b}Roxxy's mom{/b}?" if not game.timer.is_dark() and M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_roxxys_mom") from _call_expression_1545

        "Is {b}Roxxy{/b} busy?" if game.timer.is_dark() and M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_roxxy_busy") from _call_expression_1546

        "Yeah, is she here?" if game.timer.is_dark() and M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_she_here") from _call_expression_1547
            jump expression game.dialog_select("roxmom_dialogue_repeat")

        "Are you happy to be home" if not game.timer.is_dark() and M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_happy_home") from _call_expression_1548
            jump expression game.dialog_select("roxmom_dialogue_repeat")
        "{b}Roxxy's dad{/b}.":

            call expression game.dialog_select("button_crystal_roxxys_dad") from _call_expression_1549
            jump expression game.dialog_select("roxmom_dialogue_repeat")

        "Offer." if M_crystal.is_set("crystal sex offer") and not M_roxxy.get("roxxy crystal sex"):
            call expression game.dialog_select("trailer_interior_crystal_sex_offer_pre_repeat") from _call_expression_1550
            jump expression game.dialog_select("trailer_interior_crystal_sex_offer_menu")

        "Quickie." if M_roxxy.get("roxxy crystal sex") and L_trailer.is_here(M_crystal):
            call expression game.dialog_select("trailer_interior_crystal_sex_repeat_outside_offer_pre") from _call_expression_1551
            jump expression game.dialog_select("trailer_interior_crystal_sex_repeat_outside_offer_menu")

        "Quickie." if M_roxxy.get("roxxy crystal sex") and L_trailer_interior.is_here(M_crystal):
            label crystal_hscene_replay:
                if not store._in_replay == None:
                    scene expression game.timer.image("trailer_interior_c{}")
                    show player 11 at left
                    show crystal 2 at right
                    with dissolve
            call expression game.dialog_select("trailer_interior_crystal_sex_repeat_inside") from _call_expression_1552
            call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_menu") from _call_expression_1553
            $ anim_toggle = True
            jump expression game.dialog_select("trailer_interior_crystal_sex_loop")

        "Sorry to bother you" if M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_sorry_to_bother") from _call_expression_1554

        "I should go" if game.timer.is_dark() and M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_should_go_evening") from _call_expression_1555

        "I should go" if not game.timer.is_dark() and M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_should_go_day") from _call_expression_1556

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
