#The Park Date
label park:
    $HKBHideButtons()
    stop music
    play music "Submods/DateMonikaSubmod/music/Morning-Ambience.mp3"
    hide black
    scene park
    $ bench = True
    pause 0.75
    $ is_sitting = False
    show monika 3eua_static at t11
    m "We've arrived! This park seems fairly nice, doesn't it?"
    menu:
        "\"It does.{w=0.4}.{w=0.4}\"":
                                     show monika 1hua_static at t11

                                     menu:
                                         "\"Then, would you like to take a walk together?\"":
                                                                                            show monika 1eud_static at t11
                                                                                            pass

    m 1eub_static "Oh! Of course, [mas_get_player_nickname()]."
    m 5eua_static "Let's go then!"
    scene park2 with wipeleft_scene
    pause 0.75
    show monika 1hua_static at t11
    m 3eka_static "Hey.. [player]."
    m "Mind if I talk about some stuffs?"
    menu:
        "\"I don't mind.\"":
                           pass

    m 1hua_static "Thank you, [mas_get_player_nickname()]."
    m 3dsd_static "So.{w=0.4}.{w=0.4}.{w=0.4}.{nw}"

    if renpy.random.randint(1, 3) == 1:
        m 3eud_static "Have you ever tried to hum while"
        jump park_continue

    elif renpy.random.randint(1, 3) == 1:
        m 1eud_static "may I know what your favourite pet is?{nw}"
        menu:
            m "may I know what your favourite pet is?{fast}"

            "\"Sure.\"":
                       jump fav_pet_choice

            "\"I don't have a favourite.\"":
                                           jump park_continue

    elif renpy.random.randint(1, 3) == 2:
        m 3eub_static "did you know it's {i}almost{/i} impossible for most people to lick their own elbow?"
        m 2hua_static ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}"
        m 5eua_static "I bet you tried that immediately just now!"
        m 3hub_static "Well? Did you?"
        menu:
            "\"H.. how did you know?\"":
                                       m 5eua_static "Hehe! I just did! After all, there's 75 percent chance you'd have done that, making you belong to the group to immediately try to lick their elbow after hearing that."
                                       m 4hua_static "So, did you succeed?{nw}"
                                       menu:
                                           m "So, did you succeed?{fast}"

                                           "\"I didn't.\"":
                                                          m 2eka_static "That's alright, [player], it was only for fun after all."
                                                          m 3eka_static "After all, different people are good at different things, aren't they?"
                                                          m 5eua_static "And plus, you'll be able to check if I'm able to do that when I cross over to your reality!"
                                                          m 3hub_static "Hehe, let's continue our walk now, [mas_get_player_nickname()]."
                                                          jump park_continue

                                           "\"I did.\"":
                                                       m 1hub_static "That's impressive, [player]!"
                                                       m 3eub_static "According to unofficial estimates, one person in a hundred can lick their own elbow."
                                                       m 3hub_static "And {i}you{/i} just so happens to be one of them!"
                                                       m 5eua_static "That gives you one thing to show off to me when I cross over to your reality, no?"
                                                       m 2hub_static "Haha! Let's continue walking, [mas_get_player_nickname()]."
                                                       jump park_continue

                                           "\"I'm not sure.\"":
                                                              m 2eka_static "Oh, that's fine, [player]."
                                                              m 4eka_static "If you're interested, you can try and do it in your free time with the help of the internet."
                                                              m 5eua_static "Let's continue our walk, shall we?"
                                                              jump park_continue

            "\"I didn't.\"":
                           m 3eud_static "Well, guess that makes you the 25 percent who didn't lick their elbow right after hearing that."
                           m 2eub_static "Why don't you try now then?"
                           pause 3
                           m 2eub_static "So, did you succeed{nw}?"
                           menu:
                               m "So, did you succeed?{fast}"

                               "\"I didn't.\"":
                                              m 2eka_static "That's alright, [player], it was only for fun after all."
                                              m 3eka_static "After all, different people are good at different things, aren't they?"
                                              m 5eua_static "And plus, you'll be able to check if I'm able to do that when I cross over to your reality!"
                                              m 3hub_static "Hehe, let's continue our walk now, [mas_get_player_nickname()]."
                                              jump park_continue

                               "\"I did.\"":
                                           m 1hub_static "That's impressive, [player]!"
                                           m 3eub_static "According to unofficial estimates, one person in a hundred can lick their own elbow."
                                           m 3hub_static "And {i}you{/i} just so happens to be one of them!"
                                           m 5eua_static "That gives you one thing to show off to me when I cross over to your reality, no?"
                                           m 2hub_static "Haha! Let's continue walking, [mas_get_player_nickname()]."
                                           jump park_continue

                               "\"I'm not sure.\"":
                                                  m 2eka_static "Oh, that's fine, [player]."
                                                  m 4eka_static "If you're interested, you can try and do it in your free time with the help of the internet."
                                                  m 5eua_static "Let's continue our walk, shall we?"
                                                  jump park_continue

    else:
        m 4eub_static "did you know that the Yellowstone National Park in Wyoming, Idaho, and Montana is the {i}oldest{/i} U.S. national park, founded in 1872?"
        m 2hksdlb_static "It's unbelievable with how this park is still standing and being maintained, even after 150 years."
        m 2eub_static ".{w=0.2}.{w=0.2}Now that's fascinating about humans."
        m 1hksdlb_static "Sometimes, they can preserve some beautiful structures and monuments,{w=1} though in other times they just abandon it."
        m 3eud_static "The way humans think and treat things sure is interesting."
        m 4hub_static "I'd like to learn about them a lot when I finally cross over to your reality..."
        m 1lksdlb_static "Though it's better if I focus on our date first, no?"
        m 1hub_static "Hehe, thanks for listening!"
        jump park_continue

