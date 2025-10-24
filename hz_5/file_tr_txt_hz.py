# feldata 
import random as rmd  
import numpy as np 
def fil_txt_random_toss():
    with open(file="kiseret.txt" ,mode="a", ) as test_txt:
       for i in range(rmd.randint(0,5000)):
        i = rmd.choice(["T","I"])
        test_txt.write(f"{i}\n")

#fil_txt_random_toss()

def How_many_toss(file = "kiseret.txt"):
   """
    so this func returning the len(txt)->file lines 
    and the coins tosses % like pr_a :foat = 20.01
   """
   txt_len_int = 0 
   Many_I_int = 0 
   with open(file= file , mode= "r") as gamble_toss_txt_results:
        for i in gamble_toss_txt_results:
          txt_len_int +=1 
          if i == "I\n":
             Many_I_int +=1 
              
        gamble_toss_txt_results.close() 
        pr_a  =  (Many_I_int/txt_len_int)*100 
        pr_b = 100- pr_a
        return round(pr_a,2), round(pr_b,2) , txt_len_int 

#print(How_many_toss())
def How_manny_dd_I_toss(path="kiseret.txt", I_toss=0):
    with open(path, "r", encoding="utf-8") as II_dd_toss:
        big_list = [line.strip() for line in II_dd_toss]
    for idx, val in enumerate(big_list[:-1]):
        if val == "I" and big_list[idx + 1] == "I":
            I_toss += 1
    return I_toss
  

#print(How_manny_dd_I_toss())


"""feladat 2 """

"""3 feladat """
#from https://mathspp.com/blog/base-conversion-in-python
def from_base(digits, base): 
    """Converts a list of digits in the given base to an integer.

    The first digit is the most significant and the base is assumed to
    be an integer greater than or equal to 2.
    """
    power = 1
    number = 0
    for digit in reversed(digits):
        number += power * digit
        power *= base
    return number


def base_transformater_to_arrey(base_number):
   #10→a; 11→b; 12→c; 13→d; 14→e; 15→f.
   letter_numer = {
      "a":10, 
      "b":11,
      "c":12,
      "d":13,
      "e":14,
      "f":15
   }
   list_base = []
   for i in str(base_number).lower():
      if i in set("abcdef"):
         list_base.append(letter_numer[i])
         continue
      list_base.append(int(i))
   
   return list_base

def get_min_base_In_arrey(transformed_arrey):
   return int(max(transformed_arrey)) + 1

def main():
   #setting the min base number up // helper  
   base_mistery_number_one = "110a10101"
   base_mistery_number_second = 223313020003
   #transforming the bases to arreys 
   trans_arrey1 = base_transformater_to_arrey(base_mistery_number_one)
   trans_arrey2 = base_transformater_to_arrey(base_mistery_number_second)
   # min bases from transformed arreys
   min_base1 = get_min_base_In_arrey(trans_arrey1)   
   min_base2 = get_min_base_In_arrey(trans_arrey2)

   while True:
      from_base_1 = from_base(digits=trans_arrey1, base=min_base1)
      from_base_2 = from_base(digits=trans_arrey2, base=min_base2)
      if from_base_2 == from_base_1:
         return from_base_2, min_base1, min_base2  # number, first number base, second number base
      # move the smaller value upward
      if from_base_1 < from_base_2:
         min_base1 += 1  
      else:
         min_base2 += 1

#print(main())

"""feladat 4"""


