def calculate_investment_return(initial_investment, annual_rate, time_years):
    future_value = initial_investment * (1 + annual_rate / 100) ** time_years
    return future_value

def main():
    print("=== Investment Return Calculator ===")
    initial_investment = float(input("Enter Initial Investment Amount (₹): "))
    annual_rate = float(input("Enter Expected Annual Rate of Return (%): "))
    time_years = float(input("Enter Investment Time Period (Years): "))

    future_value = calculate_investment_return(initial_investment, annual_rate, time_years)

    print(f"\nFuture Value of Investment after {time_years} years: ₹ {future_value:.2f}")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