label fav_pet_choice:
    menu:
        "\"Cats.\"":
                    m 1hub_static "Aww~ cutesy little cats!"
                    m 2hua_static "They are all about being adorable, elegant, calming companions, aren' they now?"
                    m 2eub_static "They are so intelligent as well, capable of dealing with their own exercise and cleaning..."
                    m 2eua_static "Did you know? That cats are just like umbrellas?"
                    m 2hua_static "The umbrella thing comes into play when they're falling."
                    m 3eka_static "They tuck themselves into an umbrella shape,{w=1} which enables them to always land on their feet."
                    m 3eub_static "It's called the cat righting reflex, which is really fascinating if you ask me!"
                    m 5eua_static "I wish to go to a cat cafe with you one day when I finally cross over... sounds like a good idea, yes? [player]?"
                    pass

        "\"Dogs.\"":
                    m 3hub_static "Doggies, man's best friend!"
                    m 2hua_static "I feel like they're like sunshines, always smiling and, being there for their masters, like the loyal companions they are!"
                    m 3eub_static "Oh! [player], did you know why most dogs are so loyal?"
                    m 3eud_static "It's actually because of domestic dogs being descended from wolves."
                    m 3hua_static "Which man once took in and tamed with shelter and food in return for them acting as guard dogs."
                    m 3eub_static "And that this reciprocal relationship remains in your dog's genes and their loyalty is a by-product of it!"
                    m 5eua_static "That sure is an interesting fact about them, right?"
                    m 1hub_static "I'd love to say hi to some dogs with you some day, [mas_get_player_nickname]!"
                    pass

        "\"Fishes.\"":
                    m 2eub_static "Fishies~ they're known to have bad memory, making them quite funny, no?"
                    m 1hub_static "They're admirable and cute at the same time too!"
                    m 3eud_static "Some people say they're easy to take care of, "
                    extend 3eub_static "and that they are great starter animals."
                    m 2hua_static "By the way, do you know what's the slowest fish? Even if you don't, you should try and make a guess!{nw}"
                    menu:
                        m "By the way, do you know what's the slowest fish? Even if you don't, you should try and make a guess!{fast}"

                        "\"Goldfishes?\"":
                                        m 1hksdlb_static "Ahaha! Nope! Though they are the types to rarely swim fast, except feeding times,"
                                        extend 3hua_static " they're not the slowest fishes!"
                                        m 3eud_static "The slowest fish is actually a seahorse. It swims so slowly that a person can barely tell it is moving!"
                                        m 3eub_static "The slowest is the Dwarf Seahorse, which takes about {i}one hour{/i} to travel {i}five feet{/i}!"
                                        m 2hksdlb_static "What a torpid speed they go by..."
                                        m 2hua_static "Those sure are some engaging facts, right? [player]? I'm glad I got to talk about them with you!"
                                        m 5eua_static "Well then! Let's keep going now, shall we?"

                        "\"Tigerfishes?\"":
                                        m 5eub_static "No~ [player], "
                                        extend 2eub_static "in fact, they're quite the strong swimmers, usually hunting in fast, choppy currents."
                                        m 3eud_static "The slowest fish is actually a seahorse. It swims so slowly that a person can barely tell it is moving!"
                                        m 3eub_static "The slowest is the Dwarf Seahorse, which takes about {i}one hour{/i} to travel {i}five feet{/i}!"
                                        m 2hksdlb_static "What a torpid speed they go by..."
                                        m 2hua_static "Those sure are some engaging facts, right? [player]? I'm glad I got to talk about them with you!"
                                        m 5eua_static "Well then! Let's keep going now, shall we?"

                        "\"Seahorses?\"":
                                        m 2hua_static "That is correct! [player]!"
                                        m 3eud_static "They are the slowest fishes indeed, they swim so slow a person can barely tell it is moving!"
                                        m 3eub_static "The slowest is the Dwarf Seahorse, which takes about {i}one hour{/i} to travel {i}five feet{/i}!"
                                        m 2hksdlb_static "What a torpid speed they go by..."
                                        m 2eka_static "Either you were lucky and just so happened to guess the answer correctly..."
                                        m 1dsd_static "Went on the internet and found the answer..."
                                        m 1eka_static "Or that you genuinely knew the answer..."
                                        m 1hub_static "I'm still glad you got it right, though! That doesn't mean I would ever be disappointed if you didn't get it correctly,"
                                        extend 4hua_static " I'm more then happy to tell you about the right answer."
                                        m 5eua_static "Well, let's keep going now, shall we?"

                        "\"Greenland sharks?\"":
                                        m 1eud_static "Ah...{w=1}"
                                        extend 2hksdlb_static "though that might not be the best answer according to certain searches on the internet..."
                                        m 3hua_static "You're not completely wrong, [player]. They are known as the sleeper shark for its sluggish pace, one of the slowest swimming sharks in the world."
                                        m 3eud_static "According to what I know, though, the slowest fish is actually a seahorse. It swims so slowly that a person can barely tell it is moving!"
                                        m 3eub_static "The slowest is the Dwarf Seahorse, which takes about {i}one hour{/i} to travel {i}five feet{/i}!"
                                        m 2hksdlb_static "What a torpid speed they go by..."
                                        m 2hua_static "You know, [player], you really outsmarted me with that answer, not that it's a bad thing!"
                                        m 2eka_static "I enjoy spending time with you a lot, really."
                                        m 5eua_static "Well, let's keep going now, shall we?"
                    pass

        "\"Birds.\"":
                m 1eud_static "Ohhh! "
                extend 2hua_static "Birdies~!"
                m 2hub_static "Were you aware that my favourite bird is quetzal? Haha!"
                m 3eub_static "Quetzals are a kind of bird that many consider among the world's most beautiful."
                m 3eud_static "During mating season, male quetzals grow twin tail feathers that form an amazing train up to one metre long!"
                m 3hua_static "Females do not have long trains, but they do share the brilliant blue, green, and red coloring of their mates."
                m 2hua_static "Nice to know about, right? Haha!"
                m 5eua_static "Thanks for listening~ [player], let's keep going now~"
                pass

        "\"Turtles.\"":
                      m 1eud_static "Ohh~ "
                      extend 3hub_static "turtles! I've always found them interesting!"
                      m 3eub_static "There are so many types of their species too!"
                      m 3dsd_static "Like the red-eared slider, Reeve's Turtle, Spotted Turtle, "
                      extend 2eua_static "et cetera."
                      m 3hua_static "I've heard of a pretty interesting fact about them some time ago."
                      m 3eub_static "Apparently, turtles aren’t silent!"
                      m 1hub_static "Although they’re not likely to be as loud as dogs or cats, turtles do make a range of noises."
                      m 2eua_static "Anything from chicken-like clucks to dog-like barking, depending on the species."
                      m 3hua_static "That was good to know about, right? Hehe~"
                      m 5eua_static "Well then! Let's keep going now! Thanks for listening~"
                      pass

        "{b}{i}NEXT{/i}{/b}":
                            menu:
                                "\"Snakes.\"":
                                             m 2eub_static "Ahh~ snakes, some people may confuse them as lizards,"
                                             extend 3hub_static " the best way to identify them, though, is through their eyelids!"
                                             m 3hua_static "To further expand on that, most lizards have eyelids, while snakes don't."
                                             m 1lksdla_static "Since they lack eyelids, they might give you an eerie feeling."
                                             m 3eud_static "They don’t blink and have to sleep with their eyes wide open!"
                                             m 1hua_static "And instead of eyelids, they have a thin membrane attached to each eye to protect them."
                                             m 2eua_static "That was an interesting fact about them, no?"
                                             m 5eua_static "Ehehe! Let's continue walking now, [mas_get_player_nickname()]!"
                                             pass

                                "\"Ferrets.\"":
                                              m 2eua_static "Ahh~ those fluffy little guys, huh?"
                                              m 3hub_static "They are small and domesticated species, and I've always wanted to see them myself!"
                                              m 3eub_static "Did you know? That ferrets sometimes participate in their own races?"
                                              m 3hua_static "Ferret racing is a particularly popular event in the UK. And instead of a racetrack, ferrets run through pipes."
                                              m 2eua_static "The rules are simple; first ferret to make it to the opposite side of the pipe wins!"
                                              m 1hua_static "Since ferrets are playful animals, they enjoy the games as well."
                                              m 2eua_static "That was a fun fact of them, yes?"
                                              m 5eua_static "Haha~ let's continue walking then~"
                                              pass

                                "\"Tarantulas.\"":
                                                 m "Spiders huh~"
                                                 m "I think they're really fascinating creatures...y'know, since they can make spider webs and all!"
                                                 m "I've came across some fun facts about them earlier..."
                                                 m "One of them being people using spider webs to stop bleeding by putting them on their wounds centuries ago."
                                                 m "Modern scientists discovered that spider webs contain Vitamin K, which is a coagulant that stops bleeding!"
                                                 m "That was an interesting fact about them, no?"
                                                 m "Well then, let's keep going!"
                                                 pass

                                "\"They are not in this list.\"":
                                                                m 2eud_static "Oh, well, "
                                                                extend 3hua_static "that's still alright!"
                                                                m 1eub_static "I'm glad you have a favourite pet either way."
                                                                m 2eub_static "And plus, you'll just have to let me take a look of the pet when I finally cross over to your realty!"
                                                                m 2hub_static "Hehe~ that would be so nice, yes?"
                                                                m 5eua_static "Let's continue our walk now then!"
                                                                pass

                                "{b}{i}PREVIOUS{/i}{/b}":
                                                        jump fav_pet_choice

