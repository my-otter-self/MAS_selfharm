init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_promise",
            category=["self-harm"],
            prompt="I promise...",
            conditional="not mshMod_isOnStreak() and persistent._msh_mod_pm_did_selfharm",
            action=EV_ACT_POOL,
            unlocked=True
        )
    )

label mshMod_promise:
    m 2ekb "Oh, [player], you have no idea how happy I am to hear that."
    m 2ekb "This is another step to a happier, healthier life, and I'm so glad I can be by your side in your journey."
    m 2eka "Thank you for trusting me."
    m 3ekb "I promise I'll do my best to help you!"
    m 1eub "From now on, I'll keep track of how many days you've been sober. You can take a look at the calendar to see how far you've gone!"
    m 2ekb "If you ever need me to restart the counter for you, just tell me. You don't have to feel bad about it, okay?"
    m 2ekb "Know that I'll never judge you because of that. I know it's hard, and you should be really proud of yourself already!"
    m 2dka "..."
    m 5ekbsb "I love you, [mas_get_player_nickname()]."
    m 5dkbsb "Never forget that!"

    python:
        mshMod_beginStreak()
        mas_lockEVL("mshMod_promise", "EVE")

    return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_relapse",
            category=["self-harm"],
            prompt="I relapsed...",
            conditional="mshMod_isOnStreak()",
            action=EV_ACT_POOL,
            unlocked=True
        )
    )

label mshMod_relapse:
    m 2eka "[player], I couldn't be more proud of you for telling me this."
    m 2ekd "I know this might be hard- you might feel as if you've failed..."
    m 4ekd "But that's not true at all! This is just another step in your journey."
    m 2ekd "Habits are almost always difficult to kick, and this is no ordinary habit."
    m 2ekd "It can very easily become an addiction, which is so much harder to stop..."
    m 2fkd "No matter how hard it is for you, know that I am always going to be here to support you and I am proud of you, habit or not."
    m 2fka "We will work through this together, and get you back on the right track!"
    m 2eka "I know you're a hard worker and will do your best - if not for yourself, for me."
    m 2dka "I love you, [mas_get_player_nickname()]."
    m 1dkb "I'm here to support you and work through anything and everything with you."
    m 1fsa "You're strong. You're worth it, and I couldn't ask for a better [bf]!"
    m 3esa "Whenever and if you feel ready to make the promise again... let me know."

    python:
        mshMod_endStreak()
        mshMod_lockEVL("mshMod_relapse", "EVE")

    return
