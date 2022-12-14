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
        # Il faut tester d'abord si le dresseur poss??de d??j?? ce pok??mon.
        # Dressuer ne peut pas avoir deux pok??mons identiques
        if pokemon in (self.__touslesPokemons): 
            print("Vous avez d??ja eu ce Pok??mon, essayez-vous de capturer l'autre pokemon :D")
        else:    
            self.__touslesPokemons.append(pokemon) #Capturer ce pok??mon
            print("Vous avez r??ussi ?? capturer {} !".format(pokemon.nom))
    
    # Dans le match, voir les informations du dresseur            
    def voirdeck(self): 
        """
        Fonction pour voir le deck. Afin d'utiliser cette fonciton dans le  
        combat, il faut d'abord tester si la vie du pok??mon n'est pas 0.
        Enfin, cette fonction retourne une liste qui contient les pok??mons disponibles
        """
        #Cr??er une liste qui contient les pok??mons disponibles(la vie != 0)
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
        Fonction pour changer pok??mon pendant le combat.      
        De m??me, on affiche d'abord les pok??mons disponibles.
        Enfin, cette fonction retourne un pok??mon actif
        """
        pokemonDispo = self.voirdeck()
        while True:
            opera = input("Quel Pokemon voulez-vous choisir ?? faire le combat ? (0-2)") 
            # Il faut tester si la commande est acceptabe (la command est un chiffre et ne d??passer pas le long du deck)
            if opera.isdecimal() and int(opera) < len(pokemonDispo): 
                Pokemonchoisi = pokemonDispo[int(opera)]
                print("Pokemon de {0} actuel est {1}".format(self.nom, Pokemonchoisi.nom))
                return Pokemonchoisi
            else:
                print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
                 
    def voirtouslesPokemons(self):
        #Cette fonction affiche tous vos pok??mons poss??d??s        
        print("Tous vos Pokemons sont:"), print(" ")
        for i in range (len(self.__touslesPokemons)):
            print("{0}.{1}".format(i,self.__touslesPokemons[i]))
            print("-------------------------------------------")
        print(''), time.sleep(0.3)

    # En mode non-combat, changer le deck du dresseur           
    def changmentDeck(self): 
        """
        Cette fonction consiste ?? changer le deck en mode non-combat. 
        Il permet le dresseur changer son deck s'il n'est pas en combat
        Enfin, il retourne "self.__deck"
        """
        flag = True,  print(" ")
        # Cr??er d'abord une liste qui contient les pok??mons qui n'est pas dans le deck
        PokemonSaufDeck = [k for k in self.__touslesPokemons if k not in self.__deck]
        print("Changement de Deck\nVoici vos Pok??mons dans deck:"), print(" ")
        self.voirdeck()
        while True:
            # Le joueur saisit le Pok??mon qu'il souhaite d??placer
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
                        #on remplace le pok??mon par pok??mon choisit
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
    
    # Fonction d'??voluer Pok??mon
    def evolution(self):
        """
        Cette fonction permet d'??valuer le Pok??mon. Des que le niveau du Pok??mon 
        atteint le niveau maximum et le pok??mon peut ??valuer,il ??value.
        Le Pok??mon ??volu?? est un nouveau object et remplace le Pok??mon d'origine.
        """
# =============================================================================
#         for i in self.__deck:
#             # V??rifier si le niveau atteint maximum et le pok??mon peut ??voluer.
#             if i.niveau > niveau_max[i.numero] and i.apres_evolution != None: 
#                 avant_evolution_nom = i.nom
#                 i = i.apres_evolution # Remplacer le Pok??mon d'origine par le Pok??mon ??volu??
#                 print("Votre {0} a ??volu?? ?? {1}!\n".format(avant_evolution_nom, i.nom))
#                 time.sleep(0.3)
#         # De m??me, dans "touslespokemon", il faut aussi remplacer le Pok??mon d'origine par le Pok??mon ??volu??
#         for j in self.__touslesPokemons:
#             if j.niveau > niveau_max[j.numero] and j.apres_evolution != None: 
#                 j = j.apres_evolution 
# =============================================================================
        for i in range(len(self.__touslesPokemons)):
            # V??rifier si le niveau atteint maximum et le pok??mon peut ??voluer.
            if self.__touslesPokemons[i].niveau > niveau_max[self.__touslesPokemons[i].numero] \
                and self.__touslesPokemons[i].apres_evolution != None:
                avant_evolution_nom = self.__touslesPokemons[i].nom
                self.__touslesPokemons[i] = self.__touslesPokemons[i].apres_evolution
                print("Votre {0} a ??volu?? ?? {1}!\n".format(avant_evolution_nom, self.__touslesPokemons[i].nom))
        # De m??me, dans "deck", il faut aussi remplacer le Pok??mon d'origine par le Pok??mon ??volu??
        for i in range(len(self.__deck)):
            if self.__deck[i].niveau > niveau_max[self.__deck[i].numero] and self.__deck[i].apres_evolution != None:
                self.__deck[i] = self.__deck[i].apres_evolution


    #La fonction pour commencer le cambat JCE
    def explorer(self):
        """
        Cette fonction pour trouver les pok??mons sauvages dans la nature. 
        Il permet de commencer le combat Joueur contre Pok??mon.
        Pareil, il faut v??rifier si ce Pok??mon sauvages n'est pas d??ja captur?? par le dresseur
        """
        pokemonlibre = [i for i in TousPokemons_N2 if i not in self.__touslesPokemons]
        adversaire = choice(pokemonlibre)        # Choisr al??atoirement un Pok??mon.
        print("Vous avez tomb?? sur {}".format(adversaire)) 
        combatjce = CombatJcE(self, adversaire ) # Instancier le combat
        combatjce.tour_par_tour()  # Utiliser la fonction "tour_par_tour" commencer le combat
    
    # La fonction de stockage      
    def sauvegarder(self): 
        """
        Cette fonction permet de souvgarder les informations du dressuer
        On enregistre les informations dans le m??me chemin que le programe et 
        dans un dossier qui s'appelle "save". Pour enregistrement, oon souvegarder
        le nom du dresseur, "self.__deck" et "self.__touslesPokemons".
        """
        #V??rifier d'abord si la dossier "save" existe.
        if os.path.exists(chemin + "/save") : 
            # Sauvgarder l'information de "self.__deck"
            editeur1 = open(chemin + "/save/" + self.__nom + ".txt","w") 
            for i in self.__deck: 
                editeur1.write(i.nom+'\n')
            # Sauvgarder l'information de "self.__touslesPokemons"
            editeur2 = open(chemin + "/save/" + self.__nom + ".txt","a") 
            for i in self.__touslesPokemons: 
                editeur2.write(i.nom+' '+str(i.niveau)+' '+str(i.exp)+'\n')
        else: # S'il n'y a pas de dossier "save", cr??er-en un nouveau  
            os.mkdir(chemin + "/save")  
            editeur1 = open(chemin + "/save/" + self.__nom + ".txt","w")  
            for i in self.__deck: 
                editeur1.write(i.nom+'\n')
            editeur2 = open(chemin + "/save/" + self.__nom + ".txt","a") 
            for i in self.__touslesPokemons:
                editeur2.write(i.nom+' '+str(i.niveau)+' '+str(i.exp)+'\n')
   
    def menu(self):
        """
        Cette fonction permet le dresseur effectuer des op??rations sur " Menu".
        On d??finit toutes les fonctions que le joueur peut mettre en ??uvre dans l'interface d'accueil
        """
        while True:
            print(" ")
            print("=================MENU================")
            print("||   O.Voyez votre deck            ||")
            print("||   1.Voyez tous vos Pok??mons     ||")
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
                    On choisit le mode de combat: Dresseur contre IA ou contre l'autre personne r??elle
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
                            Il faut votre adversaire instancier un autre dresseur, c'est ?? dire:
                            saisit son nom, choisit ses pok??mons initiaux et son deck.
                            """
                            print(" "), print("Il faut Dressuer N??2 choisir ses Pokemons initiaux et son Deck")
                            nom, deck, tousVosPokemons = creerNouveauDresseur(TousPokemons_N3) # Instancier un nouveau dresseur 
                            dressuerN2 = Dresseur(nom, deck, tousVosPokemons ) 
                            combatjcj = CombatJCJ(self, dressuerN2) # Commencer le combat avec dresseurN2
                            combatjcj.tour_par_tour() # Utiliser la fonction "tout_par_tour" d??rouler le combat
                            break
                        elif opera2 == "1": # Combat Humain contre Ordinateur
                            """
                            Nous entrons dans le mode joueur contre IA.
                            On choisit la difficult?? de IA, et en fonction de la difficult??, on fait le diff??rent combat 
                            """
                            while True:
                                opera3 = input("Choisissez-vous le niveau de diff??cult?? de l'Ordinateur (0-2):") 
                                # V??rifier d'abord le commande est acceptable
                                if opera3.isdecimal() and int(opera3) >= 0 and int(opera3)<3:  
                                    opera3 = int(opera3)
                                    nom = "ORDINATEUR" 
                                    print("Le niveau de difficult?? est {}".format(opera3)) # Affichez Le niveau de difficult??
                                    if opera3 == 0: 
                                        # Niveau 0: S??lectionner al??atoirement 6 Pok??mons niveau 1
                                        tousVosPokemons = random.sample(PokeNiveau1_N3,6)
                                        deck = random.sample(tousVosPokemons ,3)
                                        dressuerN2 =  IA(nom, deck, tousVosPokemons,opera3 ) #Instancier IA
                                    elif opera3 == 1: 
                                        # Niveau 1: S??lectionner al??atoirement 6 Pok??mons niveau 6
                                        tousVosPokemons = random.sample(PokeNiveau6_N3,6)
                                        deck = random.sample(tousVosPokemons,3)
                                        dressuerN2 =  IA(nom, deck, tousVosPokemons, opera3 )
                                    elif opera3 == 2: 
                                        # Niveau 1: S??lectionner al??atoirement 6 Pok??mons niveau 10
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
                    # Utiliser la fonction "creerNouveauDresseur" pour cr??er un nouveau dresseur
                    nom, deck, tousVosPokemons = creerNouveauDresseur(TousPokemons) 
                    self = Dresseur(nom, deck, tousVosPokemons)   # Initialiser ce nouveau dresseur
                elif opera == "6":     # Exit 
                    self.sauvegarder() # Souvgarder des informations
                    print("Au revoir!  ?? bient??t!!!") 
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
    La classe de IA est une classe h??rite de dresseur. Dans cette class, on d??finit
    les fonctions de IA en fonction des diff??rentes difficult??s. IA est une sous-classe de Dresseur, 
    il h??rite tous les variables de Dresseur, et il pocc??de aussi les variables priv??s comme "la difficult??", 
    afin que IA puisse ??tre effectu?? selon son difficult??.
    """
    def __init__(self, nom, deck, touslesPokemons, difficulte):
        super().__init__(nom, deck, touslesPokemons)
        self.__difficulte = difficulte # le niveau de la difficult?? d'IA

    @property
    def difficulte(self): return self.__difficulte
    @difficulte.setter
    def difficulte(self, difficulte):  self.__difficulte = difficulte
    
    # Choisissez le premier Pok??mon ?? faire le combattre
    def choisirPokeDepart (self):
        """
        Cette fonction permet de choisit le premier Pok??mon ?? faire le combat en fonction de difficult??. 
        On impl??mente deux m??thodes pour choisir ce pok??mon:  quand la difficult?? est 0, IA choisit 
        al??atoirement un pok??mon de deck. Quand la diff??cult?? est sup??rieure que 0, IA compare le niveau 
        de pok??mon dans son deck, et choisit celui avec le plus haut niveau. Enfin, cette fonction retoure
        le premier Pok??mon ?? faire le combat.
        """
        # Cr??er une liste qui contient les pok??mon disponibles.
         # v??rifier les Pok??mons dont la vie n'est pas nulle
        pokemonDispo = [i for i in self.deck if i.vie != 0]   
        if self.__difficulte == 0 or "0":
            pokemonDepart = pokemonDispo[random.randint(0, len(pokemonDispo)-1)]  # choisir al??atoirement un Pok??mon
        else:
            #comparer le niveau de pok??mon dans le deck, et choisit celui avec le plus haut niveau.
            pokemonDepart = pokemonDispo[0] 
            for i in pokemonDispo:
                if i.niveau > pokemonDepart.niveau: 
                    pokemonDepart = i
        return pokemonDepart
    
    def changerPokemon(self, pokemon):
        """
        Cette fonction permet IA changer son pok??mon ?? faire le combat, diff??rent que la classe"dresseur", 
        il faut re??crire cette foncion. Enfin, il retourner un pok??mon ?? faire le combat. l'entr??e "pokemon"
        repr??sente le pok??mon qui est en train de faire le combat.
        """
        pokemonDispo = []   # Cr??er une liste qui contient les pok??mons disponibles
        for i in self.deck:
            # Si la pok??mon n'est pas le pok??mon actuel qui est en train de faire le combat, on le ajooute dans 
            # la liste "pokemonDispo". 
            if i.vie != 0 and i!=pokemon: 
                pokemonDispo.append(i)
        #Apr??s le boucle ci-dessous, si la liste"pokemonDispo" n'est pas vide, IA choisit un pk??mon al??atoirement.      
        if pokemonDispo:
            pokemon = random.sample(pokemonDispo, 1) 
            print("Pokemon de {0} actuel est {1}".format(self.nom, pokemon.nom))
            return pokemon
    
    # La fonction pour utiliser les comp??tences
    def utiliserCompetence (self, pokemon, but):
        """
        L'entr??e "pokemon" repr??sente son pokemon qui est en train de faire le combat, et "but" 
        repr??sente la cible de la comp??tence d'attaque. 
        Il y aura diff??rentes mani??res d'utiliser des comp??tences pour diff??rentes difficult??s IA.
        Pour Niveau 0, IA utiliser al??atoirement les comp??tences. 
        """
        if self.difficulte == 0: 
            compeUtilise = pokemon.competence[random.randint(0, len(pokemon.competence)-1)] 
            pokemon.utiliserCompet(compeUtilise, but) # rappeler la fonciton "utiliserCompet" pour utiliser la comp??tence
        """
        IA d??terminera d'abord si sa vie est inf??rieure ?? 20% de vie maximale, et si oui, recherchez la barre 
        de comp??tences pour voir s'il existe une comp??tence qui restaure la vie, et utilisez-la.
        Si non, IA d??terminera si son ??nergie est inf??rieure ?? 20% d' ??nergie maximale, et si oui, recherchez la barre 
        de comp??tences pour trouver une comp??tence qui restaure l'??nergie, et utilisez-la.
        Si les conditions ci-dessus ne sont pas remplies, la comp??tence attaque sera utilis??e au hasard.
        """
        if self.difficulte == 1: 
            flag = True 
            while True:
                if pokemon.vie < (0.2*pokemon.vie_max):        # Si la vie du Pok??mon est inf??rieure ?? 20% de vie maximale
                    for i in pokemon.competence:
                        if isinstance(i, CompetenceDefence) and i.soin !=0:   # Chercher la comp??tence qui restaure la vie.
                            pokemon.utiliserCompet(i, but)     # Si oui, utiliser-la
                            flag = False
                            break
                    if not flag: break
                
                if pokemon.energie <(0.2*pokemon.energie_max):  # Si l'energie du Pok??mon est inf??rieure ?? 20% d'??nergie maximale
                    for i in pokemon.competence:
                        if isinstance(i, CompetenceDefence) and i.energie !=0: # Chercher la comp??tence qui restaure l'??nergie.
                            pokemon.utiliserCompet(i, but)      # Si oui, utiliser-la
                            flag = False
                            break
                    if not flag: break
                #Cr??er une liste qui contient les competences attaques et chercher les comp??tences attaques
                compeAttaque = [i for i in pokemon.competence if isinstance(i, CompetenceAttaque)]             
                compeUtilise = compeAttaque[random.randint(0, len(compeAttaque)-1)] # Choisir au hasard une comp??tence attaque
                pokemon.utiliserCompet(compeUtilise, but)
                break
        """
        le niveau 2 fait quelques am??liorations sur la base du niveau 1: IA d??termine d'abord si sa vie est inf??rieure ?? 40% 
        de vie maximale.De plus, IA ne d??cide plus d'utiliser ou non la comp??tence de r??g??n??ration de l'??nergie en fonction 
        de la valeur d'??nergie restante,mais v??rifiera d'abord si son ??nergie restante est suffisante pour utiliser une comp??tence 
        d'attaque. Si oui, il choisit la comp??tence d'attaque la plus puissantes. De plus, IA changera ??galement le Pok??mon en fonction 
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
                # Cr??er une liste qui contient les competences attaques et 
                # r??cup??rer les comp??tences qui peuvent ??tre utilis?? en fonction d'??nergie restante 
                compeAttaqueDispo = [i for i in pokemon.competence if i.cout < pokemon.energie \
                                     and isinstance(i,CompetenceAttaque)]          

                if compeAttaqueDispo:           # Si la liste de comp??tence disponible n'est pas vide
                    compeUtilise = compeAttaqueDispo[0]       
                    for i in compeAttaqueDispo: # Choisir les comp??tences les plus puissantes dans cette liste
                        if i.puissance > compeUtilise.puissance:
                            compeUtilise = i
                    pokemon.utiliserCompet(compeUtilise, but) # Utiliser-la
                    break
                else: # Si l'??nergie restante n'est pas suffisante pour effecter une comp??tence attaque, r??g??n??rer l'??nergie!
                    for i in pokemon.competence: 
                        if isinstance(i, CompetenceDefence) and i.energie !=0:
                            pokemon.utiliserCompet(i, but)  
                            flag = False
                            break
                    if not flag: break
                    # Si aucune des conditions ci-dessus n'est remplie (Pok??mon ne peut pas r??g??n??rer HP, l'??nergie,
                    # et utiliser de comp??tence d'attaque), IA remplacera Pok??mon.
                    pokemonDispo = [i for i in self.deck if i.vie != 0 and i!= pokemon ]

                    if pokemonDispo: # Si cette liste n'est pas vide
                        pokemon = random.sample(pokemonDispo, 1)# S??lectionner au hasard un Pok??mon dans la liste 
                        print("{} change son pokemon".format(self.nom)) 
                        print("Pokemon de {0} actuel est {1}".format(self.nom, pokemon.nom))
                        return pokemon
                    else: #Si IA n'a m??me pas de Pok??mon disponible, alors il juste fait quelque chose au hasard...
                        compeUtilise = pokemon.competence[random.randint(0, len(pokemon.competence)-1)] 
                        pokemon.utiliserCompet(compeUtilise, but)
                        break
                    
