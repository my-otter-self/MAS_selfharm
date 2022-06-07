label mas_self_harm_submod_team_mas_self_harm_submod_v1_0_5(version="v1_0_5"):
    ## Undo full unlock on events and only unlock start_date and end_date ##
    for ev_label in (ev_label for ev_label in mas_all_ev_db.keys() if ev_label.startswith("mshMod_sober_milestone_")):
        # Reset to template
        persistent._mas_event_init_lockdb[ev_label] = persistent._mas_event_init_lockdb_template

        # Unlock start_date and end_date
        Event.unlockInit("start_date", ev_label=ev_label)
        Event.unlockInit("end_date", ev_label=ev_label)
