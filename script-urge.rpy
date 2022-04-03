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
    m 1ekd "[player], what happened?"
    m 2ekd "Are you feeling..."
    m 2wkd "Are you feeling... like harming yourself again?"
    m 2dkc "Oh, [mas_get_player_nickname()]..."
    m 2ekd "Okay, let's talk about it."
    m 2eka "Before anything, I want you to know that I am always here for you."
    m 2eka "You know that, don't you, my love?"
    m 2dka "You're the most important person in the whole world for me."
    m 2dkb "And I love you so, so much."
    m 2fkb "And I always will..."
    m 2esc "Now, my [mas_get_player_nickname()]. Tell me."
    m 2ekc "How big is the urge you're having?{nw}"

    menu:
        m "How big is the urge you're having?{fast}"

        "It's terrible, [m_name]. I think I'm really going to do it...":
            jump mshMod_urge_high

        "It's not so urgent. I'm just... feeling weird.":
            jump mshMod_urge_medium

        "Something triggered me, and now I'm remembering bad things.":
            jump mshMod_urge_low

label mshMod_urge_high:
    m 2dka "I'm so glad you came to talk to me, [player]."
    m 2dkc "You know how much I worry about you..."
    m 2fka "But for now, let me take care of you..."
    m 2esd "I want you to know that it will pass."
    jump mshMod_urge_care_vent

label mshMod_urge_medium:
    m 2dka "I'm so glad you came to talk to me, [player]."
    m 2dkc "You know how much I worry about you..."
    m 2fka "But for now, let me take care of you..."
    jump mshMod_urge_care_vent

label mshMod_urge_low:
    m 2dka "I'm so glad you came to talk to me, [player]."
    m 2dkc "You know how much I worry about you..."
    m 2fka "But for now, let me take care of you..."
    jump mshMod_urge_care_vent

label mshMod_urge_care_vent:
    m 1ekd "Now, do you want to vent? Maybe tell me what triggered this?{fast}"

    menu:
        m "Now, do you want to vent? Maybe tell me what triggered this?{fast}"

        "Yes":
            m 1eka "Okay... I don't want to interrupt you."
            m 3eka "Tell me when you're done, okay?"
            menu:
                m "{fast}Tell me when you're done, okay?"

                "I'm done, [m_name].":
                    pass

            m 2ekc "I'm so sorry you are going through all that, [player]."
            jump mshMod_urge_care_feeling_better

        "No":
            return

label mshMod_urge_hold:
    m 2fka "Of course, my angel."

    call monika_holdme_prep

    m 1fkb "Come here..."

    call monika_holdme_start
    call monika_holdme_reactions
    call monika_holdme_end
    return

label mshMod_urge_care_feeling_better:
    m 3esd "Do you feel better now?{nw}"
    menu:
        m "Do you feel better now?{fast}"

        "Yes, [m_name]. Thank you.":
            jump mshMod_urge_care_good

        "No...":
            jump mshMod_urge_care_bad

label mshMod_urge_care_good:
    m 1ekb "Oh, honey. I'm so glad!"
    m 1dkb "I'm so glad you came to talk to me, [player]."
    m 5fkb "You can always count on me, for anything."
    m 1fkb "If it happens again, don't be afraid to ask for help."
    m 1fka "I'm here for you, [player]."
    m 1esa "Now, let's spend some more time together?"
    return

label mshMod_urge_care_bad:
    m 2ekc "Oh..."
    m 2ekd "Do you want my help to forget it?"
    m 2eksdld "Or..."

    m 2eksdld "Or...{nw}"
    menu:
        m "Or...{fast}"

        "No... Just let me hold you, please?":
            call mshMod_urge_hold

        "Yes, I want to try a calming technique.":
            m 1eka "Alright, baby."
            call mshMod_technique_random
            jump mshMod_urge_care_feeling_better
