#Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="Wilt3r",
        name="Take Monika On A Date",
        description="Adds a button to take Monika on a date here in the game!",
        version="1.0.1"
    )


#Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Take Monika On A Date",
            user_name="wowm03",
            repository_name="DateMonikaSubmod",
            update_dir="",
            attachment_id=None
        )


#Adds the Dates option
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="pick_date",category=['Dates'],prompt="Let's go on a date",pool=True,unlocked=True))


#Choose where to go for the date
label pick_date:
    m 1sublb "We're going on a date?"
    m 3hub "Sounds exciting~!"
    m 1eua "Where do you want to go for our date?{nw}"

    menu:
        m "Where do you want to go for our date?{fast}"

        "Cafe":
              play sound "Submods/DateMonikaSubmod/music/notice.mp3"
              call screen dialog(message="Error: Script file is missing or corrupt.\nPlease check or reinstall the Submod.", ok_action=Return())
              return

        "Park":
              m 6hub "Alright, let's go!"
              window hide
              show black zorder 100 with Dissolve(5.0, alpha=True)
              call park

        "Beach":
               play sound "Submods/DateMonikaSubmod/music/notice.mp3"
               call screen dialog(message="Error: Script file is missing or corrupt.\nPlease check or reinstall the Submod.", ok_action=Return())
               return

        "Nevermind":
                   m 1eka "Oh, alright."
                   return


#Defenitions
image cafe = "Submods/DateMonikaSubmod/images/cafe.png"
image cafemenu = "Submods/DateMonikaSubmod/images/cafemenu.png"
image cafetable = "Submods/DateMonikaSubmod/images/cafetable.png"
image park = "Submods/DateMonikaSubmod/images/park.png"
image park2 = "Submods/DateMonikaSubmod/images/park2.png"
image park3 = "Submods/DateMonikaSubmod/images/park3.png"
image park4 = "Submods/DateMonikaSubmod/images/park4.png"
image park5 = "Submods/DateMonikaSubmod/images/park5.png"
image park_lake = "Submods/DateMonikaSubmod/images/park-lake.png"
image forest = "Submods/DateMonikaSubmod/images/forest.png"