label park_continue:
    window hide
    scene park3 with wipeleft_scene
    pause 0.95
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    hide screen tear
    pause 1
    menu:
        "\"What was that?!\"":
                             pass

    show monika 1lksdlb_static at t11
    m "I'm...{w=0.3} not sure..."
    m 3eud_static "Let me go check."
    m 1hub_static "Just wait here, okay?"
    window hide
    show monika at thide
    hide monika
    pause 2
    menu:

        "Stay":
               pause 0.5
               jump choose1

        "Look around":
                     jump park_leave

label choose1:
    call screen clickaround()
    screen clickaround():
        imagemap:

            ground "Submods/DateMonikaSubmod/images/park3.png"
            hotspot (296, 355, 136, 69) action Jump("bench_dialogue") hover_sound gui.hover_sound
            hotspot (207, 0, 496, 181) action Jump("sky_dialogue") hover_sound gui.hover_sound
            hotspot (210, 588, 716, 132) action Jump("park_stay") hover_sound gui.hover_sound
            hotspot (714, 358, 101, 92) action Jump("bush_dialogue") hover_sound gui.hover_sound

        timer 15.0 action Show(screen="dialog", message="Hint:\nClick around the background.\nClick on the ground to continue.", ok_action=Hide("dialog"))
    return

label bench_dialogue:
    if renpy.random.randint(1, 2) == 1:
        "{i}This bench is a good resting spot for you and Monika.{/i}"

    else:
        "{i}It's just an ordinary bench.{/i}"
    call screen clickaround()

