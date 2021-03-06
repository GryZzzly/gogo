label shed:
    $ player.go_to(L_diane_shed)
    if aunt_had_sex:
        if game.timer.is_dark():
            if quest12 in completed_quests and quest13 not in quest_list and aunt.started(aunt_breeding_help):
                call expression game.dialog_select("dianes_shed_diane_breeding_help_started") from _call_expression_146
                $ quest_list.append(quest13)
                $ aunt_breeding_help.status = True
    else:

        scene expression game.timer.image("shed{}")
        if not player.has_item("pump") and quest08 not in completed_quests:
            show pump_object at Position(xpos = 118, ypos = 437)

        if shed_dialogue == 0 and not M_dewitt.is_state([S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint, S_dewitt_make_replacement_guitar]):
            call expression game.dialog_select("dianes_shed_shed_dialouge_0") from _call_expression_147
            $ shed_dialogue = 1

        elif shed_dialogue == 1 and drink_milk_offer and not aunt_shed_scene and game.timer.is_evening():
            call expression game.dialog_select("dianes_shed_shed_dialouge_1_intro") from _call_expression_148
            menu:
                "It's ok.":
                    call expression game.dialog_select("dianes_shed_shed_dialouge_1_okay") from _call_expression_149
                "No, it was wrong.":

                    call expression game.dialog_select("dianes_shed_shed_dialouge_1_wrong") from _call_expression_150
            $ aunt_shed_scene = True
    $ game.main()

label locked_shed_dialogue:
    scene garden
    if seen_shed_locked:
        call expression game.dialog_select("dianes_shed_seen_shed_locked") from _call_expression_151
    else:
        call expression game.dialog_select("dianes_shed_not_seen_shed_locked") from _call_expression_152
        $ seen_shed_locked = True
    $ game.main()

label aunt_dialogue_button_night:
    label aunt_shed_sex_seated:
        call expression game.dialog_select("dianes_shed_dianes_dialogue") from _call_expression_153
    if not store._in_replay == None:
        call expression game.dialog_select("aunt_shed_replay_1") from _call_expression_154
        call expression game.dialog_select("dianes_shed_dianes_dialogue_lets_milk_no_sex") from _call_expression_155
        dia "Let's get set up on the {b}breeding chair{/b}..."
        $ anim_toggle = False
        $ xray = False
        $ shed_cow_outfit = True
        $ M_aunt.set("sex speed", .4)
        $ previous_shed_sex_action = 0
        if store._in_replay == "aunt_shed_sex_seated":
            $ shed_sex_action = 1
        else:
            $ shed_sex_action = 0
            call expression game.dialog_select("dianes_shed_dianes_dialogue_lets_milk") from _call_expression_156
        jump expression game.dialog_select("shed_sex_loop")
    dia "Is there anything you want to talk about before we get started?"
    menu dia_default_dialogue_options_night:
        "Package." if quest13 in quest_list and quest13 not in completed_quests and not player.has_item("package"):
            call expression game.dialog_select("dianes_shed_dianes_dialogue_not_package") from _call_expression_157
            call expression game.dialog_select("dia_default_dialogue_options_night") from _call_expression_158

        "Package." if quest13 in quest_list and quest13 not in completed_quests and player.has_item("package"):
            call expression game.dialog_select("dianes_shed_dianes_dialogue_package") from _call_expression_159
            $ completed_quests.append(quest13)
            $ player.remove_item("package")
            call expression game.dialog_select("dia_default_dialogue_options_night") from _call_expression_160

        "Let's milk!" if quest12 not in completed_quests or quest13 not in completed_quests:
            call expression game.dialog_select("dianes_shed_dianes_dialogue_not_lets_milk") from _call_expression_161

        "Let's milk!" if quest12 in completed_quests and quest13 in completed_quests:
            if not shed_had_sex:
                call expression game.dialog_select("dianes_shed_dianes_dialogue_lets_milk_no_sex") from _call_expression_162
            else:

                call expression game.dialog_select("dianes_shed_dianes_dialogue_lets_milk_no_sex") from _call_expression_163
            call expression game.dialog_select("dianes_shed_dianes_dialogue_lets_milk") from _call_expression_164
            $ anim_toggle = False
            $ xray = False
            $ shed_cow_outfit = True
            $ previous_shed_sex_action = 0
            $ shed_sex_action = 0
            $ shed_sex_angle = 0
            $ M_aunt.set("sex speed", .4)
            call expression game.dialog_select("shed_sex_loop") from _call_expression_165
        "I should go.":

            call expression game.dialog_select("dianes_shed_dianes_dialogue_leave") from _call_expression_166
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
