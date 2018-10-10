label garden_dialogue:
    $ player.go_to(L_diane_garden)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if not game.timer.is_dark():
        if aunt_shed_scene and not aunt.known(aunt_drunken_splur):
            call expression game.dialog_select("dianes_garden_diane_drunken_splur_not_known") from _call_expression_1737

            $ aunt.add_event(aunt_drunken_splur)

        elif quest09_3 and not aunt.known(aunt_mouse_attack):
            call expression game.dialog_select("dianes_garden_diane_mouse_attack_not_known") from _call_expression_1738

            $ aunt.add_event(aunt_mouse_attack)

        elif aunt_count == 0 and not aunt_dialogue_advance:
            if in_garden:
                $ in_garden = False
                $ game.main()

            if quest20 not in quest_list:
                call expression game.dialog_select("dianes_garden_diane_need_shovel") from _call_expression_1739
                $ quest_list.append(quest20)

                if not player.has_item("shovel"):
                    call expression game.dialog_select("dianes_garden_diane_need_shovel_no_shovel") from _call_expression_1740
                else:

                    call expression game.dialog_select("dianes_garden_diane_need_shovel_have_shovel") from _call_expression_1741
                    call expression game.dialog_select("dianes_garden_diane_have_shovel") from _call_expression_1742
                    $ L_bank.unlock()
                    $ aunt_dialogue_advance = True
                    $ completed_quests.append(quest20)
                    $ game.main()

        elif aunt_count == 1 and quest21 not in completed_quests and garden_done >= 3:
            if in_garden:
                $ in_garden = False
                $ game.main()

            scene location_diane_garden_day_blur
            if quest21 in quest_list:
                call expression game.dialog_select("dianes_garden_diane_need_shovel_remove_waste_repeat") from _call_expression_1743
            else:

                call expression game.dialog_select("dianes_garden_diane_need_shovel_remove_waste") from _call_expression_1744
                $ quest_list.append(quest21)

            if player.stats.str() >= 2:
                call expression game.dialog_select("dianes_garden_diane_need_shovel_remove_waste_pass") from _call_expression_1745
                $ completed_quests.append(quest21)
                $ aunt_dialogue_advance = True
            else:

                call expression game.dialog_select("dianes_garden_diane_need_shovel_remove_waste_fail") from _call_expression_1746

        elif aunt_count == 2 and quest08 not in quest_list:
            if in_garden:
                $ in_garden = False
                $ game.main()
            call expression game.dialog_select("dianes_garden_diane_retrieve_pump") from _call_expression_1747
            $ shed_unlocked = True
            $ quest_list.append(quest08)

        elif aunt_count == 3 and not aunt_dialogue_advance and quest09 not in quest_list:
            if not game.timer.is_weekend():
                if in_garden:
                    $ in_garden = False
                    $ game.main()
                call expression game.dialog_select("dianes_garden_diane_milk_delivery_week") from _call_expression_1748
                $ quest_list.append(quest09)
                $ M_annie.place(place = L_school_cafeteria)
                $ M_annie.force(tod = [0,1])
            else:


                call expression game.dialog_select("dianes_garden_diane_milk_delivery_weekend") from _call_expression_1749

        elif aunt_count == 4 and not aunt_dialogue_advance and quest10 not in quest_list:
            if quest10 in quest_list and not infestation_done:
                scene garden_dead with None
            else:

                scene garden with None
            call expression game.dialog_select("dianes_garden_diane_bug_infestation") from _call_expression_1750
            $ quest_list.append(quest10)

        elif aunt_count == 5 and not aunt_dialogue_advance:
            if in_garden:
                $ in_garden = False
                $ game.main()
            call expression game.dialog_select("dianes_garden_diane_missing") from _call_expression_1751


        elif aunt_count == 6 and not aunt_dialogue_advance:
            if in_garden:
                $ in_garden = False
                $ game.main()
            label dianes_garden_diane_sunbathing_replay:
                call expression game.dialog_select("dianes_garden_diane_sunbathing") from _call_expression_1752
            menu:
                "Sure!":
                    call expression game.dialog_select("dianes_garden_diane_sunbathing_okay") from _call_expression_1753
                    $ renpy.end_replay()
                    $ persistent.cookie_jar["Diane"]["unlocked"] = True
                    $ persistent.cookie_jar["Diane"]["gallery"]["01_unlocked"] = True
                    $ drunk_dialogue = True
                    $ aunt_dialogue_advance = True
                    call expression game.dialog_select("map_dialogue") from _call_expression_1754

                "I'd rather not." if store._in_replay == None:
                    call expression game.dialog_select("dianes_garden_diane_sunbathing_leave") from _call_expression_1755
                    $ game.main()

        elif aunt_count == 6 and aunt_dialogue_advance and drunk_dialogue:
            call expression game.dialog_select("dianes_garden_diane_do_not_disturb") from _call_expression_1756
            call expression game.dialog_select("map_dialogue") from _call_expression_1757

        elif aunt_count == 7 and not aunt_apology_seen:
            if in_garden:
                $ in_garden = False
                $ game.main()

            if drunk_dialogue:
                call expression game.dialog_select("dianes_garden_diane_drunk_apology") from _call_expression_1758
                $ aunt_apology_seen = True
                $ game.main()
        else:

            if aunt_count < 8 and aunt_count != 5:
                if in_garden:
                    $ in_garden = False
                    $ game.main()

                if quest10 in quest_list and not infestation_done:
                    scene garden_dead
                else:
                    scene garden
                call expression game.dialog_select("dianes_garden_diane_gardening_help") from _call_expression_1759
            $ game.main()
    else:

        if quest09 in completed_quests and not aunt_shed_scene and aunt_count < 8:
            if quest10 in quest_list and not infestation_done:
                scene garden_dead_night
            else:

                scene garden_night
            call expression game.dialog_select("dianes_garden_diane_shed_still_open") from _call_expression_1760
        else:

            if aunt_count < 8:
                call expression game.dialog_select("night_closed_garden") from _call_expression_1761
    $ game.main()

