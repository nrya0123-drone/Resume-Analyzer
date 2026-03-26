# AI Resume Analyzer

skills = ["python", "java", "c++", "machine learning", "ai", "data science", "sql"]
resume = input("Paste your resume text:\n").lower()
found_skills = []
missing_skills = []

for skill in skills:
    if skill in resume:
        found_skills.append(skill)
    else:
        missing_skills.append(skill)

print("\n--- RESULT ---")

print("\nSkills Found:")

for s in found_skills:
    print("#", s)

print("\nSkills Missing:")
for s in missing_skills:
    print("#", s)

score = (len(found_skills) / len(skills)) * 100
print(print("\nYour resume score is:", score, "%"))

if score < 50:
    print("Suggestion: Improve your skills to strengthen your resume.")
else:
    print("Suggestion: Good resume! Keep improving.")

