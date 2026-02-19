import random

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

salada_frutas = random.sample(frutas, k=3)

print(f'A salada de frutas surpresa foi feita com esses ingredientes {salada_frutas}')