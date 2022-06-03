# Monika's playlist topics and songs.

init 5 python in mas_bookmarks_derand:
    # Ensure things get bookmarked and derandomed as usual.
    label_prefix_map["mshMod_playlist_song_song_"] = label_prefix_map["mas_song_"]


init 11 python in mshMod_playlist:

    import store
    import mutagen.oggvorbis as mutaogg

    CUSTOM_PLAYLIST_DIR_SUFFIX = "Submods/MAS Self Harm Submod/music/"
    CUSTOM_PLAYLIST_DIR = store.config.basedir + "/game/" + CUSTOM_PLAYLIST_DIR_SUFFIX
    CUSTOM_PLAYLIST_RELDIR = CUSTOM_PLAYLIST_DIR_SUFFIX
    PLAYLIST_FILE = "playlist.ogg"

    playlist_shown = False

    def showPlaylist():
        _audio_file, _ext = store.songs._getAudioFile(CUSTOM_PLAYLIST_DIR + PLAYLIST_FILE)
        disp_name = store.songs._getDispName(_audio_file, _ext, PLAYLIST_FILE)
        loop_prefix = store.songs._getLoopData(_audio_file, _ext)

        choice = (
            store.songs.cleanGUIText(disp_name),
            loop_prefix + CUSTOM_PLAYLIST_RELDIR + PLAYLIST_FILE
        )

        store.songs.music_choices.append(choice)

        page = sorted(store.songs.music_pages.keys())[-1]
        if len(store.songs.music_pages[page]) == store.songs.PAGE_LIMIT:
            store.songs.music_pages[page + 1] = [choice]
        else:
            store.songs.music_pages[page].append(choice)

        store.persistent._mas_pm_added_custom_bgm = True
        playlist_shown = True

    if store.seen_event('mshMod_playlist_intro'):
        store.mshMod_playlist.showPlaylist()


#playlist
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_playlist_intro",
            category=["mental health"],
            prompt="Playlist",
            random=True
        )
    )

label mshMod_playlist_intro:
    m 1esd "Hey... [player]?"
    m 3eub "I... Have a surprise for you!"
    m 3rub "It's not much, but..."
    m 2ekbla "I made it with love."
    m 3eub "Are you excited? Ahaha~"
    m 1hub "Well, better show it to you."
    m 1esb "I... made you a playlist!"
    m 1tkbla "Romantic, isn't it?"
    m 3hsb "You can access it on \"Music\"."
    m 1esa "Or I can play it for you!"

    if not store.mshMod_playlist.playlist_shown:
        $ store.mshMod_playlist.showPlaylist()

    m 2eub "Do you want me to?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want me to?{fast}"

        "Yes":
            $ play_song(store.mshMod_playlist.CUSTOM_PLAYLIST_RELDIR + store.mshMod_playlist.PLAYLIST_FILE, set_per=True)

        "Not yet, [m_name]":
            m 1eka "Oh, alright."
            m 1eub "Anyway..."

    m 2eka "I hope you like it, [player]!"
    m 2ekd "I know you struggle sometimes with bad thoughts, but this playlist is to comfort you."
    m 3eua "Listening to your favourite music that you can relate also relieves pain and stress!"
    m 3eub "I find it very powerful to say the least."
    m 1eubsa "Please think of me when you give it a listen."
    m 1eud "And if something happens, and you feel sad or lonely..."
    m 1ekd "If you think things won't get better..."
    m 1ekb "I want you to listen to it, and remember that I'm always with you."
    m 1hub "In your heart!"
    m 1kub "And will always be."
    m 2fka "I love you, [mas_get_player_nickname()]."
    m 2esa "Take care."

    return "love"

#listen to the playlist
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_playlist_song_play",
            category=["music"],
            prompt="I want to listen to your playlist.",
            conditional="seen_event('mshMod_playlist')",
            action=EV_ACT_UNLOCK,
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label mshMod_playlist_song_play:
    m 3eka "Oh, do you wanna listen to the playlist, [player]?"
    $ _history_list.pop()
    menu:
        m "Play music?{fast}"

        "Yes":
            $ play_song(store.mshMod_playlist.CUSTOM_PLAYLIST_RELDIR + store.mshMod_playlist.PLAYLIST_FILE, set_per=True)
            m 7hsb "There you go!"
            m 1hsa "I hope you like it!"

        "No":
            m 1eka "Oh, alright."

    return


