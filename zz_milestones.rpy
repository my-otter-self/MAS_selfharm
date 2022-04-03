# This file contains milestone API/Framework. Hopefully everything here is at
# least readable and processable by whoever reads this. Feel free to modify,
# but please stick to the overall code style used in here.


# Instance of datetime.date representing initial day of sober streak.
default persistent._msh_mod_pm_sober_streak = None

# Tuple of (datetime.date, int) where first item is initial streak day and
# the second item is amount of days streak lasted for.
default persistent._msh_mod_pm_sober_personal_best = None


init 4 python:

    ### ASSERTIONS ###

    def _mshMod_assertOnStreak():
        """
        Assetion function for checking if player is currently on sober streak.

        NOTE:
            An internal function. Should not be used by other submods.

        THROWS:
            AssertionError if player is on sober streak.
        """

        if not mshMod_isOnStreak():
            raise AssertionError("expected player to be on streak")

    def _mshMod_assertNotOnStreak():
        """
        Assetion function for checking if player is currently not on sober
        streak.

        NOTE:
            An internal function. Should not be used by other submods.

        THROWS:
            AssertionError if player is not on sober streak.
        """

        if mshMod_isOnStreak():
            raise AssertionError("expected player not to be on streak")

    def _mshMod_assertHasPersonalBest():
        """
        Assetion function for checking if player has personal best in sober
        streak.

        NOTE:
            An internal function. Should not be used by other submods.

        THROWS:
            AssertionError if player is has no personal best set.
        """

        if not mshMod_hasPersonalBest():
            raise AssertionError("personal best is not set")


    ### STREAK OPERATIONS ###

    def mshMod_isOnStreak():
        """
        Checks if player is currently on sober streak.

        RETURNS:
            Boolean True if player is on sober streak, False otherwise.
        """

        return persistent._msh_mod_pm_sober_streak is not None

    def mshMod_getStreakDuration():
        """
        Calculates amount of days since the first day of streak.

        NOTE: This function asserts player is on sober streak.

        RETURNS:
            Integer amount of days since initial sober streak date.
        """

        _mshMod_assertOnStreak()

        return (datetime.date.today() - persistent._msh_mod_pm_sober_streak).days

    def mshMod_beginStreak():
        """
        Begins streak if player is not on it already.

        NOTE: This function asserts player is not on sober streak.
        """

        _mshMod_assertNotOnStreak()

        persistent._msh_mod_pm_sober_streak = datetime.date.today()
        _mshMod_rebuildMilestoneDates()

    def mshMod_endStreak():
        """
        Ends streak if player is on it.

        NOTE: This function asserts player is on sober streak.
        """

        _mshMod_assertOnStreak()

        # Update personal best if current streak is longer than the previous.
        if persistent._msh_mod_pm_sober_personal_best is not None:
            since, days = persistent._msh_mod_pm_sober_personal_best
            c_days = (datetime.date.today() - persistent._msh_mod_pm_sober_personal_best[0]).days
            if c_days > days:
                persistent._msh_mod_pm_sober_personal_best = (persistent._msh_mod_pm_sober_streak, c_days)
        else:
            persistent._msh_mod_pm_sober_personal_best = (persistent._msh_mod_pm_sober_streak, (datetime.date.today() - persistent._msh_mod_pm_sober_streak).days)

        # Reset streak initial date and rebuild the calendar and events.
        persistent._msh_mod_pm_sober_streak = None
        _mshMod_rebuildMilestoneDates()
        _mshMod_updateMilestoneEvents()

    def mshMod_hasPersonalBest():
        """
        Checks if player has personal best in sober streak.

        RETURNS:
            Boolean True if player has personal best set, False otherwise.
        """

        return persistent._msh_mod_pm_sober_personal_best is not None

    def mshMod_resetPersonalBest():
        """
        Resets player's personal best in sober streak.

        NOTE: This function asserts player has personal best.
        """

        _mshMod_assertHasPersonalBest()

        persistent._msh_mod_pm_sober_personal_best = None
        _mshMod_updateMilestoneEvents()


    ### MILESTONE DATE DEFINITION ###

    def _mshMod_getEndDateTuple(date):
        """
        Produces (datetime.date, datetime.date) tuple of the provided date
        and the date one day ahead of it.

        NOTE:
            An internal function. Should not be used by other submods.

        IN:
            date - datetime.date instance to produce end date tuple for.

        RETURNS:
            Tuple (datetime.date, datetime.date) with the provided date
            and the end date for it.
        """

        return (date, date + datetime.timedelta(days=1))

    def _mshMod_getWeeklyMilestone(weeks, since=None):
        """
        Produces properly computed weekly milestone for the given amount of
        weeks since the provided date or (by default) player's sober streak
        initial date.

        NOTE:
            An internal function. Should not be used by other submods. Also
            asserts player is on sober streak.

        IN:
            weeks - integer amount of weeks for the milestone.
            since - datetime.date instance to start counting from.

        RETURNS:
            datetime.date of the requested amount weeks milestone.

        RAISES:
            ValueError if weeks is less than zero.
        """

        if weeks < 0:
            raise ValueError("weeks cannot be less than 0")

        if since is None:
            _mshMod_assertOnStreak()
            since = persistent._msh_mod_pm_sober_streak

        return _mshMod_getEndDateTuple(since + datetime.timedelta(days=weeks * 7))

    def _mshMod_getMonthlyMilestone(months, since=None):
        """
        Produces properly computed monthly milestone for the given amount of
        months since the provided date or (by default) player's sober streak
        initial date.

        NOTE:
            An internal function. Should not be used by other submods. Also
            asserts player is on sober streak.

        IN:
            years - integer amount of months for the milestone.
            since - datetime.date instance to start counting from.

        RETURNS:
            datetime.date of the requested amount months milestone.

        RAISES:
            ValueError if months is less than zero.
        """

        if months < 0:
            raise ValueError("months cannot be less than 0")

        if since is None:
            _mshMod_assertOnStreak()
            since = persistent._msh_mod_pm_sober_streak

        new_y, new_m = since.year, since.month + months
        new_y, new_m = new_y + new_m // 12, new_m % 12

        new_d = since.day
        if since.day > 28 and new_m == 2:
            new_d = 29 if ((new_y % 4 == 0 and not new_y % 100 == 0) or new_y % 400 == 0) else 28
        elif since.day > 30 and new_m in (4, 6, 9, 11):
            new_d = 30

        return _mshMod_getEndDateTuple(since.replace(year=new_y, month=new_m, day=new_d))

    def _mshMod_getYearlyMilestone(years, since=None):
        """
        Produces properly computed yearly milestone for the given amount of
        years since the provided date or (by default) player's sober streak
        initial date.

        NOTE:
            An internal function. Should not be used by other submods. Also
            asserts player is on sober streak.

        IN:
            years - integer amount of months for the milestone.
            since - datetime.date instance to start counting from.

        RETURNS:
            datetime.date of the requested amount months milestone.

        RAISES:
            ValueError if years is less than zero.
        """

        if years < 0:
            raise ValueError("years cannot be less than 0")

        if since is None:
            _mshMod_assertOnStreak()
            since = persistent._msh_mod_pm_sober_streak

        return _mshMod_getEndDateTuple(since.replace(year=since.year+years))

    _mshMod_milestoneDates = dict()
    def _mshMod_rebuildMilestoneDates():
        """
        Rebuilds _mshMod_milestoneDates dictionary based on current
        sober streak initial date (if on streak) or empties it.

        NOTE:
            An internal function. Should not be used by other submods.
        """

        if not mshMod_isOnStreak():
            if _mshMod_milestoneDates:
                _mshMod_milestoneDates.clear()
        else:
            _mshMod_milestoneDates.update({
            # Weeks
                "1w": _mshMod_getWeeklyMilestone(1),
                "2w": _mshMod_getWeeklyMilestone(2),
                "3w": _mshMod_getWeeklyMilestone(3),

            # Months
                "1m": _mshMod_getMonthlyMilestone(1),
                "3m": _mshMod_getMonthlyMilestone(3),
                "6m": _mshMod_getMonthlyMilestone(6),

            # Years
                "1y": _mshMod_getYearlyMilestone(1),
                "2y": _mshMod_getYearlyMilestone(2),
                "3y": _mshMod_getYearlyMilestone(3),
                "4y": _mshMod_getYearlyMilestone(4),
                "5y": _mshMod_getYearlyMilestone(5)}
            )

    def _mshMod_getPersonalBestDateTuple():
        """
        Produces a convenient (datetime.date, datetime.date) tuple for use
        in attribute modification of personal best Event.

        NOTE:
            An internal function. Should not be used by other submods. Also
            asserts that player has personal best set.

        RETURNS:
            Tuple (datetime.date, datetime.date) where first item is Event
            start date, and the second item is Event end date.
        """

        _mshMod_assertHasPersonalBest()

        since, days = persistent._msh_mod_pm_sober_personal_best
        start = since + datetime.timedelta(days=days)
        return start, start + datetime.timedelta(days=1)

    def _mshMod_getMilestoneDateTuple(code):
        """
        Produces a convenient (datetime.date, datetime.date) tuple for use
        in attribute modification of milestone Event.

        NOTE:
            An internal function. Should not be used by other submods.

        IN:
            code - Milestone code (1w, 2w, 3w, etc) to get date tuple for.

        RETURNS:
            Tuple (datetime.date, datetime.date) where first item is Event
            start date, and the second item is Event end date.

        RAISES:
            KeyError if the requested milestone does not exist.
        """

        date = _mshMod_milestoneDates.get(code)
        if date is not None:
            return _mshMod_milestoneDates[code]
        raise KeyError("unknown milestone code " + code)

    def mshMod_getMilestoneDate(code):
        """
        Produces a milestone date as datetime.date instance.

        IN:
            code - Milestone code (1w, 2w, 3w, etc) to get date for.

        RETURNS:
            datetime.date instance representing milestone date.

        RAISES:
            KeyError if the requested milestone does not exist.
        """

        return _mshMod_getMilestoneDateTuple(code)[0]

    def mshMod_isMilestoneToday(code):
        """
        Checks if the provided milestone is today.

        IN:
            code - Milestone code (1w, 2w, 3w, etc) to check milestone of.

        RETURNS:
            Boolean True if the requested milestone is today, False otherwise.
        """

        return mshMod_getMilestoneDate(code) == datetime.date.today()

    def mshMod_isMilestonePast(code):
        """
        Checks if the provided milestone is in past.

        IN:
            code - Milestone code (1w, 2w, 3w, etc) to check milestone of.

        RETURNS:
            Boolean True if the requested milestone is in past, False otherwise.
        """

        return mshMod_getMilestoneDate(code) < datetime.date.today()

    def mshMod_getTodayMilestone():
        """
        Finds and returns (if found) milestone that is today.

        RETURNS:
            Today's milestone code as string or None if not found.
        """

        for code in _mshMod_milestoneDates.keys():
            if mshMod_isMilestoneToday(code):
                return code
        return None

    def mshMod_getPastMilestones():
        """
        Finds milestones that are in past.

        NOTE:
            Today's milestone is not included.

        RETURNS:
            List of past milestone codes as strings.
        """

        milestones = list()

        for code in _mshMod_milestoneDates.keys():
            if mshMod_isMilestonePast(code):
                milestones.append(code)

        return milestones


    ### EVENT MANAGEMENT ###

    _mshMod_eventProperties = (
        "eventlabel", "prompt", "label", "category", "unlocked",
        "random", "pool", "conditional", "action", "start_date",
        "end_date", "unlock_date", "shown_count", "last_seen",
        "years", "sensitive", "aff_range", "show_in_idle", "flags"
    )

    _mshMod_milestoneEvents = (dict(), dict())
    def mshMod_addMilestoneEvent(event, milestone):
        """
        Calls addEvent and binds milestone code to the event.

        NOTE:
            This function should be invoked in init 5.

        IN:
            event - Event object to call addEvent on.
            code - Milestone code (1w, 2w, 3w, etc) to bind milestone of.
        """

        by_label, by_code = _mshMod_milestoneEvents
        data = (event, milestone)
        by_label[event.eventlabel] = data
        by_code[milestone] = data

        addEvent(event)

    def _mshMod_getMilestoneEvent(code):
        """
        Returns milestone's bound Event object.

        NOTE:
            An internal function. Should not be used by other submods.

        IN:
            code - Milestone code (1w, 2w, 3w, etc) to get event of.

        RETURNS:
            Event object bound to the milestone wit the provided code.

        RAISES:
            KeyError if there is no such milestone code.
        """

        ev = _mshMod_milestoneEvents[1].get(code)
        if ev is not None:
            return ev
        raise KeyError("unknown milestone " + code)

    def _mshMod_updateMilestoneEvents():
        """
        Updates milestone/personal best Event operations in order to
        render/hide them on calendar depending on current streak length,
        streak status and personal best status.

        NOTE:
            An internal function. Should not be used by other submods.
        """

        if mshMod_isOnStreak():
            for milestone in mshMod_getPastMilestones():
                ev, _ = _mshMod_getMilestoneEvent(milestone)

                # Past events must have start and end date in order
                # to display on calendar.
                ev.start_date, ev.end_date = _mshMod_getMilestoneDateTuple(milestone)
                store.mas_calendar.addEvent(ev)

                # Derandom and unlock this event so it can be repeated through the menu.
                ev.random, ev.unlocked = False, True
                ev.unlock_date, ev.last_seen = None, None

                # Also mark it seen for Ren'Py/MAS.
                _mshMod_seeLabel(ev.eventlabel)

            # Add today's milestone to calendar if possible.
            milestone = mshMod_getTodayMilestone()
            if milestone is not None:
                ev, _ = _mshMod_getMilestoneEvent(milestone)

                ev.start_date, ev.end_date = _mshMod_getMilestoneDateTuple(milestone)

                store.mas_calendar.addEvent(ev)
                if not mas_seenLabels([ev.eventlabel]):
                    ev.random, ev.unlocked = True, False
                    ev.unlock_date, ev.last_seen = None, None
        else:
            for label, data in _mshMod_milestoneEvents[0].items():
                ev = data[0]

                # Remove these events from the calendar.
                store.mas_calendar.removeEvent(ev)

                # Since we're not on streak, these events should never trigger.
                ev.start_date, ev.end_date = None, None
                ev.random, ev.unlocked = False, False

        if persistent._msh_mod_pm_sober_personal_best is not None:
            since, days = persistent._msh_mod_pm_sober_personal_best

            ev = _mshMod_personalBestEvent
            store.mas_calendar.removeEvent(ev)

            ev.start_date, ev.end_date = _mshMod_getPersonalBestDateTuple()
            store.mas_calendar.addEvent(ev)
        else:
            store.mas_calendar.removeEvent(_mshMod_personalBestEvent)


    ### UTILITIES ###

    def _mshMod_seeLabel(label):
        """
        Marks the provided label as seen for Ren'Py and MAS.

        NOTE:
            An internal function. Should not be used by other submods.

        IN:
            label - Ren'Py label to mark seen.
        """

        persistent._seen_ever[label] = True

    def _mshMod_unseeLabel(label):
        """
        Marks the provided label as unseen for Ren'Py and MAS.

        NOTE:
            An internal function. Should not be used by other submods.

        IN:
            label - Ren'Py label to mark unseen.
        """

        if label in persistent._ever_seen:
            del persistent._seen_ever[label]


