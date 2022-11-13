"""
# =============================================================================
# Projet Programmation Orientée Objet - POOkemon
# =============================================================================
13/01/2022

# =============================================================================
# Auteur
# =============================================================================
Xiaowei CHEN 
Yizen SUN
Hanlin LIU    3971558

# =============================================================================
# Encadrants
# =============================================================================
Thomas Dietenbeck
Florence OSSART

# =============================================================================
# README
# =============================================================================

"""
#%% Importer les bibliotheques utilisés
import random as random
from random import choice
import sys
import time
import os
from abc import ABC , abstractmethod
# from DossierDonnee import * 
# import DossierDonnee as DossierDonnee
# from quitter import quitter
# from ChoisirPokemon import chosirPokemon, aleatoire
# from Interface import interfaceConnexion, creerNouveauDresseur
#%%
chemin = os.getcwd()
#%% lire les informations dans le fichier "Pokemons".

# Construire les tableaus de l'information du Pokemon
pokemon_nom=[]        # Nom de Pokemon
liste_competence=[]   # La competence de Pokemon
liste_element=[]      # L'élément de Pokemon
niveau_init=[]        # Le niveau initial de Pokemon
niveau_max=[]         # Le niveau maximal de Pokemon
vie_init = []         # La vie initiale de Pokemon
vie_max = []          # La vie maximale de Pokemon
vie_upgrade = []      # La vie augmentée à chaque niveau
energie_init =[]      # L'énergie initiale de Pokemon
energie_max = []      # L'énergie maximale de  Pokemon
energie_upgrade=[]    # L'energie augmentée à chaque niveau
regene_init = []      # La valeur initiale de la régénération
regene_max =[]        # La valeur maximale de la régénération
regene_upgrade=[]     # La régénération augmentée à chaque niveau
resist_init = []      # La résistance initiale de Pokemon
resist_max = []       # La résistance initiale de Pokemons
resist_upgrade=[]     # La résistance augmentée à chaque niveau

# Ouvrir le fichier 'Pokémon', Lire les données.
Atry1 = True
try: 
    donnees_pokemon = open(chemin + '/pokemon.txt').readlines()
#except: Atry1 = False
except:
    donnees_pokemon = open(chemin + '/pokemon.csv').readlines()
    
# =============================================================================
# donnees_pokemon= open(chemin + '/pokemon.txt').readlines() 
# =============================================================================

# Récupérer les informations de chaque Pokemon
for i in range(1,len(donnees_pokemon)):
    pokemon_nom.append(donnees_pokemon[i].split('\t')[0])
    liste_element.append(donnees_pokemon[i].split('\t')[3])
    niveau_init.append(donnees_pokemon[i].split('\t')[4].split('-')[0])
    niveau_max.append(int(donnees_pokemon[i].split('\t')[4].split('-')[1]))
    vie_init.append(donnees_pokemon[i].split('\t')[5].split('-')[0])
    vie_max.append(donnees_pokemon[i].split('\t')[5].split('-')[1])
    vie_upgrade.append(int(int(donnees_pokemon[i].split('\t')[5].split('-')[1])-int(donnees_pokemon[i].split('\t')[5].split('-')[0]))/4)
    energie_init.append((donnees_pokemon[i].split('\t')[6].split('-')[0]))
    energie_max.append(donnees_pokemon[i].split('\t')[6].split('-')[1])
    energie_upgrade.append(int(int(donnees_pokemon[i].split('\t')[6].split('-')[1])-int(donnees_pokemon[i].split('\t')[6].split('-')[0]))/4)
    regene_init.append(donnees_pokemon[i].split('\t')[7].split('-')[0])
    regene_max.append(donnees_pokemon[i].split('\t')[7].split('-')[1])
    regene_upgrade.append(int(int(donnees_pokemon[i].split('\t')[7].split('-')[1])-int(donnees_pokemon[i].split('\t')[7].split('-')[0]))/4)
    resist_init.append(donnees_pokemon[i].split('\t')[8].split('-')[0])
    resist_max.append(donnees_pokemon[i].split('\t')[8].split('-')[1])
    resist_upgrade.append(int(int(donnees_pokemon[i].split('\t')[8].split('-')[1])-int(donnees_pokemon[i].split('\t')[8].split('-')[0]))/4)
    liste_competence.append(donnees_pokemon[i].split('\t')[9].replace('[','').replace(']','').split(','))

#%% Le fichier 'defense'

# Construire les tableaux de la compétence défensee
defense_nom = []     # Le nom de la compétence défensee
defense_desc =[]     # La description de la compétence défensee
defense_elem = []    # L'élement de la compétence défensee
defense_soin = []    # La valeur de soin
defense_energie = [] # La valeur d'énergie
defense_cout = []    # La valeur de cour

# Ouvrir le fichier, Lire les données
Atry2 = True
try: 
    dossier_defence = open(chemin + '/defense.txt').readlines()
except:
    dossier_defence = open(chemin + '/defense.csv').readlines()

for i in range(len(dossier_defence )):
    dossier_defence [i] = dossier_defence [i].split(';')

# récupérer les informations  
for i in range(1,len(dossier_defence)):
    defense_nom.append(dossier_defence [i][0])
    defense_desc.append(dossier_defence [i][1])
    defense_elem.append(dossier_defence [i][2])
    defense_soin.append(dossier_defence [i][3])
    defense_energie.append(dossier_defence [i][4])
    defense_cout.append(dossier_defence [i][5])
#%% le fichier 'attack '

# Construire les tableaux de la compétence attack
attaque_nom = []    # Le nom
attaque_desc =[]    # La description de la compétence attack
attaque_elem = []   # L'élément de la compétence attack
attaque_puiss = []  # La puissance de la compétence attack
attaque_prec = []   # La precision de la compétence attack
attaque_cout = []   # Le cout de la compétence attack

# Ouvrir le fichier, Lire les données
Atry3 = True
try: 
    dossier_attaque = open(chemin + '/attaque.txt').readlines()
except:
    dossier_attaque = open(chemin + '/attaque.csv').readlines()
    
# =============================================================================
# dossier_attaque = open(chemin + '/attaque.csv').readlines()
# =============================================================================
for i in range(len(dossier_attaque)):
    dossier_attaque[i] = dossier_attaque[i].split(';')

# récupérer les informations  
for i in range(1,len(dossier_attaque)):
    attaque_nom.append(dossier_attaque[i][0])
    attaque_desc.append(dossier_attaque[i][1])
    attaque_elem.append(dossier_attaque[i][2])
    attaque_puiss.append(int(dossier_attaque[i][3]))
    attaque_prec.append(int(dossier_attaque[i][4]))
    attaque_cout.append(int(dossier_attaque[i][5]))
#%% Programme de Dresseur en classe
class Dresseur: 
    def __init__(self, nom, deck, touslesPokemons):
        self.__nom = nom
        self.__deck = deck
        self.__touslesPokemons = touslesPokemons
        
    @property
    def nom(self): return  self.__nom
    @nom.setter 
    def nom(self, nom): self.__nom = nom
    @property
    def deck(self): return  self.__deck
    @deck.setter
    def deck (self, deck): self.__deck = deck 
    @property
    def touslesPokemons(self): return self.__touslesPokemons
    @touslesPokemons.setter
    def touslesPokemons(self, touslesPokemons): self.__touslesPokemons = touslesPokemons
        
    # Afficher l'informations du dresseur
    def __str__(self):
        res = "Dresseur: " + self.__nom + "avec ses Pokemons ci-dessous: "
        for i in range (len(self.__touslesPokemons)):
            res += self.__touslesPokemons[i] + "\n"
        return res
    
    def capturerPokemon(self, pokemon):
        # Il faut tester d'abord si le dresseur possède déjà ce pokémon.
        # Dressue ne peut pas avoir deux pokémons identiques
        if pokemon in (self.__touslesPokemons): 
            print("Vous avez déja eu ce Pokémon, essayez-vous de capturer l'autre pokemon :D")
        else:    
            self.__touslesPokemons.append(pokemon) #Capturer ce pokémon
            print("Vous avez réussi à capturer {} !".format(pokemon.nom))
    
    # Dans le match, voir les informations du dresseur            
    def voirdeck(self): 
        """
        Fonction pour voir le deck. Afin d'utiliser cette fonciton dans le  
        combat, il faut d'abord tester si la vie du pokémon n'est pas 0.
        Enfin, cette fonction retourne une liste qui contient les pokémons disponibles
        """
        #Créer une liste qui contient les pokémons disponibles(la vie != 0)
        pokemonDispo = [i for i in self.__deck if i.vie !=0] 
        print("Vos pokemons disponibles chez Deck sont:\n"), print(" ")
# =============================================================================
#         for i in self.__deck:
#             if i.vie !=0:
#                 pokemonDispo.append(i)
# =============================================================================
        # Afficher la liste de pokemon disponible       
        for i in range(len(pokemonDispo)):
                print("{0}.{1}".format(i,pokemonDispo[i])) 
                print("-------------------------------------------") 
        print(""), time.sleep(0.3)
        return pokemonDispo
    
    def changerPokemon(self):
        """
        Fonction pour changer pokémon pendant le combat.      
        De même, on affiche d'abord les pokémons disponibles
        Enfin, cette fonction retourne un pokémon choisit
        """
        pokemonDispo = self.voirdeck()
        while True:
            opera = input("Quel Pokemon voulez-vous choisir à faire le combat ? (0-2)") 
            # Il faut tester si la commande est acceptabe (la command est un chiffre et ne dépasser pas le long du deck)
            if opera.isdecimal() and int(opera) < len(pokemonDispo): 
                Pokemonchoisi = pokemonDispo[int(opera)]
                print("Pokemon de {0} actuel est {1}".format(self.nom, Pokemonchoisi.nom))
                return Pokemonchoisi
            else:
                print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
                 
    def voirtouslesPokemons(self):
        #Cette fonction affiche tous vos pokémons possédés        
        print("Tous vos Pokemons sont:"), print(" ")
        for i in range (len(self.__touslesPokemons)):
            print("{0}.{1}".format(i,self.__touslesPokemons[i]))
            print("-------------------------------------------")
        print(''), time.sleep(0.3)

    # En mode non-combat, changer le deck du dresseur           
    def changmentDeck(self): 
        """
        Cette fonction consiste à changer le deck. 
        Il permet le dresseur changer son deck s'il n'est pas en combat
        Enfin, il retourne "self.__deck"
        """
        flag = True,  print(" ")
        # Créer d'abord une liste qui contient les pokémons qui n'est pas dans le deck
        PokemonSaufDeck = [k for k in self.__touslesPokemons if k not in self.__deck]
# =============================================================================
#         for k in self.__touslesPokemons:
#             if k not in self.__deck:
#                 PokemonSaufDeck.append(k)
# =============================================================================
        print("Changement de Deck\nVoici vos Pokémons dans deck:"), print(" ")
        self.voirdeck()
        while True:
            # Le joueur saisit le Pokémon qu'il souhaite déplacer
            opera_changer = input("Quel pokmon voulez vous remplacer? (0-2):")
            print('')
            if opera_changer.isdecimal() and int(opera_changer)<=2:
                print("Voici vos Pokemons disponibles :")
                for j in range (len(PokemonSaufDeck)):
                    print("{0}.{1}".format(j, PokemonSaufDeck[j]))
                    print("--------------------------------------------")
                while True:
                    opera_ajouter = input("Quel pokemon voulez vous ajouter? ")
                    if opera_ajouter.isdecimal() and int(opera_ajouter) <= len(PokemonSaufDeck):
                        #on remplace le pokémon par pokémon choisit
                        self.__deck[int(opera_changer)] = PokemonSaufDeck[int(opera_ajouter)]
                        print(""), print("Actuellement votre deck est :"), print("")
                        self.voirdeck()
                        flag = False #Cette petite "flag" permet de finir le boucle
                        break
                    else:
                        print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
                if not flag:
                    break
            else:
                print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
        return self.__deck
    
    # Fonction d'évoluer Pokémon
    def evolution(self):
        """
        Cette fonction permet d'évaluer le Pokémon. Des que le niveau du Pokémon 
        atteint le niveau maximum et le pokémon peut évaluer,il évalue.
        Le Pokémon évolué est un nouveau object et remplace le Pokémon d'origine.
        """
# =============================================================================
#         for i in self.__deck:
#             # Vérifier si le niveau atteint maximum et le pokémon peut évoluer.
#             if i.niveau > niveau_max[i.numero] and i.apres_evolution != None: 
#                 avant_evolution_nom = i.nom
#                 i = i.apres_evolution # Remplacer le Pokémon d'origine par le Pokémon évolué
#                 print("Votre {0} a évolué à {1}!\n".format(avant_evolution_nom, i.nom))
#                 time.sleep(0.3)
#         # De même, dans "touslespokemon", il faut aussi remplacer le Pokémon d'origine par le Pokémon évolué
#         for j in self.__touslesPokemons:
#             if j.niveau > niveau_max[j.numero] and j.apres_evolution != None: 
#                 j = j.apres_evolution 
# =============================================================================
        for i in range(len(self.__touslesPokemons)):
            if self.__touslesPokemons[i].niveau > niveau_max[self.__touslesPokemons[i].numero] \
                and self.__touslesPokemons[i].apres_evolution != None:
                avant_evolution_nom = self.__touslesPokemons[i].nom
                self.__touslesPokemons[i] = self.__touslesPokemons[i].apres_evolution
                print("Votre {0} a évolué à {1}!\n".format(avant_evolution_nom, self.__touslesPokemons[i].nom))
        for i in range(len(self.__deck)):
            if self.__deck[i].niveau > niveau_max[self.__deck[i].numero] and self.__deck[i].apres_evolution != None:
                self.__deck[i] = self.__deck[i].apres_evolution
                
    #La fonction pour commencer le cambat avec le pokémon
    def explorer(self):
        """
        Cette fonction pour trouver les pokémons sauvages dans la nature. 
        Il permet de commencer le combat Joueur contre Pokémon.
        Pareil, il faut vérifier si ce Pokémon sauvages n'est pas déja capturé par le dresseur
        """
        pokemonlibre = [i for i in TousPokemons_N2 if i not in self.__touslesPokemons]