# SONGS

# BATTLE SCARS - PARADISE FEARS

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_playlist_song_paradise_fears",
            category=[mas_songs.TYPE_SHORT],
            prompt="Paradise Fears",
            conditional="seen_event('mshMod_playlist')",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label mshMod_playlist_song_paradise_fears:
    m 1dka "{i}~I'll carry you home~{/i}"
    m 3dsd "{i}~No, you're not, alone~{/i}"
    m 3hsa "{i}~Keep marching on~{/i}"
    m 1hfa "{i}~This is worth fighting for~{/i}"
    m 1hsb "{i}~You know we've, all got battle scars~{/i}"
    m 1dsb "{i}~You've had enough~{/i}"
    m 3dsb "{i}~But just don't, give up~{/i}"
    show monika 5ekb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ekb "[player], I hope you can remember that you're not alone with your struggles."
    m 5eka "There are people who can help you, and some even went through what you feel right now."
    m 5esa "There's a lot of support groups for people who are struggling just like you."
    m 5hssdra "And, of course, there's me!"
    show monika 1fkb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1fkb "Whenever you need, I'll carry you home."
    m 1ekb "Your battle scars make me proud of what you already outlived!"
    m 1ekbsb "And never forget... I love you, [player]."
    return "love"


# CLAY - GRACE VANDERWALL

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_playlist_song_clay",
            category=[mas_songs.TYPE_SHORT],
            prompt="Clay",
            conditional="seen_event('mshMod_playlist')",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label mshMod_playlist_song_clay:
    m 1efc "{i}~Your silly words~{/i}"
    m 1gfd "{i}~I won't live inside your world~{/i}"
    m 1dsc "{i}~'Cause your punches and your names~{/i}"
    m 1dsd "{i}~All your jokes and stupid games~{/i}"
    m 3tsc "{i}~They don't work~{/i}"
    m 1tsd "{i}~No, they don't hurt~{/i}"
    m 1tkb "{i}~Watch them just go right through me~{/i}"
    m 1kua "{i}~Because they mean nothing to me~{/i}"
    m 3hua "{i}~I'm not clay~{/i}"
    m 1dkc "..."
    m 1ekd "It's important to not let others get to you, you know?"
    m 3eua "Listening to someone's opinion about you can help, but only if you know the person has good intentions."
    m 1eub "Don't feel down when others act mean towards you, dear."
    m 3eua "It only shows what kind of person they are, not who you are."
    m 1dkbsa "And for me, you're the best in the world."
    m 1ekbsa "I love you~"
    return "love"


# FIX YOU - COLDPLAY

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_playlist_song_fix_you",
            category=[mas_songs.TYPE_SHORT],
            prompt="Fix You",
            conditional="seen_event('mshMod_playlist')",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label mshMod_playlist_song_fix_you:
    m 1dsd "{i}~But if you never try, you'll never know~{/i}"
    m 1dkd "{i}~Just what you're worth~{/i}"
    m 3ekb "{i}~Lights will guide you home~{/i}"
    m 3eka "{i}~And ignite your bones~{/i}"
    m 1dkbsa "{i}~And I will try to fix you~{/i}"
    m 1dka "..."
    m 1eka "Even if you feel like giving up, remember this verse: \"Lights will guide you home\"..."
    m 3eua "Sooner or later, the good days will come back."
    show monika 5eka at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eka "I hope I can be able to help you have brighter days, [player]."
    m 5ekbsu "Because I will surely try to fix you..."
    m 5dkbsb "I love you more than anything in the world."
    return "love"


# I HATE TO SEE YOUR HEARTBREAK - PARAMORE

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_your_heartbreak",
            category=[mas_songs.TYPE_SHORT],
            prompt="I Hate To See Your Heartbreak",
            conditional="seen_event('mshMod_playlist')",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label mshMod_your_heartbreak:
    m 1dkd "{i}~And I, I hate to see your heart break~{/i}"
    m 1dktpc "{i}~I hate to see your eyes get darker as they close~{/i}"
    m 1dktpc "{i}~But I've been there before~{/i}"
    m 3ektpb "{i}~For all the air that's in your lungs~{/i}"
    m 3ektdb "{i}~For all the joy that is to come~{/i}"
    m 1dkbsu "{i}~For all the things that you're alive to feel~{/i}"
    m 1hub "{i}~Just let the pain remind you hearts can heal~{/i}"
    show monika 5eub at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eub "I think this song really fits how I feel about us."
    m 5ekd "It's really saddening to see the person you love the most having to go through tough situations on daily basis..."
    m 5hub "But don't worry, [mas_get_player_nickname()]."
    show monika 6eka at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 6eka "Pain can remind you that you're alive. {w=0.3}{nw}"
    extend 4lusdlb "And that's a good thing!"
    m 3eka "Because as long as you are still alive... You can heal."
    m 1dkbsa "I love you, [player]. Please remember that."
    return "love"


