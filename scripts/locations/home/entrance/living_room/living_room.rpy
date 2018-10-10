label home_livingroom_dialogue:
    python:
        sis_caught_spying = False
    $ player.go_to(L_home_livingroom)
    if sister.in_progress(sis_couch01) and game.timer.is_evening() and not M_mom.is_state(S_mom_sleepover):
        call expression game.dialog_select("living_room_sis_couch_1_progress") from _call_expression_385
        jump expression game.dialog_select("home_entrance")

    elif sister.started(sis_couch03) and game.timer.is_evening() and (not M_mom.is_state(S_mom_sleepover) or not player.location.is_here(M_mom)):
        call expression game.dialog_select("living_room_sis_couch_3_started") from _call_expression_386
        jump expression game.dialog_select("home_livingroom_tv")

    elif M_mom.is_state(S_mom_spy) and not game.timer.is_dark():
        call expression game.dialog_select("living_room_mom_spy") from _call_expression_387
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
