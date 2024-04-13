from  time import time, sleep

# décorateur Python qui enregistre le temps d'exécution d'une fonction
def timer(function):
    def wrapper(*args, **kwargs):
        debut = time()  # Temps de début de l'exécution de la fonction
        resultat = function(*args, **kwargs)  # Appel de la fonction
        fin = time()
     
        print(f"le temps d'éxecution de la fonction {function.__name__}: {debut - fin} secondes")
        return resultat
    return wrapper


# fonction Python qui prend une liste d'entiers et renvoie une nouvelle liste contenant uniquement les nombres pairs
@timer
def list_of_even_number(numbers):
    try:
        return [num for num in numbers if num %2==0]
    except:
        print("erreur")
    
input_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,]

result = list_of_even_number(input_num)
print(f"{result}")
    
    # choice = "o"
    # my_list = []
    # even_number_list = []

    # def even_number(number: int):
    #     return (int(number) % 2)

    # while choice == "o":

    #     nbr = input("Entrer un nombre ")
    #     my_list.append(nbr)
    #     verify = even_number(nbr)
    #     if verify == 0:
    #         even_number_list.append(nbr)
    #     choice = input("voulez vous continuer ? o/n ")
        
    # print("votre liste de chiffre paire est {0}".format(even_number_list))
    # print("Fin merci d'avoir participer :)")
    # print(my_list)
    # return my_list
    


    





