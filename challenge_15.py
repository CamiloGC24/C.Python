def get_user_grades(no_of_subjects:int)->list:
    grades_list = list()
    for i in range(no_of_subjects):
        grade = float(input(f'\n Enter grade: : '))
        grades_list.append(grade)
    return grades_list

def print_user_report(name :str,grades_list:list):
    grades_list.sort(reverse=True)
    print(f'\n Hi {name}, your grades are : ')
    for i in range(len(grades_list)) :
        print(f'\n Subject - {i+1} ---> {grades_list[i]} ')
    

    average = round(sum(grades_list)/len(grades_list),2)

    print(f'\n Summary of your grades : ')
    print(f'\n Total number of grades : {len(grades_list)}')
    print(f'\n Average grade : {average}')
    print(f'\n Highest grade : {grades_list[0]}')
    print(f'\n Lowest grade  : {grades_list[-1]}')
    return average

def print_grades_needed(grades_list:float, exp_average:float):
      new_grade = (exp_average * (len(grades_list)+1)) - sum(grades_list) 
      print(f'\n You should score {new_grade} grades next time, in order to get average of {exp_average}')  

print('\n Welcome to the GPA calculator app')

user_name = str(input('\n Enter your name : '))
no_of_subjects = int(input('\n How many grades would you like to enter: '))
grades_list = get_user_grades(no_of_subjects)





original_average = print_user_report(user_name,grades_list)

desired_average = float(input('\n Enter your desired average : '))
print_grades_needed(grades_list, desired_average)

print('\n Let\'s see what would have been the average, if your grades were different')
subject_no = int(input('\n Enter the subject number that you want to modify : '))
modified_grade = int(input('\n Enter the grade : '))

copy_grades_list = grades_list[:]
copy_grades_list.pop(subject_no)
copy_grades_list.append(modified_grade)

wishful_average = print_user_report(user_name,copy_grades_list)
difference = wishful_average-original_average
change = ""
if difference > 0 :
    change = "UP"
else:
    change = "DOWN"

print(f'\n You\'re updated average would have been {wishful_average}, that\'s {abs(difference)} points {change} !')
print(f'\n Unfortunately, this changes nothing, go and work hard! Good Luck {user_name}')