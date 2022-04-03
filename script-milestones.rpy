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
            prompt="Sober, 1 week",
            category=["self-harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_1w:
    m "1 week milestone test."
    # TODO: By the way, we might need to consider if we need milestones to
    # unlock or not. Do we need it though?
    return "derandom|unlock"
