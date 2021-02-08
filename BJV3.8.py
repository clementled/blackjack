import random
import time
import os

os.system("cls")
print (' ')
print ("BLACK JACK MADE BY CLEMENT AND CYRIL ")
print ('si vous voulez nous aider, vous pouvez faire un don en cliquant sue le lien suivant : ')
print ("https://paypal.me/pools/c/8wIOjZl6W7")
print ('donateurs : Thibaut (1€) ')
time.sleep(5)
print (' ')

g = ['1','2','3','4','5','6','7','8','9','0']
nom = []
argent = []
partie = 0
cartes = [1,2,3,4,5,6,7,8,9,10,10,10,10]
rejouer = 'oui'
n = 0

def nbj (nom,nb) :
    confirmer = 'non'
    while confirmer not in ('oui','ui','yes','yep') :
        for i in range (nb) :
            nom.append(input("nom du joueur : "))
            time.sleep(0.5)
            while nom[i] in (' ') :
                del nom[i]
                nom.append(str(input("pardon ? ",)))           
            argent.append(str(input("combien avez-vous d'argent ? ",)))
            while argent[i][0] not in (g) :
                del argent[i]
                argent.append(str(input("combien avez-vous d'argent ? ",)))
            argent[i] = int(argent[i])
            time.sleep(0.6)
        for i in range (nb) :
            print (nom[i]," : ",argent[i],"$")
        confirmer = input("confirmer ? ",)
        while (confirmer.isdigit()) :
            print ('pardon ? ',)
            confirmer = input("confirmer ? ",)
        confirmer = str(confirmer)

    return 

def miser (nb) :
    for i in range (nb) :
        print (nom[i]," : ")
        mise.append(str(input("combien voulez-vous miser ? ", )))
        while mise[i][0] not in (g) :
            del mise[i]
            mise.append(str(input("combien voulez-vous miser (valeur positive) ? ",)))
        mise[i] = int(mise[i])
        if mise[i] < 0 :
            del mise[i]
            mise.append(int(input("combien voulez-vous miser ? (valeur positive) ", )))

        while mise[i] > argent[i] :
            del mise[i]
            print ("tu n'as pas assez d'argent") 
            mise.append(str(input("combien veux-tu miser cette fois espèce de voleur ? ", )))
            while mise[i][0] not in (g) :
                mise[i] = (str(input("combien voulez-vous miser (valeur positive) ? ",)))
            mise[i] = int(mise[i])
            if ( mise[i].isdigit()) :
                mise[i] = int(mise[i])
            else:
                del mise[i]
                nb = int(input("veuillez rentrer une valeur chifrée : ",))         
        argent[i] = argent[i] - mise[i]
    return

def deal (nb) :
    for i in range (nb) :
        for p in range (2) :
            cartepersonne[i].append(random.choice(cartes))
        if cartepersonne[i] == [10,1] or cartepersonne[i] == [1,10] :
            print (nom[i],": BLACK JACK, tu remportes 2x ta mise")
            argent[i] += 3 * mise[i]
            mise[i] = 0
    return

def pioche (double) :
    for i in range (nb) :
        print (nom[i],":")
        if cartepersonne[i] == [10,1] or cartepersonne[i] == [1,10] :
            print (nom[i],", tu as eu un Black Jack, tu as déja gagné")
        elif cartepersonne[i] != [10,1] and cartepersonne[i] != [1,10] and argent[i] - mise[i] >= 0 :
            double = str(input("veux tu doubler ta mise et prendre une dèrnière carte ? ",))
            while double[0] in (g) :
                double = (str(input("veux tu doubler ta mise et prendre une dèrnière carte ? ",)))
        if double in ('oui','yes','yep','ui','o') :
            cartepersonne[i].append(random.choice(cartes))
            mise[i] *= 2
            argent[i] -= mise[i] / 2
            if sum(cartepersonne[i]) > 21 :
                print (nom[i],", tu as perdu, tu as dépassé 21 ")
                prendrecarte = 'non'
                cartepersonne[i].append(99)
        if cartepersonne[i] != [10,1] and cartepersonne[i] != [1,10] and double not in ('oui','yes','yep','ui','o') :
            prendrecarte = input('veux-tu reprendre une carte ? ',)
            while prendrecarte[0] in (g) :
                prendrecarte = (str(input("veux-tu reprendre une carte ? ",)))
            while prendrecarte in ('oui','ui','o','yes','yep') :
                cartepersonne[i].append(random.choice(cartes))
                print ("tes cartes sont maintenant : ", cartepersonne[i], " total : ",sum(cartepersonne[i]))
                if sum(cartepersonne[i]) > 21 :
                    print (nom[i],", tu as perdu, tu as dépassé 21 ")
                    prendrecarte = 'non'
                    cartepersonne[i].append(99)
                else :
                    prendrecarte = input('veux-tu reprendre une carte ? ',)
                    while prendrecarte[0] in (g) :
                        prendrecarte = (str(input("veux-tu reprendre une carte ? ",)))
    return

