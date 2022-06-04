#
# MOD DATE WIPE SCRIPT
#
# Programmatically wipes mod-related data from persistent.
# Apply in case there is a need to wipe mod data from persistent in a safe way,
# without completely resetting the progress.
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

init python:
    P = persistent

    import re
    pattern = re.compile('msh(_m|M)od')
    match = lambda key: bool(pattern.search(key))

    def clean_dict(_dict):
        if type(_dict) is not dict and hasattr(_dict, '__dict__'):
            _dict = _dict.__dict__
        for key in _dict.keys():
            if match(key):
                mas_utils.mas_log.debug('[CLEANUP] Removing key: {0!r}.'.format(key))
                del _dict[key]

    clean_dict(P)
    clean_dict(P._changed)
    clean_dict(P._mas_event_init_lockdb)

    for key in P._seen_ever.keys():
        if type(key) is tuple:
            del_key = key[0]
        else:
            del_key = key
        if match(del_key):
            mas_utils.mas_log.debug('[CLEANUP] Removing key: {0!r}.'.format(key))
            del P._seen_ever[del_key]

    for item in P._seen_translates:
        if match(item):
            mas_utils.mas_log.debug('[CLEANUP] Removing item: {0!r}.'.format(item))
            P._seen_translates.remove(item)

    clean_dict(P.event_database)

    for year in P._mas_history_archives.values():
        clean_dict(year)
