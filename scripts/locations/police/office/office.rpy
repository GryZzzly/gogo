label police_office_dialogue:
    $ player.go_to(L_police_office)
    if L_police_office.first_visit and player.location.is_here(M_harold):
        call expression game.dialog_select("police_office_first_visit_pre") from _call_expression_1104
        menu:
            "Where's {b}Mia{/b}?":
                call expression game.dialog_select("police_office_first_visit_wheres_mia") from _call_expression_1105
                $ L_police_office.visited()

    elif M_mia.is_set("questioned yumi") and M_mia.is_set("questioned earl"):
        call expression game.dialog_select("police_office_mia_clues_summary") from _call_expression_1106
        $ M_mia.trigger(T_mia_clues_summary)

    elif M_mia.is_state(S_mia_harold_gift):
        call expression game.dialog_select("police_office_mia_harold_gift") from _call_expression_1107
        $ player.remove_item("aviators")

        $ M_mia.trigger(T_harold_glasses)

    elif M_mia.is_state(S_mia_convince_harold):
        call expression game.dialog_select("police_office_mia_convince_harold_pre") from _call_expression_1108
        if erik.over(erik_thief):
            call expression game.dialog_select("police_office_mia_convince_harold_pre_erik_thief") from _call_expression_1109
        else:

            call expression game.dialog_select("police_office_mia_convince_harold_pre_no_erik_thief") from _call_expression_1110

        call expression game.dialog_select("police_office_mia_convince_harold_mid") from _call_expression_1111
        if erik.over(erik_thief):
            call expression game.dialog_select("police_office_mia_convince_harold_mid_erik_thief") from _call_expression_1112
        else:

            call expression game.dialog_select("police_office_mia_convince_harold_mid_no_erik_thief") from _call_expression_1113

        call expression game.dialog_select("police_office_mia_convince_harold_after") from _call_expression_1114
        $ M_mia.trigger(T_harold_find_goods)

    elif M_mia.is_state(S_mia_return_goods):
        call expression game.dialog_select("police_office_mia_return_goods_pre") from _call_expression_1115
        if erik.over(erik_thief):
            call expression game.dialog_select("police_office_mia_return_goods_pre_erik_thief") from _call_expression_1116
        else:

            call expression game.dialog_select("police_office_mia_return_goods_pre_no_erik_thief") from _call_expression_1117

        call expression game.dialog_select("police_office_mia_return_goods_after") from _call_expression_1118
        $ M_mia.trigger(T_harold_promotion)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