# =============================================================================
#         for i in TousPokemons_N2:
#             if i not in self.__touslesPokemons:
#                 pokemonlibre.append(i)
# =============================================================================
        adversaire = choice(pokemonlibre)        # Choisr aléatoirement un Pokémon.
        print("Vous avez tombé sur {}".format(adversaire)) 
        combatjce = CombatJcE(self, adversaire ) # Instancier le combat
        combatjce.tour_par_tour()  # Utiliser la fonction "tour_par_tour" commencer le combat
    
    # La fonction de stockage      
    def sauvegarder(self): 
        """
        Cette fonction permet de souvgarder les informations du dressuer
        On enregistre les informations dans le même chemin que le programe et 
        dans un dossier qui s'appelle "save". Pour enregistrement, oon souvegarder
        le nom du dresseur, "self.__deck" et "self.__touslesPokemons".
        """
        #Vérifier d'abord si la dossier "save" existe.
        if os.path.exists(chemin + "/save") : 
            # Sauvgarder l'information de "self.__deck"
            editeur1 = open(chemin + "/save/" + self.__nom + ".txt","w") 
            for i in self.__deck: 
                editeur1.write(i.nom+'\n')
            # Sauvgarder l'information de "self.__touslesPokemons"
            editeur2 = open(chemin + "/save/" + self.__nom + ".txt","a") 
            for i in self.__touslesPokemons: 
                editeur2.write(i.nom+' '+str(i.niveau)+' '+str(i.exp)+'\n')
        else: # S'il n'y a pas de dossier "save", créer-en un nouveau  
            os.mkdir(chemin + "/save")  
            editeur1 = open(chemin + "/save/" + self.__nom + ".txt","w")  
            for i in self.__deck: 
                editeur1.write(i.nom+'\n')
            editeur2 = open(chemin + "/save/" + self.__nom + ".txt","a") 
            for i in self.__touslesPokemons:
                editeur2.write(i.nom+' '+str(i.niveau)+' '+str(i.exp)+'\n')
   
    def menu(self):
        """
        Cette fonction permet le dresseur effectuer des opérations sur " Menu".
        On définit toutes les fonctions que le joueur peut mettre en œuvre dans l'interface d'accueil
        """
        while True:
            print(" ")
            print("=================MENU================")
            print("||   O.Voyez votre deck            ||")
            print("||   1.Voyez tous vos Pokémons     ||")
            print("||   2.Changez le deck             ||")
            print("||   3.Capturez/Combattrez Pokemon ||")
            print("||   4.Combattrez Dresseur         ||")
            print("||   5.Creez un nouveau dresseur   ||")
            print("||   6.Exit                        ||")
            print("||   7.Sauvgarder                  ||")
            print("=====================================")
            opera=input("Qu'est ce que vous voulez faire? (0-7)") 
            flag = True
            if opera.isdecimal():
                if opera == "0":   time.sleep(0.3), self.voirdeck(),            time.sleep(0.3) 
                elif opera == "1": time.sleep(0.3), self.voirtouslesPokemons(), time.sleep(0.3) 
                elif opera == "2": time.sleep(0.3), self.changmentDeck(),       time.sleep(0.3) 
                elif opera == "3": time.sleep(0.3), self.explorer(),            time.sleep(0.3) 
                elif opera == "4": 
                    """
                    Commencer le Combat Joueur contre Joueur
                    On choisit le mode de combat: Dresseur contre IA ou contre l'autre personne réelle
                    0 est Joueur contre Joueur, 1 est Joueur contre IA.
                    """
                    while True:
                        # Choisir le combat homme-machine 1 et le combat du joueur 0
                        opera2 = input("Quel type de Combat JCJ voulez vous jouer ?\
                                       \n0,Combat Humain contre Humain\
                                       \n1,Combat Humain contre Ordinateur")
                        if opera2 == "0": 
                            """
                            Nous entrons dans le mode joueur contre joueur.
                            Il faut votre adversaire instancier un autre dresseur, c'est à dire:
                            saisit son nom, choisit ses pokémons initiaux et son deck.
                            """
                            print(" "), print("Il faut Dressuer N°2 choisir ses Pokemons initiaux et son Deck")
                            nom, deck, tousVosPokemons = creerNouveauDresseur(TousPokemons_N3) # Instancier un nouveau dresseur 
                            dressuerN2 = Dresseur(nom, deck, tousVosPokemons ) 
                            combatjcj = CombatJCJ(self, dressuerN2) # Commencer le combat avec dresseurN2
                            combatjcj.tour_par_tour() # Utiliser la fonction "tout_par_tour" dérouler le combat
                            break
                        elif opera2 == "1": # Combat Humain contre Ordinateur
                            """
                            Nous entrons dans le mode joueur contre IA.
                            On choisit la difficulté de IA, et en fonction de la difficulté, on fait le différent combat 
                            """
                            while True:
                                opera3 = input("Choisissez-vous le niveau de difféculté de l'Ordinateur (0-2):") 
                                # Vérifier d'abord le commande est acceptable
                                if opera3.isdecimal() and int(opera3) >= 0 and int(opera3)<3:  
                                    opera3 = int(opera3)
                                    nom = "ORDINATEUR" 
                                    print("Le niveau de difficulté est {}".format(opera3)) # Affichez Le niveau de difficulté
                                    if opera3 == 0: 
                                        # Niveau 0: Sélectionner aléatoirement 6 Pokémons niveau 1
                                        tousVosPokemons = random.sample(PokeNiveau1_N3,6)
                                        deck = random.sample(tousVosPokemons ,3)
                                        dressuerN2 =  IA(nom, deck, tousVosPokemons,opera3 ) #Instancier IA
                                    elif opera3 == 1: 
                                        # Niveau 1: Sélectionner aléatoirement 6 Pokémons niveau 6
                                        tousVosPokemons = random.sample(PokeNiveau6_N3,6)
                                        deck = random.sample(tousVosPokemons,3)
                                        dressuerN2 =  IA(nom, deck, tousVosPokemons, opera3 )
                                    elif opera3 == 2: 
                                        # Niveau 1: Sélectionner aléatoirement 6 Pokémons niveau 10
                                        tousVosPokemons = random.sample(PokeNiveau10_N3,6)
                                        deck = random.sample(tousVosPokemons,3)
                                        dressuerN2 =  IA(nom, deck, tousVosPokemons, opera3 )
                                    combatjcj = CombatJCJ(self, dressuerN2) #Instancier le Combat
                                    combatjcj.HumainvsOrdi()                #Commencer le Combat
                                    flag = False
                                    break
                                else:
                                    print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")    
                        else:
                            print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
                        if not flag : 
                            break
                elif opera == "5":      # Creezeun nouveau dresseur
                    self.sauvegarder()  # Stocker le dresseur actuel
                    # Utilisez la fonction "creerNouveauDresseur" pour créer un nouveau dresseur
                    nom, deck, tousVosPokemons = creerNouveauDresseur(TousPokemons) 
                    self = Dresseur(nom, deck, tousVosPokemons)   # Initialiser ce nouveau dresseur
                elif opera == "6":     # Exit 
                    self.sauvegarder() # Souvgarder des informations
                    print("Au revoir!  à bientôt!!!") 
                    quitter()          # la fonction "quitter" permet de quitter le programme
                elif opera =="7":      # Sauvgarder
                    self.sauvegarder()
                    print("Bien souvgarder !")
                else:
                    print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
            else:
                print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
                
#%% La classe de l'IA
class IA(Dresseur):
    """
    La classe de IA est une classe hérite de dresseur. Dans cette class, on définit
    les fonctions de IA en fonction des différentes difficultés. IA est une sous-classe de Dresseur, 
    il hérite tous les variables de Dresseur, et il poccède aussi les variables privés comme "la difficulté", 
    afin que IA puisse être effectué selon son difficulté.
    """
    def __init__(self, nom, deck, touslesPokemons, difficulte):
        super().__init__(nom, deck, touslesPokemons)
        self.__difficulte = difficulte # le niveau de la difficulté d'IA

    @property
    def difficulte(self): return self.__difficulte
    @difficulte.setter
    def difficulte(self, difficulte):  self.__difficulte = difficulte
    
    # Choisissez le premier Pokémon à faire le combattre
    def choisirPokeDepart (self):
        """
        Cette fonction permet de choisit le premier Pokémon à faire le combat en fonction de difficulté. 
        On implémente deux méthodes pour choisir ce pokémon:  quand la difficulté est 0, IA choisit 
        aléatoirement un pokémon de deck. Quand la difféculté est supérieure que 0, IA compare le niveau 
        de pokémon dans son deck, et choisit celui avec le plus haut niveau. Enfin, cette fonction retoure
        le premier Pokémon à faire le combat.
        """
        # Créer une liste qui contient les pokémon disponibles.
         # vérifier les Pokémons dont la vie n'est pas nulle
        pokemonDispo = [i for i in self.deck if i.vie != 0]   
# =============================================================================
#         for i in self.deck: # vérifier les Pokémons dont la vie n'est pas nulle
#             if i.vie != 0:
#                 pokemonDispo.append(i)    
# =============================================================================
        if self.__difficulte == 0 or "0":
            pokemonDepart = pokemonDispo[random.randint(0, len(pokemonDispo)-1)]  # choisir aléatoirement un Pokémon
        else:
            #comparer le niveau de pokémon dans le deck, et choisit celui avec le plus haut niveau.
            pokemonDepart = pokemonDispo[0] 
            for i in pokemonDispo:
                if i.niveau > pokemonDepart.niveau: 
                    pokemonDepart = i
        return pokemonDepart
    
    def changerPokemon(self, pokemon):
        """
        Cette fonction permet IA changer son pokémon à faire le combat, différent que la classe"dresseur", 
        il faut reécrire cette foncion. Enfin, il retourner un pokémon à faire le combat. l'entrée "pokemon"
        représente le pokémon qui est en train de faire le combat.
        """
        pokemonDispo = []   # Créer une liste qui contient les pokémons disponibles
        for i in self.deck:
            # Si la pokémon n'est pas le pokémon actuel qui est en train de faire le combat, on le ajooute dans 
            # la liste "pokemonDispo". 
            if i.vie != 0 and i!=pokemon: 
                pokemonDispo.append(i)
        #Après le boucle ci-dessous, si la liste"pokemonDispo" n'est pas vide, IA choisit un pkémon aléatoirement.      
        if pokemonDispo:
            pokemon = random.sample(pokemonDispo, 1) 
            print("Pokemon de {0} actuel est {1}".format(self.nom, pokemon.nom))
            return pokemon
    
    # La fonction pour utiliser les compétences
    def utiliserCompetence (self, pokemon, but):
        """
        L'entrée "pokemon" représente son pokemon qui est en train de faire le combat, et "but" 
        représente la cible de la compétence d'attaque. 
        Il y aura différentes manières d'utiliser des compétences pour différentes difficultés IA.
        Pour Niveau 0, IA utiliser aléatoirement les compétences. 
        """
        if self.difficulte == 0: 
            compeUtilise = pokemon.competence[random.randint(0, len(pokemon.competence)-1)] 
            pokemon.utiliserCompet(compeUtilise, but) # rappeler la fonciton "utiliserCompet" pour utiliser la compétence
        """
        IA déterminera d'abord si sa vie est inférieure à 20% de vie maximale, et si oui, recherchez la barre 
        de compétences pour voir s'il existe une compétence qui restaure la vie, et utilisez-la.
        Si non, IA déterminera si son énergie est inférieure à 20% d' énergie maximale, et si oui, recherchez la barre 
        de compétences pour trouver une compétence qui restaure l'énergie, et utilisez-la.
        Si les conditions ci-dessus ne sont pas remplies, la compétence attaque sera utilisée au hasard.
        """
        if self.difficulte == 1: 
            flag = True 
            while True:
                if pokemon.vie < (0.2*pokemon.vie_max):        # Si la vie du Pokémon est inférieure à 20% de vie maximale
                    for i in pokemon.competence:
                        if isinstance(i, CompetenceDefence) and i.soin !=0:   # Chercher la compétence qui restaure la vie.
                            pokemon.utiliserCompet(i, but)     # Si oui, utiliser-la
                            flag = False
                            break
                    if not flag: break
                
                if pokemon.energie <(0.2*pokemon.energie_max):  # Si l'energie du Pokémon est inférieure à 20% d'énergie maximale
                    for i in pokemon.competence:
                        if isinstance(i, CompetenceDefence) and i.energie !=0: # Chercher la compétence qui restaure l'énergie.
                            pokemon.utiliserCompet(i, but)      # Si oui, utiliser-la
                            flag = False
                            break
                    if not flag: break
                #Créer une liste qui contient les competences attaques et chercher les compétences attaques
                compeAttaque = [i for i in pokemon.competence if isinstance(i, CompetenceAttaque)]             
# =============================================================================
#                 for i in pokemon.competence:  #
#                     if isinstance(i, CompetenceAttaque): 
#                        compeAttaque.append(i)  
# =============================================================================
                compeUtilise = compeAttaque[random.randint(0, len(compeAttaque)-1)] # Choisir au hasard une compétence attaque
                pokemon.utiliserCompet(compeUtilise, but)
                break
        """
        le niveau 2 fait quelques améliorations sur la base du niveau 1: IA détermine d'abord si sa vie est inférieure à 40% 
        de vie maximale.De plus, IA ne décide plus d'utiliser ou non la compétence de régénération de l'énergie en fonction 
        de la valeur d'énergie restante,mais vérifiera d'abord si son énergie restante est suffisante pour utiliser une compétence 
        d'attaque. Si oui, il choisit la compétence d'attaque la plus puissantes. De plus, IA changera également le Pokémon en fonction 
        de la situation.
        """
        if self.difficulte == 2: 
           flag = True 
           while True:
                if pokemon.vie <0.4*pokemon.vie_max:
                    for i in pokemon.competence:
                        if isinstance(i, CompetenceDefence) and i.soin !=0: 
                            pokemon.utiliserCompet(i, but) 
                            flag = False
                            break
                    if not flag: break
                # Créer une liste qui contient les competences attaques et 
                # récupérer les compétences qui peuvent être utilisé en fonction d'énergie restante 
                compeAttaqueDispo = [i for i in pokemon.competence if i.cout < pokemon.energie \
                                     and isinstance(i,CompetenceAttaque)]          
