label helens_bedroom:
    $ player.go_to(L_miahouse_helensbedroom)
    if M_mia.is_state(S_mia_midnight_help):
        call expression game.dialog_select("helens_bedroom_mia_midnight_help") from _call_expression_1143

    elif M_mia.is_state(S_mia_helen_talk):
        call expression game.dialog_select("helens_bedroom_mia_helen_talk") from _call_expression_1144
        $ M_mia.trigger(T_mia_helen_deny)

    elif M_mia.is_state(S_mia_unexpected_visit) and game.timer.is_afternoon():
        call expression game.dialog_select("helens_bedroom_mia_unexpected_visit") from _call_expression_1145
        $ M_mia.trigger(T_helen_caught_masturbating)

    elif M_mia.is_state(S_mia_helen_outfit_request) and player.has_item("red_corset") and not game.timer.is_dark():
        call expression game.dialog_select("helens_bedroom_mia_helen_outfit_request") from _call_expression_1146
        $ persistent.cookie_jar["Helen"]["unlocked"] = True
        $ persistent.cookie_jar["Helen"]["gallery"]["01_unlocked"] = True
        $ player.remove_item("red_corset")
        $ M_mia.trigger(T_helen_sexy_lingerie)

    elif M_helen.is_state(S_helen_master_servant_fun):
        call expression game.dialog_select("helens_bedroom_helen_master_servant_fun") from _call_expression_1147
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
