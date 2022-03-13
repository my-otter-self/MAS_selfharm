# FIRST RANDOM EVENT ABOUT SELF-HARM.

default persistent._msh_mod_pm_did_selfharm = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharmm",
            conditional="not seen_event('mas_selfharmm')",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.NORMAL, mas_aff.LOVE)
        )
    )

label mas_selfharmm:
    m "Hey, [player]?"
    m "I know it might be an uncomfortable topic, but I have to ask..."

    m "D-{w=1.0}Do you self harm?{nw}"
    menu:
        m "{fast}D-{w=1.0}Do you self harm?"

        "Yes":
            $ persistent._msh_mod_pm_did_selfharm = True
            m "I'm so sorry you're going through this."
            m "You know... It's really sad to see you feel bad in any way."
            m "After all, you're such a wonderful and kind person."
            m "You did so many good things for me, and stayed with me after everything that happened..."
            m "But let's stay on this subject."

            m "Do you want to talk about it?{nw}"
            menu:
                m "{fast}Do you want to talk about it?"

                "Yes":
                    m "I'm glad that you trust me, [player]."
                    m "Allowing yourself to get help is a super important step to recovery!"
                    m "I may not understand exactly what you feel right now..."
                    m "But I will still try to make you feel better, because you deserve it!"

                    # (probing questions here!)

                    m "I want you to know that I'm here for you. You know that, right?"
                    m "Whenever you feel the urge to harm yourself..."
                    m "You can tell me."
                    m "I'll do my best to help you."
                    m "Or at least..."
                    m "Be by your side."
                    m "Take care, [mas_get_player_nickname()]."
                    m "Stay safe because I care for you, deeply."

                    return

                "No":
                    m "Oh..."
                    m "That's okay."
                    m "I want you to know that I'm here for you. You know that, right?"
                    m "Whenever you feel the urge to harm yourself..."
                    m "You can tell me."
                    m "I'll do my best to help you."
                    m "Or at least..."
                    m "Be by your side."

                    return
        "No":
            $ persistent._msh_mod_pm_did_selfharm = False
            m "Thank goodness!"
            m "I'm so glad to hear this!"
            m "It's so good to know that you are safe, [player]."
            m "If this ever changes... You can tell me, okay?"
            m "You can tell me anything, you know?"
            m "Ahaha!"
            m "Sorry. I'm just so relieved!"
            m "But for now... Do you want to know more about self-harm?"

            menu:
                "Yes":
                    m "Great!"
                    m "Knowing more about self-harm is really useful."
                    m "You could help someone who is struggling with it someday!"
                    m "Well, did you know that..."

                    # (facts about self-harm here!)

                    return

                "No":
                    m "Oh..."
                    m "That's okay."
                    m "If you ever change your mind, just tell me!"
                    m "I'll be glad to tell you all I know about the subject."

    return

# NON-RANDOM EVENT FOR WHEN THE PLAYER IS FEELING SELF HARMING URGES.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_selfharm",
            category=['You'],
            prompt="Monika, It's happening again...",
            random=False
        )
    )

