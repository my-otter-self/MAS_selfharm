# Sober streak tracking API. Includes milestones, sober streak duration, personal best, etc.

# Instance of datetime.date representing initial day of sober streak.
default persistent._msh_mod_pm_sober_streak = None

# Tuple of (datetime.date, int) where first item is initial streak day and
# the second item is amount of days streak lasted for.
default persistent._msh_mod_pm_sober_personal_best = None


init 4 python in mshMod_sober_streak:

    import store
    import datetime

    ### ASSERTIONS ###

    def _assertOnStreak():
        """
        Assetion function for checking if player is currently on sober streak.

        NOTE:
            An internal function. Should not be used by other submods.

        THROWS:
            AssertionError if player is on sober streak.
        """

        if not isOnStreak():
            raise AssertionError("expected player to be on streak")

    def _assertNotOnStreak():
        """
        Assetion function for checking if player is currently not on sober
        streak.

        NOTE:
            An internal function. Should not be used by other submods.

        THROWS:
            AssertionError if player is not on sober streak.
        """

        if isOnStreak():
            raise AssertionError("expected player not to be on streak")

    def _assertHasPersonalBest():
        """
        Assetion function for checking if player has personal best in sober
        streak.

        NOTE:
            An internal function. Should not be used by other submods.

        THROWS:
            AssertionError if player is has no personal best set.
        """

        if not hasPersonalBest():
            raise AssertionError("personal best is not set")


    ### STREAK OPERATIONS ###

    def isOnStreak():
        """
        Checks if player is currently on sober streak.

        RETURNS:
            Boolean True if player is on sober streak, False otherwise.
        """

        return store.persistent._msh_mod_pm_sober_streak is not None

    def getStreakDuration():
        """
        Calculates amount of days since the first day of streak.

        NOTE: This function asserts player is on sober streak.

        RETURNS:
            Integer amount of days since initial sober streak date.
        """

        _assertOnStreak()

        return (datetime.date.today() - store.persistent._msh_mod_pm_sober_streak).days

    def beginStreak(begin=None):
        """
        Begins streak if player is not on it already.

        NOTE: This function asserts player is not on sober streak.

        IN:
            begin - date instance to begin streak with. If None,
                then date.today() is used (default.)
        """

        _assertNotOnStreak()

        store.persistent._msh_mod_pm_sober_streak = (begin or datetime.date.today())
        _rebuildMilestoneDates()
        _updateMilestoneEvents()

        # Show streak check event
        store.mas_showEVL("mshMod_sober_check", "EVE", unlock=True)

    def endStreak():
        """
        Ends streak if player is on it.

        NOTE: This function asserts player is on sober streak.
        """

        _assertOnStreak()

        # Update personal best if current streak is longer than the previous.
        if store.persistent._msh_mod_pm_sober_personal_best is not None:
            since, days = store.persistent._msh_mod_pm_sober_personal_best
            c_days = (datetime.date.today() - store.persistent._msh_mod_pm_sober_personal_best[0]).days
            if c_days > days:
                store.persistent._msh_mod_pm_sober_personal_best = (store.persistent._msh_mod_pm_sober_streak, c_days)
        else:
            store.persistent._msh_mod_pm_sober_personal_best = (store.persistent._msh_mod_pm_sober_streak, (datetime.date.today() - store.persistent._msh_mod_pm_sober_streak).days)

        # Reset streak initial date and rebuild the calendar and events.
        store.persistent._msh_mod_pm_sober_streak = None
        _rebuildMilestoneDates()
        _updateMilestoneEvents()

        # Hide streak check event
        store.mas_hideEVL("mshMod_sober_check", "EVE", lock=True)

    def hasPersonalBest():
        """
        Checks if player has personal best in sober streak.

        RETURNS:
            Boolean True if player has personal best set, False otherwise.
        """

        return store.persistent._msh_mod_pm_sober_personal_best is not None

    def resetPersonalBest():
        """
        Resets player's personal best in sober streak.

        NOTE: This function asserts player has personal best.
        """

        _assertHasPersonalBest()

        # NOTE: removing repeatable from calendar HERE and not in _updateMilestoneEvents
        # for sake of optimization; otherwise we'd have to perform a full scan.
        store.mas_calendar.removeRepeatable("milestone_personal_best", store.persistent._msh_mod_pm_sober_personal_best[0])

        store.persistent._msh_mod_pm_sober_personal_best = None
        _updateMilestoneEvents()


    ### MILESTONE DATE DEFINITION ###

    def _getEndDateTuple(date):
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

    def _getWeeklyMilestone(weeks, since=None):
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
            _assertOnStreak()
            since = store.persistent._msh_mod_pm_sober_streak

        return _getEndDateTuple(since + datetime.timedelta(days=weeks * 7))

    def _getMonthlyMilestone(months, since=None):
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
            _assertOnStreak()
            since = store.persistent._msh_mod_pm_sober_streak

        new_y, new_m = since.year, since.month + months
        new_y, new_m = new_y + new_m // 12, (new_m % 12) or 12

        new_d = since.day
        if since.day > 28 and new_m == 2:
            new_d = 29 if ((new_y % 4 == 0 and not new_y % 100 == 0) or new_y % 400 == 0) else 28
        elif since.day > 30 and new_m in (4, 6, 9, 11):
            new_d = 30

        return _getEndDateTuple(since.replace(year=new_y, month=new_m, day=new_d))

    def _getYearlyMilestone(years, since=None):
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
            _assertOnStreak()
            since = store.persistent._msh_mod_pm_sober_streak

        return _getEndDateTuple(since.replace(year=since.year+years))

    _milestoneDates = dict()
    def _rebuildMilestoneDates():
        """
        Rebuilds _milestoneDates dictionary based on current
        sober streak initial date (if on streak) or empties it.

        NOTE:
            An internal function. Should not be used by other submods.
        """

        if not isOnStreak():
            if _milestoneDates:
                _milestoneDates.clear()
        else:
            _milestoneDates.update({
            # Weeks
                "1w": _getWeeklyMilestone(1),
                "2w": _getWeeklyMilestone(2),
                "3w": _getWeeklyMilestone(3),

            # Months
                "1m": _getMonthlyMilestone(1),
                "3m": _getMonthlyMilestone(3),
                "6m": _getMonthlyMilestone(6),

            # Years
                "1y": _getYearlyMilestone(1),
                "2y": _getYearlyMilestone(2),
                "3y": _getYearlyMilestone(3),
                "4y": _getYearlyMilestone(4),
                "5y": _getYearlyMilestone(5)}
            )

    def _getPersonalBestDateTuple():
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

        _assertHasPersonalBest()

        since, days = store.persistent._msh_mod_pm_sober_personal_best
        start = since + datetime.timedelta(days=days)
        return start, start + datetime.timedelta(days=1)

    def _getMilestoneDateTuple(code):
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

        date = _milestoneDates.get(code)
        if date is not None:
            return _milestoneDates[code]
        raise KeyError("unknown milestone code " + code)

    def getMilestoneDate(code):
        """
        Produces a milestone date as datetime.date instance.

        IN:
            code - Milestone code (1w, 2w, 3w, etc) to get date for.

        RETURNS:
            datetime.date instance representing milestone date.

        RAISES:
            KeyError if the requested milestone does not exist.
        """

        return _getMilestoneDateTuple(code)[0]

    def isMilestoneToday(code):
        """
        Checks if the provided milestone is today.

        IN:
            code - Milestone code (1w, 2w, 3w, etc) to check milestone of.

        RETURNS:
            Boolean True if the requested milestone is today, False otherwise.
        """

        return getMilestoneDate(code) == datetime.date.today()

    def isMilestonePast(code):
        """
        Checks if the provided milestone is in past.

        IN:
            code - Milestone code (1w, 2w, 3w, etc) to check milestone of.

        RETURNS:
            Boolean True if the requested milestone is in past, False otherwise.
        """

        return getMilestoneDate(code) < datetime.date.today()

    def getTodayMilestone():
        """
        Finds and returns (if found) milestone that is today.

        RETURNS:
            Today's milestone code as string or None if not found.
        """

        for code in _milestoneDates.keys():
            if isMilestoneToday(code):
                return code
        return None

    def getPastMilestones():
        """
        Finds milestones that are in past.

        NOTE:
            Today's milestone is not included.

        RETURNS:
            List of past milestone codes as strings.
        """

        milestones = list()

        for code in _milestoneDates.keys():
            if isMilestonePast(code):
                milestones.append(code)

        return milestones


    ### EVENT MANAGEMENT ###

    _milestoneEvents = (dict(), dict())
    def addMilestoneEvent(event, milestone):
        """
        Calls addEvent and binds milestone code to the event.

        NOTE:
            This function should be invoked in init 5.

        IN:
            event - Event object to call addEvent on.
            code - Milestone code (1w, 2w, 3w, etc) to bind milestone of.
        """

        by_label, by_code = _milestoneEvents
        data = (event, milestone)
        by_label[event.eventlabel] = data
        by_code[milestone] = data

        store.addEvent(event)

    def _getMilestoneEvent(code):
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

        ev = _milestoneEvents[1].get(code)
        if ev is not None:
            return ev
        raise KeyError("unknown milestone " + code)

    def _updateMilestoneEvents():
        """
        Updates milestone/personal best Event operations in order to
        render/hide them on calendar depending on current streak length,
        streak status and personal best status.

        NOTE:
            An internal function. Should not be used by other submods.
        """

        if isOnStreak():
            for milestone in getPastMilestones():
                ev, data = _getMilestoneEvent(milestone)

                # Remove it from calendar if it's present.
                store.mas_calendar.removeEvent(ev)

                # Past events must have start and end date in order
                # to display on calendar.
                ev.start_date, ev.end_date = _getMilestoneDateTuple(milestone)
                store.mas_calendar.addEvent(ev)

                # Random and unlock this event so it can be repeated through the menu.
                ev.random, ev.unlocked = False, True

                # Also mark it seen for Ren'Py/MAS.
                _seeLabel(ev.eventlabel)

            # Add today's milestone to calendar if possible.
            milestone = getTodayMilestone()
            if milestone is not None:
                ev, data = _getMilestoneEvent(milestone)

                ev.start_date, ev.end_date = _getMilestoneDateTuple(milestone)

                store.mas_calendar.addEvent(ev)
                if not store.renpy.seen_label(ev.eventlabel) or (ev.last_seen or datetime.datetime.min).date() < datetime.date.today():
                    # Set QUEUE action to this event so that it is always queued, regardless of random chatter.
                    # Only do it if it wasn't seen or wasn't last seen today.
                    ev.action = store.EV_ACT_QUEUE
        else:
            for label, data in _milestoneEvents[0].items():
                ev = data[0]

                # Remove these events from the calendar.
                store.mas_calendar.removeEvent(ev)

                # Since we're not on streak, these events should never trigger.
                ev.start_date, ev.end_date = None, None
                ev.random, ev.unlocked = False, False

                # Also unsee it for Ren'Py/MAS
                _unseeLabel(ev.eventlabel)

        if store.persistent._msh_mod_pm_sober_personal_best is not None:
            since, days = store.persistent._msh_mod_pm_sober_personal_best

            store.mas_calendar.removeRepeatable("milestone_personal_best", since)

            start_date, end_date = _getPersonalBestDateTuple()
            store.mas_calendar.addRepeatable_dt(
                "milestone_personal_best", _("Sober streak, personal best"),
                datetime.datetime.combine(start_date.today(), datetime.datetime.min.time()),
                year_param=[start_date.year]
            )

    def unlockMilestone():
        ev = store.mas_submod_utils.this_ev
        ev.random, ev.unlocked = True, True


    ### UTILITIES ###

    def _seeLabel(label):
        """
        Marks the provided label as seen for Ren'Py and MAS.

        NOTE:
            An internal function. Should not be used by other submods.

        IN:
            label - Ren'Py label to mark seen.
        """

        store.persistent._seen_ever[label] = True

    def _unseeLabel(label):
        """
        Marks the provided label as unseen for Ren'Py and MAS.

        NOTE:
            An internal function. Should not be used by other submods.

        IN:
            label - Ren'Py label to mark unseen.
        """

        if label in store.persistent._seen_ever:
            del store.persistent._seen_ever[label]


init 7 python in mshMod_sober_streak:

    ### EVENT PROPERTIES UNLOCK ###

    by_label, by_code = _milestoneEvents
    for code, data in by_code.items():
        ev = store.mas_getEV(data[0].eventlabel)
        store.mshMod_utils.unlockAllEventProps(ev)

        # Keep a reference to event object saved in events list.
        data_pair = (ev, data[1])
        by_label[ev.eventlabel] = data_pair
        by_code[code] = data_pair


    ### DAILY MILESTONES REBUILD/UPDATE ###

    def _dailyMilestoneUpdate():
        _rebuildMilestoneDates()
        _updateMilestoneEvents()

    store.mas_submod_utils.registerFunction("ch30_day", _dailyMilestoneUpdate)


    ### INITIAL APPLICATION OF MILESTONE EVENTS ###

    _dailyMilestoneUpdate()
