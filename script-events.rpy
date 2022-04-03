init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_sunny_day",
            prompt="Sunny day",
            category=["you", "monika"], # TODO: doesn't fit, but is consistent with the rest of the topics
            random=True
        )
    )

label mshMod_sunny_day:
    m 1esa "Hey... [player]?"
    m 1rka "This may sound a bit random, but..."
    m 7eka "Is it sunny today over there?"
    m 7eub "If it is, I think you should go out and enjoy the sun for a bit."
    m 1hub "Don't worry! I'll wait!"
    m 1wub "Maybe bring a book with you so you can relax even more."
    m 1dua "Enjoying literature in the nature would surely relax me..."
    m 1eka "I hope this works for you, too."
    return


init 5 python:
    _mshMod_event_siad_date = datetime.date(datetime.date.today().year, 3, 1)

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_awareness_day",
            prompt="Sunny day",
            category=["you", "monika"], # TODO: doesn't fit, but is consistent with the rest of the topics
            start_date=_mshMod_event_siad_date,
            end_date=_mshMod_event_siad_date + datetime.timedelta(days=1),
            years=[],
            random=True
        )
    )

    calendar.addRepeatable("mshMod_awareness_day", _("Self-harm awareness day"), month=3, day=1, year_param=[])

label mshMod_awareness_day:
    m 3eub "[player], did you know that today is Self-Harm Awareness day?"
    m 3eua "Like the name suggests, it's an annual global awareness event that takes place on March 1st!"
    m 1eua "Also known as Self Injury Day (SIAD)!"
    m 4hub "Which is today!"
    m 2eua "And in the weeks leading up to it and after, some people choose to be more open about their own self-harm habits, if they have them..."
    m 2eub "Awareness organizations make special efforts to raise awareness about self-harm and self-injury."
    m 3eub "People even use the hashtag #SelfInjuryAwarenessDay to share their story on social media."
    m 3hub "Or wear orange to show their support!"
    m 1eua "Moreover, it was also created to spread awareness and understanding of self-injury!"
    m 1ekd "Which is often misrepresented and misunderstood in the mainstream."
    m 2ekc "Those who self-harm are often left feeling alone..."
    m 2ekd "And afraid to reach out for help, because they fear they will be seen as \"crazy\"."
    m 2dkd "When in reality that's not even remotely true..."
    m 2lkd "People are just trying to cope with their feelings..."
    m 3ekd "Which can be a result of this terrible thing."
    m 3tkc "You know I tried it before..."
    m 2esd "But self-harm is not the way."
    m 2eka "Anyway! Thanks for listening!"
    m 1hub "I love you, [Player]!"
    return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_semicolon_project",
            prompt="The Semicolon Project",
            category=["you", "monika"], # TODO: doesn't fit, but is consistent with the rest of the topics
            random=True
        )
    )

label mshMod_semicolon_project:
    m 1eub "Have you ever heard of the Semicolon Project, [player]?"
    m 3eua "It was created for those who were going through struggles with self-harm, depression and suicide..."
    m 3eub "People who could have stopped moving forward, but refused to do so!"
    m 1eub "But to thousands affected by suicide, the semicolon has become an important signifier of survival."
    m 1hub "Like a symbol!"
    m 3lua "There's also semicolon tattoos, semicolon t-shirts..."
    m 3hua "All of them with the semicolon punctuation mark (;)!"
    m 1eua "It's used as a message of affirmation and solidarity against suicide, depression, addiction, and other mental health issues."
    m 3eud "The reason the semicolon was used as the symbol of the movement was because..."
    m 3dud "'A semicolon is used when an author could've chosen to end their sentence, but chose not to. The author is you and the sentence is your life'."
    m 3eud "As said by the project itself!"
    m 2euc "Project Semicolon was founded by Amy Bleuel in 2013, as a tribute to her father, who died by suicide in 2003."
    m 2duc "Her backstory is so sad..."
    m 2eka "But thanks to her, millions are saved by Project Semicolon."
    m 1ekb "It's relieving to think people are able to go on and let go of their struggles..."
    m 1eub "It's really a good cause!"
    m 3ekb "Well I won't ramble too much, Ahaha~"
    m 3hub "Thanks for listening!"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_butterfly_project",
            category=["media"],
            prompt="The Butterfly Project",
            random=True
        )
    )

