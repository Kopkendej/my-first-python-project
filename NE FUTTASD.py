def windows_torlo():
    import random
    import os
    number = random.randint(1,10)
    guess = int(input("Tippelj egy számot 1-10 kozott!"))

    if guess == number:
        print("Nyertél!")
        windows_torlo()
    else:
        os.remove(r"C:\Users\kopha\OneDrive\Asztali gép\OpenRGB_0.9_Windows_64_b5f46e3")

windows_torlo()