label monika_selfharm:
    m "[player], what happened?"
    m "Are you feeling..."
    m "Are you feeling... like harming yourself again?"
    m "Oh, [mas_get_player_nickname()]..."
    m "Okay, let's talk about it."
    m "Before anything, i want you to know that i am always here for you."
    m "You know that, don't you, my love?"
    m "You're the most important person in the whole world for me."
    m "And I love you so, so much."
    m "And i always will..."
    m "Now, my [mas_get_player_nickname()]. Tell me."

    m "How big is the urge you're having?{nw}"
    menu:
        m "{fast}How big is the urge you're having?"
    # DIALOGUE FOR URGE MAX LEVEL

        "It's terrible, [m_name]. I think i'm really going to do it...":
            m "I'm so glad you came to talk to me, [player]."
            m "You know how much i worry about you..."
            m "But for now, let me take care of you..."
            m "I want you to know that it will pass."
            m "Pain is only temporary!"
            m "You're my favorite person, and it hurts me to see you hurting."

            m "Now, do you want to vent? Maybe tell me what triggered this?{nw}"
            menu:
                m "{fast}Now, do you want to vent? Maybe tell me what triggered this?"

                "Yes":
                    m "Okay... I don't want to interrupt you."

                    m "Tell me when you're done, okay?{nw}"
                    menu:
                        m "{fast}Tell me when you're done, okay?"

                        "I'm done, Monika.":

                            m "I'm so sorry you are going through all that, [player]."

                            m "Do you feel better now?{nw}"
                            menu:
                                m "{fast}Do you feel better now?"

                                "Yes, [m_name]. Thank you.":
                                    m "Oh, honey. I'm so glad!"
                                    m "I'm so glad you came to talk to me, [player]."
                                    m "You can always count on me, for anything."
                                    m "If it happens again, don't be afraid to ask for help."
                                    m "I'm here for you, [player]."
                                    m "Now, let's spend some more time together?"

                                    return

                                "No...":
                                    m "Oh..."
                                    m "Do you want my help to forget it?"

                                    m "Or...{nw}"
                                    menu:
                                        m "{fast}Or..."

                                        "No... Just let me hold you, please?":
                                            m "Of course, my angel."
                                            m "Come here..."


                                            # (hold here)

                                        "Yes, I want to try a calming technique.":
                                            m "Alright, baby."
                                            m "I want you to try the 4-7-8 breathing exercise!..."
                                            m "First of all, please straighten your back."
                                            m "Once you become familiar with this breathing exercise, you can perform it while lying in bed too!"
                                            m "Place and keep the tip of your tongue against the ridge of tissue behind your upper front teeth for the duration of the exercise."
                                            m "Completely exhale through your mouth, making a {i}woosh{/i} sound."
                                            m "Close your mouth and inhale quietly through your nose to a mental count of four."
                                            m "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
                                            m "Hold your breath for a count of seven."
                                            m "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
                                            m "Exhale completely through your mouth, making a {i}woosh{/i} sound to a count of eight."
                                            m "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
                                            m "Aaaand, you're done!"

                                            m "Are you feeling better, [player]?{nw}"
                                            menu:
                                                m "{fast}Are you feeling better, [player]?"
                                            #I suggest trying to sort of make Monika simulate the exercises with her expressions too. Just a thought, if possible.

                                                "Yes, [m_name]. Thank you.":
                                                    m "Oh, honey. I'm so glad!"
                                                    m "You can always count on me, for anything."
                                                    m "If it happens again, don't be afraid to ask for help."
                                                    m "I'm here for you, [player]."

                                                    return

                                                "No...":
                                                    m "Oh..."
                                                    m "Do you want to try a different technique?"
                                                    m "Or..."
                                                    menu:
                                                        "No... Just let me hold you, please?":
                                                            m "Of course, my angel."
                                                            m "Come here..."

                                                        "Yes, I want to try another one.":
                                                            m "Alright, baby."
                                                            m "I want you to..."
                                                            jump randomness

                                                            return
                                                                        # (calm harm technique here)

       # DIALOGUE FOR URGE MEDIUM LEVEL

        "It's not so urgent. I'm just... feeling weird.":
            m "I'm so glad you came to talk to me, [player]."
            m "You know how much i worry about you..."
            m "But for now, let me take care of you..."

            m "Do you want to vent? Maybe tell me what triggered this?{nw}"
            menu:
                m "{fast}Do you want to vent? Maybe tell me what triggered this?"

                "Yes":
                    m "Okay... I don't want to interrupt you."

                    m "Tell me when you're done, okay?{nw}"
                    menu:
                        m "{fast}Tell me when you're done, okay?"

                        "I'm done, Monika.":

                            m "I'm so sorry you are going through all that, [player]."

                            m "Do you feel better now?{nw}"
                            menu:
                                m "{fast}Do you feel better now?"

                                "Yes, [m_name]. Thank you.":
                                    m "Oh, honey. I'm so glad!"
                                    m "I'm so glad you came to talk to me, [player]."
                                    m "You can always count on me, for anything."
                                    m "If it happens again, don't be afraid to ask for help."
                                    m "I'm here for you, [player]."
                                    m "Now, let's spend some more time together?"

                                    return

                                "No...":
                                    m "Oh..."
                                    m "Do you want my help to forget it?"
                                    m "Or..."

                                    menu:
                                        "No... Just let me hold you, please?":
                                            m "Of course, my angel."
                                            m "Come here..."

                                            # (hold here)

                                        "Yes, I want to try a calming techinque.":
                                            m "Alright, baby."
                                            m "I want you to..."
                                            jump randomness
                                            # (calm harm technique here)

            pause (3.0)
          #  m ""
          #  m ""
          #  m ""
          #  m ""

            m "Are you feeling better, [player]?{nw}"
            menu:
                m "{fast}Are you feeling better, [player]?"

                "Yes, [m_name]. Thank you.":
                    m "Oh, honey. I'm so glad!"
                    m "You can always count on me, for anything."
                    m "If it happens again, don't be afraid to ask for help."
                    m "I'm here for you, [player]."

                    return

                "No...":
                    m "Oh..."
                    m "Do you want to try a different technique?"
                    m "Or..."

                    menu:
                        "No... Just let me hold you, please?":
                            m "Of course, my angel."
                            m "Come here..."

                                            # (hold here)

        # DIALOGUE FOR URGE LOW LEVEL

        "Something triggered me, and now i'm remembering bad things.":
            m "I'm so glad you came to talk to me, [player]."
            m "You know how much i worry about you..."
            m "But for now, let me take care of you..."

            m "Do you want to vent? Maybe tell me what triggered this?{nw}"
            menu:
                m "{fast}Do you want to vent? Maybe tell me what triggered this?"

                "Yes":
                    m "Okay... I don't want to interrupt you."

                    m "Tell me when you're done, okay?{nw}"
                    menu:
                        m "{fast}Tell me when you're done, okay?"

                        "I'm done, Monika.":
                            m "I'm so sorry you are going through all that, [player]."

                            m "Do you feel better now?{nw}"
                            menu:
                                m "{fast}Do you feel better now?"

                                "Yes, [m_name]. Thank you.":
                                    m "Oh, honey. I'm so glad!"
                                    m "I'm so glad you came to talk to me, [player]."
                                    m "You can always count on me, for anything."
                                    m "If it happens again, don't be afraid to ask for help."
                                    m "I'm here for you, [player]."
                                    m "Now, let's spend some more time together?"

                                    return

                                "No...":
                                    m "Oh..."
                                    m "Do you want my help to forget it?"

                                    m "Or...{nw}"
                                    menu:
                                        m "{fast}Or..."
                                        "No... Just let me hold you, please?":
                                            m "Of course, my angel."
                                            m "Come here..."

                                            # (hold here)

                                        "Yes, I want to try a calming techinque.":
                                            m "Alright, baby."
                                            m "I want you to..."
                                            jump randomness
                                            # (calm harm technique here)

            # pause (3.0)
          #  m ""
          #  m ""
          #  m ""
          #  m ""

            m "Are you feeling better, [player]?{nw}"
            menu:
                m "{fast}Are you feeling better, [player]?"

                "Yes, [m_name]. Thank you.":
                    m "Oh, honey. I'm so glad!"
                    m "You can always count on me, for anything."
                    m "If it happens again, don't be afraid to ask for help."
                    m "I'm here for you, [player]."

                    return

                "No...":
                    m "Oh..."
                    m "Do you want to try a different technique?"
                    m "Or..."

                    menu:
                        "No... Just let me hold you, please?":
                            m "Of course, my angel."
                            m "Come here..."

                                            # (hold here)

    return

