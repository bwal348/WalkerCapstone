def calculate_water_intake(weight_lbs: float, activity_level: int) -> float:
    """
    Calculates daily water needed for an individual, based on weight and activity level.
    :param weight_lbs: Weight in pounds
    :param activity_level: activity level (1 = low, 2 = moderate, 3 = high)
    :return: recommended water intake level
    """

    base_intake_oz = weight_lbs * 0.5

    activity_multipliers = {
        1: 1.0, # low activity
        2: 1.2, # moderate activity (3-4 times per week)
        3: 1.5 # high activity (5-7 times per week)
    }

    multiplier = activity_multipliers.get(activity_level, 1.2) # moderate activity will be the default

    #calculates the total water intake
    total_water_intake_oz = base_intake_oz * multiplier

    return round(total_water_intake_oz, 2)