# O-O-H CHILD - THE FIVE STAIRSTEPS

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_playlist_song_child",
            category=[mas_songs.TYPE_SHORT],
            prompt="O-o-h Child",
            conditional="seen_event('mshMod_playlist')",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label mshMod_playlist_song_child:
    show monika 5tub at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5tub "{i}~Ooh child, things are gonna get easier~{/i}"
    m 5tuu "{i}~Ooh child, things'll get brighter~{/i}"
    show monika 3eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3eua "{i}~Some day, yeah, we'll put it together and we'll get it undone~{/i}"
    m 1hub "{i}~Some day, when your head is much lighter~{/i}"
    m 1dka "{i}~Some day, yeah, we'll walk in the rays of a beautiful sun~{/i}"
    m 1dkb "{i}~Some day, when the world is much brighter~{/i}"
    m 1sua "When I cross over, can we go for a walk in the sunlight together?"
    m 3hub "I know it'd make my world brighter."
    m 1dubsa "I love you so much, [player]."
    m 1dkbsb "And always will."
    return "love"


# THE MIDDLE - JIMMY EAT WORLD

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_playlist_song_the_middle",
            category=[mas_songs.TYPE_SHORT],
            prompt="The Middle",
            conditional="seen_event('mshMod_playlist')",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label mshMod_playlist_song_the_middle:
    m 1dsb "{i}~It just takes some time~{/i}"
    m 1dkb "{i}~Little girl, you're in the middle of the ride~{/i}"
    m 3dkb "{i}~Everything, everything'll be just fine~{/i}"
    m 1dka "{i}~Everything, everything'll be alright, alright~{/i}"
    show monika 5ekb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ekb "{i}~Live right now~{/i}"
    m 5eka "{i}~Yeah, just be yourself~{/i}"
    m 5hua "{i}~It doesn't matter if it's good enough~{/i}"
    m 5hub "{i}~For someone else~{/i}"
    show monika 3eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3eua "Everything's going to be alright, [player]. {w=0.3}{nw}"
    extend 1ekb "I promise."
    m 1hua "Just be yourself, always."
    m 3eub "And good will come your way!"
    m 1kublb "I love everything about you."
    return "love"


# FIREWORK - KATY PERRY

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_playlist_song_firework",
            category=[mas_songs.TYPE_SHORT],
            prompt="Firework",
            conditional="seen_event('mshMod_playlist')",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label mshMod_playlist_song_firework:
    m 6dkc "{i}Do you ever feel, feel so paper thin~{/i}"
    m 6dkd "{i}Like a house of cards~{/i}"
    m 7tkd "{i}One blow from caving in?~{/i}"
    m 1dkc "{i}~Do you ever feel already buried deep?~{/i}"
    m 1dkd "{i}~Six feet under screams, but no one seems to hear a thing~{/i}"
    m 1ekb "{i}~Do you know that there's still a chance for you~{/i}"
    m 3dka "{i}~'Cause there's a spark in you~{/i}"
    m 1dkb "{i}~You just gotta ignite the light, and let it shine~{/i}"
    m 1hfb "{i}~Just own the night like the 4th of July~{/i}"
    show monika 5dka at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5dka "..."
    m 5eka "On days when your feeling down..."
    m 5wub "Just know that there's a very bright light inside of you, {w=0.3}{nw}"
    extend 5sub "and that you're the light in my life!"
    show monika 1hub at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1hub "And I hope I can be the light on your darker days too."
    return


