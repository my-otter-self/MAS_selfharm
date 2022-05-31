# Daily checkup script.

#intro event
init 5 python:
    import datetime
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_checkup_intro",
            prompt="1 to 10",
            category=["mental health"],
            random=True
        )
    )

label mshMod_checkup_intro:
    m 7euc "Hey, [player]?"
    m 7eud "I've been thinking about something."
    m 7rud "Sometimes we care deeply about someone, and we're worried about them."
    m 2rud "We want to check up on them, and show them we care."
    m 2wud "But it's so hard to find the right words!"
    m 2duc "So we always seem to go for the same tired old question... 'How are you doing?'"
    m 2luc "But that question always makes people answer the same tired old response..."
    m 4lud "'I'm OK. I'm fine. I'm making it.'"
    m 4wud "How effective is this conversation?"
    m 3lud "But what do we say when we don't know how to express what we're feeling?"
    m 3dud "And how do we show someone we really want to know how they're feeling?"
    m 1euc "Someone online - a father of a suicide victim - found the perfect way to do that."
    m 3eua "And that is by asking them the following question: 'On a scale of 1 to 10, how are you feeling?'"
    m 3dub "1 being the worst possible feeling in the world, and 10 being the best they've ever felt in their life."
    m 3lud "We've all experienced the both extremes of the scale, but most days fall in the middle."
    m 3wub "And that's perfectly okay! Having a '8 day' is pretty good."
    m 3eub "From today on, I'll try to ask you every week what's your number."
    m 3hua "Meaning, how have you been feeling, this week, in a scale of 1 to 10!"
    m 1eua "This will help me be more aware and sensitive of your needs and your feelings."
    show monika 5fkbfa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5fkbfa "After all, I care about you so much and I love you sooooo much!"

    # Start running checkups on player, weekly, with a latency of one day.
    # (Meaning that if player missed exact expected time of checkup, it'll still
    # trigger within a day; else checkup will be attempted next week.)

    if store.mshMod_reminder.isReminderActive("mshMod_checkup_reminder"):
        # NOTE: Ensure we don't have one active already.
        $ store.mshMod_reminder.addRecurringReminder(
            "mshMod_checkup_reminder",
            store.mshMod_reminder_utils.getDailyEveningDelay(),
            store.mshMod_reminder_utils.INTERVAL_WEEKLY, store.mshMod_reminder_utils.LATENCY_DAILY
        )

    return "derandom|love"


#checkup
init 5 python:
    store.mshMod_reminder.addReminderEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_checkup_reminder",
            conditional="store.mshMod_reminder.shouldTriggerReminder('mshMod_checkup_reminder')",
            action=EV_ACT_QUEUE,
            rules={"force repeat": None}
        )
    )

