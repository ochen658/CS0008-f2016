form = input('Which system you wnat to use,usc press 1, metric press 2')
if form==1:
    distance_usc=float(input('how many miles you drove?'))
    distance_metric= distance_usc*0.621371
    gas_usc=float(input('how much gas you used?'))
    gas_metric= gas_usc*0.264172
    consumption_usc = distance_usc / gas_usc
    consumption_metric=(100*gas_metric)/distance_metric
    if consumption_metric > 20:
        consumption_rate = 'extremely poor'
    else:
        if consumption_metric <= 20 and consumption_metric > 15:
            consumption_rate = 'poor'
        elif consumption_metric <= 15 and consumption_metric > 10:
            consumption_rate = 'average'
        elif consumption_metric <= 10 and consumption_metric > 8:
            consumption_rate = 'good'
        else: consumption_rate='excellent'
    print('                     ','USC','                   ','Metric')
    print("distance___________: ", format(distance_usc,'9.3f'), 'miles', format(distance_metric,'9.3f'), 'km')
    print('Gas________: ', format(gas_usc,'9.3f'), 'gallons', format(gas_metric,'9.3f'), 'Liters')
    print('Consumption____: ', format(consumption_usc,'9.3f'), 'mpg', format(consumption_metric,'9.3f'), '1/100km')
    print('Gas Consumption rate:',consumption_rate)
elif form==2:
    distance_metric = float(input('how many km you drove?'))
    distance_usc = distance_metric * 1.60934
    gas_metric = float(input('how much gas you used?'))
    gas_usc = gas_metric * 3.78541
    consumption_metric = (100*gas_metric) / distance_metric
    consumption_usc=distance_usc/gas_usc
    if consumption_metric > 20:
        consumption_rate = 'extremely poor'
    else:
        if consumption_metric <= 20 and consumption_metric > 15:
            consumption_rate = 'poor'
        elif consumption_metric <= 15 and consumption_metric > 10:
            consumption_rate = 'average'
        elif consumption_metric <= 10 and consumption_metric > 8:
            consumption_rate = 'good'
        else: consumption_rate='excellent'
    print('                     ', 'USC', '                   ', 'Metric')
    print("distance___________: ", format(distance_usc, '9.3f'), 'miles', format(distance_metric, '9.3f'), 'km')
    print('Gas________: ', format(gas_usc,'9.3f'), 'gallons', format(gas_metric,'9.3f'), 'Liters')
    print('Consumption____: ', format(consumption_usc, '9.3f'), 'mpg', format(consumption_metric, '9.3f'), '1/100km')
    print('Gas Consumption rate:', consumption_rate)
