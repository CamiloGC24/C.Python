def conversion_app():
    print("\tWelcome to the Miles Per Hour Conversion App")

    miles = float(input("\tWhat is your speed in miles per hour:\t"))

    kmXh = round(miles * 0.4474,2)

    print(f"\tYour speed in meters per second is: {kmXh}")

conversion_app()