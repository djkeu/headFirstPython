bottles = "bottles of beer"

for beer_num in range(99, 0, -1):
    print(f"{beer_num} {bottles} on the wall")
    print(f"{beer_num} {bottles}")
    print("Take one down")
    print("Pass it around")

    if beer_num == 1:
        print("No more bottles of beer on the wall")
    else:
        beer_num -= 1
        if beer_num == 1:
            bottles = "bottle of beer"
        print(f"{beer_num} {bottles} on the wall")
    
    print()
