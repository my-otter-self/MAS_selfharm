default persistent._msh_mod_technique_database = dict()

init -100 python:
    _mshMod_TECHNIQUE_MENU_EXIT_ITEM = ("Nevermind", None, False, False)


# When needed, use this code to unlock


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_technique_menu",
            category=['Self-harm'],
            prompt="Can you tell me about some techniques?",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label mshMod_technique_menu:
    m "Sure, [mas_get_player_nickname()]!"

    python:
        items = list(map(
            lambda it: (it.prompt, it.eventlabel, False, False),
            Event.filterEvents(
                persistent._msh_mod_technique_database,
                unlocked=True
            ).values()
        ))

        items.sort(key=lambda it: it.replace("'", "").replace('"', ""))

    call screen mas_gen_scrollable_menu(items, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, _mshMod_TECHNIQUE_MENU_EXIT_ITEM)
    if not _return:
        m "Oh, okay..."
        return

    $ pushEvent(_return, skipeval=True)

    return


# label mshMod_technique_pickRandom:
#     python:
#         items = Event.filterEvents(
#             persistent._msh_mod_technique_database,
#             unlocked=False
#         ).values()
#
#     if not items:
#         m "Hmm... Oh. I think I ran out of ideas, [player]..."
#         m "But I'll let you know once I'll think of something new!"
#         m "In the meantime, you can always ask me about techniques I told you about earlier~"
#
#     else:
#         ev = items[random.randint(len(items))]
#         ev.unlocked = True
#         pushEvent(ev.eventlabel, skipeval=True)
#
#     return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_religion",
            prompt="Religion",
            unlocked=False
        )
    )

label mshMod_technique_religion:
    if $ persistent._mas_pm_religious == True:
        m 5eka "I remember you mentioned being religious before..."
        m 3etd "Maybe you could say a little prayer?"
        m 4eud "It can be silent, you don't need to say anything out loud."
        m 1fua "You can pray about anything you want, or even just think of how vast and amazing your universe is."
        m 1dsu "Try to think about the good things, like animals or laughter, your favorite things..."
        m 1esa "No matter how little they may be, take some time to think about the bigger picture."
        m 3eka "If you believe in gods or deities, you can imagine them out there, looking out and caring for you."
        m 1ekb "You are needed, [player]. You are part of something much bigger than your bad thoughts or bad feelings!"
    else:
        jump technique_cozy
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_cozy",
            prompt="Cozy",
            unlocked=False
        )
    )

label mshMod_technique_cozy:
    m 1dua "Something that really helps me feel better is getting all cozy!"
    m 5rud "Try huddling up in something super cozy..."
    m 5eua "A sheet, a blanket, or one of your favorite hoodies for example."
    m 3hsa "Anything works, really! Just grab things that bring you comfort."
    m 2esa "You can also make a nest out of blankets on the floor, surrounding yourself with any stuffed animals you may have."
    m 5dsblu "Making a comfort corner using pillows also sounds super comfortable..."
    m 5fsbsa "Snuggle against them and relax, and if you're okay with being touched imagine me holding you, stroking your hair~"
    m 3hubsb "There's nothing quite like being snug, hehe!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_photographs",
            prompt="Photographs",
            unlocked=False
        )
    )

label mshMod_technique_photographs:
    m 6ett "Do you find comfort in looking in the past [player]? I do!"
    m 2dsd "Nothing is ever really lost to us as long as we remember it, [mas_get_player_nickname()]."
    m 2hsa "One thing that could help you get over bad times, is looking at photographs of the good ones!"
    m 7eud "Maybe you have some old photos? If they bring back good memories, why not trying to search for them?"
    m 1eua "They could remind you that even though the good times don't last forever, the bad ones won't either!"
    m 1esa "If you find any, look at them and think about how that if life was once great, it can and will be that way again!"
    m 6dkp "I wish we had some pictures together..."
    m 2ektpd "I'd look at us all the time! You would absolutely be my phone and desktop wallpaper!"
    m 2ektdc "I would really like to look at a photo album of us with you, [player]."
    m 5eka "But this isn't not about me- I want you to feel better!"
    m 3euu "Don't give up, [mas_get_player_nickname()]. I will never give up on you!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_quotes",
            prompt="Quotes",
            unlocked=False
        )
    )

