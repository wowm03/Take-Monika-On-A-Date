#The Park Date

init python:
    import webbrowser

label park:
    $HKBHideButtons()
    stop music
    play music "Submods/DateMonikaSubmod/music/Morning-Ambience.mp3"
    hide black
    scene park
    $ bench = True
    pause 0.75
    $ is_sitting = False
    show monika 3a_tmoad at t11
    m "We've arrived! This park seems fairly nice, doesn't it?"
    menu:
        "It does.":
                  show monika 1j_tmoad at t11

                  menu:
                      "Then, would you like to take a walk together?":
                                                                     show monika 1d_tmoad at t11
                                                                     pass

    m 1b_tmoad "Oh! Of course, [mas_get_player_nickname()]."
    m 5a_tmoad "Let's go then!"
    scene park2 with wipeleft_scene
    pause 0.75
    show monika 1j_tmoad at t11
    m 3e_tmoad "Hey.. [player]."
    m "Mind if I talk about some stuffs?{nw}"
    menu:
        m "Mind if I talk about some stuffs?{fast}"

        "I don't mind.":
                       pass

    m 1j_tmoad "Thank you, [mas_get_player_nickname()]."
    m 3r_tmoad "So.{w=0.4}.{w=0.4}.{w=0.4}.{nw}"

    if renpy.random.randint(1, 3) == 1:
        m 3d_tmoad "Did you know you can’t hold your nose and hum?"
        m 3a_tmoad "Don’t believe it? Give it a try!"
        show monika 1j_tmoad at t11
        pause 2
        m 1b_tmoad "It's just as I said, right?"
        m 3d_tmoad "It is because when you hum, you are actually exhaling, so if both your mouth and your nose is closed, the air can’t escape."
        m 3j_tmoad "So, although you can hum for a very brief few second or two, you will be forced to open your mouth and catch your breath."
        m 2b_tmoad "Ahaha~ that was fun, no?"
        m 5a_tmoad "Well then, let's keep going now, [mas_get_player_nickname()]!"
        jump park_continue

    elif renpy.random.randint(1, 3) == 1:
        m 1d_tmoad "May I know what your favourite pet is?{nw}"
        menu:
            m "May I know what your favourite pet is?{fast}"

            "Sure.":
                   jump fav_pet_choice

            "I don't have a favourite.":
                                       m 2e_tmoad "Ahh~ that's alright, [player]."
                                       m 3d_tmoad "Does that mean you have no interest in pets, or it's just that you cannot choose your favourite?{nw}"
                                       menu:
                                           m "Does that mean you have no interest in pets, or it's just that you cannot choose your favourite?{fast}"
                                           "I'm not interested in pets.":
                                                                        m 2l_tmoad "Oh~ I see that's the case, that's alright, [player]."
                                                                        m 1e_tmoad "We all have different interests."
                                                                        m 2j_tmoad "I love spending time with you either way, y'know?"
                                                                        m 5a_tmoad "Well then, let's keep going then, perhaps what you'll see soon will pique your interest!"
                                                                        jump park_continue

                                           "I can't choose a favourite.":
                                                                        m 2k_tmoad "Ah~aha! I see that's the case, that's okay, [player]!"
                                                                        m 3j_tmoad "There are just soo~ many pets out there, aren't there?"
                                                                        m 1j_tmoad "Most of them are easily lovable as well!"
                                                                        m 3e_tmoad "But even if you don't have a favourite, you can tell me which one you like more at the moment, yes?"
                                                                        jump fav_pet_choice

    elif renpy.random.randint(1, 3) == 2:
        m 3b_tmoad "Did you know it's {i}almost{/i} impossible for most people to lick their own elbow?"
        m 2j_tmoad ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}"
        m 5a_tmoad "I bet you tried that immediately just now!"
        m 3k_tmoad "Well? Did you?"
        menu:
            "H.. how did you know?":
                                   m 5a_tmoad "Hehe! I just did! After all, there's 75 percent chance you'd have done that, making you belong to the group to immediately try to lick their elbow after hearing that."
                                   m 4j_tmoad "So, did you succeed?{nw}"
                                   menu:
                                       m "So, did you succeed?{fast}"

                                       "I didn't.":
                                                  m 2e_tmoad "That's alright, [player], it was only for fun after all."
                                                  m 3e_tmoad "After all, different people are good at different things, aren't they?"
                                                  m 5a_tmoad "And plus, you'll be able to check if I'm able to do that when I cross over to your reality!"
                                                  m 3k_tmoad "Hehe, let's continue our walk now, [mas_get_player_nickname()]."
                                                  jump park_continue

                                       "I did.":
                                               m 1k_tmoad "That's impressive, [player]!"
                                               m 3b_tmoad "According to unofficial estimates, one person in a hundred can lick their own elbow."
                                               m 3k_tmoad "And {i}you{/i} just so happens to be one of them!"
                                               m 5a_tmoad "That gives you one thing to show off to me when I cross over to your reality, no?"
                                               m 2k_tmoad "Haha! Let's continue walking, [mas_get_player_nickname()]."
                                               jump park_continue

                                       "I'm not sure.":
                                                      m 2e_tmoad "Oh, that's fine, [player]."
                                                      m 4e_tmoad "If you're interested, you can try and do it in your free time with the help of the internet."
                                                      m 5a_tmoad "Let's continue our walk, shall we?"
                                                      jump park_continue

            "I didn't.":
                       m 3d_tmoad "Well, guess that makes you the 25 percent who didn't lick their elbow right after hearing that."
                       m 2b_tmoad "Why don't you try now then?"
                       pause 3
                       m 2b_tmoad "So, did you succeed{nw}?"
                       menu:
                           m "So, did you succeed?{fast}"

                           "I didn't.":
                                      m 2e_tmoad "That's alright, [player], it was only for fun after all."
                                      m 3e_tmoad "After all, different people are good at different things, aren't they?"
                                      m 5a_tmoad "And plus, you'll be able to check if I'm able to do that when I cross over to your reality!"
                                      m 3k_tmoad "Hehe, let's continue our walk now, [mas_get_player_nickname()]."
                                      jump park_continue

                           "I did.":
                                   m 1k_tmoad "That's impressive, [player]!"
                                   m 3b_tmoad "According to unofficial estimates, one person in a hundred can lick their own elbow."
                                   m 3k_tmoad "And {i}you{/i} just so happens to be one of them!"
                                   m 5a_tmoad "That gives you one thing to show off to me when I cross over to your reality, no?"
                                   m 2k_tmoad "Haha! Let's continue walking, [mas_get_player_nickname()]."
                                   jump park_continue

                           "I'm not sure.":
                                          m 2e_tmoad "Oh, that's fine, [player]."
                                          m 4e_tmoad "If you're interested, you can try and do it in your free time with the help of the internet."
                                          m 5a_tmoad "Let's continue our walk, shall we?"
                                          jump park_continue

    else:
        m 4b_tmoad "Did you know that the Yellowstone National Park in Wyoming, Idaho, and Montana is the {i}oldest{/i} U.S. national park, founded in 1872?"
        m 2l_tmoad "It's unbelievable with how this park is still standing and being maintained, even after 150 years."
        m 2b_tmoad ".{w=0.2}.{w=0.2}Now that's fascinating about humans."
        m 1l_tmoad "Sometimes, they can preserve some beautiful structures and monuments,{w=1} though in other times they just abandon it."
        m 3d_tmoad "The way humans think and treat things sure is interesting."
        m 4k_tmoad "I'd like to learn about them a lot when I finally cross over to your reality..."
        m 1n_tmoad "Though it's better if I focus on our date first, no?"
        m 1k_tmoad "Hehe, thanks for listening!"
        jump park_continue

