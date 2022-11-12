key = 5

def pipi():
   def chose():
       chose = input("Ви бажаєте зашифрувати ?")
       chose = chose.lower()
       if chose == "e" or "encrypt":
           return chose
       elif chose == "d" or "decrypt":
           return chose
       else:
           print("Недійсна відповідь, спробуйте ще раз.")
           chose()

   def message():
       user = input("Введіть своє повідомлення : ")
       return user

   def waffle(chose, message, key):
       translated = ""
       if chose == "e" or "encrypt":
           for character in message:
               num = ord(character)
               num += key
               translated += chr(num)

               dereck = open('Encrypted.txt', 'w')
               dereck.write(translated)
           dereck.close()
           return translated
       else:
           for character in message:
               num = ord(character)
               num -= key
               translated += chr(num)
           return translated

   choice = chose()
   message = message()
   final = waffle(choice, message, key)
   print("\nOperation complete!")
   print(final)

pipi()