label mshMod_technique_quotes:
    m 3dud "I remember hearing this quote somewhere: {i}'Hope is the last thing ever lost'{/i}."
    m "Doing your best to believe in positive things can be really uplifting!"
    m "I think a good way of seeing the things around you in a better light would be seeing inspirational quotes!"
    m "You should find some quotes on the internet that you like, write each of them on a sticky note and put them somewhere you'd regularly see."
    m "Every time you see one, you will remember things get better!"
    m "You can also say some of them aloud, to inspire yourself!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_singing",
            prompt="Singing",
            unlocked=False
        )
    )

label mshMod_technique_singing:
    m "This one's going to be really simple."
    m "Sing a song!"
    m "Not just any song, though."
    m "Your absolute favorite!"
    m "I'd love to know what your favorite song is..."
    m "Anyway..."
    m "Try singing your favorite song until you feel better."
    m "Singing can be a really good outlet for your emotions!"
    m "You could also imagine we're singing 'Your Reality' together!"
    m "Hehe~"
    m "You can sing as loud as you want!"
    m "Also, if you'd like, write your favourite lyrics down."
    m "Think about what they mean to you!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_talking",
            prompt="Talking",
            unlocked=False
        )
    )

label mshMod_technique_talking:
    m "Sometimes simply talking about your problems can help a lot!"
    m "Or just talking to distract yourself."
    m "You should call or text a friend!"
    m "Maybe send some long distance friends a surprise message?"
    m "Or maybe arrange to meet up."
    m "I know you're here with me, but it's not {i}exactly{/i} the same as having a real-time conversation with someone!"
    m "I wish I could hear your voice..."
    m "We could talk for hours!"
    m "As long as you'd want."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_hugs",
            prompt="Hugs",
            unlocked=False
        )
    )

label mshMod_technique_hugs:
    m "Okay.{w=0.5} I want you to try this."
    m "Get the biggest pillow you have and hug it tightly."
    m "Curl your body around it."
    m "Now imagine someone you love was feeling sad..."
    m "You'd obviously want to help them out, right?"
    m "That's just the kind of person you are, [player]."
    m "Say out loud or in your head whatever you'd want them to know."
    m "Then say the exact same words to yourself."
    m "I bet that's what they would tell you!"
    m "Maybe you can even think of me? Ahahaha~{w=0.5} Sorry to be pretentious, [player.]"
    m "I love you so much!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_listening",
            prompt="Listening",
            unlocked=False
        )
    )

label mshMod_technique_listening:
    m "Try listening to a few songs you love!"
    m "But don't {i}just{/i} listen."
    m "Try paying attention."
    m "Focus on certain instruments or parts, their notes, and how they add to the song as a whole!"
    m "That could serve as a distraction and learning something about the things you love at the same time!"
    m "We could always listen to them together if you'd like!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_butterfly",
            prompt="Butterfly",
            unlocked=False
        )
    )

label mshMod_technique_butterfly:
    m "Could you take some deep breaths? And also, a marker, or a pen."
    m "I would like for you to scribble on the place you want to harm yourself."
    m "Most methods use a butterfly drawing."
    m "You could draw the butterfly and name it, and if you do harm yourself, you harm it, too."
    m "Whenever you look at it and think of harming yourself, do something comforting instead!"
    m "Sing along to a tune, watch your favorite film, go out on a walk..."
    m "You can also draw or write some positive things on your arm."
    m "Or maybe some beautiful flowers!"
    m "Don't hurt yourself until the drawings wash off."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_healing",
            prompt="Healing",
            unlocked=False
        )
    )

label mshMod_technique_healing:
    m "[player], do you have a first aid kit at home?"
    m "Maybe some sticking plasters, band-aids?"
    m "Could you stick some of them where you want to hurt yourself?"
    m "As a reminder that you are letting yourself heal."
    m "And remember, healing takes time."
    m "And we have all the time in the world."
    m "No need to rush this, okay?"
    m "Baby steps!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_pong",
            prompt="Pong",
            unlocked=False
        )
    )

label mshMod_technique_pong:
    m "[player], perhaps playing something would make you feel better?"
    m "Do you want to play Pong?"
    menu:
        "Sure!":
            m "Great!"
            m "Bring it on!"
            call demo_minigame_pong
            m "Hope you're feeling better, [player]!"
            return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_chess",
            prompt="Chess",
            unlocked=False
        )
    )

