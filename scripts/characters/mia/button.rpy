label mia_button_dialogue:
    if M_helen.is_set("helen route"):
        call expression game.dialog_select("mia_dialogue_helen_route") from _call_expression_870

    elif M_mia.is_state(S_mia_helen_change_news):
        call expression game.dialog_select("mia_dialogue_helen_change_news") from _call_expression_871
        $ M_mia.trigger(T_mia_thanks)
        $ game.main()

    if player.location == L_miahouse_miaroom:
        if M_mia.is_state(S_mia_end):
            call expression game.dialog_select("mia_dialogue_mia_bedroom_mia_end_intro") from _call_expression_872
            menu:
                "Study":
                    call expression game.dialog_select("mia_dialogue_mia_bedroom_mia_end_study") from _call_expression_873
                    $ M_mia.set("sex speed", .175)
                    jump expression game.dialog_select("mia_strip_repeat")
                "I have to go.":

                    call expression game.dialog_select("mia_dialogue_mia_bedroom_mia_end_leave") from _call_expression_874
                    $ game.main()

        elif M_mia.is_state(S_mia_night_visit):
            jump expression game.dialog_select("mia_strip_show")

        elif M_mia.is_state(S_mia_tattoo_help):
            call expression game.dialog_select("mia_dialogue_mia_bedroom_mia_tattoo_help") from _call_expression_875
            $ game.timer.tick()
            $ M_mia.trigger(T_mia_delay)
            $ player.go_to(L_miahouse)
            $ game.main()

        elif M_mia.is_state(S_mia_church_plan):
            call expression game.dialog_select("mia_dialogue_mia_bedroom_mia_church_plan") from _call_expression_876
        else:

            call expression game.dialog_select("mia_dialogue_mia_bedroom_intro") from _call_expression_877

    elif player.location == L_school_scienceclassroom:
        show mial 1f zorder 2 at right
        if M_mia.is_state(S_mia_strip_aftermath):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_strip_aftermath") from _call_expression_878
            $ game.main()

        elif M_mia.is_state(S_mia_consult):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_consult") from _call_expression_879
            $ M_mia.trigger(T_mia_plan)

        elif M_mia.is_state(S_mia_parent_unblock):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_parent_unblock") from _call_expression_880
            $ M_mia.trigger(T_mia_results)
            $ game.main()

        elif M_mia.is_state(S_mia_favor):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_favor") from _call_expression_881
            $ M_mia.trigger(T_mia_dinner_plan)
            $ game.main()

        elif M_mia.is_state(S_mia_need_space):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_need_space") from _call_expression_882
            $ game.main()

        elif M_mia.is_state(S_mia_church_plan):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_church_plan") from _call_expression_883

        elif M_mia.is_state(S_mia_urgent_help):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_urgent_help") from _call_expression_884
        else:

            call expression game.dialog_select("mia_dialogue_science_classroom_intro") from _call_expression_885

    elif player.location == L_miahouse_entrance:
        if M_mia.is_state(S_mia_favor):
            call expression game.dialog_select("mia_dialogue_mias_house_entrance_mia_favor") from _call_expression_886
            $ M_mia.trigger(T_mia_dinner_plan)
            $ game.main()

        elif M_mia.is_state(S_mia_helen_talk):
            call expression game.dialog_select("mia_dialogue_mias_house_entrance_mia_helen_talk") from _call_expression_887
            $ game.main()

        elif M_mia.is_state([S_mia_church_plan, S_mia_clues]):
            call expression game.dialog_select("mia_dialogue_mias_house_entrance_mia_church_plan") from _call_expression_888
        else:

            call expression game.dialog_select("mia_dialogue_mias_house_entrance_intro") from _call_expression_889
    menu mia_dialogue:
        "Chat" if player.location == L_miahouse_miaroom:
            call expression game.dialog_select("mia_dialogue_chat") from _call_expression_890
            jump expression game.dialog_select("mia_dialogue")

        "Talent Show." if M_dewitt.is_set("talent ask mia"):
            if M_dewitt.is_set("talent helping kevin"):
                call expression game.dialog_select("dewitt_talent_show_helping_kevin") from _call_expression_891

            elif M_dewitt.is_set("talent helping eve"):
                call expression game.dialog_select("dewitt_talent_show_helping_eve") from _call_expression_892
            else:

                call expression game.dialog_select("mia_dialogue_talent_show_help") from _call_expression_893
                $ M_dewitt.set("talent ask mia", False)

        "Parents." if player.location == L_school_scienceclassroom and M_mia.between_states(S_mia_start, S_mia_helen_refusal):
            call expression game.dialog_select("mia_dialogue_parents") from _call_expression_894
            jump expression game.dialog_select("mia_dialogue")

        "{b}Harold{/b}." if M_mia.is_state(S_mia_clues):
            call expression game.dialog_select("mia_dialogue_mia_clues") from _call_expression_895

        "{b}Harold{/b}." if M_mia.is_state(S_mia_convince_harold):
            call expression game.dialog_select("mia_dialogue_mia_convince_harold") from _call_expression_896

        "Glasses." if M_mia.is_state(S_mia_harold_gift):
            call expression game.dialog_select("mia_dialogue_glasses") from _call_expression_897

        "Donuts." if M_mia.is_state(S_mia_impress_harold):
            call expression game.dialog_select("mia_dialogue_donuts") from _call_expression_898
            jump expression game.dialog_select("mia_dialogue")

        "Tattoo." if M_mia.is_state([S_mia_find_easel, S_mia_draw_tattoo]):
            call expression game.dialog_select("mia_dialogue_mia_draw_tattoo") from _call_expression_899

        "Tattoo." if list(set(["tattoo_dolphin", "tattoo_stars", "tattoo_flowers", "tattoo_skull", "tattoo_cookie"]) & set(player.inventory.items)):
            call expression game.dialog_select("mia_dialogue_mia_show_tattoo_fail") from _call_expression_900
            $ player.remove_item(drawn_tattoo)
            $ M_mia.trigger(T_mia_wrong_tattoo)

        "Tattoo." if player.has_item("tattoo_butterfly"):
            call expression game.dialog_select("mia_dialogue_mia_show_tattoo_pass") from _call_expression_901
            $ player.remove_item(drawn_tattoo)
            $ M_mia.trigger(T_mia_right_tattoo)

        "Sugar Tats" if M_mia.is_state([S_mia_get_tattoo, S_mia_buy_tattoo]):
            call expression game.dialog_select("mia_dialogue_mia_get_tattoo") from _call_expression_902

        "Church." if M_mia.is_state(S_mia_church_plan):
            call expression game.dialog_select("mia_dialogue_church") from _call_expression_903

        "Art Sessions." if player.location == L_school_scienceclassroom and M_ross.is_state(S_ross_ask_mia_partner):
            call expression game.dialog_select("mia_dialogue_art_sessions_intro") from _call_expression_904
            if player.has_required_chr(3):
                call expression game.dialog_select("mia_dialogue_art_sessions_stat_pass") from _call_expression_905
                $ M_ross.trigger(T_ross_convinced_mia)
            else:

                call expression game.dialog_select("mia_dialogue_art_sessions_stat_fail") from _call_expression_906

        "Homework." if player.location == L_school_scienceclassroom and not M_helen.is_set("helen route"):
            if not M_mia.between_states(S_mia_start, S_mia_helen_refusal) and not M_mia.is_state([S_mia_study_sex, S_mia_end]):
                call expression game.dialog_select("mia_dialogue_homework_want_parents_back") from _call_expression_907
            else:

                call expression game.dialog_select("mia_dialogue_homework_intro") from _call_expression_908
                if M_mia.is_state(S_mia_do_homework):
                    call expression game.dialog_select("mia_dialogue_homework_still_busy") from _call_expression_909
                    $ game.main()
                else:

                    call expression game.dialog_select("mia_dialogue_homework_study") from _call_expression_910
                jump expression game.dialog_select("mia_dialogue")

        "Study" if player.location == L_miahouse_miaroom and not M_helen.is_set('helen route'):
            if M_mia.is_set("study"):
                call expression game.dialog_select("mia_dialogue_study_repeat") from _call_expression_911
                $ game.timer.tick()
                $ player.go_to(L_miahouse)
                $ game.main()
            else:

                if M_mia.between_states(S_mia_start, S_mia_helen_refusal):
                    call expression game.dialog_select("mia_dialogue_study_first") from _call_expression_912
                    jump expression game.dialog_select("mia_study")
                else:

                    call expression game.dialog_select("mia_dialogue_study_want_parents_back") from _call_expression_913
                    jump expression game.dialog_select("mia_dialogue")

        "I have to go." if player.location == L_miahouse_miaroom:
            call expression game.dialog_select("mia_dialogue_mias_bedroom_leave") from _call_expression_914

        "Nothing." if player.location == L_school_scienceclassroom:
            call expression game.dialog_select("mia_dialogue_science_classroom_leave") from _call_expression_915

        "I have to go." if player.location == L_miahouse_entrance:
            call expression game.dialog_select("mia_dialogue_mias_house_entrance_leave") from _call_expression_916
    hide player
    hide mia
    hide mial
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