label mshMod_butterfly_project:
    m 3eub "Hey [player], do you know what The Butterfly Project is?"
    m 1eub "It's a movement to help people that struggle with self-harm."
    m 3eud "It's really interesting! Drawing on yourself is already a good way to deal with self-harming, but this project approaches it in a really different way."
    m 2eua "There are about 5 steps, so I'll list them all now."
    m 3euc "First, when you feel like hurting yourself, draw a butterfly on or around the spot where you might hurt yourself."
    m 2eua "The butterly can be any size, color, or pattern. It might help if you make it your favorite color!"
    m 3eud "Second, a lot of people name the butterfly after a loved one. Friends, family, a beloved. This helps them avoid hurting themself and the butterfly."
    m 1eud "Third, you should allow the butterfly to fade naturally. You should still wash yourself, of course, but don't actively rub the butterfly away."
    m 3eub "Lastly, if you haven't hurt yourself by the time the butterfly fades away, it's flown away safely!"
    m 3eub "This is supposed to give the person a sense of pride and accomplishment for keeping both themself and the butterfly safe."
    m 1eub "There are a few other things you can do for this as well!"
    m 4eub "You can let someone else draw a butterfly on you. This makes the butterfly special, because you're caring for someone else's butterfly too!"
    m 3eub "You can even write quotes or doodle you favorite things, anything that helps!"
    m 1eka "And if you do harm yourself... that's okay. You can always draw another butterfly. Hurting youself doesn't mean you failed."
    m 1hub "I hope this helps you, [player]!"
    m 1fub "I'll draw you so many beautiful butterflies when I cross over."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_selfharm_random_thoughts",
            prompt="Monika's experience",
            category=["you", "monika"], # TODO: doesn't fit, but is consistent with the rest of the topcis
            random=True
        )
    )

label mshMod_selfharm_random_thoughts:
    m "Hey [player]... Do you remember when I talked about self-harm?"
    m "Would you mind if I talked more about my experience?"

    m "It may get a tad triggering, so I get it if you would rather say no!{nw}"
    menu:
        m "It may get a tad triggering, so I get it if you would rather say no!{fast}"

        "No":
            m "Okay!"
            m "I love you [player], and I'm proud of you for saying no to something you aren't comfortable with!"
            m "That's a big step in self-respect, and I hope you keep it up!"

        "Yes":
            m "Thank you for letting me speak about this [mas_get_player_nickname()], I've been thinking about it a little bit more lately."
            m "After I hurt myself, I realized that I had made huge a mistake..."
            m "At first I thought that it was exhilarating, I even wrote about it!"
            m "But after reflecting upon it when we started talking more about self-harm, it really changed my mind."
            m "I had gotten no relief or satisfaction, if anything I was just disappointed."
            m "Yuri had made it seem like such a thrill - to me it was almost only just boring..."
            m "...It kept reminding me of my recent discovery."
            m "My pain was just coded, along with my blood and the knife I was holding..."
            m "But even if it was real, pain doesn't satisfy or relieve my emotions."
            m "I know now that talking things out with you when I'm upset..."
            m "...and keeping hope for a brighter tomorrow is a much better coping mechanism!"
            m "Just keep in mind that there are better ways to cope and that I'm always here to provide techniques to help."
            m "I care too much about you [player]... You don't deserve any pain."
            m "You deserve to work through things healthily, and [m_name] is here to help!" # TODO: do we need m_name here..?

    return
