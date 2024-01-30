# Author: Dimitriοs Dimopoulos

try: # Για τυχόν προβλήματα 
     CALORIES_GOAL_LIMIT = 0 
     def calculator():
          """Πέρνει τις θερμίδες που έφαγε και τις αφερεί από το όριο. Αν δεν βάλει θερμίδες, τερματίζει το πρόγραμμα"""
          global calories_limit
          global Efaga
          global inflag
          inflag = False
          Efaga= ""
          while type(Efaga) != type(0):
               Efaga = input("Θερμίδες που πήρες (Δώσε ENTER για τερματισμό):")
               if Efaga == "":
                    inflag = True
                    break
               else:
                    try:
                         Efaga= int(Efaga)
                    except ValueError:
                         print("Δώσε αριθμό για θερμίδες!")
          if inflag == False:
               calories_limit= int(calories_limit) - int(Efaga)

     def Apominaria(calories_limit, CALORIES_GOAL_LIMIT):
          """Εμφανίζει πόσες θερμίδες του μένουν"""
          if calories_limit == 1:
               print(f"Σου απομένει 1 θερμίδα από τις {CALORIES_GOAL_LIMIT}")
          else:
               print(f"Σου απομένουν {calories_limit} θερμίδες από τις {CALORIES_GOAL_LIMIT}")

     def Extra(calories_limit, CALORIES_GOAL_LIMIT):
          """Εμφανίζει πόσες έξτρα θερμίδες έχει πάρει"""
          if calories_limit == -1:
               print(f"Πήρες έξτρα 1 θερμίδα από τις {CALORIES_GOAL_LIMIT}")
          else:
               calories_extra= int(calories_limit) * -1
               print(f"Πήρες έξτρα {calories_extra} θερμίδες από τις {CALORIES_GOAL_LIMIT}")

     Akribos = f"Έχεις συμπληρώσει το όριο των {CALORIES_GOAL_LIMIT} θερμίδων... \nΠλύνε δόντια!"

     def Output(calories_limit, CALORIES_GOAL_LIMIT, Akribos=Akribos,):
          """Επιλέγει την καταλληλότερη εμφάνιση και την εμφανίζει"""
          if calories_limit == 0:
               print(Akribos)
          elif int(calories_limit) > 0:
               Apominaria(calories_limit, CALORIES_GOAL_LIMIT)
          elif int(calories_limit) < 0: #else
               Extra(calories_limit, CALORIES_GOAL_LIMIT)
          

     with open("Calories.txt", 'a') as o:
          pass
     with open("Calories.txt", 'r') as rf:
          v = rf.read()
     if v == "":    #Γράφει τα δεδομένα την πρώτη φορά που τρέχει το πρόγραμμα
          calories_limit=(input("Όριο Θερμιδών (δώσε ENTER για 2000):"))
          if calories_limit== "":
               calories_limit= CALORIES_GOAL_LIMIT= 2000 #kcal
               with open("Calories.txt", "w", encoding="utf-8") as gf:
                    gf.write(str(CALORIES_GOAL_LIMIT))
          else:
               while type(calories_limit) != type(0):
                    try:
                         calories_limit= CALORIES_GOAL_LIMIT= int(calories_limit)
                    except: 
                         print("Δώσε αριθμό!")
                         calories_limit=(input("Όριο Θερμιδών (δώσε ENTER για 2000):"))
          while True:
                    calculator()
                    if inflag == True:
                         break
                    else:
                         Output(calories_limit, CALORIES_GOAL_LIMIT)
                    with open("Calories.txt", 'w', encoding="utf-8") as f:
                         f.write(str(CALORIES_GOAL_LIMIT))
                         f.write("\n")
                         f.write(str(calories_limit))
          print("Πλύνε δόντια!")
          with open("Calories.txt", 'w', encoding="utf-8") as f:
               f.write("")
          
     else:     #Διαβάζει τα δεδομένα για τις υπόλοιπες φορές που τρέχει το πρόγραμμα
               #Γράφει τα καινούργια δεδομένα
          with open("Calories.txt", 'r') as varf:
               CALORIES_GOAL_LIMIT= int(varf.readline())
               calories_limit= int(varf.readline())
          Output(calories_limit, CALORIES_GOAL_LIMIT)
          while True:
               calculator()
               if inflag == True:
                         break
               else:
                    Output(calories_limit, CALORIES_GOAL_LIMIT)
               with open("Calories.txt", 'w', encoding="utf-8") as f:
                    f.write(str(CALORIES_GOAL_LIMIT))
                    f.write("\n")
                    f.write(str(calories_limit))

          print("Πλύνε δόντια!")
          with open("Calories.txt", 'w', encoding="utf-8") as f:
               f.write("")
except:
     with open("Calories.txt", 'w', encoding="utf-8") as f:
               f.write("")