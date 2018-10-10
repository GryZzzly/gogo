label library_desk_dialogue:
    scene librarydesk
    if M_bissette.is_state(S_bissette_find_dictionary):
        call expression game.dialog_select("jane_library_dialogue_bissette_find_dictionary") from _call_expression_658
        $ M_bissette.trigger(T_bissette_check_library)

    elif M_bissette.is_state(S_bissette_get_dictionary) and player.has_item("french_dictionary"):
        call expression game.dialog_select("jane_library_dialogue_bissette_get_dictionary") from _call_expression_659
        $ M_bissette.trigger(T_bissette_check_library_shelf)


    elif M_bissette.is_state(S_bissette_return_overdue_books):
        call expression game.dialog_select("jane_library_dialogue_bissette_return_overdue_books") from _call_expression_660
        $ M_bissette.trigger(T_bissette_return_books)
        $ player.remove_item("oedipuss")
        $ player.remove_item("quick_mafs")
        $ player.remove_item("cholas_tricks")
    else:

        call expression game.dialog_select("jane_library_dialogue_pre") from _call_expression_661
        menu:
            "Milk production book." if aunt.started(aunt_breeding_guide):
                call expression game.dialog_select("jane_library_dialogue_milk_production_books") from _call_expression_662
                $ aunt_breeding_guide.finish()

            "French Poetry." if M_bissette.is_state(S_bissette_find_poem_reference_book):
                call expression game.dialog_select("jane_library_dialogue_french_poetry") from _call_expression_663

            "French Food." if M_bissette.between_states(S_bissette_find_food_book, [S_bissette_got_dexters_martinez_books, S_bissette_got_dexters_eriks_books,
                                                                                   S_bissette_got_eriks_dexters_books, S_bissette_got_eriks_martinez_books,
                                                                                   S_bissette_got_martinez_dexters_books, S_bissette_got_martinez_eriks_books
                                                                                  ]):
                if M_bissette.is_state(S_bissette_find_food_book):
                    call expression game.dialog_select("jane_library_dialogue_french_food_find_books") from _call_expression_664
                    $ M_bissette.trigger(T_bissette_check_library)
                else:

                    call expression game.dialog_select("jane_library_dialogue_french_food_book_holders") from _call_expression_665

            "Magazines" if M_ross.is_state(S_ross_find_magazines):
                if M_ross.get("talked with jane"):
                    call expression game.dialog_select("jane_library_dialogue_magazines_repeat") from _call_expression_666
                else:

                    call expression game.dialog_select("jane_library_dialogue_magazines_first") from _call_expression_667
                    $ M_ross.set("talked with jane", True)

            "Return library books" if get_returnable_books():
                call expression game.dialog_select("jane_library_dialogue_return_books_pre") from _call_expression_668
                if M_jane.get("first book returned"):
                    call expression game.dialog_select("jane_library_dialogue_return_books_first") from _call_expression_669
                    $ M_jane.set("first book returned", False)
                call expression game.dialog_select("jane_library_dialogue_return_books_after") from _call_expression_670
            "Nevermind.":

                call expression game.dialog_select("jane_library_dialogue_leave") from _call_expression_671

    hide xtra
    hide player
    hide jane
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