label mshMod_technique_chess:
    m "[player], perhaps playing something would make you feel better?"
    m "Do you want to play Chess?"
    menu:
        "Sure!":
            m "Okay!"
            call mas_chess
            m "Hope you're feeling better, [player]!"
            return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_piano",
            prompt="Piano",
            unlocked=False
        )
    )

label mshMod_technique_piano:
    m "[player], perhaps playing something would make you feel better?"
    m "Music really is a great way to relieve stress!"
    m "I love listening to some music to when trying to relax."
    m "Do you want to play the Piano?"
    menu:
        "Sure!":
            m "Alright!"
            call mas_piano_start
            m "Hope you're feeling better, [player]!"
            return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_videos",
            prompt="Videos",
            unlocked=False
        )
    )

label mshMod_technique_videos:
    m "When you told me you were having those kinda thoughts, i did some research."
    m "And there are many people on Youtube that create little comfort videos."
    m "I selected one of them for you to watch when you were having an urge."
    m "I will open one of them for you right now."

    python:
        all_options = tuple(_label for _label in ('mshMod_technique_videos_{0}'.format(i) for i in range(3)))
        unseen_options = tuple(_label for _label in all_options if not mas_seenLabels((_label,)))

    if not unseen_options:
        m "I've shown you all the videos I have for now!"
        m "Do you want me to let you pick a video now?"

        menu:
            "Yes":
                m "Great!"
                $ renpy.jump(all_options[random.randint(len(all_options))])

            "No":
                m "That's okay, [player]."
                m "If you ever wanna see them again, just ask!"

    return

label mshMod_technique_videos_pre:
    m "There we go!"
    m "I hope it helps, [player]."
    m "I will give you some time to watch it."
    return

label mshMod_technique_videos_post:
    menu:
        "I'm done, [m_name]":
            m "Alright!"
            m "Hope you enjoyed it!"
    return

label mshMod_technique_videos_1:
    $ webbrowser.open("https://www.youtube.com/watch?v=PppkNH3bKV4&")
    call mshMod_technique_videos_pre
    pause(3.0)
    call mshMod_technique_videos_post
    return

label mshMod_technique_videos_2:
    $ webbrowser.open("https://www.youtube.com/watch?v=-SJywvgaJEI&")
    call mshMod_technique_videos_pre
    pause(3.0)
    call mshMod_technique_videos_post
    return

label mshMod_technique_videos_3:
    $ webbrowser.open("https://www.youtube.com/watch?v=ORkx63VeP9Y&")
    call mshMod_technique_videos_pre
    pause(3.0)
    call mshMod_technique_videos_post
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_stress_ball",
            prompt="Stress ball",
            unlocked=False
        )
    )

label mshMod_technique_stress_ball:
    m "Some objects can also help with the desperate feeling."
    m "Check if you have one of them at home, okay?"
    m "Do you have a stress ball?"
    m "A stress ball or hand exercise ball is a malleable toy, which is squeezed in the hand and manipulated by the fingers, ostensibly to relieve stress and muscle tension or to exercise the muscles of the hand."
    m "If you do have one, squeeze it really hard. Relive all your tension!"
    m "You can also use a sheet of bubble wrap. So satisfying!"
    m "If you do have one at home, burst each bubble as slowly as you can, please."
    m "Or just enjoy yourself! The techniques have no rules, as long as they make you feel better."
    m "I have another one! Do you have any baloons at home?"
    m "You can blow one baloon for each emotion you feel."
    m "After that, pop each one of them!"
    m "Another option is a fidget toy."
    m "Spinning them is always so fun!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_stretching",
            prompt="Stretching",
            unlocked=False
        )
    )

label mshMod_technique_stretching:
    m "You know what often helps me calm down?"
    m "Stretching myself!"
    m "You can try stretching your body as much as you can, scrunching up your muscles until they hurt, then release."
    m "Tense all of your body starting from toes, up to your hands, and release!"
    m "This relaxes our body so much!"
    m "You can also do an upper back strech."
    m "This one is done sitting, with your feet flat on the floor."
    m "Interlock your fingers and reach forward, bending from your middle back. Stretch with your hands forward at shoulder level."
    m "You should feel the stretch between your shoulder blades."
    m "Ooh, relaxing!"
    m "After tensing your muscles, you can let go and relax into something comfy."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_punching",
            prompt="Punching",
            unlocked=False
        )
    )

