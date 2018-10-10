label kass_dialogue:
    scene location_mall_cupid_blur
    if kassy_first_visit:
        $ kassy_first_visit = False
        call expression game.dialog_select("kassy_first_visit") from _call_expression_1270
    else:

        call expression game.dialog_select("kassy_repeat") from _call_expression_1271

    hide kass
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
