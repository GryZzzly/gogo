label sis_button_dialogue:
    if sis_panties_trade:
        if not sis_panties_bought:
            call expression game.dialog_select("jenny_dialogue_panties_trade_pre") from _call_expression_672
            if player.has_money(100):
                menu:
                    "Here's $100.":
                        $ player.spend_money(100)
                        $ player.get_item("panties")
                        $ sis_panty01.finish()
                        $ completed_quests.append(quest07)
                        $ sis_panties_bought = True
                        call expression game.dialog_select("jenny_dialogue_panties_trade_buy") from _call_expression_673
                    "I don't need it.":

                        call expression game.dialog_select("jenny_dialogue_panties_trade_do_not_buy") from _call_expression_674
            else:

                menu:
                    "I don't have enough.":
                        call expression game.dialog_select("jenny_dialogue_panties_trade_cant_buy") from _call_expression_675
            jump expression game.dialog_select("hallway_dialogue")
        else:

            call expression game.dialog_select("jenny_dialogue_pre") from _call_expression_676
            menu sis_bedroom_menu:
                "Talk.":
                    if not sister.over(sis_shower_cuddle02):
                        call expression game.dialog_select("jennybedroom_talk_after_cuddle") from _call_expression_677
                    else:
                        call expression game.dialog_select("jenny_dialogue_talk_before_cuddle") from _call_expression_678

                "I love you." if sister.over(sis_final2):
                    if sis_confession_first:
                        call expression game.dialog_select("jenny_dialogue_confess_first") from _call_expression_679
                        $ sis_confession_first = False
                    else:

                        call expression game.dialog_select("jenny_dialogue_confess_repeat") from _call_expression_680
                    jump expression game.dialog_select("hallway_dialogue")

                "{b}Roxxy{/b}." if M_bissette.is_state(S_bissette_jenny_mentoring_payment):
                    call expression game.dialog_select("jenny_dialogue_roxxy_pre") from _call_expression_681
                    menu:
                        "Pay" if player.has_money(500):
                            $ player.spend_money(500)
                            call expression game.dialog_select("jenny_dialogue_roxxy_pay") from _call_expression_682
                            $ M_bissette.trigger(T_bissette_jenny_paid)
                        "Don't Pay":

                            call expression game.dialog_select("jenny_dialogue_roxxy_do_not_pay") from _call_expression_683

                "{b}[deb_name]{/b} needs you." if sis_panties_bought and not sis_diary_unlocked and sister.over(sis_shower_cuddle01) and sister.completed(sis_panty02):
                    call expression game.dialog_select("sis_bedroom_sis_mom_needs_you") from _call_expression_684
                    $ diary_scene = True
                    $ sis_diary_unlocked = True
                    $ M_jenny.place(place = L_NULL)
                    $ M_jenny.force(tod = [0,1])

                "Trade for panties." if not sister.completed(sis_panty04):
                    call expression game.dialog_select("jenny_dialogue_trade_panties") from _call_expression_685

                "Make a deal." if sister.over(sis_breakfast):
                    call expression game.dialog_select("jenny_dialogue_make_deal") from _call_expression_686
                    jump expression game.dialog_select("hallway_dialogue")

                "Cam show." if sister.known(sis_final2):
                    $ sis_cheerleader_sex2_menu = False
                    if sister.completed(sis_final2):
                        $ game.timer.tick()
                        $ anim_toggle = False
                        $ xray = False
                        call expression game.dialog_select("jenny_dialogue_cam_show_pre") from _call_expression_687
                        if sis_final_cum == "Inside" and sis_final_cum_inside_first:
                            call expression game.dialog_select("jenny_dialogue_cam_show_pre_inside") from _call_expression_688
                            $ sis_final_cum_inside_first = False

                        elif sis_final_cum == "Outside":
                            call expression game.dialog_select("jenny_dialogue_cam_show_pre_outside") from _call_expression_689
                        call expression game.dialog_select("jenny_dialogue_cam_show_pre_after") from _call_expression_690
                        jump expression game.dialog_select("sis_cheerleader_fuck_looprep")

                    elif not player.has_item("handcuffs") or not player.has_item("cheerleader_outfit"):
                        call expression game.dialog_select("jenny_dialogue_cam_show_no_items") from _call_expression_691
                        jump expression game.dialog_select("hallway_dialogue")

                    elif player.has_item("handcuffs") and player.has_item("cheerleader_outfit"):
                        $ game.timer.tick()
                        $ player.remove_item("handcuffs")
                        $ player.remove_item("cheerleader_outfit")
                        $ sis_final2.finish()
                        $ sister.add_event(sis_shower_cuddle05)
                        label sis_cheerleader_replay:
                            call expression game.dialog_select("jenny_dialogue_cam_show_have_items") from _call_expression_692
                        $ anim_toggle = False
                        $ xray = False
                        jump expression game.dialog_select("sis_cheerleader_fuck_looprep")

                "Need toys?" if sister.over(sis_shower_cuddle05) and not sister.completed(sis_webcam04):
                    if not sister.known(sis_webcam04):
                        call expression game.dialog_select("jenny_dialogue_need_toys") from _call_expression_693
                        $ sister.add_event(sis_webcam04)

                    elif not player.has_item("badmonster"):
                        call expression game.dialog_select("jenny_dialogue_need_toys_do_not_have_toys") from _call_expression_694

                    elif player.has_item("badmonster"):
                        call expression game.dialog_select("jenny_dialogue_need_toys_have_toys") from _call_expression_695
                        $ player.remove_item("badmonster")
                        $ sis_webcam04.finish()

                "Watch TV tonight." if sister.over(sis_final2) and not sis_watch_tv_tonight:
                    call expression game.dialog_select("jenny_dialogue_watch_tv_tonight") from _call_expression_696
                    $ sis_watch_tv_tonight = True
                    jump expression game.dialog_select("sis_bedroom_menu")

                "Watch the neighbors." if sister.over(sis_final2):
                    $ game.timer.tick()
                    call expression game.dialog_select("jenny_dialogue_watch_neighbours") from _call_expression_697
                    call expression game.dialog_select("jenny_dialogue_watch_neighbours_continue01") from _call_expression_698
                    label neighbors_spy_replay:
                        call expression game.dialog_select("jenny_dialogue_watch_neighbours_continue02") from _call_expression_699
                    $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
                    $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["03_unlocked"] = True
                    call expression game.dialog_select("jenny_dialogue_watch_neighbours_continue03") from _call_expression_700
                    $ anim_toggle = False
                    $ xray = False
                    call expression game.dialog_select("jenny_dialogue_watch_neighbours_menu") from _call_expression_701
                    jump expression game.dialog_select("bedroom_dialogue")
    hide player
    hide jenny
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
