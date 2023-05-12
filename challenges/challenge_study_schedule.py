def study_schedule(permanence_period, target_time):
    frequency = 0
    if target_time is None:
        return None

    for period in permanence_period:
        if not type(period[0]) == int or not type(period[1]) == int:
            return None
        if period[0] <= target_time <= period[1]:
            frequency += 1

    return frequency
