while True:
    # Demander à l'utilisateur de saisir une valeur
    user_input = input("Entrez une valeur (ou 'exit' pour quitter) : ")

    # Vérifier si l'utilisateur souhaite quitter
    if user_input.lower() == 'exit':
        print("Au revoir !")
        break  # Quitter la boucle while

    # Vérifier le type de variable
    if user_input.isdigit():
        print("L'entrée est numérique.")
    elif user_input.lower() == 'true' or user_input.lower() == 'false':
        print("L'entrée est un booléen.")
    elif user_input.isalpha():
        print("L'entrée est une chaîne de caractères.")
    else:
        print("L'entrée ne correspond à aucun type connu.")