def verif (nb) :
    for i in range (nb) :
        print (' ')
        time.sleep(0.75)
        print ("bilan",nom[i],":")
        if sum(cartepersonne[i]) > sum(croupier) and cartepersonne[i][-1] != 99 and cartepersonne[i][0:2] != [10,1] and cartepersonne[i][0:2] != [1,10] :
            print (nom[i],", tu as gagné, tu remporte ta mise")
            if croupier[-1] == 99 :
                print (nom[i],"tes cartes : ",cartepersonne[i]," total : ",sum(cartepersonne[i]))
                print ("cartes du croupier : ", croupier[0:-1]," total : ",sum(croupier[0:-1]))
            else :
                print (nom[i],"tes cartes : ",cartepersonne[i]," total : ",sum(cartepersonne[i]))
                print ("cartes du croupier : ", croupier," total : ",sum(croupier))
            argent[i] += 2 * mise[i]
        if sum(cartepersonne[i]) == sum(croupier) and cartepersonne[i][-1] != 99 and cartepersonne[i][0:2] != [10,1] and cartepersonne[i][0:2] != [1,10] :
                print (nom[i],", toi et le croupier êtes à égalité, tu es remboursé")
                print (nom[i],"tes cartes : ",cartepersonne[i],"total : ",sum(cartepersonne[i]))
                print ("cartes du croupier : ",croupier," total : ",sum(croupier))
                argent[i] += mise[i]
        if cartepersonne[i][-1] == 99 and cartepersonne[i][0:2] != [10,1] and cartepersonne[i][0:2] != [1,10] :
            if croupier[-1] == 99 :
                print (nom[i],", toi et le croupier avez dépassé 21")
                print (nom[i],"tes cartes : ",cartepersonne[i][0:-1]," total : ",sum(cartepersonne[i][0:-1]))
                print ("cartes du croupier : ", croupier[0:-1]," total : ",sum(croupier[0:-1]))
            else :
                print ("tu as perdu, tu avais dépassé 21")
                print (nom[i],"tes cartes : ",cartepersonne[i][0:-1]," total : ",sum(cartepersonne[i][0:-1]))
                print ("cartes du croupier : ", croupier," total : ",sum(croupier))
        if croupier[-1] == 99 and cartepersonne[i][0:2] != [10,1] and cartepersonne[i][0:2] != [1,10] :
            if cartepersonne[i][-1] != 99 :
                print ("tu as gagné, le croupier avait dépassé 21")
                print (nom[i],"tes cartes : ",cartepersonne[i]," total : ",sum(cartepersonne[i]))
                print ("cartes du croupier : ", croupier[0:-1]," total : ",sum(croupier[0:-1]))
                argent[i] += 2 * mise[i]
        if sum(croupier) > sum(cartepersonne[i]) and cartepersonne[i][-1] != 99 and croupier[-1] != 99 and cartepersonne[i][0:2] != [10,1] and cartepersonne[i][0:2] != [1,10] :
            print (nom[i],", le croupier t'a battu")
            print (nom[i],"tes cartes : ",cartepersonne[i]," total : ",sum(cartepersonne[i]))
            print ("cartes du croupier : ", croupier," total : ",sum(croupier))
        if cartepersonne[i] == [10,1] or cartepersonne[i] == [1,10] :
            print ('tu as eu un Black Jack')

