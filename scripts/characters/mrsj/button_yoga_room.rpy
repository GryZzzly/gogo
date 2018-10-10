label mrsj_yoga_button_dialogue:
    scene expression game.timer.image("yoga_room{}")
    if not mrsj.known(mrsj_yoga_intro):
        call expression game.dialog_select("mrsj_button_yoga_room_dialogue_pre_first") from _call_expression_1648
        $ mrsj.add_event(mrsj_yoga_intro)
        $ mrsj_yoga_intro.finish()
    else:

        call expression game.dialog_select("mrsj_button_yoga_room_dialogue_pre_repeat") from _call_expression_1649
    menu mrsj_button_yoga_room_dialogue_options:
        "How's {b}Erik{/b}?":
            call expression game.dialog_select("mrsj_button_yoga_room_dialogue_hows_erik") from _call_expression_1650
            jump expression game.dialog_select("mrsj_button_yoga_room_dialogue_options")
        "What was that?":

            call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that") from _call_expression_1651
            jump expression game.dialog_select("mrsj_button_yoga_room_dialogue_options")
        "You're so fit!":

            call expression game.dialog_select("mrsj_button_yoga_room_dialogue_youre_so_fit") from _call_expression_1652
            jump expression game.dialog_select("mrsj_button_yoga_room_dialogue_options")
        "I have to go train!":

            call expression game.dialog_select("mrsj_button_yoga_room_dialogue_have_to_train") from _call_expression_1653
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
