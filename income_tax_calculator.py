def calculate_tax(income, deductions):
    taxable_income = income - deductions
    tax = 0

    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = (250000 * 0.05) + (taxable_income - 500000) * 0.20
    else:
        tax = (250000 * 0.05) + (500000 * 0.20) + (taxable_income - 1000000) * 0.30

    return tax

def main():
    print("=== Income Tax Calculator ===")
    income = float(input("Enter your Annual Income (₹): "))
    deductions = float(input("Enter your Deductions (₹): "))

    tax = calculate_tax(income, deductions)

    print(f"\nEstimated Tax Payable: ₹ {tax:.2f}")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
