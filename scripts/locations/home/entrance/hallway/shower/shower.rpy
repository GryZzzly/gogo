label shower_dialogue:
    $ player.go_to(L_home_shower)
    if game.timer.is_dark():
        $ game.main()


    if M_mom.is_state(S_mom_sis_check):
        call expression game.dialog_select("shower_mom_sis_check") from _call_expression_813
        $ M_mom.trigger(T_mom_sis_order)
        jump hallway_dialogue

    elif M_mom.is_state(S_mom_close_valve):
        call expression game.dialog_select("shower_mom_close_valve") from _call_expression_814
        jump hallway_dialogue

    elif M_mom.is_state(S_mom_pipe_check):
        call expression game.dialog_select("shower_mom_pipe_check") from _call_expression_815
        $ M_mom.trigger(T_mom_get_wrench)
        jump hallway_dialogue

    elif M_mom.is_state(S_mom_fix_pipe) and not player.has_item("wrench"):
        call expression game.dialog_select("shower_mom_fix_pipe_no_wrench") from _call_expression_816
        jump hallway_dialogue

    elif M_mom.is_state(S_mom_fix_pipe) and player.has_item("wrench"):
        call expression game.dialog_select("shower_mom_fix_pipe_wrench") from _call_expression_817
        $ player.remove_item("wrench")
        $ M_mom.trigger(T_mom_fixed_broken_pipe)
        jump hallway_dialogue

    elif player.location.is_here(M_jenny):
        $ playSound("<loop 1>audio/ambience_shower_room.ogg")
        jump sis_shower

    elif player.location.is_here(M_mom):
        $ playSound("<loop 1>audio/ambience_shower_room.ogg")
        jump mom_shower
    else:

        scene shower1
        player_name "( There's no one in here. )"
    $ game.main()

label mom_shower:
    if M_mom.is_state(S_mom_shower_peek_after):
        call expression game.dialog_select("shower_mom_shower_peek_after") from _call_expression_818
        $ player.go_to(L_home_hallway)
        $ game.main()

    scene shower06a
    if M_mom.is_state(S_mom_shower_peek):
        call expression game.dialog_select("shower_mom_shower_peek") from _call_expression_819
        $ M_mom.trigger(T_mom_shower_admire)

    elif M_mom.is_state(S_mom_shower_walk_in):
        call expression game.dialog_select("shower_mom_walk_in") from _call_expression_820
        menu:
            "Go inside.":
                call expression game.dialog_select("shower_mom_walk_in_yes") from _call_expression_821
                $ M_mom.trigger(T_mom_shower_admire)
                $ game.timer.tick()
                $ playSound()
            "Leave.":

                call expression game.dialog_select("shower_mom_walk_in_no") from _call_expression_822

    elif M_mom.get("shower sex available"):
        label shower_mom_sex_replay:
            call expression game.dialog_select("shower_mom_sex") from _call_expression_823
        if not store._in_replay == None:
            $ M_mom.set("sex available", True)
            call expression game.dialog_select("shower_mom_sex_walk_in_pre") from _call_expression_824
            jump expression game.dialog_select("mom_shower_question")
        menu:
            "Walk inside":
                $ playSound("<loop 0.5>audio/ambience_shower_interior.ogg")
                call expression game.dialog_select("shower_mom_sex_walk_in_pre") from _call_expression_825
                label mom_shower_question:
                    $ M_mom.set("shower fingered", False)
                call expression game.dialog_select("shower_mom_sex_walk_in_after") from _call_expression_826
                menu:
                    "Wash [deb_name].":
                        call expression game.dialog_select("shower_mom_sex_wash") from _call_expression_827
                        menu shower_mom_sex_wash_menu:
                            "Handjob.":
                                call expression game.dialog_select("shower_mom_sex_wash_handjob") from _call_expression_828
                                jump expression game.dialog_select("mom_shower_end")

                            "Finger {b}[deb_name]{/b}." if M_mom.is_set("sex available") and not M_mom.is_set("shower fingered"):
                                call expression game.dialog_select("shower_mom_sex_finger") from _call_expression_829
                                $ M_mom.set("shower fingered", True)
                                jump expression game.dialog_select("shower_mom_sex_wash_menu")

                            "Blowjob." if M_mom.is_set("sex available"):
                                call expression game.dialog_select("shower_mom_sex_blowjob") from _call_expression_830
                                menu shower_mom_sex_blowjob_menu:
                                    "Keep going":
                                        call expression game.dialog_select("shower_mom_sex_blowjob_loop") from _call_expression_831
                                        jump expression game.dialog_select("shower_mom_sex_blowjob_menu")
                                    "Cum in mouth":

                                        call expression game.dialog_select("shower_mom_sex_blowjob_cum_in_mouth") from _call_expression_832
                                        jump expression game.dialog_select("mom_shower_end")
                                    "Cum on face":

                                        call expression game.dialog_select("shower_mom_sex_blowjob_cum_on_face") from _call_expression_833
                                        jump expression game.dialog_select("mom_shower_end")

                            "Sex." if M_mom.is_set("sex available"):
                                if M_mom.is_set("shower fingered"):
                                    call expression game.dialog_select("shower_mom_sex_already_fingered") from _call_expression_834
                                    call expression game.dialog_select("shower_mom_sex_wash_handjob") from _call_expression_835
                                    jump expression game.dialog_select("mom_shower_end")
                                else:

                                    jump expression game.dialog_select("mom_shower_sex")
                            "Leave":

                                jump expression game.dialog_select("mom_shower_end")

                    "Sex." if M_mom.is_set("sex available"):
                        label mom_shower_sex:
                            $ M_mom.set("sex speed", .4)
                            $ anim_toggle = False
                            $ xray = False
                            $ cum = False
                        call expression game.dialog_select("shower_mom_sex_fuck_pre") from _call_expression_836
                        jump expression game.dialog_select("mom_shower_sex_loop")
            "Leave":

                call expression game.dialog_select("shower_mom_sex_leave") from _call_expression_837
    else:
        call expression game.dialog_select("shower_mom_shower_peek") from _call_expression_838
        $ player.go_to(L_home_hallway)
        $ game.main()
    hide debbie_shower
    hide debbie
    hide debbies
    hide player
    with dissolve
    $ player.go_to(L_home_hallway)
    $ game.main()

label sis_shower:
    call expression game.dialog_select("shower_sis_sex_pre") from _call_expression_839
    menu:
        "Peep." if sister.known(sis_shower_cuddle01):
            if sister.over(sis_shower_cuddle01):
                call expression game.dialog_select("shower_sis_sex_peep_after_cuddle") from _call_expression_840
            else:

                call expression game.dialog_select("shower_sis_sex_peep_before_cuddle") from _call_expression_841
                $ sis_shower_cuddle01.finish()

        "Go inside." if sister.known(sis_shower_cuddle02):
            $ playSound("<loop 0.5>audio/ambience_shower_interior.ogg")
            call expression game.dialog_select("shower_sis_sex_go_inside") from _call_expression_842
            jump expression game.dialog_select("shower_sis_sex_intro")
        "Leave.":

            call expression game.dialog_select("shower_sis_sex_leave") from _call_expression_843
    jump expression game.dialog_select("hallway_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
