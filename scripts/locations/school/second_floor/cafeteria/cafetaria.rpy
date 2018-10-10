label cafeteria_dialogue:
    $ player.go_to(L_school_cafeteria)
    call pa_announcement from _call_pa_announcement_4
    if quest09 in quest_list and quest09 not in completed_quests and quest09_1 == False and quest09_2 == False and quest09_3 == False:
        call expression game.dialog_select("cafeteria_milk_delivery") from _call_expression_496
        $ quest09_1 = True


    elif quest09 in quest_list and quest09 not in completed_quests and quest09_2 == True:
        call expression game.dialog_select("cafeteria_milk_delivery_invoice") from _call_expression_497
        $ player.remove_item("milk_carton")
        $ quest09_2 = False
        $ quest09_3 = True


    elif not erik.known(erik_favor) and player.location.is_here(M_kevin):
        call expression game.dialog_select("cafeteria_erik_favor_not_known") from _call_expression_498
        $ erik.add_event(erik_favor)

    elif erik.known(erik_favor) and not erik.completed(erik_favor_2) and player.location.is_here(M_kevin):
        call expression game.dialog_select("cafeteria_erik_favor_known") from _call_expression_499

    elif player.location.is_here(M_erik) and erik.completed(erik_favor_2):
        call expression game.dialog_select("cafeteria_erik_favor_2_completed") from _call_expression_500
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
