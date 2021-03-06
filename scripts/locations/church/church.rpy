label church_dialogue:
    $ player.go_to(L_church)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 3.9>audio/ambience_church.ogg"):
            $ playSound("<loop 3.9>audio/ambience_church.ogg")

    if L_church.first_visit and not (game.timer.is_weekend() and game.timer.is_morning()):
        call expression game.dialog_select("church_first_visit") from _call_expression_651
        $ L_church.visited()

    if M_mia.is_state(S_mia_church_plan) and game.timer.is_weekend() and game.timer.is_morning():
        call expression game.dialog_select("church_mia_church_plan") from _call_expression_652

    elif M_mia.is_state(S_mia_convince_helen):
        call expression game.dialog_select("church_mia_convince_helen") from _call_expression_653
        $ M_mia.trigger(T_helen_confessional)

    elif M_mia.is_state(S_mia_return_priest_outfit):
        call expression game.dialog_select("church_mia_return_priest_outfit") from _call_expression_654

    elif M_mia.is_state(S_mia_nun_thoughts):
        call expression game.dialog_select("church_mia_nun_thoughts") from _call_expression_655

        $ M_mia.trigger(T_mc_nun_thoughts)

    elif M_mia.is_state(S_mia_church_night_visit) and game.timer.is_dark():
        call expression game.dialog_select("church_mia_church_night_visit") from _call_expression_656
    $ game.main()

label church_front_dialogue:
    $ player.go_to(L_church_front)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
