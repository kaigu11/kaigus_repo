class ageCalculator:
    def __init__(self, birth_year, current_year):
        self.birth_year = birth_year
        self.current_year = current_year
    def calculate_age(self):
        age_in_years = self.current_year - self.birth_year
        age_in_months = age_in_years * 12
        age_in_days = age_in_years * 365.24
        return age_in_years, age_in_months, age_in_days


def main():
    birth_year = int(input("Enter your birth Year: "))
    current_year = 2023
    age_calculator = ageCalculator(birth_year, current_year)
    age_in_years, age_in_months, age_in_days = age_calculator.calculate_age()
    print("Your age in years is:", age_in_years)
    print("Your age in months is:", age_in_months)
    print("Your age in days is:", age_in_days)

if __name__ == "__main__":
    main()