# =============================================================================
#                 for i in pokemon.competence:# Récupérer les compétences qui peuvent être utilisé en fonction d'énergie restante 
#                     if i.cout < pokemon.energie and isinstance(i,CompetenceAttaque): 
#                         compeAttaqueDispo.append(i)
# =============================================================================
                if compeAttaqueDispo:           # Si la liste de compétence disponible n'est pas vide
                    compeUtilise = compeAttaqueDispo[0]       
                    for i in compeAttaqueDispo: # Choisir les compétences les plus puissantes dans cette liste
                        if i.puissance > compeUtilise.puissance:
                            compeUtilise = i
                    pokemon.utiliserCompet(compeUtilise, but) # Utiliser-la
                    break
                else: # Si l'énergie restante n'est pas suffisante pour effecter une compétence attaque, régénérer l'énergie!
                    for i in pokemon.competence: 
                        if isinstance(i, CompetenceDefence) and i.energie !=0:
                            pokemon.utiliserCompet(i, but)  
                            flag = False
                            break
                    if not flag: break
                    # Si aucune des conditions ci-dessus n'est remplie (Pokémon ne peut pas régénérer HP, l'énergie,
                    # et utiliser de compétence d'attaque), IA remplacera Pokémon.
                    pokemonDispo = [i for i in self.deck if i.vie != 0 and i!= pokemon ]
# =============================================================================
#                     for i in self.deck:
#                         if i.vie != 0 and i!= pokemon:
#                             pokemonDispo.append(i) 
# =============================================================================
                    if pokemonDispo: # Si cette liste n'est pas vide
                        pokemon = random.sample(pokemonDispo, 1)# Sélectionner au hasard un Pokémon dans la liste 
                        print("{} change son pokemon".format(self.nom)) 
                        print("Pokemon de {0} actuel est {1}".format(self.nom, pokemon.nom))
                        return pokemon
                    else: #Si IA n'a même pas de Pokémon disponible, alors il juste fait quelque chose au hasard...
                        compeUtilise = pokemon.competence[random.randint(0, len(pokemon.competence)-1)] 
                        pokemon.utiliserCompet(compeUtilise, but)
                        break
#%% La classe de Pokemopn
class Pokemon:
    def __init__(self, nom, elem, niveau, exp, vie, energie, regene, resist, competence, apres_evolution):
        self.__nom = nom     # le nom du Pokemon
        self.__elem = elem   # L'élement du Pokemon
        self.__niveau = int(niveau)           # Le niveau du Pokemon 
        self.__niveau_max = self.__niveau + 5 # Le niveau maximal actuel du Pokemon
        self.__exp = int(exp)                 # L'expérience du Pokemon
        self.__vie = int(vie)                 # La vie du Pokemon
        self.__energie = int(energie)  # L'énergie du Pokemon
        self.__regene = int(regene)    # La régénération du Pokemon
        self.__resist = int(resist)    # La résistance du Pokemon
        self.__competence = competence # Les compétences du Pokemon
        
        # "self._apres_evolution" est un object, qui représente le Pokémon évolué du Pokémon actuel.
        # Si ce Pokémon ne peut pas continuer à évoluer, alors "self._apres_evolution" = None.
        self.__apres_evolution = apres_evolution 
        # Obtenir la position du Pokémon dans la liste de tous les pokémons
        self.__numero = pokemon_nom.index(self.__nom)   
        
        # Conserver la valeur de vie maximale et d'énergie maximale 
        # Il sert à restaurer la vie et l'énergie à maximum avant le Cambat
        self.__vie_max = int(vie)         # La vie maximale du Pokemon 
        self.__energie_max = int(energie) # L'energie maximale du Pokemon
        
    @property
    def nom (self): return  self.__nom
    @property
    def elem (self): return  self.__elem
    @property
    def niveau (self): return  self.__niveau
    @property 
    def exp (self) : return self.__exp
    @property
    def vie (self): return  self.__vie
    @property
    def energie (self): return  self.__energie
    @property 
    def regene (self) : return self.__regene
    @property
    def resist (self): return  self.__resist
    @property
    def competence(self): return self.__competence
    @property
    def vie_max(self) : return self.__vie_max
    @property
    def energie_max(self) : return self.__energie_max
    @property 
    def apres_evolution(self): return self.__apres_evolution
    @property 
    def numero(self): return self.__numero
    
    @vie.setter
    def vie (self, vie): self.__vie = vie
    @energie.setter 
    def energie(self, energie) : self.__energie = energie
    @vie_max.setter
    def vie_max (self, vie_max): self.__vie_max = vie_max
    @energie_max.setter 
    def energie_max(self, energie_max) : self.__energie_max = energie_max
    @regene.setter 
    def regene(self, regene) : self.__regene = regene
    @resist.setter 
    def resist(self, resist) : self.__resist = resist
    @competence.setter
    def competence(self, competence):self.__competence = competence
    @exp.setter
    def exp(self, exp): self.__exp = exp
    @niveau.setter 
    def niveau(self,niveau): self.__niveau = niveau 
    @apres_evolution.setter 
    def apres_evolution(self, apres_evolution): self.__apres_evolution = apres_evolution
    
    #Cette fonction permet de comparer l'objet pokémon
    def __eq__(self, other):
        if not isinstance(other,Pokemon): return False
        if self is other:                 return True
        
    # La fonction permet d'afficher le nom de chaque compétence qui sert à la fonction "__str__".
    def nomCompetence(self):
        nomCompetence = "[" 
        nomCompetence+= ", ".join(i.nom for i in self.__competence)
        nomCompetence += "]"
        return nomCompetence
    
    # La fonciton pour afficher les informations de Pokémon
    def __str__(self):
        res = "{0} (LvI {1}, Exp {2}/100, {3}):Vie {4}/{5}, Energis {6}/{7} (+{8}), Resistance {9}, avec competence: {10} "\
                .format(self.__nom, self.__niveau, self.__exp, self.__elem, self.__vie, self.__vie_max, self.__energie, \
                        self.__energie_max, self.__regene, self.__resist, self.nomCompetence())
        return res
    
    def augementerNiveau(self):
        """
        Cette fonction permet d'augementer le niveau du pokémon, de même, il augemente la vie, l'énergie, etc. du Pokémon 
        si l'expérience du Pokémon atteint maximal. On vérifie l'expérience atteint 100 et le pokémon peut continuer à 
        augmenter son niveau. Si le niveau atteint niveau max, il faut évoluer!
        """
        if self.__exp >= 100 and self.__niveau <= self.__niveau_max : 
            self.__niveau += 1  # le niveau plus 1
            self.__exp = 0      # l'expérience réinitialiser à zéro
            self.__vie_max += vie_upgrade[self.__numero] # Augmentation de la vie maximale
            self.__vie = self.__vie_max   # Augmentation de la vie 
 
            self.__energie_max += energie_upgrade[self.__numero] # Augmentation de l'énergie maximale 
            self.__energie = self.__energie_max                  # Augmentation de l'energie
            self.__regene += regene_upgrade[self.__numero]       # Augmentation de la régénération maximale
            self.__resist += resist_upgrade[self.__numero]       # Augmentation de la résistance maximale
            print("{0} est upgrade ! pour l'instant son niveau est {1}".format(self.__nom, self.__niveau))
    
    # La fonction pour set damage
    def setDamage(self, dmg):
        """
        La fonction servit de prendre des dégâts et déduire son propre vie.
        l'éntrée "dmg" représente le dégat
        """
        self.__vie -= dmg  # déduire son vie
        # Si la vie est inférieure à 0, la vie est zéro
        if self.__vie < 0: self.__vie = 0 
    
    def sethealing(self, healing):
        """
        La fonction pour restaurer la vie, l'éntrée "healing" représente la valeur de régénération de vie
        """
        self.__vie += healing 
        # Si la vie de Pokémon est superieur à la vie maximale, la vie = la vie maximale
        if self.__vie > self.__vie_max:  self.__vie = self.__vie_max 
    
    def setRegenEnergie(self, regene) :
        """
        Même que la fonction précédente, cette fonciton servit à la régénération de l'énergie
        """
        self.__energie += regene 
        if self.__energie > self.__energie_max: self.__energie = self.__energie_max 

    def gangerExperienceJCE(self, pokemonvaincus):
        """
        Selon la formule, calculer l'expérience gagnée, l'éntrée "pokemonvaincus" représente le pokémon vaincu
        De plus, afin de mieux ressentir l'effet de l'augementation de niveau, nous avons 
        légèrement modifié la valeur de la formule. 
        """
        exp_gagner = round((300 + pokemonvaincus.niveau - self.__niveau)/3)
        self.__exp +=  exp_gagner  # mettre à jour l'expérience
        print("{0} a gagné exp: {1}. Son experience actuel est {2}".format(self.__nom, exp_gagner,  self.__exp)) 
    
   
    def gangerExperienceJCJ(self, playervaincus):
        """
        De même, cette fonction servit à gagner l'expérience dans mode Cambat JCJ
        """
        exp_gagner =  round(300 + (playervaincus.deck[0].niveau + playervaincus.deck[1].niveau \
                                + playervaincus.deck[2].niveau)/3 - self.__niveau)
        self.__exp +=  exp_gagner # mettre à jour la nouvelle l'expérience
        print("{0} a gagné exp: {1}. Son experience actuel est {2}".format(self.__nom, exp_gagner,  self.__exp)) 
    # La methode pour les Pokémon utilisent des compétences 
    def utiliserCompet(self, competence, pokemon2):
        """
        Fonciton pour utiliser la conmétence, l'éntrée "competence" représente la compétence utilisé, 
        "pokemon2" représente la cible de la compétence d'attaque.
        On détermine d'abord si l'énergie est suffiante pour cette compétence, si non,print "Pas assez d'énergie" 
        et passer son tour. Si oui, on le utilise en fonciton son type (Attque ou défence). 
        """
        if competence.cout > self.__energie:  # Vérifiez si la compétence peut être utilisée
            print("Pas assez d'énergie ! Veuillez attendre la regénération d'énergie")
        else: 
            self.__energie = self.__energie - competence.cout # L'énergie moins le coût de compétence
            if isinstance(competence, CompetenceAttaque):     # Vérifier si la compétence est une compétence d'attaque
                degat = competence.utilisation(pokemon2.resist, self.__elem, self.__niveau) # Si oui, calculer le dégat
                pokemon2.setDamage(degat)                     # Set le dégat à la cible
                print(" ")                                    # Afficher les informations 
                print("{0} a utilisé {1}".format(self.nom,  competence.nom))
                print("{0} avez fait le dégat de {1} à {2}".format(self.__nom, degat, pokemon2.nom))
                print("Pour l'instant, la vie de {0} est {1}".format(pokemon2.nom,pokemon2.vie ))
            else: # Vérifier si la compétence est une compétence defense
                soin, energie = competence.utilisation()      # Calculer la valeur de la régénération de vie ou/et d'énergie.
                self.setRegenEnergie(energie)                 # Régénérer l'énergie
                self.sethealing(soin)                         # Régénérer la vie
                print("{0} a utilisé {1}".format(self.nom,  competence.nom)) # Afficher les informations 
                print("{0} a fait traitement de {1}, et obtenu energie de {2}".format(self.__nom, soin, energie))
                print("Pour l'instant sa vie est {0}, son énergie est {1}".format(self.__vie, self.__energie))
                
#%% La classe de Combat 
class Combat(ABC):
    """
    Cette une classe abstraite car on ne l'instantcie jamais. Dans cette class, 
    il implémente trois méthodes arbitraires, "tour_par_tour" servit à dérouler le combat, 
    "regen_max" pour tous les Pokemons commencent le combat avec leur vie et énergie au maximum.
    "debutCombat" servit à afficher les informations de Cambat et permet les dresseurs choisissent ses
    pokémon à faire le combat. 
    """
    def __init__(self, dresseur):
        self.__dresseur = dresseur
    @property
    def dresseur(self): return self.__dresseur 
    @dresseur.setter 
    def dresseur(self, dresseur): self.__dresseur  = dresseur
    
    @abstractmethod
    def tour_par_tour(self): pass
    @abstractmethod
    def regen_max(self):pass
    @abstractmethod
    def debutCombat (self) :pass

    def regen_energie_automatique(self, PokemonN1,PokemonN2 ):
        """
        À la fin de chaque tour, Pokémon restaurera automatiquement une certaine quantité d'énergie.
        les éntrées "PokemonN1" et "PokemonN2" représentent les deux pokémons qui fait le combat.
        """
        print("A la fin de chaque tour, les Pokémons régénèrent certaines quentité de l'énergie automatiquement")
        print("Leur energies actuelles sont: {0}: {1}, {2}: {3}"\
              .format(PokemonN1.nom, PokemonN1.energie, PokemonN2.nom, PokemonN2.energie))
        PokemonN1.energie += PokemonN1.regene
        if PokemonN1.energie > PokemonN1.energie_max:  # Vérifier si l'énergie est l'énergie maximale
            PokemonN1.energie = PokemonN1.energie_max  # Quand l'énergie est supérieure à l'énergie max, l'énergie = l'énergie max
        PokemonN2 .energie += PokemonN2 .regene
        if PokemonN2 .energie> PokemonN2 .energie_max:  
            PokemonN2 .energie = PokemonN2 .energie_max
        print("Après regénération, Leur energies sont {0}: {1}, {2}: {3}"\
              .format(PokemonN1.nom, PokemonN1.energie, PokemonN2.nom, PokemonN2.energie))
        
