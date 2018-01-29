# print(route_file[:20])
def get_cost():
    route_file = ''
    # with open('erase.txt') as file:
    # with open('small_route_nums.txt') as file:
    with open('route_costs_100000.txt') as file:
        # route_file = file.read().split('\n')
        route_file = sorted(file.read().split('\n'))

    phone_file = ''
    # with open('erase2.txt') as file2:
    # with open('small_phone_nums.txt') as file2:
    with open('phone_nums_1000.txt') as file2:
        phone_file = sorted(file2.read().split('\n'))

    final_cost = {}
    route_index = 0
    group_index = 0
    while group_index <= (len(phone_file) - 1) and route_index < len(route_file):
        phone_prefix = phone_file[group_index][1:5]
        
        route_prefix = route_file[route_index][1:5]

        if route_prefix > phone_prefix:
            group_index += 18
            continue
        
        if route_prefix != phone_prefix:
            route_index += 1
            continue
        else:
            old_group_index = group_index
            route_num = route_file[route_index].split(',')[0][1:]
            route_cost = route_file[route_index][-4:]
            for count in range(18):
                phone_num = phone_file[group_index][1:]
                if route_num in phone_num:

                    if phone_num in final_cost:
                        old_price = final_cost[phone_num][0]
                        old_route = final_cost[phone_num][1]

                        if len(route_num) > len(old_route):
                            group_index += 1
                            final_cost[phone_num] = (route_cost, route_num)

                        elif len(route_num) == len(old_route) and route_cost < old_price:
                            group_index += 1
                            final_cost[phone_num] = (route_cost, route_num)


                    elif phone_num not in final_cost:
                        final_cost[phone_num] = (route_cost, route_num)
                        group_index += 1


                    if count == 17:
                        group_index = old_group_index
                        route_index += 1
                        break
                else:
                    group_index += 1
                    if count == 17:
                        group_index = old_group_index
                        route_index += 1
                        break
    return final_cost

def main():
    import time
    print(" ")
    start_time = time.time()
    get_cost()
    end_time = time.time()
    print("Run time:", end_time - start_time)
    print("--------")

if __name__ == '__main__':
    main()