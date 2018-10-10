label ivy_button_dialogue:
    if M_ivy.is_state(S_ivy_start):
        call expression game.dialog_select("button_ivy_start_intro") from _call_expression_963
        $ M_ivy.trigger(T_ivy_intro)
    else:
        call expression game.dialog_select("button_ivy_end_intro") from _call_expression_964
    menu:
        "Okay." if M_ivy.is_state(S_ivy_start):
            call expression game.dialog_select("button_ivy_massage_first") from _call_expression_965
            call screen pamphlet

        "Massage." if not M_ivy.is_state(S_ivy_start):
            call expression game.dialog_select("button_ivy_massage") from _call_expression_966
            call screen pamphlet

        "Package." if quest13 in quest_list and quest13 not in completed_quests and not player.has_item("package"):
            call expression game.dialog_select("button_ivy_package") from _call_expression_967
            $ player.get_item("package")
        "Just shopping.":

            call expression game.dialog_select("button_ivy_just_shopping") from _call_expression_968

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
