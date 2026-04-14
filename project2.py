import sys
sys.stdout.reconfigure(encoding='utf-8')

import time
import random


def analyze_reason(reason):
    suggestions = {
        "hard": "Break it into smaller steps. Start with just 10 minutes.",
        "boring": "Pair it with something fun like music or a reward.",
        "confusing": "Spend 15 minutes understanding the basics first.",
        "tired": "Take a short break or power nap before starting.",
        "lazy": "Start anyway. Action creates motivation, not the other way around."
    }
    return suggestions.get(reason.lower(), "Just start small. Progress matters more than perfection.")


def get_motivation():
    quotes = [
        "You don’t have to be perfect, just consistent.",
        "Small steps today lead to big results tomorrow.",
        "Discipline is choosing what you want most over what you want now.",
        "Start where you are. Use what you have. Do what you can."
    ]
    return random.choice(quotes)


def start_timer(minutes):
    total_seconds = minutes * 60

    print(f"\n⏳ Timer started for {minutes} minutes. Stay focused!\n")

    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\r⏱️  {timer}", end="")
        time.sleep(1)
        total_seconds -= 1

    print("\n\n✅ Time's up! Great job for showing up.")
    print("\a")  # Beep sound (works on many systems)


def main():
    print("\n" + "="*50)
    print("      PROCRASTINATION ANALYZER")
    print("="*50)
    time.sleep(1)

    task = input("\nWhat task are you avoiding? ")
    time.sleep(1)

    print("\nWhy are you avoiding it?")
    print("Options: hard / boring / confusing / tired / lazy")
    reason = input("Enter your reason: ")

    time.sleep(1)
    print("\nAnalyzing your procrastination pattern...\n")
    time.sleep(2)

    print("\n🔍 ANALYSIS RESULT")
    print("-"*30)

    suggestion = analyze_reason(reason)

    print(f"📌 Task: {task}")
    print(f"⚠️  Reason: {reason}")
    print(f"💡 Suggestion: {suggestion}")

    print("\n✨ Motivation:")
    print(get_motivation())

    print("\n🚀 Action Plan:")
    print(f"Start with: Spend just 5–10 minutes on '{task}'.")

    # TIMER SECTION
    print("\n⏳ Choose your focus time:")
    print("1. 5 minutes")
    print("2. 10 minutes")
    print("3. 25 minutes (Pomodoro)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        start_timer(5)
    elif choice == "2":
        start_timer(10)
    elif choice == "3":
        start_timer(25)
    else:
        print("Skipping timer. But try starting anyway!")

    print("\n" + "="*50)


if __name__ == "__main__":
    main()