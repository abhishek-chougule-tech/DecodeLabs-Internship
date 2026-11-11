def expense_tracker():
    # INITIALIZATION (MEMORY): Initialized OUTSIDE the loop to preserve state
    total = 0

    print("=== EXPENSE TRACKER ===")
    print("Enter transaction amounts. Type 'quit' to stop and view final total.\n")

    # CONTINUOUS AUDIT LOOP
    while True:
        user_input = input("Enter expense: ").strip()

        # THE KILL SWITCH (Sentinel Value Check)
        if user_input.lower() == 'quit':
            break

        # DEFENSIVE CODING (Digital Poka-Yoke / Type-Safety)
        try:
            # PHASE 1: THE GATEKEEPER (int Transformation Mechanism)
            expense = int(user_input)
            
            # ACCUMULATOR PATTERN (Stateful Ledger: total += new_expense)
            total += expense

        except ValueError:
            # SHIELD INTERFACE
            print("Invalid Data")

    # PHASE 3: OUTPUT DISPLAY
    print(f"\nFINAL TOTAL: ${total:.2f}")


if __name__ == "__main__":
    expense_tracker()