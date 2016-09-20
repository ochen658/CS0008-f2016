min_salary = 30000.0
min_year = 2
salary = float(input('Enter your salary:'))
years_on_job = int(input('Enter the number'+
                         'of years employed'))
if years_on_job >= min_year:
  if salary >= min_salary:
    print('you qualify for the loan')
else:
    print('you must have been empoyed at least','for', min_year,'year to qualify.')
if salary >= min_salary:
    print('you qualify for the loan')
else:
    print('you must aat least earn', format(min_salary, ',.2f'),'per year to qualify')
#