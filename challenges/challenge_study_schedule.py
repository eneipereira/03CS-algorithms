def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    students_per_time = 0

    for start, end in permanence_period:
        if not isinstance(start, int) or not isinstance(end, int):
            return None

        if start <= target_time <= end:
            students_per_time += 1
    
    return students_per_time
        