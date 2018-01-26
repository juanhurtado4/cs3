def get_cost(phone_num):
    with open('erase_carrier_route.txt') as file:
        previous = ''
        for carrier_route in file.readlines():
            arr_route = carrier_route.split(',')
            (c_phone, c_cost) = (arr_route[0], arr_route[1])
            if phone_num == c_phone:
                return float(c_cost)
            elif phone_num in c_phone and len(c_phone) > len(previous):
                previous = c_phone
                result = c_cost

        return 0 if previous == '' else float(result)
