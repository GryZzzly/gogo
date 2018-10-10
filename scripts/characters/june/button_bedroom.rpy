label june_bedroom_dialogue:
    $ game.timer.tick()
    $ june_hang_out = False
    if June.in_progress(june_cosplay):
        label june_cosplay_replay:
            call expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_pre") from _call_expression_1845
        call expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_intro") from _call_expression_1846
        $ anim_toggle = False
        $ xray = False
        $ M_june.set("sex speed", .3)
        jump expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_loop")
    else:

        scene bedroom_sex2
        if June.over(june_cosplay):
            call expression game.dialog_select("june_bedroom_dialogue_sex_pre_cosplay") from _call_expression_1847
        else:

            call expression game.dialog_select("june_bedroom_dialogue_sex_pre_no_cosplay") from _call_expression_1848
        menu:
            "Sex!" if June.over(june_cosplay):
                call expression game.dialog_select("june_bedroom_dialogue_sex_normal_pre") from _call_expression_1849
                call expression game.dialog_select("june_bedroom_dialogue_normal_sex_intro") from _call_expression_1850
                $ anim_toggle = False
                $ xray = False
                $ M_june.set("sex speed", .3)
                jump expression game.dialog_select("june_bedroom_dialogue_normal_sex_loop")

            "Cosplay sex!" if June.over(june_cosplay):
                call expression game.dialog_select("june_bedroom_dialogue_sex_cosplay_pre") from _call_expression_1851
                call expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_intro") from _call_expression_1852
                $ anim_toggle = False
                $ xray = False
                $ M_june.set("sex speed", .3)
                jump expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_loop")
            "Play games.":

                if June.over(june_cosplay):
                    call expression game.dialog_select("june_bedroom_dialogue_play_games_cosplay_over") from _call_expression_1853
                else:

                    call expression game.dialog_select("june_bedroom_dialogue_play_games_cosplay_not_over") from _call_expression_1854
                jump expression game.dialog_select("orc_battle_start")
            "I have to sleep.":

                $ tmp_deb_name = deb_name.capitalize()
                call expression game.dialog_select("june_bedroom_dialogue_leave") from _call_expression_1855
                $ del tmp_deb_name
                jump expression game.dialog_select("sleeping")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
