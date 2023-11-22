from problem_02 import Car, CommercialAirplane, FighterJet

def main():
    # bmw = Car(
    #     model = "BMW M3 G80", 
    #     age = 3, 
    #     condition = 0.9, 
    #     odometer=14_762
    # )
    # print(bmw)

    # raptor_F22 = FighterJet(
    #     model = "Boeing F-22 Raptor", 
    #     age = 10, 
    #     condition = 0.8,
    #     nationality = "US",
    #     weaponry = ["rotary cannon", "air-to-air missiles", "GPS-guided ground bombs"]
    # )
    # print(raptor_F22)

    print("\ninstantiating an A380 commercial airliner:")
    first_A380 = CommercialAirplane(
        model = "Airbus A380", 
        age = 16, 
        condition = 0.6,
        airline = "Singapore Airlines", 
        seating_capacity = 525
    )
    print(first_A380)

    print("\nflying 18 round-trips on a 10-hour route, slightly reducing condition for each time:")
    for _ in range(18):
        first_A380.fly(10) # to destination
        first_A380.fly(10) # back to base
    print(first_A380)

    print("\nrestoring the plane to 'mint' condition:")
    first_A380.restore()
    print(first_A380)

if __name__ == "__main__":
    main()
