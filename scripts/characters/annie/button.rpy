label annie_button_dialogue:
    if player.location == L_school_musicclassroom:
        scene music_classroom_c
    else:
        scene location_school_second_closeup
    show player 13 at left
    show annie 1 at right
    with dissolve

    if player.location == L_school_musicclassroom:
        call expression game.dialog_select("annie_dialogue_music_classroom_intro") from _call_expression_738
        $ game.main()

    menu:
        "Model." if M_ross.is_state(S_ross_ask_model):
            call expression game.dialog_select("annie_dialogue_ross_ask_model") from _call_expression_739
        "Hi!":

            call expression game.dialog_select("annie_dialogue_leave") from _call_expression_740
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
