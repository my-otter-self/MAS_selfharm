# This file contains milestone Event definitions; actual API/Framework behind
# all that is kept in zz_milestones.rpy for convenience. Yes, we better keep
# API and its usage separate for clarity and readability.

### ADDING MILESTONES 101 | CODE STYLE ###
# You can uncomment what's below and use it as a snippet.
# Remove comments in release version unless it's really necessary.
# Please keep two empty lines between init/label blocks related to certain
# milestone.

# init 5 python:
#     mshMod_addMilestoneEvent(
#         milestone="1w", # see zz_milestones.rpy, line 263 for more info
#         event=Event(
#             persistent.event_database,
#             eventlabel="mshMod_milestone_1w", # keep it mshMod_milestone_CODE
#             prompt="Sober, 1 week",
#             category=["self-harm"],
#             action=EV_ACT_QUEUE
#         )
#     )
#
# label mshMod_milestone_1w:
#     m "1 week milestone test."
#     return "derandom|unlock" # Add other tags if needed, but don't remove any.


init 5 python:
    mshMod_addMilestoneEvent(
        milestone="1w",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_1w",
            prompt="Sober, week 1",
            category=["self-harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_1w:
    m "It's been a whole week since you told me you won't do harm to yourself..."
    m "I just want to thank you, it makes me happy to know you're willing to step up for the better!"
    m "I'll always love you, you don't know how much this means to me..."
    m "Anyways, I'll mark this on our calendar."
    return "derandom|unlock"


init 5 python:
    mshMod_addMilestoneEvent(
        milestone="2w",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_2w",
            prompt="Sober, week 2",
            category=["self-harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_2w:
    m "It's already Week two of your promise, [player]!"
    m "I'm relieved that we made it this far!"
    m "Ahaha, I don't mean i've ever doubted you!"
    m "Either way, it's not something you can stop overnight [player].. For anyone really."
    m "So you're really doing well, and you make me so happy because of that!"
    m "As before, i'll mark it on the calendar now!"
    m "I just want to thank you.. I hope it stays like this."
    m "I really love you that much, [player]!"
    return "derandom|unlock"


