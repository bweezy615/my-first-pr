import random


def run_raffle(participants: list[str], num_winners: int = 1) -> list[str]:
    if not participants:
        raise ValueError("No participants in the raffle")
    if num_winners > len(participants):
        raise ValueError("Cannot pick more winners than participants")
    return random.sample(participants, num_winners)


def main():
    print("=== Tennessee Charity Raffle ===")
    print("(For qualifying nonprofit organizations only)\n")

    names_input = input("Enter participant names separated by commas: ")
    participants = [name.strip() for name in names_input.split(",") if name.strip()]

    if not participants:
        print("No participants entered. Exiting.")
        return

    try:
        num_winners = int(input(f"How many winners? (1-{len(participants)}): "))
    except ValueError:
        print("Invalid number. Defaulting to 1 winner.")
        num_winners = 1

    try:
        winners = run_raffle(participants, num_winners)
    except ValueError as e:
        print(f"Error: {e}")
        return

    print("\n--- Results ---")
    for i, winner in enumerate(winners, 1):
        print(f"  Winner #{i}: {winner}")


if __name__ == "__main__":
    main()
