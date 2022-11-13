"""
# =============================================================================
# dresseur
# =============================================================================
Contient:
les class "Dresseur, IA"
les class "Combat, CombatJCJ, CombatJcE"
les fonctions "quitter, creerNouveauDresseur, chosirPokemon, aleatoire"

# =============================================================================
# Auteur
# =============================================================================
Hanlin LIU    3971558
Xiaowei CHEN  3971591
Yizen SUN     3970896


# =============================================================================
# Encadrants
# =============================================================================
Thomas Dietenbeck
Florence OSSART

# =============================================================================
# README
# =============================================================================

"""
import random as random
from random import choice
import sys
import time
import os
from abc import ABC , abstractmethod
#%%
from compobject import*
from pokeobject import*
from opendoc import*
from pokemon import Competence, CompetenceAttaque, CompetenceDefence
from pokemon import Pokemon
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
        
    # Afficher l'information du dresseur
    def __str__(self):
        res = "Dresseur: " + self.__nom + "avec ses Pokemons ci-dessous: "
        for i in range (len(self.__touslesPokemons)):
            res += self.__touslesPokemons[i] + "\n"
        return res
    
    def capturerPokemon(self, pokemon):
        # Il faut tester d'abord si le dresseur possède déjà ce pokémon.
        # Dressuer ne peut pas avoir deux pokémons identiques
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
        # Afficher la liste de pokemon disponible       
        for i in range(len(pokemonDispo)):
                print("{0}.{1}".format(i,pokemonDispo[i])) 
                print("-------------------------------------------") 
        print(""), time.sleep(0.3)
        return pokemonDispo
    
    def changerPokemon(self):
        """
        Fonction pour changer pokémon pendant le combat.      
        De même, on affiche d'abord les pokémons disponibles.
        Enfin, cette fonction retourne un pokémon actif
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
        Cette fonction consiste à changer le deck en mode non-combat. 
        Il permet le dresseur changer son deck s'il n'est pas en combat
        Enfin, il retourne "self.__deck"
        """
        flag = True,  print(" ")
        # Créer d'abord une liste qui contient les pokémons qui n'est pas dans le deck
        PokemonSaufDeck = [k for k in self.__touslesPokemons if k not in self.__deck]
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
                    if opera_ajouter.isdecimal() and int(opera_ajouter) <len(PokemonSaufDeck):
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
            # Vérifier si le niveau atteint maximum et le pokémon peut évoluer.
            if self.__touslesPokemons[i].niveau > niveau_max[self.__touslesPokemons[i].numero] \
                and self.__touslesPokemons[i].apres_evolution != None:
                avant_evolution_nom = self.__touslesPokemons[i].nom
                self.__touslesPokemons[i] = self.__touslesPokemons[i].apres_evolution
                print("Votre {0} a évolué à {1}!\n".format(avant_evolution_nom, self.__touslesPokemons[i].nom))
        # De même, dans "deck", il faut aussi remplacer le Pokémon d'origine par le Pokémon évolué
        for i in range(len(self.__deck)):
            if self.__deck[i].niveau > niveau_max[self.__deck[i].numero] and self.__deck[i].apres_evolution != None:
                self.__deck[i] = self.__deck[i].apres_evolution


    #La fonction pour commencer le cambat JCE
    def explorer(self):
        """
        Cette fonction pour trouver les pokémons sauvages dans la nature. 
        Il permet de commencer le combat Joueur contre Pokémon.
        Pareil, il faut vérifier si ce Pokémon sauvages n'est pas déja capturé par le dresseur
        """
        pokemonlibre = [i for i in TousPokemons_N2 if i not in self.__touslesPokemons]
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
                                       \n0.Combat Humain contre Humain\
                                       \n1.Combat Humain contre Ordinateur")
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
                elif opera == "5":      # Creer un nouveau dresseur
                    self.sauvegarder()  # Stocker le dresseur actuel
                    # Utiliser la fonction "creerNouveauDresseur" pour créer un nouveau dresseur
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

                    if pokemonDispo: # Si cette liste n'est pas vide
                        pokemon = random.sample(pokemonDispo, 1)# Sélectionner au hasard un Pokémon dans la liste 
                        print("{} change son pokemon".format(self.nom)) 
                        print("Pokemon de {0} actuel est {1}".format(self.nom, pokemon.nom))
                        return pokemon
                    else: #Si IA n'a même pas de Pokémon disponible, alors il juste fait quelque chose au hasard...
                        compeUtilise = pokemon.competence[random.randint(0, len(pokemon.competence)-1)] 
                        pokemon.utiliserCompet(compeUtilise, but)
                        break
                    
