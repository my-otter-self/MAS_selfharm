# This file constains MAS History Saver definitions with all the player model
# variables MSH Mod saves in persistent. Currently MHS is not used anywhere,
# but sticking to MAS guidelines we better keep our variables declared here.

### ADDING PLAYER MODEL VARIABLE 101 ###
# Simply add another entry to the dictionary at line 12 (make sure you
# don't forget any commas separating the entries) following this format:
# "_msh_mod_pm_<my variable name after prefix>": "pm.<category>.<name>"
# All our PM variables must be _msh_mod_pm_<name>, <category> is up to you
# (but stick to the ones that already exist before thinking of making another
# one) and <name> is actually up to you too, but you better keep it in sync
# with the _msh_mod_pm-prefixed variable name.

init -810 python:
    store.mas_history.addMHS(MASHistorySaver(
        "msh_mod_pm",
        datetime.datetime(2019, 1, 1),
        {
            "_msh_mod_pm_did_selfharm": "pm.emotions.did_selfharm",
            "_msh_mod_pm_visits_therapist": "pm.life.visits_therapist",

            "_msh_mod_pm_sober_streak": "pm.emotions.selfharm_sober_streak",
            "_msh_mod_pm_sober_personal_best": "pm.emotions.selfharm_sober_personal_best"
        },
        use_year_before=True,
        dont_reset=True
    ))