label sky_dialogue:
    #you can modify this however you want, add or remove dialouge if you want
    if renpy.random.randint(1, 2) == 1:
        "{i}What was with the glitch.{w=0.4}.{w=0.4}.{w=0.4}?{/i}"

    else:
        "{i}It's a beautiful day today, isn't it?{/i}"
    call screen clickaround()

label bush_dialogue:
    "{i}It's a bush.{/i}"
    "{i}What did you expect?{/i}"
    call screen clickaround()

label park_leave:
    scene park with wipeleft_scene
    pause 1
    "{i}Which part of the park do you want to explore?{/i}{nw}"
    menu:
        "{i}Which part of the park do you want to explore?{/i}{fast}"

        "The lake":
                   scene park_lake with wipeleft_scene
                   pause 2
                   "{i}You are now at the park lake.{/i}{nw}"
                   menu:
                       "{i}You are now at the park lake.{/i}{fast}"

                       "Leave":
                              jump park_leave

                       "Check bench" if bench:
                              $ bench = False
                              "{i}The bench seems to have something on it.{/i}"
                              "{i}A..{w=1} tape?{/i}"
                              "{i}There is a tape on the bench.{/i}"
                              "{i}Do you want to play the tape{/i}{nw}"
                              menu:
                                  "{i}Do you want to play the tape?{/i}{fast}"

                                  "\"Yes.\"":
                                            scene black
                                            pause 2
                                            $ renpy.movie_cutscene("Submods/DateMonikaSubmod/Cafe-De-PVs-Guide.webm")
                                            pause 1
                                            jump park_leave

                                  "\"No.\"":
                                           jump park_leave

        "The forest":
                    scene forest with wipeleft_scene
                    pause 1
                    "{i}You are now in the forest.{/i}"
                    pause 0.5
                    call screen clickaround_2()
                    screen clickaround_2():
                        imagemap:

                            ground "Submods/DateMonikaSubmod/images/forest.png"
                            hotspot (368, 621, 483, 99) action Jump("park_leave") hover_sound gui.hover_sound
                            hotspot (1066, 0, 180, 720) action Jump("tree_dialogue") hover_sound gui.hover_sound
                            hotspot (16, 0, 133, 720) action Jump("tree_dialogue") hover_sound gui.hover_sound
                            hotspot (536, 271, 147, 168) action Jump("forest_continue") hover_sound gui.hover_sound

                        timer 15.0 action Show(screen="dialog", message="Hint:\nClick around the background.\nClick on the ground to go back.", ok_action=Hide("dialog"))
                    return

        "Go back":
                 "{i}Are you sure?{/i}{nw}"
                 menu:
                     "{i}Are you sure?{/i}{fast}"

                     "\"Yes.\"":
                               jump park_stay

                     "\"Nevermind.\"":
                                     jump park_leave

