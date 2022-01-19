def computepay(hours,rate):
    hours = input("Enter number of hours\n")
    rate = input("Enter the rate\n")
    try:
        ihours = int(hours)
        irate = int(rate)
    except:
        ihours = 0
        irate = 0
        print("Please enter a number\n")

if ihours < 40:
    result = ihours * irate
else:
    result = (40 * irate) +(1.5*irate*(ihours-40))

print("you will be paid",result)
