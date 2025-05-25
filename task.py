num_cars = int(input())
sum_speed = 0

for _ in range(num_cars):
    init_speed = int(input())
    sum_speed += init_speed

average_speed = sum_speed / num_cars 

print(average_speed)