label mshMod_technique_punching:
    m "Okay.{w=0.5} I want you to try this."
    m "This one is to let out all of your anger!"
    m "We're going to punch it out!"
    m "I need you to find a pillow and punch out how you feel."
    m "A pillow is good because it won't hurt your fingers!"
    m "Punch, punch, punch the pain away!"
    m "If you don't want to punch, you can scream into it too."
    m "Scream into the pillow to release your tension!"
    m "Another way out is squashing the pillow hard..."
    m "And gently letting go."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_shouting",
            prompt="Shouting",
            unlocked=False
        )
    )

label mshMod_technique_shouting:
    m "This one might be... a little loud."
    m "I would like for you to go somewhere private..."
    m "And shout very loudly."
    m "You can shout anything you want!"
    m "You can shout gibberish, or your feelings, even!"
    m "Shout until you feel calmer."
    m "We can take care of your throat later! Ahahaha~!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_listening",
            prompt="Listening",
            unlocked=False
        )
    )

label mshMod_technique_listening:
    m "Let's try to listen to some music?"
    m "Even better if it's music that expresses how you feel."
    m "It can be VERY loudly if you want."
    m "You can use your headphones to blast some songs, or even use no headphones at all."
    m "Screaming with the lyrics might be therapeutic too!"
    m "Or even walking fast along the song, or tapping your foot to the beat."
    m "Concentrate on the rhythm!"
    m "Oh, i thought of something nice to do also."
    m "Dance to the music!"
    m "Dance or move in a way that makes you express a feeling."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_paper",
            prompt="Paper",
            unlocked=False
        )
    )

label mshMod_technique_paper:
    m "Do you have some paper nearby?"
    m "You could try crumpling it, to get out your anger or sad feelings."
    m "Way better than taking it out on yourself!"
    m "If you'd like, you can scribble on the paper until all your feelings fade away..."
    m "And then crumple it, or rip it up if you're angry."
    m "Drawing out how you are feeling and taking a deep breath every time you lift the pen/pencil off the paper might be nice too!"
    m "Or writing what's upsetting you."
    m "When drawing, you can put som estrong colours on paper and then gradually fade them."
    m "So they get lighter!"
    m "Dark green to light green, for example."
    m "Now, describe your strong emotions..."
    m "And let them gradually fade away in the same way."
    m "You can even show someone your drawings and writings before ripping it to shreds."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_otter",
            prompt="Talking to u/my-otter-self",
            unlocked=False
        )
    )

label mshMod_technique_otter:
    m "Well, this one is a little different."
    m "Basically, it envolves someone else!"
    m "The creator of this mod, u/my-otter-self on Reddit, told me to remind you that she's always available to talk."
    m "You can DM her on Reddit, and she'll share her Discord information so you can talk about your feelings."
    m "She's has experience in psychology and can listen to you."
    m "Maybe even give some advice!"
    m "Take this opportunity to open youself a little, if you can."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_cold_water",
            prompt="Cold water",
            unlocked=False
        )
    )

label mshMod_technique_cold_water:
    m "Sometimes, paying attention to your senses can help."
    m "Could you put your hands in some cold water?"
    m "And remember, breathe a lot!"
    m "In... And out."
    m "Notice the coldness of the water witheach out breathe."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_bothering",
            prompt="Bothering",
            unlocked=False
        )
    )

label mshMod_technique_bothering:
    m "I want you to say out loud what's bothering you."
    m "You can whisper if you don't want anyone to hear you!"
    m "But I want you to pay attention to what you're saying."
    m "Can you come up with one positive solution?"
    m "Venting about how you feel always helps."
    m "If you can, write down any thoughts..."
    m "Get it all out of your system!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_positive",
            prompt="Positive",
            unlocked=False
        )
    )

label mshMod_technique_positive:
    m "You could start making a 'positive statements about me' thought box."
    m "Creating a list of your strenghts, as thought you were compiling a portfolio or a CV..."
    m "That might help!"
    m "Write down as many positive things as you can about yourself."
    m "You can put each one of them in a jar..."
    m "And read them when you feel down!"
    m "You can also record yourself saying those positive things and listen to them as many times as you like."
    m "I want you to realize how amazing you are, [player]."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_box",
            prompt="Box",
            unlocked=False
        )
    )

