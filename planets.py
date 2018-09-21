def weight_on_planets():
   # write your code here
   weight = input("What do you weigh on earth? ")
   weight = int(weight)
   weightOnMars = weight * 0.38
   weightOnJupiter = weight * 2.34
   print("\n" + "On Mars you would weigh " + str(weightOnMars) + " pounds."
         + "\n" + "On Jupiter you would weigh " + str(weightOnJupiter) + " pounds.")

if __name__ == '__main__':
   weight_on_planets()