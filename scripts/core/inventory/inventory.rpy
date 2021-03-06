init -1 python:
    class Item:
        def __init__(self, name_id):
            self.name = store.items[name_id]["name"]
            self.id_ = store.items[name_id]["id"]
            self.cost = int(store.items[name_id]["cost"])
            self.image = store.items[name_id]["image"]
            if self.image.startswith("transform"):
                self.transform = self.image
                self.image = Transform(self.image.split("-")[1])
            else:
                self.transform = None
            self.description = store.items[name_id]["description"]
            counter = 0
            newdesc = ""
            for char in self.description:
                counter += 1
                if counter >= 65 and char == " " or counter >= 80:
                    counter = 0
                    newdesc += "\n"
                newdesc += char
            self.description = newdesc
            self.closeup = store.items[name_id]["closeup"]
            self.dialogue = store.items[name_id]["dialogue_label"]
            self.name_id = name_id
        
        def __str__(self):
            return self.name_id

    class Inventory(object):
        def __init__(self, money = 20, savings = 0):
            self.items = []
            self.picked_up = []
            self.money = money
            self.savings = savings
        
        def __contains__(self, item):
            return item in self.items
        
        def get_item (self, item):
            if item not in self.items and self.money >= Item(item).cost:
                self.picked_up.append(item)
                self.items.append(item)
                self.money -= Item(item).cost
                if Item(item).cost > 0:
                    renpy.play("audio/sfx_coins2.ogg")
        
        def remove_item (self, item):
            if str(item) in self.items:
                self.items.remove(str(item))
        
        def trade_item (self, item, item_2):
            if str(item) in self.items:
                self.items.remove(str(item))
                self.items.append(str(item_2))
        
        def spend_money (self, value):
            self.money -= value
            renpy.play("audio/sfx_coins2.ogg")

    def deposit_money(d_money):
        if player.inventory.money >= d_money and (player.inventory.savings + d_money) <= 25000:
            player.inventory.savings += d_money
            player.inventory.money -= d_money

    def withdraw_money(d_money):
        if player.inventory.savings >= d_money:
            player.inventory.savings -= d_money
            player.inventory.money += d_money

screen item_desc(Item):
    $ description = Item.description
    text description pos 205, 555

screen item_name(Item):
    $ name = Item.name
    text name pos 205, 530

screen inventory_item_preview(Item):
    imagebutton:
        idle "backgrounds/location_backpack_closeup.jpg"
        action Hide("inventory_item_preview")

    imagebutton idle Item.closeup action NullAction() focus_mask True at Position(xalign = 0.5, yalign = 1.0)

screen backpack:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("item_desc"), Hide("item_name"), Hide("backpack"), Play("audio", "audio/sfx_backpack_close.ogg")]

    imagebutton idle "buttons/backpack.png" xalign 0.5 yalign 1.0 action [Hide("backpack"), Play("audio", "audio/sfx_backpack_close.ogg")] focus_mask True

    imagebutton idle "buttons/backpack_preloop.png" xpos 190 ypos 134 action NullAction() focus_mask True

    default backback_page = 1
    default items_per_page = 15
    default current_item = 0
    default start_item = 0
    default total_items = len(player.inventory.items)
    default Inv = player.inventory.items

    for current_item in xrange(start_item, (backback_page * items_per_page)):
        if current_item < total_items:
            $ start_xpos = 191
            $ start_ypos = 134
            $ row_ypos = math.trunc(current_item / 5)
            $ row_xpos = current_item - (row_ypos * 5)
            $ row_ypos -= math.trunc(start_item / 5)
            $ start_xpos += 130 * row_xpos
            $ start_ypos += 130 * row_ypos

            vbox:
                area (start_xpos,start_ypos,130,130)
                imagebutton:
                    idle Item(Inv[current_item]).image
                    if Item(Inv[current_item]).transform == None:
                        hover HoverImage(Item(Inv[current_item]).image)
                    else:
                        hover HoverImage(Item(Inv[current_item]).transform)
                    xalign 0.5
                    yalign 0.5
                    action [If(Item(Inv[current_item]).closeup == "",
                                NullAction(),
                                Show("inventory_item_preview", Item = Item(Inv[current_item]))
                            ),
                            If(Item(Inv[current_item]).dialogue == "",
                                NullAction(),
                                Function(renpy.call_in_new_context, Item(Inv[current_item]).dialogue, item = Item(Inv[current_item]))
                            ),
                            
                            Play("audio", "audio/sfx_backpack_select2.ogg")
                           ] hovered [Show(("item_name"), Item = Item(Inv[current_item])),
                                      Show(("item_desc"), Item = Item(Inv[current_item]))
                                     ] unhovered [Hide("item_desc"), Hide("item_name")]

    if backback_page > 1:
        imagebutton:
            focus_mask True
            pos (43,261)
            idle "buttons/backpack_left.png"
            action SetScreenVariable("backback_page", backback_page - 1), SetScreenVariable("start_item", start_item - 15)

    if current_item + 1 < total_items:
        imagebutton:
            focus_mask True
            pos (874,264)
            idle "buttons/backpack_right.png"
            action SetScreenVariable("backback_page", backback_page + 1), SetScreenVariable("start_item", start_item + 15)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
