def main():

   print("Beräknar differensen av jämna/udda tal...")


   sum_odd = 0
   sum_even = 0


   for i in range(1, 1000, 2):
       sum_odd += i


   for i in range(2, 1000, 2):
       sum_even += i

 
   difference = sum_odd - sum_even


   print("Differensen=", difference)



main()