#%% La classe de CombatJCJ        
class CombatJCJ(Combat):
    """
    La class CombatJcJ hérite la classe Combat. 
    Sauf le dresseur "vous", il faut déclare un autre attribut "dressuer2" comme votre adversaire.
    """
    def __init__(self, dresseur, dressuer2):
        super().__init__(dresseur)
        self.__dresseur2 = dressuer2
        
    @property
    def dresseur2(self): return self.__dresseur2 
    @dresseur2.setter 
    def dresseur2(self, dresseur2): self.__dresseur2  = dresseur2
    
    def regen_max(self):
        """
        Comme expliquer dans la class "Combat", cette fonction permet tous les Pokemons
        commencent le combat avec leur vie et énergie au maximum.
        """
        for i in range (len(self.dresseur.deck)):
            self.dresseur.deck[i].vie = self.dresseur.deck[i].vie_max         # Restaurer la vie en vie maximale du dresseur1
            self.dresseur.deck[i].energie = self.dresseur.deck[i].energie_max # Restaurer l'énergie en énergie maximale du dresseur1
            self.__dresseur2.deck[i].vie = self.__dresseur2.deck[i].vie_max   # Restaurer la vie en vie maximale du dresseur2
            self.__dresseur2.deck[i].energie = self.__dresseur2.deck[i].energie_max # Restaurer l'énergie en énergie maximale du dresseur2
    
    def debutCombat (self):
        """
        Cette fonciton affiche les informations de Cambat au début du combat et permet les dresseurs choisissent 
        leur pokémon à faire le combat.
        Enfin, cette fonction return les deux pokémons choisit à faire le combat
        """
        print("Combat JCJ commence, |{0}|  ===VS===  |{1}|"\
              .format(self.dresseur.nom, self.__dresseur2.nom)), print(" ")
        print("{0} choisit son pokemon qui fait le combat : (0-2)"\
              .format(self.dresseur.nom)), time.sleep(0.5), print(" ")
        # Dresseur 1 choisit son pokémon à faire le combat
        while True:
            self.dresseur.voirdeck(), time.sleep(0.5) #Afficher les pokémons dans la deck
            opera = input() 
            if opera.isdecimal() and (opera == "0" or opera == "1" or opera == "2"): # Assurer l'entrée est correcte 
                time.sleep(0.5), print(" ")
                break
# =============================================================================
#                 if opera == "0" or opera == "1" or opera == "2":
#                     time.sleep(0.5), print(" ")
#                     break
#                 else:
#                     print("\n-------------------\nInvalide! Ressayer!\n-------------------\n"), print(" ")
# =============================================================================
            else:
                 print("\n-------------------\nInvalide! Ressayer!\n-------------------\n"), print(" ")
        print("{0} choisit son pokemon qui fait le combat : (0-2)".format(self.__dresseur2.nom)), time.sleep(0.5), print(" ")
        # Dresseur 2 choisit son pokémon à faire le combat
        while True:
            self.__dresseur2.voirdeck(), time.sleep(0.5)
            opera2 = input()
            if opera2.isdecimal() and (opera2 == "0" or opera2 == "1" or opera2 == "2"): # Assurer l'entrée est correcte 
                time.sleep(0.5)
                break
# =============================================================================
#                 if opera2 == "0" or opera2 == "1" or opera2 == "2":
#                     time.sleep(0.5)
#                     break
#                 else:
#                     print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
# =============================================================================
            else:
                print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
        return self.dresseur.deck[int(opera)], self.__dresseur2.deck[int(opera2)] 
    
    # La sélection des informations homme-machine dans le combat homme-machine
    def debutCombat_IA (self):
        """
        Le principe de cette fonction est pareil que la fonction précédente, mais il sert à mode Combat Humain contre Ordinateur
        
        """
        print("Combat JCJ commence, |{0}|  ===VS===  |{1}|"\
              .format(self.dresseur.nom, self.__dresseur2.nom)), print(" ")
        print("Votre enemi est {} avec ses Pokemon: ".format(self.__dresseur2.nom))
        for i in self.__dresseur2.deck: print(i)
        print(" ")
        print("{0} choisit son pokemon qui fait le combat: (0-2)"\
              .format(self.dresseur.nom)), time.sleep(0.5), print(" ")
        while True:
            self.dresseur.voirdeck(), time.sleep(0.5)
            opera = input()
            if opera.isdecimal() and (opera == "0" or opera == "1" or opera == "2"):
                time.sleep(0.5), print(" ")
                break
# =============================================================================
#                 if opera == "0" or opera == "1" or opera == "2":
#                     time.sleep(0.5), print(" ")
#                     break
#                 else:
#                     print("\n-------------------\nInvalide! Ressayer!\n-------------------\n"), print(" ")
# =============================================================================
            else:
                 print("\n-------------------\nInvalide! Ressayer!\n-------------------\n"), print(" ")
        pokemonDepart_IA = self.__dresseur2.choisirPokeDepart() #IA choisit son pokémon en utilisant la fonciotn "choisirPokeDepart"
        return self.dresseur.deck[int(opera)], pokemonDepart_IA
    
    #La fonction déroule le combat Humain contre Humain
    def tour_par_tour(self):
        """
        Fontion déroule le combat Humain contre Humain. Après récupérer les deux pokémons choist à faire le combat, la principale partie
        de la fonction est une boucle : chaque itération le programme affiche le menu d'opération,  un dresseur peut soit utiliser une 
        compétence de son Pokemon actif, soit choisir de remplacer son Pokemon actif par un autre Pokemon de son deck, soit passer son tour
        ou déclarer forfait.
        
        A la fin de chaque itération(tour),  les pokémons restaurent automatiquement une certaine quantité d'énergie.
        
        Le combat s’arrête si les 3 Pokemons du deck d’un des dresseurs sont ko ou si l’un des dresseurs déclare forfait.
        A la fin du combat, les pokémons gagnent l'expérience, évoluent et revient à le meilleur état (Vie, énergie).
        """
        self.regen_max()  ## La fonction pour revenir à le meilleur état du Pokemon
        Pokemon_choisi, Pokemon_choisi2 = self.debutCombat() # On récupérer les deux pokémon choist à faire le combat
        time.sleep(0.5)
        print("la pokemon choisi de {} est {}".format(self.dresseur.nom, Pokemon_choisi.nom)), time.sleep(0.5), print("  ")
        print("la pokemon choisi de {} est {}".format(self.__dresseur2.nom, Pokemon_choisi2.nom)), time.sleep(0.5), print("  ")
        flag = True  # Ces deux petites ""flag" sert à break le boucle
        flag2 = True
        
        for i in range (1000): 
            #Afficher d'abord le menu d'opération du dresseur 1 
            print("=======Tour {}=======".format(i+1)),              time.sleep(0.5), print(" ")
            print("c'est à {0} de jouer".format(self.dresseur.nom)), time.sleep(0.5), print(" ")
            print("le profil de votre pokemon choisit est \n"),      time.sleep(0.5)
            print(Pokemon_choisi), time.sleep(0.5), print(" "),      time.sleep(0.5)
            #Afficher les compétence du pokémon actif du dresseur 1
            for i in range(len(Pokemon_choisi.competence)):
                print('{0}.{1}\n'.format(i, Pokemon_choisi.competence[i]))
            time.sleep(0.5)    
            #Afficher les opérations de changer de Pokémon actif, de passer le tour et de fuir le combat
            print("{0}.Changer Pokemon\n" "\n{1}.Passser votre tour\n" "\n{2}.Fuir le combat"\
                  .format(len(Pokemon_choisi.competence), len(Pokemon_choisi.competence)+1, len(Pokemon_choisi.competence)+2))
            print(" "), time.sleep(0.5)
            #Dresseur fait son opération
            while True:
                opera2 = input("Qu'est ce que vous voulez faire :")
                time.sleep(0.5)
                # Vérifier d'abord que le command est acceptable
                if opera2.isdecimal() and int(opera2)>=0 and int(opera2) <=len(Pokemon_choisi.competence)+3:
                    opera2 = int(opera2) 
                    if opera2 < len(Pokemon_choisi.competence):       # Si le commande est l'utilisation de compétence, donc utiliser-la
                        Pokemon_choisi.utiliserCompet(Pokemon_choisi.competence[opera2], Pokemon_choisi2)
                        break
                    elif opera2 == (len(Pokemon_choisi.competence)):  #En utilisant la fonction "changerPokemon" pour changer pokémon
                        print("Votre Pokemon actuelle est {}".format(Pokemon_choisi.nom)), print(" "), time.sleep(0.5)
                        Pokemon_choisi = self.dresseur.changerPokemon()
                        break
                    elif opera2 == (len(Pokemon_choisi.competence)+1):#Passer le tour 
                        print("Vous avez passé votre tour !")
                        break
                    else: # déclarer forfait
                        print("{0} est un loser!!!!!!!!!!!!!, {1} gagne le combat".format(self.dresseur.nom, self.__dresseur2.nom))
                        flag = False
                        # Si dresseur 1 échoue son combat, les pokemons du dresseur 2 gagnent l'éxpérience et évoluent.
                        for i in self.__dresseur2.deck:
                            i.gangerExperienceJCJ(self.dresseur)
                            i.augementerNiveau()
                            print(" ")
                        self.__dresseur2.evolution()
                        break
                else:
                    print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
            if not flag:
                break
            print(" "), time.sleep(0.5)
            #A la fin du tour de dresseur 1, on vérifier si la vie du pokémon actif du dresseur 2 = 0 ou pas,
            #Si oui et si il a encore des autres pokémons disponible, alores changer pokémon et continuer.
            #Si non, le combat termine, les pokémon du dresseur 1 gagnent l'exp, augmentent niveau, évoluent.
            if  Pokemon_choisi2.vie == 0:
                print("{0} de {1} est été KO".format(Pokemon_choisi2.nom, self.__dresseur2.nom))
                # Verifier si il y a d'autre pokémon disponible
                if self.__dresseur2.deck[0].vie == 0 and self.__dresseur2.deck[1].vie == 0 and self.__dresseur2.deck[2].vie == 0 :
                    print ("Tous les Pokemons de {0} sont été KO, {0} perd le combat!, {1} gange le combat !"\
                           .format(self.__dresseur2.nom, self.dresseur.nom))
                    print("Le combat se termine")
                    for i in self.dresseur.deck: #les pokémon du dresseur 1 gagnent l'exp, augmentent niveau, évoluent.
                        i.gangerExperienceJCJ(self.__dresseur2)
                        i.augementerNiveau()
                        print(" ")
                    self.dresseur.evolution()
                    break
                else: #Else, changer le pokémon actif et continuer
                    print("Il faut choisir un autre pokemon pour continuer le combat")
                    Pokemon_choisi2 = self.dresseur2.changerPokemon()
                    print("{0} choisit {1} pour continue le combat".format(self.__dresseur2.nom, Pokemon_choisi2.nom))
            """
            Ensuite, c'est la tour du dresseur 2. Il est tout à fait la même chose que la tour du dresseur 1.
            Après la tour du dresseur 1, elle passera automatiquement à la tour du joueur 2. 
            """
            print("c'est à {0} de jouer".format(self.__dresseur2.nom)), print(" "), time.sleep(0.5)
            print("le profil de votre pokemon choisit est\n "),                     time.sleep(0.5)
            print(Pokemon_choisi2),                                     print(" "), time.sleep(0.5)
            #Afficher les compétence du pokémon actif du dresseur 2
            for i in range(len(Pokemon_choisi2.competence)):
                print('{0}.{1}\n'.format(i, Pokemon_choisi2.competence[i]))
            time.sleep(0.5)    
            #Afficher les opérations de changer de Pokémon actif, de passer le tour et de fuir le combat
            print("{0}.Changer Pokemon\n" "\n{1}.Passser votre tour\n" "\n{2}.Fuir le combat"\
                  .format(len(Pokemon_choisi2.competence), len(Pokemon_choisi2.competence)+1, len(Pokemon_choisi2.competence)+2))
            print(" "), time.sleep(0.5)
            while True:
                opera5 = input("Qu'est ce que vous voulez faire :")
                time.sleep(0.5)
                # Vérifier d'abord que le command est acceptable
                if opera5.isdecimal() and int(opera5)>=0 and int(opera5) <=len(Pokemon_choisi2.competence)+3:
                    opera5 = int(opera5)
                    if opera5 < len(Pokemon_choisi2.competence): # Si le commande est l'utilisation de compétence, donc utiliser-la
                        Pokemon_choisi2.utiliserCompet(Pokemon_choisi2.competence[opera5], Pokemon_choisi)
                        break
                    elif opera5 == (len(Pokemon_choisi2.competence)):
                        print("Votre Pokemon actuelle est {}".format(Pokemon_choisi2.nom)), print(" "), time.sleep(0.5)
                        Pokemon_choisi2 = self.dresseur2.changerPokemon()
                        break
                    elif opera5 == (len(Pokemon_choisi2.competence)+1):
                        print("Vous avez passé votre tour !")
                        break
                    else:
                        print("{0} est un loser!!!!!!!!!!!!!, {1} gagne le combat".format(self.dresseur2.nom, self.dresseur.nom))
                        flag2 = False
                        for i in self.dresseur.deck:
                            i.gangerExperienceJCJ(self.__dresseur2)
                            i.augementerNiveau()
                            print(" ")
                        self.dresseur.evolution()
                        break
                else:
                    print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
            if not flag2:
                break
            print(" "), time.sleep(0.5)
            #A la fin du tour de dresseur 2, on vérifier si la vie du pokémon actif du dresseur 1 = 0 ou pas,
            #Si oui et si il a encore des autres pokémons disponible, alores changer pokémon et continuer.
            #Si non, le combat termine, les pokémon du dresseur 2 gagnent l'exp, augmentent niveau, évoluent.
            if  Pokemon_choisi.vie == 0:
                print("{0} de {1} est été KO".format(Pokemon_choisi.nom, self.dresseur.nom))
                if self.dresseur.deck[0].vie == 0 and self.dresseur.deck[1].vie == 0 and self.dresseur.deck[2].vie == 0 :
                    print ("Tous les Pokemons de {0} sont été KO, {0} perd le combat!, {1} gange le combat !"\
                           .format(self.dresseur.nom, self.__dresseur2.nom))
                    print("Le combat se termine")
                    for i in self.__dresseur2.deck:
                        i.gangerExperienceJCJ(self.dresseur)
                        i.augementerNiveau()
                        print(" ")
                    self.__dresseur2.evolution()
                    break
                else:
                    print("Il faut choisir un autre pokemon pour continuer le combat")
                    Pokemon_choisi = self.dresseur.changerPokemon()
                    print("{0} choisit {1} pour continue le combat".format(self.dresseur.nom, Pokemon_choisi.nom))
            #A la fin du tour, les pokémons restaurent automatiquement une certaine quantité d'énergie.     
            print(" "), time.sleep(0.5)
            self.regen_energie_automatique(Pokemon_choisi, Pokemon_choisi2)
            print(" "), time.sleep(0.5)
        #Enfin du combat,  les pokémons revient à le meilleur état.    
        self.regen_max()
        
    # La fonciton déroule le Combat Humain contre Ordinateur 
    def HumainvsOrdi(self):
        """
        Fonction permet de décrouler le combat Humain contre Ordinateur.
        Tout comme la fonciont précédente "tour_par_tour", la partie du dresseur est pareille, mais 
        la partie du dresseur 2 est remplacé par IA. Dans la tour de IA, la class IA et ses fonction contrôlent 
        les opération de IA.
        """
        self.regen_max()
        #On récupére les pokémon actives.
        Pokemon_choisi, Pokemon_choisi2 = self.debutCombat_IA()
        time.sleep(0.5)
        print("la pokemon choisi de {} est {}".format(self.dresseur.nom, Pokemon_choisi.nom)),     time.sleep(0.5), print("  ")
        print("la pokemon choisi de {} est {}".format(self.__dresseur2.nom, Pokemon_choisi2.nom)), time.sleep(0.5), print("  ")
        flag = True
        for i in range (1000): 
            print("=======Tour {}=======".format(i+1)),              print(" "), time.sleep(0.5) 
            print("c'est à {0} de jouer".format(self.dresseur.nom)), print(" "), time.sleep(0.5)
            print("le profil de votre pokemon choisit est \n"),                  time.sleep(0.5)
            print(Pokemon_choisi), time.sleep(0.5),                  print(" "), time.sleep(0.5)
            #Afficher les compétence du pokémon actif du dresseur 1
            for i in range(len(Pokemon_choisi.competence)):
                print('{0}.{1}\n'.format(i, Pokemon_choisi.competence[i]))
            time.sleep(0.5)    
            #Afficher les opérations de changer de Pokémon actif, de passer le tour et de fuir le combat
            print("{0}.Changer Pokemon\n" "\n{1}.Passser votre tour\n" "\n{2}.Fuir le combat"\
                  .format(len(Pokemon_choisi.competence), len(Pokemon_choisi.competence)+1, len(Pokemon_choisi.competence)+2))
            print(" "), time.sleep(0.5)
            #Dresseur fait son opération
            while True:
                opera2 = input("Qu'est ce que vous voulez faire :")
                time.sleep(0.5)
                # Vérifier d'abord que le command est acceptable
                if opera2.isdecimal() and int(opera2)>=0 and int(opera2) <=len(Pokemon_choisi.competence)+3:
                    opera2 = int(opera2)
                    if opera2 < len(Pokemon_choisi.competence):        #Si le commande est l'utilisation de compétence, donc utiliser-la
                        Pokemon_choisi.utiliserCompet(Pokemon_choisi.competence[opera2], Pokemon_choisi2)
                        break
                    elif opera2 == (len(Pokemon_choisi.competence)):   #En utilisant la fonction "changerPokemon" pour changer pokémon
                        Pokemon_choisi = self.dresseur.changerPokemon()
                        break
                    elif opera2 == (len(Pokemon_choisi.competence)+1): #Passer le tour
                        print("Vous avez passé votre tour !")
                        break
                    else: # déclarer forfait
                        print("{0} êtes un loser!!!!!!!!!!!!!, {1} gagne le combat".format(self.dresseur.nom, self.__dresseur2.nom))
                        flag = False
                        # Si dresseur 1 échoue son combat, les pokemons d'IA gagnent l'éxpérience et évoluent.
                        for i in self.__dresseur2.deck:
                            i.gangerExperienceJCJ(self.dresseur)
                            i.augementerNiveau()
                            print(" ")
                        self.__dresseur2.evolution()
                        break
                else:
                    print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
            if not flag:
                break
            print(" "), time.sleep(0.5)
            #A la fin du tour de dresseur 1, on vérifier si la vie du pokémon actif d'IA' = 0 ou pas,
            #Si oui et si il a encore des autres pokémons disponible, alores changer pokémon et continuer.
            #Si non, le combat termine, les pokémon du dresseur 1 gagnent l'exp, augmentent niveau, évoluent.
            if  Pokemon_choisi2.vie == 0:
                print("{0} de {1} est été KO".format(Pokemon_choisi2.nom, self.__dresseur2.nom))
                if self.__dresseur2.deck[0].vie == 0 and self.__dresseur2.deck[1].vie == 0 and self.__dresseur2.deck[2].vie == 0 :
                    print ("Tous les Pokemons de {0} sont été KO, {0} perd le combat!, {1} gange le combat !"\
                           .format(self.__dresseur2.nom, self.dresseur.nom))
                    print("Le combat se termine")
                    for i in self.dresseur.deck:
                        i.gangerExperienceJCJ(self.__dresseur2)
                        i.augementerNiveau()
                        print(" ")
                    self.dresseur.evolution()
                    break
                else: #Else, changer le pokémon actif et continuer
                    print("Il faut choisir un autre pokemon pour continuer le combat")
                    Pokemon_choisi2 = self.dresseur2.choisirPokeDepart()
                    print("{0} choisit {1} pour continue le combat".format(self.__dresseur2.nom, Pokemon_choisi2.nom))
            # Passer à la tour d'IA, IA fait opération en fonction de difficulté        
            self.dresseur2.utiliserCompetence(Pokemon_choisi2, Pokemon_choisi)
            #Avant de passer le tour suivant, il faut tester si le pokemon actif du dresseur peut contuner à combattre
            #Si non, il faut changer le pokémon actif, si la vie tous les pokemons dans deck = 0, alors dresseur
            #échoue le combat.
            if  Pokemon_choisi.vie == 0:
                print(" "), print("Votre pokemon est été KO")
                if self.dresseur.deck[0].vie == 0 and self.dresseur.deck[1].vie == 0 and self.dresseur.deck[2].vie == 0 :
                    print ("Tous vos Pokemons dans Deck sont été KO, vous êtes un loser !")
                    print("Le combat se termine")
                    break
                else:#Changer le pokemon actif
                    print("Il faut choisir un autre pokemon pour continuer le combat")
                    Pokemon_choisi = self.dresseur.changerPokemon()
            #A la fin du tour, les pokémons restaurent automatiquement une certaine quantité d'énergie.         
            print(" "), time.sleep(0.5)
            self.regen_energie_automatique(Pokemon_choisi,Pokemon_choisi2)
            print(" "), time.sleep(0.5)
        #Enfin du combat,  les pokémons revient à le meilleur état.     
        self.regen_max()        
        
