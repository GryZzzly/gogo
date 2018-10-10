label police_yumi_dialogue:
    call expression game.dialog_select("yumi_police_basement_dialogue_pre") from _call_expression_734
    menu:
        "Donuts." if M_mia.is_state(S_mia_impress_harold):
            $ harold_topping = M_harold.get("topping")
            call expression game.dialog_select("yumi_police_basement_dialogue_donuts") from _call_expression_735
            $ del harold_topping

        "{b}Harold{/b}." if M_mia.is_state(S_mia_clues):
            call expression game.dialog_select("yumi_police_basement_dialogue_harold") from _call_expression_736
            $ M_mia.set("questioned yumi", True)
            jump expression game.dialog_select("police_basement_dialogue")
        "Just visiting.":

            call expression game.dialog_select("yumi_police_basement_dialogue_leave") from _call_expression_737

    hide player
    hide yumi
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
