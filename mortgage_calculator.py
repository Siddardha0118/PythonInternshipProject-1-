def calculate_mortgage_payment(principal, annual_interest_rate, loan_term_years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    number_of_payments = loan_term_years * 12

    if monthly_interest_rate == 0:
        monthly_payment = principal / number_of_payments
    else:
        monthly_payment = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments
        monthly_payment /= ((1 + monthly_interest_rate) ** number_of_payments - 1)

    return monthly_payment

def main():
    print("=== Mortgage Calculator ===")
    principal = float(input("Enter Loan Amount (₹): "))
    annual_interest_rate = float(input("Enter Annual Interest Rate (%): "))
    loan_term_years = int(input("Enter Loan Term (Years): "))

    monthly_payment = calculate_mortgage_payment(principal, annual_interest_rate, loan_term_years)

    print(f"\nYour Monthly Payment is: ₹ {monthly_payment:.2f}")
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
