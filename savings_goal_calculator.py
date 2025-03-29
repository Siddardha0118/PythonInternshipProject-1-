def calculate_monthly_savings(goal_amount, annual_rate, time_years):
    monthly_rate = annual_rate / 12 / 100
    total_months = time_years * 12

    if monthly_rate == 0:
        monthly_savings = goal_amount / total_months
    else:
        monthly_savings = goal_amount * monthly_rate / (((1 + monthly_rate) ** total_months - 1))

    return monthly_savings

def main():
    print("=== Savings Goal Calculator ===")
    goal_amount = float(input("Enter your Savings Goal Amount (₹): "))
    annual_rate = float(input("Enter Expected Annual Rate of Return (%): "))
    time_years = int(input("Enter Time Frame to Achieve Goal (Years): "))

    monthly_savings = calculate_monthly_savings(goal_amount, annual_rate, time_years)

    print(f"\nYou need to save ₹ {monthly_savings:.2f} every month to reach your goal of ₹ {goal_amount:.2f} in {time_years} years.")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
