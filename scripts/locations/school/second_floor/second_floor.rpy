label stairs_dialogue:
    $ player.go_to(L_school_floor2)
    call pa_announcement from _call_pa_announcement_5
    if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg") and not game.timer.is_dark():
        $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)

    if stairs_dialogue_count == 0:
        call expression game.dialog_select("second_floor_first_visit") from _call_expression_637
        $ stairs_dialogue_count = 1

    elif M_okita.is_state(S_okita_dose_smith):
        call expression game.dialog_select("second_floor_okita_dose_smith") from _call_expression_638
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
