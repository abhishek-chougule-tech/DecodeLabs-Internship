# Project 4: The General Knowledge Quiz

# State Management: Initialize score vault
score = 0

print("Welcome to The General Knowledge Quiz!\n")

# --- Question 1 ---
# Step 1 & 2: Ask, Capture, and Sanitize
ans1 = input("1. What is the capital of France? ").strip().lower()

# Step 3 & 4: Evaluate & Execute
if ans1 == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Paris.\n")

# --- Question 2 ---
# Step 1 & 2: Ask, Capture, and Sanitize
ans2 = input("2. What language is primarily used for this project? ").strip().lower()

# Step 3 & 4: Evaluate & Execute
if ans2 == "python":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Python.\n")

# --- Question 3 ---
# Step 1 & 2: Ask, Capture, and Sanitize
ans3 = input("3. Which planet is known as the Red Planet? ").strip().lower()

# Step 3 & 4: Evaluate & Execute
if ans3 == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Mars.\n")

# --- Output: Final Results using F-String Formatting ---
print("=" * 30)
print(f"Quiz Completed! Your Final Score: {score}/3")
print("=" * 30)
