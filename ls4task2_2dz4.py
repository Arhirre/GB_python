# _author_ = Nikita_Savchenko

# не совсем явно какую вернюю границу взять и входит ли сами 20 и 240 в список.
# если да, то рэндж от 20 до 241
# если нет, то от 21 до 240
#

print(f'Nums from 20 to 240 divisible for 20 or 21 are: {[ele for ele in range(20, 241) if ele % 20 == 0 or ele % 21 == 0]}')