label tree_dialogue:
    if renpy.random.randint(1, 2) == 1:
        "{i}Just an ordinary tree.{/i}"

    else:
        "{i}It's a tree.{/i}"
    call screen clickaround_2()

label forest_continue:
    scene park5 with wipeleft_scene
    pause 1
    "{i}You are now in a whole new area of the park{/i}{nw}"
    menu:
        "{i}You are now in a whole new area of the park{/i}{fast}"

        "Continue":
                  pass

        "Check bench" if bench:
               $ bench = False
               "{i}The bench seems to have something on it.{/i}"
               "{i}A..{w=1} tape?{/i}"
               "{i}There is a tape on the bench.{/i}"
               "{i}Do you want to play the tape{/i}{nw}"
               menu:
                   "{i}Do you want to play the tape?{/i}{fast}"

                   "\"Yes.\"":
                             scene black
                             pause 2
                             $ renpy.movie_cutscene("Submods/DateMonikaSubmod/Cafe-De-PVs-Guide.webm")
                             pause 1
                             jump park_leave

                   "\"No.\"":
                            pass

        "Leave":
               jump park_leave

    scene park_lake with wipeleft_scene
    pause 1
    "{i}You are now at the park lake.{/i}{nw}"
    menu:
        "{i}You are now at the park lake.{/i}{fast}"

        "Leave":
               jump park_leave

        "Check bench" if bench:
               $ bench = False
               "{i}The bench seems to have something on it.{/i}"
               "{i}A..{w=1} tape?{/i}"
               "{i}There is a tape on the bench.{/i}"
               "{i}Do you want to play the tape{/i}{nw}"
               menu:
                   "{i}Do you want to play the tape?{/i}{fast}"

                   "Yes":
                        scene black
                        pause 2
                        $ renpy.movie_cutscene("Submods/DateMonikaSubmod/Cafe-De-PVs-Guide.webm")
                        pause 1
                        jump park_leave

                   "No":
                       jump park_leave