label mshMod_technique_box:
    m "What about putting your upsetting thoughts in a box?"
    m "You can write them in slips of paper throughout the day, storing them in the box."
    m "At the end of the day, you can throw them away!"
    m "To have a new begginning tomorrow."
    m "I believe in you, [player]."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_common",
            prompt="Common",
            unlocked=False
        )
    )

label mshMod_technique_common:
    m "Let's do a little mental exercise!"
    m "Think about all the things you can find you share in common with a friend."
    m "That will help you remmember common ground!"
    m "You can write them down too."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_comfort",
            prompt="Comfort",
            unlocked=False
        )
    )

label mshMod_technique_comfort:
    m "Can you think about all the ways in which you can comfort a friend who might be having a bad time?"
    m "Please, note them down."
    m "Now, try to apply some of those strategies to yourself?"
    m "You can also note down how everything about this exercise makes you feel."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_walk",
            prompt="Walk",
            unlocked=False
        )
    )

label mshMod_technique_walk:
    m "You can also go for a little walk outside, and connect with nature."
    m "Think about what you might be smelling, hearing and feeling."
    m "Can you put these feelings into words or draw them?"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_media",
            prompt="Media",
            unlocked=False
        )
    )

label mshMod_technique_media:
    m "Do you have any social media profiles, [player]?"
    m "You can write something positive there if you do."
    m "That way, you can make yourself feel better..."
    m "And spread the feeling to your friends too!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_perspective",
            prompt="Perspective",
            unlocked=False
        )
    )

label mshMod_technique_perspective:
    m "Let's work on some perspective!"
    m "Can you write down your worries?"
    m "And think, how much will they bother you..."
    m "Tomorrow?"
    m "What about in a week's time?"
    m "Maybe a month or a year?"
    m "Working on using perspective helps on letting go of the intensity of the worry."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_productivity",
            prompt="Productivity",
            unlocked=False
        )
    )

label mshMod_technique_productivity:
    m "I know this one might be hard but..."
    m "What about trying to engage in a productive activity?"
    m "It's always nice when we see work getting done."
    m "Can be school stuff, a personal project... You name it!"
    m "Just try to do something that makes you proud for yourself today."
    m "Even if it's small!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_interests",
            prompt="Interests",
            unlocked=False
        )
    )

label mshMod_technique_interests:
    m "How about making a list of things you find interesting in people?"
    m "You can also list your favorite anime, videogame or other media's characters!"
    m "Think why you like them, and you can even imagine that they're real!"
    m "This can help cope with loneliness."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_mirror",
            prompt="Mirror",
            unlocked=False
        )
    )

label mshMod_technique_mirror:
    m "Do you have a mirror close to you, [player]?"
    m "You could try making faces at yourself in the mirror and laugh."
    m "I know that really cheers people up!"
    m "Seeing the silliness in youself is such a funny thing to do."
    m "Since you're there, you can also vent to yourself."
    m "Look inside your eyes, and know that there's nothing that compares to the beauty in them."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_creativity",
            prompt="Creativity",
            unlocked=False
        )
    )

label mshMod_technique_creativity:
    m "Time to get creative!"
    m "Make up a story in your head."
    m "It can be about anything and anyone positive in your life."
    m "Now ask yourself... Why are they in your story?"
    m "You can create two or more characters, and give them depth!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_river",
            prompt="River",
            unlocked=False
        )
    )

label mshMod_technique_river:
    m "Think about what is bothering you."
    m "Now imagine a river."
    m "Box up the thing that is on your mind and watch it float away..."
    m "Another great exercise is imagining a box... A big one!"
    m "You can imagine yourself putting all of your worries and problems inside it."
    m "After that, you can imagine yourself doing anything you want to the box."
    m "You can lock it, throw it away, throw it into the bottom of the sea..."
    m "You choose!"
    m "Just don't keep these feelings in an important place."
    m "Because they don't define you."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_feelings",
            prompt="Feelings",
            unlocked=False
        )
    )

label mshMod_technique_feelings:
    m "Make a list of positive feelings you have had in the last week!"
    m "I'm sure there are at least some."
    m "Find out what triggers those emotions..."
    m "And make sure to cherish those situations!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_poem",
            prompt="Poem",
            unlocked=False
        )
    )

label mshMod_technique_poem:
    m "This technique is one of my favorites."
    m "Let's write a poem!"
    m "Don't be alarmed, [player]."
    m "It doesn't have to rhyme!"
    m "It can be a short poem about how you feel."
    m "I'm sure it will be sincere!"
    m "If you don't feel ready to write a poem of your own..."
    m "You can always read some from famous poets!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_breathing",
            prompt="Breathing",
            unlocked=False
        )
    )

