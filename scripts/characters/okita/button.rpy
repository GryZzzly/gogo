label okita_button_dialogue:
    scene expression "backgrounds/location_school_science_closeup.jpg"
    if M_okita.is_state(S_okita_intro):
        call expression game.dialog_select("button_okita_intro") from _call_expression_1324
        $ M_okita.trigger(T_okita_get_keycode)

    elif M_okita.is_state(S_okita_get_keycode):
        call expression game.dialog_select("button_okita_get_keycode") from _call_expression_1325

    elif M_okita.is_state(S_okita_foam_misshap):
        call expression game.dialog_select("button_okita_foam_misshap") from _call_expression_1326
        $ M_okita.trigger(T_okita_get_bifocal_lenses)

    elif M_okita.is_state(S_okita_get_bifocal_lenses):
        call expression game.dialog_select("button_okita_get_bifocal_lenses") from _call_expression_1327

    elif M_okita.is_state(S_okita_picture_taken) and player.has_item("judith_glasses"):
        call expression game.dialog_select("science_classroom_okita_has_glasses") from _call_expression_1328
        if M_okita.is_set("glasses assembly fail"):
            menu:
                "Try again":
                    call expression game.dialog_select("science_classroom_okita_has_glasses_try_again") from _call_expression_1329
                "Nothing.":

                    $ game.main()

        if player.has_required_int(5):
            call expression game.dialog_select("science_classroom_okita_has_glasses_int_pass") from _call_expression_1330
            $ M_okita.set("glasses assembly fail", False)
            $ player.remove_item("judith_glasses")

            $ M_okita.trigger(T_okita_xray_perved_classroom)
        else:

            call expression game.dialog_select("science_classroom_okita_has_glasses_int_fail") from _call_expression_1331
            $ M_okita.set("glasses assembly fail", True)
            $ player.go_to(L_map)
            $ game.timer.tick(2)
            $ game.main()

    elif M_okita.is_state(S_okita_glasses_completed):
        call expression game.dialog_select("button_okita_get_faptic_engine") from _call_expression_1332
        $ M_okita.trigger(T_okita_requested_faptic_engine)

    elif M_okita.is_state(S_okita_faptic_engine):
        call expression game.dialog_select("button_okita_get_faptic_engine_repeat") from _call_expression_1333

    elif M_okita.is_state(S_okita_get_controller) and player.has_item("faptic_engine"):
        call expression game.dialog_select("science_classroom_okita_has_faptic") from _call_expression_1334
        if M_okita.is_set("belt assembly fail"):
            menu:
                "Try again":
                    call expression game.dialog_select("science_classroom_okita_has_faptic_try_again") from _call_expression_1335
                "Nothing.":

                    $ game.main()

        if player.has_required_int(8):
            scene expression "backgrounds/location_school_science_cutscene04.jpg"
            pause
            call expression game.dialog_select("science_classroom_okita_has_faptic_int_pass") from _call_expression_1336
            $ M_okita.set("belt assembly fail", False)

            $ player.remove_item("faptic_engine")
            $ M_okita.trigger(T_okita_belt_assembled)
        else:

            scene expression "backgrounds/location_school_science_cutscene04b.jpg"
            pause
            call expression game.dialog_select("science_classroom_okita_has_faptic_int_fail") from _call_expression_1337
            $ M_okita.set("belt assembly fail", True)
            $ player.go_to(L_map)
            $ game.timer.tick(2)
            $ game.main()

    elif M_okita.is_state(S_okita_tinkering_with_belt, S_okita_tinkering_with_belt_delay, S_okita_tinkering_with_belt_delay2):
        call expression game.dialog_select("button_okita_tinkering_belt") from _call_expression_1338

    elif M_okita.is_state(S_okita_tinkering_with_belt_delay3):
        call expression game.dialog_select("button_okita_tinkered_belt") from _call_expression_1339
        $ M_okita.trigger(T_okita_finished_tinkering_belt)
        $ game.timer.tick()
        $ player.go_to(L_school_floor3)
        $ game.main()

    elif M_okita.is_state(S_okita_tired_from_belt):
        call expression game.dialog_select("button_okita_tired_from_belt") from _call_expression_1340
        $ M_okita.trigger(T_okita_get_ingredients)

    elif M_okita.is_state(S_okita_get_ingredients):
        if player.has_item("mushroom") and player.has_item("toad") and player.has_item("caveflower") and player.has_item("chicken_stock") and player.has_item("tissue"):
            call expression game.dialog_select("button_okita_got_all_ingredients") from _call_expression_1341
            $ M_okita.trigger(T_okita_got_all_ingredients)
        else:

            scene location_school_science_closeup
            show player 11 at left
            show okita 2 at right
            player_name "About those items you needed..."
            menu okita_items:
                "Mushroom" if not player.has_item("mushroom"):
                    call expression game.dialog_select("button_okita_ingredients_mushroom") from _call_expression_1342

                "Horny Toad" if not player.has_item("toad"):
                    call expression game.dialog_select("button_okita_ingredients_toad") from _call_expression_1343

                "Flower" if not player.has_item("caveflower"):
                    call expression game.dialog_select("button_okita_ingredients_flower") from _call_expression_1344

                "Base Liquid" if not player.has_item("chicken_stock"):
                    call expression game.dialog_select("button_okita_ingredients_stock") from _call_expression_1345

                "Smith DNA" if not player.has_item("tissue"):
                    call expression game.dialog_select("button_okita_ingredients_tissue") from _call_expression_1346
                "That's all.":

                    player_name "I'll get back to collecting those items then."
                    $ game.main()
            jump expression game.dialog_select("okita_items")

    elif M_okita.is_state(S_okita_extract_cum):
        call expression game.dialog_select("button_okita_extract_cum") from _call_expression_1347

    elif M_okita.is_state(S_okita_dose_smith):
        call expression game.dialog_select("button_okita_dose_smith") from _call_expression_1348

    elif M_okita.is_state(S_okita_wait_for_smith_serum):
        call expression game.dialog_select("button_okita_wait_for_smith_serum") from _call_expression_1349
        $ game.timer.tick(2)
        $ M_okita.trigger(T_okita_smith_effects_seen)

    elif M_okita.is_state(S_okita_wait_for_okita_serum, S_okita_wait_for_okita_serum_delay, S_okita_wait_for_okita_serum_delay2):
        call expression game.dialog_select("button_okita_wait_for_okita_serum") from _call_expression_1350

    elif M_okita.is_state(S_okita_wait_for_okita_serum_delay3):
        call expression game.dialog_select("button_okita_serum_effects") from _call_expression_1351
        $ M_okita.trigger(T_okita_serum_took_effect)

    elif M_okita.get("Q3 completed"):
        call expression game.dialog_select("button_okita_generic_after_q3") from _call_expression_1352

    elif not M_okita.get("Q3 completed"):
        call expression game.dialog_select("button_okita_generic_before_q3") from _call_expression_1353
    hide player
    hide okita
    hide principal
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
