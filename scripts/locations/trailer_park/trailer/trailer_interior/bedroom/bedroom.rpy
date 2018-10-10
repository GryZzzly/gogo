label trailer_bedroom_dialogue:
    $ player.go_to(L_trailer_bedroom)
    if M_roxxy.is_state(S_roxxy_wait_in_her_room):
        call expression game.dialog_select("trailer_bedroom_roxxy_get_uniform_on_doggo_intro") from _call_expression_1082
        if M_roxxy.get("lost shooting"):
            call expression game.dialog_select("trailer_bedroom_roxxy_wait_in_her_room_lost_shooting") from _call_expression_1083
        else:

            call expression game.dialog_select("trailer_bedroom_roxxy_wait_in_her_room_won_shooting") from _call_expression_1084
        $ M_roxxy.trigger(T_roxxy_has_uniform)

        $ player.go_to(L_map)

    elif M_roxxy.is_state(S_roxxy_picnic_done):
        call expression game.dialog_select("trailer_bedroom_roxxy_go_to_picnic") from _call_expression_1085
        $ M_roxxy.trigger(T_roxxy_kissed)

        $ game.timer.tick()
        $ player.go_to(L_map)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
