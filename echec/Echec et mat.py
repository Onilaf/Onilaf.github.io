import pygame
pygame.init() #faire pip install pygame pour lancer le programme

class Plateau:
    def __init__(self):
        self.tour = True
        self.blanc = False
        self.fin = False
        self.info = False
        self.clic = None
        self.observateur = False
        self.plateau = []
        self.pions = []
        self.historique = []
        self.tab120 = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,56,57,58,59,60,61,62,63,-1,-1,48,49,50,51,52,53,54,55,-1,-1,40,41,42,43,44,45,46,47,-1,-1,32,33,34,35,36,37,38,39,-1,-1,24,25,26,27,28,29,30,31,-1,-1,16,17,18,19,20,21,22,23,-1,-1,8,9,10,11,12,13,14,15,-1,-1,0,1,2,3,4,5,6,7,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1)
        self.tab64 = (91,92,93,94,95,96,97,98,81,82,83,84,85,86,87,88,71,72,73,74,75,76,77,78,61,62,63,64,65,66,67,68,51,52,53,54,55,56,57,58,41,42,43,44,45,46,47,48,31,32,33,34,35,36,37,38,21,22,23,24,25,26,27,28)
        for y in range(8):
            self.blanc = not self.blanc
            for x in range(8):
                self.pions.append(Pion())
                self.blanc = not self.blanc
                self.plateau.append(Case(x,y,self.blanc))
                if y == 1:
                    self.pions[x+y*8] = Pion("pion","blanc")
                elif y == 6:
                    self.pions[x+y*8] = Pion("pion","noir")
        self.pions[0] = Pion("tour","blanc","gauche")
        self.pions[1] = Pion("cavalier","blanc")
        self.pions[2] = Pion("fou","blanc")
        self.pions[3] = Pion("dame","blanc")
        self.pions[4] = Pion("roi","blanc")
        self.pions[5] = Pion("fou","blanc")
        self.pions[6] = Pion("cavalier","blanc")
        self.pions[7] = Pion("tour","blanc","droit")
        self.pions[56] = Pion("tour","noir","gauche")
        self.pions[57] = Pion("cavalier","noir")
        self.pions[58] = Pion("fou","noir")
        self.pions[59] = Pion("dame","noir")
        self.pions[60] = Pion("roi","noir")
        self.pions[61] = Pion("fou","noir")
        self.pions[62] = Pion("cavalier","noir")
        self.pions[63] = Pion("tour","noir","droit")

    def echec_et_pat(self,couleur):
        if couleur:
            couleur = "blanc"
        else:
            couleur = "noir"
        for i in range(64):
            aller = self.peut_aller(i)
            if self.pions[i].couleur == couleur:
                for place in aller:
                    if not self.echec(couleur,[i,place]):
                        return None
                if self.echec(couleur):
                    self.fin = "echec et mat aux "+couleur+"s"
                else:
                    self.fin = "pat aux "+couleur+"s"
                self.info = False

    def echec(self,couleur,bouge=None):
        self.verif_blanc = []
        self.verif_noir = []
        self.roi_blanc = None
        self.roi_noir = None
        if bouge:
            sauvegarde = self.clic
            self.move(bouge[0],bouge[1])
        for i in range(64):
            if self.pions[i].couleur == "blanc":
                if self.pions[i].nature == "roi":
                    self.roi_blanc = i
                if self.peut_aller(i):
                    for j in self.peut_aller(i):
                        self.verif_blanc.append(j)
            else:
                if self.pions[i].nature == "roi":
                    self.roi_noir = i
                if self.peut_aller(i):
                    for j in self.peut_aller(i):
                        self.verif_noir.append(j)
        if bouge:
            self.retour()
            self.clic = sauvegarde
            self.plateau[sauvegarde].brillant = pygame.image.load("images/autres/clic.png")
        self.verif_blanc = list(set(self.verif_blanc))
        self.verif_noir = list(set(self.verif_noir))
        if couleur == "blanc" and self.roi_blanc in self.verif_noir:
            self.info = "echec aux "+couleur+"s"
            return True
        if couleur == "noir" and self.roi_noir in self.verif_blanc:
            self.info = "echec aux "+couleur+"s"
            return True
        self.info = False
        return False

    def cliquer(self,case):
        self.observateur = False
        if self.clic != None and self.pions[case].choisit:
            self.move(self.clic,case)
            self.echec_et_pat(self.tour)
        for i in range(64):
            self.pions[i].choisit = False
            self.plateau[i].brillant = pygame.image.load("images/autres/rien.png")
        if self.pions[case].nature != None:
            if (self.tour and self.pions[case].couleur == "blanc") or (not self.tour and self.pions[case].couleur == "noir"):
                self.plateau[case].brillant = pygame.image.load("images/autres/clic.png").convert_alpha()
                self.clic = case
                self.pions[case].aller = self.peut_aller(case)
                for i in self.pions[case].aller:
                    self.pions[i].choisit = True
        else:
            self.clic = None

    def peut_aller(self,place):
        if self.pions[place].nature != None:
            lst = []
            color = "noir"
            if self.pions[place].couleur == "noir":
                color = "blanc"
            passant = -1
            if self.historique:
                if self.historique[-1][2].nature == "pion" and self.historique[-1][0]-self.historique[-1][1] in [16,-16]:
                    passant = int((self.historique[-1][0]+self.historique[-1][1])/2)
            if self.pions[place].nature == "pion":
                if color == "noir":
                    if self.pions[place+8].nature == None:
                        lst.append(place+8)
                        if place not in [48,49,50,51,52,53,54,55]:
                            if self.pions[place+16].nature == None and place in [8,9,10,11,12,13,14,15]:
                                lst.append(place+16)
                    if self.pions[place+7].couleur == color or passant == place+7:
                        lst.append(place+7)
                    if self.pions[place+9].couleur == color or passant == place+9:
                        lst.append(place+9)
                else:
                    if self.pions[place-8].nature == None:
                        lst.append(place-8)
                        if place not in [8,9,10,11,12,13,14,15]:
                            if self.pions[place-16].nature == None and place in [48,49,50,51,52,53,54,55]:
                                lst.append(place-16)
                    if self.pions[place-7].couleur == color or passant == place-7:
                        lst.append(place-7)
                    if self.pions[place-9].couleur == color or passant == place-9:
                        lst.append(place-9)
            if self.pions[place].nature == "cavalier" or self.pions[place].nature == "roi":
                for i in self.pions[place].deplacement:
                    if self.tab120[self.tab64[place]+i] != -1:
                        if self.pions[self.tab120[self.tab64[place]+i]].couleur in [color, None]:
                            lst.append(self.tab120[self.tab64[place]+i])
            if self.pions[place].nature == "tour" or self.pions[place].nature == "fou" or self.pions[place].nature == "dame":
                for i in self.pions[place].deplacement:
                    k=1
                    while True:
                        if self.tab120[self.tab64[place]+(i*k)] != -1:
                            if self.pions[self.tab120[self.tab64[place]+(i*k)]].couleur in [color, None]:
                                lst.append(self.tab120[self.tab64[place]+(i*k)])
                            else:
                                break
                        else:
                            break
                        if self.pions[self.tab120[self.tab64[place]+(i*k)]].couleur != None:
                            break
                        k+=1
            if not self.observateur:
                self.observateur = True
                if self.pions[place].nature == "roi":
                    blanc = [True,True,True]
                    noir = [True,True,True]
                    for i in self.historique:
                        if i[2].nature == "roi" and i[2].couleur == "blanc":
                            blanc[0] = False
                        elif i[2].nature == "roi" and i[2].couleur == "noir":
                            noir[0] = False
                        elif i[2].nature == "tour" and i[2].couleur == "blanc":
                            if i[2].tours == "gauche":
                                blanc[1] = False
                            else:
                                blanc[2] = False
                        elif i[2].nature == "tour" and i[2].couleur == "noir":
                            if i[2].tours == "gauche":
                                noir[1] = False
                            else:
                                noir[2] = False
                    if self.pions[place].couleur == "blanc" and blanc[0]:
                        if self.pions[5].nature == None and self.pions[6].nature == None and blanc[2]:
                            if not self.echec("blanc") and not self.echec("blanc",[4,5]) and not self.echec("blanc",[4,6]):
                                lst.append(6)
                        if self.pions[3].nature == None and self.pions[2].nature == None and self.pions[1].nature == None and blanc[1]:
                            if not self.echec("blanc") and not self.echec("blanc",[4,3]) and not self.echec("blanc",[4,2]):
                                lst.append(2)
                    elif self.pions[place].couleur == "noir" and noir[0]:
                        if self.pions[61].nature == None and self.pions[62].nature == None and noir[2]:
                            if not self.echec("noir") and not self.echec("noir",[60,61]) and not self.echec("noir",[60,62]):
                                lst.append(62)
                        if self.pions[59].nature == None and self.pions[58].nature == None and self.pions[57].nature == None and noir[1]:
                            if not self.echec("noir") and not self.echec("noir",[60,59]) and not self.echec("noir",[60,58]):
                                lst.append(58)
                sauv = []
                for tout in lst:
                    if self.echec(self.pions[place].couleur,[place,tout]):
                        sauv.append(lst.index(tout))
                for azerty in range(len(sauv)):
                    del lst[sauv[-1]]
                    del sauv[-1]
            return lst

    def move(self,a,b):
        self.historique.append([a,b,self.pions[a],self.pions[b],None,None])
        if len(self.historique)>1:
            if self.pions[a].nature == "pion" and self.historique[-2][2].nature == "pion" and self.historique[-2][0]-self.historique[-2][1] in [-16,16]:
                if a-b in [-7,9] and self.historique[-2][1] == a-1:
                    self.historique[-1][4] = [a-1,self.pions[a-1]]
                    self.pions[a-1] = Pion()
                if a-b in [7,-9] and self.historique[-2][1] == a+1:
                    self.historique[-1][4] = [a+1,self.pions[a+1]]
                    self.pions[a+1] = Pion()
            if self.pions[a].nature == "roi" and a-b in [-2,2]:
                if b in [2,58]:
                    place = b-2
                    place2 = b+1
                elif b in [6,62]:
                    place = b+1
                    place2 = b-1
                self.historique[-1][5] = [b,place2]
        self.pions[b] = self.pions[a]
        self.pions[a] = Pion()
        if type(self.historique[-1][5]) == list:
            self.historique[-1][1] = place
            self.historique[-1][3] = self.pions[place]
            self.pions[place2] = self.pions[place]
            self.pions[place] = Pion()
        self.tour = not self.tour

    def retour(self):
        self.fin = False
        self.clic = None
        for i in range(64):
            self.pions[i].choisit = False
            self.plateau[i].brillant = pygame.image.load("images/autres/rien.png")
        change = self.historique[-1]
        self.pions[change[0]] = change[2]
        self.pions[change[1]] = change[3]
        if type(change[5]) == list:
            self.pions[change[5][0]] = Pion()
            self.pions[change[5][1]] = Pion()
        elif type(change[4]) == list:
            self.pions[change[4][0]] = change[4][1]
        del self.historique[-1]
        self.tour = not self.tour

    def reine(self,case):
        if (self.pions[case].nature == "pion") and ((self.pions[case].couleur == "blanc" and case in [56,57,58,59,60,61,62,63]) or (self.pions[case].couleur == "noir" and case in [0,1,2,3,4,5,6,7])):
            self.pions[case] = Pion("dame",self.pions[case].couleur)


