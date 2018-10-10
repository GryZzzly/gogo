label roz_dialogue:
    call expression game.dialog_select("roz_dialogue_intro") from _call_expression_488
    if not Roz.known(roz_intro):
        $ Roz.add_event(roz_intro)
        $ roz_intro.finish()
    menu roz_dialogue_options:
        "1st floor?":
            call expression game.dialog_select("roz_dialogue_1st_floor") from _call_expression_489
            jump expression game.dialog_select("roz_dialogue_options")
        "2nd floor?":

            call expression game.dialog_select("roz_dialogue_2nd_floor") from _call_expression_490
            jump expression game.dialog_select("roz_dialogue_options")
        "Schedule.":

            call expression game.dialog_select("roz_dialogue_schedule") from _call_expression_491
            jump expression game.dialog_select("roz_dialogue_options")

        "Ancestry." if M_aqua.is_state(S_aqua_boatsmith_search) and M_roz.is_state(S_roz_start):
            call expression game.dialog_select("roz_dialogue_ancestory") from _call_expression_492
            $ M_roz.trigger(T_roz_favour)
            $ M_roz.set("fun time", True)

        "Go on break." if M_roz.is_state(S_roz_end) and not M_roz.is_set("fun time"):
            call expression game.dialog_select("roz_dialogue_go_on_break") from _call_expression_493
            $ M_roz.set("fun time", True)
        "Nothing.":

            call expression game.dialog_select("roz_dialogue_nothing") from _call_expression_494

    hide player
    hide roz
    hide roz_desk
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
