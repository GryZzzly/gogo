label police_harold_dialogue:
    scene police_c_2
    if M_mia.is_set("mia route"):
        call expression game.dialog_select("harold_police_office_dialogue_mia_route") from _call_expression_297

    elif M_helen.is_state([S_helen_route_split, S_helen_mia_breakdown]):
        call expression game.dialog_select("harold_police_office_dialogue_helen_route_split") from _call_expression_298
        $ M_helen.trigger(T_harold_new_girl)

    elif M_mia.is_state(S_mia_harold_backup):
        call expression game.dialog_select("harold_police_office_dialogue_mia_harold_backup") from _call_expression_299
        $ M_mia.trigger(T_harold_grows_a_pair)

    elif M_mia.is_state(S_mia_harolds_thoughts):
        call expression game.dialog_select("harold_police_office_dialogue_mia_harolds_thoughts") from _call_expression_300
        $ M_mia.trigger(T_harold_indecisiveness)

    elif M_roxxy.is_state(S_roxxy_ask_earl_release) and not M_roxxy.get("talked to harold"):
        call expression game.dialog_select("harold_police_office_dialogue_roxxy_ask_earl_release") from _call_expression_301
        $ M_roxxy.set("talked to harold", True)
    else:

        call expression game.dialog_select("harold_police_office_dialogue_pre") from _call_expression_302
        menu:
            "Where's {b}Mia{/b}?":
                call expression game.dialog_select("harold_police_office_dialogue_wheres_mia") from _call_expression_303

            "The chief." if M_roxxy.is_state(S_roxxy_ask_earl_release):
                call expression game.dialog_select("harold_police_office_dialogue_the_chief") from _call_expression_304

            "{b}Larry{/b}." if M_mia.is_state(S_mia_stolen_goods) and erik.over(erik_thief):
                call expression game.dialog_select("harold_police_office_dialogue_larry") from _call_expression_305

            "Thief." if M_mia.is_state(S_mia_stolen_goods) and not erik.over(erik_thief):
                call expression game.dialog_select("harold_police_office_dialogue_thief") from _call_expression_306

            "Donuts." if M_mia.is_state(S_mia_impress_harold) and not player.has_item("donuts_correct") and not player.has_item("donuts_fail"):
                call expression game.dialog_select("harold_police_office_dialogue_donuts") from _call_expression_307

            "Donuts." if M_mia.is_state(S_mia_impress_harold) and player.has_item("donuts_fail"):
                call expression game.dialog_select("harold_police_office_dialogue_donuts_wrong") from _call_expression_308
                $ player.remove_item("donuts_fail")

            "Donuts." if M_mia.is_state(S_mia_impress_harold) and player.has_item("donuts_correct"):
                $ harold_glaze = M_harold.get("glaze")
                $ harold_topping = M_harold.get("topping")
                call expression game.dialog_select("harold_police_office_dialogue_donuts_correct") from _call_expression_309
                $ del harold_glaze
                $ del harold_topping
                $ A_donuts.unlock()
                $ player.remove_item("donuts_correct")
                $ M_mia.trigger(T_harold_donuts)

    hide player
    hide harold
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
