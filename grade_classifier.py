#Grade Classifier
learner_name = input("Enter learner's name: ") 

# first subject
subject1 = input("Enter name for first subject: ")
first_subject = float(input("Enter the mark for first subject: "))

 # second subject 
subject2 = input("Enter the second subject: ")
second_subject = float(input("Enter the mark for second subject: "))

 # third subject 
subject3 = input("Enter the third subject: ") 
third_subject = float(input("Enter the mark for third subject: "))

 # average mark 
average_mark = (first_subject + second_subject + third_subject) / 3


if average_mark >= 80:
    letter_grade = "A"
elif average_mark >= 70:
    letter_grade = "B"      
elif average_mark >= 60:
    letter_grade = "C"  
elif average_mark >= 50:
    letter_grade = "D"  
else: letter_grade = "F"

if average_mark >= 50: pass_status = "Pass"
else: pass_status = "Fail"

#intervention status
interventions = [] 
if first_subject < 40: interventions.append(subject1) 
if second_subject < 40: interventions.append(subject2)
if third_subject < 40: interventions.append(subject3)


 # Display report card 
print("--------------------") 
print(f"REPORT CARD")
print("--------------------")
print(f"Learner name: {learner_name}")
print("--- SUBJECT MARKS ---")
print(f"{subject1}: {first_subject}")
print(f"{subject2}: {second_subject}")
print(f"{subject3}: {third_subject}") 
print("--- OVERALL RESULTS ---")
print(f"Average mark: {round(average_mark, 0)}") 
print(f"Letter grade: {letter_grade}") 
print(f"Pass status: {pass_status}") 
print("--- INTERVENTION STATUS ---")
for subject in interventions:
    print(f"Intervention needed for: {subject}")  
else:
    print("No intervention required.")