
total_run_count = 0


def my_decorator_func(func):

    def wrapper_function():
        global total_run_count
        func()
        total_run_count += 1

    return wrapper_function

def my_second_decorator_func(func):

    def wrapper_function():
        global total_run_count
        func()
        print("The second decorator function was run")

    return wrapper_function


@my_decorator_func
@my_second_decorator_func
def email_student():
    print('Student was emailed!')

#student = ["Hudson", "Nolan", "Jack", "Tina", "Ethan"]

for _ in range(5):
    email_student()