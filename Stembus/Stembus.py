# Task to register leader name who want to participate in election
leider = []
for i in range(1, 6):
    leider_name = input("Voer je naam in als lijstrekker :")
    leider.append(leider_name)
    n = len(leider)
    if n < 5 :
        print("Je hebt je succesvol geregristeerd")
    else :
        print("Maximaal aantal lijstrekkers doen mee")

# Task to register candidate who want to caste their vote
stemmer = []
nummer = int(input("Voer het aantal stemmers die mee iwllen doen in :"))
for i in range(1,stemmer + 1):
    stemmer_nummer = int(input("Voer je stemnummer in:"))
    stemmer.append(stemmer_nummer)

leider_1_stemmen = 0
leider_2_stemmen = 0
leider_3_stemmen = 0
leider_4_stemmen = 0
leider_5_stemmen = 0

max = 0

num_of_stemmer = len(stemmer)




while True:
    if stemmer == []:
        print("Stemmen is over")
        max = leider_1_stemmen
        if leider_2_stemmen > max:
            max = leider_2_stemmen
            percent = (leider_2_stemmen / num_of_stemmer) * 100
            print(leider[1], "heeft gewonnen", "met", percent, "% stemmen")
            break
        elif leider_3_stemmen > max:
            max = leider_3_stemmen
            percent = (leider_3_stemmen / num_of_stemmer) * 100
            print(leider[2], "heeft gewonnen", "met", percent, "% stemmen")
            break
        elif leider_4_stemmen > max:
            max = leider_4_stemmen
            percent = (leider_4_stemmen / num_of_stemmer) * 100
            print(leider[3], "heeft gewonnen", "met", percent, "% stemmen")
            break
        elif leider_5_stemmen > max:
            max = leider_5_stemmen
            percent = (leider_5_stemmen / num_of_stemmer) * 100
            print(leider[4], "heeft gewonnen", "met", percent, "% stemmen")
            break
        else:
            percent = (leider_1_stemmen / num_of_stemmer) * 100
            print(leider[0], "heeft gewonnen", "met", percent, "% stemmen")
            break


    else:
        stemmer_nummer = int(input("Voer je stemnummer in :"))
        if stemmer_nummer in stemmer:
            print("You are a voter ")
            stemmer.remove(stemmer_nummer)
            print("========================================================\n")
            print("Hier is de lijst van de lijstrekkers :")
            print(" 1.leader-1 : ", leider[0],
                  "\n 2.leader-2 :", leider[1],
                  "\n 3.leader-3 :", leider[2],
                  "\n 4.leader-4 :", leider[3],
                  "\n 5.leader-5 :", leider[4])

            stem = int(input("Je kunt alleen stemmen met stemnummers zoals: 1,2,3,4,5  :\n"
                             " Voer alleen het nummer in van de lijstrekker zoals(1 of 2) :\n"))
            print("===========================================================\n")
            if stem == 1:
                leider_1_stemmen += 1
                print("Bedankt voor het stemmen! ")
            elif stem == 2:
                leider_2_stemmen += 1
                print("Bedankt voor het stemmen!")
            elif stem == 3:
                leider_3_stemmen += 1
                print("Bedankt voor het stemmen!")
            elif stem == 4:
                leider_4_stemmen += 1
                print("Bedankt voor het stemmen!")
            elif stem == 5:
                leider_5_stemmen += 1
                print("Bedankt voor het stemmen!")
            else:
                print("Lijstrekker is niet gevonden \n voer het correcte nummer in")


        else:

            print("Je hebt al gestemd of je stem nummer is verkeerd  ")