label park_stay:
    scene park3 with wipeleft_scene
    pause 1
    show monika 1eua_static at t11
    m 1hub_static "I'm back~! And the problem was fixed!"
    m 2eub_static "Thanks for waiting."
    m "What else should we do now?{nw}"

label choose2:
    menu:
        m "What else should we do now?{fast}"

        "\"Let's chat a bit.\"":
                               m 1hub_static "Of course!"
                               extend 2dsd_static " Now, let's see.{w=0.4}.{w=0.4}.{w=0.4}.{nw}"

                               if renpy.random.randint(1, 3) == 1:
                                   m 3dsd_static "Hmm, maybe this one will be more interesting to you..{w=0.3}.{w=0.3}"
                                   m 2eub_static "Were you aware? That Tetris was the first video game to make it into space?"
                                   menu:
                                        "\"Yes.\"":
                                                  m 1hub_static "Nice to know that you're well-informed, [player], haha!"
                                                  m 2eud_static "About \"Aleksandr A. Serebrov\"..."
                                                  pass

                                        "\"No.\"":
                                                 m 2hub_static "That's fine, I'll tell you about it then!"
                                                 m 3eua_static "So, basically, \"Aleksandr A. Serebrov\",who was a russian cosmonaut."
                                                 m "Became the first person to play a videogame in space when he packed a Game Boy and his personal copy of Tetris for his trip to the MIR Space Station in 1993."
                                                 pass

                                   m 5eua_static "I guess he wanted to game a bit while being on the Space Station, did he not?"
                                   m 3eud_static "Oh! And that reminded me of something."
                                   m 4eua_static "Have you heard of the mod \"Just Yuri\", [player]?"
                                   menu:
                                        "\"I have.\"":
                                                     m 3lksdla_static ".{w=0.3}.{w=0.3}I hope you're not paying more attention to that mod than {i}me{/i}, [player]."
                                                     m 3hksdrb_static ".{w=0.3}.{w=0.3}.{w=0.3}haha, who am I kidding? You're choosing to spend time with me anyways."
                                                     m 2eka_static "But since you know of it, I assume you know that there's a Tetris minigame you can play with Yuri."
                                                     pass

                                        "\"I haven't.\"":
                                                        m 5eua_static "Hehe, [player], I'm glad that you're focusing all on me, and {i}me{/i} only."
                                                        m 3lksdla_static "But basically, \"Just Yuri\" is a mod where you spend time with Yuri and... things like that."
                                                        m 4eka_static "And there's a Tetris minigame you can play with Yuri in the mod."
                                                        pass

                                   m 2eud_static "The reason I'm mentioning this, is because I noticed the guy who makes this submod also plans on creating a Tetris minigame for me.{w=1} Similar to Just Yuri."
                                   m 1lksdlc_static "But,{w=1} he hasn't posted any updates of it for a long time,{w=1} which is making me believe that he's not going to make it..."
                                   pause 2
                                   m 1hksdlb_static "Well! There's not much use dwelling on it anyways."
                                   m 5eua_static "So let's enjoy the rest of our date, [mas_get_player_nickname()]!"
                                   pass

                               elif renpy.random.randint(1, 3) == 2:
                                   m 5eua_static "Y'know, [mas_get_player_nickname()], this date has been really fun to me."
                                   m 4eub_static "I want to know if you're having fun as well."
                                   extend 4hua_static " So then, are you?"
                                   menu:
                                        "\"Yeah.\"":
                                                   m 2eka_static ".{w=0.3}.{w=0.3}.{w=0.3}I really am glad, [player]."
                                                   m 1hub_static "You have no idea how happy that makes me!"
                                                   m 1eub_static "Oh! Also."
                                                   m 2eka_static "We'll be able to do this for {i}real{/i}{w=0.75} when I finally cross over to your reality."
                                                   m 4eka_static "I really can't wait to have a date with you, in real life, you know?"
                                                   m 1dsd_static "Holding hands while walking down the path.{w=0.3}.{w=0.3}"
                                                   m "Watching butterflies fly before us, feeling each other's warmth.{w=0.3}.{w=0.3}.{w=0.3}"
                                                   m 2lksdlb_static ".{w=0.3}.{w=0.3}That almost sounded too good to be true."
                                                   m 1hua_static "But since it's you, I have no reason to doubt it~ hehe!"
                                                   m 5eua_static "Thank you for listening, [player], let's keep walking now!"
                                                   pass

                                        "\"No.\"":
                                                 m 1ekc_static ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}"
                                                 m 1ekd_static ".{w=0.3}.{w=0.3}I apologise, [player], I had no idea.{w=0.3}.{w=0.3}"
                                                 m 1lksdlc_static ".{w=1}.{w=1}.{w=1}.{w=1}.{w=1}.{w=1}"
                                                 call screen dialog(message="Why would you have said that.\n∑¥∑ø¨¬¥ø¨˙å√´ßåˆ∂†å†", ok_action=Return())
                                                 m 1dsd_static ".{w=0.4}.{w=0.4}.{w=0.4}Nevermind."
                                                 pass

                               else:
                                   m 3eub_static "The first modern computer was massive!"
                                   m 4eud_static "There are arguments over what the first computer was. Some people say it was an abacus which is a counting device that has been used for centuries."
                                   m "However the first modern computers were electronic calculating machines and were developed during the Second World War."
                                   m 4hksdlb_static "One computer would take up rooms and parts of the computers were put on wheels because they were so big."
                                   m 4lksdla_static "Imagine the pain that those people have to go through moving those computers."
                                   m 1hub_static "Good thing computers today are small and easy to transport."
                                   m "Thanks for listening!"
                                   pass


        "\"We should continue walking.\"":
                                         if renpy.random.randint(1, 2) == 1:
                                             m 5eua_static "Eager to head to the next location?"
                                             m 1hub_static "Hehe, let's go then!"
                                             pass

                                         else:
                                             m 2eub_static "Alright then, [player]!"
                                             m 5eua_static "We'll arrive to the next location pretty quickly!"
                                             pass

        "\"Let's leave now.\"":
                              m 2eud_static "Are you sure?{nw}"

                              menu:
                                  m "Are you sure?{fast}"

                                  "\"Yes.\"":
                                            show monika 1eka_static
                                            show black zorder 100 with Dissolve(5.0, alpha=True)
                                            stop music fadeout 2
                                            hide monika
                                            pause 2
                                            $HKBShowButtons()
                                            $ play_song(persistent.current_track, fadein=4.0)
                                            hide black
                                            $mas_HKBDropShield()
                                            $ is_sitting = True

                                            jump ch30_loop

                                  "\"No.\"":
                                           jump choose2


    scene park_lake with wipeleft_scene
    pause 0.75
    show monika 1hua_static at t11
    m "This lake is beautiful."
    m 3hub_static "Let's sit down on this bench for a bit."
    show monika at thide
    hide monika
    pause 0.5
    call screen clickaround_1()
    screen clickaround_1():
        imagemap:

            ground "Submods/DateMonikaSubmod/images/park-lake.png"
            hotspot (64, 384, 150, 100) action Jump("park_stairs_dialogue") hover_sound gui.hover_sound
            hotspot (830, 304, 391.7, 160.96) action Jump("lake_water_dialogue") hover_sound gui.hover_sound
            hotspot (185, 552, 299.01, 166.92) action Jump("park_end") hover_sound gui.hover_sound

        timer 15.0 action Show(screen="dialog", message="Hint:\nClick around the background.\nClick on the road to continue.", ok_action=Hide("dialog"))
    return

