label classroom_dialogue:
    $ player.go_to(L_school_frenchclassroom)
    call pa_announcement from _call_pa_announcement_14
    if M_roxxy.is_state(S_roxxy_lolipop):
        call expression game.dialog_select("french_class_roxxy_lolipop_intro") from _call_expression_2221
        menu:
            "Just this once.":
                call expression game.dialog_select("french_class_roxxy_lolipop_just_once") from _call_expression_2222
                $ M_roxxy.trigger(T_roxxy_lolipop_once)
            "In exchange for your Lolipop.":
                call expression game.dialog_select("french_class_roxxy_lolipop_for_lolipop") from _call_expression_2223
                $ M_roxxy.trigger(T_roxxy_lolipop_lolipop)

    elif M_roxxy.is_state(S_roxxy_dexter_alcohol_fight) and not M_roxxy.get("alcohol talked to eve"):
        call expression game.dialog_select("frenchclassroom_roxxy_dexter_alcohol_fight") from _call_expression_2224
        $ M_roxxy.set("alcohol talked to eve", True)

    elif M_roxxy.is_state(S_roxxy_ask_exam_copy):
        call expression game.dialog_select("frenchclassroom_roxxy_ask_exam_copy") from _call_expression_2225
        $ M_roxxy.trigger(T_roxxy_find_exams)
        $ game.sleep_lock = True

    if player.location.is_here(M_bissette):
        if M_bissette.is_state(S_bissette_intro):
            call expression game.dialog_select("french_classroom_bissette_intro") from _call_expression_2226
            $ M_bissette.trigger(T_bissette_improvement_challenge)

        elif M_bissette.is_state(S_bissette_tutoring):
            call expression game.dialog_select("french_classroom_bissette_tutoring") from _call_expression_2227

        elif M_bissette.is_state(S_bissette_study):
            call expression game.dialog_select("french_classroom_bissette_study") from _call_expression_2228
            $ M_mia.trigger(T_mc_homework)
            $ M_bissette.trigger(T_bissette_private_study)
            $ player.go_to(L_map)
            $ game.timer.tick(2)

        elif M_bissette.is_state(S_bissette_smith_report):
            call expression game.dialog_select("french_classroom_bissette_smith_report") from _call_expression_2229
            $ M_bissette.trigger(T_bissette_smith_threat)

        elif M_bissette.is_state(S_bissette_hand_in_assignment):
            call expression game.dialog_select("french_classroom_bissette_hand_in_assignment") from _call_expression_2230
            $ M_bissette.trigger(T_bissette_private_study)
            $ player.go_to(L_map)
            $ game.timer.tick(2)

        elif M_bissette.is_state(S_bissette_poem_assignment):
            call expression game.dialog_select("french_classroom_bissette_poem_assignment") from _call_expression_2231
            $ M_bissette.trigger(T_bissette_french_poem)

        elif M_bissette.is_state(S_bissette_hand_in_poem_assignment):
            call expression game.dialog_select("french_classroom_bissette_hand_in_poem_assignment_pre") from _call_expression_2232
            if M_roxxy.get("roxxy trailer sex"):
                call expression game.dialog_select("french_classroom_bissette_hand_in_poem_assignment_roxxy_sex") from _call_expression_2233
            else:
                call expression game.dialog_select("french_classroom_bissette_hand_in_poem_assignment_no_roxxy_sex") from _call_expression_2234
            label french_classroom_bissette_assignment_replay:
            if M_mom.is_set("practice kissing"):
                call expression game.dialog_select("french_classroom_bissette_hand_in_poem_assignment_have_kissed") from _call_expression_2235
            else:
                call expression game.dialog_select("french_classroom_bissette_hand_in_poem_assignment_havent_kissed") from _call_expression_2236
            call expression game.dialog_select("french_classroom_bissette_hand_in_poem_assignment_continue") from _call_expression_2237
            $ renpy.end_replay()
            $ persistent.cookie_jar["Bissette"]["unlocked"] = True
            $ persistent.cookie_jar["Bissette"]["gallery"]["01_unlocked"] = True
            $ M_bissette.trigger(T_bissette_private_study)
            $ player.go_to(L_map)
            $ game.timer.tick(2)

        elif M_bissette.is_state(S_bissette_quiz):
            jump expression game.dialog_select("french_classroom_bissette_quiz")

        elif M_bissette.is_state(S_bissette_smith_final_report):
            call expression game.dialog_select("french_classroom_bissette_smith_final_report") from _call_expression_2238
            $ M_bissette.trigger(T_bissette_smith_pleased)
            $ M_bissette.set_default_locations([[L_school_frenchclassroom, L_school_bissetteoffice, L_school_bissetteoffice, L_NULL],
                                                [L_NULL, L_NULL, L_NULL, L_NULL]])
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