def achat (g) :
    for i in range (nb) :
        print (' ')
        print (nom[i]," : ")
        time.sleep(0.5)
        demande = input("veux tu faire un achat ? ", )
        while demande[0] in (g) :
            demande = (str(input("veux tu faire un achat ? ",)))
        if demande in ('oui','ui','yes','yep','oe','ouais') :
            h = 0
            while h == 0 :
                for m in range (len(objet)) :
                    print (objet[m]," : ",objetargent[m],"$")
                time.sleep(0.4546)
                print(' ')
                selection = str(input("que veux tu acheter ? ", ))
                while selection[0] in (g) :
                    selection = (str(input("que veux tu acheter ? ",)))
                if selection in ('rien','nothing') :
                    h = 1
                for p in range (len(objet)) :
                    if selection == objet[p] :
                        if argent[i] - objetargent[p] < 0 :
                            print ("vous n'avez pas assez d'argent")
                        else :
                            objetpersonne[i].append(selection)
                            argent[i] -= objetargent[p]
                            print ("achat effectué")
                            print (' ')
                            time.sleep(0.6)
                            print ("tes bien :")
                            for v in range (len(objetpersonne[i])) :
                                print (objetpersonne[i][v])
                            print (' ')
                            time.sleep(.3456)
                            print ("il te reste à acheter :")
                            for g in range (len(objet)) :
                                if objet[g] not in objetpersonne[i] :
                                    print (objet[g])
                            print (' ')
                            time.sleep(0.3)
                            print ("argent : ",argent[i])
                            h = 1
    return
                    
def objets () :
    f = -1
    ajouterobj = 'oui'
    while ajouterobj in ('oui','ui','yes','yep','oe','ouais') :
        f += 1
        objet.append(str(input("quel objet veux tu ajouter ? ", )))
        time.sleep(0.5)
        objetargent.append(str(input("combien coûte cet objet ? ", )))
        while objetargent[f][0] not in (g) :
            objetargent[f] = str(input("combien coûte cet objet ? ",))
        objetargent[f] = int(objetargent[f])
        print (' ')
        ajouterobj = str(input("veux tu ajouter un objet ? ", ))
    print (' ')
    print ("les objets sont : ")
    for i in range (len(objet)) :
        print (objet[i]," : ",objetargent[i],"$")
    return