#%% La classe de CombatJcE                    
class CombatJcE(Combat):
    
    """
    La class CombatJcE hérite la classe Combat. 
    Sauf le dresseur "vous", il faut déclare un autre attribut "pokemons" qui représente 
    le pokemon sauvage.
    
    Nous avons reécrit les fonctions arbitraire, de plus, nous avons ajouté une fonction "utiliseComp_poke"
    qui permet le pokemon sauvage utilise ses compétence aléatoirement.
    """
    def __init__(self, dresseur, pokemon2):
        super().__init__(dresseur)
        self.__pokemon2 = pokemon2
    
    # On redéfinir la fonciton "regen_max" afin d'adapter la class "CombatJcE"
    def regen_max(self):
        for i in range (len(self.dresseur.deck)):
            self.dresseur.deck[i].vie = self.dresseur.deck[i].vie_max         # Restaurer la vie en vie maximale du dresseur
            self.dresseur.deck[i].energie = self.dresseur.deck[i].energie_max # Restaurer l'énergie en énergie maximale du dresseur
        self.__pokemon2.vie = self.__pokemon2.vie_max                         # Restaurer la vie en vie maximale du pokemon
        self.__pokemon2.energie = self.__pokemon2.energie_max                 # Restaurer l'énergie en énergie maximale du pokemon
    
    # Opération d'IA      
    def utiliseComp_poke(self, but):
        #Fonction permet le pokemon sauvage utilise ses compétence aléatoirement
        compeUtilise = self.__pokemon2.competence[random.randint(0, len(self.__pokemon2.competence)-1)]
        self.__pokemon2.utiliserCompet(compeUtilise, but) # En utilisant la fonciton "utiliserCompet" pour utiliser la compétence

    # Commencer à se battre               
    def debutCombat (self):
        """
        De même, Cette fonciton affiche les informations de Cambat au début du combat et permet le dresseur choisit 
        sa pokémon à faire le combat.
        Enfin, cette fonction return le pokémon actif
        """
        print(" ")
        print("Combat commence, votre adversaire est {}".format(self.__pokemon2.nom))
        print("Veuillez Choisir un pokemon pour combattre : (0-2)"), time.sleep(0.5), print(" ")
        while True:
            self.dresseur.voirdeck(), time.sleep(0.5) #Afficher les informations du pokémon
            opera = input()
            if opera == "0" or opera == "1" or opera == "2": #Vérifier si le command est acceptable
                time.sleep(0.5)
                return self.dresseur.deck[int(opera)]
            else:
                print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")   

    #La fonction déroule le combat dresseur contre pokémon
    def tour_par_tour(self):
        """
        De même, cette fontion déroule le combat dresseur contre pokémon. Après récupérer le pokémons actif, la principale partie
        de la fonction est une boucle : chaque itération le programme affiche le menu d'opération,  le dresseur peut soit utiliser une 
        compétence de son Pokemon actif, soit choisir de remplacer son Pokemon actif par un autre Pokemon de son deck, soit capture 
        le pokémon, soit passer son tour ou déclarer forfait.
        
        Comme le caiher de charge, le dresseur peut essayer de capture le pokémon quand la vie du pokémon descend en-dessous de 20%.
        
        A la fin de chaque itération(tour),  les pokémons restaurent automatiquement une certaine quantité d'énergie.
        
        Le combat s’arrête si les 3 Pokemons du deck du dresseur sont ko ou si l’un des dresseurs déclare forfait ou
        la vie du pokémon sauvage = 0 ou le pokémon été capturé.
        
        A la fin du combat, les pokémons gagnent l'expérience, évoluent et revient à le meilleur état (Vie, énergie).
        """
        self.regen_max()
        Pokemon_choisi = self.debutCombat() #Récupérer le pokémon actif
        print("Combat JCE commence, |{0}|  ===VS===  |{1}|"\
               .format(Pokemon_choisi.nom, self.__pokemon2.nom)),  print(" ")
        time.sleep(0.5)
        print("Votre pokemon choisi est {}".format(Pokemon_choisi.nom)), time.sleep(0.5), print(" ")
        flag = True #"flag" permet de break la boucle
        for i in range (1000): 
            #Afficher le menu d'opération du dresseur
            print("=======Tour {}=======".format(i+1)),              time.sleep(0.5), print(" ")
            print("c'est à {0} de jouer".format(self.dresseur.nom)), time.sleep(0.5), print(" "),
            print("le profil de votre pokemon choisit est : "),      time.sleep(0.5), print(" ")
            print(Pokemon_choisi),                                   time.sleep(0.5), print(" ")
            
            for i in range(len(Pokemon_choisi.competence)):
                print('{0},{1}\n'.format(i, Pokemon_choisi.competence[i])), 
            time.sleep(0.5)    

            #Afficher les opérations de capturer le Pokémon, de changer le Pokémon actif, 
            #de passer le tour et de fuir le combat
            print("{0},Changer Pokemon\n" "\n{1},Capturer ce Pokemon\n" "\n{2},Passser votre tour\n" "\n{3},Fuir le combat"\
                  .format(len(Pokemon_choisi.competence), len(Pokemon_choisi.competence)+1, len(Pokemon_choisi.competence)+2, len(Pokemon_choisi.competence)+3))
            print(" "), time.sleep(0.5)
            #Dresseur fait son opération
            while True:
                opera2 = input("Qu'est ce que vous voulez faire :")
                time.sleep(0.5)
                # Vérifier d'abord que le command est acceptable
                if opera2.isdecimal() and int(opera2)>=0 and int(opera2) <= len(Pokemon_choisi.competence)+3:
                    if int(opera2) < len(Pokemon_choisi.competence):      #Si le commande est l'utilisation de compétence, donc utiliser-la
                        Pokemon_choisi.utiliserCompet(Pokemon_choisi.competence[int(opera2)], self.__pokemon2)
                        break
                    elif int(opera2) == (len(Pokemon_choisi.competence)): #En utilisant la fonction "changerPokemon" pour changer pokémon
                        print("Votre Pokemon actuelle est {}".format(Pokemon_choisi.nom)), print(" "), time.sleep(0.5)
                        Pokemon_choisi = self.dresseur.changerPokemon()
                        break
                    elif int(opera2) == (len(Pokemon_choisi.competence)+1):
                        #Afin de capturer le pokémon, il faut d'abord tester si la vie du pokémon descend en-dessous de 20%
                        if self.__pokemon2.vie > 0.2*self.__pokemon2.vie_max:  
                            print("Pas possible! Ressayez quand la vie de Pokemon descend en-dessous de 20% de sa vie max !\n"), time.sleep(1)
                            break
                        else:
                            # Si la condition de limite est satisfait, on peut essayer de le capture. 
                            # Calculer la possibilité de réussite
                            possibilite = 4*(0.2 - self.__pokemon2.vie / self.__pokemon2.vie_max)
                            aleatoire = random.uniform(0,1)
                            if aleatoire <= possibilite:
                                self.dresseur.capturerPokemon(self.__pokemon2) #Réussir à capturer, le combat termine.
                                flag = False
                                break
                            else: # échouer de capturer, le combat continue. 
                                print("Désolé, Capturer echoue !\n"), time.sleep(0.5)
                                break
                    elif int(opera2) == (len(Pokemon_choisi.competence)+2): #Passer la tour
                        print("Vous avez passé votre tour !")
                        break
                    else: # déclarer forfait
                        print("Vous êtes un loser!!!!!!!!!!!!!")
                        flag = False
                        break
                else:
                    print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
            if not flag: 
                break
            print(" "), time.sleep(0.5)
            # A la fin du tour de dresseur, on vérifier si la vie du pokémon= 0 ou pas, si oui le combat termine
            # les pokémon du dresseur gagnent l'exp, augmentent niveau, évoluent.
            if self.__pokemon2.vie == 0:
                print("KO!!! Vous avez gagner le combat!!")
                print("Le combat se termine")
                for i in self.dresseur.deck:
                    i.gangerExperienceJCE(self.__pokemon2)
                    i.augementerNiveau()
                    print(" ")
                self.dresseur.evolution()
                break
            else: #Si non, en utilisant la fonciton "utiliseComp_poke", le pokémon utilise la compétence aléatoire
                print("c'est à {0} de jouer\n{1}".format(self.__pokemon2.nom, self.__pokemon2)), time.sleep(0.5)
                self.utiliseComp_poke(Pokemon_choisi)
            #Avant de passer le tour suivant, il faut tester si le pokemon actif du dresseur peut contuner à combattre
            #Si non, il faut changer le pokémon actif, si la vie tous les pokemons dans deck = 0, alors dresseur
            #échoue le combat.
            if  Pokemon_choisi.vie == 0:
                print("Votre pokemon est été KO")
                if self.dresseur.deck[0].vie == 0 and self.dresseur.deck[1].vie == 0 and self.dresseur.deck[2].vie == 0 :
                    print ("Tous vos Pokemons dans Deck sont été KO, vous êtes un loser !")
                    print("Le combat se termine")
                    break
                else:#Changer le pokemon actif
                    print("Il faut choisir un autre pokemon pour continuer le combat")
                    Pokemon_choisi = self.dresseur.changerPokemon()
            #A la fin du tour, les pokémons restaurent automatiquement une certaine quantité d'énergie.        
            print(" "), time.sleep(0.5)
            self.regen_energie_automatique(Pokemon_choisi, self.__pokemon2 )
            print(" "), time.sleep(0.5)
        #Enfin du combat,  les pokémons revient à le meilleur état.
        self.regen_max()
