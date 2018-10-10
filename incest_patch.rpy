






init 900 python:


    renpy.image("library_shelf", "backgrounds/location_library_shelf_patched.jpg")
    renpy.image("mc_locker", "backgrounds/location_school_locker_mc_day_patched.jpg")
    renpy.image("mc_locker_night", "backgrounds/location_school_locker_mc_night_patched.jpg")
    renpy.image("erik_locker", "backgrounds/location_school_locker_erik_day_patched.jpg")
    renpy.image("erik_locker_night", "backgrounds/location_school_locker_erik_night_patched.jpg")
    renpy.image("splash", "backgrounds/menu_splash_patched.jpg")
    renpy.image("unlock34", "boxes/popup_debbiebed_patched.png")
    renpy.image("popup_debbiebedroom", "boxes/popup_debbiebedroom_patched.png")
    renpy.image("popup_debbieshower", "boxes/popup_debbieshower_patched.png")
    renpy.image("computer_icon2", "buttons/computer_icon_02_patched.png")
    renpy.image("computer_icon9", "buttons/computer_icon_09_patched.png")
    renpy.image("computer_window1", "buttons/computer_window_01_patched.png")
    renpy.image("jenny_diary 01", "objects/object_diary_01_patched.png")
    renpy.image("jenny_diary 03", "objects/object_diary_03_patched.png")
    renpy.image("mailbox_letter", "objects/object_mailbox_item03_closeup_patched.png")
    renpy.image("mailbox_package_day", "objects/object_mailbox_item04_patched.png")
    renpy.image("mailbox_package_night", "objects/object_mailbox_item04_night_patched.png")
    renpy.image("debbienote", "objects/object_note_01_patched.png")


    dia.name = "Aunt Diane"


    incestPatchChanged1 = {
    
        
        "Where's {b}Mrs. Johnson{/b}?" : "Where's {b}Erik's Mom{/b}?",

    
        
        "... Do you need a place to stay? I'm sure, my {b}Landlady{/b} wouldn't mind letting you crash on the couch for as long as you need." : "... Do you need a place to stay? I'm sure, my {b}Mom{/b} wouldn't mind letting you crash on the couch for as long as you need.",

    
        
        "Help {b}[deb_name]{/b} around the house." : "Help {b}Mom{/b} around the house.",

    
        
        "( Something {b}[deb_name]{/b} would like? )" : "( Something {b}Mom{/b} would like? )",
        
        "Okay, {b}[deb_name]{/b}. How about this?" : "Okay, {b}Mom{/b}. How about this?",
        
        "Heh, thanks {b}[deb_name]{/b}!" : "Well, thanks {b}Mom{/b}!",
        
        "You look beautiful, {b}[deb_name]{/b}!" : "You look beautiful, {b}Mom{/b}!",

    
        
        "What if {b}[jen_name]{/b} comes in?" : "Just don't let {b}your sister{/b} see us.",
        
        "Heh, don't worry, she's up in her room." : "I can stop if I hear something...",
        
        "It's pretty bad, {b}[deb_name]{/b}... I don't think I can fix this one." : "It's pretty bad, {b}Mom{/b}... I don't think I can fix this one.",
        
        "I'm sure it'll be alright, {b}[deb_name]{/b}. I'll go and talk to the {b}dealership{/b}." : "It'll be alright, {b}Mom{/b}. I'll see if the {b}dealership{/b} can help us.",
        
        "What if {b}[jen_name]{/b} comes in?" : "Just don't let {b}your sister{/b} see us.",
        
        "Heh, don't worry. She's up in her room." : "I can stop if I hear something...",
        
        "Oh, {b}[deb_name]{/b}!" : "Oh, {b}Mom{/b}!",
        
        "Oh, I love it when you take charge!" : "You get so rough when you take me from behind.",
        
        "Hey, {b}[deb_name]{/b}..." : "Hey, {b}Mom{/b}...",
        
        "Hey {b}[deb_name]{/b}, got a minute?" : "Hey {b}Mom{/b}, got a minute?",
        
        "Need something, {b}[firstname]{/b}?" : "Sure, need something, {b}Sweetie{/b}?",
        
        "Or can I do something for you?" : "Or can {b}Mommy{/b} do something for you?",
        
        "{b}[jen_name]{/b} is in the shower." : "{b}Your sister{/b} is in the shower.",
        
        "Hello, {b}[deb_name]{/b}." : "Hello, {b}Mom{/b}.",
        
        "I hope you didn't fall too far behind, what with all that's happened?" : "I'm sorry you fell behind at your school after what happened...",
        
        "Nah, I'll catch up." : "It's okay, {b}Mom{/b}, I'm doing fine!",
        
        "Just let me know if there is ever anything I can do to help?" : "I'm just checking on my beautiful son, to make sure he's okay!",
        
        "Okay, {b}[deb_name]{/b}..." : "Okay, {b}Mom{/b}...",
        
        "{b}[deb_name]{/b}, do you know what happened to my {b}Dad{/b}?" : "{b}Mom{/b}... What happened to {b}Dad{/b}?",
        
        "In fact, It's my understanding that the case is on hold due to lack of evidence." : "They couldn't find any evidence, so they put the case on hold...",
        
        "I want closure on this whole thing too..." : "I want closure as much as {b}you and your sister{/b}...",
        
        "You're a young man and you need to focus on living your life" : "You're still a teenager. Live your life.",
        
        "Do it for your {b}Dad{/b}." : "It's what he would've wanted.",
        
        "Thanks, {b}[deb_name]{/b}." : "Thanks, {b}Mom{/b}.",
        
        "{b}[deb_name]{/b}, about what you said on the phone..." : "{b}Mom{/b}, about what you said on the phone...",
        
        "Everything is going to be fine!" : "We'll be alright!",
        
        "I feel somewhat responsible for all this stress..." : "I don't like seeing you so stressed out by this...",
        
        "You can help me by staying in school!" : "You're still in school!",
        
        "{b}[deb_name]{/b}, I wanted to talk about what that guy in the suit said..." : "{b}Mom{/b}, I wanted to talk about what that guy in the suit said...",
        
        "Was my {b}Dad{/b} involved with them?" : "Did you know about {b}Dad{/b}?",
        
        "{b}*Sigh({/b} I suppose, I can't keep you in the dark forever..." : "{b}*Sigh*{/b} I suppose, I can't keep you in the dark forever...",
        
        "Your {b}Father{/b} was a good man, {b}[firstname]{/b}." : "It was going fine, until a few years ago...",
        
        "... But he had a weakness for gambling." : "Then your Father started gambling, and eventually built up a lot of debt...",
        
        "He always told me it was nothing to concern myself over and that he had it all in hand." : "He told me he was able to pay it off, so I didn't press the issue too much.",
        
        "... But now he's gone and it seems there's a lot he didn't share with me." : "Suddenly, the accident happened...",
        
        "Your {b}Father{/b} owed those men a lot of money and they are still trying to collect." : "And now, they're trying to get the money from us...",
        
        "NO! I'm afraid of what might happen if I involve the authorities in this!" : "If what that man said is true... I can't risk them harming {b}you or your sister{/b}.",
        
        "So what, you're just going to pay those scumbags?!" : "Are we going to pay them?",
        
        "I've done my best but I'm afraid I just don't have the money to cover it all, Sweetie." : "We don't have the money, Sweetie.",
        
        "{b}*Sigh({/b} Maybe you and I should just disappear and start over somewhere else." : "{b}*Sigh*{/b} Maybe the whole family should just move away and start fresh...",
        
        "Heh, that would be an adventure, wouldn't it?" : "We'll figure something out.",
        
        "Thanks, {b}[deb_name]{/b}! Bye, {b}[deb_name]{/b}!" : "Thanks, {b}Mom{/b}! Love you, bye!",
        
        "You're welcome, {b}[deb_name]{/b}." : "You're welcome, {b}Mom{/b}.",
        
        "( I should go check the {b}car{/b} like {b}[deb_name]{/b} asked me to. )" : "( I should go check the {b}car{/b} like {b}Mom{/b} asked me to. )",
        
        "( I have to visit the {b}car dealership{/b}. Maybe they can fix {b}[deb_name]{/b}'s car... )" : "( I have to visit the {b}car dealership{/b}. Maybe they can fix {b}Mom{/b}'s car... )",
        
        "Hey, {b}[deb_name]{/b}, anything I can do to help around the house?" : "Hey, {b}Mom{/b}, anything I can do to help around the house?",
        
        "So uhh.." : "So uhh... {b}Mom{/b}...",
        
        "Hey, {b}[deb_name]{/b}!" : "Hey, {b}Mom{/b}!",
        
        "Would you like to join me in your room?" : "Want to...take a break with me in your bedroom?",
        
        "... Just make sure, {b}[jen_name]{/b} doesn't see us." : "... Just make sure, {b}your sister{/b} doesn't see us.",
        
        "You're going to wear me out!" : "But we can't do this all the time. You're going to wear {b}Mommy{/b} out!",
        
        "Get your butt upstairs and get those clothes off!" : "Oh, well in that case, let's get upstairs {b}Sweetie{/b}.",
        
        "Would you like to join me in your room?" : "Want to...take a break with me in your bedroom?",
        
        "Let's just make sure, {b}[jen_name]{/b} doesn't see us." : "Let's just make sure {b}your sister{/b} doesn't see us.",
        
        "I was hoping you'd bring me in here for this today!" : "You know, I was hoping you wanted to have some fun today.",
        
        "You were really thinking about it?" : "Oh yeah? What were you thinking about?",
        
        "Does that really surprise you?" : "Just of all those things you do that make me feel...good...",
        
        "I'm always thinking about that big cock of yours..." : "I can't stop thinking about that big cock of yours... And what made you think of me?",
        
        "Heh, I think about it a lot too... Especially when you're wearing that robe of yours." : "Every time I see your cleavage through your robe I just...",
        
        "You mean this old thing?" : "You mean these?",
        
        "Hehe, why don't you take off those clothes and come play with me?" : "Why don't you get undressed so we can play together...",
        
        "Come and get me, big boy!" : "Come to {b}Mommy{/b}, big boy!",
        
        "{b}[deb_name]{/b}, would you come with me for a second?" : "Hey {b}Mom{/b}, would you come with me for a second?",
        
        "Hehe, Alright. Let's go quickly while {b}[jen_name]{/b} is upstairs." : "Alright. Let's go quickly while {b}your sister{/b} is upstairs.",
        
        "Hehe, I'll take that as a yes!" : "Mmmm, I'll take that as a yes!",
        
        "Get those clothes off and get on the washer!" : "Hop up on that washing machine and let {b}Mommy{/b} take care of that for you...",
        
        "You look beautiful, {b}[deb_name]{/b}." : "You look beautiful, {b}Mom{/b}.",
        
        "Hey, {b}[deb_name]{/b}... Do you want to hang out in the basement for some quick fun?" : "Hey, {b}Mom{/b}... Can you come down to the basement for a minute?",
        
        "Hey... Umm, {b}[deb_name]{/b}?" : "Hey... Umm, {b}Mom{/b}?",
        
        "[chr_warn]It's okay, {b}[deb_name]{/b}." : "[chr_warn]It's okay, {b}Mom{/b}.",
        
        "Thanks {b}[deb_name]{/b}!" : "Thanks {b}Mom{/b}!",
        
        "Hehe, it's alright, Sweetheart." : "Oh, it's alright, Sweetheart.",
        
        "Actually, nevermind, see you later, {b}[deb_name]{/b}." : "Actually, never-mind, see you later, {b}Mom{/b}.",

    
        
        "Hey, {b}[deb_name]{/b}!" : "Hey, {b}Mom{/b}!",
        
        "Mmm, come get me, Sweetie!" : "Now, lay on top of {b}Mommy{/b}...",
        
        "{b}[deb_name]{/b}, want to have some fun?" : "{b}Mom{/b}, want to have some fun?",
        
        "Give me a minute to get ready." : "Give {b}Mommy{/b} a minute to get ready.",
        
        "Well, come back if you'd like... I'm a bit bored..." : "Well, come back if you'd like... {b}Mommy{/b} is a bit bored...",

    
        
        "Message from {b}Mr. Johnson{/b}." : "Message from {b}Erik's Dad{/b}.",
        
        "{b}Mrs. Johnson{/b}." : "{b}Erik's Mom{/b}.",
        
        "Where's {b}Mrs. Johnson{/b}?" : "Where's {b}Erik's Mom{/b}?",

    
        
        "You remember that {b}Master Blaster{/b} game {b}Mrs. Johnson{/b} bought you for Christmas a few years ago?" : "You remember that {b}Master Blaster{/b} game {b}your Mom{/b} bought you for Christmas a few years ago?",
        
        "Oh, right! Yeah, those are {b}Mr. Johnson's{/b} old guitars." : "Oh, right! Yeah, those are {b}my Dad's{/b} old guitars.",
        
        "Sometimes, I think he loved those guitars more than {b}Mrs. Johnson{/b}." : "Sometimes, I think he loved those guitars more than he loved {b}my Mom{/b}.",
        
        "... You wanna borrow one of {b}Mr. Johnson's{/b} guitars?" : "... You wanna borrow one of {b}my Dad's{/b} guitars?",
        
        "Well I don't mind but I'm not sure {b}Mrs. Johnson{/b} would like the idea of me loaning out {b}Mr. Johnson's{/b} old stuff." : "Well I don't mind but I'm not sure {b}my Mom{/b} would like the idea of me loaning out {b}my Dad's{/b} old stuff.",
        
        "{b}Mrs. Johnson{/b} would kill me!" : "{b}My Mom{/b} would kill me!",
        
        "( Hmm, I should be able to make a fake guitar using the {b}lumber near the treehouse{/b} and some {b}paint from Diane's shed.{/b} )" : "( Hmm, I should be able to make a fake guitar using the {b}lumber near the treehouse{/b} and some {b}paint from Aunt Diane's shed.{/b} )",
        
        "( Hmm, I should be able to make a fake guitar using the {b}lumber near the treehouse{/b} and some {b}paint from Diane's shed.{/b} )" : "( Hmm, I should be able to make a fake guitar using the {b}lumber near the treehouse{/b} and some {b}paint from Aunt Diane's shed.{/b} )",
        
        "Hey man, could I take a case of {b}Mr. Johnson's beer{/b}?" : "Hey man, could I take a case of {b}your dad's beer{/b}?",
        
        "What did {b}Mrs. Johnson{/b} want us to get again?" : "What did {b}your Mom{/b} want us to get again?",
        
        "I saw that {b}Larry{/b} guy. You know, {b}Mrs. Johnson's ex-husband{/b}?" : "I saw {b}your dad{/b}.",
        
        "Well, he's locked up and he asked me to apologize to {b}Mrs. Johnson{/b} for him." : "Well, he's still locked up, and he actually saw me when I was there...",
        
        "Yeah. He just wants to say he's sorry and he hopes that one day she'll forgive him." : "He wants you to know that he's sorry about everything...",
        
        "... I don't know if I should even bother telling her. What do you think?" : "...And hopefully, you will forgive him so he can see you again one day.",
        
        "Yeah, I dunno either. I don't think it will do much good, she really hates him..." : "I see...",
        
        "I'll let her know, Dude." : "Thanks for telling me that, {b}[firstname]{/b}.",
        
        "That works for me. Thanks, {b}Erik{/b}!" : "No problem, {b}Erik{/b}.",
        
        "Hey, you know that thing we did with {b}Mrs. Johnson{/b} after the poker game?" : "Hey, you know that thing we did with {b}your Mom{/b} after the poker game?",
        
        "Would you prefer to do stuff with {b}Mrs. Johnson{/b}?" : "Would you prefer to do stuff with {b}your Mom{/b}?",
        
        "We could always talk to {b}Mrs. Johnson{/b} about it?" : "We could always talk to {b}your Mom{/b} about it?",
        
        "I didn't know you and {b}Mrs. Johnson{/b} were... so close." : "I didn't know you and {b}your Mom{/b} were... so close.",
        
        "I mean, {b}Mrs. Johnson{/b} is like... really hot!" : "I mean, {b}your Mom{/b} is like... really hot!",
        
        "Just...please don't tell anyone alright?" : "It's just that... it's {b}my Mom{/b}, you know? Just...please don't tell anyone alright?",
        
        "Where's {b}Mrs. Johnson{/b}?" : "Where's {b}Erik's Mom{/b}?",
        
        "Is everyone alright at your new place?" : "Is everything OK at home with your family?",
        
        "{b}[deb_name]'s{/b} been getting {b}weird phone calls{/b} but she say's everything's fine so..." : "{b}Mom's{/b} been getting {b}weird phone calls{/b} but she says everything's fine so...",
        
        "What should I ask {b}Mrs. Johnson{/b} again?" : "What should I ask {b}your Mom{/b} again?",

    
        
        "I'll talk with him. I know his wife." : "I'll talk with him. His son is my best friend.",
        
        "( I have to make sure I get the right ingredients... )" : "( I have to make sure I get the right {b}glaze flavor{/b} and {b}topping{/b}... )",

    
        
        "{b}Diane{/b}?" : "{b}Aunt Diane{/b}?",
        
        "Let me check... Right! Here it is!" : "{b}*THUD*{/b} Oops, I'm such a klutz! I didn't hear what you said before \"Diane\", but I know I saw that name earlier... Ah, here it is!",

    
        
        "The second is a {b}Mr. Erik J-{/b}." : "The second is a {b}Mr. Erik Johnson{/b}.",

    
        
        "{b}[deb_name]{/b} needs you." : "{b}Mom{/b} needs you.",

    
        
        "What would the little pervert want this time?" : "And what would my perverted {b}little brother{/b} want this time?",
        
        "Hey, {b}[jen_name]{/b}..." : "Hey, {b}Sis{/b}...",
        
        "Why are you talking like that?" : "Why would you even say that?",
        
        "I'm not your girlfriend, you IDIOT!!" : "I'm {b}your sister{/b}! Not some girlfriend from school, you IDIOT!!",
        
        "I knew he liked me but... I can't believe that little pervert is starting to have feelings for me now." : "I knew he liked me but... I can't believe my {b}little brother{/b} is starting to have feelings for me now.",
        
        "Ugh!! He's probably just horny." : "Ugh!! He's probably just {b}REALLY{/b} horny. Yeah, that must totally be it.",
        
        "I'm not your girlfriend, you IDIOT!!" : "I'm {b}your sister{/b}! Not some girlfriend from school, you IDIOT!!",
        
        "Ugh!! He's probably just horny." : "Ugh!! He's probably just {b}REALLY{/b} horny. Yeah, that must totally be it.",
        
        "I wouldn't want a pervert spying on me." : "I wouldn't want my pervert {b}little brother{/b} spying on me.",

    
        
        "I guess you have to be a witness, then." : "I you'll just have to be my witness then, {b}little brother{/b}.",

    
        
        "You want to feel my wet pussy wrapped around your cock, huh?" : "You wanna feel {b}your big sister's{/b} wet pussy wrapped around your cock again, huh?",
        
        "Just sit back, keep that cock of yours nice and hard, and let me know when you're about to cum." : "Just lay back, keep your big cock hard, and your big mouth shut. No one can find out that you're {b}my brother{/b}!",
        
        "Just sit back, keep that cock of yours nice and hard, and let me know when you're about to cum." : "Just lay back, keep your big cock hard, and your big mouth shut. No one can find out that you're {b}my brother{/b}!",
        
        "Will you look at that nice, thick, long cock..." : "Will you look at that beautiful thick, long cock...",

    
        
        "Oh, and do me a favor: try not to spend TOO much time with {b}[deb_name]{/b}..." : "Oh, and do me a favor - try not to spend TOO much \"naughty time\" with {b}Mom{/b}...",
        
        "Don't lie to me! I know you've been fantasizing about this moment for a long while now." : "I know you've been jacking off while dreaming of {b}fucking your big sister{/b} for years now. Well, now's your chance.",
        
        "So this is your chance, pervert." : "No bullshit. No tricks. Are you man enough to fuck me or what, {b}little brother{/b}?",
        
        "Just sit back, keep that cock of yours nice and hard, and let me know when you're about to cum." : "Just lay back, keep your big cock hard, and your big mouth shut. No one can find out that you're {b}my brother{/b}!",
        
        "Will you look at that nice, thick, long cock..." : "Will you look at that beautiful thick, long cock...",
        
        "You did pretty well, I guess." : "I thought you'd be pretty awful, but you were throwing some serious dick back there, {b}little brother{/b}.",
        
        "Oh, and do me a favor, try not to spend TOO much time with {b}[deb_name]{/b}..." : "Oh, and do me a favor - try not to spend TOO much \"naughty time\" with {b}Mom{/b}...",
        
        "My subscribers are expecting more cam shows this week." : "My subscribers won't pay to see a huge cock that won't get hard, and you've gotta be able to shoot as much cum as you did today {b}every time{/b}.",

    
        
        "Yeah, you did pretty well, I guess." : "Honestly, I thought you'd be pretty awful, but you were throwing some serious dick in there, {b}little brother{/b}.",
        
        "Oh, and do me a favor, and try not to spend TOO much time with {b}[deb_name]{/b}..." : "Oh, and do me a favor - try not to spend TOO much \"naughty time\" with {b}Mom{/b}...",
        
        "My subscribers are expecting more cam shows this week." : "My subscribers won't pay to see a huge cock that won't get hard, and you've gotta be able to shoot as much cum as you did today {b}every time{/b}.",
        
        "You mean, you want me to play with you on the couch?" : "You mean, you want your {b}older sister{/b} to play with you on the couch?",
        
        "Let's go quick, while {b}[deb_name]{/b} is downstairs..." : "Let's go quick, while {b}Mom's{/b} busy downstairs...",
        
        "Hmm... Hold on, I see... {b}Mrs. Johnson{/b} on her bed..." : "Hmm... Hold on, I see... {b}Erik's mom{/b} on her bed...",
        
        "Well done, pervert!" : "Well done, {b}little brother{/b}!",
        
        "( I can't believe {b}[jen_name]{/b} was so into this... )" : "( I can't believe {b}my Sister{/b} was so into this... )",

    
        
        "What was {b}[deb_name]'s{/b} vanity plate again?" : "What was {b}Mom's{/b} vanity plate again?",
        
        "We're kinda going through a rough patch at the moment." : "My family is kinda going through a rough patch at the moment.",
        
        "The woman I'm living with only has the one car and it's pretty important to us..." : "My {b}Mom{/b} doesn't exactly have a job..",
        
        "I should probably talk to {b}[deb_name]{/b} about this." : "I should probably talk to {b}Mom{/b} about this.",

    
        
        "Yeah. I don't think [deb_char_name] will be bothering us." : "Yeah. I don't think {b}my Mom{/b} will be bothering us.",
        
        "Yeah... [tmp_deb_name] said I need to get to bed earlier." : "Yeah... {b}my Mom{/b} said I need to get to bed earlier.",
        
        "Yeah, [deb_char_name] is going to get suspicious with all the time we spend in here..." : "Yeah, {b}my Mom{/b} is going to get suspicious with all the time we spend in here...",
        
        "Yeah, [deb_char_name] is going to get suspicious with all the time we spend in here..." : "Yeah, {b}my Mom{/b} is going to get suspicious with all the time we spend in here...",
        
        "Yeah, [deb_char_name] is going to get suspicious with all the time we spend in here..." : "Yeah, {b}my Mom{/b} is going to get suspicious with all the time we spend in here...",

    
        
        "I just... I was hoping you'd give {b}Tammy{/b} a message from me?" : "I just... I was hoping you'd give {b}Erik{/b} a message from me?",
        
        "I need you to tell her that I'm sorry!" : "I need you to tell him that I'm sorry!",
        
        "I'll tell you where it is if you just tell {b}Tammy{/b} I'm sorry." : "I'll tell you where they are if you tell {b}my son{/b} that everything I did was to help him.",
        
        "I just don't want her to hate me forever, you know?" : "I was trying to get back on top, you know?",
        
        "I should never left her..." : "I just...did it the wrong way, and I'm sorry for that...",
        
        "Just please tell her I'm sorry..." : "Can you just tell {b}Erik{/b} I'm sorry... and that I love him?",
        
        "Hopefully, she can find it in her heart to forgive me one day..." : "Hopefully, he can forgive me one day and... perhaps we can see each other again?",
        
        "Just tell {b}Tammy{/b} that I'm sorry. I should never have left her..." : "Talk to {b}Erik{/b} and tell him I love him and that I'm sorry...",
        
        "Did you get a chance to speak with {b}Tammy{/b}?" : "Did you get a chance to speak to {b}Erik{/b} like I asked?",
        
        "And what... what did she say?!" : "And what... what did he say?!",
        
        "She didn't! Look, Man... She got the message like you wanted." : "He'll think about it.",
        
        "You didn't say anything about bringing you a message back!" : "You need to give him some time, I guess...",
        
        "Yeah, you're right. Sorry." : "Thanks, kid.",
        
        "You held up your end of the bargain." : "You did the right thing...",
        
        "And maybe... One day... {b}Tammy{/b} will take me back!" : "And... and maybe, someday you can even convince {b}Erik{/b} to come visit me?",

    
        
        "Hi, {b}Mrs. Johnson{/b}!" : "Oh, Hi!",
        
        "You're... very pretty, {b}Mrs. Johnson{/b}." : "You're... very pretty, {b}Mom{/b}.",
        
        "I just wanted {b}Erik{/b} to experience and see what women are all about!" : "I just wanted {b}my Baby Boy{/b} to experience and see what women are all about!",
        
        "Do you think you could help your... favorite neighbor??" : "Do you think you could help out {b}your best friend's Mother{/b}??",

    
        
        "Hi, {b}Mrs. Johnson{/b}!" : "Oh, Hi!",
        
        "Hi, {b}Mrs. Johnson{/b}!" : "Oh, Hi!",
        
        "You know, I think he's having problems adjusting to life out on his own." : "You know that his {b}Father{/b} left us when he was born so...",
        
        "I worry about him." : "...He's had a lonely upbringing!",
        
        "He's not used to being the man of the house." : "He's never had a {b}Dad{/b} or {b}brothers{/b}!",
        
        "... And he has such a hard time with girls." : "He also never had any girls in his life... Other than his {b}Mom{/b}...",
        
        "The poor thing has to be lonely." : "...So, I just try to give him all the affection he needs!",
        
        "It's a good thing he has a loyal friend like you, {b}[firstname]{/b}!" : "Anyway, I want to thank you for being so friendly to my boy!",
        
        "He needs you." : "You are such a good friend to him...",
        
        "Of course not! I'm just chatting with a friend of my tenant, {b}Erik{/b}!" : "Of course not! I'm just chatting with a friend of my son!",

    
        
        "( I wonder what {b}[jen_name]{/b} is doing right now. )" : "( I wonder what {b}my Sister{/b} is doing right now? )",
        
        "( I wonder what {b}Mrs. Johnson{/b} is doing right now. )" : "( I wonder what {b}Erik's Mom{/b} is doing right now. )",

    
        
        "A girl that lives at the same house as me." : "{b}My older Sister{/b}, {b}[jen_name]!",
        
        "A girl that lives at the same house as me." : "{b}My older Sister{/b}, {b}[jen_name]!",
        
        "... But..." : "He'd appreciate knowing you've been taking care of things for us.",

    
        
        "I guess I could save up some of that money {b}Diane{/b} gives me..." : "I guess I could save up some of that money {b}Aunt Diane{/b} gives me...",

    
        
        "( I don't think {b}[deb_name]{/b} would mind... )" : "( I don't think {b}Mom{/b} would mind... )",
        
        "I don't think {b}[deb_name]{/b} would be very happy if I brought you home." : "I don't think {b}Mom{/b} would be very happy if I brought you home.",

    
        
        "{b}Diane{/b}!" : "{b}Aunt Diane{/b}!",
        
        "{b}Diane{/b}..." : "{b}Aunt Diane{/b}...",
        
        "Sorry! Just a silly old woman screaming at imaginary rodents. Hahah!" : "Sorry! Just your {b}Auntie{/b} screaming about an imaginary rodent. Hahah!",
        
        "It's alright, {b}Diane{/b}. I don't mind." : "It's alright, {b}Aunt Diane{/b}. I don't mind.",
        
        "No, I'm serious! You're a real knockout, {b}Diane{/b}." : "No, I'm serious! You're a real knockout, {b}Aunt Diane{/b}.",
        
        "You're welcome, {b}Diane{/b}." : "You're welcome, {b}Aunt Diane{/b}.",
        
        "( I just saw {b}Diane{/b} in her underwear! )" : "(Never thought I'd see {b}Aunt Diane{/b} like this.)",

    
        
        "{b}Diane{/b} is probably asleep..." : "{b}Aunt Diane{/b} is probably asleep...",

    
        
        "Yoo-hooo! Theeere's my handsome little man!" : "Yoo-hooo! Theeere's {b}my handsome nephew{/b}!",
        
        "{b}Diane{/b}? Are you drunk?" : "{b}Aunt Diane{/b}? Are you okay?",
        
        "{b}Diane{/b}, your clothes... they um... slipped." : "{b}Aunt Diane{/b}, your clothes... they um... slipped.",
        
        "That's what happens when you start drinking before you get dressed..." : "That's what happens when you start drinking before you get dressed, {b}my sweet nephew{/b}.",
        
        "Have I ever told you how much I dislike {b}[deb_name]'s{/b} other tenant?" : "Have I ever told you you're my {b}favorite nephew{/b}?",
        
        "Uh, no. You mean, {b}[jen_name]{/b}?" : "Uh... a few times?",
        
        "Yes! *hic* That's the one!" : "I mean, {b}your sister{/b} is such a... bitch, you know?",
        
        "She's such a biiiitch!" : "But I like you a lot more...",
        
        "I wish I had nice young tits like her though..." : "I wish I had nice young perky tits like {b}your sister{/b} though...",
        
        "I mean, don't you think they look better than these old things?" : "I mean, don't you think they look better than your {b}Auntie's{/b} old boobs?",
        
        "I am so enjoying our little chats!" : "And that's why you're my {b}favorite nephew{/b}!",
        
        "You must think I'm a- *hic* a big lush." : "You must think your {b}Auntie{/b} is just an easy lush.",
        
        "Huh. Where's {b}Diane{/b}?" : "Huh. Where's {b}Aunt Diane{/b}?",
        
        "Hi, {b}Diane{/b}!" : "Hi, {b}Aunt Diane{/b}!",
        
        "Wow! You look so much like {b}[deb_name]{/b}..." : "Wow! You look so much like {b}Mom{/b}...",
        
        "Oh, come now. I'm not nearly as pretty as {b}[deb_name]{/b}..." : "Oh, {b}your Mom{/b} was always the prettier {b}twin{/b}...",
        
        "Well, I think you look great, {b}Diane{/b}!" : "Well, I think you look great, {b}Aunt Diane{/b}!",
        
        "I'm guessing {b}[deb_name]{/b} told you I am looking for someone to help me this summer?" : "I'm guessing, {b}your Mom{/b} told you I was looking to pay a strong, young man to help me take care of my garden?",
        
        "Yeah and I could definitely use the money for tuition..." : "Yeah, I could use the money for College, starting in the fall, and I don't have any other jobs yet, so...",
        
        "It's okay, {b}Diane{/b}." : "It's okay, {b}Aunt Diane{/b}.",
        
        "Hi, {b}Diane{/b}." : "Hi, {b}Aunt Diane{/b}.",
        
        "You think you can take care of that waste problem today?" : "You think you can help your old {b}Aunt{/b} with the wheelbarrow this time?",
        
        "It's no problem!" : "It's no problem, {b}Aunt Diane{/b}!",
        
        "Hi, {b}Diane{/b}!" : "Hi, {b}Aunt Diane{/b}!",
        
        "It's so heavy though! I'm afraid it's too much for my poor back!" : "But it's too heavy, and your poor old {b}Aunt's{/b} back hurts!",
        
        "You look great, {b}Diane{/b}." : "You look great, {b}Aunt Diane{/b}.",
        
        "Thanks, {b}Diane{/b}." : "Thanks, {b}Aunt Diane{/b}.",
        
        "[str_warn]I... I can't do it..." : "[str_warn]I... I can't do it, {b}Aunt Diane{/b}...",
        
        "Hi {b}Diane{/b}!" : "Hi {b}Aunt Diane{/b}!",
        
        "Sure, {b}Diane{/b}! Anything you need!" : "Sure, {b}Aunt Diane{/b}! Anything you need!",
        
        "Sure, {b}Diane{/b}! Anything you need!" : "Sure, {b}Aunt Diane{/b}! Anything you need!",
        
        "{b}Diane{/b}?" : "{b}Aunt Diane{/b}?",
        
        "Sure, {b}Diane{/b}, I can have a look." : "Sure, {b}Aunt Diane{/b}, I can have a look.",
        
        "Where's {b}Diane{/b}?" : "Where's {b}Aunt Diane{/b}?",
        
        "Hi {b}Diane{/b}!" : "Hi {b}Aunt Diane{/b}!",
        
        "You don't want me to burn, do you?" : "You don't want your poor {b}Aunt Diane{/b} to burn, do you?",
        
        "( I can't believe I'm touching {b}Diane{/b}'s naked back... )" : "( I can't believe I'm touching {b}Aunt Diane{/b}'s naked back... )",
        
        "I'm so sorry {b}Diane{/b}!!" : "I'm so sorry {b}Aunt Diane{/b}!!",
        
        "Well... You're naked, {b}Diane{/b}!" : "Well... You're naked, {b}Aunt Diane{/b}!",
        
        "I should visit {b}Diane{/b} another time..." : "I should visit {b}Aunt Diane{/b} another time...",
        
        "Hi {b}Diane{/b}..." : "Hi {b}Aunt Diane{/b}...",
        
        "It's okay {b}Diane{/b}..." : "It's okay {b}Aunt Diane{/b}...",
        
        "Don't worry... I won't tell anyone." : "Don't worry... I won't tell {b}Mom{/b}.",
        
        "Aww! Thanks hun! You're such a gentleman!" : "Aw! Thanks hun. That's why you're my {b}favorite nephew{/b}!",
        
        "Hey Handsome! You here to help old {b}Diane{/b} pick some vegetables?" : "Hey Handsome! You came back to help your poor old {b}Aunt{/b} pick her favorite vegetables?",
        
        "I don't think you look old at all, {b}Diane{/b}." : "I don't think you look old at all, {b}Aunt Diane{/b}.",
        
        "{b}Diane's{/b} shed is {b}still open{/b}..." : "{b}Aunt Diane's{/b} shed is {b}still open{/b}...",
        
        "You sure know how to put a smile on my face, {b}[firstname]{/b}!" : "You sure know how to please your {b}Aunt{/b}... And that is very sweet of you...",
        
        "I knew you would enjoy my breasts." : "You seem to enjoy playing with your {b}Aunt{/b}'s body...",
        
        "I'm sorry, {b}Diane{/b}!" : "I'm sorry, {b}Aunt Diane{/b}!",
        
        "I've got myself a little crush on you." : "...You're obviously having strong desires for {b}my body{/b}...",
        
        "And you obviously have an attraction to me as well..." : "...and your {b}Aunt{/b} hasn't had any attention from a man in a very long time...",
        
        "I don't see any reason we can't explore this a little further. So long as we keep it {b}between us{/b}, do you agree?" : "...So why don't we keep this situation just {b}between us{/b}?",
        
        "Well, you just let me know when you want some to have some fun with me." : "Well... You just let me know if you want some \"special attention\" from your {b}Aunt{/b}...",
        
        "Especially not {b}[deb_name]{/b}! She'd kill me!!!" : "Especially not {b}your Mom{/b}! She'd kill me!!!",
        
        "Hey Handsome! You here to help old {b}Diane{/b} pick some vegetables?" : "Hey Handsome! You came back to help your poor old {b}Aunt{/b} pick her favorite vegetables?",
        
        "I don't think you look old at all, {b}Diane{/b}." : "I don't think you look old at all, {b}Aunt Diane{/b}.",
        
        "You've been very helpful to {b}[deb_name]{/b} and I during this whole thing with {b}my dad{/b}." : "You used to come by all the time and hang out with {b}Mom{/b}...",
        
        "I betcha {b}[deb_name]{/b} would love it if you came around more often..." : "I betcha {b}my Mom{/b} would love it if you came around again...",
        
        "I'm just glad I could make things a little easier on you two." : "I guess your {b}Aunt{/b} just likes to have some alone time, lately.",
        
        "Honestly, I've been enjoying the company as well." : "After all, there's so much to do here... with my garden...",
        
        "Well, I guess, I've just gotten used to being on my own." : "Well... After my last divorce...",
        
        "Since my husband and I divorced, I don't get out as much as I used to." : "I guess... I don't see the point in trying to meet people, anymore.",
        
        "Heh, makes me feel like I'm turning into a sour old woman!" : "So I just don't go out as much!",
        
        "Don't say that..." : "Oh. I see...",
        
        "You probably don't know this, but {b}[deb_name]{/b} and I used to get pretty crazy back in our day!" : "You might not know this, but I used to go out with {b}your Mom{/b} all the time!",
        
        "We were fighting men off everywhere we went." : "We were known around town as the {b}Slinky Twins{/b}...",
        
        "... And the parties we used to throw! Phew!" : "We were partying all the time!",
        
        "We would go out on the town and dance all night together!" : "We would go out on double dates, and dance all night together.",
        
        "That's how we met and became friends with your {b}Father{/b}!" : "That's how {b}your Mom{/b} met {b}your Father{/b}, and I met all my stupid, ex-husbands.",
        
        "... and also where I found my stupid ex-husband. Haha!" : "That's what I get for drinking too much, and making poor decisions! Haha...",
        
        "What am I saying? You don't want to hear all of this!" : "What am I saying? You don't want to hear about your {b}old Aunt's{/b} problems!",
        
        "{b}[deb_name]{/b} said she gave the old paint in the garage." : "{b}Mom{/b} said she gave the old paint in the garage.",
        
        "I've got some great news, {b}Diane{/b}!" : "I've got some great news, {b}Aunt Diane{/b}!",
        
        "Awesome! Thanks, {b}Diane{/b}!" : "Awesome! Thanks, {b}Aunt Diane{/b}!",
        
        "But don't worry, {b}Diane{/b}! I'll find a way!" : "But don't worry, {b}Aunt Diane{/b}! I'll find a way!",
        
        "I'm so lucky to have a {b}handy man{/b} like you around, {b}[firstname]{/b}!" : "I'm so lucky to have such a... {b}handy Nephew{/b}...",
        
        "Hehe, see? Two can play at this game!" : "{b}Your Aunt{/b} can play this game too!",
        
        "Come here, and give old {b}Diane{/b} a nice {b}kiss{/b}!" : "Come here, and give your {b}Aunt{/b} a nice {b}kiss{/b}!",
        
        "Dropping by my house on the way back from school?" : "Dropping by {b}your Aunt{/b}'s house on the way back from school?",
        
        "Bored at home, and felt like seeing little old me?" : "Bored at home, and felt like seeing {b}your Aunt{/b}?",
        
        "You've been missing me?" : "You've been missing your {b}Auntie{/b}?",
        
        "It's been a long time since a man has shown me any interest." : "I haven't had a man around... In quite some time.",
        
        "That's crazy! You're so sexy, {b}Diane{/b}." : "I appreciate everything you've been doing for me, {b}Aunt Diane{/b}...",
        
        "I can't believe you're wasting your time with me..." : "I've never had someone give me that kind of... Attention, before...",
        
        "... You're completely out of my league!" : "...And you're so pretty...",
        
        "Don't be silly, {b}[firstname]{/b}. You're wonderful!" : "You're so sweet!",
        
        "I know it really gets my motor going!" : "That's why you're my favorite. I can trust you to keep this between us!",
        
        "Well my door is always open for you, {b}[firstname]{/b}." : "Your {b}Auntie{/b} will always have her... Door open for you.",
        
        "I worry about {b}[deb_name]{/b}..." : "I worry about {b}Mom{/b}...",
        
        "She seems really stressed out, with everything that's happened recently..." : "She seems really stressed out, after all that happened with {b}Dad{/b}...",
        
        "I've known {b}[deb_name]{/b} since we were kids. She's a strong woman, {b}[firstname]{/b}." : "Hmmm... Well, my {b}Sister{/b} is a strong woman, just like me.",
        
        "{b}[firstname]{/b}, do you have feelings for {b}[deb_name]{/b}?" : "{b}[firstname]{/b}, do you have feelings for {b}your Mom{/b} as well?",
        
        "Huh? Feelings?" : "Well... I love {b}my Mom{/b}, of course.",
        
        "Sexual feelings... Do you ever imagine yourself doing things with her? Things like you and I do during our {b}secret fun{/b} sessions?" : "Do you {b}fantasize{/b} about her? Do you want to do things to her, like you do with me?",
        
        "I can't help it! She's so beautiful..." : "I've been thinking about her... And I get all excited when I see her...",
        
        "... And we're around each other so often nowadays." : "Like when I catch her in the shower, and stare at her naked...",
        
        "Heh, well this is an interesting turn of events!" : "Oh {b}wow{/b}...",
        
        "Have you told her?" : "Does she know?",
        
        "Why not? If she's making you feel this way-" : "You must be horny constantly.",
        
        "I can't do that! What if she freaks out?!" : "I know. I have these urges, and I keep thinking about doing stuff with {b}Mom{/b}... and {b}You{/b}.",
        
        "Oh, good grief! Trust me, {b}[firstname]{/b}. She's not the type to freak out over something like this!" : "My goodness! You must have a thing for {b}twins{/b}!",
        
        "I'm sure she's lonely too. She lost her husband ages ago and now that your {b}father{/b} is gone..." : "Well, she's lonely... She could use a man around her.",
        
        "She could use a man that's willing to take care of her and satisfy her needs..." : "Someone to take care of her, and satisfy... Whatever needs she has!",
        
        "She's lucky to have you staying with her." : "Well, you're doing just fine! And she's lucky to have such a caring {b}Son{/b}.",
        
        "You're such a great kid, {b}[firstname]{/b}!" : "Oh, you're the best nephew in the whole world!",
        
        "It's nothing, {b}Diane!{/b}" : "It's nothing, {b}Aunt Diane!{/b}",
        
        "So what do you think, {b}Diane{/b}?" : "So what do you think, {b}Aunt Diane{/b}?",
        
        "You're welcome, {b}Diane{/b}!" : "You're welcome, {b}Aunt Diane{/b}!",
        
        "My ex never wanted any..." : "My exes never wanted any...",
        
        "I can't believe how turned on I am by that farming manual!" : "I can't believe {b}my nephew{/b} is suggesting farming manuals...",
        
        "I wonder how {b}[firstname]{/b} would feel about being my {b}bull{/b}?" : "The only person I can think of who might \"breed\" me is... {b}my nephew{/b}.",
        
        "He's still in college though! He's practically a kid! I can't ask him for this... Can I?" : "Come on, {b}Diane{/b}! You're thinking about {b}fucking your sister's son raw to get knocked up{/b}!",
        
        "What would {b}[deb_name]{/b} say if she heard me talking about this?!" : "What would I say to {b}my twin sister{/b} if I had a kid with {b}her son{/b}?",
        
        "Doing nothing isn't really an option." : "He's done nothing BUT help... satisfy me, lately.",
        
        "I suppose I could talk with him about it." : "God, I keep thinking about his huge cock!",
        
        "[chr_warn]Sure, {b}Diane{/b}." : "[chr_warn]Sure, {b}Aunt Diane{/b}.",
        
        "We're talking about bringing a life into the world. That means responsibilities!" : "You're {b}my Sister's kid{/b}!",
        
        "I know. I thought you were ready to accept those responsibilities?" : "I'm sorry, I thought maybe you'd want to.",
        
        "I... I am!" : "I... I do!",
        
        "Who's asking me? I'm offering to {b}breed you, Diane{/b}. I want to." : "Who's asking me? I'm offering to {b}breed you, Aunt Diane{/b}. I want to.",
        
        "No, I... I really like doing those things with you {b}Diane{/b}!" : "No, I... I really like doing those things with you {b}Aunt Diane{/b}!",
        
        "{b}[deb_name]{/b} can never know about this, okay?!" : "{b}Your Mother{/b} can never know about this, okay?",
        
        "See you there, {b}Diane{/b}!" : "See you there, {b}Aunt Diane{/b}!",
        
        "I've never seen one this big before..." : "I've never seen one this big before... None of my ex husbands come close to this...",
        
        "You're so pretty, {b}Diane{/b}..." : "You're so pretty, {b}Aunt Diane{/b}...",
        
        "[chr_warn]I... I want to be inside you {b}Diane{/b}." : "[chr_warn]I... I want to be inside you {b}Aunt Diane{/b}.",
        
        "I... I want to be inside you {b}Diane{/b}." : "I... I want to be inside you {b}Aunt Diane{/b}.",
        
        "You're so pretty, {b}Diane{/b}..." : "You're so pretty, {b}Aunt Diane{/b}...",
        
        "I... I want to be inside you {b}Diane{/b}." : "I... I want to be inside you {b}Aunt Diane{/b}.",
        
        "I... I want to be inside you {b}Diane{/b}." : "I... I want to be inside you {b}Aunt Diane{/b}.",
        
        "We'll relieve all that stress you're building up at school." : "Especially after school, when you need to release all that stress!",
        
        "You don't want to keep {b}[deb_name]{/b} waiting!" : "You don't want to keep {b}your Mom{/b} waiting!",
        
        "Don't worry, {b}Diane{/b}, I won't tell anyone." : "Don't worry, {b}Aunt Diane{/b}, I won't tell anyone.",
        
        "You don't want to keep {b}[deb_name]{/b} waiting!" : "You don't want to keep {b}your Mom{/b} waiting!",
        
        "Don't worry, {b}Diane{/b}, I won't tell anyone." : "Don't worry, {b}Aunt Diane{/b}, I won't tell anyone.",
        
        "Any time. I'm always hungry..." : "Any time. {b}Your Aunt{/b} is always hungry...",
        
        "{b}Diane{/b} said she would be in the {b}barn{/b}." : "{b}Aunt Diane{/b} said she would be in the {b}shed{/b}.",
        
        "{b}Diane{/b} is probably asleep... I don't think I can work on the garden right now." : "{b}Aunt Diane{/b} is probably asleep... I don't think I can work on the garden right now.",
        
        "I should give {b}Diane{/b} her {b}drink{/b} before I get back to work..." : "I should give {b}Aunt Diane{/b} her {b}drink{/b} before I get back to work...",
        
        "( ... What is she... )" : "( ...{b}Aunt Diane{b}... What is she... )",
        
        "I should find out if {b}Diane{/b} is home first." : "I should find out if {b}Aunt Diane{/b} is home first.",

    
        
        "Talk about {b}[deb_name]{/b}." : "Talk about {b}Mom{/b}.",

    
        
        "Good morning, {b}Diane{/b}." : "Good morning, {b}Aunt Diane{/b}.",
        
        "( Is that {b}Diane{/b} screaming?! )" : "( Is that {b}Aunt Diane{/b} screaming?! )",
        
        "( {b}Diane{/b} is outside by the garden. )" : "( {b}Aunt Diane{/b} is outside by the garden. )",
        
        "( I can't just leave, {b}Diane{/b} might be in trouble. )" : "( I can't just leave, {b}Aunt Diane{/b} might be in trouble. )",
        
        "( {b}Diane{/b} gets a little bit too... Loving, when she has a few drinks. )" : "( {b}Aunt Diane{/b} gets a little bit too... Loving, when she has a few drinks. )",

    
        
        "{b}Diane{/b}?!" : "{b}Aunt Diane{/b}?!",

    
        
        "{b}Diane{/b}!??" : "{b}Aunt Diane{/b}!??",
        
        "It's fine, {b}Diane{/b}." : "It's fine, {b}Aunt Diane{/b}.",
        
        "I'll keep this to myself. Don't worry." : "I won't tell {b}Mom{/b}. Don't worry.",
        
        "I don't know, {b}Diane{/b}." : "I don't know, {b}Aunt Diane{/b}.",
        
        "Sure, {b}Diane{/b}..." : "Sure, {b}Aunt Diane{/b}...",
        
        "That's... really sexy, {b}Diane{/b}." : "That's... really sexy, {b}Aunt Diane{/b}.",
        
        "... And {b}this cow isn't pregnant yet{/b}. Is her {b}bull{/b} ready to {b}breed{/b} her?" : "I guess what I'm trying to say is... {b}Your Aunt{/b} needs a bull to... {b}Breed{/b} her...",
        
        "Breed me, {b}[firstname]{/b}! Claim my womb as yours!" : "...You think you could help your {b}Auntie{/b} with that?",
        
        "You're beautiful, {b}Diane{/b}!" : "You're beautiful, {b}Aunt Diane{/b}!",
        
        "...You think you could help me with that?" : "...You think you could help your {b}Auntie{/b} with that?",
        
        "You're so wet, {b}Diane{/b}." : "You're so wet, {b}Aunt Diane{/b}.",
        
        "Pretty soon I'll have the finest milk in town!" : "Your {b}Aunt{/b} will have some of the finest milk in town!",
        
        "You don't want to keep {b}[deb_name]{/b} waiting!" : "You don't want to keep {b}your Mom{/b} waiting!",
        
        "Don't worry, {b}Diane{/b}, I won't tell anyone." : "Don't worry, {b}Aunt Diane{/b}, I won't tell anyone.",
        
        "But It's getting late and {b}[deb_name]'s{/b} gonna be worried." : "But It's getting late and {b}Mom's{/b} gonna be worried.",

    
        
        "{b}Mr. Johnson{/b}?!" : "{b}DAD{/b}?!",
        
        "I... I missed you, {b}Tammy{/b}..." : "I... wanted to see my only son, {b}Erik{/b}...",
        
        "I've been stopping by at night for the last couple months, hoping to bump into you..." : "I've been stopping by at night for the last couple months, hoping to bump into him...",
        
        "You should have thought about that before leaving me!!" : "You should have thought about that before leaving us!!",
        
        "{b}Mrs. Johnson{/b}... What happens now?" : "{b}Mom{/b}... What happens now?",
        
        "{b}Tammy{/b}!" : "{b}Erik{/b}!",

    
        
        "Sorry, {b}Mrs. Johnson{/b}." : "Sorry about that.",
        
        "Are you sure, {b}Mrs. Johnson{/b}?" : "Are you sure, {b}Mom{/b}?",
        
        "Sorry for keeping you up, {b}Mrs. Johnson{/b}..." : "Sorry for keeping you up, {b}Mom{/b}...",

    
        
        "( Now I just need to get the real guitar out of here without {b}Mrs. Johnson{/b} seeing me. )" : "( Now I just need to get the real guitar out of here without {b}Erik's Mom{/b} seeing me. )",
        
        "Aww, he's such a sweet young man to care about my feelings so much." : "Aww, my {b}Pumpkin{/b} is so sweet to care about {b}his Mommy's{/b} feelings so much!",
        
        "I never understood why that good for nothing ex of mine loved them so much. He wasn't even very good at playing them." : "I never understood why {b}Erik's father{/b} loved them so much. He wasn't even very good at playing them.",
        
        "You don't have to... {b}Mrs. Johnson{/b}." : "You don't have to... {b}Mom{/b}.",
        
        "{b}Mrs. Johnson{/b} Loses" : "{b}Erik's Mom{/b} Loses",
        
        "Yeah, {b}Mr. Johnson{/b} always kept it well stocked." : "Yeah, {b}Dad{/b} always kept it well stocked.",
        
        "But, we all had fun, didn't we?" : "But, we all had fun, didn't we, {b}Mom{/b}?",
        
        "My husband only drank whiskey." : "{b}Your Father{/b} only drank whiskey.",
        
        "{b}Mrs. Johnson{/b} is waiting for us, remember?" : "{b}My Mom{/b} is waiting for us, remember?",
        
        "Oh, {b}Mrs. Johnson{/b} wanted me to clean up the basement." : "Oh, {b}my Mom{/b} wanted me to clean up the basement.",
        
        "{b}Mrs. Johnson{/b} might flip out if things got out of hand..." : "{b}Mom{/b} might flip out if things got out of hand...",
        
        "I wonder if {b}Mrs. Johnson{/b} moved them?" : "I wonder if {b}my Mom{/b} moved them?",
        
        "Would {b}Mrs. Johnson{/b} even be okay with you selling her ex-husbands stuff?" : "Would {b}your Mom{/b} even be okay with you selling {b}your dad's{/b} stuff?",
        
        "Come on, {b}Erik{/b}. These things might have sentimental value to her." : "Come on, {b}Erik{/b}. This was {b}your dad's{/b}.",
        
        "What's so important that you need to sell off her stuff?" : "I know you don't really want to sell it. What's going on?",
        
        "Just remember. You're not going to sell any of {b}Mrs. Johnson{/b}'s things, okay?!" : "Just remember. You're not going to sell any of {b}your dad{/b}'s things, okay?!",
        
        "Plus, {b}Mr. Johnson{/b} was pretty protective of his man cave back when he was living here." : "It used to be {b}my Dad's{/b} man cave back when he was living here.",
        
        "{b}Mrs. Johnson{/b} might get pissed!" : "{b}My Mom{/b} might get pissed!",

    
        
        "Sorry to hear about your {b}Dad{/b}, by the way. How are you holding up?" : "Sorry to hear about your {b}Dad{/b}, by the way... I hope you and your family are doing okay.",
        
        "I'll be alright, man. Thanks for asking!" : "We'll be alright... Thanks for asking...",
        
        "C'mon, {b}Mrs. Johnson{/b}. I told you not to call me that..." : "C'mon, {b}Mom{/b}. I told you not to call me that...",
        
        "Dude, she is so fit! You're so lucky she's letting you rent a room!" : "Dude... {b}Your Mom{/b} is fit!",
        
        "( {b}Erik{/b} probably went out with {b}Mrs. Johnson{/b} somewhere. )" : "( {b}Erik{/b} probably went out with {b}his Mom{/b} somewhere. )",
        
        "( Milfness? Well, I know it's for {b}Mrs. Johnson{/b}. I didn't know she subscribed to these, though... )" : "( {b}Milfness{/b}? Well, I know it's for {b}Erik's Mom{/b}. I didn't know she subscribed to these, though... )",
        
        "( A letter from D?! )" : "( A letter from {b}his Dad{/b}?! I didn't know he was still trying to contact him... )",

    
        
        "Hi, {b}Mrs. Johnson{/b}!" : "Oh, Hi!",
        
        "M...{b}Mrs. Johnson{/b}, are you sure?" : "M...{b}Mom{/b}, are you sure?",
        
        "What do you need, {b}Mrs. Johnson{/b}?" : "What do you need, {b}Mom{/b}?",
        
        "Sorry, {b}Mrs. Johnson{/b}." : "Sorry about that.",
        
        "Okay, {b}Mrs. Johnson{/b}!" : "Okay, {b}Mom{/b}!",
        
        "I can't believe {b}Mrs. Johnson{/b} is okay with having sex with us..." : "I can't believe {b}my Mom{/b} is okay with having sex with us...",
        
        "I'm sure the {b}hospital has the pills Mrs. Johnson{/b} talked about..." : "I'm sure the {b}hospital has the pills your Mom{/b} talked about...",
        
        "Hey, {b}Mrs. Johnson{/b}." : "Hey, {b}Mom{/b}.",
        
        "When should we visit {b}Mrs. Johnson{/b}?" : "When should we visit {b}my Mom{/b}?",
        
        "I... What are doing here?" : "I... What are you doing here?",
        
        "Catching up in school and saving money for tuition." : "Catching up in school and saving money for college in the fall.",
        
        "Oh, it's nothing, {b}Mrs. Johnson{/b}." : "Oh, it's nothing, {b}Mom{/b}.",
        
        "Dude!! I can't believe {b}Mrs. Johnson{/b} is going to play with us." : "Dude!! I can't believe {b}your Mom{/b} is going to play with us.",
        
        "It's pretty embarrassing you had to see my ex husband like that..." : "It's pretty embarrassing you had to see {b}Erik's Father{/b} like that...",
        
        "Do you think you could help your... favorite neighbor??" : "Do you think you could help out {b}your best friend's Mother{/b}??",
        
        "( {b}Erik{/b} sure is lucky he ended up here... )" : "( {b}Erik{/b} sure is lucky to have such a cool {b}Mom{/b}... )",

    
        
        "Did you end up talking to {b}Mrs. Johnson{/b}?" : "Did you end up talking to {b}my Mom{/b}?",
        
        "Did you end up talking to {b}Mrs. Johnson{/b}?" : "Did you end up talking to {b}my Mom{/b}?",
        
        "Was that {b}Mrs. Johnson{/b}?" : "Was that {b}your Mom{/b}?",
        
        "{b}Mrs. Johnson{/b} sent you up here, huh?" : "{b}My Mom{/b} sent you up here, huh?",
        
        "But, can you please not tell {b}Mrs. Johnson{/b} I'm being bullied at school?" : "But, can you please not tell {b}my Mom{/b} I'm being bullied at school?",

    
        
        "No worries, Man. I'm working for {b}[deb_name]'s{/b} friend {b}Diane{/b} now." : "No worries, Man. I'm working for {b}my Aunt Diane{/b} now.",
        
        "I was playing in the basement... But, {b}Mrs. Johnson{/b} must've put them somewhere..." : "I was playing in the basement... But, {b}my Mom{/b} must've put them somewhere...",
        
        "{b}Mrs. Johnson{/b} didn't see it did she? I don't want her freaking out..." : "It's just... {b}My Mom{/b} would freak of she ever found out.",
        
        "Heh, I think she'd be okay with it. She seems really cool!" : "Uhh... You'd be surprised, your {b}Mom{/b} seems pretty cool!",
        
        "I've mentioned having people over to the basement to {b}Mrs. Johnson{/b}." : "I've mentioned having people over to the basement to {b}my Mom{/b}.",

    
        
        "Are you okay, {b}Mrs. Johnson{/b}?" : "Are you gonna be okay?",
        
        "What do you want us to do, {b}Mrs. Johnson{/b}?" : "What do you want us to do, {b}Mom{/b}?",
        
        "Okay, {b}Mrs. Johnson{/b}..." : "Okay, {b}Mom{/b}...",
        
        "{b}Mrs. Johnson{/b}..." : "{b}Mom{/b}...",
        
        "Sorry, {b}Mrs. Johnson{/b}." : "Sorry about that.",
        
        "Are you okay, {b}Mrs. Johnson{/b}?" : "Are you gonna be okay?",
        
        "Come on, we should leave and let {b}Mrs. Johnson{/b} rest." : "Come on, we should leave and let {b}Mom{/b} rest.",
        
        "Yeah, {b}Mrs. Johnson{/b} is awesome..." : "Yeah, {b}your Mom{/b} is awesome...",
    }

    incestPatchChanged2 = {
    
        
        "Hey, {b}[deb_name]{/b}." : "Hey, {b}Mom{/b}.",
        
        "{b}[deb_name]{/b}?" : "{b}Mom{/b}?",
        
        "{b}[deb_name]{/b}, I'm gonna..." : "{b}Mom{/b}, I'm gonna...",
        
        "I know {b}[deb_name]{/b} said not to worry about this..." : "I know {b}Mom{/b} said not to worry about this...",
        
        "{b}[deb_name]{/b}, this is {b}Roxxy{/b}." : "{b}Mom{/b}, this is {b}Roxxy{/b}.",
        
        "Thanks, {b}[deb_name]{/b}!" : "Thanks, {b}Mom{/b}!",
        
        "Your landlady is really nice..." : "Your {b}Mom{/b} is really nice...",
        
        "Hey, {b}[deb_name]{/b}." : "Hey, {b}Mom{/b}.",
        
        "Thanks, {b}[deb_name]{/b}." : "Thanks, {b}Mom{/b}.",
        
        "Does your {b}Landlady{/b} ever wear clothes?" : "Does your {b}Mom{/b} ever wear clothes?",

    
        
        "I'm fine, {b}[deb_name]{/b}. The nurse said I just had a small concussion." : "I'm fine, {b}Mom{/b}. The nurse said I just had a small concussion.",
        
        "Everything is fine. I'll be okay, {b}[deb_name]{/b}." : "Everything is fine. I'll be okay, {b}Mom{/b}.",
        
        "Your stupid school didn't even call to let me know you were in the hospital!" : "I didn't even know you'd gone to the hospital!",
        
        "I had to hear about it from {b}Tammy{/b}!" : "Oh, I'm the worst {b}Mother{/b} in the world!",
        
        "{b}[deb_name]{/b}, it's alright. I'm really fine! Calm down." : "{b}Mom{/b}, it's alright. I'm really fine! Calm down.",
        
        "I'm sorry... I was just so worried about you!" : "I left the house this morning and when I got back I realized you still weren't home yet!",
        
        "Your {b}Father{/b} is counting on me to watch over you!" : "Then {b}Tammy{/b} stopped over and...",
        
        "I'm so happy to see you're okay, {b}[firstname]{/b}." : "when I saw {b}your Mother{/b} was home, I came over and filled her in on your scuffle at school.",
        
        "I came over here to fill {b}[deb_name]{/b} in the second {b}Erik{/b} called me." : "I told her you were on your way back from the hospital with {b}Erik{/b}.",
        
        "I know {b}[deb_name]{/b}..." : "I know {b}Mom{/b}...",
        
        "{b}Your father{/b} would just throw a fit if he knew I let this happen." : "I love you.",
        
        "It's alright, {b}[deb_name]{/b}." : "I love you too, {b}Mom{/b}. But seriously, I'm fine.",
        
        "I'm so happy to hear {b}[firstname]{/b} visited our local church lately..." : "I'm so happy to hear {b}my son{/b} visited our local church lately...",
        
        "It's always a pleasure to hear that {b}[firstname]{/b} is actively involved with the church." : "It's always a pleasure to hear that {b}my son{/b} is actively involved with the church.",
        
        "( Is that {b}[deb_name]{/b} on the phone? )" : "( Is that {b}Mom{/b} on the phone? )",
        
        "Morning, {b}[deb_name]{/b}." : "Morning, {b}Mom{/b}.",
        
        "Hello, {b}[deb_name]{/b}." : "Hello, {b}Mom{/b}.",
        
        "Housework mostly. It keeps me pretty busy." : "Well...there's plenty of housework to keep me busy.",
        
        "It's not easy taking care of this big place by myself you know?" : "Especially, now that {b}your dad{/b} isn't here to help me.",
        
        "I could help, you know?" : "I could help you, {b}Mom{/b}.",
        
        "You want to help with the house work?" : "Around the house?",
        
        "Sure! I mean, I feel like I should pull my own weight around here..." : "Sure! I don't mind.",
        
        "That's a great attitude to have, {b}[firstname]{/b}!" : "That's really sweet!",
        
        "Be careful!" : "Be careful, Sweetie!",
        
        "I'm sorry. I was just trying to help {b}[deb_name]{/b}." : "I'm sorry. I was just trying to help {b}Mom{/b}.",
        
        "So what, you're going to start doing chores around here now?" : "What's with you and doing things around the house all of a sudden?",
        
        "You got a thing for {b}[deb_name]{/b} or something?" : "Are you trying to be {b}Mommy's special boy{/b} or something?",
        
        "Pfft, don't play dumb! I see what you're up to!" : "Don't act stupid! I know what you're doing!",
        
        "What's her problem?" : "What's with her lately? She's so tense all the time...",
        
        "Where's the owner of this residence?" : "Where's your {b}Mother{/b}?",
        
        "My boss aint the patient type." : "My boss ain't the patient type.",
        
        "{b}[deb_name]{/b}?" : "{b}Mom{/b}?",
        
        "{b}[jen_name]{/b} and I need your help." : "{b}Your sister's{/b} been freaking out all morning.",
        
        "I can't afford to call a repairman right now. Not with everything that's happened recently..." : "I was going to call a repairman but... you know, with our money situation and all...",
        
        "Y-yeah, okay. That sounds nice, {b}[deb_name]{/b}." : "Y-yeah, okay. That sounds nice, {b}Mom{/b}.",
        
        "Hey {b}[deb_name]{/b}!" : "Hey {b}Mom{/b}!",
        
        "Heh, sheesh {b}[deb_name]{/b}! Alright, I'll go." : "Sheesh {b}Mom{/b}! Alright, I'll go.",
        
        "Sorry {b}[deb_name]{/b}, I have something else planned for today..." : "Sorry {b}Mom{/b}, I have something else planned for today...",
        
        "I wonder if {b}[deb_name]{/b} would let me kiss her again if I asked?" : "I wonder if I'd be able to kiss {b}Mom{/b} again.",
        
        "I should {b}talk to her{/b} about it..." : "I should probably find a way to {b}ask her{/b} about it...",
        
        "Morning, {b}[deb_name]{/b}." : "Morning, {b}Mom{/b}.",
        
        "Is that so? What kind of weird dreams?" : "Oh? What kind of weird dreams?",
        
        "( I can't believe {b}[deb_name]{/b} actually rubbed my Cock! )" : "( I can't believe {b}Mom{/b} actually rubbed my cock! )",
        
        "( Hmm, sounds like {b}[deb_name]{/b} is talking to someone in the kitchen... )" : "( Hmm, sounds like {b}Mom{/b} is talking to someone in the kitchen... )",
        
        "Sorry, {b}[deb_name]{/b}." : "Sorry, {b}Mom{/b}.",
        
        "It's okay, {b}[deb_name]{/b}." : "It's okay, {b}Mom{/b}.",
        
        "( That porno {b}[jen_name]{/b} was watching was hot! I kind of feel like watching it, too... )" : "( That porno {b}Sis{/b} was watching was hot! I kind of feel like watching it, too... )",
        
        "Sure thing, {b}[deb_name]{/b}!" : "Sure thing, {b}Mom{/b}!",
        
        "Hey {b}Roxxy{/b}! You here for your session with {b}[jen_name]{/b}?" : "Hey {b}Roxxy{/b}! You here for your session with {b}my Sister{/b}?",
        
        "C'mon, {b}Roxxy{/b}. We can ditch the dweeb and get started in my room." : "C'mon, {b}Roxxy{/b}. We can ditch my dweeb of a {b}brother{/b} and get started in my room.",
        
        "{b}[jen_name]{/b} is helping somebody?" : "{b}Your sister{/b} is helping somebody? On purpose?",
        
        "Sure thing, {b}[deb_name]{/b}!" : "Sure thing, {b}Mom{/b}!",
        
        "Hey {b}Roxxy{/b}! You here for your session with {b}[jen_name]{/b}?" : "Hey {b}Roxxy{/b}! You here for your session with {b}my Sister{/b}?",
        
        "{b}[jen_name]{/b} is helping somebody?" : "{b}Your sister{/b} is helping somebody? On purpose?",
        
        "I should go check on {b}Roxxy{/b} and {b}[jen_name]{/b}..." : "I should go check on {b}Roxxy{/b} and {b}my Sister{/b}...",

    
        
        "{b}[deb_name]{/b} used to love painting farm animals..." : "{b}Mom{/b} used to love painting farm animals...",

    
        
        "{b}[deb_name]{/b}." : "{b}Mom{/b}.",

    
        
        "( {b}[jen_name]'s{/b} a camgirl?! )" : "( {b}My sister's{/b} a camgirl?! )",
        
        "( It's so weird seeing her like that... )" : "( I'm not sure how to feel about this... It's so weird seeing her like that...)",
        
        "( Man, she is so hot... )" : "( Man, I know I shouldn't find this hot, but... )",

    
        
        "Huh? {b}[deb_name]{/b}? What time is it?" : "Huh? {b}Mom{/b}? What time is it?",
        
        "{b}Mrs. Johnson{/b}? For me?" : "{b}Erik's Mom{/b} is here? For me?",
        
        "I have no idea why she's here either, {b}[deb_name]{/b}." : "Not that I know of, {b}Mom{/b}.",
        
        "Good morning, {b}[deb_name]{/b}." : "Good morning, {b}Mom{/b}.",
        
        "( Is that {b}[deb_name]{/b} on the phone? )" : "( Is that {b}Mom{/b} on the phone? )",
        
        "I hope {b}[deb_name]{/b} isn't upset with me..." : "I hope {b}Mom{/b} isn't upset with me...",
        
        "( {b}[deb_name]{/b}'s nipples taste so good... )" : "( {b}Mom{/b}'s nipples taste so good... )",
        
        "I wonder if {b}[deb_name]{/b} needs help around the house." : "I wonder if {b}Mom{/b} needs help around the house.",
        
        "I wonder if {b}[deb_name]{/b} needs my help with anything else..." : "I wonder if {b}Mom{/b} needs my help with anything else...",
        
        "( {b}[deb_name]{/b} really seemed to be enjoying that massage. )" : "( {b}Mom{/b} really seemed to be enjoying that massage. )",
        
        "I keep having naughty dreams involving {b}[deb_name]{/b}." : "I keep having naughty dreams involving {b}Mom{/b}.",
        
        "( I should really go check on {b}[deb_name]{/b}... )" : "( I should really go check on {b}Mom{/b}... )",
        
        "... {b}[deb_name]{/b} is so beautiful." : "... {b}Mom{/b} is so beautiful.",
        
        "Oh, {b}[deb_name]{/b}..." : "Oh, {b}Mom{/b}...",
        
        "... {b}[deb_name]{/b}?" : "... {b}Mom{/b}?",
        
        "I love you, {b}[deb_name]{/b}!" : "I love you, {b}Mom{/b}!",
        
        "{b}[deb_name]{/b}?" : "{b}Mom{/b}?",
        
        "{b}[deb_name]{/b}?" : "{b}Mom{/b}?",
        
        "{b}[deb_name]{/b}..." : "{b}Mom{/b}...",
        
        "... {b}[deb_name]{/b}?" : "... {b}Mom{/b}?",
        
        "Shh, we don't want to wake {b}[jen_name]{/b}!" : "Shh, we don't want to wake {b}your sister{/b}!",
        
        "It's alright, you're just excited. I'm excited too!" : "It's alright, you're just excited. {b}Mommy{/b} is excited too!",
        
        "I could hardly wait for {b}[jen_name]{/b} to get in bed." : "I could hardly wait for {b}your sister{/b} to get in bed.",
        
        "Oh wow, {b}[deb_name]{/b}, you're sopping wet!" : "Oh wow, {b}Mom{/b}, you're sopping wet!",
        
        "Now, let's not waste time... Give it to me, Sweetie!" : "Now, let's not waste time... Give it to {b}Mommy{/b}!",
        
        "You like it when I squeeze you with my pussy?" : "You like it when {b}Mommy{/b} squeezes you with her pussy?",
        
        "That's it, Baby! Fuck my pussy!" : "That's it, {b}Baby{/b}! Fuck {b}Mommy{/b}'s pussy!",
        
        "Oh yeah, {b}[deb_name]{/b}!" : "Oh yeah, {b}Mom{/b}!",
        
        "Who's my naughty boy?" : "Who's {b}Mommy's Naughty Boy{/b}?",
        
        "That's right, Baby! Fuck me harder!" : "That's right, {b}Baby{/b}! Fuck {b}Mommy{/b} harder!",
        
        "Uuhh!! You like this hard cock, {b}[deb_name]{/b}?" : "Uuhh!! You like this hard cock, {b}Mom{/b}?",
        
        "{b}[deb_name]{/b}, I'm gonna..." : "{b}Mom{/b}, I'm gonna...",
        
        "I love you too, {b}[deb_name]{/b}. You're the best!" : "I love you too, {b}Mom{/b}. You're the best!",
        
        "Wake up, {b}[deb_name]{/b}." : "Wake up, {b}Mom{/b}.",
        
        "I love you too, {b}[deb_name]{/b}!" : "I love you too, {b}Mom{/b}!",
        
        "Hmm, {b}[deb_name]{/b} must have woken before me and snuck out..." : "Hmm, {b}Mom{/b} must have woken before me and snuck out...",
        
        "... Did {b}[deb_name]{/b} leave that?" : "... Did {b}Mom{/b} leave that?",
        
        "( {b}[deb_name]{/b} needs help with the laundry? )" : "( {b}Mom{/b} needs help with the laundry? )",

    
        
        "( {b}Mrs. Johnson's{/b} yoga mat is there... )" : "( {b}Erik's Mom's{/b} yoga mat is there... )",
        
        "( {b}Mrs. Johnson's{/b} yoga mat is there... )" : "( {b}Erik's Mom's{/b} yoga mat is there... )",
        
        "( {b}Mrs. Johnson{/b} is so... flexible... )" : "( {b}Erik's Mom{/b} is so... flexible... )",
        
        "( {b}Mrs. Johnson{/b} is always doing yoga... )" : "( {b}Erik's Mom{/b} is always doing yoga... )",
        
        "( {b}Mrs. Johnson{/b} left her yoga mat outside. )" : "( {b}Erik's Mom{/b} left her yoga mat outside. )",

    
        
        "I can't enjoy myself?" : "Your {b}big sister{/b} can't enjoy herself?",

    
        
        "Something smells good." : "Do you smell that? {b}Mom's{/b} cooking!",
        
        "Uhh, Yeah. It's probably the breakfast that's waiting for you {b}downstairs{/b}, dummy." : "Duh! {b}Mom{/b} made breakfast. She's {b}downstairs{/b} waiting for you.",
        
        "I can't believe she's still making you breakfast everyday. It's been over a month since {b}your dad{/b} died." : "You'd know, if you were actually on time for once.",
        
        "Yeah, she's a nice lady." : "Perfect! I was just on my way actually...",
        
        "Ugh, yeah. Too nice if you ask me." : "Ugh. What have I done to deserve a {b}younger brother{/b} like you...",
        
        "If you go through my things again, I'm telling {b}[deb_name]{/b}." : "If touch my computer again, I'm telling {b}Mom{/b}.",
        
        "Meeting with {b}[deb_name]{/b} in her room, perhaps?" : "Meeting with {b}Mom{/b} in her room, perhaps?",
        
        "You've been sucking up to {b}[deb_name]{/b} a lot lately." : "You've been sucking up to {b}Mom{/b} a lot lately.",
        
        "Well, {b}[deb_name]{/b} needs help around the house so I'm-" : "Well, {b}Mom{/b} needs help around the house so I'm-",
        
        "Look, I don't care what you and {b}[deb_name]{/b} do in secret." : "Look, I don't care what you and {b}Mom{/b} do in secret.",
        
        "I can't let you get distracted by {b}[deb_name]{/b}." : "I can't let you get distracted by {b}Mom{/b}.",
        
        "( There are voices coming from {b}[jen_name]'s{/b} room... )" : "( There are voices coming from {b}my Sister's{/b} room... )",
        
        "Hey, {b}[deb_name]{/b}." : "Hey, {b}Mom{/b}.",
        
        "... But I'm used to it. I've had trouble sleeping since my husband left many years ago." : "... But I'm used to it. I've had trouble sleeping since I found out about {b}your Dad's{/b} gambling many years ago.",
        
        "I understand what you're going through." : "I'm sorry, I didn't think you'd care about any of this.",
        
        "Yeah. I miss your {b}Dad{/b} too." : "But I should have known better, you're the best {b}son{/b} I could ever ask for.",
        
        "We were friends for a long time, you know?" : "And of course I miss {b}your Father{/b} too. It's the worst at night, in the dark...",
        
        "At least I have you now..." : "But I still have {b}you{/b}...",
        
        "You don't mind me sleeping in your bed?" : "You don't mind me sleeping in your bed? It's been since I was little...",
        
        "I think it could do us some good..." : "Of course not! I think it could do us some good...",
        
        "...Okay. Sure, {b}[deb_name]{/b}." : "...Okay. Sure, {b}Mom{/b}.",
        
        "Hey {b}[deb_name]{/b}, what's up?" : "Hey {b}Mom{/b}, what's up?",

    
        
        "( I wonder if it's {b}[deb_name]{/b}. )" : "( I wonder if it's {b}Mom{/b}. )",
        
        "( That small trap door is {b}locked{/b}. )" : "( The hatch to the attic is {b}locked{/b}. )",

    
        
        "Fix it obviously! You're the only man around here after all!" : "Get your ass in gear and fix it you idiot! Or is my {b}little brother{/b} not man enough to turn a wrench that isn't in his boxers?",
        
        "Well you're living in a house with girls now which means you need to learn how to fix these kinda things!" : "Well you're the only one in the house without {b}tits{/b}, so sac up and find a solution, quick!",
        
        "I'm sorry, {b}[jen_name]{/b}. I was just-" : "Well, you're the one put {b}tits{/b} on my mind, and that comment was more than just a little sexist, don't you thin-",
        
        "If you're going to stare, at least be a man about it!" : "I know you're always looking at me {b}that way{/b}.",
        
        "Denying it or making excuses just makes you look like a wimp." : "Isn't this what you've always wanted since I started wearing a bra?",
        
        "No one wants to be checked out by a spineless little wimp!" : "To see what {b}these{/b} look like... under my shirt?",
        
        "If you had gotten up here to deal with this pipe situation sooner, perhaps I'd be in a better mood." : "Well, I wouldn’t be all {b}wet{/b}, if you'd shown up earlier!",
        
        "That little loser has a thing for me!" : "{b}Little brother{/b} has a thing for me!",
        
        "( {b}[deb_name]{/b}'s body looks real good but I don't want to peek at her too long... )" : "( {b}Mom{/b}'s body looks real good but I don't want to peek at her too long... )",
        
        "( {b}[deb_name]'s{/b} in the shower! )" : "( {b}Mom's{/b} in the shower! )",
        
        "I can't believe I'm living with this beautiful woman now!" : "I can't believe I just saw {b}Mom{/b} naked like that.",
        
        "... It's a shame she only sees me as my {b}Father{/b}'s kid." : "...Maybe it's wrong to think this way but... She's very pretty.",
        
        "( She would probably get mad but what if she's ok with it? )" : "( {b}Mom{/b} would probably get mad... but what if she's OK with it? )",
        
        "Sorry, {b}[deb_name]{/b}! I didn't think anyone was in here!" : "Oh, crap! Sorry, {b}Mom{/b}! I didn't think anyone was in here!",
        
        "The kissing..." : "Ever since the kissing he's been so... attached!",
        
        "( I hope she isn't too mad at me. )" : "( I hope {b}Mom{/b} won't be mad at me. )",
        
        "I love showering with you, {b}[deb_name]{/b}" : "I love showering with you, {b}Mom{/b}",
        
        "{b}[deb_name]{/b}, I'm gonna..." : "{b}Mom{/b}, I'm gonna...",
        
        "How do you always know exactly where to rub?" : "Where did you learn to do {b}that{/b} with your fingers?",
        
        "How about a special treat?" : "Just stay still and let {b}Mommy{/b} take care of this.",
        
        "Sorry, {b}[deb_name]{/b}." : "Sorry, {b}Mom{/b}.",
        
        "I love the taste!" : "I kind of missed the taste of it.",
        
        "Heheh, look at the mess you made of my face!" : "Wow... It came out so fast!",
        
        "Sorry, {b}[deb_name]{/b}." : "Sorry, {b}Mom{/b}.",
        
        "I'll finish you off with my hand." : "Why don't you let {b}Mommy{/b} finish you off with her hand?",
        
        "{b}[deb_name]{/b}..." : "{b}Mom{/b}...",
        
        "Can I put it inside you?" : "Can I put it... in?",
        
        "{b}[deb_name]{/b}, I want to do it with you." : "{b}Mom{/b}, I want to do it with you.",
        
        "Hold my leg and give me that big cock!" : "Hold {b}Mommy's{/b} leg and give me that big cock!",
        
        "{b}[deb_name]{/b}, I want you." : "{b}Mom{/b}, I want you.",
        
        "Cum for me!{p=2}{nw}" : "Cum for {b}Mommy{/b}!{p=2}{nw}",
        
        "{b}[deb_name]{/b}, I love you!{p=2}{nw}" : "{b}Mom{/b}, I love you!{p=2}{nw}",
        
        "Cum deep inside me!" : "Cum in {b}your Mommy{/b}!",
        
        "God, I love this cock of yours!" : "You really had a lot in you!",
        
        "Hehe, I'm pretty sure it feels the same way about you..." : "It's 'cause your pussy felt so good, {b}Mom{/b}.",
        
        "Hold on to me for a second. My legs are a little wobbly after all that!" : "Hold on to {b}Mommy{/b} for a second. My legs are a little wobbly after all... that!",
        
        "We'll do this again, okay?" : "I'm looking forward to our... next session.",
        
        "Make sure {b}[jen_name]{/b} doesn't see you leave the bathroom, okay?" : "Make sure {b}your sister{/b} doesn't see you leave the bathroom, okay?",
        
        "I hope {b}[jen_name]{/b} didn't hear us..." : "I hope {b}your sister{/b} didn't hear us...",
        
        "I doubt it. Not with the shower running..." : "Why? Would that stop you?",
        
        "... Yeah, I suppose I'm worrying too much." : "...Probably not.",
        
        "I should get downstairs and start cooking dinner..." : "I like your cock too much.",
        
        "Fetch me a towel?" : "Go and grab me a towel.",
        
        "Sure thing, {b}[deb_name]{/b}!" : "Sure thing, {b}Mom{/b}!",
        
        "( {b}[jen_name]{/b} is in the shower... )" : "( {b}Sis{/b} is in the shower... )",
        
        "Oh shit! {b}[jen_name]{/b} is in the shower..." : "Oh shit! {b}My sister{/b} is in the shower...",
        
        "Sorry! I didn't see you..." : "Sorry, {b}Sis{/b}! I didn't see you...",
        
        "More like me helping myself, while a perverted idiot watches..." : "More like me helping myself, while my perverted {b}little brother{/b} watches...",
        
        "Maybe later... if you treat me a little better..." : "Maybe later... if you treat your {b}older sister{/b} a little better...",
        
        "Maybe later... if you treat me a little better..." : "Maybe later... if you treat your {b}older sister{/b} a little better...",
        
        "I want you, {b}[jen_name]{/b}!!!" : "Sorry {b}Sis{/b}, I just want you so bad!!!",
        
        "You just kept shooting cum deep inside!!" : "You just kept shooting your cum in me!! And your {b}cock is so big{/b}, so it's really in there deep!!",

    
        
        "Wash [deb_name]." : "Wash {b}Mom{/b}.",
        
        "Finger {b}[deb_name]{/b}." : "Finger {b}Mom{/b}.",

    
        
        "Leave me alone, already! Why don't you just pester {b}[deb_name]{/b} for some of her panties, pervert!" : "Leave me alone, already! Why don't you just pester {b}Mom{/b} for some of her panties, pervert!",
        
        "Unless you want {b}[deb_name]{/b} to know about you stealing from me." : "Unless you want {b}Mom{/b} to know about you stealing from me?",
        
        "Listen, {b}[jen_name]{/b}! I really need this!" : "Come on, {b}Sis{/b}! I really need this!",
        
        "{b}Diane{/b}?" : "{b}Aunt Diane{/b}?",
        
        "I wouldn't want a pervert spying on me." : "I wouldn't want my pervert {b}little brother{/b} spying on me.",
        
        "Umm... Actually, {b}[deb_name]{/b} needs to..." : "Umm... Actually, {b}Mom{/b} needs to...",
        
        "Just don't touch anything, and leave my room..." : "Just don't touch anything. In fact, get out of my room...",
        
        "Though, there's always {b}[firstname]{/b}." : "Though, my {b}little brother{/b} is right down the hall...",
        
        "Don't yell! You're gonna wake up {b}[deb_name]{/b}..." : "Don't yell! You're gonna wake up {b}Mom{/b}...",
        
        "Don't yell! You're gonna wake up {b}[deb_name]{/b}..." : "Don't yell! You're gonna wake up {b}Mom{/b}...",
        
        "( Woah, they're huge... )" : "( Woah, {b}my Sister's{/b} tits are huge... )",
        
        "Don't yell! You're gonna wake up {b}[deb_name]{/b}..." : "Don't yell! You're gonna wake up {b}Mom{/b}...",
        
        "I want you, {b}[jen_name]{/b}!!!" : "Sorry {b}Sis{/b}, I just want you so bad!!!",
        
        "Don't yell! You're gonna wake up {b}[deb_name]{/b}..." : "Don't yell! You're gonna wake up {b}Mom{/b}...",
        
        "Don't lie! I felt it, it just kept shooting deep inside me!" : "Don't lie! I felt {b}your cock{/b} twitching as your pumped your cum inside me!",
        
        "( She's been staying here and doing nothing for so long... )" : "( She's been staying home and doing nothing for so long... )",
        
        "( I never knew {b}[jen_name]{/b} was THAT {b}horny{/b}... )" : "( I never knew {b}my Sister{/b} was THAT {b}horny{/b}... )",
        
        "( So many things I didn't know {b}[jen_name]{/b} was into... )" : "( So many things I didn't know {b}my Sister{/b} was into... )",
        
        "Is this some girl you're trying to bang?" : "Is this some girl you're trying to bang, {b}little brother{/b}?",
        
        "Hahahaha, good one {b}[firstname]{/b}!" : "Hahahaha, good one {b}little brother{/b}!",
        
        "Thanks again for letting me borrow your old uniform." : "Thanks again for letting me borrow your old high school uniform.",
        
        "It looks like your tits are gonna spill out, like any second..." : "It looks like your tits are gonna fall out, like any second...",
        
        "I can see why that dweeb downstairs wants to hit that." : "I can see why my dweeby {b}little brother{/b} wants to hit that.",
        
        "I can't believe you two live together!" : "I can't believe you two are related!",
        
        "We do live together after all." : "We grew up together in the same house.",
        
        "I tell everybody he's the maintenance boy..." : "I tell everybody he was adopted...",
        
        "Thanks again for letting me borrow your old uniform." : "Thanks again for letting me borrow your old high school uniform.",
        
        "It looks like your tits are gonna spill out, like any second..." : "It looks like your tits are gonna fall out, like any second...",
        
        "It must be annoying living with some random dude..." : "It must be annoying having a little brother...",
        
        "Lucky for him, you aren't interested, huh?" : "It's lucky for him you're siblings then, huh?",
        
        "Listen, you idiot." : "Listen, you idiot; I'm fine, and we're NOT friends.",
        
        "I'm fine, and we're NOT friends." : "We're {b}siblings{/b}, and you're a {b}pervert{/b}. All cleared up?",

    
        
        "I don't know If I have time, {b}[deb_name]{/b}." : "I don't know If I have time, {b}Mom{/b}.",
        
        "Thanks, {b}[deb_name]{/b} but I'm not really hungry and I'm running late for school. So..." : "Thanks, {b}Mom{/b} but I'm not really hungry and I'm running late for school. So...",
        
        "Yeah, thanks anyways, {b}[deb_name]{/b}!" : "Yeah, thanks anyways, {b}Mom{/b}!",
        
        "I spoke with my friend {b}Diane{/b} yesterday and she mentioned that she could use some {b}help with her garden{/b} over the summer!" : "I spoke with {b}Aunt Diane{/b} yesterday and she mentioned that she could use someone to {b}help with cleaning her garden{/b} over the summer!",
        
        "Hmm, I don't really know much about gardening {b}[deb_name]{/b}..." : "Hmm, I don't really know much about gardening {b}Mom{/b}...",
        
        "Oh c'mon, It's easy! {b}Diane{/b} can teach you and if you do a good job she'll pay you as well!" : "Oh c'mon, It's easy! Your {b}Aunt Diane{/b} can teach you and if you do a good job she'll pay you as well!",
        
        "Atta' boy!" : "That's my boy!",
        
        "You'll get through this. I promise things will get better." : "We'll get through this. I promise things will get better.",
        
        "Yeah, I-I know. Thanks {b}[deb_name]{/b}..." : "Yeah, I-I know. Thanks {b}Mom{/b}...",
        
        "Chin up, Sweetie! I'm here for you." : "Oh, I love you Sweetie!",
        
        "My friend {b}Diane{/b} is coming over for dinner tonight." : "{b}Diane’s{/b} going to be coming over tonight. I don't know why, but she was very persistent about it.",
        
        "Oh, {b}Diane{/b} is coming over? That's a nice surprise!" : "Oh, {b}Aunt Diane{/b} is coming over? That's a nice surprise!",
        
        "I worry about her sometimes... All alone over there." : "The family hasn’t been together since the funeral, either.",
        
        "Of course, {b}[deb_name]{/b}. What do you need?" : "Of course, {b}Mom{/b}. What do you need?",
        
        "I have a new outfit for dinner tonight and I wanted to get your opinion." : "I want you to tell me what you think of the outfit I plan on wearing to dinner with your {b}Aunt Diane{/b}.",
        
        "I'm excited to see {b}[deb_name]{/b} all dressed up!" : "{b}Mom{/b} hasn't dressed up for an occasion in a long time...",
        
        "Hey, {b}[deb_name]{/b}. I have the {b}fish{/b} you wanted." : "Hey, {b}Mom{/b}. I have the {b}fish{/b} you wanted.",
        
        "I'll let you know when it's finished, okay?" : "You can join us in the dining room when it's done. {b}Aunt Diane{/b} would really like to see you.",
        
        "I know how to treat my girl right!" : "I know how to treat my {b}twin sister{/b} right!",
        
        "Hey, {b}Diane{/b}." : "Hey, {b}Aunt Diane{/b}.",
        
        "Oh stop it, you!" : "{b}Your son{/b} really knows how to greet a lady!",
        
        "He's quite the little charmer isn't he?" : "Well, he's always been a charmer...",
        
        "I don't know how you manage to keep your hands off him!" : "Well thank you, Handsome!",
        
        "Where's your other tenant? She going to join us tonight or did she have a Bitches of Summerville meeting to attend?" : "Will {b}your sister{/b} and her sparkling personality be joining us tonight?",
        
        "No, she's gonna eat with us." : "She's getting ready, I think.",
        
        "... She's just upstairs getting ready." : "She's always in her room. She comes down at the last minute to eat...",
        
        "Typical princess..." : "Still a princess, I see.",
        
        "She's not as bad as you make her out to be..." : "She {b}is{/b} your only niece, after all.",
        
        "Heh, if you say so." : "Oh, I'm just teasing, {b}Sis{/b}. Of course {b}Auntie Diane{/b} loves her {b}only niece{/b}, \"The Princess\".",
        
        "{b}[deb_name]{/b}'s cooking smells delicious!" : "{b}Mom{/b}'s cooking smells delicious!",
        
        "I had no idea he was involved in any of this!" : "I had no idea {b}my husband{/b} was involved in any of this!",
        
        "...{b}[deb_name]{/b}?" : "...{b}Mom{/b}?",
        
        "Your {b}Father{/b} wouldn't want that, Sweetheart." : "This is not your problem Sweetheart.",
        
        "You need to keep your focus on school and {b}Save your money for tuition{/b}." : "You need to focus on school and {b}save your money for college{/b}.",
        
        "Yeah, but {b}[deb_name]{/b}, I can help..." : "Yeah, but {b}Mom{/b}, I can help...",
        
        "Just let me handle it and everything will be fine, okay? I promise." : "{b}Mommy{/b} will handle it. I promise.",
        
        "That's not surprising, he just lost the only family he ever had..." : "Well that's not surprising, he's your only son and he just lost his {b}Father{/b}!",
        
        "He probably just needs someone he can feel close with..." : "He probably feels like he needs to protect you...",
        
        "Especially with all this other stuff that's been happening to you guys." : "Especially after all that's been happening with you guys.",
        
        "It's not that. There's more to it! It's the way he looks at me, you know?" : "It's not that... I feel like there's more to it, the way he looks at me you know?",
        
        "{b}Diane{/b}, he's just a kid!" : "{b}Diane{/b}, he's also {b}my son{/b}!",
        
        "Pfft, he's in college!" : "So wait, that means you guys haven't had sex?",
        
        "Yeah, but I'm old enough to be his {b}Mother{/b}!" : "No!! Of course not...",
        
        "... But {b}you aren't{/b} his {b}Mother{/b}, {b}[deb_name]{/b}!" : "You could, you know...",
        
        "I think you should relax and enjoy it a little. Who care's about the age difference?" : "I think you should relax and let go! Enjoy the intimacy with {b}your son{/b}!",
        
        "Nope. I don't see the harm in it!" : "You both seem to be enjoying it... Where's the harm in that?",
        
        "Plus this is all really {b}HOT{/b}!" : "If he's going to learn it from somewhere, might as learn it at home! Haha!",
        
        "... Because you know I'm right! Just give it a chance. Who know's maybe it was meant to be?" : "Just see how it goes. Maybe it's just a phase that he'll grow out of.",
        
        "Yeah, I suppose anything is possible..." : "You might be right...",
        
        "Good luck, Honey." : "Good luck, {b}Sis{/b}. Love you!",
        
        "( {b}[deb_name]{/b} seemed really conflicted about all of this... )" : "( {b}Mom{/b} seemed really conflicted about all of this... )",
        
        "( Either way, I'm glad {b}Diane{/b} thinks it's okay for us to be doing these things! )" : "( Either way, I'm glad {b}Aunt Diane{/b} thinks it's okay for us to be doing these things! )",
        
        "Aww, c'mon {b}[deb_name]{/b}!" : "Aww, c'mon {b}Mom{/b}!",
        
        "I would really appreciate it, {b}[deb_name]{/b}." : "I would really appreciate it, {b}Mom{/b}.",
        
        "It's just a little something I picked up awhile back..." : "It's a trick I picked up awhile back. {b}Your Father{/b} loved it too!",
        
        "{b}[deb_name]{/b}?" : "{b}Mom{/b}?",
        
        "Really? Thanks {b}[deb_name]{/b}!" : "Really? Thanks {b}Mom{/b}!",
        
        "Sorry, {b}[deb_name]{/b}." : "Sorry, {b}Mom{/b}.",
        
        "Thanks {b}[deb_name]{/b}!" : "Thanks {b}Mom{/b}!",
        
        "Hey, {b}[deb_name]{/b}!" : "Hey, {b}Mom{/b}!",

    
        
        "I really want you, right now!" : "...Or do you want more from {b}Mommy{/b}?",
        
        "I want it so bad!" : "{b}Mommy{/b} wants to feel your fingers.",
        
        "I want to feel you inside of me!" : "{b}Mommy{/b} wants you to slide your fingers...inside...",
        
        "Hahaha! I just don't know what I'm going to do with you, {b}Diane{/b}!" : "Ha ha ha! What are you doing?",
        
        "Hmm, well I have a few suggestions..." : "What? You're too big to hug your {b}twin sister{/b}?",
        
        "I bet you do!" : "Of course not!",
        
        "You know, it's no wonder {b}[firstname]{/b} wants you so badly... You've kept yourself in great shape, {b}[deb_name]{/b}!" : "You know, sometimes I forget your boobs are as big as mine!",
        
        "... Yeah, I've been pretty fortunate! The housework helps but I think it's mostly just good genes." : "I don't know about that! I think yours are bigger!",
        
        "Your breasts are looking amazing by the way! Is that a result of your new business venture?" : "Although, it's probably all to do with your little side business.",
        
        "Tsk... You're relentless, you know that?" : "You're incorrigible, {b}Sis{/b}. Always have been.",
        
        "It's not my fault! You're the one who got me all horned up with those stories of you and your new boy toy!" : "It's not my fault! You're the one who got me all horned up with those stories of {b}your son and his huge dick{/b}!",
        
        "How's that going by the way?" : "This is fun.",
        
        "Any new developments?" : "I haven't skinny dipped in a long time.",
        
        "I want all the details!" : "Not since we tag teamed your hubbie and my first husband down at Pebble Beach, remember?",
        
        "... I still haven't decided if I want to take things further." : "Oh, that was fun... God, after you passed out they both went at me for hours before they were spent. I walked funny for two days after that.",
        
        "Don't get me wrong, It's been really tempting! I miss sex, so much..." : "God, I miss sex...",
        
        "It's so much better than regular masturbation! I think it's the taboo associated with it..." : "But don't worry. Now that you're single, maybe we can get the ol' band back to together?",
        
        "It's a bad idea, {b}Diane{/b}." : "It's a bad idea, {b}Diane{/b}. He's {b}my son{/b} for Christ's sake!",
        
        "You don't know that for certain!" : "I don't understand what the big deal is with you? He wants you, you want him - so {b}do him{/b} already!",
        
        "I'm pretty sure {b}[firstname]{/b} has a taste for older women and you specifically. You should grab hold of him before he moves on to someone else." : "I'm pretty sure {b}[firstname]{/b} has a taste for older women and you specifically. You should grab hold of him and stamp him down. Hard.",
        
        "... How can you be sure?" : "Wait - No! I'm {b}his Mother{/b}, and that's not something that should even cross a {b}good Mother's{/b} mind.",
        
        "Let's just say I have my reasons." : "What have you ever done except devote your life to your kids, {b}[deb_name]{/b}?",
        
        "Stop tormenting yourself and do it, {b}[deb_name]{/b}!" : "You {b}are a good Mother{/b}, and you're both grown adults. What else matters?",
        
        "Just make sure you really fuck his brains out! Once he gets a taste of that, he'll be hooked!" : "You gave {b}[firstname]{/b} everything and now he wants to give you something back. Something {b}big and hard{/b}. Ha-ha!",
        
        "AIs it really as big as you've made it out to be?!" : "Is it really as big as you've made it out to be?!",
        
        "Hey, don't be getting any ideas now!" : "Hey, don't start getting ideas about {b}my son{/b} now, {b}Sis{/b}!",
        
        "Good lord! I haven't even slept with him yet and you're already trying to negotiate your way into our bed!" : "He's {b}my son{/b} and {b}your nephew{/b}! But you're right, who cares? Let's go up there right now and just fuck his brains out. Both of us, together.",
        
        "Don't you have any shame?" : "Then we'll call {b}[jen_name]{/b} in and get her in on the action too. Oh, and {b}Tammy{/b} from next door, can't leave her out, and-",
        
        "Haha! You're right, I'm being a bad girl again, aren't I?" : "Haha! Ok, ok, enough, you've made your point {b}Sis{/b}. I'm being a very bad girl.",
        
        "... I think that's enough wine for you." : "... And you're officially cut off. No more wine for you.",
        
        "You know, a good friend would have at taken me for a quick spin at the very least!" : "You know, a good {b}twin sister{/b} would at least give me a little \"goodbye kiss\" {b}down there{/b} before I leave...",
        
        "... What a Goober." : "... Well, at least we know which {b}twin{/b} got all the {b}crazy{/b}... And more than her fair share of the {b}horny{/b} too!",
        
        "I had no idea {b}[deb_name]{/b} and {b}Diane{/b} were so intimate... I should ask if {b}[deb_name]{/b} needs any help." : "I had no idea {b}Mom{/b} and {b}Aunt Diane{/b} were so... {b}intimate{/b}... I should ask {b}Mom{/b} if she needs any help.",
        
        "{b}[deb_name]{/b}?" : "{b}Mom{/b}?",
        
        "Oh, heh. Sorry! It was just {b}Diane{/b} and I being silly." : "Everything's fine, Sweetie. It was just {b}your Aunt Diane{/b} and I being silly.",
        
        "Did {b}Diane{/b} leave already?" : "Did {b}Aunt Diane{/b} leave already?",
        
        "Why don't I go fetch you a towel?" : "Why don't I go grab you a towel, {b}Mom{/b}?",
        
        "You're so wet {b}[deb_name]{/b}.{p=2}{nw}" : "You're so wet {b}Mom{/b}.{p=2}{nw}",
        
        "Do you like getting fingered on the kitchen counter?{p=3}{nw}" : "Do you like having {b}your son{/b} finger you on the kitchen counter?{p=3}{nw}",
        
        "I'm such a naughty girl...{p=2}{nw}" : "{b}Your Mommy's{/b} such a naughty girl...{p=2}{nw}",
        
        "It's alright, {b}[deb_name]{/b}..." : "It's alright, {b}Mom{/b}...",
        
        "{b}[deb_name]{/b}?" : "{b}Mom{/b}?",
        
        "If you want me to take care of that for you, just let me know." : "If you want {b}Mommy{/b} to take care of that for you, just let me know.",

    
        
        "He's been helping with chores and making repairs!" : "{b}[firstname]{/b} has been so helpful and caring lately...",
        
        "He even got the car dealership to replace the engine in my car, free of charge!" : "He's really stepped up and taken on all of {b}his Father's{/b}... husbandly duties...",
        
        "It really wasn't that big a deal..." : "I umm... Yeah, just happy to help!",
        
        "Wait, seriously?! {b}Diane{/b} is living here now? Just like that?" : "Wait, seriously?! {b}Aunt Diane{/b} is moving in now? Just like that?",
        
        "She's not moving right this very second, {b}[jen_name]{/b}!" : "And just because she offered doesn't mean that we're doing it.",
        
        "Just like the sleepovers we used to have when we were kids!" : "We shared a bedroom and a bed for years, {b}Sis{/b}. I'm up for doing it again.",
        
        "... It'll be nice to spend some more time with you guys!" : "I'll get to spend more time with the family! And with my {b}favorite nephew{/b}...",
        
        "We can work out the details later." : "There's no burning rush. We can figure this all out later.",
        
        "It's great seeing you, {b}Diane{/b}! You're welcome here anytime!" : "It was great seeing you, {b}Sis{/b}! You're welcome here anytime!",
        
        "Oh, and don't go thinking I'm gonna forget about your offer!" : "You're too sweet! Oh, and I was completely serious about moving in - it's a standing offer!",
        
        "You just say the word! I'll pack my bags and be on your doorstep in an instant!" : "You just say the word! I'll grab a nightie and a pillow and be on your doorstep in an instant!",
        
        "Hah! I know you would, {b}Diane{/b}. I'll be in touch about it." : "Hah! I know you would, {b}Sis{/b}.",
        
        "Good night, {b}Diane{/b}!" : "Good night, {b}Aunt Diane{/b}!",
        
        "So you like working for {b}Diane{/b}." : "So you like working for {b}Aunt Diane{/b}.",
        
        "Come on, I know you've heard the stories about {b}Diane{/b}!" : "Come on, I know you've heard the stories about {b}Aunt Diane{/b}!",
        
        "Look, I'll pay you back one way or another, dummy!" : "Look, I'll pay you back one way or another, {b}little brother{/b}!",

    
        
        "I'm sorry, {b}[deb_name]{/b}." : "I'm sorry, {b}Mom{/b}.",
        
        "Sit up on the washer for me." : "Sit up on the washer for {b}Mommy{/b}.",
        
        "Now sit back and let me help you with your dirty sticky load." : "Now sit back and let {b}Mommy{/b} help you with your dirty sticky load.",
        
        "You're beautiful, {b}[deb_name]{/b}." : "You're beautiful, {b}Mom{/b}.",
        
        "{b}[deb_name]{/b}!" : "{b}Mom{/b}!",
        
        "Anytime, {b}[deb_name]{/b}." : "Anytime, {b}Mom{/b}.",
        
        "No, it's fine, {b}[deb_name]{/b}..." : "No, it's fine, {b}Mom{/b}...",
        
        "I love you, {b}[deb_name]{/b}!" : "I love you, {b}Mom{/b}!",
        
        "You like taking care of me, don't you?" : "You like taking care of your {b}Mommy{/b}, don't you?",
        
        "Yes, {b}[deb_name]{/b}." : "Yes, {b}Mom{/b}.",
        
        "I've got your {b}lotion{/b}, {b}[deb_name]{/b}." : "I've got your {b}lotion{/b}, {b}Mom{/b}.",
        
        "This dang back pain just won't relent!" : "My back has been killing me lately.",
        
        "It's really no fun getting old, {b}[firstname]{/b}. I don't recommend it!" : "It stinks getting old...",
        
        "You wouldn't mind?" : "You'd do that for your old {b}Mother{/b}?",
        
        "Of course not! I'd be very happy to!." : "You're not old {b}Mom{/b}.",
        
        "I can apply the lotion and give you a massage all at once!" : "But, I can see that you're in pain.",
        
        "How does that sound?!" : "I could put some lotion on your legs so you don't have to bend over with your sore back... if you want...",
        
        "... Let me just get comfortable." : "Let me just slide up on this here...",
        
        "You said your legs feel dry?" : "Where should I start?",
        
        "Yeah, they always seem to be the worst this time of year!" : "Oh, it doesn't matter. Just pick a spot.",
        
        "It's alright, Sweetie. There's a lot of ground to cover!" : "It's alright, Sweetie. I'll use the rest myself after you're finished.",
        
        "That takes care of the lower half." : "I rubbed in most of the lotion.",
        
        "Did you want me to do your thighs as well?" : "What do you want me to do with the rest?",
        
        "... Yeah, I suppose. So long as you're sure you don't mind?" : "I suppose you could put some a bit higher on my leg... would you mind?",
        
        "Mmm, you're pretty good at this, {b}[firstname]{/b}..." : "Mmm... Dig your hands in a bit deeper there.",
        
        "You can rub a bit harder if you want." : "Feel that knot?",
        
        "I've definitely got some tension stored up in my thigh muscles..." : "Try and rub that out...",
        
        "Oh, This is heaven..." : "Mmm... That feels good.",
        
        "You have wonderful hands, {b}[firstname]{/b}!" : "Oh, wow, your fingers feel wonderful...",
        
        "You should consider becoming a masseur..." : "Mmmm... you're making {b}Mommy's{/b} tension just melt away...",
        
        "I bet you would make a fortune!" : "Some little lady is going to love how helpful and attentive you are.",
        
        "... Heh, that's probably enough. I can finish from here." : "...Um... Thank you, Sweetie... I can take it from here.",
        
        "Why don't you head on upstairs?" : "Listen, I should... um...",
        
        "I've gotta keep an eye on this laundry..." : "I should probably finish this load... of laundry...",
        
        "... and get the dryer going." : "You should go on upstairs and... um...",
        
        "Thanks again, Sweetie." : "Thanks... ah... thanks again, Sweetie.",
        
        "She must have noticed me peeking." : "I think she noticed me looking...",
        
        "Was she getting excited or did I just imagine it?" : "Was she getting... wet?",
        
        "... I should probably get my mind off it!" : "I better find something else to do.",
        
        "Anything else, {b}[deb_name]{/b}?" : "Anything else, {b}Mom{/b}?",
        
        "You're welcome, {b}[deb_name]{/b}." : "You're welcome, {b}Mom{/b}.",

    
        
        "( Is it coming from {b}[deb_name]{/b}'s bedroom? )" : "( Is it coming from {b}Mom{/b}'s bedroom? )",
        
        "Thanks, {b}[deb_name]{/b}." : "Thanks, {b}Mom{/b}.",
        
        "{b}[deb_name]{/b}, I'm gonna..." : "{b}Mom{/b}, I'm gonna...",
        
        "( Oh, Shit! {b}[deb_name]{/b}'s coming out of her room! )" : "( Oh, Shit! {b}Mom{/b}'s coming out of her room! )",
        
        "No, It can't be him. It must be {b}[jen_name]{/b}." : "No, it couldn't have been {b}[firstname]{/b}. It must have been {b}his sister{/b}.",
        
        "She seems like the type who would be into porn..." : "They never used to do this sort of thing.",
        
        "... Foot fetish, though?" : "Maybe I'm being too lenient...",
        
        "I never would have guessed that!" : "{b}*sigh*{/b}",
        
        "( I guess she decided not to come down. )" : "( I guess {b}Sis{/b} decided to not come down. )",
        
        "You wouldn't want to miss out on my feet, now would you?" : "You wouldn't want to miss out on {b}your sister's{/b} feet, now would you?",
        
        "Stop moving your hips like that... It's... Too deep!!" : "Stop moving your hips so hard... You're... too {b}big{/b}... It's... Too {b}deep{/b}!!",
        
        "We're too loud. {b}[deb_name]{/b} will..." : "We're too loud! {b}Mom{/b} will...",
        
        "... It's so good!!" : "... But it feels {b}soooooo fucking good{/b}!!",
        
        "You know I need you fresh and rested for my cam shows!!" : "Now your cum is leaking out of me all over the couch! You think {b}Mom{/b} won't notice this?",
        
        "You little pervert..." : "Ah! You like {b}your sister's{/b} feet rubbing your cock, you little pervert...",
        
        "( That must be the channel {b}[jen_name]{/b} was watching. )" : "( That must be the channel {b}my Sister{/b} was watching. )",

    
        
        "( {b}[deb_name]'s{/b} sleeping. )" : "( {b}Mom's{/b} sleeping. )",
        
        "WHA-!!" : "( ...WHA-!!... )",
        
        "{b}[deb_name]{/b}?!?" : "( ...{b}Mom{/b}?!?... )",
        
        "Fuck me harder! I need to cum so bad!" : "Fuck {b}Mommy{/b} harder! She needs to cum so bad!",
        
        "Are you spying on {b}[deb_name]{/b}?" : "Are you spying on {b}Mom{/b}?",
        
        "Good lord! Are you smuggling a summer sausage in there or what?" : "Holy shit! Are you smuggling a summer sausage in there or what, {b}little brother{/b}?",
        
        "Please, don't tell {b}[deb_name]{/b} I was watching her..." : "Please, don't tell {b}Mom{/b} I was watching her...",
        
        "I can't believe I slept in {b}[deb_name]{/b}'s bed last night..." : "I can't believe I slept in {b}Mom{/b}'s bed last night...",
        
        "Heh, you're so cute!" : "You're a little cutie!",
        
        "We don't want her finding you're getting special treatment!" : "I don't need {b}your sister{/b} getting jealous!",
        
        "Feel free to come sleep here again, if you need to." : "Love you, {b}Mom{/b}.",
        
        "See you soon, Sweetie." : "Love you too.",
        
        "You look great, {b}[deb_name]{/b}!" : "You look great, {b}Mom{/b}!",
        
        "Really? How about from the back?" : "Awww... Thank you, dear. How about from the back?",
        
        "It's pretty tight..." : "Umm... Do the pants make my butt look too big? They aren't too tight, are they?",
        
        "No way! Your butt looks perfect, {b}[deb_name]{/b}!" : "Uh... No {b}Mom{/b}. Your bu... um.. I mean... your pants look great.",
        
        "... Maybe... A little." : "N-n-no, of course not, {b}Mom{/b}!!",
        
        "Heh, well at least you're honest about it!" : "Well, thank you for your honesty. It makes me happy to know my butt can still make a man stumble for words.",
        
        "Hey {b}[deb_name]{/b}, what was-" : "Hey {b}Mom{/b}, what was-",
        
        "It's nothing you haven't seen before." : "We've seen each other naked before...",
        
        "Uhh... So, what was the name of that {b}fish{/b} again? The one {b}Diane{/b} likes so much?" : "Uhh... So, what was the name of that {b}fish{/b} again? The one {b}Aunt Diane{/b} likes so much?",
        
        "You like my new lingerie?" : "How do I look now?",
        
        "It's really sexy, {b}[deb_name]{/b}." : "You look... beautiful, {b}Mom{/b}.",
        
        "Hehe, you're just the sweetest!" : "You're always so nice to me, Sweetie. Not to old to hug your {b}Mom{/b}, are you?",
        
        "Thanks, {b}[deb_name]{/b}!" : "Thanks, {b}Mom{/b}!",
        
        "( {b}[deb_name]{/b} is so hot! )" : "( {b}Mom{/b} is so... hot! )",
        
        "( {b}[deb_name]'s{/b} not in her room. )" : "( {b}Mom's{/b} not in her room. )",
        
        "Sleep with {b}[deb_name]{/b}." : "Sleep with {b}Mom{/b}.",
        
        "( These panties are really sexy... )" : "( These feel so soft against my skin... )",
        
        "{b}[deb_name]{/b}?!" : "{b}Mom{/b}?!",
        
        "I'm sorry, I didn't mean to-" : "I'm so sorry, Sweetie!!",
        
        "... I mean, I was expecting-" : "I didn't know you were in here...",
        
        "No, it's fine... Just..." : "No, it's fine... Just... finish whatever you need to do...",
        
        "... Excuse me!" : "I'll come back later!",
        
        "( Was he really just doing that?! )" : "( I never thought I would see my {b}Son{/b} doing... THAT! )",
        
        "( ... In MY room?! )" : "( And in {b}my room{/b}! )",
        
        "( Why would he be doing that in my room?! )" : "( I guess... I always saw him as my innocent little boy! )",
        
        "( Surely he can't be attracted to me, can he?! )" : "( But... Was he doing {b}-it-{/b} with... My {b}underwear{/b}? )",
        
        "( He's a young man and his hormones are making him do crazy things! )" : "( He's having hormonal changes, of course! )",
        
        "( That's gotta be it! He's probably just confused after everything that's happened recently... )" : "( I never see him bring girls over... He must be having urges... )",
        
        "( ... Things were doing so well between us and now this is going to ruin everything! )" : "( {b}Mom{/b} couldn't stop staring ...And now things are gonna be really awkward... )",
        
        "Masturbation is perfectly normal..." : "It's perfectly normal... you know... to... masturbate...",
        
        "I know you have been going through a lot recently; Losing your {b}Dad{/b} and moving in here with us..." : "And I know that young men your age have {b}urges{/b}...",
        
        "You've got to be stressed and more than a little confused..." : "You just have a lot of affection for your {b}Mother{/b}, and you don't have a girlfriend...",
        
        "... But you shouldn't be doing that in my room! ... And certainly not with my lingerie!" : "...but you can't do that in my room! ...And you're ruining my lingerie...",
        
        "I know, I'm sorry. I don't know what came over me!" : "I know, I'm sorry {b}Mom{/b}. I don't know what came over me!",
        
        "{b}[deb_name]{/b}!! Please stop, this is all really embarrassing!" : "Jeez, {b}Mom{/b}!! Please stop, this is already embarrassing!",
        
        "... Sorry. I'm just trying to help." : "Well... it's fine. You're growing up. Yes. Anyway... I want you to know that I {b}love you{/b}...",
        
        "Don't be so embarrassed. Really, it's not a big deal... Everyone masturbates. It's perfectly normal!" : "...And that I'm not mad about it!",
        
        "I still think you're a great kid! You're just having a tough time is all..." : "I just don't want you to develop some sort of complex or something...",
        
        "I'm not a kid..." : "I'll be fine, {b}Mom{/b}... momentary lapse of judgement...",
        
        "You're right, I sorry. You aren't a kid. Just promise not to do that in my room anymore." : "Alright, alright. Just... please promise not to do... {b}that{/b} in {b}Mommy's{/b} room anymore, Sweetie?",
        
        "{b}[deb_name]{/b}!!" : "{b}Mom{/b}!!",
        
        "Oh, {b}[deb_name]{/b}! You're so sexy!" : "Oh, {b}Mom{/b}! You're so sexy!",
        
        "That almost made it all the way over here!" : "Oh, my {b}[firstname]{/b}! That almost made it all the way over here!",
        
        "You're the best {b}[deb_name]{/b}..." : "Yeah, I really needed that. You're the best {b}Mom{/b}...",
        
        "{b}[deb_name]{/b}!!" : "{b}Mom{/b}!!",
        
        "I'm sorry, {b}[deb_name]{/b}..." : "I'm so sorry, {b}Mom{/b}...",
        
        "Can you do that for me?" : "Can you do that for {b}Mommy{/b}?",
        
        "Yes, Ma'am..." : "Yes, {b}Mom{/b}...",
        
        "I'm sorry, {b}[deb_name]{/b}... It just {b}feels so good{/b}..." : "I'm sorry, {b}Mom{/b}... It just {b}feels so good{/b}...",
        
        "I'm trying, {b}[deb_name]{/b}..." : "I'm trying, {b}Mom{/b}...",
        
        "{b}*Sigh*{/b} I will, {b}[deb_name]{/b}." : "Ok, I will, {b}Mom{/b}.",
        
        "We're going to get through this..." : "I love you so much, Sweetie... you know that, right?",
        
        "I'll try, {b}[deb_name]{/b}." : "I'll try, {b}Mom{/b}.",
        
        "We're going to get through this..." : "I love you so much, Sweetie... you know that, right?",
        
        "You don't mean that... You're just confused." : "But Sweetie... I'm your {b}Mother{/b}!",
        
        "No, I really do mean it! {b}[deb_name]{/b}, you're all I think about." : "I know! But all I can think about is... you...",
        
        "That's really sweet of you to say, {b}[firstname]{/b} but we can't do this!" : "Listen to me now, {b}[firstname]{/b}.",
        
        "{b}*Sigh*{/b} This is all my fault..." : "This is all {b}my{/b} fault...",
        
        "Oh god and the thing in the car!" : "Oh, god... and the thing in the car.",
        
        "I'm a terrible person..." : "I'm a terrible {b}Mother{/b}...",
        
        "It's not your fault, {b}[deb_name]{/b}..." : "No! It's not your fault, {b}Mom{/b}...",
        
        "Go ahead, {b}[firstname]{/b}. Finish what you started..." : "Go ahead, {b}Sweetie{/b}. Finish what you started...",
        
        "{b}[deb_name]{/b}..." : "{b}Mom{/b}...",
        
        "Oh, {b}[deb_name]{/b}..." : "Oh, {b}Mom{/b}...",
        
        "{b}[deb_name]{/b}!!! I'm gonna-" : "{b}Mom{/b}!!! I'm gonna-",
        
        "We're going to get through this..." : "I love you so much, Sweetie... you know that, right?",
        
        "Hey, {b}[deb_name]{/b}." : "Hey, {b}Mom{/b}.",
        
        "Come inside, I know exactly what to do." : "Come lay down, {b}Mommy{/b} knows exactly what to do.",
        
        "Oh, yes... I need it, too." : "Oh, yes... {b}Mommy{/b} needs it, too.",
        
        "Thanks, {b}[deb_name]{/b}." : "Thanks, {b}Mom{/b}.",
        
        "Yes, {b}[deb_name]{/b}." : "Yes, {b}Mom{/b}.",
        
        "I understand what you're going through..." : "I've also had trouble sleeping with everything that happened...",
        
        "... And with everything that's happened..." : "...And not having someone by my side at night.",
        
        "Thanks, {b}[deb_name]{/b}." : "Thanks, {b}Mom{/b}.",
        
        "... Here in your bed." : "...And your bed is always so warm.",
        
        "You smell really good, {b}[deb_name]{/b}..." : "You smell really good, {b}Mom{/b}...",
        
        "( Is this too much? )" : "( And moving closer... between my legs... )",
        
        "( It feels good but should I stop him? )" : "( He's never been {b}this{/b} affectionate... )",
        
        "You smell really good, {b}[deb_name]{/b}..." : "You smell really good, {b}Mom{/b}...",
        
        "{b}[deb_name]{/b}..." : "{b}Mom{/b}...",
        
        "Can I kiss you?" : "You think I could have a kiss?",
        
        "You want to kiss me?" : "A kiss?",
        
        "... Right now?" : "On your cheek?",
        
        "Y-yes, please." : "No, like... A real kiss.",
        
        "I don't know why... I just really want to kiss you right now." : "I've just never really done it with anyone other than you before, {b}Mom{/b}...",
        
        "... That's sweet, {b}[firstname]{/b}." : "Never?",
        
        "So is it alright?" : "No...",
        
        "... to kiss you, just a little bit?" : "But I always wanted to try it more.",
        
        "I suppose we can kiss but just a little bit!" : "I suppose I could teach you again. But just on the lips, okay?",
        
        "( I can feel his tongue! )" : "( I can feel his tongue! But I can't just, stop...)",
        
        "( Why is he so good at this?! )" : "( Wow, he's really into it... and not bad at it. )",
        
        "( His hands are on my breasts... )" : "( His hands are pressing against my breasts... and... His knee, rubbing on my... )",
        
        "( ... This is making me so horny! )" : "( I feel so... Hot, right now. )",
        
        "{b}*Gulp*{/b} That was really good, {b}[firstname]{/b}." : "You were... very... good, {b}Sweetie{/b}.",
        
        "Are you okay, {b}[deb_name]{/b}?" : "Are you okay, {b}Mom{/b}? I could feel you shaking.",
        
        "... Yeah, I'm fine, Sweetie. It's just hot in here." : "I... I must be getting too warm. That's all.",
        
        "( ... I wish I could take this further! )" : "( ... I can't believe my sweet little man is making me feel like this! )",
        
        "No, Sweetie. It felt wonderful!" : "No, Sweetie... {b}Mommy{/b} will be fine.",
        
        "Alright, {b}[deb_name]{/b}." : "Alright, {b}Mom{/b}.",
        
        "Goodnight, {b}[deb_name]{/b}..." : "Goodnight, {b}Mom{/b}...",
        
        "Looks like {b}[deb_name]{/b} is already up." : "Looks like {b}Mom{/b} is already up.",
        
        "You're welcome. Love you, {b}[deb_name]{/b}." : "You're welcome. Love you, {b}Mom{/b}.",
        
        "Lay back and let me take a turn." : "Lay back and let {b}Mommy{/b} take a turn.",
        
        "You just like watching my tits bounce don't you, my naughty boy?" : "You just like watching {b}Mommy's tits bounce{/b} don't you, my naughty boy?",
        
        "I'm almost there!{p=2}{nw}" : "{b}Mommy's{/b} almost there!{p=2}{nw}",
        
        "Oh, {b}[deb_name]{/b}! I can feel you clenching down on me!{p=2}{nw}" : "Oh, {b}Mom{/b}! I can feel you clenching down on me!{p=2}{nw}",
        
        "You like sucking on my titties?{p=2}{nw}" : "You like sucking {b}Mommy's{/b} titties?{p=2}{nw}",
        
        "{b}[deb_name]{/b}, I'm gonna..." : "{b}Mom{/b}, I'm gonna...",
        
        "Let it out, Sweetie!" : "Let it out, Sweetie! Give it all to {b}Mommy{/b}!",
        
        "{b}[deb_name]{/b}!!!" : "{b}Mom{/b}!!!",
        
        "Oh, {b}[deb_name]{/b}!" : "Oh, {b}Mom{/b}!",
        
        "Stay inside me for a while..." : "Stay inside {b}Mommy{/b} for a while...",
        
        "{b}[deb_name]{/b}!!!" : "{b}Mom{/b}!!!",
        
        "Sorry, {b}[deb_name]{/b}." : "Sorry, {b}Mom{/b}.",
        
        "{b}[deb_name]{/b}, I'm gonna..." : "{b}Mom{/b}, I'm gonna...",
        
        "Let it out, Sweetie!" : "Let it out, Sweetie! Give it all to {b}Mommy{/b}!",
        
        "{b}[deb_name]{/b}, can I cum on top of you?" : "{b}Mom{/b}, can I cum on top of you?",
        
        "Heh, look at me! I'm covered!" : "Go get {b}Mommy{/b} some tissues so she can clean herself, will you?",
        
        "Yeah... I guess I got a little carried away." : "Yes, {b}Mom{/b}. Sorry about the mess...",
        
        "Don't be. It feels wonderful!" : "Don't be. I like being showered in my man's cum.",
        
        "{b}[deb_name]{/b}, I'm gonna..." : "{b}Mom{/b}, I'm gonna...",
        
        "{b}[deb_name]{/b}! I'm..." : "{b}Mom{/b}! I'm...",
        
        "Wow, that's a lot..." : "Wow, that's a lot of cum...",
        
        "It's everywhere!." : "I know! I can feel it all over my tits, Sweetie.",
        
        "No, it's fine, {b}[deb_name]{/b}." : "No, it's fine, {b}Mom{/b}.",
        
        "I love you, {b}[deb_name]{/b}!" : "I love you, {b}Mom{/b}!",

    
        
        "Ask {b}[deb_name]{/b}." : "Ask {b}Mom{/b}.",

    
        
        "I don't need to use {b}[deb_name]{/b}'s car." : "I don't need to use {b}Mom{/b}'s car.",
        
        "{b}[deb_name]{/b}'s car ... wish I had a reason to drive it..." : "{b}Mom{/b}'s car ... wish I had a reason to drive it...",
        
        "( I should probably tell {b}[deb_name]{/b} about this. She won't be happy! )" : "( I should probably tell {b}Mom{/b} about this. She won't be happy! )",
        
        "Maybe {b}[deb_name]{/b} knows where it went." : "Maybe {b}Mom{/b} knows where it went.",
        
        "I hope this is good enough to fool {b}Mrs. Johnson{/b}." : "I hope this is good enough to fool {b}Erik's Mom{/b}.",
        
        "I was sceptical at first but now that we're sitting here..." : "I always wanted to...pleasure...{b}your Father{/b} when we went for a drive.",
        
        "... It's kinda turning me on." : "But he always shooed me away. Said it wasn't safe.",
        
        "Imagine if we were parked out in public somewhere?!" : "{b}Your Father{/b} was always so concerned for his family's safety.",
        
        "I'm getting wet just thinking about it!" : "Now, are you still up for some fun in the car? I'm getting wet just thinking about it!",
        
        "I'd be down to try something like that..." : "Do you think he'd be mad at me for...",
        
        "... You wouldn't be embarrassed?" : "...You know...",
        
        "Heh, I dunno... I would probably be mortified if we got caught!." : "I... I don't think he'd be mad, Sweetie.",
        
        "... But..." : "He'd appreciate knowing you've been taking care of things for us.",
        
        "... That's what makes it so exciting, you know?!" : "Besides, I'm the one who wanted to go further with our relationship, too.",
        
        "Well, at least it gets me excited..." : "You're a {b}good son{/b} and you have nothing to worry about.",
        
        "I'm getting wet just thinking about it!" : "Now, are you still up for some fun in the car? I'm getting wet just thinking about it!",
        
        "Hehe, yes..." : "Very. You want me to jerk you off, Sweetie?",
        
        "So what are we gonna do about this big, hard cock here?" : "Or, would you like {b}Mommy{/b} to give you some road head?",
        
        "It was good {b}[deb_name]{/b}! Don't worry." : "It was good {b}Mom{/b}! Don't worry.",
        
        "I can't believe your cock is so big!{p=2}{nw}" : "You've got such a big cock, {b}Baby{b}.{p=2}{nw}",
        
        "I just love your big cock!?{p=2}{nw}" : "Just let me know when you're close, will you?{p=2}{nw}",
        
        "Cum for me, {b}[firstname]{/b}!{p=2}{nw}" : "I just cleaned out the car.{p=2}{nw}",
        
        "Right there, {b}[deb_name]{/b}.{p=2}{nw}" : "Right there, {b}Mom{/b}.{p=2}{nw}",
        
        "Faster, {b}[deb_name]{/b}." : "Faster, {b}Mom{/b}.",
        
        "Thanks, {b}[deb_name]{/b}." : "Thanks, {b}Mom{/b}.",
        
        "Let's head back inside before {b}[jen_name]{/b} starts wondering where we snuck off to." : "Let's head back inside before {b}your sister{/b} starts wondering where we snuck off to.",
        
        "{b}[deb_name]{/b}, I'm gonna..." : "{b}Mom{/b}, I'm gonna...",
        
        "Wow! That was so much!" : "...You naughty boy! That was so much!",
        
        "That was awesome! You're so good at that!" : "Sorry, {b}Mom{/b}. But that was awesome!",
        
        "Hehe, well I'm glad you enjoy it, {b}[firstname]{/b}. Cause I love sucking your cock!" : "I could tell you liked it! I kinda liked it too.",
        
        "Let's head back inside before {b}[jen_name]{/b} starts wondering where we snuck off to." : "Let's head back inside before {b}your sister{/b} starts wondering where we snuck off to.",
        
        "Just let me clean myself up first..." : "Thanks-",
        
        "I'll see you in there, Sweetie!" : "No, thank you, Sweetie.",
        
        "Don't take too long..." : "I love sucking {b}my man's{/b} big cock.",

    
        
        "( I shouldn't snoop around {b}[deb_name]'s{/b} bedroom. )" : "( I shouldn't snoop around {b}Mom's{/b} bedroom. )",
        
        "( I should see go see if {b}[deb_name]{/b} is alright. )" : "( I should see go see if {b}Mom{/b} is alright. )",
        
        "( I really shouldn't disturb {b}[deb_name]{/b} when she's sleeping. )" : "( I really shouldn't disturb {b}Mom{/b} when she's sleeping. )",
        
        "Thanks, {b}[deb_name]{/b}! I'll go eat now." : "Thanks, {b}Mom{/b}! I'll go eat now.",
        
        "Sorry, {b}[deb_name]{/b}! I'll go eat now." : "Sorry, {b}Mom{/b}! I'll go eat now.",
        
        "I should go check on {b}Roxxy{/b} and {b}[jen_name]{/b}..." : "I should go check on {b}Roxxy{/b} and {b}my Sister{/b}...",

    
        
        "( Maybe this place would have a book that would help {b}Diane{/b} make more milk. )" : "( Maybe this place would have a book that would help {b}Aunt Diane{/b} make more milk. )",
        
        "( It should work with {b}Diane{/b} too. )" : "( It should work with {b}Aunt Diane{/b} too. )",

    
        
        "( I should probably ask the {b}store clerk{/b} like {b}Diane{/b} suggested. )" : "( I should probably ask the {b}store clerk{/b} like {b}Aunt Diane{/b} suggested. )",

    
        
        "No problem, {b}[deb_name]{/b}. I'm having fun!" : "No problem, {b}Mom{/b}. I'm having fun!",
        
        "Sure, {b}[deb_name]{/b}. Okay." : "Sure, {b}Mom{/b}. Okay.",
        
        "{b}[deb_name]{/b} said it should be on the {b}second floor{/b}." : "{b}Mom{/b} said it should be on the {b}second floor{/b}.",

    
        
        "I dunno {b}[deb_name]{/b}, it seems pretty girly in here..." : "I dunno {b}Mom{/b}, it seems pretty girly in here...",
        
        "Yeah, I know that, {b}[deb_name]{/b}!" : "Yeah, I know that, {b}Mom{/b}!",
        
        "( What would {b}[deb_name]{/b} like? )" : "( What would {b}Mom{/b} like? )",
        
        "{b}[deb_name]{/b}, you alright in there?" : "Uh...{b}Mom{/b}, you alright in there?",
        
        "I'm sorry, {b}[deb_name]{/b}." : "I'm sorry, {b}Mom{/b}.",
        
        "Y-yeah, sure thing, {b}[deb_name]{/b}." : "Y-yeah, sure thing, {b}Mom{/b}.",
        
        "Hmm, I should check out the necklace display for something {b}[deb_name]{/b} would like..." : "Hmm, I should check out the necklace display for something {b}Mom{/b} would like...",
        
        "I should take this necklace to {b}[deb_name]{/b} and see if she likes it." : "I should take this necklace to {b}Mom{/b} and see if she likes it.",
        
        "I have to wait for {b}[deb_name]{/b}." : "I have to wait for {b}Mom{/b}.",

    
        
        "Well, I told {b}[deb_name]{/b} that I would visit her friend {b}Diane{/b}." : "Well, I told {b}Mom{/b} that I would visit {b}Aunt Diane{/b}.",

    
        
        "Yes, Ma'am..." : "Yes, {b}Mom{/b}...",

    
        
        "...You choose to be an adulterer, a sinner, a SCAMP!!" : "...You choose to be an fornicator, a sinner, a TRAMP!!",
        
        "Oh? Does [deb_name] give you a spanking if you're home late?" : "Oh? Does {b}your Mom{/b} give you a spanking if you're home late?",

    
        
        "( Maybe {b}Mr. Johnson{/b} was telling the truth. )" : "( Maybe {b}Erik's dad{/b} was telling the truth. )",
        
        "( {b}Mr. Johnson{/b} must've been collecting these items for a while. )" : "( {b}Erik's dad{/b} must've been collecting these items for a while. )",

    
        
        "I should talk to {b}Erik{/b} about {b}taking some of Mr. Johnson's beer{/b}." : "I should talk to {b}Erik{/b} about {b}taking some of his dad's beer{/b}.",

    
        
        "I'll talk with him. I know his wife." : "I'll talk with him. His son is my best friend.",
        
        "( Sounds like I need to help him find where {b}Larry{/b} hid the stolen goods. )" : "( Sounds like I need to help him find where {b}Erik's dad{/b} hid the stolen goods. )",
        
        "{b}Larry{/b} actually told me where it was." : "{b}Erik's dad{/b}, er.. {b}Larry{/b} actually told me where it was.",

    
        
        "I told {b}Mrs. Johnson{/b} I went to see a movie at the mall..." : "I told {b}Mom{/b} I went to see a movie at the mall...",
        
        "... I just don't like to upset {b}Mrs. Johnson{/b}, you know?" : "...I just don't like to upset {b}Mom{/b}, you know?",

    
        
        "His landlord always packs him some of her homemade fudge." : "His mom always packs him some of her homemade fudge.",
        
        "Lucky guy. His landlord sure must like him." : "Lucky guy. His mom sure must love him.",

    
        
        "The end of the term is quickly approaching and you know what that means..." : "The end of the semester is quickly approaching and you know what that means...",
        
        "It's time to find yourself a date and hit the dance floor at our Annual Sorority Ball!" : "It's time to find yourself a date and hit the dance floor at Senior Prom!",
        
        "We would like to invite you all to come out and support our school Basketball Team." : "We would like to invite you all to come out and support the Summerville High Basketball Team.",
        
        "We are still looking to fill a few spots on the Summerville Athletics Team." : "We are still looking to fill a few spots on the Summerville High Track and Field Team.",

    
        
        "... Because the woman who makes it asked me to." : "Oh, it's actually from my {b}Aunt{/b}...",

    
        
        "Yeah... I didn't do too well. Sorry {b}Diane{/b}!" : "Yeah... I didn't do too well. Sorry {b}Aunt Diane{/b}!",
        
        "I always need fresh vegetables..." : "{b}Your Aunt{/b} always needs fresh vegetables...",
        
        "Thanks {b}Diane{/b}!" : "Thanks {b}Aunt Diane{/b}!",

    
        
        "We love you Summerville!" : "We love you Summerville High!",

    
        
        "We're working on it, {b}Mrs. Johnson{/b}." : "We're working on it, {b}Mom{/b}.",
        
        "We're working on it, {b}Mrs. Johnson{/b}." : "We're working on it, {b}Mom{/b}.",
        
        "Yeah, are you sure about this, {b}Mrs. Johnson{/b}?" : "Yeah, are you sure about this, {b}Mom{/b}?",
        
        "*Hic* You're completely naked, {b}Mrs. Johnson{/b}." : "*Hic* You're completely naked, {b}Mom{/b}.",
        
        "I think {b}Mrs. Johnson{/b} wants to have fun with us." : "I think {b}your Mom{/b} wants to have fun with us.",
        
        "Tell {b}Mrs. Johnson{/b}, I'm sorry." : "Tell {b}your Mom{/b}, I'm sorry.",
        
        "I can handle it, {b}Mrs. Johnson{/b}. Thanks." : "I can handle it, {b}Mom{/b}. Thanks.",
    }


    incestPatchCutscenes ={
        "Using the key and stool, I was able to get into our attic.\nI had never been up there before.\nI was filled with excitement wondering what treasures {b}[deb_name]{/b} and dad had stashed away.":"Using the key and stool, I was able to get into our attic.\nI had never been up there before.\nI was filled with excitement wondering what treasures {b}my Mom and dad{/b} had stashed away.",
        "March 3rd, on a rainy afternoon.\n{b}My father's{/b} funeral. I can't believe he's really gone.\nHe died from a work related accident at the age of 40. Leaving me all alone with no family to speak of...":"March 3rd, on a rainy afternoon.\nAll my relatives are here, mourning the loss of {b}my Father{/b}.\nHe died from a work related accident at the age of 40. Leaving behind {b}my Mom{/b}, {b}my Sister{/b}, and I...",
        "Circumstances surrounding his death have been found {i}suspicious{/i} by the police.\nThey were at our house for an entire week, bombarding me with questions to which I had no answers.\nNo {i}conclusive{/i} evidence has been found and the knowledge that my father will get no {i}justice{/i} weighs heavily upon me.":"Circumstances surrounding his death have been found {i}suspicious{/i} by the police.\nThey were at our house for an entire week asking questions, but they said nothing was {i}conclusive{/i}.\nHopefully things get sorted out and we can get some {i}justice{/i}...",
        "Luckily, {b}my father's{/b} life long friend has taken me in and given me a room in her home.\nThe night of the funeral, I overheard her reminiscing about {b}my father{/b} in the kitchen.\nShe eventually broke down and said she didn't know what to do.\nIt seems {b}my father{/b} had gotten involved with some real bad people who were now pressuring her to cover his {b}debts{/b}.":"The night of the funeral, I overheard a conversation between {b}Mom{/b} and {b}Aunt Diane{/b}. \nShe said it's been a tough year for us, and that Dad had owed a {i}lot of money{/i} to some bad people. \nNow that he was gone, she didn't know what to do.\nShe started sobbing...",
        "Now a month later, things are finally starting settle down.\nI've gotten used to my new living arrangement and today will be my first day back at college.\nIt'll be nice to see my friends again.":"Our family was a wreck. \n{b}Dad's{/b} passing was unexpected and really hit us all pretty hard as a family. \n{b}Mom{/b} even got me excused from school for a month, as we tried to sort everything out. \n...but I can't grieve forever. Tomorrow is a new day, and I have to look after Mom and my Sister.",
        "There are {i}3 things{/i} I have to take care of before the end of the semester.\n1) - {b}I have to secure a way to pay for next semester's tuition.{/b}\n2) - {b}I have to uncover the truth about my father's murder.{/b}\n3) - {b}I have to find a date for the Sorority Ball.{/b}":"There are {i}3 things{/i} I have to take care of before the end of the summer.\n1) - {b}I have to save enough money for college.{/b}\n2) - {b}I have to find out what really happened to Dad.{/b}\n3) - {b}I have to find a date for prom.{/b} ",
        "I don't think {b}[deb_name]{/b} had ever had help with dishes before... \nShe told me her late husband never did any work around the house and my {b}Dad{/b} only really helped with yard work or broken appliances. \nShe stayed with me in the kitchen until I was finished and we had a nice long chat. \nIt was nice getting to know {b}[deb_name]{/b} better...":"{b}Dad{/b} was usually the one helping {b}Mom{/b} with dishes... \nBut, I didn't mind being the one to help her now. \nShe stayed with me in the kitchen and we talked the whole time... \nIt was nice seeing {b}Mom{/b} happy for once.",
        "It's been really fun helping {b}[deb_name]{/b} out around the house. \nI think she's enjoying it as well. Always so eager to strike up a conversation and learn more about my life. \nWe've certainly been getting a lot closer as of late and I can't help but admire her beauty and charm. \nShe seems to be growing more comfortable with me too. The way she looks at me, her innocent touches...":"Recently, I've been looking forward to helping {b}Mom{/b} around the house. \nI could tell she enjoyed it too, always hanging around and asking me how things were going with girls at school... \nI feel like she's been so close to me lately... \nThe way she stands by me, touches me, and keeps staring at me all the time.",
        "{b}Diane{/b} went to lie down as I began digging up her garden.\n It was so hot outside and there were so many weeds and bugs!\nI grit my teeth and set myself to the task...\n... I hope she's planning to pay me well for all this physical labor!":"{b}Aunt Diane{/b} went to lay down as I began digging up her garden.\n It was so hot outside and there were so many weeds and bugs!\nI grit my teeth and set myself to the task...\n... I hope she's planning to pay me well for all this physical labor!",
        "As I worked, I noticed {b}Diane{/b} was watching me intently...\nI suppose she was just trying to make sure I did a good job.\nWe exchanged a few words here and there but mostly just small talk.\nHer eyes seemed fixed upon my sweat soaked body.":"As I worked, I noticed {b}Aunt Diane{/b} was watching me intently...\nI suppose she was just trying to make sure I did a good job.\nWe exchanged a few words here and there but mostly just small talk.\nHer eyes seemed fixed upon my sweat soaked body.",
        "I found that time passed quickly when I was with {b}[deb_name]{/b}...":"I found that time passed quickly when I was with {b}Mom{/b}...",
        "I felt bad {b}[deb_name]{/b} was having a hard time with her back pain. \nThe least I could do was help her out, even if it took me forever to finish. \nThe stairs were the worst part! No wonder her back is hurting her... \nAt least {b}[deb_name]{/b} kept me company while I worked.":"I felt bad {b}Mom{/b} was having a hard time with her back pain. \nI was glad I could help, even if it took a while to finish. \nI have to say, doing the stairs was harder than I thought... \nAt least {b}Mom{/b} kept me company until I finished both floors.",
        "Once I got back home I headed upstairs to fix the bathroom sink.\nI replaced the joint with a new length of pipe and tightened it as much as I could.\nIt kind of felt weird having {b}[deb_name]{/b} and {b}[jen_name]{/b} watch me the whole time.\nLucky for me, the repairs all went smoothly...":"Once I got back home I headed upstairs to fix the bathroom sink.\nI replaced the joint with a new length of pipe and tightened it as much as I could.\nIt kind of felt weird having {b}my Mom{/b} and {b}my Sister{/b} watch me the whole time.\nHowever, they both seemed quite pleased...",
        "It was a little embarrassing stripping down in front of {b}[deb_name]{/b}. \nShe didn't seem to notice though. She just hurriedly stuffed my clothes into the machine. \nI couldn't help but notice the view as she went about her work.\nNeedless to say, I forgot my embarrassment rather quickly...":"That was the first time I'd undressed in front of {b}Mom{/b} since I was too little to care. \nI was a bit shy, but she was surprisingly fine with it. \nShe bent over to add my clothes to the laundry... revealing herself to me.\nI wanted to look away, but couldn't... I was aroused by it.",
        "As I looked through the window, I spotted the guy who'd been delivering all the threats.\nIt would seem he brought backup this time.":"As I looked through the window, I spotted the guy who'd been delivering all the threats.\nIt would seem he brought backup this time.",
        "I couldn't hear what they were saying, but {b}[deb_name]{/b} looked terrified.":"I couldn't hear what they were saying, but {b}Mom{/b} looked terrified.",
        "... Then one of the goons knocked her to the floor!":"... Then one of the goons knocked her to the floor!",
        "There was no way I could just stand there and watch...\nI {b}had{/b} to do something!":"There was no way I could just stand there and watch...\nI {b}had{/b} to do something!",
        "This is a lot harder than I expected. I should've paid more attention to how {b}Dad{/b} used to do it.":"This is a lot harder than I expected. I should've paid more attention to how {b}Dad{/b} used to do it.",
        "It doesn't look half bad. I Hope {b}[deb_name]{/b} thinks the same.":"It doesn't look half bad. I Hope {b}Mom{/b} thinks the same.",
        "Hmm, I wonder how long she's been standing there? I was so focused I didn't notice her come out.":"Hmm, I wonder how long she's been standing there? I was so focused I didn't notice her come out.",
        "{b}[deb_name]{/b} certainly seemed to be enjoying it. Her melodic laughter filled the room and brought a smile to my face.":"{b}Mom{/b} certainly seemed to be enjoying it. Her melodic laughter filled the room and brought a smile to my face.",
    }


    def dialogueFixes( text ):
        def innerChange( m ):
            if m.group(0) == ( "landlady" ): return "Mom"
            elif m.group(0) == ( "Summerville College" ): return "Summerville High"
        if text in incestPatchChanged1.keys():
            return incestPatchChanged1[text]
        elif text in incestPatchChanged2.keys():
            return incestPatchChanged2[text]
        elif text in incestPatchCutscenes.keys():
            return incestPatchCutscenes[text]
        elif text is not None:
            return renpy.re.sub( r'(?:Summerville College|landlady)', innerChange, text )


    config.say_menu_text_filter = dialogueFixes
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
