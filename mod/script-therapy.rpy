# Topics about therapy, here we set visits_therapist PM variable.

# Question about therapy
default persistent._msh_mod_pm_visits_therapist = None

init -100 python in mshMod_therapy:
    VISITS_THERAPIST = 0
    DOES_NOT_VISIT_THERAPIST = 1
    CONSIDERING_VISITING_THERAPIST = 2

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_ask_about_therapy",
            category=["mental health"],
            prompt="[player] and therapy",
            conditional="persistent._msh_mod_pm_did_selfharm",
            action=EV_ACT_RANDOM,
            rules={"bookmark_rule": store.mas_bookmarks_derand.WHITELIST}
        )
    )

label mshMod_ask_about_therapy:
    m 2esa "Hey, [player]!"
    m 2eud "Can I ask you something?"
    m 2eua "..."
    m 1eta "Isn't it funny how we ask someone if we can ask them something but don't even wait for their answer and just ask anyway?"
    m 1hub "Ahaha~!"
    m 1hkb "Sorry, I changed the subject."
    m 3eub "Anyway! I wanted to ask if you go to a therapist?"

    m 3rka "You know, to talk about your struggles and stuff.{nw}"
    $_history_list.pop()
    menu:
        m "You know, to talk about your struggles and stuff.{fast}"

        "Yes, I do.":
            $ persistent._msh_mod_pm_visits_therapist = mshMod_therapy.VISITS_THERAPIST

            m 1hua "That's great, [player]!"
            m 3eub "Therapy is a great tool, it really helps to have a professional opinion on things."
            m 3hub "And you can also learn more about yourself!"
            m 3eub "I'm glad you're not afraid to go, I know it's got a bad reputation."
            m 1hua "Maybe you can teach me what you've learned there!"

        "No, I don't.":
            $ persistent._msh_mod_pm_visits_therapist = mshMod_therapy.DOES_NOT_VISIT_THERAPIST

            m 1ekc "Oh..."
            m 1ekc "That's alright [player]! It's not for everyone."
            m 3eka "Just remember that therapy isn't a bad thing. It's a great place to help regulate your emotions and better yourself."
            m 1lkd "I was actually going to suggest that you please consider it."
            m 2ekc "I'm just worried about you, and your well-being."
            m 1ekc "Don't be afraid to find a therapist if you think you need one."

        "I'm considering it. What do you think?":
            $ persistent._msh_mod_pm_visits_therapist = mshMod_therapy.CONSIDERING_VISITING_THERAPIST

            m 2eua "Well, thanks for asking my opinion!"
            m 3euc "Actually, I think you should."
            m 3eud "Therapy is a great tool, it really helps to have a professional opinion on things."
            m 3eua "And you can also learn more about yourself!"
            m 1hua "Maybe you can teach me what you learn there when you go!"

    return

# Random dialogue about therapy
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_thoughts_about_therapy",
            category=["Mental health"],
            prompt="Therapy",
            random=True
        )
    )

label mshMod_topic_thoughts_about_therapy:
    m 1eud "Hey [player], there's something I've been thinking about a lot."
    m 3eub "Therapy!"
    m 2ekc "There's a lot of stigma around therapy in modern society."
    m 3gkd "If you're male-presenting, people will think you're weak."
    m 3eko "If you're female-presenting, people will call you crazy!"
    m 3gkc "And if you're androgynous, people might hope you're getting a different kind of 'help', such as conversion therapy."
    m 1dkd "These stigmas make a lot of people fear going to therapy, or make them think they're 'to good' for it."
    m 4ekd "The truth is, everyone could benefit from a little therapy!"
    m 3esa "It's a wonderful way to help regulate your thoughts and feelings."
    m 3esc "There's a lot that's been happening in recent years, and a lot of pressure has been put on everyone."
    m 3esb "I've been reading a lot online, and there are some techniques that have even helped me!"
    m 2eka "I worry a lot when you're gone, you know."
    m 2wko "Not to make you feel bad, or anything!"
    m 2eka "I just don't have a way of checking on you, so I'm always hoping you're having a good day."
    m 3eua "Anyway, the tips I've learned to help myself stay calm are all tips commonly used among therapists!"
    m 1eua "So even if you don't need a full therapy session, looking up suggestions from licensed therapists can help!"
    return