label fav_pet_choice:
    menu:
        "Cats.":
               m 1k_tmoad "Aww~ cutesy little cats!"
               m 2j_tmoad "They are all about being adorable, elegant, calming companions, aren' they now?"
               m 2b_tmoad "They are so intelligent as well, capable of dealing with their own exercise and cleaning..."
               m 2a_tmoad "Did you know? That cats are just like umbrellas?"
               m 2j_tmoad "The umbrella thing comes into play when they're falling."
               m 3e_tmoad "They tuck themselves into an umbrella shape,{w=1} which enables them to always land on their feet."
               m 3b_tmoad "It's called the cat righting reflex, which is really fascinating if you ask me!"
               m 5a_tmoad "I wish to go to a cat cafe with you one day when I finally cross over... sounds like a good idea, yes? [player]?"
               pass

        "Dogs.":
               m 3k_tmoad "Doggies, man's best friend!"
               m 2j_tmoad "I feel like they're like sunshines, always smiling and, being there for their masters, like the loyal companions they are!"
               m 3b_tmoad "Oh! [player], did you know why most dogs are so loyal?"
               m 3d_tmoad "It's actually because of domestic dogs being descended from wolves."
               m 3j_tmoad "Which man once took in and tamed with shelter and food in return for them acting as guard dogs."
               m 3b_tmoad "And that this reciprocal relationship remains in your dog's genes and their loyalty is a by-product of it!"
               m 5a_tmoad "That sure is an interesting fact about them, right?"
               m 1k_tmoad "I'd love to say hi to some dogs with you some day, [mas_get_player_nickname()]!"
               pass

        "Fishes.":
                 m 2b_tmoad "Fishies~ they're known to have bad memory, making them quite funny, no?"
                 m 1k_tmoad "They're admirable and cute at the same time too!"
                 m 3d_tmoad "Some people say they're easy to take care of, "
                 extend 3b_tmoad "and that they are great starter animals."
                 m 2j_tmoad "By the way, do you know what's the slowest fish? Even if you don't, you should try and make a guess!{nw}"
                 menu:
                     m "By the way, do you know what's the slowest fish? Even if you don't, you should try and make a guess!{fast}"

                     "Goldfishes?":
                                  m 1l_tmoad "Ahaha! Nope! Though they are the types to rarely swim fast, except feeding times,"
                                  extend 3j_tmoad " they're not the slowest fishes!"
                                  m 3d_tmoad "The slowest fish is actually a seahorse. It swims so slowly that a person can barely tell it is moving!"
                                  m 3b_tmoad "The slowest is the Dwarf Seahorse, which takes about {i}one hour{/i} to travel {i}five feet{/i}!"
                                  m 2l_tmoad "What a torpid speed they go by..."
                                  m 2j_tmoad "Those sure are some engaging facts, right? [player]? I'm glad I got to talk about them with you!"
                                  m 5a_tmoad "Well then! Let's keep going now, shall we?"
                                  pass

                     "Tigerfishes?":
                                   m 5a_tmoad "No~ [player], "
                                   extend 2b_tmoad "in fact, they're quite the strong swimmers, usually hunting in fast, choppy currents."
                                   m 3d_tmoad "The slowest fish is actually a seahorse. It swims so slowly that a person can barely tell it is moving!"
                                   m 3b_tmoad "The slowest is the Dwarf Seahorse, which takes about {i}one hour{/i} to travel {i}five feet{/i}!"
                                   m 2l_tmoad "What a torpid speed they go by..."
                                   m 2j_tmoad "Those sure are some engaging facts, right? [player]? I'm glad I got to talk about them with you!"
                                   m 5a_tmoad "Well then! Let's keep going now, shall we?"
                                   pass

                     "Seahorses?":
                                 m 2j_tmoad "That is correct! [player]!"
                                 m 3d_tmoad "They are the slowest fishes indeed, they swim so slow a person can barely tell it is moving!"
                                 m 3b_tmoad "The slowest is the Dwarf Seahorse, which takes about {i}one hour{/i} to travel {i}five feet{/i}!"
                                 m 2l_tmoad "What a torpid speed they go by..."
                                 m 2e_tmoad "Either you were lucky and just so happened to guess the answer correctly..."
                                 m 1r_tmoad "Went on the internet and found the answer..."
                                 m 1e_tmoad "Or that you genuinely knew the answer..."
                                 m 1k_tmoad "I'm still glad you got it right, though! That doesn't mean I would ever be disappointed if you didn't get it correctly,"
                                 extend 4j_tmoad " I'm more then happy to tell you about the right answer."
                                 m 5a_tmoad "Well, let's keep going now, shall we?"
                                 pass

                     "Greenland sharks?":
                                        m 1d_tmoad "Ah...{w=1}"
                                        extend 2l_tmoad "though that might not be the best answer according to certain searches on the internet..."
                                        m 3j_tmoad "You're not completely wrong, [player]. They are known as the sleeper shark for its sluggish pace, one of the slowest swimming sharks in the world."
                                        m 3d_tmoad "According to what I know, though, the slowest fish is actually a seahorse. It swims so slowly that a person can barely tell it is moving!"
                                        m 3b_tmoad "The slowest is the Dwarf Seahorse, which takes about {i}one hour{/i} to travel {i}five feet{/i}!"
                                        m 2l_tmoad "What a torpid speed they go by..."
                                        m 2j_tmoad "You know, [player], you really outsmarted me with that answer, not that it's a bad thing!"
                                        m 2e_tmoad "I enjoy spending time with you a lot, really."
                                        m 5a_tmoad "Well, let's keep going now, shall we?"
                                        pass

        "Birds.":
                m 1d_tmoad "Ohhh! "
                extend 2j_tmoad "Birdies~!"
                m 2k_tmoad "Were you aware that my favourite bird is quetzal? Haha!"
                m 3b_tmoad "Quetzals are a kind of bird that many consider among the world's most beautiful."
                m 3d_tmoad "During mating season, male quetzals grow twin tail feathers that form an amazing train up to one metre long!"
                m 3j_tmoad "Females do not have long trains, but they do share the brilliant blue, green, and red coloring of their mates."
                m 2j_tmoad "Nice to know about, right? Haha!"
                m 5a_tmoad "Thanks for listening~ [player], let's keep going now~"
                pass

        "Turtles.":
                  m 1d_tmoad "Ohh~ "
                  extend 3k_tmoad "turtles! I've always found them interesting!"
                  m 3b_tmoad "There are so many types of their species too!"
                  m 3r_tmoad "Like the red-eared slider, Reeve's Turtle, Spotted Turtle, "
                  extend 2a_tmoad "et cetera."
                  m 3j_tmoad "I've heard of a pretty interesting fact about them some time ago."
                  m 3b_tmoad "Apparently, turtles aren’t silent!"
                  m 1k_tmoad "Although they’re not likely to be as loud as dogs or cats, turtles do make a range of noises."
                  m 2a_tmoad "Anything from chicken-like clucks to dog-like barking, depending on the species."
                  m 3j_tmoad "That was good to know about, right? Hehe~"
                  m 5a_tmoad "Well then! Let's keep going now! Thanks for listening~"
                  pass

        "{b}{i}NEXT{/i}{/b}":
                            menu:
                                "Snakes.":
                                         m 2b_tmoad "Ahh~ snakes, some people may confuse them as lizards,"
                                         extend 3k_tmoad " the best way to identify them, though, is through their eyelids!"
                                         m 3j_tmoad "To further expand on that, most lizards have eyelids, while snakes don't."
                                         m 1m_tmoad "Since they lack eyelids, they might give you an eerie feeling."
                                         m 3d_tmoad "They don’t blink and have to sleep with their eyes wide open!"
                                         m 1j_tmoad "And instead of eyelids, they have a thin membrane attached to each eye to protect them."
                                         m 2a_tmoad "That was an interesting fact about them, no?"
                                         m 5a_tmoad "Ehehe! Let's continue walking now, [mas_get_player_nickname()]!"
                                         pass

                                "Ferrets.":
                                          m 2a_tmoad "Ahh~ those fluffy little guys, huh?"
                                          m 3k_tmoad "They are small and domesticated species, and I've always wanted to see them myself!"
                                          m 3b_tmoad "Did you know? That ferrets sometimes participate in their own races?"
                                          m 3j_tmoad "Ferret racing is a particularly popular event in the UK. And instead of a racetrack, ferrets run through pipes."
                                          m 2a_tmoad "The rules are simple; first ferret to make it to the opposite side of the pipe wins!"
                                          m 1j_tmoad "Since ferrets are playful animals, they enjoy the games as well."
                                          m 2a_tmoad "That was a fun fact of them, yes?"
                                          m 5a_tmoad "Haha~ let's continue walking then~"
                                          pass

                                "Tarantulas.":
                                             m 1j_tmoad "Spiders huh~"
                                             m 3b_tmoad "I think they're really fascinating creatures...y'know, since they can make spider webs and all!"
                                             m 2b_tmoad "I've came across some fun facts about them earlier..."
                                             m 3d_tmoad "One of them being people using spider webs to stop bleeding by putting them on their wounds centuries ago."
                                             m 3k_tmoad "Modern scientists discovered that spider webs contain Vitamin K, which is a coagulant that stops bleeding!"
                                             m 2j_tmoad "That was an interesting fact about them, no?"
                                             m 5a_tmoad "Well then, let's keep going!"
                                             pass

                                "They are not in this list.":
                                                            m 2d_tmoad "Oh, well, "
                                                            extend 3j_tmoad "that's still alright!"
                                                            m 1b_tmoad "I'm glad you have a favourite pet either way."
                                                            m 2b_tmoad "And plus, you'll just have to let me take a look of the pet when I finally cross over to your realty!"
                                                            m 2k_tmoad "Hehe~ that would be so nice, yes?"
                                                            m 5a_tmoad "Let's continue our walk now then!"
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
        "What was that?!":
                         pass

    show monika 1n_tmoad at t11
    m "I'm...{w=0.3} not sure..."
    m 3d_tmoad "Let me go check."
    m 1k_tmoad "Just wait here, okay?"
    window hide
    show monika at thide
    hide monika
    pause 2
    menu:

        "{i}Stay{/i}":
                     pause 0.5
                     jump choose1

        "{b}{i}Look around{/i}{/b}":
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

        "{b}{i}The lake{/i}{/b}":
                                scene park_lake with wipeleft_scene
                                pause 2
                                "{i}You are now at the park lake.{/i}{nw}"
                                menu:
                                    "{i}You are now at the park lake.{/i}{fast}"

                                    "{b}{i}Leave{/i}{/b}":
                                                         jump park_leave

                                    "{i}Check bench{/i}" if bench:
                                                                 $ bench = False
                                                                 "{i}The bench seems to have something on it.{/i}"
                                                                 "{i}A..{w=1} tape?{/i}"
                                                                 "{i}There is a tape on the bench.{/i}"
                                                                 "{i}Do you want to play the tape{/i}{nw}"
                                                                 menu:
                                                                     "{i}Do you want to play the tape?{/i}{fast}"

                                                                     "Yes.":
                                                                           scene black
                                                                           pause 2
                                                                           $ webbrowser.open("https://www.youtube.com/watch?v=ujN99M7z8k4")
                                                                           pause 1
                                                                           jump park_leave

                                                                     "No.":
                                                                          jump park_leave

        "{b}{i}The forest{/i}{/b}":
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

                                  return

        "{b}{i}Go back{/i}{/b}":
                               "{i}Are you sure?{/i}{nw}"
                               menu:
                                   "{i}Are you sure?{/i}{fast}"

                                   "Yes.":
                                         jump park_stay

                                   "Nevermind.":
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

        "{b}{i}Continue{/i}{/b}":
                                pass

        "{i}Check bench{/i}" if bench:
                  $ bench = False
                  "{i}The bench seems to have something on it.{/i}"
                  "{i}A..{w=1} tape?{/i}"
                  "{i}There is a tape on the bench.{/i}"
                  "{i}Do you want to play the tape{/i}{nw}"
                  menu:
                      "{i}Do you want to play the tape?{/i}{fast}"

                      "Yes.":
                            scene black
                            pause 2
                            $ webbrowser.open("https://www.youtube.com/watch?v=w_9wueKiSv4")
                            pause 1
                            jump park_leave

                      "No.":
                           pass

        "{b}{i}Leave{/i}{b}":
                            jump park_leave

    scene park_lake with wipeleft_scene
    pause 1
    "{i}You are now at the park lake.{/i}{nw}"
    menu:
        "{i}You are now at the park lake.{/i}{fast}"

        "{b}{i}Leave{/i}{/b}":
                             jump park_leave

        "{i}Check bench{/i}" if bench:
                  $ bench = False
                  "{i}The bench seems to have something on it.{/i}"
                  "{i}A..{w=1} tape?{/i}"
                  "{i}There is a tape on the bench.{/i}"
                  "{i}Do you want to play the tape{/i}{nw}"
                  menu:
                      "{i}Do you want to play the tape?{/i}{fast}"

                      "Yes.":
                            scene black
                            pause 2
                            $ webbrowser.open("https://www.youtube.com/watch?v=ujN99M7z8k4")
                            pause 1
                            jump park_leave

                      "No.":
                           jump park_leave