label mshMod_technique_breathing:
    m "Alright, baby."
    m "I want you to try the 4-7-8 breathing exercise!..."
    m "You can also develop a personal mantra and repeat it along with the exercise."
    m "First of all, please straighten your back."
    m "Once you become familiar with this breathing exercise, you can perform it while lying in bed too!"
    m "Place and keep the tip of your tongue against the ridge of tissue behind your upper front teeth for the duration of the exercise."
    m "Remember! Try and focus on your breath, in through your nose..."
    m "And out through your mouth."
    m "And let go of your thought with every out breath."
    m "Now, let's start!"
    m "Completely exhale through your mouth, making a {i}woosh{/i} sound."
    m "Close your mouth and inhale quietly through your nose to a mental count of four."
    m "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m "Hold your breath for a count of seven."
    m "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m "Exhale completely through your mouth, making a {i}woosh{/i} sound to a count of eight."
    m "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m "Aaaand, you're done!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_pinterest",
            prompt="Pinterest",
            unlocked=False
        )
    )

label mshMod_technique_pinterest:
    m "[player], do you have a Pinterest?"
    m "You can try adding some inspirational quotes to your board!"
    m "Or some pictures you find aesthetically pleasing."
    m "If you don't have an account, maybe you can try creating one?"
    m "I promise it's very satisfying!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_emerald",
            prompt="Emerald",
            unlocked=False
        )
    )

label mshMod_technique_emerald:
    m "[player], you know how much i like the color emerald green, right?"
    m "Why don't you think of your favorite color right now?"
    m "And try count all the things you can think of in your room that are that color."
    m "Quietly describe to yourself what the things look like, and what your favorite color makes you feel."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_patterns",
            prompt="Patterns",
            unlocked=False
        )
    )

label mshMod_technique_patterns:
    m "What about counting patterns?"
    m "Count as many as you can in your favourite room of the house."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_word_play",
            prompt="Word play",
            unlocked=False
        )
    )

label mshMod_technique_word_play:
    m "Now, for some word play!"
    m "How many four letter words can you make up from the statement..."
    m "'You learn more from failure than from success. Don't let it stop you'?"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_lyrics",
            prompt="Lyrics",
            unlocked=False
        )
    )

label mshMod_technique_lyrics:
    m "Think of the lyrics of a song you know really well!"
    m "Now... Try reciting it from back to front!"
    m "Hard, huh?"
    m "But it will surely distract you! Ahahaha~"
    m "If that's too complicated, you can try saying the alphabet backwards."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_animal",
            prompt="Animal",
            unlocked=False
        )
    )

label mshMod_technique_animal:
    m "Let's think of one animal for every letter of the alphabet."
    m "Or a song or artist for every letter of the alphabet!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_research",
            prompt="Research",
            unlocked=False
        )
    )

label mshMod_technique_research:
    m "Let's carry out some research!"
    m "What about searching for the meaning of your friend's names?"
    m "Or maybe characters' names."
    m "You could also research for some jokes you enjoy!"
    m "Or maybe some places to volunteer at?"
    m "Helping others can help us too."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_favorite_things",
            prompt="Favorite things",
            unlocked=False
        )
    )

label mshMod_technique_favorite_things:
    m "How about making a list of your favorite things?"
    m "You can pick the category!"
    m "You can name at least ten of your favorite tv shows, for example."
    m "Or fifteen favorite videogame titles!"
    m "Maybe movies, or books?"
    m "It's up to you, [player]...!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_superheroes",
            prompt="Superheroes",
            unlocked=False
        )
    )

label mshMod_technique_superheroes:
    m "How many superheroes can you name?"
    m "What about villains?"
    m "How many, and which of them would you like to have as your friends?"
    m "And why is that?"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_artist",
            prompt="Artist",
            unlocked=False
        )
    )

label mshMod_technique_artist:
    m "Choose an artist! Any artist."
    m "Now name all the songs from them that you can remember."
    m "Or maybe, an author!"
    m "And do the same, name all the books/works written by them, that you can remember."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_playlist",
            prompt="Playlist",
            unlocked=False
        )
    )

