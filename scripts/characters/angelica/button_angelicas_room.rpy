label angelicas_room_dialogue:
    if M_helen.is_set("helen route"):
        call expression game.dialog_select("angelicas_room_dialogue_helen_route_pre") from _call_expression_2098
        menu angelicas_room_dialogue_helen_route_options:
            "Spanking.":
                call expression game.dialog_select("angelicas_room_dialogue_helen_route_spanking") from _call_expression_2099
                jump expression game.dialog_select("sacrament_complete")
            "Holy Seed.":

                call expression game.dialog_select("angelicas_room_dialogue_helen_route_holy_seed") from _call_expression_2100
                jump expression game.dialog_select("helen_mc_churchsex")
            "Spread {b}Helen{/b}.":

                call expression game.dialog_select("angelicas_room_dialogue_helen_route_spread_helen") from _call_expression_2101
                jump expression game.dialog_select("sacrament_complete")
            "Have you sinned?":

                show popup_unfinished at truecenter with dissolve
                pause
                hide popup_unfinished with dissolve
                jump expression game.dialog_select("angelicas_room_dialogue_helen_route_options")
            "Nothing.":

                call expression game.dialog_select("angelicas_room_dialogue_helen_route_leave") from _call_expression_2102

    elif M_mia.is_set("mia route"):
        call expression game.dialog_select("angelicas_room_dialogue_mia_route") from _call_expression_2103

    elif M_mia.is_state(S_mia_harolds_thoughts):
        call expression game.dialog_select("angelicas_room_dialogue_mia_harolds_thoughts") from _call_expression_2104

    elif M_mia.is_state(S_mia_find_sinners):
        call expression game.dialog_select("angelicas_room_dialogue_mia_find_sinners_pre") from _call_expression_2105
        menu:
            "Find sinners.":
                call expression game.dialog_select("angelicas_room_dialogue_mia_find_sinners") from _call_expression_2106

    elif M_mia.is_state(S_mia_angelicas_whip):
        call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_whip_pre") from _call_expression_2107
        menu:
            "The Whip.":
                if player.has_item("whip"):
                    $ player.remove_item("whip")
                    jump expression game.dialog_select("helen_sacrement_training_part2")
                call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_whip") from _call_expression_2108
            "Nothing.":

                call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_whip_leave") from _call_expression_2109
    else:

        if M_mia.is_state([S_mia_harolds_thoughts, S_mia_angelicas_final_request]):
            call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_final_request_pre") from _call_expression_2110
        else:
            call expression game.dialog_select("angelicas_room_dialogue_default_pre") from _call_expression_2111
            $ player.go_to_previous()
            $ game.main()
        menu:
            "Strap on." if M_mia.is_state([S_mia_harolds_thoughts, S_mia_angelicas_final_request]) and not player.has_item("strapon"):
                call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_final_request_strap_on") from _call_expression_2112

            "Nothing." if M_mia.is_state([S_mia_harolds_thoughts, S_mia_angelicas_final_request]):
                call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_final_request_leave") from _call_expression_2113

            "Nothing." if not M_mia.is_state([S_mia_harolds_thoughts, S_mia_angelicas_final_request]):
                call expression game.dialog_select("angelicas_room_dialogue_default_leave") from _call_expression_2114
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