#%% La classe de Combat 
class Combat(ABC):
    """
    Cette une classe abstraite car on ne l'instantcie jamais. Dans cette class, 
    il impl??mente trois m??thodes arbitraires, "tour_par_tour" sert ?? d??rouler le combat, 
    "regen_max" pour tous les Pokemons commencent le combat avec leur vie et ??nergie au maximum.
    "debutCombat" sert ?? afficher les informations de Cambat et permet les dresseurs choisissent ses
    pok??mon ?? faire le combat. 
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
        ?? la fin de chaque tour, Pok??mon restaurera automatiquement une certaine quantit?? d'??nergie.
        les ??ntr??es "PokemonN1" et "PokemonN2" repr??sentent les deux pok??mons qui fait le combat.
        """
        print("A la fin de la tour, les Pok??mons r??g??n??rent quelques l'??nergie automatiquement"), print(" ")
        print("Leur energies actuelles sont: {0}: {1}, {2}: {3}"\
              .format(PokemonN1.nom, PokemonN1.energie, PokemonN2.nom, PokemonN2.energie))
        PokemonN1.energie += PokemonN1.regene
        if PokemonN1.energie > PokemonN1.energie_max:  # V??rifier si l'??nergie est l'??nergie maximale
            PokemonN1.energie = PokemonN1.energie_max  # Quand l'??nergie est sup??rieure ?? l'??nergie max, l'??nergie = l'??nergie max
        PokemonN2 .energie += PokemonN2 .regene
        if PokemonN2 .energie> PokemonN2 .energie_max:  
            PokemonN2 .energie = PokemonN2 .energie_max
        print("Apr??s reg??n??ration, Leur energies sont {0}: {1}, {2}: {3}"\
              .format(PokemonN1.nom, PokemonN1.energie, PokemonN2.nom, PokemonN2.energie))
        
