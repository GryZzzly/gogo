label anna_yoga_button_dialogue:
    call expression game.dialog_select("anna_button_yoga_room_dialogue_pre") from _call_expression_731
    menu:
        "Where's {b}Mrs. Johnson{/b}?":
            call expression game.dialog_select("anna_button_yoga_room_dialogue_wheres_mrsj") from _call_expression_732

        "Yoga" if mrsj.completed(mrsj_yoga_help):
            call expression game.dialog_select("anna_button_yoga_room_dialogue_yoga") from _call_expression_733
            $ yoga_position = ""
            $ yoga_stage = 1
            $ boner_fail = False
            $ game.timer.tick()
            jump expression game.dialog_select("yoga_room_class")

    hide player
    hide anna
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
