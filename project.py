import sys
sys.stdout.reconfigure(encoding='utf-8')
import time

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
    import random
    return random.choice(quotes)


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
    print("\n" + "="*50)


if __name__ == "__main__":
    main()