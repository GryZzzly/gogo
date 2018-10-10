label aqua_dialogue:
    scene location_lair_mount
    if game.timer.is_night():
        $ player.go_to(L_map)
        call expression game.dialog_select("aqua_dialogue_night") from _call_expression_1311
        $ game.main()

    elif M_aqua.is_state(S_aqua_found):
        call expression game.dialog_select("aqua_dialogue_aqua_found") from _call_expression_1312
        $ player.get_item("special_lure")
        $ M_aqua.trigger(T_aqua_friended)
        $ game.main()

    elif M_aqua.is_state(S_aqua_mate):
        jump expression game.dialog_select("aqua_sex")
    else:

        call expression game.dialog_select("aqua_dialogue_pre") from _call_expression_1313
    menu aqua_dialogue_options:
        "The others.":
            call expression game.dialog_select("aqua_dialogue_the_others") from _call_expression_1314
            jump expression game.dialog_select("aqua_dialogue_options")
        "How are you?":

            call expression game.dialog_select("aqua_dialogue_how_are_you") from _call_expression_1315
            jump expression game.dialog_select("aqua_dialogue_options")

        "Mating." if M_aqua.is_state(S_aqua_mating_proposal):
            call expression game.dialog_select("aqua_dialogue_mating_pre") from _call_expression_1316
            menu:
                "Me?" if player.stats.chr() < 7:
                    call expression game.dialog_select("aqua_dialogue_mating_stat_fail") from _call_expression_1317


                "I can help!" if player.stats.chr() >= 7:
                    call expression game.dialog_select("aqua_dialogue_mating_stat_pass") from _call_expression_1318
                    $ M_aqua.trigger(T_aqua_mating_offer)

        "Mating." if M_aqua.is_state(S_aqua_valor_test):
            call expression game.dialog_select("aqua_dialogue_mating_hint") from _call_expression_1319

        "Mate." if M_aqua.is_state([S_aqua_seasucc_intro, S_aqua_seasucc_mushroom, S_aqua_end]):
            call expression game.dialog_select("aqua_dialogue_mate") from _call_expression_1320
            jump expression game.dialog_select("aqua_sex")
        "Nothing.":

            call expression game.dialog_select("aqua_dialogue_nothing") from _call_expression_1321

    hide player
    hide aqua
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
