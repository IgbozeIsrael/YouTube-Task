import webbrowser

def subscribe_to_earn_points():
    """Asks the user to subscribe to a YouTube channel to earn 100 points."""

    channel_url = "https://www.youtube.com/@solvium_puzzle"  # Replace with your channel URL

    print("Subscribe to the channel below to earn 100 points:")
    print(https://www.youtube.com/@solvium_puzzle)

    choice = input("Have you subscribed? (yes/no): ").lower()

    if choice == "yes":
        print("Congratulations! You have earned 100 points.")
    else:
        print("Please subscribe to the channel to earn your points.")

if __name__ == "__main__":
    subscribe_to_earn_points()
    