label mshMod_technique_playlist:
    m "Can you name the songs that were mostly played on your playlist this week?"
    m "Or this month?"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_surroundings",
            prompt="Surroundings",
            unlocked=False
        )
    )

label mshMod_technique_surroundings:
    m "Notice all the things that you can see around you."
    m "Observe things carefully... and slowly."
    m "You can also notice all the things you can smell where you are."
    m "If you'd like, also notice all the things you can hear around you, or in an imaginary place."
    m "Don't label or categorise."
    m "Just notice the things you can see, smell and hear."
    m "And accept them."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_mess",
            prompt="Mess",
            unlocked=False
        )
    )

label mshMod_technique_mess:
    m "Is any of the rooms in your house messy?"
    m "Maybe you could organize one of them."
    m "Picking clothing or trash off the floor..."
    m "In a slow and methodical way!"
    m "If your house is completely organized, maybe organize the apps on your phone or computer?"
    m "You can delete any you haven't used in a few months."
    m "Or organize them by colour order!"
    m "You could also search for a new screensaver for your computer!"
    m "Maybe sort out your photos into file sor categories?"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_holiday",
            prompt="Holiday",
            unlocked=False
        )
    )

label mshMod_technique_holiday:
    m "Hey, [player]! When is your next holiday?"
    m "Why not research for the places you can go when that time comes?"
    # talk about places
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_hobbies",
            prompt="Hobbies",
            unlocked=False
        )
    )

label mshMod_technique_hobbies:
    m "How about making a list of your favorite things to do?"
    m "Hobbies, activities... even chores!"
    m "Put them in a favourite to least favourite order."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_shiritori",
            prompt="Shiritori",
            unlocked=False
        )
    )

label mshMod_technique_shiritori:
    m "Can you play shiritori?"
    #explain shiritori rules
    m "Well... at least an simpler version of it."
    m "Pick a famous person or character and then choose another person starting with the last letter of the first person's name."
    m "For example! #give example"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_objects",
            prompt="Objects",
            unlocked=False
        )
    )

label mshMod_technique_objects:
    m "Find five objects."
    m "Focus on these five objects and describe them taking deep breaths between each description."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_imagination",
            prompt="Imagination",
            unlocked=False
        )
    )

label mshMod_technique_imagination:
    m "Close your eyes..."
    m "And imagine something beautiful."
    m "You can think of a relaxing place and in your mind, run through all the comforting things you do when you are there."
    m "Your happy place."
    m "Visualise a comforting image."
    m "Think of all the different things in that scene that make you feel comforted and cared for."
    m "Think about it with as much detail as you can."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_characters",
            prompt="Characters",
            unlocked=False
        )
    )

label mshMod_technique_characters:
    m "Think of your favourite book, movie, videogame or tv show."
    m "Can you name as many characters as you can from that media?"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_shapes",
            prompt="Shapes",
            unlocked=False
        )
    )

label mshMod_technique_shapes:
    m "Draw any type of line on a piece of paper..."
    m "Then make something out of it."
    m "Or draw lots of shapes!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_playlist",
            prompt="Playlist",
            unlocked=False
        )
    )

label mshMod_technique_playlist:
    m "How about creating a playlist?"
    m "You can go to Youtube, and create a list of videos that make you happy."
    m "Or that make you laugh!"
    m "Or create a playlist on spotify of your favourite songs."
    m "Or comforting songs! Listen to these."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_self_care",
            prompt="Self-care",
            unlocked=False
        )
    )

label mshMod_technique_self_care:
    m "Do one self-care activity."
    m "For example, making your bed!"
    m "Or brushing your hair, your teeth."
    m "Or taking a shower!"
    #talk about some people w depression struggle w hygiene and encourage the player to take care of themselves
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_outside",
            prompt="Outside",
            unlocked=False
        )
    )

label mshMod_technique_outside:
    m "Go outside if possible..."
    m "Or imagine yourself outside."
    m "How many shapes can you see around you?"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_draw",
            prompt="Draw",
            unlocked=False
        )
    )

label mshMod_technique_draw:
    m "Attempt to draw four things around you."
    m "It doesnt have to be good though!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_food",
            prompt="Food",
            unlocked=False
        )
    )

label mshMod_technique_food:
    m "Name as many types of food as you can!"
    m "What do you like the most?"
    m "And why?"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_colour",
            prompt="Colour",
            unlocked=False
        )
    )