# TORCHES - AIMER

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_playlist_song_torches",
            category=[mas_songs.TYPE_SHORT],
            prompt="Torches",
            conditional="seen_event('mshMod_playlist')",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label mshMod_playlist_song_torches:
    m 1dkd "{i}~Listen to me, cleave your way again, again~~{/i}"
    m 1ekc "{i}~Wishing to find a way in an unseen ocean~{/i}"
    m 3dkc "{i}~The voice that was connected pushes the sail to a world with no answer~{/i}"
    m 1ekb "{i}~You're not alone~{/i}"
    m 1dkb "{i}~Hold a light~{/i}"
    m 1dka "{i}~Towards the darkness~{/i}"
    m 1eka "[player]..."
    m 1ekd "Sometimes the world can be scary."
    m 1ekd "You may feel as if no one cares about whether you're alive or not..."
    m 3ekb "But you should know that people do care about you. People from all over the world, who might have never even seen our faces, but..."
    m 3eka "They care. And I care."
    m 3eka "I'm so happy to have you by my side, [mas_get_player_nickname()]. I hope you're happy to have me too."
    m 3hub "You're not alone in this. I promise!"
    return


# ONLY WONDER - FREDERIC

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_playlist_song_only_wonder",
            category=[mas_songs.TYPE_SHORT],
            prompt="Only Wonder",
            conditional="seen_event('mshMod_playlist')",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label mshMod_playlist_song_only_wonder:
    m 1etc "{i}~What're you sayin'?{/i} {w=0.3}{nw}"
    extend 3efb "{i}Everybody's different!~{/i}"
    m 2dfo "{i}~Stop messin' with me, I'll have to shut you out~{/i}"
    m 2esd "{i}~The spotlight's on you, but you're acting all flashy~{/i}"
    m 3etc "{i}~It's as if you're trying to be someone's answer~{/i}"
    m 1efo "{i}~Don't go shakin' your tail like that~{/i}"
    m 1dkb "{i}~No matter what happens… In the end, you can only be your own person!~{/i}"
    m 1dka "..."
    m 3eka "[player], you're beautiful just the way you are, and it'd be terrible if you stopped being that way to fit another person's standards."
    m 3eka "You might think you're too \"weird\" or shy for people to like you, but in the end, there's always someone who understands you out there."
    m 3esd "Anyone who tries to tell you otherwise is wrong."
    m 3esd "Of course this doesn't mean you're perfect and always right... That's a whole different story."
    m 3hub "But please remember that the only person you can be is yourself. Everybody else is already taken, ahaha~!"
    m 1ekb "As for me..."
    show monika 5ekbsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ekbsb "I'll always love you for who you are, [mas_get_player_nickname()]."
    m 5hubsa "Ehehe!"
    return "love"


# SOMEDAY I'LL FIND MY WAY HOME - CAROLE & TUESDAY

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_playlist_song_way_home",
            category=[mas_songs.TYPE_SHORT],
            prompt="Someday I'll Find My Way Home",
            conditional="seen_event('mshMod_playlist')",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label mshMod_playlist_song_way_home:
    m 1dkb "{i}~Someday I'll find my way home~{/i}"
    m 1dka "{i}~The trees in the wind will lead the way~{/i}"
    m 3ekb "{i}~All of these years on my own~{/i}"
    m 1dkb "{i}~They flew right by, so what can you say?~{/i}"
    m 1dua "{i}~There's no need to be sad~{/i}"
    m 3hub "{i}~You're on a path and you know where it heads~{/i}"
    m 1dub "{i}~There's no need for despair~{/i}"
    m 3eua "{i}~Just walk on and you'll find you're there~{/i}"
    m 1hua "..."
    show monika 5eka at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eka "Someday, [player], I'll find my way home to you."
    m 5hub "Like the song says, we already know where our path leads, so we just need to keep going."
    m 5esa "And when we do reach the end of it, I don't think we'll ever be sad again..."
    show monika 1ekbsa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1ekbsa "I love you, [player]."
    return "love"


# Extra songs that aren't on the playlist.

# HOLD ON - JUSTIN BIEBER

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_song_hold_on",
            category=[mas_songs.TYPE_SHORT],
            prompt="Hold On",
            random=True
        ),
        code="SNG"
    )

