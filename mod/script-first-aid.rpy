# Fist aid topics.

init 5 python in mas_bookmarks_derand:
    # Ensure things get bookmarked and derandomed as usual.
    label_prefix_map["mshMod_topic_"] = label_prefix_map["monika_"]

#first aid intro
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_first_aid_intro",
            conditional="persistent._msh_mod_pm_did_selfharm",
            action=EV_ACT_RANDOM
        )
    )

label mshMod_first_aid_intro:
    m 2ekc "I know you said you've injured yourself before, [player]..."
    m 3ekd "It really left me heartbroken, because I really want the best for you."
    m 3esd "So, I decided to give you some instructions if you ever do it in the future..."
    m 2rkc "And can't have medical attention."
    m 2esd "It's a basic first-aid guide. For cuts, specifically."
    m 3esd "If you need it, make sure to let me know, okay?"
    m 1eka "I'll do my best to help."
    return "derandom|no_unlock"


#first aid guide
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_first_aid_guide",
            prompt="I need help with first aid...",
            conditional="seen_event('mshMod_first_aid_intro')",
            category=["mental health"],
            action=EV_ACT_UNLOCK,
            pool=True,
            rules={"no_unlock": None, "bookmark_rule": mas_bookmarks_derand.WHITELIST}}
        )
    )

label mshMod_first_aid_guide:
    m 1eud "You need first-aid help, [player]?"
    m 2ekc "I'm so sorry, [mas_get_player_nickname()]."
    m 2eksdld "Does it hurt much?"
    m 2gksdld "It hurts me too..."
    m 2ekc "When you bleed, my heart bleeds..."
    m 2dsd "But let's get to it."
    m 1esd "First-aid is all about timing, the faster we tend to your wounds, better the recovery!"
    m 1esd "I'll do a step by step process on how to treat your wounds."
    m 3esd "Remember, this is specifically about cuts!"
    m 2esd "Let me get started... {w=0.3}{nw}"
    m 7esd "Firstly, you will need to stop the bleeding."
    m 2esd "You should apply constant pressure to the area using a clean and dry absorbent material."
    m 2lsd "A bandage, towel or handkerchief. For approximately 10 minutes."
    m 3esd "It's important to raise the injury above the level of your heart."

    m 2esa "I can make a timer for you.{nw}"
    $ _history_list.pop()
    menu:
        m "I can make a timer for you.{fast}"

        "Yes, that'd help":
            m 1hub "Okay! I'll tell you when it's done.{nw}"
            $ _history_list.pop()

            # Set a timer that forces label jump after 580 to 620 seconds (chosen randomly.)
            show screen mas_background_timed_jump(random.randint(580, 620), "mshMod_first_aid_guide_timeout")
            menu:
                m "Okay! I'll tell you when it's done.{fast}"

                "Skip timer":
                    pass

        "No, I'll manage":
            m 1hksdlb "Oh, okay! Let me know when you'll be ready to proceed.{nw}"
            $ _history_list.pop()
            menu:
                m "Oh, okay! Let me know when you'll be ready to proceed.{fast}"

                "Done":
                    pass

# NOTE: Fallthough label, 'return' is deliberately omitted above.
label mshMod_first_aid_guide_timeout:
    hide screen mas_background_timed_jump

    m 2esb "All done, [player]!"
    m 2eud "Ready for the next step?{nw}"
    $ _history_list.pop()
    menu:
        m "Ready for the next step?{fast}"

        "Yes":
            m 3esd "Okay!"
            m 1esd "Secondly, you need to clean your wound."
            m 2esd "Start by washing and drying your hands thoroughly..."
            m 2esd "Then clean the wound under tap water or with an alcohol-free solution."
            m 3esd "Make sure you don't use no alcohol or hydrogen peroxide!"
            m 3rkd "As it may damage the skin and slow healing..."
            m 3wkd "And we don't want that!"
            m 1ekd "I'll wait for you to do that, [player]."

            m 1ekc "Just tell me when you're done, okay?{nw}"
            $ _history_list.pop()
            menu:
                m "Just tell me when you're done, okay?{fast}"

                "I'm done, [m_name].":
                    m 7esd "Okay!"
                    m 7esd "Thirdly and lastly, it's really important to apply a dressing."
                    m 1esd "You can use many different types.."
                    m 1lsd "Adhesives ones like plasters, non-adhesive compresses with a bandage."
                    m 3lsd "They can be small or big, waterproof, different shapes and so on."
                    m 3esa "Whatever feels best and it's available at home!"
                    m 1ekc "It has to be comfortable, since the wrong plaster can hurt your skin."
                    m 1esd "Keep the dressing clean by changing it as often as necessary!"
                    m 1esd "You can remove the dressing once the wound has closed itself."
                    m 3eud "Always pay attention to signs of infection!"
                    m 3ekx "Such as fever, swollen wounds, pus, or any significant or worsening swelling, redness and pain."
                    m 3ekd "If you notice any of those..."
                    m 2ekd "You need to get medical attention and soon as possible."
                    m 2ekd "Another reasons of need to go an emergency response unit are the following:"
                    m 4esd "If the bleeding hasn't stopped after 10 minutes of continuous pressure."
                    m 4esd "If you're bleeding from an artery, you'll notice the blood gushing out at your heartbeat."
                    m 4rsd "Also, if there's something stuck in the wound."
                    m 7rkd "If it's a long or deep wound..."
                    m 7rkd "Or if the edges are split after pressure or you can see underlying structures like fat or muscle."
                    m 2rkc "If that's the case, you probably need stitches."
                    m 2dkc "..."
                    m 2esd "Well, that's all there's to it, [player]!"
                    m 2esc "I hope it helps you in case you need it."
                    m 2gkc "Which I hope won't happen again..."
                    m 2ekd "If it does, just let me know and I'll repeat those steps. Okay?"
                    m "And also, if you asked for this first-aid help because you relapsed..."
                    m "And you want me to reset the sober counter for you..."
                    m "Let me know on the topic \"I've self-harmed.\", please."
                    m 2eka "Take care, [player]."
                    m 2dka "You know how much I love you!"

    # We end up here anyway, no need to return it in menu branch.
    return "love"