label aunt_button_dialogue:
    if aunt_drink_made:
        $ aunt_drink_made = False
        $ aunt_drink_offered = False
        label dianes_dialogue_drink_replay:
            call expression game.dialog_select("dianes_dialogue_drink") from _call_expression_1762
        if not store._in_replay == None or aunt_extra_shot:
            call expression game.dialog_select("dianes_dialogue_drink_extra_shot") from _call_expression_1763
            $ renpy.end_replay()
            $ persistent.cookie_jar["Diane"]["unlocked"] = True
            $ persistent.cookie_jar["Diane"]["gallery"]["02_unlocked"] = True

            $ in_garden = True
            $ aunt_extra_shot = False
            $ aunt_drink_active = False
            $ aunt_dialogue_advance = True
            call expression game.dialog_select("garden_dialogue") from _call_expression_1764
        else:
            $ game.main()

    elif aunt_count < 8:
        call expression game.dialog_select("dianes_dialogue_pre_fun_intro") from _call_expression_1765
        menu dia_default_dialogue_options:
            "Talk.":
                call expression game.dialog_select("dianes_dialogue_pre_fun_talk") from _call_expression_1766
                call expression game.dialog_select("dia_default_dialogue_options") from _call_expression_1767

            "Paint." if M_dewitt.is_state([S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint]):
                call expression game.dialog_select("dianes_dialogue_pre_fun_paint") from _call_expression_1768
                $ M_dewitt.trigger(T_dewitt_shed_paint)

            "I found a shovel." if quest20 in quest_list and quest20 not in completed_quests and player.has_item("shovel"):
                call expression game.dialog_select("dianes_dialogue_pre_fun_found_shovel") from _call_expression_1769
                call expression game.dialog_select("dianes_garden_diane_have_shovel") from _call_expression_1770
                $ L_bank.unlock()
                $ aunt_dialogue_advance = True
                $ completed_quests.append(quest20)
                $ game.main()

            "The garden." if quest20 in completed_quests:
                call expression game.dialog_select("dianes_dialogue_pre_fun_remove_waste") from _call_expression_1771
                call expression game.dialog_select("dia_default_dialogue_options") from _call_expression_1772

            "The pump." if quest08 in quest_list and quest08 not in completed_quests:
                call expression game.dialog_select("dianes_dialogue_pre_fun_pump_intro") from _call_expression_1773
                menu:
                    "Where is it?":
                        call expression game.dialog_select("dianes_dialogue_pre_fun_pump_location") from _call_expression_1774
                        call expression game.dialog_select("dia_default_dialogue_options") from _call_expression_1775
                    "Not yet.":

                        call expression game.dialog_select("dianes_dialogue_pre_fun_pump_not_yet") from _call_expression_1776
                        call expression game.dialog_select("dia_default_dialogue_options") from _call_expression_1777

                    "I found it!" if player.has_item("pump"):
                        call expression game.dialog_select("dianes_dialogue_pre_fun_pump_found") from _call_expression_1778
                        $ player.remove_item("pump")
                        $ quest_complete(quest08)
                        $ aunt_dialogue_advance = True

            "Milk delivery." if quest09 in quest_list and quest09 not in completed_quests:
                call expression game.dialog_select("dianes_dialogue_pre_fun_milk_delivery_intro") from _call_expression_1779
                menu:
                    "Where at school?":
                        call expression game.dialog_select("dianes_dialogue_pre_fun_milk_delivery_location") from _call_expression_1780
                        call expression game.dialog_select("dia_default_dialogue_options") from _call_expression_1781
                    "Not yet.":

                        call expression game.dialog_select("dianes_dialogue_pre_fun_milk_delivery_not_yet") from _call_expression_1782
                        call expression game.dialog_select("dia_default_dialogue_options") from _call_expression_1783

                    "I delivered them!" if quest09_3:
                        call expression game.dialog_select("dianes_dialogue_pre_fun_milk_delivery_delivered") from _call_expression_1784
                        menu:
                            "Sure!":
                                call expression game.dialog_select("dianes_dialogue_pre_fun_milk_delivery_try_milk") from _call_expression_1785
                                $ M_player.set("drank milk", True)
                            "I don't like milk.":

                                call expression game.dialog_select("dianes_dialogue_pre_fun_milk_delivery_do_not_try_milk") from _call_expression_1786
                        $ drink_milk_offer = True
                        $ game.timer.tick()
                        $ completed_quests.append(quest09)
                        $ M_annie.unforce()
                        $ aunt_dialogue_advance = True
                        $ quest09_3 = False

            "Bug infestation." if quest10 in quest_list and not infestation_done:
                call expression game.dialog_select("dianes_dialogue_pre_fun_bug_infestation_intro") from _call_expression_1787
                menu:
                    "What should I do?":
                        call expression game.dialog_select("dianes_dialogue_pre_fun_bug_infestation_task") from _call_expression_1788
                        call expression game.dialog_select("dia_default_dialogue_options") from _call_expression_1789
                    "Not Yet.":

                        call expression game.dialog_select("dianes_dialogue_pre_fun_bug_infestation_not_done") from _call_expression_1790
                        call expression game.dialog_select("dia_default_dialogue_options") from _call_expression_1791

                    "I got rid of them!" if infestation_done:
                        call expression game.dialog_select("dianes_dialogue_pre_fun_bug_infestation_done") from _call_expression_1792
                        $ aunt_dialogue_advance = True
                        $ completed_quests.append(quest10)

            "Make a drink." if aunt_count == 6 and not aunt_dialogue_advance or aunt_count == 7 and not aunt_dialogue_advance:
                if player.stats.chr() >= 5:
                    call expression game.dialog_select("dianes_dialogue_pre_fun_make_drink_pass") from _call_expression_1793
                    $ aunt_drink_offered = True
                    $ aunt_drink_active = True
                else:

                    call expression game.dialog_select("dianes_dialogue_pre_fun_make_drink_fail") from _call_expression_1794
            "I have to work.":

                call expression game.dialog_select("dianes_dialogue_pre_fun_leave") from _call_expression_1795
        $ game.main()

    elif aunt_count >= 8:
        call expression game.dialog_select("dianes_dialogue_after_fun_intro") from _call_expression_1796
        menu dia_default_dialogue_options_kitchen:
            "Talk.":
                call expression game.dialog_select("dianes_dialogue_after_fun_talk") from _call_expression_1797
                call expression game.dialog_select("dia_default_dialogue_options_kitchen") from _call_expression_1798
            "Talk about {b}[deb_name]{/b}.":

                call expression game.dialog_select("dianes_dialogue_after_fun_talk_about_debbie_intro") from _call_expression_1799
                menu:
                    "Yes.":
                        call expression game.dialog_select("dianes_dialogue_after_fun_talk_about_debbie_confess") from _call_expression_1800
                        call expression game.dialog_select("dia_default_dialogue_options_kitchen") from _call_expression_1801
                    "No.":

                        call expression game.dialog_select("dianes_dialogue_after_fun_talk_about_debbie_do_not_confess") from _call_expression_1802
                        call expression game.dialog_select("dia_default_dialogue_options_kitchen") from _call_expression_1803

            "Paint." if M_dewitt.is_state([S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint]):
                call expression game.dialog_select("dianes_dialogue_pre_fun_paint") from _call_expression_1804
                $ M_dewitt.trigger(T_dewitt_shed_paint)

            "Milk production." if not aunt.known(aunt_breeding_guide):
                call expression game.dialog_select("dianes_dialogue_after_fun_diane_breeding_guide_not_known") from _call_expression_1805
                $ quest_list.append(quest12)
                $ aunt.add_event(aunt_breeding_guide)

            "The milk jug." if quest12 in quest_list and quest12 not in completed_quests and not player.has_item("milkjug"):
                call expression game.dialog_select("dianes_dialogue_after_fun_do_not_have_milkjug") from _call_expression_1806

            "The milk jug." if quest12 in quest_list and quest12 not in completed_quests and player.has_item("milkjug"):
                call expression game.dialog_select("dianes_dialogue_after_fun_have_milkjug") from _call_expression_1807
                $ player.remove_item("milkjug")
                $ completed_quests.append(quest12)

            "Milk production book." if aunt.known(aunt_breeding_guide) and player.has_item("breeding_guide") and not aunt.known(aunt_breeding_bull):
                call expression game.dialog_select("dianes_dialogue_after_fun_have_breeding_guide") from _call_expression_1808
                $ aunt.add_event(aunt_breeding_bull)
                $ player.remove_item("breeding_guide")
                call expression game.dialog_select("garden_dialogue") from _call_expression_1809

            "Breeding." if aunt.over(aunt_breeding_bull) and not aunt.known(aunt_breeding_help):
                call expression game.dialog_select("dianes_dialogue_after_fun_diane_breeding_help_not_known_intro") from _call_expression_1810
                menu:
                    "Me!" if player.stats.chr() < 7:
                        call expression game.dialog_select("dianes_dialogue_after_fun_diane_breeding_help_not_known_fail") from _call_expression_1811
                        call expression game.dialog_select("dia_default_dialogue_options_kitchen") from _call_expression_1812

                    "Me!" if player.stats.chr() >= 7:
                        call expression game.dialog_select("dianes_dialogue_after_fun_diane_breeding_help_not_known_pass") from _call_expression_1813
                        $ aunt.add_event(aunt_breeding_help)
                    "Not yet.":

                        call expression game.dialog_select("dianes_dialogue_after_fun_diane_breeding_help_not_known_leave") from _call_expression_1814
            "Have fun.":

                label dianes_dialogue_after_fun_have_fun_replay:
                    call expression game.dialog_select("dianes_dialogue_after_fun_have_fun") from _call_expression_1815
                if store._in_replay == None and not aunt_had_sex:
                    call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_first_time") from _call_expression_1816
                    menu:
                        "Yes.":
                            call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_first_time_yes") from _call_expression_1817
                            menu dia_sex_options:
                                "I want you." if player.stats.chr() < 7:
                                    call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_first_time_want_fail") from _call_expression_1818
                                    call expression game.dialog_select("dia_sex_options") from _call_expression_1819

                                "I want you." if player.stats.chr() >= 7:
                                    call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_first_time_want_pass") from _call_expression_1820
                                    $ M_aunt.set("sex speed", .4)
                                    call expression game.dialog_select("aunt_sex_loop") from _call_expression_1821
                                "Do more.":

                                    call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_first_time_more") from _call_expression_1822
                else:

                    call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_repeat") from _call_expression_1823
                    $ anim_toggle = False
                    $ xray_toggle = False
                    $ M_aunt.set("sex speed", .4)
                    menu dia_sex_options_2:
                        "Play with clit.":
                            call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_repeat_clit_play") from _call_expression_1824
                            call expression game.dialog_select("dia_sex_options_2") from _call_expression_1825
                        "Play with vegetable.":

                            call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_repeat_vegetable_play") from _call_expression_1826
                            call expression game.dialog_select("dia_sex_options_2") from _call_expression_1827
                        "Fuck raw.":

                            call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_repeat_raw_sex") from _call_expression_1828
                            $ condom_on = False
                            call expression game.dialog_select("aunt_sex_loop") from _call_expression_1829
                        "Fuck with condom.":

                            call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_repeat_safe_sex") from _call_expression_1830
                            $ condom_on = True
                            call expression game.dialog_select("aunt_sex_loop") from _call_expression_1831
            "I should go.":

                call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_repeat_leave") from _call_expression_1832
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