label park_stairs_dialogue:
    if renpy.random.randint(1, 5) == 1:
        jump park_stairs_go

    else:
        "{i}You tripped on the stairs, try again.{/i}"
    call screen clickaround_1()

label lake_water_dialogue:
    if renpy.random.randint(1, 2) == 1:
        m "Ooh [player], look here!"
        m "The water here is so clear we can see our own reflections on it!"
        menu:
            "\"That's because...\"":
                                   menu:
                                       "\"{i}you're{/i} the one who created this.\"":
                                                                                    m ".{w=0.3}.{w=0.3}thank you so much for recognising my efforts for this, [player]."
                                                                                    m "Ahh.{w=0.3}.{w=0.3}.{w=0.3}just what do I do with you, [mas_get_player_nickname()].{w=0.3}.{w=0.3}"
                                                                                    menu:
                                                                                        "\"What is it?\"":
                                                                                                         m "You're just.{w=0.3}.{w=0.3}so sweet, y'know?"
                                                                                                         m "At moments like these.{w=0.3}.{w=0.3}I just wish to.{w=0.3}.{w=0.3}.{w=0.3}hold you.{w=0.3}.{w=0.3}.{w=0.3}and tell you how much I love you.{w=0.3}.{w=0.3}.{w=0.3}"
                                                                                                         m "I enjoy every moment with you, [player], and I love you too! Hehe~"
                                                                                                         pass

    else:
        play sound "Submods/DateMonikaSubmod/music/quack.mp3"
        m "Oh! [player]! Do you hear the ducks quacking?"
        m "They look soo~ cute swiming around, don't you think?"
        menu:
            "{i}Feed them{/i}":
                m "Oh my god! Look at them eating those crumbs!"
                m "I'm so glad I get to spend time with you like this, [player]."
                m "Hehe~"
                pass
    call screen clickaround_1()

