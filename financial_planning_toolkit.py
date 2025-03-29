from mortgage_calculator import calculate_mortgage_payment
from investment_return_calculator import calculate_investment_return
from savings_goal_calculator import calculate_monthly_savings
from income_tax_calculator import calculate_tax

def mortgage_calculator_menu():
    print("\n=== Mortgage Calculator ===")
    principal = float(input("Enter Loan Amount (₹): "))
    annual_interest_rate = float(input("Enter Annual Interest Rate (%): "))
    loan_term_years = int(input("Enter Loan Term (Years): "))
    monthly_payment = calculate_mortgage_payment(principal, annual_interest_rate, loan_term_years)
    print(f"\nYour Monthly Payment is: ₹ {monthly_payment:.2f}")

def investment_return_menu():
    print("\n=== Investment Return Calculator ===")
    initial_investment = float(input("Enter Initial Investment Amount (₹): "))
    annual_rate = float(input("Enter Expected Annual Rate of Return (%): "))
    time_years = float(input("Enter Investment Time Period (Years): "))
    future_value = calculate_investment_return(initial_investment, annual_rate, time_years)
    print(f"\nFuture Value of Investment after {time_years} years: ₹ {future_value:.2f}")

def savings_goal_menu():
    print("\n=== Savings Goal Calculator ===")
    goal_amount = float(input("Enter your Savings Goal Amount (₹): "))
    annual_rate = float(input("Enter Expected Annual Rate of Return (%): "))
    time_years = int(input("Enter Time Frame to Achieve Goal (Years): "))
    monthly_savings = calculate_monthly_savings(goal_amount, annual_rate, time_years)
    print(f"\nYou need to save ₹ {monthly_savings:.2f} every month to reach your goal of ₹ {goal_amount:.2f} in {time_years} years.")

def income_tax_menu():
    print("\n=== Income Tax Calculator ===")
    income = float(input("Enter your Annual Income (₹): "))
    deductions = float(input("Enter your Deductions (₹): "))
    tax = calculate_tax(income, deductions)
    print(f"\nEstimated Tax Payable: ₹ {tax:.2f}")

def main():
    while True:
        print("\n===== Financial Planning Toolkit =====")
        print("1. Mortgage Calculator")
        print("2. Investment Return Calculator")
        print("3. Savings Goal Calculator")
        print("4. Income Tax Calculator")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            mortgage_calculator_menu()
        elif choice == '2':
            investment_return_menu()
        elif choice == '3':
            savings_goal_menu()
        elif choice == '4':
            income_tax_menu()
        elif choice == '5':
            print("Thank you for using Financial Planning Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
