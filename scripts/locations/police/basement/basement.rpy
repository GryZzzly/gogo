label police_basement_dialogue:
    $ player.go_to(L_police_basement)
    if M_roxxy.is_state(S_roxxy_ask_earl_release):
        call expression game.dialog_select("police_basement_roxxy_ask_earl_release") from _call_expression_1457
        $ player.go_to(L_police_lobby)
        $ game.main()

    elif L_police_basement.first_visit:
        call expression game.dialog_select("police_basement_first_visit") from _call_expression_1458
        $ L_police_basement.visited()

    elif M_mia.is_set("questioned yumi") and M_mia.is_set("questioned earl"):
        call expression game.dialog_select("police_basement_mia_clues_summary") from _call_expression_1459
        $ M_mia.trigger(T_mia_clues_summary)

    elif M_mia.is_state(S_mia_inmate_status):
        call expression game.dialog_select("police_basement_mia_inmate_status") from _call_expression_1460

    elif M_mia.is_state(S_mia_harold_backup):
        call expression game.dialog_select("police_basement_mia_harold_backup") from _call_expression_1461
    $ game.main()

label police_cell_dialogue:
    if M_mia.is_state(S_mia_inmate_status):
        call expression game.dialog_select("police_cell_mia_inmate_status") from _call_expression_1462
        $ M_mia.trigger(T_yumi_backup_request)

    elif M_mia.is_state(S_mia_harold_backup):
        call expression game.dialog_select("police_cell_mia_harold_backup") from _call_expression_1463

    elif M_mia.is_state(S_mia_harold_to_the_rescue):
        call expression game.dialog_select("police_cell_mia_harold_to_the_rescue") from _call_expression_1464

        $ M_mia.trigger(T_harold_backup)
    else:

        call expression game.dialog_select("police_cell_empty") from _call_expression_1465
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