#%% La classe de Competence （Abstract）    
class Competence(ABC):
    """
    Cette class est la class arbitraire. Dans cette class, il s'agit principalement d'initialiser
    les variables communes et les méthodes communes de ses sous-classes.
    Il déclare deux fonction arbitraire: "utilisation" qui permet d'utiliser ce compétence et 
    "__eq__" permet d'identifier un compétence.
    """
    # Initialiser les variables
    def __init__(self, nom, description, element, cout):
        """
        Les principales variables de compétence sont le nom, la description,l'élément de la compétence 
        et le cout de la compétence.
        """
        self.__nom = nom
        self.__description = description
        self.__element = element
        self.__cout = cout
          
    @property    
    def nom(self):         return self.__nom
    @property    
    def cout(self):        return self.__cout
    @property    
    def description(self): return self.__description
    @property    
    def element(self):     return self.__element    
    
    # Fonction d'affichage des informations
    def __str__(self): 
        res  = "{0}: {1} {2}, cout : {3}".format(self.__nom, self.__description,self.__element,  self.__cout)
        return res
    
    @abstractmethod 
    def utilisation (self):pass
    @abstractmethod 
    def __eq__ (self):     pass

#%% La classe de CompetenceAttaque
class CompetenceAttaque(Competence):
    """
    La class CompetenceAttaque est une class hérite de la class "Competence". Sauf les variables communs, 
    Ses variables privés sont " puissance" et "precision".
    Dans cette class, on redéfinit la fonction "__str__" et déclare la fonction "utilisation" et "__eq__". 
    """
    def __init__(self, nom, description, element, cout, puissance, precision):
        super().__init__(nom, description, element, cout)
        self.__puissance = puissance
        self.__precision = precision
    
    @property
    def puissance(self): return self.__puissance
    @property
    def precision(self): return self.__precision
     
    def __str__(self):
        res = super().__str__()
        res += ", puissance: {0}, precision : {1}".format(self.__puissance, self.__precision)
        return res
    
    def __eq__(self, other):
        if not isinstance(other,CompetenceAttaque): return False
        if self is other:                           return True
        
    # Utilisation des compétences
    def utilisation(self, resist_assailli, elem_Pokemon, niveau_Pokemon): 
        """
        En fonction du caiher de charge, cette fonction permet de calculer de dégat de la compétence atteque.
        Dans un premièr temps, on détermine la réussite de l’attaque, si Miss, on passe directement ce tour.
        Si l'attaque réussie, on calcule les dégats infligés par cette compétence d'attaque.
        
        les entrées:" resist_assailli" représente la résistance du pokémon assailli.
        "elem_Pokemon" représente l'élément du pokémon assailli, "niveau_Pokemon" représente le niveau du pokémon assaillant.
        Enfin, cette fonction return la valeur de dégat(Si Miss, dégat = 0)
        """
        tirage = random.randint(0, 101)
        if tirage > self.__precision:
            print("!!!!!MISS !!!!!")
            degat =  0          # Si Miss, dégat = 0
        else : 
            if self.element == "Air" :
                if elem_Pokemon == "Air":   b = 1
                elif elem_Pokemon == "Eau": b = 1.5
                elif elem_Pokemon == "Feu": b = 0.5
                else:                       b = 1
            elif self.element == "Eau":
                if elem_Pokemon == "Air":   b = 1
                elif elem_Pokemon == "Eau": b = 1
                elif elem_Pokemon == "Feu": b = 0.5
                else:                       b = 1.5
            elif self.element == "Feu":
                if elem_Pokemon == "Air":   b = 0.5
                elif elem_Pokemon == "Eau": b = 1
                elif elem_Pokemon == "Feu": b = 1
                else:                       b = 1.5
            else:
                if elem_Pokemon == "Air":   b = 1.5
                elif elem_Pokemon == "Eau": b = 0.5
                elif elem_Pokemon == "Feu": b = 1
                else:                       b = 1
            cm = b*random.uniform(0.85,1)
            numerateur = self.__puissance * (4 * niveau_Pokemon + 2)
            degat = round(((numerateur/resist_assailli)+2) * cm)
        return degat
#%% La classe de CompetenceDefence   
class CompetenceDefence(Competence):
    """
    Cette classe est une sous-classe de Compétence, de même, sauf les varibles communs, 
    ses varibles privés sont "soin" et "energie" qui représentent la régénération de la vie et l'énergie
    """
    def __init__(self, nom, description, element, soin, energie, cout): 
        super().__init__(nom, description, element, cout)
        self.__soin = soin
        self.__energie = energie
    
    @property
    def soin(self):    return self.__soin
    @property
    def energie(self): return self.__energie
    
    def __str__(self):
        res = super().__str__()
        res += ", soin: {0}, energie : {1}".format(self.__soin, self.__energie)
        return res
    
    def __eq__(self, other):
        if not isinstance(other,CompetenceDefence): return False
        if self is other:                           return True
   
    # Utiliser les compétences
    def utilisation(self):
        """
        Lors de l’utilisation d’une compétence défensive par un Pokemon, on génère un nombre aléatoire compris entre 
        les 2 valeurs données pour déterminer la quantité de vie ou d’énergie restaurée par la compétence.
        """
        soin = random.randint(self.__soin[0], (self.__soin[1]))
        energie = random.randint(self.__energie[0], (self.__energie[1]))
        return soin, energie
#%% Instanciation de CompétenceAttaque
"""
l'instanciation  de chaque compétence attaque.
"""
attaque_object = []
for k in range(len(attaque_nom)):
    attaque_object.append(CompetenceAttaque(attaque_nom[k], attaque_desc[k], attaque_elem[k], attaque_cout[k], attaque_puiss[k], attaque_prec[k]))
    attaque_object[k].name = attaque_nom[k]

#Instanciation de chaque CompétenceAttaques
BecVrille = attaque_object[0]
CageEclair = attaque_object[1]
CruAiles = attaque_object[2]
Eclair = attaque_object[3]
FatalFoudre =  attaque_object[4]
Picpic = attaque_object[5]
Pique = attaque_object[6]
PoingEclair = attaque_object[7]
Tonnerre = attaque_object[8]
Tornade = attaque_object[9]
Vol = attaque_object[10]
Blizzard = attaque_object[11]
BullesdO = attaque_object[12]
Cascade = attaque_object[13]
Claquoir = attaque_object[14]
Ecume = attaque_object[15]
Hydrocanon = attaque_object[16]
LaserGlace = attaque_object[17]
OndeBoreale = attaque_object[18]
PinceMasse = attaque_object[19]
PistoletaO = attaque_object[20]
PoingGlace = attaque_object[21]
Surf = attaque_object[22]
Deflagration = attaque_object[23]
Flammeche = attaque_object[24]
LanceFlammes = attaque_object[25]
PoingFeu = attaque_object[26]
Boutefeu = attaque_object[27]
Canicule = attaque_object[28]
CrocsFeu = attaque_object[29]
FeuSacre = attaque_object[30]
Surchauffe = attaque_object[31]
PiedBruleur = attaque_object[32]
RouedeFeu = attaque_object[33]
JetPierres = attaque_object[34]
BalleGraine = attaque_object[35]
CanonGraine = attaque_object[36]
FouetLianes = attaque_object[37]
Fulmigraine = attaque_object[38]
LameFeuille = attaque_object[39]
Martobois = attaque_object[40]
Eboulement = attaque_object[41]
LamedeRoc = attaque_object[42]
RocBoulet = attaque_object[43]
Roulade = attaque_object[44]
Tomberoche = attaque_object[45]
#%% Instanciation de CompetenceDefence 
"""
l'instanciation  de chaque compétence défense.
"""
Atterrissage = CompetenceDefence(defense_nom[0], defense_desc[0], defense_elem[0], [20,50], [0,0], 10)
PileDuracell = CompetenceDefence(defense_nom[1], defense_desc[1], defense_elem[1], [0,0], [30,60], 0)
AnneauHydro = CompetenceDefence(defense_nom[2], defense_desc[2], defense_elem[2], [30,50], [0,0], 20)
FontainedeVie = CompetenceDefence(defense_nom[3], defense_desc[3], defense_elem[3], [10,30], [0,0], 10)
Aurore = CompetenceDefence(defense_nom[4], defense_desc[4], defense_elem[4], [5,25], [0,0], 5)
Sangchaud = CompetenceDefence(defense_nom[5], defense_desc[5], defense_elem[5], [10,50], [0,0], 10)
PhotoSynthese = CompetenceDefence(defense_nom[6], defense_desc[6], defense_elem[6], [0,0], [30,60], 0)
Racines = CompetenceDefence(defense_nom[7], defense_desc[7], defense_elem[7], [30,50], [30,60], 20)

#%% Instanciation de la liste des joueurs Pokémon
"""
l'instanciation de pokemon, cet ensemble de pokemon est utilisé par "vous", c'est à dire le dresseur.
"""
pokemon_object = []
for k in range(len(pokemon_nom)):
    pokemon_object.append(Pokemon(pokemon_nom[k], liste_element[k], niveau_init[k], 0, (vie_init[k]), energie_init[k], regene_init[k], resist_init[k], liste_competence[k], None))
    pokemon_object[k].name = pokemon_nom[k]

#Instanciation de chaque Pokémon
Pikachu = pokemon_object[0]
Raichu = pokemon_object[1]
Roucool = pokemon_object[2]
Roucoups = pokemon_object[3]
Roucarnage = pokemon_object[4]
Carapuce = pokemon_object[5]
Carabaffe = pokemon_object[6]
Tortank = pokemon_object[7]
Psykokwak = pokemon_object[8]
Akwakwak = pokemon_object[9]
Ptitard = pokemon_object[10]
Tetarte = pokemon_object[11]
Tartard = pokemon_object[12]
Salameche = pokemon_object[13]
Reptincel = pokemon_object[14]
Dracaufeu = pokemon_object[15]
Goupix = pokemon_object[16]
Feunard = pokemon_object[17]
Ponyta = pokemon_object[18]
Galopa = pokemon_object[19]
Bulbizarre = pokemon_object[20]
Herbizarre = pokemon_object[21]
Florizarre = pokemon_object[22]
Sabelette = pokemon_object[23]
Sablaireau = pokemon_object[24]
Nidoran = pokemon_object[25]
Nidorina = pokemon_object[26]
Nidoqueen = pokemon_object[27]

#Définir les compétences de pokemon et leur "object" de "apres_evolution".
Pikachu.competence, Pikachu.apres_evolution = [Eclair,Tonnerre, CageEclair], Raichu
Raichu.competence = [Eclair,Tonnerre, CageEclair, FatalFoudre, PileDuracell]
Roucool.competence, Roucool.apres_evolution= [BecVrille,Vol, Picpic], Roucoups
Roucoups.competence, Roucoups.apres_evolution = [BecVrille,Vol, Picpic, CruAiles], Roucarnage
Roucarnage.competence = [BecVrille,Vol, Picpic, CruAiles, Tornade]
Carapuce.competence, Carapuce.apres_evolution = [BullesdO,Ecume, Surf], Carabaffe
Carabaffe.competence,Carabaffe.apres_evolution  = [BullesdO,Ecume, Surf, Cascade], Tortank
Tortank.competence = [BullesdO,Ecume, Surf, Cascade, Hydrocanon]
Psykokwak.competence, Psykokwak.apres_evolution = [OndeBoreale, PinceMasse,PoingGlace ], Akwakwak
Akwakwak.competence = [OndeBoreale, PinceMasse,PoingGlace ]
Ptitard.competence, Ptitard.apres_evolution = [BullesdO, Ecume, OndeBoreale], Tetarte
Tetarte.competence, Tetarte.apres_evolution = [BullesdO, Ecume, OndeBoreale, PoingGlace], Tartard
Tartard.competence = [BullesdO, Ecume, OndeBoreale, PoingGlace, FontainedeVie]
Salameche.competence, Salameche.apres_evolution = [CrocsFeu, PoingFeu, Flammeche], Reptincel
Reptincel.competence, Reptincel.apres_evolution = [CrocsFeu, PoingFeu, Flammeche, Deflagration], Dracaufeu
Dracaufeu.competence = [CrocsFeu, PoingFeu, Flammeche, Deflagration, LanceFlammes]
Goupix.competence, Goupix.apres_evolution = [PoingFeu, FeuSacre, CrocsFeu], Feunard
Feunard.competence =[PoingFeu, FeuSacre, CrocsFeu, RouedeFeu,Aurore ]
Ponyta.competence, Ponyta.apres_evolution = [Canicule, PiedBruleur, Boutefeu], Galopa
Galopa.competence = [Canicule, PiedBruleur, Boutefeu, RouedeFeu, Sangchaud]
Bulbizarre.competence, Bulbizarre.apres_evolution = [Fulmigraine,CanonGraine, BalleGraine], Herbizarre
Herbizarre.competence, Herbizarre.apres_evolution = [Fulmigraine,CanonGraine, BalleGraine, FouetLianes], Florizarre
Florizarre.competence = [Fulmigraine,CanonGraine, BalleGraine, FouetLianes, LameFeuille]
Sabelette.competence, Sabelette.apres_evolution = [JetPierres,LamedeRoc, RocBoulet ], Sablaireau
Sablaireau.competence = [JetPierres,LamedeRoc, RocBoulet, Tomberoche, Racines ]
Nidoran.competence, Nidoran.apres_evolution = [Roulade,Martobois, Eboulement ], Nidorina
Nidorina.competence, Nidorina.apres_evolution = [Roulade,Martobois, Eboulement, Tomberoche ], Nidoqueen
Nidoqueen.competence = [Roulade,Martobois, Eboulement, Tomberoche, PhotoSynthese ]

