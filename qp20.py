# 20. Accept the following from the user and calculate the percentage of attendance 
# Total number of working days 
# Total number of days absent 
# After calculating the percentage show that if the percentage is less than 75, then the student will not be able to attend the exam
# ..................................................................................................................................................

working_days = int(input('enter the total number of working days: '))
absent_days = int(input('Enter the total number of absent days: '))

percent = ((working_days - absent_days) * 100) // working_days
if percent < 75:
    print(percent, '%, The student will not be able to attend the exam')
else:
    print(percent, '%, The student will able to attend the exam')
    