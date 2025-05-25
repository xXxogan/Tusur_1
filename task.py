num_cars = int(input())
sum_speed = 0
check = 0
 
for _ in range(num_cars):
    init_speed = int(input())
    sum_speed += init_speed
    if init_speed >= 60:
        check = 1

average_speed = sum_speed / num_cars 

if check == 1:
    print('Yes')

print(average_speed)