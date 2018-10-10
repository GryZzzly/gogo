label bank_dialogue:
    $ player.go_to(L_bank)
    if not L_bank.is_visited:
        call expression game.dialog_select("bank_first_time") from _call_expression_969
        $ L_bank.visited()
    $ game.main()

label bank_teller_dialogue:
    call expression game.dialog_select("bank_liu_start") from _call_expression_970
    menu:
        "Check my account.":
            call expression game.dialog_select("bank_liu_account_info") from _call_expression_971
            menu:
                "More information.":
                    call expression game.dialog_select("bank_liu_more_info") from _call_expression_972
                "Thanks, I have to go.":

                    call expression game.dialog_select("bank_liu_gtg") from _call_expression_973
        "Chat.":

            call expression game.dialog_select("bank_liu_chat") from _call_expression_974
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
