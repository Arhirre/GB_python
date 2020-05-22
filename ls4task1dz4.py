# _author_ = Nikita_Savchenko


def sal_calc(work_h, sal_h, bonus):
    if work_h > 0:
        return (work_h * sal_h)+bonus
    elif work_h <= 0:
        return print('You did not worked that day!')


print(f'Your today salary is: {sal_calc(float(input("Enter work time in hours: ")), float(input("Enter worker salary per hour: ")), float(input("Enter bonus: ")))} ')