class Pion(pygame.sprite.Sprite):
    def __init__(self,nature=None,couleur=None,tours=None):
        super().__init__()
        self.nature = nature
        self.couleur = couleur
        self.tours = tours
        self.choisit = False
        self.aller = None
        if nature and couleur:
            self.image = pygame.image.load("images/pieces/"+nature+"_"+couleur+".png")
        else:
            self.image = pygame.image.load("images/autres/rien.png")
        if nature == "tour":
            self.deplacement = [10,1,-10,-1]
        elif nature == "fou":
            self.deplacement = [11,-9,-11,9]
        elif nature == "cavalier":
            self.deplacement = [21,12,-8,-19,-21,-12,8,19]
        elif nature == "roi" or nature == "dame":
            self.deplacement = [10,1,-10,-1,11,-9,-11,9]


class Case(pygame.sprite.Sprite):
    def __init__(self,x,y,couleur):
        super().__init__()
        self.brillant = pygame.image.load("images/autres/rien.png")
        self.image = pygame.image.load("images/autres/"+str(couleur)+".png")
        self.rect = self.image.get_rect()
        self.rect.y = 498-64*y
        self.rect.x = 125+64*x

fenetre = pygame.display.set_mode((662,612))
pygame.display.set_caption("Echec")
pygame.display.set_icon(pygame.image.load("images/autres/icone.png"))
running = True
fond = pygame.image.load("images/autres/fond.png")
game = Plateau()
buttonplay = pygame.transform.scale(pygame.image.load("images/autres/play.png"),(100,75))
buttonplay_rect = buttonplay.get_rect()
buttonretour = pygame.transform.scale(pygame.image.load("images/autres/retour.png"),(100,75))
buttonretour_rect = buttonretour.get_rect()
buttonretour_rect.y = 100


