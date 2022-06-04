#
# EMERGENCY FIX FOR BROKEN STREAK STATE
#
# Performs streak reset programmatically.
# Apply when streak state is broken and there is no way to normally reset it.
#
# How to apply:
#
#   1. Close the game if it's running
#   2. Drop into 'game' folder
#   3. Start the game
#   4. Say goodbye and exit
#   5. Delete this file and corresponding .rpyc file from 'game' folder
#   6. Start the game again
#

init 1000 python:
    store.mshMod_sober_streak.endStreak()
    store.mshMod_sober_streak.resetPersonalBest()

    mas_hideEVL("mshMod_sober_relapse", "EVE", lock=True)
    mas_hideEVL("mshMod_sober_check", "EVE", lock=True)
    mas_showEVL("mshMod_sober_promise", "EVE", unlock=True)