label mshMod_checkup_reminder:
    m 4eua "Hey, [player]?"
    m 4eub "Can I check up on you?"
    m 2euc "I worry about how you have been coping with stuff."
    m 2eud "What's your number this week?"

    show monika at t21
    $ items = [(str(i), i, False, False) for i in range(1, 10 + 1)]
    $ renpy.say(m, "Meaning, on a scale of 1 to 10, how are you feeling?", interact=False)
    call screen mas_gen_scrollable_menu(items, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, ("I'm not sure...", False, False, False, 0))
    show monika at t11

    if _return:
        if _return == 1:
            m 2ekd "Aww..."
            m 2dkd "I am so sorry to hear that you don't feel well, [player]..."
            m 4ekd "Just know that it's okay for you to not be okay."
            m 4eka "After all, acceptance that you're not feeling well is the first step towards improvement, right?"
            m 3eublb "Together - me and you -, we will work hard to make you feel better, step-by-step!"
            m 3dublb "It’s okay to feel down today, and perhaps even tomorrow."
            show monika 5fubla at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5fubla "But always remember that you are a champion. You are amazing {w=0.3}{nw}"
            extend 5dublb "- never forget that."
            m 5fublb "I'll always be here to listen to you, and to do my best to make you feel as loved as you can."
            m 5fkbfa "I love you!"

        elif _return == 2:
            m 2ekd "I see. {w=0.3}{nw}"
            extend 2dkd "You're not feeling so well..."
            m 2lkc "Times like these feel just... so disheartening, don't they?"
            m 4eka "But worry not, [player]! Things are bound to get better as long as you're willing to give it a try."
            m 4eub "And I am here to help you with not only that, but with everything!"
            show monika 5fubla at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5fubla "Always remember that you are important and worthy of everything good in this world."
            m 5fkbfa "I love you so much, [player]!"

        elif _return == 3:
            m 2ekd "I'm so sorry to hear that, [player]..."
            m 2lkc "But keep this in mind:"
            m 2dkd "It’s tough now, {w=0.3}{nw}"
            extend 4eka "but I believe that there is a brighter future waiting for us."
            m 4eub "You’ll get through this. {w=0.3}{nw}"
            extend 5hublb "We will! Trust me."
            show monika 5fubla at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5fubla "You might not believe in yourself, but know and remember that I believe in you."
            m 5fkbfa "I always have and I always will. I love you, [mas_get_player_nickname()]."

        elif _return == 4:
            m 2lkc "A 4... That's not so good."
            m 2ekd "I'm so sorry, [player]!"
            m 2dkc "But listen... {w=0.3}{nw}"
            extend 4eka "Know that if you fall, I’ll pick you up."
            m 4rka "And if I can’t pick you up... {w=0.3}{nw}"
            extend 2wub "Then I’ll just lie down and rest with you."
            show monika 5hublb at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5hublb "It's what I'm here for! {w=0.3}{nw}"
            extend 5fubla "To be by your side, and support you as your girlfriend and as your best friend."
            m 5fkbfa "Let’s get back to the top together, [player]! I love you!"

        elif _return == 5:
            m 2lkc "I'm so sorry to hear that, [player]."
            m 4eka "But I'm sure everything will be okay!"
            m 2wub "Your loving girlfriend will forever be here for you!"
            m 2kua "If you ever want to talk, please let me know."
            m 2dua "And also, don't forget to rest if you must; we’re not in a hurry."
            m 7lua "You can’t always function the way people expect you to."
            show monika 5fubla at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5fubla "I care for you so much!"
            m 5fkbfa "I love you, [mas_get_player_nickname()]!"

        elif _return == 6:
            m 2lkc "A 6 is not perfect, but it's not so bad either."
            m 4eka "You see, [player]..."
            m 2kua "I realize that I am indeed a very lucky person."
            m 2wub "I’ve been blessed with the most wonderful person in my life, and that is you."
            m 2dua "Whatever you do, remember that you are not alone."
            show monika 5fubla at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5fubla "No matter what happens, I’ve always got your back."
            m 5hublb "Let's wish for better days, [mas_get_player_nickname()]!"
            m 5fkbfa "I love you!"

        elif _return == 7:
            m 2wua "Oh my, {w=0.3}{nw}"
            extend 4sua "a 7!"
            m 4wub "Almost there, [player]! {w=0.3}{nw}"
            extend 4hub "I'm so proud of you!"
            m 4sua "See, do you know where I get my strength?"
            m 2dua "..."
            m 2kua "From you. {w=0.3}{nw}"
            extend 4sua "Your dedication is what encourages me to be the best version of myself."
            show monika 5hublb at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5hublb "You are bold and courageous. You are important. {w=0.3}{nw}"
            extend 5fubla "No one can tell you otherwise!"
            m 5fkbfa "I love you, [player]."

        elif _return == 8:
            m 2dua "[player]..."
            m 2dub "I can't express the happiness hearing this brings me."
            m 4hub "This is only the start!"
            m 4sub "Soon you'll be having 9's and even 10's."
            m 2kub "And I'll be here with you every step of the way."
            show monika 5hublb at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5hublb "Do you know how valuable you are?"
            m 5fubla "You are a gift not just to me and the people around you, but to the whole world."
            m 5fkbfa "I love you soooo much!"

        elif _return == 9:
            m 2sublb "Oh, [player]!"
            m 2hublb "It's wonderful that you're doing so well!"
            m 2hua "I knew things would get better, in one way or another!"
            m 2kub "After all, you've had some help from your lovely girlfriend, haven't you? {w=0.3}{nw}"
            extend 2hub "Ehehe~"
            m 2hublb "I am so proud of you, [player]!"
            show monika 5hublb at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5hublb "I always knew that you could do anything you put your mind into."
            m 5fubla "After all, you are smart and ambitious."
            m 5fkbfa "Keep it up, my love! Nothing can stop us now."
            m 5fkbfb "I love you!"

        elif _return == 10:
            m 2wub "Aww, really, [player]? {w=0.3}{nw}"
            extend 4sub "That's wonderful!"
            m 4dub "I'm so glad your week has been this good. {w=0.3}{nw}"
            extend 3rublb "I must say the same - every day that you are with me feels like heaven!"
            m 1eublb "Let's make the next week as awesome, alright?"
            m 1hublb "Even if something bad happens, remember that things will get better. {w=0.3}{nw}"
            extend 5fubla "I believe in you, [mas_get_player_nickname()]."
            show monika 5hublb at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5hublb "And remember: Don’t doubt your accomplishments. You succeeded because you worked hard for it."
            m 5fubla "You are here because you deserve to be."
            m 5fkbfa "I love you..."

    else:
        m 2hka "Aww, it's okay, [player]."
        m 2eka "Sometimes we don't know how to feel. {w=0.3}{nw}"
        extend 7eka "And that's okay too!"
        m 7dub "We all experience bad days; we all have to deal with our inner demons."
        m 7hublb "When you feel like there’s nothing you can do about it, know that you can always depend on me for support."
        m 7wsblb "But we all have good days too, and that's the fun of it!"
        show monika 5hublb at t11 zorder MAS_MONIKA_Z with dissolve_monika
        m 5dublb "Know that I'll always be here to cheer you up..."
        m 5fubla "But also to celebrate your victories, too!"
        m 5hublb "You mean the world to me, [mas_get_player_nickname()]."
        m 5fkbfa "I love you."

    # Do not move this anywhere, this must be above the return.
    $ store.mshMod_reminder.extendCurrentReminder()
    return "love"