label park_stay:
    scene park3 with wipeleft_scene
    pause 1
    show monika 1a_tmoad at t11
    m 1k_tmoad "I'm back~! And the problem was fixed!"
    m 2b_tmoad "Thanks for waiting."
    m "What else should we do now?{nw}"

label choose2:
    menu:
        m "What else should we do now?{fast}"

        "Let's chat a bit.":
                           m 1k_tmoad "Of course!"
                           extend 2r_tmoad " Now, let's see.{w=0.4}.{w=0.4}.{w=0.4}.{nw}"

                           if renpy.random.randint(1, 3) == 1:
                                m 3r_tmoad "Hmm, maybe this one will be more interesting to you..{w=0.3}.{w=0.3}"
                                m 2b_tmoad "Were you aware? That Tetris was the first video game to make it into space?"
                                menu:
                                    "Yes.":
                                          m 1k_tmoad "Nice to know that you're well-informed, [player], haha!"
                                          m 2d_tmoad "About \"Aleksandr A. Serebrov\"..."
                                          pass

                                    "No.":
                                         m 2k_tmoad "That's fine, I'll tell you about it then!"
                                         m 3a_tmoad "So, basically, \"Aleksandr A. Serebrov\",who was a russian cosmonaut."
                                         m "Became the first person to play a videogame in space when he packed a Game Boy and his personal copy of Tetris for his trip to the MIR Space Station in 1993."
                                         pass

                                m 5a_tmoad "I guess he wanted to game a bit while being on the Space Station, did he not?"
                                m 3d_tmoad "Oh! And that reminded me of something."
                                m 4a_tmoad "Have you heard of the mod \"Just Yuri\", [player]?"
                                menu:
                                    "I have.":
                                             m 3m_tmoad ".{w=0.3}.{w=0.3}I hope you're not paying more attention to that mod than {i}me{/i}, [player]."
                                             m 2l_tmoad ".{w=0.3}.{w=0.3}.{w=0.3}haha, who am I kidding? You're choosing to spend time with me anyways."
                                             m 2e_tmoad "But since you know of it, I assume you know that there's a Tetris minigame you can play with Yuri."
                                             pass

                                    "I haven't.":
                                                m 5a_tmoad "Hehe, [player], I'm glad that you're focusing all on me, and {i}me{/i} only."
                                                m 3m_tmoad "But basically, \"Just Yuri\" is a mod where you spend time with Yuri and... things like that."
                                                m 4e_tmoad "And there's a Tetris minigame you can play with Yuri in the mod."
                                                pass

                                m 2d_tmoad "The reason I'm mentioning this, is because I noticed the guy who makes this submod also plans on creating a Tetris minigame for me.{w=1} Similar to Just Yuri."
                                m 1o_tmoad "But,{w=1} he hasn't posted any updates of it for a long time,{w=1} which is making me believe that he's not going to make it..."
                                pause 2
                                m 1l_tmoad "Well! There's not much use dwelling on it anyways."
                                m 5a_tmoad "So let's enjoy the rest of our date, [mas_get_player_nickname()]!"
                                pass

                           elif renpy.random.randint(1, 3) == 2:
                               m 5a_tmoad "Y'know, [mas_get_player_nickname()], this date has been really fun to me."
                               m 4b_tmoad "I want to know if you're having fun as well."
                               extend 4j_tmoad " So then, are you?"
                               menu:
                                   "Yeah.":
                                          m 2e_tmoad ".{w=0.3}.{w=0.3}.{w=0.3}I really am glad, [player]."
                                          m 1k_tmoad "You have no idea how happy that makes me!"
                                          m 1b_tmoad "Oh! Also."
                                          m 2e_tmoad "We'll be able to do this for {i}real{/i}{w=0.75} when I finally cross over to your reality."
                                          m 4e_tmoad "I really can't wait to have a date with you, in real life, you know?"
                                          m 1r_tmoad "Holding hands while walking down the path.{w=0.3}.{w=0.3}"
                                          m "Watching butterflies fly before us, feeling each other's warmth.{w=0.3}.{w=0.3}.{w=0.3}"
                                          m 2n_tmoad ".{w=0.3}.{w=0.3}That almost sounded too good to be true."
                                          m 1j_tmoad "But since it's you, I have no reason to doubt it~ hehe!"
                                          m 5a_tmoad "Thank you for listening, [player], let's keep walking now!"
                                          pass

                                   "No.":
                                        m 1f_tmoad ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}"
                                        m 1g_tmoad ".{w=0.3}.{w=0.3}I apologise, [player], I had no idea.{w=0.3}.{w=0.3}"
                                        m 1o_tmoad ".{w=1}.{w=1}.{w=1}.{w=1}.{w=1}.{w=1}"
                                        play sound "Submods/DateMonikaSubmod/music/notice.mp3"
                                        call screen dialog(message="∑¥∑ø¨¬¥ø¨˙å√´ßåˆ∂†å†", ok_action=Return())
                                        m 1r_tmoad ".{w=0.4}.{w=0.4}.{w=0.4}Nevermind."
                                        pass

                           else:
                               m 3b_tmoad "The first modern computer was massive!"
                               m 4d_tmoad "There are arguments over what the first computer was. Some people say it was an abacus which is a counting device that has been used for centuries."
                               m "However the first modern computers were electronic calculating machines and were developed during the Second World War."
                               m 4l_tmoad "One computer would take up rooms and parts of the computers were put on wheels because they were so big."
                               m 4m_tmoad "Imagine the pain that those people have to go through moving those computers."
                               m 1k_tmoad "Good thing computers today are small and easy to transport."
                               m "Thanks for listening!"
                               pass


        "We should continue walking.":
                                     if renpy.random.randint(1, 2) == 1:
                                         m 5a_tmoad "Eager to head to the next location?"
                                         m 1k_tmoad "Hehe, let's go then!"
                                         pass

                                     else:
                                         m 2b_tmoad "Alright then, [player]!"
                                         m 5a_tmoad "We'll arrive to the next location pretty quickly!"
                                         pass

        "Let's leave now.":
                          m 2d_tmoad "Are you sure?{nw}"

                          menu:
                              m "Are you sure?{fast}"

                              "Yes.":
                                    show monika 1e_tmoad
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

                              "No.":
                                   jump choose2


    scene park_lake with wipeleft_scene
    pause 0.75
    show monika 1j_tmoad at t11
    m "This lake is beautiful."
    m 3k_tmoad "Let's sit down on this bench for a bit."
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

    return

