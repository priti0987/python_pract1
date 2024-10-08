import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Example usage: countdown timer for 10 seconds
countdown_timer(3)
