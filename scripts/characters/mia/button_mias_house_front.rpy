label mia_dialogue_mias_house_front:
    call expression game.dialog_select("mia_dialogue_mias_house_front_intro") from _call_expression_1859
    menu:
        "About that homework.":
            call expression game.dialog_select("mia_dialogue_mias_house_front_homework") from _call_expression_1860
        "I forgot...":

            call expression game.dialog_select("mia_dialogue_mias_house_front_leave") from _call_expression_1861
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