#%% La classe de CombatJCJ        
class CombatJCJ(Combat):
    """
    La class CombatJcJ h??rite la classe Combat. 
    Sauf le dresseur "vous", il faut d??clare un autre attribut "dressuer2" comme votre adversaire.
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
        commencent le combat avec leur vie et ??nergie au maximum.
        """
        for i in range (len(self.dresseur.deck)):
            self.dresseur.deck[i].vie = self.dresseur.deck[i].vie_max         # Restaurer la vie en vie maximale du dresseur1
            self.dresseur.deck[i].energie = self.dresseur.deck[i].energie_max # Restaurer l'??nergie en ??nergie maximale du dresseur1
            self.__dresseur2.deck[i].vie = self.__dresseur2.deck[i].vie_max   # Restaurer la vie en vie maximale du dresseur2
            self.__dresseur2.deck[i].energie = self.__dresseur2.deck[i].energie_max # Restaurer l'??nergie en ??nergie maximale du dresseur2
    
    def debutCombat (self):
        """
        Cette fonciton affiche les informations de Cambat au d??but du combat et permet les dresseurs choisissent 
        leur pok??mon ?? faire le combat.
        Enfin, cette fonction return les deux pok??mons choisit ?? faire le combat
        """
        print("Combat JCJ commence, |{0}|  ===VS===  |{1}|"\
              .format(self.dresseur.nom, self.__dresseur2.nom)), print(" ")
        print("{0} choisit son pokemon qui fait le combat : (0-2)"\
              .format(self.dresseur.nom)), time.sleep(0.5), print(" ")
        # Dresseur 1 choisit son pok??mon ?? faire le combat
        while True:
            self.dresseur.voirdeck(), time.sleep(0.5) #Afficher les pok??mons dans la deck
            opera = input() 
            if opera.isdecimal() and (opera == "0" or opera == "1" or opera == "2"): # Assurer l'entr??e est correcte 
                time.sleep(0.5), print(" ")
                break

            else:
                 print("\n-------------------\nInvalide! Ressayer!\n-------------------\n"), print(" ")
        print("{0} choisit son pokemon qui fait le combat : (0-2)".format(self.__dresseur2.nom)), time.sleep(0.5), print(" ")
        # Dresseur 2 choisit son pok??mon ?? faire le combat
        while True:
            self.__dresseur2.voirdeck(), time.sleep(0.5)
            opera2 = input()
            if opera2.isdecimal() and (opera2 == "0" or opera2 == "1" or opera2 == "2"): # Assurer l'entr??e est correcte 
                time.sleep(0.5)
                break
            else:
                print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
        return self.dresseur.deck[int(opera)], self.__dresseur2.deck[int(opera2)] 
    
    # La s??lection des informations homme-machine dans le combat homme-machine
    def debutCombat_IA (self):
        """
        Le principe de cette fonction est pareil que la fonction pr??c??dente, mais il sert ?? mode Combat Humain contre Ordinateur
        
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
        pokemonDepart_IA = self.__dresseur2.choisirPokeDepart() #IA choisit son pok??mon en utilisant la fonciotn "choisirPokeDepart"
        return self.dresseur.deck[int(opera)], pokemonDepart_IA
    
    #La fonction d??roule le combat Humain contre Humain
    def tour_par_tour(self):
        """
        Fontion d??roule le combat Humain contre Humain. Apr??s r??cup??rer les deux pok??mons choist ?? faire le combat, la principale partie
        de la fonction est une boucle : chaque it??ration le programme affiche le menu d'op??ration,  un dresseur peut soit utiliser une 
        comp??tence de son Pokemon actif, soit choisir de remplacer son Pokemon actif par un autre Pokemon de son deck, soit passer son tour
        ou d??clarer forfait.
        
        A la fin de chaque it??ration(tour),  les pok??mons restaurent automatiquement une certaine quantit?? d'??nergie.
        
        Le combat s???arr??te si les 3 Pokemons du deck d???un des dresseurs sont ko ou si l???un des dresseurs d??clare forfait.
        A la fin du combat, les pok??mons gagnent l'exp??rience, ??voluent et revient ?? le meilleur ??tat (Vie, ??nergie).
        """
        self.regen_max()  ## La fonction pour revenir ?? le meilleur ??tat du Pokemon
        Pokemon_choisi, Pokemon_choisi2 = self.debutCombat() # On r??cup??rer les deux pok??mon choist ?? faire le combat
        time.sleep(0.5)
        print("la pokemon choisi de {} est {}".format(self.dresseur.nom, Pokemon_choisi.nom)), time.sleep(0.5), print("  ")
        print("la pokemon choisi de {} est {}".format(self.__dresseur2.nom, Pokemon_choisi2.nom)), time.sleep(0.5), print("  ")
        flag = True  # Ces deux petites ""flag" sert ?? break le boucle
        flag2 = True
        
        for i in range (1000): 
            #Afficher d'abord le menu d'op??ration du dresseur 1 
            print("=======Tour {}=======".format(i+1)),              time.sleep(0.5), print(" ")
            print("c'est ?? {0} de jouer".format(self.dresseur.nom)), time.sleep(0.5), print(" ")
            print("le profil de votre pokemon choisit est \n"),      time.sleep(0.5)
            print(Pokemon_choisi), time.sleep(0.5), print(" "),      time.sleep(0.5)
            #Afficher les comp??tence du pok??mon actif du dresseur 1
            for i in range(len(Pokemon_choisi.competence)):
                print('{0}.{1}\n'.format(i, Pokemon_choisi.competence[i]))
            time.sleep(0.5)    
            #Afficher les op??rations de changer de Pok??mon actif, de passer le tour et de fuir le combat
            print("{0}.Changer Pokemon\n" "\n{1}.Passser votre tour\n" "\n{2}.Fuir le combat"\
                  .format(len(Pokemon_choisi.competence), len(Pokemon_choisi.competence)+1, len(Pokemon_choisi.competence)+2))
            print(" "), time.sleep(0.5)
            #Dresseur fait son op??ration
            while True:
                opera2 = input("Qu'est ce que vous voulez faire :")
                time.sleep(0.5)
                # V??rifier d'abord que le command est acceptable
                if opera2.isdecimal() and int(opera2)>=0 and int(opera2) <=len(Pokemon_choisi.competence)+3:
                    opera2 = int(opera2) 
                    if opera2 < len(Pokemon_choisi.competence):       # Si le commande est l'utilisation de comp??tence, donc utiliser-la
                        Pokemon_choisi.utiliserCompet(Pokemon_choisi.competence[opera2], Pokemon_choisi2)
                        break
                    elif opera2 == (len(Pokemon_choisi.competence)):  #En utilisant la fonction "changerPokemon" pour changer pok??mon
                        print("Votre Pokemon actuelle est {}".format(Pokemon_choisi.nom)), print(" "), time.sleep(0.5)
                        Pokemon_choisi = self.dresseur.changerPokemon()
                        break
                    elif opera2 == (len(Pokemon_choisi.competence)+1):#Passer le tour 
                        print("Vous avez pass?? votre tour !")
                        break
                    else: # d??clarer forfait
                        print("{0} est un d??faite!!!!!!!!, {1} gagne le combat".format(self.dresseur.nom, self.__dresseur2.nom))
                        flag = False
                        # Si dresseur 1 ??choue son combat, les pokemons du dresseur 2 gagnent l'??xp??rience et ??voluent.
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
            #A la fin du tour de dresseur 1, on v??rifier si la vie du pok??mon actif du dresseur 2 = 0 ou pas,
            #Si oui et si il a encore des autres pok??mons disponible, alores changer pok??mon et continuer.
            #Si non, le combat termine, les pok??mon du dresseur 1 gagnent l'exp, augmentent niveau, ??voluent.
            if  Pokemon_choisi2.vie == 0:
                print("{0} de {1} est ??t?? KO".format(Pokemon_choisi2.nom, self.__dresseur2.nom))
                # Verifier si il y a d'autre pok??mon disponible
                if self.__dresseur2.deck[0].vie == 0 and self.__dresseur2.deck[1].vie == 0 and self.__dresseur2.deck[2].vie == 0 :
                    print ("Tous les Pokemons de {0} sont ??t?? KO, {0} perd le combat!, {1} gange le combat !"\
                           .format(self.__dresseur2.nom, self.dresseur.nom))
                    print("Le combat se termine")
                    for i in self.dresseur.deck: #les pok??mon du dresseur 1 gagnent l'exp, augmentent niveau, ??voluent.
                        i.gangerExperienceJCJ(self.__dresseur2)
                        i.augementerNiveau()
                        print(" ")
                    self.dresseur.evolution()
                    break
                else: #Else, changer le pok??mon actif et continuer
                    print("Il faut choisir un autre pokemon pour continuer le combat")
                    Pokemon_choisi2 = self.dresseur2.changerPokemon()
                    print("{0} choisit {1} pour continue le combat".format(self.__dresseur2.nom, Pokemon_choisi2.nom))
            """
            Ensuite, c'est la tour du dresseur 2. Il est tout ?? fait la m??me chose que la tour du dresseur 1.
            Apr??s la tour du dresseur 1, elle passera automatiquement ?? la tour du joueur 2. 
            """
            print("----------------------------")
            print("c'est ?? {0} de jouer".format(self.__dresseur2.nom)), print(" "), time.sleep(0.5)
            print("le profil de votre pokemon choisit est\n "),                     time.sleep(0.5)
            print(Pokemon_choisi2),                                     print(" "), time.sleep(0.5)
            #Afficher les comp??tence du pok??mon actif du dresseur 2
            for i in range(len(Pokemon_choisi2.competence)):
                print('{0}.{1}\n'.format(i, Pokemon_choisi2.competence[i]))
            time.sleep(0.5)    
            #Afficher les op??rations de changer de Pok??mon actif, de passer le tour et de fuir le combat
            print("{0}.Changer Pokemon\n" "\n{1}.Passser votre tour\n" "\n{2}.Fuir le combat"\
                  .format(len(Pokemon_choisi2.competence), len(Pokemon_choisi2.competence)+1, len(Pokemon_choisi2.competence)+2))
            print(" "), time.sleep(0.5)
            while True:
                opera5 = input("Qu'est ce que vous voulez faire :")
                time.sleep(0.5)
                # V??rifier d'abord que le command est acceptable
                if opera5.isdecimal() and int(opera5)>=0 and int(opera5) <=len(Pokemon_choisi2.competence)+3:
                    opera5 = int(opera5)
                    if opera5 < len(Pokemon_choisi2.competence): # Si le commande est l'utilisation de comp??tence, donc utiliser-la
                        Pokemon_choisi2.utiliserCompet(Pokemon_choisi2.competence[opera5], Pokemon_choisi)
                        break
                    elif opera5 == (len(Pokemon_choisi2.competence)):
                        print("Votre Pokemon actuelle est {}".format(Pokemon_choisi2.nom)), print(" "), time.sleep(0.5)
                        Pokemon_choisi2 = self.dresseur2.changerPokemon()
                        break
                    elif opera5 == (len(Pokemon_choisi2.competence)+1):
                        print("Vous avez pass?? votre tour !")
                        break
                    else:
                        print("{0} est d??faite!!!!!!!!!, {1} gagne le combat".format(self.dresseur2.nom, self.dresseur.nom))
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
            #A la fin du tour de dresseur 2, on v??rifier si la vie du pok??mon actif du dresseur 1 = 0 ou pas,
            #Si oui et si il a encore des autres pok??mons disponible, alores changer pok??mon et continuer.
            #Si non, le combat termine, les pok??mon du dresseur 2 gagnent l'exp, augmentent niveau, ??voluent.
            if  Pokemon_choisi.vie == 0:
                print("{0} de {1} est ??t?? KO".format(Pokemon_choisi.nom, self.dresseur.nom))
                if self.dresseur.deck[0].vie == 0 and self.dresseur.deck[1].vie == 0 and self.dresseur.deck[2].vie == 0 :
                    print ("Tous les Pokemons de {0} sont ??t?? KO, {0} perd le combat!, {1} gange le combat !"\
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
            #A la fin du tour, les pok??mons restaurent automatiquement une certaine quantit?? d'??nergie.     
            print(" "), time.sleep(0.5)
            self.regen_energie_automatique(Pokemon_choisi, Pokemon_choisi2)
            print(" "), time.sleep(0.5)
        #Enfin du combat,  les pok??mons revient ?? le meilleur ??tat.    
        self.regen_max()
        
    # La fonciton d??roule le Combat Humain contre Ordinateur 
    def HumainvsOrdi(self):
        """
        Fonction permet de d??crouler le combat Humain contre Ordinateur.
        Tout comme la fonciont pr??c??dente "tour_par_tour", la partie du dresseur est pareille, mais 
        la partie du dresseur 2 est remplac?? par IA. Dans la tour de IA, la class IA et ses fonction contr??lent 
        les op??ration de IA.
        """
        self.regen_max()
        #On r??cup??re les pok??mon actives.
        Pokemon_choisi, Pokemon_choisi2 = self.debutCombat_IA()
        time.sleep(0.5)
        print("la pokemon choisi de {} est {}".format(self.dresseur.nom, Pokemon_choisi.nom)),     time.sleep(0.5), print("  ")
        print("la pokemon choisi de {} est {}".format(self.__dresseur2.nom, Pokemon_choisi2.nom)), time.sleep(0.5), print("  ")
        flag = True
        for i in range (1000): 
            print("=======Tour {}=======".format(i+1)),              print(" "), time.sleep(0.5) 
            print("c'est ?? {0} de jouer".format(self.dresseur.nom)), print(" "), time.sleep(0.5)
            print("le profil de votre pokemon choisit est \n"),                  time.sleep(0.5)
            print(Pokemon_choisi), time.sleep(0.5),                  print(" "), time.sleep(0.5)
            #Afficher les comp??tence du pok??mon actif du dresseur 1
            for i in range(len(Pokemon_choisi.competence)):
                print('{0}.{1}\n'.format(i, Pokemon_choisi.competence[i]))
            time.sleep(0.5)    
            #Afficher les op??rations de changer de Pok??mon actif, de passer le tour et de fuir le combat
            print("{0}.Changer Pokemon\n" "\n{1}.Passser votre tour\n" "\n{2}.Fuir le combat"\
                  .format(len(Pokemon_choisi.competence), len(Pokemon_choisi.competence)+1, len(Pokemon_choisi.competence)+2))
            print(" "), time.sleep(0.5)
            #Dresseur fait son op??ration
            while True:
                opera2 = input("Qu'est ce que vous voulez faire :")
                time.sleep(0.5)
                # V??rifier d'abord que le command est acceptable
                if opera2.isdecimal() and int(opera2)>=0 and int(opera2) <=len(Pokemon_choisi.competence)+3:
                    opera2 = int(opera2)
                    if opera2 < len(Pokemon_choisi.competence):        #Si le commande est l'utilisation de comp??tence, donc utiliser-la
                        Pokemon_choisi.utiliserCompet(Pokemon_choisi.competence[opera2], Pokemon_choisi2)
                        break
                    elif opera2 == (len(Pokemon_choisi.competence)):   #En utilisant la fonction "changerPokemon" pour changer pok??mon
                        Pokemon_choisi = self.dresseur.changerPokemon()
                        break
                    elif opera2 == (len(Pokemon_choisi.competence)+1): #Passer le tour
                        print("Vous avez pass?? votre tour !")
                        break
                    else: # d??clarer forfait
                        print("{0} est d??faite!!!!!!!, {1} gagne le combat".format(self.dresseur.nom, self.__dresseur2.nom))
                        flag = False
                        # Si dresseur 1 ??choue son combat, les pokemons d'IA gagnent l'??xp??rience et ??voluent.
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
            #A la fin du tour de dresseur 1, on v??rifier si la vie du pok??mon actif d'IA' = 0 ou pas,
            #Si oui et si il a encore des autres pok??mons disponible, alores changer pok??mon et continuer.
            #Si non, le combat termine, les pok??mon du dresseur 1 gagnent l'exp, augmentent niveau, ??voluent.
            if  Pokemon_choisi2.vie == 0:
                print("{0} de {1} est ??t?? KO".format(Pokemon_choisi2.nom, self.__dresseur2.nom))
                if self.__dresseur2.deck[0].vie == 0 and self.__dresseur2.deck[1].vie == 0 and self.__dresseur2.deck[2].vie == 0 :
                    print ("Tous les Pokemons de {0} sont ??t?? KO, {0} perd le combat!, {1} gange le combat !"\
                           .format(self.__dresseur2.nom, self.dresseur.nom))
                    print("Le combat se termine")
                    for i in self.dresseur.deck:
                        i.gangerExperienceJCJ(self.__dresseur2)
                        i.augementerNiveau()
                        print(" ")
                    self.dresseur.evolution()
                    break
                else: #Else, changer le pok??mon actif et continuer
                    print("Il faut choisir un autre pokemon pour continuer le combat")
                    Pokemon_choisi2 = self.dresseur2.choisirPokeDepart()
                    print("{0} choisit {1} pour continue le combat".format(self.__dresseur2.nom, Pokemon_choisi2.nom))
            # Passer ?? la tour d'IA, IA fait op??ration en fonction de difficult?? 
            print("----------------------------")
            self.dresseur2.utiliserCompetence(Pokemon_choisi2, Pokemon_choisi)
            #Avant de passer le tour suivant, il faut tester si le pokemon actif du dresseur peut contuner ?? combattre
            #Si non, il faut changer le pok??mon actif, si la vie tous les pokemons dans deck = 0, alors dresseur
            #??choue le combat.
            if  Pokemon_choisi.vie == 0:
                print(" "), print("Votre pokemon est ??t?? KO")
                if self.dresseur.deck[0].vie == 0 and self.dresseur.deck[1].vie == 0 and self.dresseur.deck[2].vie == 0 :
                    print ("Tous vos Pokemons dans Deck sont ??t?? KO, D??faite !")
                    print("Le combat se termine")
                    break
                else:#Changer le pokemon actif
                    print("Il faut choisir un autre pokemon pour continuer le combat")
                    Pokemon_choisi = self.dresseur.changerPokemon()
            #A la fin du tour, les pok??mons restaurent automatiquement une certaine quantit?? d'??nergie.         
            print(" "), time.sleep(0.5)
            self.regen_energie_automatique(Pokemon_choisi,Pokemon_choisi2)
            print(" "), time.sleep(0.5)
        #Enfin du combat,  les pok??mons revient ?? le meilleur ??tat.     
        self.regen_max()        
        
#%% La classe de CombatJcE                    
class CombatJcE(Combat):
    
    """
    La class CombatJcE h??rite la classe Combat. 
    Sauf le dresseur "vous", il faut d??clare un autre attribut "pokemons" qui repr??sente 
    le pokemon sauvage.
    
    Nous avons re??crit les fonctions arbitraire, de plus, nous avons ajout?? une fonction "utiliseComp_poke"
    qui permet le pokemon sauvage utilise ses comp??tence al??atoirement.
    """
    def __init__(self, dresseur, pokemon2):
        super().__init__(dresseur)
        self.__pokemon2 = pokemon2
    
    # On red??finir la fonciton "regen_max" afin d'adapter la class "CombatJcE"
    def regen_max(self):
        for i in range (len(self.dresseur.deck)):
            self.dresseur.deck[i].vie = self.dresseur.deck[i].vie_max         # Restaurer la vie en vie maximale du dresseur
            self.dresseur.deck[i].energie = self.dresseur.deck[i].energie_max # Restaurer l'??nergie en ??nergie maximale du dresseur
        self.__pokemon2.vie = self.__pokemon2.vie_max                         # Restaurer la vie en vie maximale du pokemon
        self.__pokemon2.energie = self.__pokemon2.energie_max                 # Restaurer l'??nergie en ??nergie maximale du pokemon
    
    # Op??ration d'IA      
    def utiliseComp_poke(self, but):
        #Fonction permet le pokemon sauvage utilise ses comp??tence al??atoirement
        compeUtilise = self.__pokemon2.competence[random.randint(0, len(self.__pokemon2.competence)-1)]
        self.__pokemon2.utiliserCompet(compeUtilise, but) # En utilisant la fonciton "utiliserCompet" pour utiliser la comp??tence

    # Commencer ?? se battre               
    def debutCombat (self):
        """
        De m??me, Cette fonciton affiche les informations de Cambat au d??but du combat et permet le dresseur choisit 
        sa pok??mon ?? faire le combat.
        Enfin, cette fonction return le pok??mon actif
        """
        print(" ")
        print("Combat commence, votre adversaire est {}".format(self.__pokemon2.nom))
        print("Veuillez Choisir un pokemon pour combattre : (0-2)"), time.sleep(0.5), print(" ")
        while True:
            self.dresseur.voirdeck(), time.sleep(0.5) #Afficher les informations du pok??mon
            opera = input()
            if opera == "0" or opera == "1" or opera == "2": #V??rifier si le command est acceptable
                time.sleep(0.5)
                return self.dresseur.deck[int(opera)]
            else:
                print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")   

    #La fonction d??roule le combat dresseur contre pok??mon
    def tour_par_tour(self):
        """
        De m??me, cette fontion d??roule le combat dresseur contre pok??mon. Apr??s r??cup??rer le pok??mons actif, la principale partie
        de la fonction est une boucle : chaque it??ration le programme affiche le menu d'op??ration,  le dresseur peut soit utiliser une 
        comp??tence de son Pokemon actif, soit choisir de remplacer son Pokemon actif par un autre Pokemon de son deck, soit capture 
        le pok??mon, soit passer son tour ou d??clarer forfait.
        
        Comme le caiher de charge, le dresseur peut essayer de capture le pok??mon quand la vie du pok??mon descend en-dessous de 20%.
        
        A la fin de chaque it??ration(tour),  les pok??mons restaurent automatiquement une certaine quantit?? d'??nergie.
        
        Le combat s???arr??te si les 3 Pokemons du deck du dresseur sont ko ou si l???un des dresseurs d??clare forfait ou
        la vie du pok??mon sauvage = 0 ou le pok??mon ??t?? captur??.
        
        A la fin du combat, les pok??mons gagnent l'exp??rience, ??voluent et revient ?? le meilleur ??tat (Vie, ??nergie).
        """
        self.regen_max()
        Pokemon_choisi = self.debutCombat() #R??cup??rer le pok??mon actif
        print("Combat JCE commence, |{0}|  ===VS===  |{1}|"\
               .format(Pokemon_choisi.nom, self.__pokemon2.nom)),  print(" ")
        time.sleep(0.5)
        print("Votre pokemon choisi est {}".format(Pokemon_choisi.nom)), time.sleep(0.5), print(" ")
        flag = True #"flag" permet de break la boucle
        for i in range (1000): 
            #Afficher le menu d'op??ration du dresseur
            print("=======Tour {}=======".format(i+1)),              time.sleep(0.5), print(" ")
            print("c'est ?? {0} de jouer".format(self.dresseur.nom)), time.sleep(0.5), print(" "),
            print("le profil de votre pokemon choisit est : "),      time.sleep(0.5), print(" ")
            print(Pokemon_choisi),                                   time.sleep(0.5), print(" ")
            
            for i in range(len(Pokemon_choisi.competence)):
                print('{0}.{1}\n'.format(i, Pokemon_choisi.competence[i])), 
            time.sleep(0.5)    

            #Afficher les op??rations de capturer le Pok??mon, de changer le Pok??mon actif, 
            #de passer le tour et de fuir le combat
            print("{0}.Changer Pokemon\n" "\n{1}.Capturer ce Pokemon\n" "\n{2}.Passser votre tour\n" "\n{3}.Fuir le combat"\
                  .format(len(Pokemon_choisi.competence), len(Pokemon_choisi.competence)+1, len(Pokemon_choisi.competence)+2, len(Pokemon_choisi.competence)+3))
            print(" "), time.sleep(0.5)
            #Dresseur fait son op??ration
            while True:
                opera2 = input("Qu'est ce que vous voulez faire :")
                time.sleep(0.5)
                # V??rifier d'abord que le command est acceptable
                if opera2.isdecimal() and int(opera2)>=0 and int(opera2) <= len(Pokemon_choisi.competence)+3:
                    if int(opera2) < len(Pokemon_choisi.competence):      #Si le commande est l'utilisation de comp??tence, donc utiliser-la
                        Pokemon_choisi.utiliserCompet(Pokemon_choisi.competence[int(opera2)], self.__pokemon2)
                        break
                    elif int(opera2) == (len(Pokemon_choisi.competence)): #En utilisant la fonction "changerPokemon" pour changer pok??mon
                        print("Votre Pokemon actuelle est {}".format(Pokemon_choisi.nom)), print(" "), time.sleep(0.5)
                        Pokemon_choisi = self.dresseur.changerPokemon()
                        break
                    elif int(opera2) == (len(Pokemon_choisi.competence)+1):
                        #Afin de capturer le pok??mon, il faut d'abord tester si la vie du pok??mon descend en-dessous de 20%
                        if self.__pokemon2.vie > 0.2*self.__pokemon2.vie_max:  
                            print("Pas possible! Ressayez quand la vie de Pokemon descend en-dessous de 20% de sa vie max !\n"), time.sleep(1)
                            break
                        else:
                            # Si la condition de limite est satisfait, on peut essayer de le capture. 
                            # Calculer la possibilit?? de r??ussite
                            possibilite = 4*(0.2 - self.__pokemon2.vie / self.__pokemon2.vie_max)
                            aleatoire = random.uniform(0,1)
                            if aleatoire <= possibilite:
                                self.dresseur.capturerPokemon(self.__pokemon2) #R??ussir ?? capturer, le combat termine.
                                flag = False
                                break
                            else: # ??chouer de capturer, le combat continue. 
                                print("D??sol??, Capturer echoue !\n"), time.sleep(0.5)
                                break
                    elif int(opera2) == (len(Pokemon_choisi.competence)+2): #Passer la tour
                        print("Vous avez pass?? votre tour !")
                        break
                    else: # d??clarer forfait
                        print("!!!!!!D??faite!!!!!!")
                        flag = False
                        break
                else:
                    print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
            if not flag: 
                break
            print(" "), time.sleep(0.5)
            # A la fin du tour de dresseur, on v??rifier si la vie du pok??mon= 0 ou pas, si oui le combat termine
            # les pok??mon du dresseur gagnent l'exp, augmentent niveau, ??voluent.
            if self.__pokemon2.vie == 0:
                print("KO!!! Vous avez gagner le combat!!")
                print("Le combat se termine")
                for i in self.dresseur.deck:
                    i.gangerExperienceJCE(self.__pokemon2)
                    i.augementerNiveau()
                    print(" ")
                self.dresseur.evolution()
                break
            else: #Si non, en utilisant la fonciton "utiliseComp_poke", le pok??mon utilise la comp??tence al??atoire
                print("----------------------------")
                print("c'est ?? {0} de jouer\n{1}".format(self.__pokemon2.nom, self.__pokemon2)), time.sleep(0.5)
                self.utiliseComp_poke(Pokemon_choisi)
            #Avant de passer le tour suivant, il faut tester si le pokemon actif du dresseur peut contuner ?? combattre
            #Si non, il faut changer le pok??mon actif, si la vie tous les pokemons dans deck = 0, alors dresseur
            #??choue le combat.
            if  Pokemon_choisi.vie == 0:
                print("Votre pokemon est ??t?? KO")
                if self.dresseur.deck[0].vie == 0 and self.dresseur.deck[1].vie == 0 and self.dresseur.deck[2].vie == 0 :
                    print ("Tous vos Pokemons dans Deck sont ??t?? KO, d??faite !")
                    print("Le combat se termine")
                    break
                else:#Changer le pokemon actif
                    print("Il faut choisir un autre pokemon pour continuer le combat")
                    Pokemon_choisi = self.dresseur.changerPokemon()
            #A la fin du tour, les pok??mons restaurent automatiquement une certaine quantit?? d'??nergie.        
            print(" "), time.sleep(0.5)
            self.regen_energie_automatique(Pokemon_choisi, self.__pokemon2 )
            print(" "), time.sleep(0.5)
        #Enfin du combat,  les pok??mons revient ?? le meilleur ??tat.
        self.regen_max()
        
#%% Fonction pour quitter le jeu
def quitter():# La fonction pour quitter le jeu
    sys.exit(0)
    
# Cr??er un nouveau joueur
def creerNouveauDresseur(lesPokemons):
    """
    Cette fonction pour cr??er un nouveau dresseur, comme la fonciton ci-dessus, il nous fournit deux
    m??thodes de choix d'un Pok??mon : le joueur choisit 6 Pok??mon soit-m??me, ou il obtient six Pok??mon 
    au hasard. Enfin, cette fonciton return les informations du dresseur: "nom", "deck", "tousVosPokemons".
    """
    nom = input("Saisissez votre nom:")
    print('Votre nom est:{}'.format(nom)), time.sleep(0.3) 
    print("{} est n??!".format(nom)),       print('')
    while True:
        opera2 = input("Pour l'instant, nous pouvons vous fournir six Pok??mons initiaux de Niveau 1, vous pouvez(0-1) :\
                       \n\n0. Choisissez votre 6 Pok??mons initiaux par vous-m??me. \n1. Nous vous fournissons al??atoirement six Pok??mons initiaux")        
        if opera2 == "0":  # Le joueur choisit 6 Pok??mon soi-m??me
            deck, tousVosPokemons  = chosirPokemon(lesPokemons)
            return nom, deck, tousVosPokemons    
        elif opera2 =="1": # Il obtient six Pok??mon au hasard.
            deck, tousVosPokemons = aleatoire(lesPokemons)
            return nom, deck, tousVosPokemons
        else:
            print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
            
#%% Choisir Pok??mon 
def chosirPokemon(TousPokemons):
    """
    Cette fonciton permet de chosit 6 pok??mons initiaux. Avant chaque s??lection, nous v??rifions si nous avons d??ja 
    s??lectionn?? ce Pok??mon. L'entr??e "TousPokemons" est une liste de tous les objects de pok??mon.
    Enfin, cette fonction return deux liste: "deck" et "tousVosPokemons".
    """
    deck = []               # Deck
    tousVosPokemons = []    # Tous les pok??mons poss??d??s
    print('Choisissez votre six Pokemons initiaux :\n')
    for i in range(len(TousPokemons)):
        print("{0}.{1}".format(i, TousPokemons[i]))
    time.sleep(0.5)
    cpt = 1                 # Compter le nombre de pok??mons d??ja s??lection??s
    while True:
        while cpt  < 7 :
            input1=input('Choisissez votre compagnes(0-27)  N??{}:'.format(cpt))
            # V??rifier d'abord le commande est acceptable
            if input1.isdecimal() and int(input1) <= len(TousPokemons)-1:
                if TousPokemons[int(input1)] in tousVosPokemons: # V??rifier si nous avons d??ja s??lectionn?? ce Pok??mon
                    print("{0} est d??ja votre compagne!, veuillez Choisissez un autre Pokemon\n" \
                              .format(TousPokemons[int(input1)].nom)), time.sleep(0.3)
                else: # Ajouter ce pok??mon dans la liste "tousVosPokemons".
                    pokemon = TousPokemons[int(input1)]
                    print('Vous obtenez {}!'.format(pokemon.nom)), print(' ')
                    tousVosPokemons.append(pokemon)
                    cpt += 1
                    time.sleep(0.3)
            else:
                print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
        break
    # Eusuite, on choisit trois pok??mons pour construire le deck
    print("Maintenant, veuillez choisir trois Pok??mons ?? mettre dans votre deck"), print(" ")
    for i in range(len(tousVosPokemons)):
        print("{0},{1}".format(i, tousVosPokemons[i]))
    time.sleep(0.3)
    cpt = 1                 # Compter le nombre de pok??mons d??ja s??lection??s
    while True:
        while cpt  < 4 :
            print(" "), 
            input1=input('Choisissez votre Pok??mon dans Deck(0-5) N??{}:'.format(cpt))
            if input1.isdecimal() and int(input1) <= len(tousVosPokemons)-1:
                if tousVosPokemons[int(input1)] in deck:  # V??rifier si nous avons d??ja s??lectionn?? ce Pok??mon
                    print("{0} est d??ja dans votre deck !, veuillez Choisir un autre Pokemon\n" \
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
    Cette fonction permet au syst??me de nous aider ?? choisir au hasard six Pok??mon initiaux. 
    IL a exactement le m??me r??sultat que la fonction pr??c??dente. Avec l'aide de cette fonction,
    nous pouvons sauter l'??tape consistant ?? choisir nous-m??mes six Pok??mons et entrer le jeu directement.
    """
    deck = []
    tousVosPokemons = random.sample(TousPokemons,6)
    print("Votre compagnes sont : "), print(" ")
    for i in range(len(tousVosPokemons)):
        print("{0},{1}".format(i, tousVosPokemons[i]))
    print("Maintenant, veuillez choisir trois Pok??mons ?? mettre dans votre deck"), print(" ")
    time.sleep(0.5)
    cpt = 1        # Compter le nombre de pok??mons d??ja s??lection??s
    while True:
        while cpt  < 4 :
            print(" ")
            input1=input('Choisissez votre Pok??mon dans Deck(0-5) N??{}:'.format(cpt))
            # V??rifier d'abord le commande est acceptable
            if input1.isdecimal() and int(input1) <= len(tousVosPokemons)-1  :
                if tousVosPokemons[int(input1)] in deck:  # V??rifier si nous avons d??ja s??lectionn?? ce Pok??mon
                    print("{0} est d??ja dans votre deck !, veuillez Choisir un autre Pokemon\n"\
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