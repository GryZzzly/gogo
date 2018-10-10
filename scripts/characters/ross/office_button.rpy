label button_ross_office_dialogue:
    if not M_ross.is_state(S_ross_end):
        call expression game.dialog_select("button_ross_office_generic_pre_hscene") from _call_expression_780
    else:
        call expression game.dialog_select("button_ross_office_generic_post_hscene") from _call_expression_781
    menu:
        "Private Lesson." if M_ross.is_state((S_ross_paint_with_body, S_ross_end)):
            call expression game.dialog_select("ross_dialogue_office_private_lessons") from _call_expression_782
            jump expression game.dialog_select("ross_hscene_start")
        "Nothing right now.":

            call expression game.dialog_select("ross_dialogue_office_leave") from _call_expression_783
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
