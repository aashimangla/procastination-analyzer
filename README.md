# 🧠 Procrastination Analyzer

A simple yet insightful CLI-based Python project that helps users understand *why* they are procrastinating and suggests actionable steps to overcome it.

## 🚀 Features
- 🧠 Procrastination Analysis
  Identifies the reason behind task avoidance (hard, boring, confusing, tired, lazy).
- 💡 Smart Suggestions
  Provides personalized, actionable advice based on the user’s input.
- ✨ Motivational Boost
  Displays random motivational quotes to encourage users to take action.
- ⏳ Built-in Focus Timer
  Includes 5, 10, and 25-minute (Pomodoro) timers to help users get started instantly.
- 🎯 Action-Oriented Approach
  Encourages users to begin with small, manageable steps instead of overwhelming tasks.
- 💻 Simple CLI Interface
  Easy-to-use terminal-based interaction with clean and structured output.

## 💡 How It Works
The program asks the user:
1. What task they are avoiding  
2. Why they are avoiding it (hard, boring, confusing, tired, lazy)

Based on the input, it:
- Maps the reason to a predefined solution
- Generates a helpful suggestion
- Displays a random motivational quote

## 🛠️ Tech Stack
- Python
- Built-in libraries:
  - `time`
  - `random`
  - `sys`


## 📌 Example Output

```
==================================================
      PROCRASTINATION ANALYZER
==================================================

What task are you avoiding? Chores

Why are you avoiding it?
Options: hard / boring / confusing / tired / lazy
Enter your reason: lazy

Analyzing your procrastination pattern...


🔍 ANALYSIS RESULT
------------------------------
📌 Task: Chores
⚠️  Reason: lazy
💡 Suggestion: Start anyway. Action creates motivation, not the other way around.

✨ Motivation:
Discipline is choosing what you want most over what you want now.

🚀 Action Plan:
Start with: Spend just 5–10 minutes on 'Chores'.

⏳ Choose your focus time:
1. 5 minutes
2. 10 minutes
3. 25 minutes (Pomodoro)
Enter choice (1/2/3): 1

⏳ Timer started for 5 minutes. Stay focused!

⏱️  00:01

✅ Time's up! Great job for showing up.

==================================================
```
## 🎯 Purpose

This project is designed to:
- Demonstrate basic Python concepts (functions, dictionaries, user input)
- Apply simple behavioral logic
- Create an interactive CLI experience

## 🌱 Future Improvements

- Add GUI using Tkinter  
- Store user history  
- More advanced behavioral analysis  
- Personalized tracking and progress insights  

## 👩‍💻 Author

Aashi Mangla
