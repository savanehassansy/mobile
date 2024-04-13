def duplicate_list(list_1,list_2):
    return list(set(list_1)&set(list_2))



    # lenght = 0
    # limit = input("Entrer une limite pour les élément du tableau: ")

    # print("Liste 1")
    # while lenght < int(limit):
    #     val = input("Entrer une valeur: ")
    #     list_1.append(val)
    #     lenght = len(list_1)
        
    # print("Liste 1: ",list_1)
    # lenght = 0

    # print("Liste 2")
    # while lenght < int(limit):
    #     val = input("Entrer une valeur: ")
    #     list_2.append(val)
    #     lenght = len(list_2)
    # print("Liste 2: ",list_2)

    

    # for val in list_1:
    #     if val in list_2:
    #         if val in final_list:
    #             None
    #         else:
    #             final_list.append(val)
    # print("Liste d'élément se répétant dans les deux liste: ",final_list) 
    # return final_list

list1=[0,1,2,3,4,5,6,7,8,9,10,11,12]
list2=[2,3,5,7,11]

result = duplicate_list(list1,list2)

print(f'{result}')