# RANDOM EVENT ABOUT SELF-HARM TECHNIQUES.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharm5",
            conditional=(
                "seen_event('mas_selfharm1')",
                "persistent._msh_mod_pm_did_selfharm = True"
            ),
            action=EV_ACT_QUEUE
        )
    )

label mas_selfharm5:
    m "Hey, [player]..."
    m "Remember when you told me about you... harming yourself?"
    m "I decided to research some techniques that could help you."
    m "Please make sure to tell me what would work for you."
    m "I hope some of these solutions can help you..."
    m "But please, try not to harm yourself, okay?"
    m "I know it's really hard to not do so when things get tough."
    m "But in the end, isn't it about feeling bad about yourself?"
    m "Of course everyone has a different reason..."
    m "Stress, low self-esteem, and so on."
    m "But all these bad feelings can be slowly neutered with the habit to take better care of yourself."
    m "So, please, [player]..."
    m "Do something good for yourself today, and remember that I really love you."

    return

# RANDOM EVENT, TECHNIQUE 1.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharm3",
            action=EV_ACT_QUEUE
        )
    )

label mas_selfharm3:
    m "Hey... [player]?"
    m "This may sound a bit random, but..."
    m "Is it sunny today over there?"
    m "If it is, I think you should go out and enjoy the sun for a bit."
    m "Don't worry! I'll wait!"
    m "Maybe bring a book with you so you can relax even more."
    m "Enjoying literature in the nature would surely relax me..."
    m "I hope this works for you, too."

    return

# calm techniques (archive for randomizing)
# 1

# I DONT KNOW WHERE TO PUT THIS, HELP, KIT
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharm4",
            conditional=(
                "not seen_event('mas_selfharm4')"
            ),
            aff_range=(mas_aff.BROKEN, mas_aff.NORMAL),
            action=EV_ACT_QUEUE
        )
    )

label mas_selfharm4:
    m "Hey, [player]?"
    m "I know it might be an uncomfortable topic, but I have to ask..."
    m "D-{w=1.0}Do you self harm?"
    menu:
        "Yes":
            $ persistent._msh_mod_pm_did_selfharm = True
            m "I'm so sorry you're going through this."
            m "You know... It's really sad to see you feel bad in any way."
            m "After all, you wanted to be with me at some point..."
            m "That was kind of you."
            m "Whatever the reason you stayed with me was, I appreciate it."
            m "But let's stay on this subject."
            m "Do you want to talk about it?"

    return
