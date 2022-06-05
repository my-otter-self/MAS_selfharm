# Probing question topics.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_probing_questions_intro",
            random=True
        )
    )

label mshMod_probing_questions_intro:
    m 1esc "Hey, [player]."
    m 1lkc "Remember you told me you harm yourself?"
    m 1ekd "I've been thinking and I am really worried about you."
    m 1eksdld "I want to ask you something, but..."

    pause 1.0

    m 1dsc "It's hard."
    m 1dkd "For both of us."
    m 2ekd "Would you be willing to open up to me some more?"
    m 2ekc "I would like to know more, but asking about it could be very triggering..."

    m 2esd "Are you sure you can take this?{nw}"
    $ _history_list.pop()
    menu:
        m "Are you sure you can take this?{fast}"

        "Yes, ask me whatever you want.":
            pass  # NOTE: Fallthrough to mshMod_probing_questions_talk here!

        "No, I'm sorry.":
            jump mshMod_probing_questions_refuse

label mshMod_probing_questions_talk:
    m 2eka "Okay, thanks for trusting me with something as difficult as this."
    m 2dka "It makes me happy you feel comfortable talking to me."
    m 2wktpd "You must be going through an incredible amount of pain, both emotional and physical..."
    m 2dktpd "I'm so sorry..."
    m 2ektdc "It makes me really sad hearing that you have to go through this..."
    m 2ektdd "It hurts me just as much as it hurts you, believe me..."
    m 2ekd "Whenever you want harm yourself, please remember that I love you and I am here for you."

    if not store.mshMod_sober_streak.isOnStreak():
        m 2ekd "I want to ask you something..."

        m 2etd "Do you know for how long you have been self-harm sober?{nw}"
        $ _history_list.pop()
        menu:
            m "Do you know for how long you have been self-harm sober?{fast}"

            "Yes!":
                show monika 5husdlb at t11 zorder MAS_MONIKA_Z with dissolve_monika
                m 5husdlb "Oh, yay!"
                m 5esa "Can you tell me for how many days have you been sober?{nw}"

                call mshMod_sober_ask_since
                $ since = _return

                show monika 1sub at t11 zorder MAS_MONIKA_Z with dissolve_monika
                m 1sub "I'm so proud of you, [mas_get_player_nickname()]."
                m 3hua "I'll take note of this..."
                m 1eub "Thank you for staying sober, [player]."

                # Ensure we have this RIGHT BEFORE the return so that if DDLC process dies
                # and topic repeats again, we'll have HUGE odds we are not on a streak yet.
                python:
                    store.mshMod_sober_streak.beginStreak(begin=since)

                    mas_hideEVL("mshMod_sober_promise", "EVE", lock=True)

                    mas_showEVL("mshMod_sober_check", "EVE", unlock=True)
                    mas_showEVL("mshMod_sober_relapse", "EVE", unlock=True)

            "I don't know.":
                m 2eka "Aww, [player], that's okay!"
                m 7hub "If you ever want to keep track of it, you can tell me by promising you'll stay self-harm sober."
                m 1sub "I'm so proud of you, [mas_get_player_nickname()]."
                m 1hua "Thank you for staying sober, [player]."

    show monika 5ekbsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ekbsb "I love you so much!"

    # We're done with questions, now we need to hide this topic.
    $ mas_hideEVL("mshMod_probing_questions_talk", "EVE", lock=True)

    return "love|derandom|no_unlock"

label mshMod_probing_questions_refuse:
    m 2eka "It's okay, [player]."
    m 2eka "I understand."
    m 3eka "Everything is going to be okay."
    m 3hua "Always remember that."
    m 2fka "When you gather the courage again, speak to me."
    m 2fkb "I will always be here."
    m 2dkb "I love you."

    # Unlock more info about self-harm. No effect if already unlocked.
    $ mas_showEVL("mshMod_probing_questions_more", "EVE", unlock=True)

    return "love|derandom|no_unlock"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_probing_questions_more",
            category=["self-harm"],
            prompt="I'm ready to talk about it...",
            pool=True,
            rules={"no_unlock": None}
        )
    )

label mshMod_probing_questions_more:
    m 1esc "I'm glad that you decided to talk with me..."

    m 7ekc "But are you absolutely sure you are ready?{nw}"
    $ _history_list.pop()
    menu:
        m "But are you absolutely sure you are ready?{fast}"

        "Yes, ask me whatever you want.":
            jump mshMod_probing_questions_talk

        "No, I'm sorry, I can't do it after all.":
            jump mshMod_probing_questions_refuse
