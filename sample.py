def compound_interest(principal, duration, interest_rate):
    # Check if the interest rate is valid
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None

    # Check if the duration (years) is a positive number
    if duration < 0:
        print("Please enter a positive number of years")
        return None

    # Loop through each year and calculate the amount earned
    for year in range(1, duration + 1):
        total_for_the_year = principal * (1 + interest_rate) ** year
        print(f"The total amount of money earned by the investment in year {year} is {round(total_for_the_year)} £")

    # Final value after all years
    final_value = principal * (1 + interest_rate) ** duration

    # Return the final value as an integer
    return int(final_value)

# Example test
result = compound_interest(1000, 5, 0.03)
print("Final investment value after 5 years:", result, "£")



