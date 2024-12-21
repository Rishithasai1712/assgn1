def taxi_fare(list):
    sum=0
    for i in range(len(list)):
        d =list[i]*10+50
        print(f"Trip {i}:${d}")
        sum+=d
    return sum
list=[5,10,3]
print(f"Total Fare: ${taxi_fare(list)}")