init 7 python:

    ### MILESTONE EVENT PROPERTIES UNLOCK ###

    _mshMod_lockedProps = (
        "unlocked", "random", "pool", "conditional",
        "action", "start_date", "end_date", "unlock_date",
        "shown_count", "last_seen"
    )

    def _mshMod_unlockAllEventProps(ev):
        """
        Forcibly unlock all attributes of Event. Required for modification
        of start_date/end_date and almost every other attribute.

        NOTE:
            An internal function. Should not be used by other submods.

        IN:
            ev - Event label to unlock attributes of.
        """

        for prop in _mshMod_lockedProps:
            Event.unlockInit(prop, ev=ev)


    by_label, by_code = _mshMod_milestoneEvents
    for code, data in by_code.items():
        ev = mas_getEV(data[0].eventlabel)
        _mshMod_unlockAllEventProps(ev)

        # Keep a reference to event object saved in events list.
        data_pair = (ev, data[1])
        by_label[ev.eventlabel] = data_pair
        by_code[code] = data_pair

    # Make personal best event modifiable.
    _mshMod_personalBestEvent = mas_getEV(_mshMod_personalBestEventLabel)
    _mshMod_unlockAllEventProps(_mshMod_personalBestEvent)


init 7 python:

    ### INITIAL APPLICATION OF MILESTONE EVENTS ###

    _mshMod_rebuildMilestoneDates()
    _mshMod_updateMilestoneEvents()


    ### DAILY MILESTONES REBUILD/UPDATE ###

    import time

    def _mshMod_dailyUpdaterThread():
        # HACK: Unless we find a better way to run the checker task
        # in the background, we could stick to *not so cheap* threads.
        # Ideally it would fit into MASDelayedActions, but alas...

        last_checked_day = datetime.date.today().day

        while True:
            time.sleep(5)

            day = datetime.date.today().day
            if last_checked_day != day:
                _mshMod_rebuildMilestoneDates()
                _mshMod_updateMilestoneEvents()

    renpy.invoke_in_thread(_mshMod_dailyUpdaterThread)


init 5 python:

    _mshMod_personalBestEventLabel = "mshMod_milestone_personal_best"
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_personal_best",
            prompt="Sober, personal best",
            conditional="False",
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_personal_best:
    # This exists just for sake of rendering of the personal best
    # event on the calendar. Do not touch this!
    return