#%% La classe de Combat 
class Combat(ABC):
    """
    Cette une classe abstraite car on ne l'instantcie jamais. Dans cette class, 
    il implémente trois méthodes arbitraires, "tour_par_tour" sert à dérouler le combat, 
    "regen_max" pour tous les Pokemons commencent le combat avec leur vie et énergie au maximum.
    "debutCombat" sert à afficher les informations de Cambat et permet les dresseurs choisissent ses
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
        print("A la fin de la tour, les Pokémons régénèrent quelques l'énergie automatiquement"), print(" ")
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
                        print("{0} est un défaite!!!!!!!!, {1} gagne le combat".format(self.dresseur.nom, self.__dresseur2.nom))
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
            print("----------------------------")
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
                        print("{0} est défaite!!!!!!!!!, {1} gagne le combat".format(self.dresseur2.nom, self.dresseur.nom))
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
                        print("{0} est défaite!!!!!!!, {1} gagne le combat".format(self.dresseur.nom, self.__dresseur2.nom))
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
            print("----------------------------")
            self.dresseur2.utiliserCompetence(Pokemon_choisi2, Pokemon_choisi)
            #Avant de passer le tour suivant, il faut tester si le pokemon actif du dresseur peut contuner à combattre
            #Si non, il faut changer le pokémon actif, si la vie tous les pokemons dans deck = 0, alors dresseur
            #échoue le combat.
            if  Pokemon_choisi.vie == 0:
                print(" "), print("Votre pokemon est été KO")
                if self.dresseur.deck[0].vie == 0 and self.dresseur.deck[1].vie == 0 and self.dresseur.deck[2].vie == 0 :
                    print ("Tous vos Pokemons dans Deck sont été KO, Défaite !")
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
                print('{0}.{1}\n'.format(i, Pokemon_choisi.competence[i])), 
            time.sleep(0.5)    

            #Afficher les opérations de capturer le Pokémon, de changer le Pokémon actif, 
            #de passer le tour et de fuir le combat
            print("{0}.Changer Pokemon\n" "\n{1}.Capturer ce Pokemon\n" "\n{2}.Passser votre tour\n" "\n{3}.Fuir le combat"\
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
                        print("!!!!!!Défaite!!!!!!")
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
                print("----------------------------")
                print("c'est à {0} de jouer\n{1}".format(self.__pokemon2.nom, self.__pokemon2)), time.sleep(0.5)
                self.utiliseComp_poke(Pokemon_choisi)
            #Avant de passer le tour suivant, il faut tester si le pokemon actif du dresseur peut contuner à combattre
            #Si non, il faut changer le pokémon actif, si la vie tous les pokemons dans deck = 0, alors dresseur
            #échoue le combat.
            if  Pokemon_choisi.vie == 0:
                print("Votre pokemon est été KO")
                if self.dresseur.deck[0].vie == 0 and self.dresseur.deck[1].vie == 0 and self.dresseur.deck[2].vie == 0 :
                    print ("Tous vos Pokemons dans Deck sont été KO, défaite !")
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
        
#%% Fonction pour quitter le jeu
def quitter():# La fonction pour quitter le jeu
    sys.exit(0)
    
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
            input1=input('Choisissez votre compagnes(0-27)  N°{}:'.format(cpt))
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