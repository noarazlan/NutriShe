from datetime import date

def calculate_age(date_of_birth : date):
    today = date.today()
    age = today.year - date_of_birth.year
    if(today.month, today.day) < (date_of_birth.month, date_of_birth.day):
        age -=1
    return age

def calculate_daily_calories(weight : float , height: float, date_of_birth : date, activity_level : str, goal : str ):
    age = calculate_age(date_of_birth)
    rmr = (weight * 10) + (height * 6.25) - (age * 5) - 161
    activity_factor = 0

    if(activity_level == "none"):
        activity_factor = 1.2

    elif(activity_level == "light"):
        activity_factor = 1.375

    elif(activity_level == "moderate"):
        activity_factor = 1.55

    else:
        activity_factor = 1.725
    
    maintain = rmr * activity_factor

    if(goal == "cut"):
        return round(maintain * 0.9, 1)
         

    elif (goal == "bulk"):
        return round(maintain * 1.1, 1)
         
    
    return round(maintain,1)
    


def protein_calculation(weight : float , activity_level : str, goal : str):
    if (activity_level == "none"):
        if(goal == "cut"):
            return round(weight * 1.2, 1)
        elif(goal == "bulk"):
            return round(weight * 1.0, 1)
        return round(weight * 0.8, 1)
    
    elif (activity_level == "light"):
        if(goal == "cut"):
            return round(weight * 1.6, 1)
        elif(goal == "bulk"):
            return round(weight * 1.4,1)
        return round(weight * 1.2, 1)
        

    elif (activity_level == "moderate"):
        if(goal == "cut"):
            return round(weight * 1.8, 1)
        elif(goal == "bulk"):
            return round(weight * 1.6 , 1)
        return round(weight * 1.4, 1)
    
    else:
        if(goal == "cut"):
            return round(weight * 2.0, 1)
        elif(goal == "bulk"):
            return round(weight * 1.8, 1)
        return round(weight * 1.6, 1)
    


def fats_calculation(weight : float , height: float, date_of_birth : date, activity_level : str, goal : str):
    cal = calculate_daily_calories(weight, height, date_of_birth, activity_level , goal )
    return round((cal * 0.3)/9 , 1)


def carbohydrates_calculation(weight : float , height: float, date_of_birth : date, activity_level : str, goal : str):
    cal = calculate_daily_calories(weight, height, date_of_birth, activity_level , goal)
    protein = protein_calculation(weight, activity_level, goal)
    fats = fats_calculation(weight, height, date_of_birth, activity_level , goal)

    protein_calories = protein * 4
    fat_calories = fats * 9
    return round((cal - protein_calories - fat_calories) / 4 , 1)