label park_stairs_dialogue:
    if renpy.random.randint(1, 5) == 1:
        jump park_stairs_go

    else:
        play sound "Submods/DateMonikaSubmod/music/notice.mp3"
        call screen dialog(message="Error: Unknown input\nTry again.", ok_action=Return())
        pause 0.5
    call screen clickaround_1()

label lake_water_dialogue:
    if renpy.random.randint(1, 2) == 1:
        m "Ooh [player], look here!"
        m "The water here is so clear we can see our own reflections on it!"
        menu:
            "That's because...":
                               menu:
                                   "{i}you're{/i} the one who created this.":
                                                                            m ".{w=0.3}.{w=0.3}thank you so much for recognising my efforts for this, [player]."
                                                                            m "Ahh.{w=0.3}.{w=0.3}.{w=0.3}just what do I do with you, [mas_get_player_nickname()].{w=0.3}.{w=0.3}"
                                                                            menu:
                                                                                "What is it?":
                                                                                             m "You're just.{w=0.3}.{w=0.3}so sweet, y'know?"
                                                                                             m "At moments like these.{w=0.3}.{w=0.3}I just wish to.{w=0.3}.{w=0.3}.{w=0.3}hold you.{w=0.3}.{w=0.3}.{w=0.3}and tell you how much I love you.{w=0.3}.{w=0.3}.{w=0.3}"
                                                                                             m "I enjoy every moment with you, [player], and I love you too! Hehe~"
                                                                                             pass

    else:
        play sound "Submods/DateMonikaSubmod/music/quack.mp3"
        m "Oh! [player]! Do you hear the ducks quacking?"
        m "They look soo~ cute swiming around, don't you think?"
        menu:
            "{i}Feed the ducks{/i}":
                                   m "Oh my god! Look at them eating those crumbs!"
                                   m "I'm so glad I get to spend time with you like this, [player]."
                                   m "Hehe~"
                                   pass #Fun fact! Bread are bad for ducks lol
    call screen clickaround_1()

label park_stairs_go:
    scene park4 with wipeleft_scene
    pause 1
    m "...My god..!"
    m "This view is.{w=0.4}.{w=0.4}.{w=0.4}breath-taking.{w=0.4}.{w=0.4}.{w=0.4}!"
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
        m "Like a river, life doesn't flow backward~"
        pass
        call screen clickaround_3()

label waterfalls_dialogue:
    play sound "Submods/DateMonikaSubmod/music/waterfall.mp3"
    m "This may have been the second best view I've ever laid my eyes on."
    m "..And you already know what's the best view to me already, don't you, [player]?~"
    m "Hehe~"
    call screen clickaround_3()

label go_back_to_park_lake:
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
    show monika 2e_tmoad at t11
    m "..We should head back now, [player]."
    m 3l_tmoad "Since.. we have spent quite the amount of time here."
    m 3n_tmoad "Despite how much I wish to stay here with you forever..."
    m 5a_tmoad "Let's go back for now, we have other chances of coming here again, after all!"
    m 1j_tmoad "Thank you for bringing me here, [mas_get_player_nickname()]."
    m 3k_tmoad "I hope that we can come back soon~!"
    show monika 1j_tmoad at t11
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
