grades_list = []
def get_user_grades(nums_grades:int)->list:
    
    for i in range(nums_grades):
        grade = float(input(f'\n Enter grade: : '))
        grades_list.append(grade)

def print_grades_needed(grades_list:float, exp_average:float):
      new_grade = (exp_average * (len(grades_list)+1)) - sum(grades_list) 
      print(f'\n You will need to get a {new_grade} on your next assignment to earn a {exp_average} average.') 


print('\n Welcome to the GPA calculator app')

user_name = str(input('\n Enter your name : '))
nums_grades = int(input('\n How many grades would you like to enter: '))
get_user_grades(nums_grades)
print("Grades Highest to Lowest:", sorted(grades_list,reverse = True))
nums_org = sorted(grades_list,reverse = True)
average = round(sum(grades_list)/(len(grades_list)),2)

print(f'\n Summary of your grades : ', sum(grades_list))
print(f'\n Total number of grades : {len(grades_list)}')
print(f'\n Average grade : {average}')
print(f'\n Highest grade : {nums_org[0]}')
print(f'\n Lowest grade  : {nums_org[-1]}')

desired_average = float(input('\n Enter your desired average : '))
print_grades_needed(grades_list, desired_average)

print('\n Let\'s see what would have been the average, if your grades were different')
subject_no = int(input('\n Enter the subject number that you want to modify : '))
modified_grade = int(input('\n Enter the grade : '))

copy_grades_list = grades_list
grades_list.remove(subject_no) 
grades_list.append(modified_grade)

average1 = round(sum(copy_grades_list)/(len(copy_grades_list)),2)

nums_org1 = sorted(copy_grades_list,reverse = True)

print(f'\n Summary of your grades : ', sum(copy_grades_list))
print(f'\n Total number of grades : {len(copy_grades_list)}')
print(f'\n Average grade : {average1}')
print(f'\n Highest grade : {nums_org1[0]}')
print(f'\n Lowest grade  : {nums_org1[-1]}')

difference = average1 - average


print(f'\n You\'re Your new average would be a {average1}, compared to your real average of {average} \n That is a change of {abs(difference)}')
print(f'\n Unfortunately, this changes nothing, go and work hard! Good Luck {user_name}')