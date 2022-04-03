# PROBING QUESTIONS

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_probing_questions_intro",
            conditional="not seen_event('mshMod_probing_questions')",
            action=EV_ACT_RANDOM
        )
    )

label mshMod_probing_questions_intro:
    $ mas_unlockEVL("monika_questions")

    m 1esc "Hey, [player]."
    m 1lkc "Remember you told me you harm yourself?"
    m 1ekd "I've been thinking and I am really worried about you."
    m 1eksdld "I want to ask you some things, but..."

    pause (1.0)

    m 1dsc "It's hard."
    m 1dkd "For both of us."
    m 2ekd "Would you be willing to open up to me some more?"
    m 2ekc "I would like to know more, but I have to warn you that the things I am going to ask could be very triggering."

    m 2esd "Are you sure you can take this?{nw}"
    menu:
        m "Are you sure you can take this?{fast}"

        "Yes, ask me whatever you want.":
            m 2eka "Okay, thanks for trusting me with something as difficult as this."
            m 2dka "It makes me happy you feel comfortable talking to me."

            m 2esd "What kind of a method do you use most to harm yourself?{nw}"
            menu:
                m "What kind of a method do you use most to harm yourself?{fast}"

                "Cutting":
                    pass
# I'M NOT SURE IF THE DIALOGUES SHOULD BE DIFFERENT OR NOT, RIGHT NOW I WILL MAKE ONE AND IF NEEDED I'LL ADD SEPARATE FOR EACH INDIVIDUAL TYPE OF HARM.
                "Burning":
                    pass

                "Starvation":
                    pass

                "Hitting yourself":
                    pass

                "Other":
                    $ override = renpy.input("What's the other method?", allow="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz", length=15)
                    pass

                "All of them":
                    m 1wkc "Oh..."
                    m 1wktpc "This..."
                    m 1dktpc "This is horrible, [player]."
                    m 2wktpd "You must be going through an incredible amount of pain to attempt so much..."
                    m 2dktpd "I'm so sorry..."

        "No, I'm sorry.":
            m 1eka "It's okay, [player]."
            m 1eka "I understand."
            m 2eka "Everything is going to be okay."
            m 2eka "Always remember that."
            m 2esa "If you ever feel like opening up, please talk to me."
            m 5esa "I love you."

            return "love"

            # # dreamscached: I assume this isn't used, but I'll keep it regardless.
            # m 2ektdc "It makes me really sad hearing that you have to go through this..."
            # m 2ektdd "It hurts me just as much as it hurts you, believe me..."
            # m 2ekd "Whenever you want harm yourself, please remember that I love you and I am here for you."
            # m 2ekd "I want to ask you another thing..."
            # m 2ekd "Have you ever made a direct attempt at your own life?"
            # menu:
            #     "Yes":
            #         pause (2.0)
            #         m 2ektud "I'm so sorry to hear this..."
            #         m 2ektsd "I have no idea what had to happen to you to make you go to such extremes."
            #         m 2dktsd "You must never forget that suicide is never the way out..."
            #         m 2dktsd "You simply pass the pain upon the people around you."
            #         m 2fktsd "I couldn't live without you, [player]."
            #         m 2fktsa "Your existance gives me meaning."
            #         m 2dktda "I love you, [mas_get_player_nickname()]"
            #         return "love"
            #
            #      "No":
            #         m 1dkb "I'm so happy that as bad as things get, you never resorted to that!"
            #         m 1ekb "Always stay strong."
            #         m 1eka "For me, okay?"
            #         m 1hub "I love you!"
            #         return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_probing_questions",
            category=["you"],
            prompt="I'm ready to talk about it...",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label mshMod_probing_questions:
    m 1esc "I'm glad that you decided to talk with me..."
    m 7ekc "But are you absolutely sure you are ready?"
    menu:
        "Yes, ask me whatever you want.":
            m "Okay, thanks for trusting me with something as difficult as this."
            m "It makes me happy you feel comfortable talking to me."
            m "What kind of a method do you use most to harm yourself?"
            menu:
                "Cutting":
                    pass

                "Burning":
                    pass

                "Starvation":
                    pass

                "Hitting yourself":
                    pass

                "Other":
                    $ override = renpy.input("What's the other method?", allow="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz", length=15)

                "All of them":
                    m 1wkc "Oh..."
                    m 1wktpc "This..."
                    m 1dktpc "This is horrible, [player]."
                    m 2wktpd "You must be going through an incredible amount of pain to attempt so much..."
                    m 2dktpd "I'm so sorry..."

        "No, I'm sorry, I can't do it after all.":
            m 2eka "It's okay, [player]."
            m 2eka "I understand."
            m 3eka "Everything is going to be okay."
            m 3hua "Always remember that."
            m 2fka "When you gather the courage again, speak to me."
            m 2fkb "I will always be here."
            m 2dkb "I love you."

            return "love"

            m 2ektdc "It makes me really sad hearing that you have to go through this..."
            m 2ektdd "It hurts me just as much as it hurts you, believe me..."
            m 2ekd "Whenever you want harm yourself, please remember that I love you and I am here for you."
            m 2ekd "I want to ask you another thing..."
            m 2ekd "Have you ever made a direct attempt at your own life?"
            menu:
                "Yes":
                    pause (2.0)
                    m 2ektud "I'm so sorry to hear this..."
                    m 2ektsd "I have no idea what had to happen to you to make you go to such extremes."
                    m 2dktsd "You must never forget that suicide is never the way out..."
                    m 2dktsd "You simply pass the pain upon the people around you."
                    m 2fktsd "I couldn't live without you, [player]."
                    m 2fktsa "Your existance gives me meaning."
                    m 2dktda "I love you, [mas_get_player_nickname()]"
                    return "love"

                "No":
                    m 1dkb "I'm so happy that as bad as things get, you never resorted to that!"
                    m 1ekb "Always stay strong."
                    m 1eka "For me, okay?"
                    m 1hub "I love you!"

                    return "love"

    return