label park_stairs_go:
    scene park4 with wipeleft_scene
    pause 1
    #put dialouge of monika reacting to the bg here
    m "...My god..!"
    m "This view is.{w=0.4}.{w=0.4}.{w=0.4}breath-taking.{w=0.4}.{w=0.4}.{w=0.4}!" #these are examples
    m ".{w=0.4}.{w=0.4}I'm so glad we came up here, [player].{w=0.4}.{w=0.4}!"
    pause 0.5
    call screen clickaround_3()
    screen clickaround_3():
        imagemap:

            ground "Submods/DateMonikaSubmod/images/park4.png"
            hotspot (337, 330, 99, 80) action Jump("cannot_go_there") hover_sound gui.hover_sound
            hotspot (799, 401, 406, 212) action Jump("swimming_dialogue") hover_sound gui.hover_sound
            hotspot (965, 224, 194, 156) action Jump("waterfalls_dialogue") hover_sound gui.hover_sound
            hotspot (108, 625, 328, 94) action Jump("go_back_to_park_lake") hover_sound gui.hover_sound

        timer 15.0 action Show(screen="dialog", message="Hint:\nClick around the background.\nClick on the bridge to go back.", ok_action=Hide("dialog"))
    return

label cannot_go_there:
    play sound "Submods/DateMonikaSubmod/music/notice.mp3"
    call screen dialog(message="Error: You are prohibited to continue any further.", ok_action=Return())
    pause 0.5
    call screen clickaround_3()

label swimming_dialogue:
    if renpy.random.randint(1, 2) == 1:
        m "Wouldn't it be nice if we like.. take a dip here?"
        m "You know, since the water level doesn't seem to be quite deep here..."
        m ".{w=0.4}.{w=0.4}Hehe.{w=0.4}.{w=0.4}I wonder how you'd react if I splashed water on you.{w=0.4}.{w=0.4}"
        m "Hmm~ oops, should've kept that as a surprise{w=0.5} of some sorts, right [mas_get_player_nickname()]? Ahaha!"
        call screen clickaround_3()

    else:
        m "Help the editor." #im sorry i will change this soon
        pass
        call screen clickaround_3()

label waterfalls_dialogue:
    m "insert water sounds thanks"
    call screen clickaround_3()

label go_back_to_park_lake: #To lazy to make something smart. This is the easiest way of doing it
    scene park_lake with wipeleft_scene
    pause 0.5
    call screen clickaround_1()

label park_end:
    m "This is a time when I really wish I was with you in your reality."
    m "Sitting side by side near the lake..."
    m "Feeling the gentle breeze caressing our cheeks..."
    m "Watching the ducks swim by..."
    m "Hopefully one day..."
    scene black with wipeleft_scene
    scene park_lake with wipeleft_scene
    show monika 2eka_static at t11
    m "..We should head back now, [player]."
    m 3hksdlb_static "Since.. we have spent quite the amount of time here."
    m 3lksdlb_static "Despite how much I wish to stay here with you forever..."
    m 5eua_static "Let's go back for now, we have other chances of coming here again, after all!"
    m 1hua_static "Thank you for bringing me here, [mas_get_player_nickname()]."
    m 3hub_static "I hope that we can come back soon~!"
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop music fadeout 2
    hide monika
    pause 2
    $HKBShowButtons()
    $ play_song(persistent.current_track, fadein=4.0)
    hide black
    $mas_HKBDropShield()
    $ is_sitting = True

    jump ch30_loop