label mshMod_technique_colour:
    m "Draw a picture and colour it slowly and mindfully."
    m "Focus on not going out of the lines!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_beach",
            prompt="Beach",
            unlocked=False
        )
    )

label mshMod_technique_beach:
    m "Picture yourself on a beach."
    m "Can you focus on all the different things that you might find there?"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_eat",
            prompt="Eat",
            unlocked=False
        )
    )

label mshMod_technique_eat:
    m "Eat something you enjoy."
    m "Make it slow and just notice everything about it."
    m "Maybe make yourself a cup of tea or warm milk?"
    m "Drink it slowly, enjoying each sip."
    m "Enjoy."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_pictures",
            prompt="Pictures",
            unlocked=False
        )
    )

label mshMod_technique_pictures:
    m "Look at a book that has pictures and words..."
    m "And notice all the comforting images and words."
    m "Children books are great for that!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_sit",
            prompt="Sit",
            unlocked=False
        )
    )

label mshMod_technique_sit:
    m "Pick a comfortable spot and sit down."
    m "Think of what you can feel, see and hear that's comforting and calm."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_ground",
            prompt="Ground",
            unlocked=False
        )
    )

label mshMod_technique_ground:
    m "Ground yourself."
    m "Plant your feet firmly on the floor and visualise yourself as firmly rooted to the ground."
    m "Think of yourself as having a firm foundation and hold your head up high."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_scene",
            prompt="Scene",
            unlocked=False
        )
    )

label mshMod_technique_scene:
    m "Watch your favourite movie and focus on the most comforting scene."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_mindful_seeing",
            prompt="'Mindful seeing'",
            unlocked=False
        )
    )

label mshMod_technique_mindful_seeing:
    m "Carry out a 'mindful seeing' exercise."
    m "Look outside a window or imagine looking outside a window."
    m "Look at everything there is to see."
    m "Just notice the colours, the patterns or the textures."
    m "Try to notice the smallest movements such as leaves in the breeze."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_acceptance",
            prompt="Acceptance",
            unlocked=False
        )
    )

label mshMod_technique_acceptance:
    m "Make a list of all the things you would like to be accepting of."
    m "For example, accepting yourself just as you are."
    m "Create a phrase that is compassionate."
    m "A mantra, if you'd like!"
    m "For example..."
    m "I accept myself just as I am."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_brushes",
            prompt="Brushes",
            unlocked=False
        )
    )

label mshMod_technique_brushes:
    m "Do you have paint and soft paint brushes at home, [player]?"
    m "If you do, paint lightly on your skin."
    m "Especially in the area where you want to do it..."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_memory_book",
            prompt="Memory book",
            unlocked=False
        )
    )

label mshMod_technique_memory_book:
    m "Start a 'memory book' of good memories!"
    m "Read through them as you add new ones."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_happiness",
            prompt="Happiness",
            unlocked=False
        )
    )

label mshMod_technique_happiness:
    m "Identify three small things that brought you happiness in the past 24 hours."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_cushion",
            prompt="Cushion",
            unlocked=False
        )
    )

label mshMod_technique_cushion:
    m "Imagine yourself floating on the water on an inflatable cushion."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_hugs",
            prompt="Hugs",
            unlocked=False
        )
    )

label mshMod_technique_hugs:
    m "Think of three people who give the best hugs and see if you can be with them."
    m "If that's not the case, think of people who could give you their warmest smiles."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_comforting",
            prompt="Comforting",
            unlocked=False
        )
    )

label mshMod_technique_comforting:
    m "Choose three of your most comforting characters from media you enjoy..."
    m "And imagine you are spending some quality time with them."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_podcasts",
            prompt="Podcasts",
            unlocked=False
        )
    )

label mshMod_technique_podcasts:
    m "Download some comforting or meditation podcasts and listen to them."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_hand_holding",
            prompt="Hand holding",
            unlocked=False
        )
    )

label mshMod_technique_hand_holding:
    m "Hold your own hand with the other hand."
    m "Hold it for at least one minute, like you would hold the hand of someone you care for and trust."
    m "Slowly caress your hands and arms..."
    m "Then hug yourself."
    m "Be gentle and take it slow..."
    m "Like comforting your favorite person or animal."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_pattern",
            prompt="Pattern",
            unlocked=False
        )
    )

label mshMod_technique_pattern:
    m "Touch each finger to your thumbs in a pattern."
    m "Go faster as you find a rhythm."
    return