#TODO: Finish the cafe date and release it somewhere in 2023. If I have motivation to do so.
#The Cafe Date
#label cafe:
#    $HKBHideButtons()
#    stop music
#    play music "<loop 4.444>bgm/5_monika.ogg" fadein 2
#    $ morning_flag = False
#    $ prev_flt = store.mas_sprites.get_filter()
#    $ store.mas_sprites.set_filter(store.mas_sprites.FLT_NIGHT)
#    hide black
#    scene cafe
#    $ is_sitting = False
#    show monika 4hub_static at t11
#    $ amongusoption = True
#    m "We're here~!"
#    m 1eua_static "It's so nice of you to take me on a date."
#
#    menu:
#        "You're welcome":
#                        pass
#
#        "Because I love you~":
#                             pass
#
#    m 2eub "Now c'mon, let's go to our table."
#    scene cafetable with wipeleft_scene
#    $ is_sitting = True
#    show monika 1euc at t11
#    pause 2
#    m 1eub "Oh look,{w=1} our menu's are already here."
#    m 3hub "What great customer service this restaurant have!"
#label amongusoptionisnowdisable:
#    hide black
#    m 1eua "So,{w=1} what are you getting?"
#    play audio page_turn
#    show cafemenu zorder 11 with Dissolve(1.0, alpha=True)
#    pause 2
#    m "These choices are....{w} {i}Intresting{/i}."
#
#label CafeMenu:
#    menu:
#        "Salad":
#               show monika 1euc zorder MAS_MONIKA_Z
#               play audio page_turn
#               hide cafemenu with Dissolve(1.0, alpha=True)
#               "A Salad appeared on the table."
#               "The Salad consist of,{w=0.30} well what you normally put on a salad."
#               "Vegetables and stuff."
#               "It also comes with soda."
#               m 1eua "You picked a Salad."
#               m 3hub "Great choice!"
#               m 7eub "Did you know Salad comes from the Latin word {i}herba salta{/i} or {i}salted herbs,{/i} so called because such greens were usually seasoned with dressings containing lots of salt."
#               m 2tuu "Bet you didn't know that."
#               m 2etc "Or you probably did."
#               m 1hua "Anyway, now I'm going to pick..."
#               pause 2
#               m 1hub "Coffee!"
#               pass
#
#        "Bread":
#               show monika 1euc zorder MAS_MONIKA_Z
#               play audio page_turn
#               hide cafemenu with Dissolve(1.0, alpha=True)
#               "Bread appeared on the table."
#               "The Bread consist of bread."
#               "It also comes with coffee."
#               m 1eua "You picked Bread."
#               m 3hub "Great choice!"
#               m 1hua "Now I'm going to pick..."
#               pass
#
#        "Among Us Meal" if amongusoption:
#                       $ amongusoption = False
#                       show monika 1euc
#                       play audio page_turn
#                       hide cafemenu with Dissolve(1.0, alpha=True)
#                       "{i}An Among Us Meal appeared on the table.{/i}"
#                       "{i}The Among Us Meal consist of a salad shape as a crewmate.{/i}"
#                       "{i}5 chicken nuggets at the side also shape as crewmates.{/i}"
#                       "{i}And a soda named {b}Sus Juice{/b}.{/i}"
#                       stop music
#                       show noise zorder 3 at noisefade(5):
#                           alpha 1.0
#                       show vignette zorder 3 at vignettefade(2):
#                           alpha 1.0
#                       m 6efd "Is that a Among Us Meal."
#                       menu:
#                           "Yes":
#                                 pass
#                       m 2dsc "An Among Us Meal..."
#                       pause 2
#                       show screen tear(20, 0.1, 0.1, 0, 40)
#                       play sound "sfx/s_kill_glitch1.ogg"
#                       pause 0.25
#                       hide screen tear
#                       m "You got..."
#                       pause 2
#                       m 2cub "An amogus meal-{nw}"
#                       show screen tear(20, 0.1, 0.1, 0, 40)
#                       play sound "sfx/s_kill_glitch1.ogg"
#                       pause 0.25
#                       hide screen tear
#                       show black zorder 11
#                       hide vignette
#                       hide noise
#                       pause 5
#                       $ renpy.movie_cutscene("Submods/DateMonikaSubmod/")
#                       pause 2
#                       play music "<loop 4.444>bgm/5_monika.ogg"
#                       jump amongusoptionisnowdisable
#                       jump cafe_end
#
#        "Coffee":
#                show monika 1euc zorder MAS_MONIKA_Z
#                play audio page_turn
#                hide cafemenu with Dissolve(1.0, alpha=True)
#                "Coffee appeared on the table."
#                m 1eua "You picked Coffee."
#                m 3hub "Great choice!"
#                m 1hua "Now I'm going to pick..."
#                pass
#
#        "Dark Coffee":
#                     show monika 1euc zorder MAS_MONIKA_Z
#                     play audio page_turn
#                     hide cafemenu with Dissolve(1.0, alpha=True)
#                     "Dark Coffee appeared on the table."
#                     m 1eua "You picked Dark Coffee."
#                     m 3hub "Great choice!"
#                     m 1hua "Now I'm going to pick..."
#                     pass
#
#        "White Coffee":
#                      show monika 1euc zorder MAS_MONIKA_Z
#                      play audio page_turn
#                      hide cafemenu with Dissolve(1.0, alpha=True)
#                      "White Coffee appeared on the table."
#                      m 1eua "You picked White Coffee."
#                      m 3hub "Great choice!"
#                      m 1hua "Now I'm going to pick..."
#                      pass
#
#        "Fries":
#               show monika 1euc zorder MAS_MONIKA_Z
#               play audio page_turn
#               hide cafemenu with Dissolve(1.0, alpha=True)
#               "Fries appeared on the table."
#               "The Fries consist of potatos."
#               "It also comes with a soda."
#               m 1eua "You picked Fries."
#               m 3hub "Great choice!"
#               m 1hua "Now I'm going to pick..."
#               pass
#
#        "{b}{i}NEXT{/i}{/b}":
#                     menu:
#                         "Mint Ice Cream":
#                                         show monika 1euc zorder MAS_MONIKA_Z
#                                         play audio page_turn
#                                         hide cafemenu with Dissolve(1.0, alpha=True)
#                                         "Mint Ice Cream appeared on the table."
#                                         m 1eua "You picked Mint Ice Cream."
#                                         m 3hub "Great choice!"
#                                         m 1hua "Now I'm going to pick..."
#                                         pass
#
#                         "Chocolate Ice Cream":
#                                              show monika 1euc zorder MAS_MONIKA_Z
#                                              play audio page_turn
#                                              hide cafemenu with Dissolve(1.0, alpha=True)
#                                              "Chocolate Ice Cream appeared on the table."
#                                              m 1eua "You picked Chocolate Ice Cream."
#                                              m 3hub "Great choice!"
#                                              m 1hua "Now I'm going to pick..."
#                                              pass
#
#                         "Vanilla Ice Cream":
#                                           show monika 1euc zorder MAS_MONIKA_Z
#                                          play audio page_turn
#                                            hide cafemenu with Dissolve(1.0, alpha=True)
#                                            "Vanilla Ice Cream appeared on the table."
#                                            m 1eua "You picked Vanilla Ice Cream."
#                                            m 3hub "Great choice!"
#                                            m 1hua "Now I'm going to pick..."
#                                            pass
#
#                         "Milk":
#                               show monika 1euc zorder MAS_MONIKA_Z
#                               play audio page_turn
#                               hide cafemenu with Dissolve(1.0, alpha=True)
#                               "Milk appeared on the table."
#                               m 1eua "You picked Milk."
#                               m 3hub "Great choice!"
#                               m 1hua "Now I'm going to pick..."
#                               pass
#
#                         "Chocolate Milk":
#                                         show monika 1euc zorder MAS_MONIKA_Z
#                                         play audio page_turn
#                                         hide cafemenu with Dissolve(1.0, alpha=True)
#                                         "Chocolate Milk appeared on the table."
#                                         m 1eua "You picked Chocolate Milk."
#                                         m 3hub "Great choice!"
#                                         m 1hua "Now I'm going to pick..."
#                                         pass
#
#                         "{b}{i}PREVIOUS{/i}{/b}":
#                                          jump CafeMenu
#
#label cafe_end:
#
#    show black zorder 11 with Dissolve(5.0, alpha=True)
#    pause 2
#    scene cafe
#    hide black with Dissolve(5.0, alpha=True)
#    $ is_sitting = False
#    show monika 4hub at t11
#    m "That was great!"
#    m 1eka "I want to thank you for taking me on this date, [mas_get_player_nickname()]."
#    m 1hua "I hope you can take me on a date again soon~"
#    m 1hub "I love you so much, [player]!"
#    show black zorder 11 with Dissolve(5.0, alpha=True)
#    stop music fadeout 2
#    hide monika
#    pause 2
#    $HKBShowButtons()
#    $ morning_flag = True
#    $ prev_flt = store.mas_sprites.get_filter()
#    $ store.mas_sprites.set_filter(store.mas_sprites.FLT_DAY)
#    $ play_song(persistent.current_track, fadein=4.0)
#    hide black
#    $mas_HKBDropShield()
#    $ is_sitting = True
#
#    jump ch30_loop
