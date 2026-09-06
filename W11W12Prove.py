import statistics
year_of_interest = int(input("Enter the year of interest: "))
print()

life_expectancy_of_target_year = []
average_life_expectancy = 0
max_life_expectancy = 0
max_life_expectancy_country = ""
min_life_expectancy = 999
min_life_expectancy_country = ""


lowest_life_expectancy = 999
country_with_lowest = ""
year_with_lowest = 0

highest_life_expectancy = 0
country_with_highest = ""
year_with_highest = 0


#open file
with open ("life-expectancy.csv") as file:
    #skip the first line
    next(file)

    #read line by line
    for line in file:
        # print(line)

        #strip away extra spaces
        cleaned_line = line.strip()
        # print(cleaned_line)

        #split into small parts
        parts = cleaned_line.split(",")
        # print(parts)

        #get each element
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])
       

        # What is the year and country that has the lowest life expectancy in the dataset?
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
            country_with_lowest = country
            year_with_lowest = year

        # What is the year and country that has the highest life expectancy in the dataset?
        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy
            country_with_highest = country
            year_with_highest = year

        # Allow the user to type in a year, then, find the average life expectancy for that year. Then find the country with the minimum and the one with the maximum life expectancies for that year.
        if year == year_of_interest:

            # NOTE: We are finding the average of all life_expectancy values for all countries in a target year.
            
            # Using average_life_expectancy = statistics.mean(life_expectancy)
            # will cause this error:
            # TypeError: 'float' object is not iterable

            # statistics.mean(numbers) is used to calculate the average of a collection of numbers inside a LIST.

            # This happens because life_expectancy contains only ONE value (a float),
            # while statistics.mean() expects an iterable, such as a LIST.

            # Using average_life_expectancy = statistics.mean([life_expectancy])
            # works because [life_expectancy] creates a LIST containing one number.

            # However, the "average" is not supposed to simply be that single value.

            # ===> TO FIX:
            # Create a LIST to store all life_expectancy values for all countries
            # in the target year, and append each value to the list.
            
            life_expectancy_of_target_year.append(life_expectancy)

            average_life_expectancy = statistics.mean(life_expectancy_of_target_year)

            if life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy
                min_life_expectancy_country = country

            if life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy
                max_life_expectancy_country = country

    
    print(f"The overall max life expectancy is: {highest_life_expectancy} from {country_with_highest} in {year_with_highest}") 

    print(f"The overall min life expectancy is: {lowest_life_expectancy} from {country_with_lowest} in {year_with_lowest}\n")   

    print(f"For the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")
    print(f"The max life expectancy was in {max_life_expectancy_country} with {max_life_expectancy}")
    print(f"The min life expectancy was in {min_life_expectancy_country} with {min_life_expectancy}")
       
            

   


    