while running:
    fenetre.blit(fond,(0,0))
    fenetre.blit(buttonplay,buttonplay_rect)
    fenetre.blit(buttonretour,buttonretour_rect)
    if game.tour:
        tour = "blanc"
        couleur = (255,255,255)
    else:
        tour = "noir"
        couleur = (0,0,0)
    fenetre.blit(pygame.font.SysFont("Ink Free",25).render("aux {}s".format(tour),True,couleur,(64,64,64)),[0,200])
    if game.echec(tour):
        fenetre.blit(pygame.font.SysFont("Ink Free",25).render("{}".format(game.info),True,(255,0,0),(64,64,64)),[300,10])
    if game.fin:
        fenetre.blit(pygame.font.SysFont("Ink Free",25).render("{}".format(game.fin),True,(255,0,0),(64,64,64)),[250,10])
    for case in range(64):
        game.reine(case)
        if game.pions[case].choisit == True:
            game.plateau[case].brillant = pygame.image.load("images/autres/move.png").convert_alpha()
        fenetre.blit(game.plateau[case].image,game.plateau[case].rect)
        if game.pions[case] != None:
            fenetre.blit(game.pions[case].image,game.plateau[case].rect)
        fenetre.blit(game.plateau[case].brillant,game.plateau[case].rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if buttonplay_rect.collidepoint(event.pos):
                game = Plateau()
            elif buttonretour_rect.collidepoint(event.pos) and game.historique:
                game.retour()
            for case in range(64):
                if game.plateau[case].rect.collidepoint(event.pos) and not game.fin:
                    game.cliquer(case)