changermode = 'oui'
relancermode = 'oui'
choixmulti = 'oui'
while choixmulti in ('oui','ui','yes','yep') :
    multijoueur = str(input("veux tu jouer en multijoueur ? ", ))
    while multijoueur[0] in (g) :
            multijoueur = (str(input("veux tu jouer en multijoueur ? ",)))
    if multijoueur in ('oui','ui','yes','yep') :
        while changermode in ('oui','ui','yes','yep') :
            print ("jeux : normal / achats / battle royale")
            time.sleep(2.5)
            print (' ')
            modejeux = str(input("mode de jeux : ",))
            while modejeux[0] in (g) :
                modejeux = (str(input("mode de jeux : ",)))
            while modejeux not in ('normal','wtf','battle royal','br','achat','achats') :
                modejeux = str(input("mode de jeux : ",))
            if modejeux == 'normal' : 
                relancermode = 'oui'
                while relancermode in ('oui','ui','yes','yep') :
                    nb = str(input("à combien voulez-vous jouer ? ", ))
                    while nb[0] not in (g) :
                        nb = (str(input("à combien voulez-vous jouer ? ",)))
                    nb = int(nb)
                    print (' ')
                    time.sleep(1)
                    nbj (nom,nb)
                    print (' ')
                    time.sleep(0.398972)
                    while nb != 0 :
                        n += 1
                        print(" ")
                        print ('//////////////////// tour',n,'////////////////////')
                        time.sleep(0.36575495465757545)
                        print(" ")
                        for i in range (nb) :
                            time.sleep(0.62)
                            print (nom[i],',tu as ',argent[i],"$")
                        print (' ')
                        croupier = []
                        mise = []
                        cartepersonne = []
                        for i in range (nb) :
                            cartepersonne.append([])
                        miser (nb)
                        deal (nb)
                        time.sleep(0.456775)
                        print (" ")
                        for i in range (nb) :
                            print (nom[i]," : ",argent[i],"$  cartes : ",cartepersonne[i],"total : ",sum(cartepersonne[i]))
                        for i in range (2) :
                            croupier.append(random.choice(cartes))
                        print ("cartes du croupier : ",croupier[0],"/ ?")
                        print (' ')
                        time.sleep(0.56455)
                        pioche (0)
                        while sum(croupier) > 0 and sum(croupier) < 17 :
                                croupier.append(random.choice(cartes))
                                if sum(croupier) > 21 :
                                    croupier.append(99)
                        verif(nb)
                        print (' ')
                        for i in range (nb) :
                            time.sleep(0.62)
                            print (nom[i],',tu as ',argent[i],"$")
                        t = nb
                        for i in range (nb) :
                            t -= 1
                            if argent[t] == 0 : 
                                del nom[t]
                                del argent[t]
                                del cartepersonne[t]
                                nb -= 1
                            else :
                                pass

                        if nb > 0 :
                            continuer = str(input("continuer ? ", ))
                            while continuer[0] in (g) :
                                continuer = (str(input("continuer ? ",)))
                            if continuer in ('oui','ui','yes','yep') :
                                pass
                            else :
                                nb = 0
                        time.sleep(3)
                        os.system("cls")
                    relancermode = str(input("veux tu rejouer à ce mode de jeux ? ", ))
                    while relancermode[0] in (g) :
                        relancermode = (str(input("veux tu rejouer à ce mode de jeux ? ",)))
                changermode = str(input("veux tu changer de mode ? ", ))
                while changermode[0] in (g) :
                    changermode = (str(input("veux tu changer de mode ? ",)))

            elif modejeux in ('achats','achat') :
                relancermode = 'oui'
                while relancermode in ('oui','ui','yes','yep') :
                    objet = []
                    objetargent = []
                    objetpersonne = []
                    nb = str(input("à combien voulez-vous jouer ? ", ))
                    while nb[0] not in (g) :
                        nb = (str(input("à combien voulez-vous jouer ? ",)))
                    nb = int(nb)
                    for i in range (nb) :
                        objetpersonne.append([])
                    print (' ')
                    time.sleep(1)
                    nbj (nom,nb)
                    print (' ')
                    time.sleep(0.398972)
                    objets ()
                    while nb != 0 :
                            n += 1
                            print(" ")
                            print ('//////////////////// tour',n,'////////////////////')
                            time.sleep(0.36575495465757545)
                            print(" ")
                            for i in range (nb) :
                                time.sleep(0.62)
                                print (nom[i],',tu as ',argent[i],"$")
                            print (' ')
                            achat
                            croupier = []
                            mise = []
                            cartepersonne = []
                            for i in range (nb) :
                                cartepersonne.append([])
                            miser (nb)
                            deal (nb)
                            time.sleep(0.456775)
                            print (" ")
                            for i in range (nb) :
                                print (nom[i]," : ",argent[i],"$  cartes : ",cartepersonne[i],"total : ",sum(cartepersonne[i]))
                            for i in range (2) :
                                croupier.append(random.choice(cartes))
                            print ("cartes du croupier : ",croupier[0],"/ ?")
                            print (' ')
                            time.sleep(0.56455)
                            pioche (0)
                            while sum(croupier) > 0 and sum(croupier) < 17 :
                                    croupier.append(random.choice(cartes))
                                    if sum(croupier) > 21 :
                                        croupier.append(99)
                            verif(nb)
                            print (' ')
                            for i in range (nb) :
                                time.sleep(0.62)
                                print (nom[i],',tu as ',argent[i],"$")

                            t = nb
                            for i in range (nb) :
                                t -= 1
                                if argent[t] == 0 : 
                                    print (nom[t],", tu es éliminé")
                                    del nom[t]
                                    del argent[t]
                                    del cartepersonne[t]
                                    nb -= 1
                                    
                                else :
                                    pass
                            achat (g)
                            time.sleep(0.5)

                            for i in range (nb) :
                                o = 0
                                for f in range (len(objet)) :
                                    if objet[f] in objetpersonne[i] :
                                        o += 1
                                print (o)
                                if o == len(objet) :
                                    print (nom[i],"a gagné, il a acheté tous les objets")
                                    nb = 0
                            os.system("cls")

            
                    
                    time.sleep(3)
                    os.system("cls")
                    relancermode = str(input("veux tu rejouer à ce mode de jeux ? ", ))
                    while relancermode[0] in (g) :
                        relancermode = (str(input("veux tu rejouer à ce mode de jeux ? ",)))
                changermode = str(input("veux tu changer de mode ? ", ))
                while changermode[0] in (g) :
                    changermode = (str(input("veux tu changer de mode ? ",)))

            else :
                relancermode = 'oui'
                while relancermode in ('oui','ui','yes','yep') :
                    nb = 1
                    while nb < 2 :
                        print ("il faut être au moins 2 pour jouer à ce mode")
                        nb = input("à combien voulez-vous jouer ? ", )
                        while nb[0] not in (g) :
                            nb = (str(input("à combien voulez-vous jouer ? ",)))
                        nb = int(nb)
                    print (' ')
                    time.sleep(1)
                    confirmer = 'non'
                    while confirmer not in ('oui','ui','yes','yep') :
                        for i in range (nb) :
                            nom.append(input("nom du joueur : "))
                            time.sleep(0.5)
                            while nom[i] in (' ') :
                                del nom[i]
                                nom.append(str(input("pardon ? ",)))
                            confirmer = str(input("confirmer ? "))
                            while confirmer[0] in (g) :
                                confirmer = str(input("confirmer ? "))

                    argent = []
                    for i in range (nb) :
                        argent.append(1000)
                    print ("bienvenue dans le battle royal, ici, vous avez  tous 1000 $ et le dernier a avoir de l'argent remporte la partie")
                    print (' ')
                    time.sleep(0.398972)
                    n = 0
                    while nb != 0 :
                        n += 1
                        print(" ")
                        print ('//////////////////// tour',n,'////////////////////')
                        demon = n * 0.5
                        if n > 4 :
                            demon = n * 0.25
                        for i in range (nb) :
                            argent[i] -= 100 * demon
                        time.sleep(0.36575495465757545)
                        print(" ")
                        print ("de l'argent vous a été retirer")
                        t = nb
                        for i in range (nb) :
                            t -= 1
                            if argent[t] <= 0 : 
                                del nom[t]
                                del argent[t]
                                del cartepersonne[t]
                                nb -= 1
                            else :
                                pass
                        if nb == 0 :

                            print ("vous avez tous perdu")
                        if nb == 1 :
                            os.system("cls")
                            print (nom[0],"remporte la partie")
                            nb = 0


                        for i in range (nb) :
                            time.sleep(0.62)
                            print (nom[i],',tu as ',argent[i],"$")
                        print (' ')
                        croupier = []
                        mise = []
                        cartepersonne = []
                        for i in range (nb) :
                            cartepersonne.append([])
                        miser (nb)
                        deal (nb)
                        time.sleep(0.456775)
                        print (" ")
                        for i in range (nb) :
                            print (nom[i]," : ",argent[i],"$  cartes : ",cartepersonne[i],"total : ",sum(cartepersonne[i]))
                        if nb == 1 :
                            os.system("cls")
                        else :
                            for i in range (2) :
                                croupier.append(random.choice(cartes))
                            print ("cartes du croupier : ",croupier[0],"/ ?")
                        print (' ')
                        time.sleep(0.56455)
                        pioche (0)
                        while sum(croupier) > 0 and sum(croupier) < 17 :
                                croupier.append(random.choice(cartes))
                                if sum(croupier) > 21 :
                                    croupier.append(99)
                        verif(nb)
                        print (' ')
                        for i in range (nb) :
                            time.sleep(0.62)
                            print (nom[i],',tu as ',argent[i],"$")
                        t = nb
                        for i in range (nb) :
                            t -= 1
                            if argent[t] <= 0 : 
                                del nom[t]
                                del argent[t]
                                del cartepersonne[t]
                                nb -= 1
                            else :
                                pass
                        if nb == 0 :
                            print ("vous avez tous perdu")
                        if nb == 1 :
                            print (nom[1],"remporte la partie")
                            nb = 0

                        if nb > 0 :
                            continuer = str(input("continuer ? ", ))
                            while continuer[0] in (g) :
                                continuer = (str(input("continuer ? ",)))
                            if continuer in ('oui','ui','yes','yep') :
                                pass
                            else :
                                nb = 0
                            time.sleep(3)
                            os.system("cls")
                    relancermode = str(input("veux tu rejouer à ce mode de jeux ? ", ))
                    while relancermode[0] in (g) :
                            relancermode = (str(input("veux tu rejouer à ce mode de jeux ? ",)))
                changermode = str(input("veux tu changer de mode ? ", ))
                while changermode[0] in (g) :
                    changermode = (str(input("veux tu changer de mode ? ",)))
        choixmulti = str(input("retour au menu 'multi ou  solo' ? ",))
        while choixmulti[0] in (g) :
            choixmulti = (str(input("retour au menu 'multi ou  solo' ? ",)))
    else :
        print ("prochainement disponible")