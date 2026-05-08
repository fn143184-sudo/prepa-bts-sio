courses = []

while True:
    print("\n=== MENU LISTE DE COURSES ===")
    print("1 - Ajouter un article")
    print("2 - Supprimer un article")
    print("3 - Afficher la liste")
    print("4 - Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        article = input("Entrez le nom de l'article à ajouter : ")
        courses.append(article)
        print(f"'{article}' a été ajouté.")

    elif choix == "2":
        article = input("Entrez le nom de l'article à supprimer : ")
        if article in courses:
            courses.remove(article)
            print(f"'{article}' a été supprimé.")
        else:
            print("Cet article n'est pas dans la liste.")

    elif choix == "3":
        print("\n--- Votre liste de courses ---")
        if len(courses) == 0:
            print("La liste est vide.")
        else:
            for i, item in enumerate(courses, start=1):
                print(f"{i}. {item}")

    elif choix == "4":
        print("Au revoir !")
        break

    else:
        print("Option invalide.")
