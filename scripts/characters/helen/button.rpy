label helen_button_dialogue:
    if M_helen.is_state(S_helen_master_servant_fun):
        jump expression game.dialog_select("helen_bedroom_sex")

    scene expression game.timer.image("mia_house_helen_c{}")
    if M_mia.is_set("mia route"):
        call expression game.dialog_select("helen_dialogue_mia_route") from _call_expression_1953

    elif M_helen.is_state(S_helen_end):
        call expression game.dialog_select("helen_dialogue_helen_end_intro") from _call_expression_1954
        menu:
            "Purify your body.":
                call expression game.dialog_select("helen_dialogue_helen_end_sex") from _call_expression_1955
                $ M_helen.set("sex speed", .175)
                jump expression game.dialog_select("helen_bedroom_sex_start")
            "Another time.":

                call expression game.dialog_select("helen_dialogue_helen_end_leave") from _call_expression_1956

    elif M_mia.is_set("helen dialogue change"):
        call expression game.dialog_select("helen_dialogue_change_intro") from _call_expression_1957
        menu:
            "{b}Harold{/b}." if not M_mia.is_state(S_mia_clues):
                call expression game.dialog_select("helen_dialogue_change_harold") from _call_expression_1958

            "{b}Harold{/b}." if M_mia.is_state(S_mia_clues):
                call expression game.dialog_select("helen_dialogue_change_mia_clues") from _call_expression_1959

            "Corset." if M_mia.is_state(S_mia_helen_outfit_request):
                call expression game.dialog_select("helen_dialogue_change_corset") from _call_expression_1960

            "Angelica." if M_mia.is_set('helen angelica training'):
                call expression game.dialog_select("helen_dialogue_change_angelica") from _call_expression_1961

            "Whipping." if M_mia.is_state(S_mia_helen_condition):
                call expression game.dialog_select("helen_dialogue_change_whipping") from _call_expression_1962
                $ M_mia.trigger(T_helen_thanks)

            "Ritual." if M_mia.is_state(S_mia_find_sinners):
                call expression game.dialog_select("helen_dialogue_change_ritual") from _call_expression_1963
                menu:
                    "I don't know." if player.stats.chr() < 5:
                        call expression game.dialog_select("helen_dialogue_change_ritual_stat_fail") from _call_expression_1964

                    "Ancient sacrament." if player.stats.chr() >= 5:
                        call expression game.dialog_select("helen_dialogue_change_ritual_stat_pass") from _call_expression_1965
                        $ M_mia.trigger(T_helen_secret_sacrement)

    elif M_mia.is_set("helen button"):
        call expression game.dialog_select("helen_dialogue_intro") from _call_expression_1966
        menu helen_dialogue:
            "{b}Harold{/b}.":
                call expression game.dialog_select("helen_dialogue_harold") from _call_expression_1967
    else:

        call expression game.dialog_select("helen_dialogue_leave") from _call_expression_1968
    hide player
    hide helen
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
