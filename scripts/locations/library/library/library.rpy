label library_dialogue:
    $ player.go_to(L_library)
    if getPlayingSound("<loop 9 to 83>audio/ambience_library.ogg"):
        $ playSound("<loop 9 to 83>audio/ambience_library.ogg", 1.0)

    if aunt.started(aunt_breeding_guide):
        call expression game.dialog_select("library_diane_breeding_intro") from _call_expression_85

    elif M_jane.is_state(S_jane_intro):
        call expression game.dialog_select("library_jane_intro") from _call_expression_86

    elif M_bissette.is_state(S_bissette_find_poem_reference_book) and player.location.is_here(M_mia):
        call expression game.dialog_select("library_bissette_find_poem_reference_book") from _call_expression_87


    elif M_ross.is_state(S_ross_find_magazines) and not M_ross.get("talked with jane"):
        call expression game.dialog_select("library_ross_find_magazines") from _call_expression_88
    $ game.main()

label library_bookshelf:
    $ player.go_to(L_library_bookshelf)
    $ player.location.call_screen(ui = False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