#Etablir un ensemble des instances de pokemon
pokemon_object = [Pikachu, Raichu, Roucool,Roucoups, Roucarnage, Carapuce, Carabaffe,\
                  Tortank,Psykokwak, Akwakwak,  Ptitard,Tetarte, Tartard, Salameche,Reptincel,Dracaufeu,\
                      Goupix, Feunard,Ponyta, Galopa, Bulbizarre, Herbizarre, Florizarre, Sabelette, Sablaireau, Nidoran, Nidorina, Nidoqueen ]
TousPokemons = pokemon_object

#Classification des pokemons par rapport à leur niveau initiale
PokeNiveau1 = [Pikachu, Roucool, Carapuce,Psykokwak,Ptitard,Salameche,Goupix,Ponyta, Bulbizarre,Sabelette,Nidoran]
PokeNiveau6 = [Raichu,Roucoups, Carabaffe,Akwakwak,Tetarte,Reptincel,Feunard,Galopa,Herbizarre,Sablaireau,Nidorina]
PokeNiveau10 = [Roucarnage,Tortank,Tartard,Dracaufeu,Florizarre,Nidoqueen]
#%% L'instanciation d'un Pokémon ennemi ou joueur 2
"""
Cet ensemble de pokemon N°2 est utilisé dans le combat Joueur contre pokemon, comme les pokemons sauvages
"""
pokemon_object_N2 = []
for k in range(len(pokemon_nom)):
    pokemon_object_N2.append(Pokemon(pokemon_nom[k], liste_element[k], niveau_init[k], 0, (vie_init[k]), energie_init[k], regene_init[k], resist_init[k], liste_competence[k], None))
    pokemon_object_N2[k].name = pokemon_nom[k]

Pikachu_N2 = pokemon_object_N2[0]
Raichu_N2 = pokemon_object_N2[1]
Roucool_N2 = pokemon_object_N2[2]
Roucoups_N2 = pokemon_object_N2[3]
Roucarnage_N2 = pokemon_object_N2[4]
Carapuce_N2 = pokemon_object_N2[5]
Carabaffe_N2 = pokemon_object_N2[6]
Tortank_N2 = pokemon_object_N2[7]
Psykokwak_N2 = pokemon_object_N2[8]
Akwakwak_N2 = pokemon_object_N2[9]
Ptitard_N2 = pokemon_object_N2[10]
Tetarte_N2 = pokemon_object_N2[11]
Tartard_N2 = pokemon_object_N2[12]
Salameche_N2 = pokemon_object_N2[13]
Reptincel_N2 = pokemon_object_N2[14]
Dracaufeu_N2 = pokemon_object_N2[15]
Goupix_N2 = pokemon_object_N2[16]
Feunard_N2 = pokemon_object_N2[17]
Ponyta_N2 = pokemon_object_N2[18]
Galopa_N2 = pokemon_object_N2[19]
Bulbizarre_N2 = pokemon_object_N2[20]
Herbizarre_N2 = pokemon_object_N2[21]
Florizarre_N2 = pokemon_object_N2[22]
Sabelette_N2 = pokemon_object_N2[23]
Sablaireau_N2 = pokemon_object_N2[24]
Nidoran_N2 = pokemon_object_N2[25]
Nidorina_N2 = pokemon_object_N2[26]
Nidoqueen_N2 = pokemon_object_N2[27]

Pikachu_N2.competence, Pikachu_N2.apres_evolution = [Eclair,Tonnerre, CageEclair], Raichu_N2
Raichu_N2.competence = [Eclair,Tonnerre, CageEclair, FatalFoudre, PileDuracell]
Roucool_N2.competence, Roucool_N2.apres_evolution= [BecVrille,Vol, Picpic], Roucoups_N2
Roucoups_N2.competence, Roucoups_N2.apres_evolution = [BecVrille,Vol, Picpic, CruAiles], Roucarnage_N2
Roucarnage_N2.competence = [BecVrille,Vol, Picpic, CruAiles, Tornade]
Carapuce_N2.competence, Carapuce_N2.apres_evolution = [BullesdO,Ecume, Surf], Carabaffe_N2
Carabaffe_N2.competence,Carabaffe_N2.apres_evolution  = [BullesdO,Ecume, Surf, Cascade], Tortank_N2
Tortank_N2.competence = [BullesdO,Ecume, Surf, Cascade, Hydrocanon]
Psykokwak_N2.competence, Psykokwak_N2.apres_evolution = [OndeBoreale, PinceMasse,PoingGlace ], Akwakwak_N2
Akwakwak_N2.competence = [OndeBoreale, PinceMasse,PoingGlace ]
Ptitard_N2.competence, Ptitard_N2.apres_evolution = [BullesdO, Ecume, OndeBoreale], Tetarte_N2
Tetarte_N2.competence, Tetarte.apres_evolution = [BullesdO, Ecume, OndeBoreale, PoingGlace], Tartard_N2
Tartard_N2.competence = [BullesdO, Ecume, OndeBoreale, PoingGlace, FontainedeVie]
Salameche_N2.competence, Salameche_N2.apres_evolution = [CrocsFeu, PoingFeu, Flammeche], Reptincel_N2
Reptincel_N2.competence, Reptincel_N2.apres_evolution = [CrocsFeu, PoingFeu, Flammeche, Deflagration], Dracaufeu_N2
Dracaufeu_N2.competence = [CrocsFeu, PoingFeu, Flammeche, Deflagration, LanceFlammes]
Goupix_N2.competence, Goupix_N2.apres_evolution = [PoingFeu, FeuSacre, CrocsFeu], Feunard_N2
Feunard_N2.competence =[PoingFeu, FeuSacre, CrocsFeu, RouedeFeu,Aurore ]
Ponyta_N2.competence, Ponyta_N2.apres_evolution = [Canicule, PiedBruleur, Boutefeu], Galopa_N2
Galopa_N2.competence = [Canicule, PiedBruleur, Boutefeu, RouedeFeu, Sangchaud]
Bulbizarre_N2.competence, Bulbizarre_N2.apres_evolution = [Fulmigraine,CanonGraine, BalleGraine], Herbizarre_N2
Herbizarre_N2.competence, Herbizarre_N2.apres_evolution = [Fulmigraine,CanonGraine, BalleGraine, FouetLianes], Florizarre_N2
Florizarre_N2.competence = [Fulmigraine,CanonGraine, BalleGraine, FouetLianes, LameFeuille]
Sabelette_N2.competence, Sabelette_N2.apres_evolution = [JetPierres,LamedeRoc, RocBoulet ], Sablaireau_N2
Sablaireau_N2.competence = [JetPierres,LamedeRoc, RocBoulet, Tomberoche, Racines ]
Nidoran_N2.competence, Nidoran_N2.apres_evolution = [Roulade,Martobois, Eboulement ], Nidorina_N2
Nidorina_N2.competence, Nidorina_N2.apres_evolution = [Roulade,Martobois, Eboulement, Tomberoche ], Nidoqueen_N2
Nidoqueen_N2.competence = [Roulade,Martobois, Eboulement, Tomberoche, PhotoSynthese ]

#Etablir un ensemble des instances de pokemon
pokemon_object_N2 = [Pikachu_N2, Raichu_N2, Roucool_N2,Roucoups_N2, Roucarnage_N2, Carapuce_N2, Carabaffe_N2,\
                  Tortank_N2,Psykokwak_N2, Akwakwak_N2,  Ptitard_N2,Tetarte_N2, Tartard_N2, Salameche_N2,Reptincel_N2,Dracaufeu_N2,\
                      Goupix_N2, Feunard_N2,Ponyta_N2, Galopa_N2, Bulbizarre_N2, Herbizarre_N2, Florizarre_N2, Sabelette_N2, Sablaireau_N2, Nidoran_N2, Nidorina_N2, Nidoqueen_N2 ]
TousPokemons_N2 = pokemon_object_N2

# =============================================================================
# #Remplir le deck de joueur 2
# deck_N2 = [Raichu_N2, Roucool_N2, Carapuce_N2]
# =============================================================================
#%% L'instanciation d'un Pokémon ennemi ou joueur 3
"""
Cet ensemble de pokemon N°3 est utilisé par le dresseur "adversaire" dans le Combat Joueur contre Joueur.
"""
pokemon_object_N3 = []
for k in range(len(pokemon_nom)):
    pokemon_object_N3.append(Pokemon(pokemon_nom[k], liste_element[k], niveau_init[k], 0, (vie_init[k]), energie_init[k], regene_init[k], resist_init[k], liste_competence[k], None))
    pokemon_object_N3[k].name = pokemon_nom[k]

Pikachu_N3 = pokemon_object_N3[0]
Raichu_N3 = pokemon_object_N3[1]
Roucool_N3 = pokemon_object_N3[2]
Roucoups_N3 = pokemon_object_N3[3]
Roucarnage_N3 = pokemon_object_N3[4]
Carapuce_N3 = pokemon_object_N3[5]
Carabaffe_N3 = pokemon_object_N3[6]
Tortank_N3 = pokemon_object_N3[7]
Psykokwak_N3 = pokemon_object_N3[8]
Akwakwak_N3 = pokemon_object_N3[9]
Ptitard_N3 = pokemon_object_N3[10]
Tetarte_N3 = pokemon_object_N3[11]
Tartard_N3 = pokemon_object_N3[12]
Salameche_N3 = pokemon_object_N3[13]
Reptincel_N3 = pokemon_object_N3[14]
Dracaufeu_N3 = pokemon_object_N3[15]
Goupix_N3 = pokemon_object_N3[16]
Feunard_N3 = pokemon_object_N3[17]
Ponyta_N3 = pokemon_object_N3[18]
Galopa_N3 = pokemon_object_N3[19]
Bulbizarre_N3 = pokemon_object_N3[20]
Herbizarre_N3 = pokemon_object_N3[21]
Florizarre_N3 = pokemon_object_N3[22]
Sabelette_N3 = pokemon_object_N3[23]
Sablaireau_N3 = pokemon_object_N3[24]
Nidoran_N3 = pokemon_object_N3[25]
Nidorina_N3 = pokemon_object_N3[26]
Nidoqueen_N3 = pokemon_object_N3[27]

Pikachu_N3.competence, Pikachu_N3.apres_evolution = [Eclair,Tonnerre, CageEclair], Raichu_N3
Raichu_N3.competence = [Eclair,Tonnerre, CageEclair, FatalFoudre, PileDuracell]
Roucool_N3.competence, Roucool_N3.apres_evolution= [BecVrille,Vol, Picpic], Roucoups_N3
Roucoups_N3.competence, Roucoups_N3.apres_evolution = [BecVrille,Vol, Picpic, CruAiles], Roucarnage_N3
Roucarnage_N3.competence = [BecVrille,Vol, Picpic, CruAiles, Tornade]
Carapuce_N3.competence, Carapuce_N3.apres_evolution = [BullesdO,Ecume, Surf], Carabaffe_N3
Carabaffe_N3.competence,Carabaffe_N3.apres_evolution  = [BullesdO,Ecume, Surf, Cascade], Tortank_N3
Tortank_N3.competence = [BullesdO,Ecume, Surf, Cascade, Hydrocanon]
Psykokwak_N3.competence, Psykokwak_N3.apres_evolution = [OndeBoreale, PinceMasse,PoingGlace ], Akwakwak_N3
Akwakwak_N3.competence = [OndeBoreale, PinceMasse,PoingGlace ]
Ptitard_N3.competence, Ptitard_N3.apres_evolution = [BullesdO, Ecume, OndeBoreale], Tetarte_N3
Tetarte_N3.competence, Tetarte.apres_evolution = [BullesdO, Ecume, OndeBoreale, PoingGlace], Tartard_N3
Tartard_N3.competence = [BullesdO, Ecume, OndeBoreale, PoingGlace, FontainedeVie]
Salameche_N3.competence, Salameche_N3.apres_evolution = [CrocsFeu, PoingFeu, Flammeche], Reptincel_N3
Reptincel_N3.competence, Reptincel_N3.apres_evolution = [CrocsFeu, PoingFeu, Flammeche, Deflagration], Dracaufeu_N3
Dracaufeu_N3.competence = [CrocsFeu, PoingFeu, Flammeche, Deflagration, LanceFlammes]
Goupix_N3.competence, Goupix_N3.apres_evolution = [PoingFeu, FeuSacre, CrocsFeu], Feunard_N3
Feunard_N3.competence =[PoingFeu, FeuSacre, CrocsFeu, RouedeFeu,Aurore ]
Ponyta_N3.competence, Ponyta_N3.apres_evolution = [Canicule, PiedBruleur, Boutefeu], Galopa_N3
Galopa_N3.competence = [Canicule, PiedBruleur, Boutefeu, RouedeFeu, Sangchaud]
Bulbizarre_N3.competence, Bulbizarre_N3.apres_evolution = [Fulmigraine,CanonGraine, BalleGraine], Herbizarre_N3
Herbizarre_N3.competence, Herbizarre_N3.apres_evolution = [Fulmigraine,CanonGraine, BalleGraine, FouetLianes], Florizarre_N3
Florizarre_N3.competence = [Fulmigraine,CanonGraine, BalleGraine, FouetLianes, LameFeuille]
Sabelette_N3.competence, Sabelette_N3.apres_evolution = [JetPierres,LamedeRoc, RocBoulet ], Sablaireau_N3
Sablaireau_N3.competence = [JetPierres,LamedeRoc, RocBoulet, Tomberoche, Racines ]
Nidoran_N3.competence, Nidoran_N3.apres_evolution = [Roulade,Martobois, Eboulement ], Nidorina_N3
Nidorina_N3.competence, Nidorina_N3.apres_evolution = [Roulade,Martobois, Eboulement, Tomberoche ], Nidoqueen_N3
Nidoqueen_N3.competence = [Roulade,Martobois, Eboulement, Tomberoche, PhotoSynthese ]

