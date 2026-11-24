scores = []

for i in range(1, 6):
    score = int(input(f"Enter Quiz {i} score:"))
    scores.append(score)

number = len(scores)
total = sum(scores)
average = total / number
max_score = max(scores)
min_score = min(scores)

print("===== QUIZ SCORE REPORT =====")
print(f"Quiz Scores: {scores}")
print(f"Total Score: {total}")
print(f"Average Score: {average:.2f}")
print(f"Highest Score: {max_score}")
print(f"Lowest Score: {min_score}")
print(f"Ascending: {sorted(scores)}")
print(f"Descending: {sorted(scores, reverse=True)}")
print(f"Original Scores: {scores}")

