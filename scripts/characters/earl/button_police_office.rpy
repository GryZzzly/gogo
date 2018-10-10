label police_earl_dialogue:
    scene police_c_1
    if M_roxxy.is_state(S_roxxy_ask_earl_release):
        call expression game.dialog_select("earl_police_office_dialogue_roxxy_ask_earl_release") from _call_expression_1629
        $ M_roxxy.trigger(T_roxxy_talk_to_crystal)

    elif police_earl_first_visit:
        call expression game.dialog_select("earl_police_office_dialogue_first_visit") from _call_expression_1630
        $ police_earl_first_visit = False
    else:

        call expression game.dialog_select("earl_police_office_dialogue_pre") from _call_expression_1631
        menu:
            "Donuts." if M_mia.is_state(S_mia_impress_harold):
                $ harold_glaze = M_harold.get("glaze")
                call expression game.dialog_select("earl_police_office_dialogue_donuts") from _call_expression_1632
                $ del harold_glaze

            "{b}Harold{/b}." if M_mia.is_state(S_mia_clues):
                call expression game.dialog_select("earl_police_office_dialogue_harold") from _call_expression_1633
                $ M_mia.set("questioned earl", True)
                jump police_office_dialogue

            "{b}Roxxy's mom{/b}." if M_roxxy.get("trailer foreclosed"):
                call expression game.dialog_select("earl_police_office_dialogue_roxxys_mom") from _call_expression_1634
            "Nothing.":

                call expression game.dialog_select("earl_police_office_dialogue_leave") from _call_expression_1635

    hide earl
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