#Etablir un ensemble des instances de pokemon
pokemon_object_N3 = [Pikachu_N3, Raichu_N3, Roucool_N3,Roucoups_N3, Roucarnage_N3, Carapuce_N3, Carabaffe_N3,\
                  Tortank_N3,Psykokwak_N3, Akwakwak_N3,  Ptitard_N3,Tetarte_N3, Tartard_N3, Salameche_N3,Reptincel_N3,Dracaufeu_N3,\
                      Goupix_N3, Feunard_N3,Ponyta_N3, Galopa_N3, Bulbizarre_N3, Herbizarre_N3, Florizarre_N3, Sabelette_N3, Sablaireau_N3, Nidoran_N3, Nidorina_N3, Nidoqueen_N3 ]
TousPokemons_N3 = pokemon_object_N3    

#Classification des pokemons par rapport à leur niveau initiale
PokeNiveau1_N3 = [Pikachu_N3, Roucool_N3, Carapuce_N3,Psykokwak_N3,Ptitard_N3,Salameche_N3,Goupix_N3,Ponyta_N3, Bulbizarre_N3,Sabelette_N3,Nidoran_N3]
PokeNiveau6_N3 = [Raichu_N3,Roucoups_N3, Carabaffe_N3,Akwakwak_N3,Tetarte_N3,Reptincel_N3,Feunard_N3,Galopa_N3,Herbizarre_N3,Sablaireau_N3,Nidorina_N3]
PokeNiveau10_N3 = [Roucarnage_N3,Tortank_N3,Tartard_N3,Dracaufeu_N3,Florizarre_N3,Nidoqueen_N3]
#%% Fonction pour quitter le jeu
def quitter():# La fonction pour quitter le jeu
    sys.exit(0)

#%% Page d'accueil    
def interfaceConnexion():
    """
    La fonciton de la page d'accueil, comme son nom, il affiche le menu du jeu et nous permet de 
    faire plusieurs opération, ainsi que la réalisation de la fonction après sélection.
    "Nouveau Jeu" permet de commancer un nouveaux jeu: instancier le dresseur
    "Chargez votre jeu" permet de continuer le jeu: récupérer un dresseur souvgardé
    """
    print('# - - - - - - - - - - - - - - - - - - - #')
    print('#        Bienvenue dans POOkemon!       #')
    print('#  Le jeu de Pokemon Oriente Object :D  #')
    print('#                                       #')
    print('#           0.Nouveau Jeu               #')
    print('#           1.Chargez votre jeu         #')
    print('#           2.Exit                      #')
    print('# - - - - - - - - - - - - - - - - - - - #')
    tousVosPokemons = []   #Créer une liste qui contient tous les pokémons possédés par le dresseur
    flag = True
    while True:
        opera = input("\nQu'est-ce que voulez vous faire ? (0-2):")
        # Voici l'opération pour créer un nouveau joueur de jeu.
        # Nous entrons le nom du joueur, et sélectionnons le Pokémon initial.
        if opera == "0":
            nom = input("Saisissez votre nom:")
            print('Votre nom est:{}'.format(nom)), time.sleep(0.3) 
            print("{} est né!".format(nom)), print('')
            while True:
                opera2 = input("Pour l'instant, nous pouvons vous fournir six Pokémons initiaux de Niveau 1, vous pouvez(0-1) :\
                               \n\n0. Choisissez votre 6 Pokémons initiaux par vous-même. \
                                  \n1. Nous vous fournissons aléatoirement six Pokémons initiaux")
                if opera2 == "0":
                    deck, tousVosPokemons  = chosirPokemon(PokeNiveau1)   # Le joueur choisit 6 Pokémon soi-même
                    flag = False
                    return nom, deck, tousVosPokemons
                elif opera2 =="1":
                    deck, tousVosPokemons = aleatoire(PokeNiveau1)        # Il obtient six Pokémon au hasard.
                    flag = False
                    return nom, deck, tousVosPokemons
                else:
                    print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
            if not flag:break
        #Afin de rechager un dresseur, on vérifie d'abord le dossier "save" existe et nous avons déja souvgarder un dressuer.     
        elif opera == "1":
            if os.path.exists(chemin + "/save"):           # On vérifie d'abord le dossier "save" existe
                if not os.listdir(chemin + "/save") == []: # On vérifie que nous avons déja souvgarder un dressuer.
                    print("Ici votre comptes sauvgardés :") 
                    for fichier in os.listdir(chemin + "/save/"):
                        print (fichier[0:-4])
                    while True:
                        nom = input("Tapez votre nom:\n")
                        if not os.path.isfile(chemin + "/save/" + nom + ".txt"):
                            print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
                        else :                             # On récupérer les informations du dresseur et des pkémons possédé
                            lire_save = open(chemin + "/save/" + nom + ".txt").readlines()
                            pokemon_nom_save = []
                            pokemon_niveau_save = []
                            pokemon_exp_save = []
                            for i in range(3,len(lire_save)):
                                pokemon_nom_save.append(lire_save[i].split(' ')[0])
                                pokemon_niveau_save.append(lire_save[i].split(' ')[1])
                                pokemon_exp_save.append(lire_save[i].split(' ')[2])
                                for j in pokemon_object:
                                    if j.nom == pokemon_nom_save[i-3]:
                                        code1 = pokemon_nom_save.index(j.nom)
                                        j.niveau = int(pokemon_niveau_save[code1])
                                        j.exp = int(pokemon_exp_save[code1])
                                        code2 = pokemon_nom.index(j.nom)
                                        j.vie = int(vie_init[code2]) + float(vie_upgrade[code2]) * (j.niveau - int(niveau_init[code2]))
                                        j.vie_max = j.vie
                                        j.energie = int(energie_init[code2]) + float(energie_upgrade[code2]) * (j.niveau - int(niveau_init[code2]))
                                        j.energie_max = j.energie
                                        j.regene = int(regene_init[code2]) + float(regene_upgrade[code2]) * (j.niveau - int(niveau_init[code2]))
                                        j.resist = int(resist_init[code2]) + float(resist_upgrade[code2]) * (j.niveau - int(niveau_init[code2]))
                                        tousVosPokemons.append(j)
                            deck = []
                            for i in range(0,3):
                                deck.append(tousVosPokemons[pokemon_nom_save.index(lire_save[i].replace("\n",''))]) 
                            break
                    print("Bienvenue,",nom,"!\n"), time.sleep(0.3)
                    return nom, deck, tousVosPokemons
                    break
                else :
                    print("Dossier vide ! Commencez un nouveau jeux!")
                    time.sleep(0.3)
            else:
                print("Aucun compte sauvgardé ! Ressayez!")
                time.sleep(0.3)

        #Choisissez 2 ici pour quitter le jeu
        if opera == "2": quitter()
        else:
            print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")

# Créer un nouveau joueur
def creerNouveauDresseur(lesPokemons):
    """
    Cette fonction pour créer un nouveau dresseur, comme la fonciton ci-dessus, il nous fournit deux
    méthodes de choix d'un Pokémon : le joueur choisit 6 Pokémon soit-même, ou il obtient six Pokémon 
    au hasard. Enfin, cette fonciton return les informations du dresseur: "nom", "deck", "tousVosPokemons".
    """
    nom = input("Saisissez votre nom:")
    print('Votre nom est:{}'.format(nom)), time.sleep(0.3) 
    print("{} est né!".format(nom)),       print('')
    while True:
        opera2 = input("Pour l'instant, nous pouvons vous fournir six Pokémons initiaux de Niveau 1, vous pouvez(0-1) :\
                       \n\n0. Choisissez votre 6 Pokémons initiaux par vous-même. \n1. Nous vous fournissons aléatoirement six Pokémons initiaux")        
        if opera2 == "0":  # Le joueur choisit 6 Pokémon soi-même
            deck, tousVosPokemons  = chosirPokemon(lesPokemons)
            return nom, deck, tousVosPokemons    
        elif opera2 =="1": # Il obtient six Pokémon au hasard.
            deck, tousVosPokemons = aleatoire(lesPokemons)
            return nom, deck, tousVosPokemons
        else:
            print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
    
#%% Choisir Pokémon 
def chosirPokemon(TousPokemons):
    """
    Cette fonciton permet de chosit 6 pokémons initiaux. Avant chaque sélection, nous vérifions si nous avons déja 
    sélectionné ce Pokémon. L'entrée "TousPokemons" est une liste de tous les objects de pokémon.
    Enfin, cette fonction return deux liste: "deck" et "tousVosPokemons".
    """
    deck = []               # Deck
    tousVosPokemons = []    # Tous les pokémons possédés
    print('Choisissez votre six Pokemons initiaux :\n')
    for i in range(len(TousPokemons)):
        print("{0}.{1}".format(i, TousPokemons[i]))
    time.sleep(0.5)
    cpt = 1                 # Compter le nombre de pokémons déja sélectionés
    while True:
        while cpt  < 7 :
# =============================================================================
#             #print('Choisissez votre compagnes(0-26)  {}:'.format(cpt))  
# =============================================================================
            input1=input('Choisissez votre compagnes(0-26)  N°{}:'.format(cpt))
            # Vérifier d'abord le commande est acceptable
            if input1.isdecimal() and int(input1) <= len(TousPokemons)-1:
                if TousPokemons[int(input1)] in tousVosPokemons: # Vérifier si nous avons déja sélectionné ce Pokémon
                    print("{0} est déja votre compagne!, veuillez Choisissez un autre Pokemon\n" \
                              .format(TousPokemons[int(input1)].nom)), time.sleep(0.3)
                else: # Ajouter ce pokémon dans la liste "tousVosPokemons".
                    pokemon = TousPokemons[int(input1)]
                    print('Vous obtenez {}!'.format(pokemon.nom)), print(' ')
                    tousVosPokemons.append(pokemon)
                    cpt += 1
                    time.sleep(0.3)
            else:
                print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
        break
    # Eusuite, on choisit trois pokémons pour construire le deck
    print("Maintenant, veuillez choisir trois Pokémons à mettre dans votre deck"), print(" ")
    for i in range(len(tousVosPokemons)):
        print("{0},{1}".format(i, tousVosPokemons[i]))
    time.sleep(0.3)
    cpt = 1                 # Compter le nombre de pokémons déja sélectionés
    while True:
        while cpt  < 4 :
            print(" "), 
# =============================================================================
#             print('Choisissez votre Pokémon dans Deck(0-5) N°{}:'.format(cpt))  
# =============================================================================
            input1=input('Choisissez votre Pokémon dans Deck(0-5) N°{}:'.format(cpt))
            if input1.isdecimal() and int(input1) <= len(tousVosPokemons)-1:
                if tousVosPokemons[int(input1)] in deck:  # Vérifier si nous avons déja sélectionné ce Pokémon
                    print("{0} est déja dans votre deck !, veuillez Choisir un autre Pokemon\n" \
                          .format(tousVosPokemons[int(input1)].nom)), time.sleep(0.3)
                else:
                    pokemon = tousVosPokemons[int(input1)]
                    print('Vous choisissez {}.'.format(pokemon.nom))
                    deck.append(pokemon)
                    cpt += 1
                    time.sleep(0.3)
            else:
                print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
        break
    return deck, tousVosPokemons

def aleatoire(TousPokemons):
    """
    Cette fonction permet au système de nous aider à choisir au hasard six Pokémon initiaux. 
    IL a exactement le même résultat que la fonction précédente. Avec l'aide de cette fonction,
    nous pouvons sauter l'étape consistant à choisir nous-mêmes six Pokémons et entrer le jeu directement.
    """
    deck = []
    tousVosPokemons = random.sample(TousPokemons,6)
    print("Votre compagnes sont : "), print(" ")
    for i in range(len(tousVosPokemons)):
        print("{0},{1}".format(i, tousVosPokemons[i]))
    print("Maintenant, veuillez choisir trois Pokémons à mettre dans votre deck"), print(" ")
    time.sleep(0.5)
    cpt = 1        # Compter le nombre de pokémons déja sélectionés
    while True:
        while cpt  < 4 :
            print(" ")
# =============================================================================
#             print('Choisissez votre Pokémon dans Deck(0-5) N°{}:'.format(cpt))  
# =============================================================================
            input1=input('Choisissez votre Pokémon dans Deck(0-5) N°{}:'.format(cpt))
            # Vérifier d'abord le commande est acceptable
            if input1.isdecimal() and int(input1) <= len(tousVosPokemons)-1  :
                if tousVosPokemons[int(input1)] in deck:  # Vérifier si nous avons déja sélectionné ce Pokémon
                    print("{0} est déja dans votre deck !, veuillez Choisir un autre Pokemon\n"\
                          .format(tousVosPokemons[int(input1)].nom)), time.sleep(0.5)
                else:
                    pokemon = tousVosPokemons[int(input1)]
                    print('Vous choisissez {}.'.format(pokemon.nom)), print(' ')
                    deck.append(pokemon)
                    cpt += 1
                    time.sleep(0.5)
            else:
                print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
        break
    return deck, tousVosPokemons
#%% Programme principal
nom, deck, tousVosPokemons= interfaceConnexion() # Exécuter l'écran d'accueil et récupérer les informations du dresseur
player=Dresseur(nom,deck,tousVosPokemons)        # Instancier le dresseur 
while True:
    time.sleep(0.5)
    player.menu()