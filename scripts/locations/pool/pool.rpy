label pool_dialogue:
    $ player.go_to(L_pool)
    $ used_changing_girls = []
    if M_cassie.is_state(S_cassie_ban_from_pool):
        if not game.timer.is_dark():
            call expression game.dialog_select("pool_banned_from_pool_day") from _call_expression_388
        else:

            call expression game.dialog_select("pool_banned_from_pool_night") from _call_expression_389
            call expression game.dialog_select("pool_banned_from_pool_night_swim") from _call_expression_390
            $ M_cassie.trigger(T_cassie_lift_ban)
        $ player.go_to(L_map)

    elif not game.timer.is_dark():
        if M_cassie.is_state(S_cassie_medic_room):
            call expression game.dialog_select("pool_cassie_after_fun") from _call_expression_391
            $ M_cassie.trigger(T_cassie_end)
    else:

        call expression game.dialog_select("pool_closed_night") from _call_expression_392
    $ game.main()

label medic_room_dialogue:
    scene changeroom02
    if M_cassie.is_state(S_cassie_medic_room) and not M_cassie.get("had sex"):
        label medic_room_cassie_replay:
            if not store._in_replay is None:
                scene changeroom02
            call expression game.dialog_select("medic_room_dialogue_count_0") from _call_expression_393
        menu:
            "Ok, let's try it.":
                call expression game.dialog_select("medic_room_dialogue_count_0_lets_try") from _call_expression_394
                $ M_cassie.set("had sex", True)
                jump expression game.dialog_select("gloryhole_medic")

            "I don't feel like it." if store._in_replay is None:
                call expression game.dialog_select("medic_room_dialogue_count_0_do_not_feel_like_it") from _call_expression_395

    elif M_cassie.is_state(S_cassie_medic_room) and M_cassie.get("had sex"):
        call expression game.dialog_select("medic_room_dialogue_count_1") from _call_expression_396
        $ renpy.end_replay()
        $ persistent.cookie_jar["Cassie"]["unlocked"] = True
        $ persistent.cookie_jar["Cassie"]["gallery"]["01_unlocked"] = True
        show unlock19 at truecenter with dissolve
        pause
        hide unlock19 with dissolve

    elif M_cassie.is_state(S_cassie_end) and not M_cassie.get("had sex"):
        call expression game.dialog_select("medic_room_dialogue_count_2") from _call_expression_397
        menu:
            "I'd love to.":
                call expression game.dialog_select("medic_room_dialogue_count_2_love_to") from _call_expression_398
                $ M_cassie.set("had sex", True)
                jump expression game.dialog_select("gloryhole_medic")
            "Just changing.":

                call expression game.dialog_select("medic_room_dialogue_count_2_just_changing") from _call_expression_399
                if wearing_swimsuit:
                    $ wearing_swimsuit = False
                    $ changing_count = 0
                else:

                    $ wearing_swimsuit = True
                $ used_changing_girls = []
    else:

        call expression game.dialog_select("medic_room_dialogue_count_finished") from _call_expression_400
        $ M_cassie.set("had sex", False)
    jump expression game.dialog_select("pool_dialogue")

label poolrules_dialogue:
    scene pool
    if M_cassie.is_state(S_cassie_start):
        if not player.has_item("swimsuit"):
            call expression game.dialog_select("poolrules01_dialogue_pre") from _call_expression_401
            call expression game.dialog_select("poolrules01_dialogue_after") from _call_expression_402
            $ game.main()
        else:
            call expression game.dialog_select("poolrules02_dialogue") from _call_expression_403

    elif M_cassie.is_state(S_cassie_caught_skinny_dipping):
        call expression game.dialog_select("pool_cutscene01_dialogue") from _call_expression_404
        call expression game.dialog_select("pool_rescued_dialogue") from _call_expression_405
        $ M_cassie.trigger(T_cassie_drowning)
        $ M_player.set("first swim", False)
        jump expression game.dialog_select("medic_room_dialogue")
    else:

        if M_player.get("first swim"):
            call expression game.dialog_select("pool_cutscene01") from _call_expression_406
            call expression game.dialog_select("pool_rescued_dialogue") from _call_expression_407
            $ M_cassie.trigger(T_cassie_drowning)
            jump expression game.dialog_select("medic_room_dialogue")
        else:

            call expression game.dialog_select("pool_cutscene02") from _call_expression_408
            $ changing_count = 0
            if not ronda_after_swimming:
                call expression game.dialog_select("ronda_after_swimming") from _call_expression_409
                $ ronda_after_swimming = True
            else:

                jump expression game.dialog_select("pool_dialogue")

    hide player
    hide cassie
    with dissolve
    $ game.main()

label changing_dialogue:
    $ rand_girl = renpy.random.choice(changing_girls)
    scene changeroom01
    if wearing_swimsuit:
        call expression game.dialog_select("changing_dialogue_wearing_swimsuit") from _call_expression_410

    elif changing_count == 0:
        call expression game.dialog_select("changing_dialogue_occupied_pre") from _call_expression_411
        $ used_changing_girls.append(rand_girl)
        call expression game.dialog_select("changing_dialogue_occupied_after") from _call_expression_412
        $ changing_count = 1

    elif changing_count == 1:
        call expression game.dialog_select("changing_dialogue_occupied_pre") from _call_expression_413
        $ used_changing_girls.append(rand_girl)
        call expression game.dialog_select("changing_dialogue_occupied_after") from _call_expression_414
        $ changing_count = 2
        if M_cassie.is_state(S_cassie_start):
            $ M_cassie.trigger(T_cassie_ban_mc)
            call expression game.dialog_select("changing_caught") from _call_expression_415
            $ player.go_to(L_map)
            $ used_changing_girls = []
            $ game.main()

    elif changing_count == 2:
        call expression game.dialog_select("changing_dialogue_change") from _call_expression_416
        $ wearing_swimsuit = True
        $ changing_count = 3
        $ used_changing_girls = []
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
