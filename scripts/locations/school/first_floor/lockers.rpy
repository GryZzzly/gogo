label annie_locker:
    call locker_check ("right", L_school_locker_annie) from _call_locker_check
    if not L_school_locker_annie.is_visited:
        call expression game.dialog_select("annie_locker_first_visit") from _call_expression_1702
        $ L_school_locker_annie.visited()
    $ player.go_to(L_school_locker_annie)
    $ player.location.call_screen(False)

label dexter_locker:
    call locker_check ("right", L_school_locker_dexter) from _call_locker_check_1
    if M_bissette.is_set("dexters book search"):
        call expression game.dialog_select("dexter_locker_first_visit") from _call_expression_1703
        python:
            for image in renpy.get_showing_tags():
                renpy.hide(image)
        call screen dexters_locker
        $ player.get_item("quick_mafs")
        call expression game.dialog_select("dexter_locker_book_found") from _call_expression_1704

        if M_bissette.is_state(S_bissette_jane_return_books):
            call expression game.dialog_select("bissette_book_search_2_books_left") from _call_expression_1705
        elif M_bissette.is_state([S_bissette_got_dexters_book, S_bissette_got_eriks_book, S_bissette_got_martinez_book]):
            call expression game.dialog_select("bissette_book_search_1_book_left") from _call_expression_1706
        else:
            call expression game.dialog_select("bissette_book_search_no_books_left") from _call_expression_1707
        $ M_bissette.trigger(T_bissette_ask_dexter)
        $ game.main()

    elif not L_school_locker_dexter.is_visited:
        call expression game.dialog_select("dexter_locker_first_visit") from _call_expression_1708
        $ L_school_locker_dexter.visited()
    $ player.go_to(L_school_locker_dexter)
    $ player.location.call_screen(False)

label erik_locker:
    call locker_check ("right", L_school_locker_erik) from _call_locker_check_2
    if not L_school_locker_erik.is_visited:
        call expression game.dialog_select("erik_locker_first_visit") from _call_expression_1709
        $ L_school_locker_erik.visited()
    $ player.go_to(L_school_locker_erik)
    $ player.location.call_screen(False)

label eve_locker:
    call locker_check ("right", L_school_locker_eve) from _call_locker_check_3
    if not L_school_locker_eve.is_visited:
        call expression game.dialog_select("eve_locker_first_visit") from _call_expression_1710
        $ L_school_locker_eve.visited()
    $ player.go_to(L_school_locker_eve)
    $ player.location.call_screen(False)

label judith_locker:
    call locker_check ("left", L_school_locker_judith) from _call_locker_check_4
    if not L_school_locker_judith.is_visited:
        call expression game.dialog_select("judith_locker_first_visit") from _call_expression_1711
        $ L_school_locker_judith.visited()
    $ player.go_to(L_school_locker_judith)
    $ player.location.call_screen(False)

label kevin_locker:
    call locker_check ("right", L_school_locker_kevin) from _call_locker_check_5
    if not L_school_locker_kevin.is_visited:
        call expression game.dialog_select("kevin_locker_first_visit") from _call_expression_1712
        $ L_school_locker_kevin.visited()
    $ player.go_to(L_school_locker_kevin)
    $ player.location.call_screen(False)

label mia_locker:
    call locker_check ("right", L_school_locker_mia) from _call_locker_check_6
    if not L_school_locker_mia.is_visited:
        call expression game.dialog_select("mia_locker_first_visit") from _call_expression_1713
        if M_mia.between_states(S_mia_start, S_mia_need_space):
            call expression game.dialog_select("mia_locker_first_visit_early_route") from _call_expression_1714

        elif M_mia.between_states(S_mia_concerning_visit, S_mia_route_split):
            call expression game.dialog_select("mia_locker_first_visit_helping_parents") from _call_expression_1715

        elif M_helen.get("helen route"):
            call expression game.dialog_select("mia_locker_first_visit_helen_route") from _call_expression_1716
        $ L_school_locker_mia.visited()
    $ player.go_to(L_school_locker_mia)
    $ player.location.call_screen(False)

label ronda_locker:
    call locker_check ("right", L_school_locker_ronda) from _call_locker_check_7
    if not L_school_locker_ronda.is_visited:
        call expression game.dialog_select("ronda_locker_first_visit") from _call_expression_1717
        $ L_school_locker_ronda.visited()
    $ player.go_to(L_school_locker_ronda)
    $ player.location.call_screen(False)

label roxxy_locker:
    call locker_check ("left", L_school_locker_roxxy) from _call_locker_check_8
    if not L_school_locker_roxxy.is_visited:
        call expression game.dialog_select("roxxy_locker_first_visit") from _call_expression_1718
        $ L_school_locker_roxxy.visited()
    $ player.go_to(L_school_locker_roxxy)
    $ player.location.call_screen(False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