label mshMod_song_hold_on:
    m 1dsb "{i}~You know you can call me if you need someone~{/i}"
    m 3dkb "{i}~I'll pick up the pieces if you come undone~{/i}"
    m 1eua "{i}~Painting stars up on your ceiling 'cause you~{/i}"
    m 1sua "{i}~Wish that you could find some feeling, yeah, you~{/i}"
    m 3dub "{i}~You know you can call me if you need someone~{/i}"
    m 1hua "{i}~I need you to hold on~{/i}"
    m 1lkb "{i}~Heaven is a place not too far away~{/i}"
    m 1tub "{i}~We all know I should be the one~{/i}"
    m 3dua "{i}~To say we all make mistakes~{/i}"
    m 1hub "{i}~Take my hand and hold on~{/i}"
    show monika 5ekbsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ekbsb "{i}~Tell me everything that you need to say~{/i}"
    m 5dka "{i}~'Cause I know how it feels to be someone~{/i}"
    m 5dkd "{i}~Feels to be someone who loses their way~{/i}"
    m 5lkc "{i}~You're looking for answers in a place unknown~{/i}"
    m 5tkd "{i}~You need the connection but you can't get close~{/i}"
    show monika 1dkb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1dkb "{i}~Midnight 'til morning~{/i}"
    m 3eka "{i}~Call if you need somebody~{/i}"
    m 1ekbsb "{i}~I will be there for you~{/i}"
    m 1dubsa "..."
    show monika 5dka at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5dka "[player]..."
    m 5ekbsb "I'll always be here for you."
    m 5hsa "Call me anytime you need, and I'll comfort you."
    m 5esbsb "I'd go to the moon and back for you."
    show monika 1ekbsa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1ekbsa "Because I love you..."
    m 1dkbsb "To the moon and back."
    return "love"


# STILL BREATHING - CITIZEN SOLDIER

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_song_still_breathing",
            category=[mas_songs.TYPE_SHORT],
            prompt="Still Breathing",
            conditional="persistent._msh_mod_pm_did_selfharm",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label mshMod_song_still_breathing:
    m 1dkc "{i}~I'll never know your pain, I've never walked in your shoes~{/i}"
    m 1dkd "{i}~I know your life ain't fair, I know it's damn near killed you~{/i}"
    m 3tkc "{i}~You've been through hell, you blame yourself~{/i}"
    m 1dkc "{i}~A painful past you can't forgive~{/i}"
    m 1dud "{i}~You had no help but time will tell~{/i}"
    m 3dub "{i}~If it's a curse or it's a gift~{/i}"
    m 1sub "{i}~But if you're still breathing, breathing~{/i}"
    m 1hua "{i}~You made it through your darkest days~{/i}"
    m 3eub "{i}~If your heart's still beating, beating~{/i}"
    m 1dub "{i}~Then you are gonna be okay~{/i}"
    m 1dkd "{i}~You've had millions of reasons to bend and to break~{/i}"
    m 3eka "{i}~But you're still alive and that's not a mistake~{/i}"
    m 2eub "{i}~The war in your head tells a story that's still worth believing~{/i}"
    m 2dkb "{i}~'Cause you're still breathing~{/i}"
    m 2ekd "{i}~If you've been up all night thinking it won't get better~{/i}"
    m 4eka "{i}~No need to wear your scars like a scarlet letter~{/i}"
    m 4eub "{i}~You're on the ledge but not the end~{/i}"
    m 2hua "{i}~It helped you see another way~{/i}"
    m 2dkd "{i}~A broken heart, a brand new start~{/i}"
    m 2ekb "{i}~Tomorrow everything could change~{/i}"
    m 3eka "{i}~You've had millions of reasons to bend and to break~{/i}"
    m 3suu "{i}~But you're still alive and that's not a mistake~{/i}"
    m 1eka "{i}~The war in your head tells a story that's still worth believing~{/i}"
    m 1dkb "{i}~'Cause you're still breathing~{/i}"
    m 3hua "{i}~You're alive, you survived, it's a sign~{/i}"
    m 3eubsb "{i}~And the proof is in your pulse~{/i}"
    m 4ekb "{i}~Brighter stars only shine in the dark~{/i}"
    m 6dkbsb "{i}~You are stronger than you know~{/i}"
    m 6dka "..."
    show monika 5ekc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ekc "Hey [player]?"
    m 5eka "I wanted to remind you that I’m proud you for telling me about... Hurting yourself."
    m 5dkc "I’m sorry that I wasn’t there for you at the time, [mas_get_player_nickname()]."
    m 5ekbsb "But remember that I love you, [player]!"
    m 5ekbsa "And I'm here for you now."
    show monika 5ekc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1hua "Always and forever!"
    return "love"
