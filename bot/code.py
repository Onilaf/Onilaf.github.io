import discord
import asyncio
import random
from discord.ext import commands

# permettre l'audio avec la commande f!voc.

global prefix
global activity
TOKEN = "caché"
prefix = "f!"
activity = discord.Game(name=prefix+"help")
bot = commands.Bot(command_prefix = commands.when_mentioned_or(prefix))
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Funny est READY !!!")
    await bot.change_presence(activity=activity)

def jeux(action,perso=None):
    global start
    global salon
    global game
    global pif
    global debut
    global activity
    global joueur
    global freddy
    global bonnie
    global chica
    global foxy
    global nuits
    global IAs
    global minuteur
    global portel
    global porter
    global power
    global look
    if action == "move":
        if perso == "freddy":
            move = random.randint(115-IAs[0]*5,125-IAs[0]*5)
        elif perso == "chica":          
            move = random.randint(90-IAs[1]*4,100-IAs[1]*4)
        elif perso == "bonnie":
            move = random.randint(105-IAs[2]*4,115-IAs[2]*4)           
        elif perso == "foxy":
            move = random.randint(120-int(IAs[3]**1.5),130-int(IAs[3]**1.5))
        return move
    if action == "cam":
        if perso == "freddy":
            if IAs[0] == 0:
                cam = "1A"
            elif freddy == "1A":
                cam = "1B"
            elif freddy == "1B":
                cam = "7"
            elif freddy == "7":
                cam = "6"
            elif freddy == "6":
                cam = "4A"
            elif freddy == "4A":
                cam = "4B"
            elif freddy == "4B":            
                bouge = random.randint(1,IAs[0])
                if bouge <= 4:
                    place = random.randint(1,10)
                    if place == 1 or place == 5:
                        cam = "7"
                    elif place == 2 or place == 6 or place == 8 or place == 10:
                        cam = "4A"
                    elif place == 3 or place == 7 or place == 9:
                        cam = "6"
                    elif place == 4:
                        cam = "1B"
                else:
                    cam = "4B"
            else:
                cam = "dead"
        elif perso == "chica":
            bouge = random.randint(1,5)
            if bouge == 1:
                if chica == "1A":
                    cam = "1A"
                elif chica == "1B":
                    cam = "1B"
                elif chica == "7":
                    cam = "1B"
                elif chica == "6":
                    cam = "7"
                elif chica == "4A":
                    cam = "6"
                elif chica == "4B":
                    cam = "4A"
                elif chica == "door":
                    if porter == "open":
                        cam = "bureau"
                    else:
                        cam = "4A"
            else:
                if chica == "1A":
                    cam = "1B"
                elif chica == "1B":
                    cam = "7"
                elif chica == "7":
                    cam = "6"
                elif chica == "6":
                    cam = "4A"
                elif chica == "4A":
                    cam = "4B"
                elif chica == "4B":
                    cam = "door"
                elif chica == "door":
                    if porter == "open":
                        cam = "bureau"
                    else:
                        cam = "7"
        elif perso == "bonnie":
            bouge = random.randint(1,7)
            if bouge == 1:
                if bonnie == "1A":
                    cam = "1A"
                elif bonnie == "1B":
                    cam = "5"
                elif bonnie == "5":
                    cam = "5"
                elif bonnie == "2A":
                    cam = "3"
                elif bonnie == "2B":
                    cam = "2A"
                elif bonnie == "3":
                    cam = "3"
                elif bonnie == "door":
                    if portel == "open":
                        cam = "bureau"
                    else:
                        cam = "2B"
            if bouge == 7:
                if bonnie == "1A":
                    cam = "5"
                elif bonnie == "1B":
                    cam = "5"
                elif bonnie == "5":
                    cam = "2A"
                elif bonnie == "2A":
                    cam = "3"
                elif bonnie == "2B":
                    cam = "door"
                elif bonnie == "3":
                    cam = "door"
                elif bonnie == "door":
                    if portel == "open":
                        cam = "bureau"
                    else:
                        cam = "2B"
            else:
                if bonnie == "1A":
                    cam = "1B"
                elif bonnie == "1B":
                    cam = "2A"
                elif bonnie == "5":
                    cam = "1B"
                elif bonnie == "2A":
                    cam = "2B"
                elif bonnie == "2B":
                    cam = "door"
                elif bonnie == "3":
                    cam = "2B"
                elif bonnie == "door":
                    if portel == "open":
                        cam = "bureau"
                    else:
                        cam = "1B"            
        elif perso == "foxy":
            cam = None
            if foxy == 3:
                look = False
                if portel == "close":
                    foxy = 0
            if look == False:
                foxy += 1
            look = False
        print(perso,"change de position:",cam,"/",foxy)
        return cam

@bot.event
async def on_message(message):
        await bot.process_commands(message)
        global prefix
        global activity
        global go
        global start
        global salon
        global game
        global pif
        global debut
        global joueur
        global freddy
        global bonnie
        global chica
        global foxy
        global nuits
        global IAs
        global minuteur
        global portel
        global porter
        global power
        global look
        global fomove
        global chrono
        global timetodie
        
        if(message.author == bot.user):
            return
        
        if(message.content.startswith("f!start")):
            try:
                if nuits == -1:
                    await message.channel.send("**aucune nuit séléctionnée, utilise f!nuits pour choisir.**")
                elif (str(message.author)) == joueur:
                    start = True
                    await message.channel.send("**Les animatroniques ne bougeront qu'après le message: 'Il est actuellement 12AM', utilise f!cam, f!right et f!left pour survivre.**")
                    while not go:
                        await asyncio.sleep(1)
                    fmove = jeux("move","freddy")
                    cmove = jeux("move","chica")
                    bmove = jeux("move","bonnie")
                    fomove = jeux("move","foxy")
                    chrono = 0
                    timetodie = 0
                    while start:
                        await asyncio.sleep(1)
                        fmove -= 1
                        cmove -= 1
                        bmove -= 1
                        fomove -= 1
                        if power<=0:
                            if timetodie == 0:
                                await message.channel.send("https://imgur.com/TYYX7mD")
                            portel="open"
                            porter="open"
                            chica="None"
                            bonnie="None"
                            freddy="None"
                            timetodie += 1
                            if timetodie==25-IAs[0]:
                                await message.channel.send("https://imgur.com/q1t6vSM")
                            if timetodie==50-(IAs[0]*2):
                                await message.channel.send("https://imgur.com/imXLWM9")
                                await message.channel.send("**Le joueur est mort de freddy (power), la partie est donc supprimée.**")
                                await bot.change_presence(status=discord.Status.online, activity=activity)
                                start = False
                                game = False
                                go = False
                                look = False
                                del joueur
                                del freddy
                                del bonnie
                                del chica
                                del foxy
                                del nuits
                                del IAs
                                del minuteur
                                del portel
                                del porter
                                del power
                                return None
                        if portel == "close" or porter == "close":
                            chrono += 1
                            if portel == "close":
                                if chrono == 3:
                                    power -= 1
                            if porter == "close":
                                if chrono == 3:
                                    power -= 1
                            if chrono == 3:
                                chrono = 0
                        else:
                            chrono = 0
                        if fmove == 0:
                            freddy = jeux("cam","freddy")
                            fmove = jeux("move","freddy")
                            if freddy == "dead":
                                await message.channel.send("https://imgur.com/TeowBFT")
                                await message.channel.send("**Le joueur est mort de freddy, la partie est donc supprimée.**")
                                await bot.change_presence(status=discord.Status.online, activity=activity)
                                start = False
                                game = False
                                go = False
                                look = False
                                del joueur
                                del freddy
                                del bonnie
                                del chica
                                del foxy
                                del nuits
                                del IAs
                                del minuteur
                                del portel
                                del porter
                                del power
                                return None
                        if cmove == 0:
                            chica = jeux("cam","chica")
                            cmove = jeux("move","chica")
                        if bmove == 0:
                            bonnie = jeux("cam","bonnie")
                            bmove = jeux("move","bonnie")
                        if fomove == 0:
                            jeux("cam","foxy")
                            fomove = jeux("move","foxy")
                            if foxy == 4:
                                await message.channel.send("https://imgur.com/98VZs12")
                                await message.channel.send("**Le joueur est mort de foxy, la partie est donc supprimée.**")
                                await bot.change_presence(status=discord.Status.online, activity=activity)
                                start = False
                                game = False
                                go = False
                                look = False
                                del joueur
                                del freddy
                                del bonnie
                                del chica
                                del foxy
                                del nuits
                                del IAs
                                del minuteur
                                del portel
                                del porter
                                del power
                                return None
                else:
                    await message.channel.send("**seul le gardien de nuit peut commencer son job.**")
            except NameError:
                await message.channel.send("**utilise f!game en premier pour commencer à jouer.**")
        
        if(message.content.startswith("f!game")):
            try:
                if (str(message.author)) != joueur:
                    await message.channel.send("**tu ne peux pas utiliser cette commande, il y a déjà un joueur.**")
                else: 
                    await message.channel.send("**tu es déjà en préparation.**")
            except NameError:
                await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)
                await message.channel.send("attention, le jeu est en cours de programmation, il peut y avoir des bugs")
                await message.channel.send("**quelle nuit veux tu jouer ? (*utilise f!nuits*)**")
                await message.channel.send("**Une fois choisit, fait f!start pour commencer à jouer, tu as 30 secondes sinon la game est supprimée.**")
                joueur = str(message.author)
                freddy = "1A"
                bonnie = "1A"
                chica = "1A"
                foxy = 0
                nuits = -1
                IAs = [0,0,0,0]
                portel = "open"
                porter = "open"
                minuteur = 360
                start = False
                game = True
                go = False
                look = False
                power = 100
                chrono = 0
                for i in range(30):
                    await asyncio.sleep(1)
                    if not game:
                        return None
                if start:
                    await message.channel.send("**Il est actuellement 12AM**")
                    if nuits != 0:
                        go = True
                    while minuteur >= 0:
                        try:
                            if minuteur:
                                await asyncio.sleep(1)
                                minuteur -= 1
                                if game:
                                    if minuteur == 300:
                                        await message.channel.send("**Il est actuellement 1AM**")
                                    elif minuteur == 240:
                                        await message.channel.send("**Il est actuellement 2AM**")
                                    elif minuteur == 180:
                                        await message.channel.send("**Il est actuellement 3AM**")
                                    elif minuteur == 120:
                                        await message.channel.send("**Il est actuellement 4AM**")
                                    elif minuteur == 60:
                                        await message.channel.send("**Il est actuellement 5AM**")
                                    elif minuteur == 0:
                                        await message.channel.send("**Il est actuellement 6AM**")
                                        start = False
                                        game = False
                                        go = False
                                        await message.channel.send("**félicitation à {0.author.mention} qui viens de finir la nuit**".format(message))
                                        await bot.change_presence(status=discord.Status.online, activity=activity)
                                        del joueur
                                        del freddy
                                        del bonnie
                                        del chica
                                        del foxy
                                        del nuits
                                        del IAs
                                        del minuteur
                                        del portel
                                        del porter
                                        del power
                                        await message.channel.send("**Un nouveau gardien de nuit peut tenter ça chance**")
                                        return None
                        except NameError:
                            return None
                else:                  
                    await message.channel.send("**Le joueur met trops de temps à lancer ça game, la game est supprimée**")
                    await bot.change_presence(status=discord.Status.online, activity=activity)
                    del joueur
                    del freddy
                    del bonnie
                    del chica
                    del foxy
                    del nuits
                    del IAs
                    del minuteur
                    del portel
                    del porter
                    del power
                    game = False
            
        if(message.content.startswith("f!cam")):
            try:
                if (str(message.author)) == joueur:
                    if start:
                        cam = str(message.content.replace("f!cam ","")).upper()
                        if cam == "MAP":
                            await message.channel.send("https://imgur.com/CX6dq5a")
                        if power <= 0:
                            await message.channel.send("https://imgur.com/TYYX7mD")
                        elif bonnie == "bureau":
                            await message.channel.send("https://imgur.com/cOqeycE")
                            await message.channel.send("**Le joueur est mort de bonnie, la partie est donc supprimée.**")
                            await bot.change_presence(status=discord.Status.online, activity=activity)
                            start = False
                            game = False
                            go = False
                            look = False
                            del joueur
                            del freddy
                            del bonnie
                            del chica
                            del foxy
                            del nuits
                            del IAs
                            del minuteur
                            del portel
                            del porter
                            del power
                            return None
                        elif chica == "bureau":
                            await message.channel.send("https://imgur.com/bXpd4Gm")
                            await message.channel.send("**Le joueur est mort de chica, la partie est donc supprimée.**")
                            await bot.change_presence(status=discord.Status.online, activity=activity)
                            start = False
                            game = False
                            go = False
                            look = False
                            del joueur
                            del freddy
                            del bonnie
                            del chica
                            del foxy
                            del nuits
                            del IAs
                            del minuteur
                            del portel
                            del porter
                            del power
                            return None
                        elif cam == "1A":
                            power -= 1
                            if freddy == "1A" and chica == "1A" and bonnie == "1A":
                                await message.channel.send("https://imgur.com/Iat3YIa")
                            elif chica == "1A" and freddy == "1A":
                                await message.channel.send("https://imgur.com/NLHmVCj")
                            elif freddy == "1A" and bonnie == "1A":
                                await message.channel.send("https://imgur.com/ZZRusKe")
                            elif chica == "1A" and bonnie == "1A":
                                await message.channel.send("https://imgur.com/T4KHlSD")
                            elif chica == "1A":
                                await message.channel.send("https://imgur.com/AMIASI8")
                            elif bonnie == "1A":
                                await message.channel.send("https://imgur.com/n6bYJ5b")
                            elif freddy == "1A":
                                await message.channel.send("https://imgur.com/ohB18D3")
                            else:
                                await message.channel.send("https://imgur.com/RPNeSLi")
                        elif cam == "1B":
                            power -= 1
                            if chica == "1B" and bonnie == "1B":
                                await message.channel.send("https://imgur.com/bv8lsty")
                            elif chica == "1B":
                                await message.channel.send("https://imgur.com/ahFFHMl")
                            elif bonnie == "1B":
                                await message.channel.send("https://imgur.com/qp488Po")
                            elif freddy == "1B":
                                await message.channel.send("https://imgur.com/mfhJHa6")
                            else:
                                await message.channel.send("https://imgur.com/jsqYUXO")
                        elif cam == "1C":
                            power -= 1                            
                            if foxy == 3:
                                await message.channel.send("https://imgur.com/yBDiN1M")
                            elif foxy == 2:
                                look = True
                                await message.channel.send("https://imgur.com/fh818p0")
                            elif foxy == 1:
                                look = True
                                await message.channel.send("https://imgur.com/H0XkNEv")
                            else:
                                await message.channel.send("https://imgur.com/MnUHBBx")
                        elif cam == "2A":
                            power -= 1
                            if foxy == 3:
                                fomove = 3
                                await message.channel.send("https://imgur.com/z2v93W7") 
                            elif bonnie == "2A":
                                await message.channel.send("https://imgur.com/Qw2Znfs")
                            else:
                                await message.channel.send("https://imgur.com/C3zcHak")
                        elif cam == "2B":
                            power -= 1
                            if bonnie == "2B":
                                await message.channel.send("https://imgur.com/axNNwHP")
                            else:
                                await message.channel.send("https://imgur.com/xGNIqvm")
                        elif cam == "3":
                            power -= 1
                            if bonnie == "3":
                                await message.channel.send("https://imgur.com/YO5jExo")
                            else:
                                await message.channel.send("https://imgur.com/buzUbAX")
                        elif cam == "4A":
                            power -= 1
                            if chica == "4A":
                                await message.channel.send("https://imgur.com/I7YGYNT")
                            elif freddy == "4A":
                                await message.channel.send("https://imgur.com/Ru2bDnj")
                            else:
                                await message.channel.send("https://imgur.com/1p9xf9w")
                        elif cam == "4B":
                            power -= 1
                            if chica == "4B":
                                await message.channel.send("https://imgur.com/B1TELpc")
                            elif freddy == "4B":
                                await message.channel.send("https://imgur.com/0K6SrtQ")
                            else:
                                await message.channel.send("https://imgur.com/pEF9MrV")
                        elif cam == "5":
                            power -= 1
                            if bonnie == "5":
                                await message.channel.send("https://imgur.com/3ptXkBM")
                            else:
                                await message.channel.send("https://imgur.com/KHNMlmA")
                        elif cam == "6":
                            power -= 1
                            await message.channel.send("**erreur: caméra désactivé ou détruite. erreur: aucun audio**")
                        elif cam == "7":
                            power -= 1
                            if chica == "7":
                                await message.channel.send("https://imgur.com/PY8978H")
                            elif freddy == "7":
                                await message.channel.send("https://imgur.com/6LfBlcQ")
                            else:
                                await message.channel.send("https://imgur.com/7V2A3QX")
                        else:
                            if cam != "MAP":
                                await message.channel.send("**La caméra n'existe pas.**")
                        if cam in ["1A","1B","1C","2A","2B","3","4A","5","6","7"] and freddy == "4B" and porter == "open":
                            freddy = "bureau"
                    else:
                        await message.channel.send("**Tu n'as pas encore reçut ton moniteur.**")                                                                                                                                                                                                            
                else:
                    await message.channel.send("**seul le gardien de nuit a un moniteur.**")
            except NameError:
                await message.channel.send("**tu n'as pas de moniteur, utilise f!game.**")
                    
        if(message.content.startswith("f!left")):
            try:
                if (str(message.author)) == joueur:
                    if start:
                        commande = str(message.content.replace("f!left ","")).lower()
                        if power <= 0:
                            await message.channel.send("https://imgur.com/TYYX7mD")
                            return None
                        if commande == "open":
                            portel = "open"
                            await message.channel.send("https://imgur.com/rZltWuJ")
                        elif commande == "close":
                            if bonnie == "bureau":
                                await message.channel.send("https://imgur.com/rZltWuJ")
                            else:
                                await message.channel.send("https://imgur.com/E6uuImo")
                                portel = "close"
                        elif commande == "light":
                            portel = "open"
                            if bonnie == "bureau":
                                await message.channel.send("https://imgur.com/rZltWuJ")
                            elif bonnie == "door":
                                await message.channel.send("https://imgur.com/yr6RpEi")
                                power -= 1
                            else:
                                await message.channel.send("https://imgur.com/4nNhwew")
                                power -= 1
                    else:
                        await message.channel.send("**Tu n'es pas encore dans ton bureau.**")
                else:
                    await message.channel.send("**seul le gardien de nuit peut utilisé les portes.**")
            except NameError:
                await message.channel.send("**le bureau est interdit au public, fait f!game pour être embauché.**")
                    
        if(message.content.startswith("f!right")):
            try:
                if (str(message.author)) == joueur:
                    if start:
                        commande = str(message.content.replace("f!right ","")).lower()
                        if power <= 0:
                            await message.channel.send("https://imgur.com/TYYX7mD")
                            return None
                        if commande == "open":
                            porter = "open"
                            await message.channel.send("https://imgur.com/bDLPYXK")
                        elif commande == "close":
                            if chica == "bureau" or freddy == "bureau" or freddy == "dead":
                                await message.channel.send("https://imgur.com/bDLPYXK")
                            else:
                                await message.channel.send("https://imgur.com/jjwTT7a")
                                porter = "close"
                        elif commande == "light":
                            porter = "open"
                            if chica == "bureau" or freddy == "bureau" or freddy == "dead":
                                await message.channel.send("https://imgur.com/bDLPYXK")
                            elif chica == "door":
                                await message.channel.send("https://imgur.com/pZln1SX")
                                power -= 1
                            else:
                                await message.channel.send("https://imgur.com/JnNwTGr")
                                power -= 1
                    else:
                        await message.channel.send("**Tu n'es pas encore dans ton bureau.**")
                else:
                    await message.channel.send("**seul le gardien de nuit peut utilisé les portes.**")
            except NameError:
                await message.channel.send("**le bureau est interdit au public, fait f!game pour être embauché.**")


        if(message.content.startswith("f!nuits")):
            try:
                if (str(message.author)) == joueur:
                    if start:
                        await message.channel.send("Les animatroniques sont déja programmés, tu ne peux pas changer la dificultée maintenant.")
                        return
                    nuits = int(message.content.replace("f!nuits ",""))
                    if nuits == 0:
                        await message.channel.send("**La nuit 0 a été séléctionné, les animatroniques ne t'attaqueront pas.**")
                        IAs = [0,0,0,0]
                    elif nuits == 1:
                        await message.channel.send("**La nuit 1 a été séléctionné, trouillard.**")
                        IAs = [0,3,2,1]
                    elif nuits == 2:
                        await message.channel.send("**La nuit 2 a été séléctionné, trop facile.**")
                        IAs = [1,4,5,3]
                    elif nuits == 3:
                        await message.channel.send("**La nuit 3 a été séléctionné, mouais... niveau moyen...**")
                        IAs = [3,7,7,8]
                    elif nuits == 4:
                        await message.channel.send("**La nuit 4 a été séléctionné, ah, ça commence à venir.**")
                        IAs = [8,11,11,10]
                    elif nuits == 5:
                        await message.channel.send("**La nuit 5 a été séléctionné, ça devient compliquer non ?**")
                        IAs = [11,13,15,13]
                    elif nuits == 6:
                        await message.channel.send("**La nuit 6 a été séléctionné, bonne chance !**")
                        IAs = [16,18,17,15]
                    elif nuits == 7:
                        await message.channel.send("**La nuit 4/20 a été séléctionné, ON CROIT TOUS EN TOI !!!**")
                        IAs = [20,20,20,20]
                    else:
                        nuits = -1
                        await message.channel.send("**choisit un nombre entier entre 0 et 7.**")
                else:
                    await message.channel.send("**tu n'as pas accès aux animatroniques, changer leur niveau est imposible.**")
            except NameError:
                await message.channel.send("**utilise f!game pour modifier leur IA.**")
            except ValueError:
                await message.channel.send("**tu dois juste faire f!nuits 'chiffre', c'est simple merde !.**")
        
        if(message.content.startswith("f!power")):
            try:
                if (str(message.author)) == joueur:
                    if start:
                        if power <= 0:
                            await message.channel.send("**Le courant est coupé**")
                        else:
                            await message.channel.send("**Tu es à {}%**".format(power))
                    else:
                        await message.channel.send("**Tu n'es pas encore mis sur le générateur.**")
                else:
                    await message.channel.send("**seul le gardien de nuit peut voir l'énergie qu'il reste.**")
            except NameError:
                await message.channel.send("**utilise l'énergie que tu as pour faire f!game.**")
                
        if(message.content.startswith("f!time")):
            try:
                if (str(message.author)) == joueur:
                    if start:
                            await message.channel.send("**Il est 6AM dans {} secondes**".format(minuteur))
                    else:
                        await message.channel.send("**Il n'est pas encore minuit.**")
                else:
                    await message.channel.send("**l'heure n'est utile que pour le gardien de nuit.**")
            except NameError:
                await message.channel.send("**vite, utilise f!game pour qu'il soit minuit.**")
                
        if(message.content.startswith("f!stop")):
            try:
                if (str(message.author)) == joueur:
                    if start:
                        await message.channel.send("**Le gardien de nuit a fuit, une nouvelle game peux être lancée.**")
                        game = False
                        start = False
                        await bot.change_presence(status=discord.Status.online, activity=activity)
                        del joueur
                        del freddy
                        del bonnie
                        del chica
                        del foxy
                        del nuits
                        del IAs
                        del minuteur
                        del portel
                        del porter
                        del power
                    else:
                        await message.channel.send("**La partie sera supprimer dans moins de 30 secondes, attend juste.**")
                else:
                    await message.channel.send("**Tu n'es pas son patron, tu ne peux pas le viré.**")
            except NameError:
                await message.channel.send("**Personne ne s'amuse encore avec moi, fait donc f!game.**")

@bot.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(colour = discord.Color(0xff0000))
    embed.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="**f!info**",value="Permet de connaître les règles (change beaucoup de la vrai version).",inline=False)
    embed.add_field(name="**f!game**",value="Permet de lancer le jeu *five nights at Discord* (mon status indique si je suis déjà en game).",inline=False)
    embed.add_field(name="**f!stop**",value="Permet d'arrêter le jeu.",inline=False)
    embed.add_field(name="**f!cam 'cam'**",value="Permet de regarder les cameras ('cam' = map,1A,1B,1C,2A,2B,3,4A,4B,5,6,7).",inline=False)
    embed.add_field(name="**f!nuits '0-7'**",value="Permet de choisir la nuit (0 pour entrainement et 7 pour la custom night 4/20).",inline=False)
    embed.add_field(name="**f!start**",value="Permet de commencer à jouer après avoir choisit les options.",inline=False)
    embed.add_field(name="**f!'côté' 'action'**",value="Permet d'actionner les portes ('côté' = right,left et action = light,close,open).",inline=False)
    embed.add_field(name="**f!power**",value="Permet de savoir l'énergie qu'il te reste.",inline=False)
    embed.add_field(name="**f!time**",value="Permet de savoir l'heure qu'il est (dans le jeu).",inline=False)
    embed.add_field(name="**f!invite**",value="Pour créer une invitation.",inline=False)
    await ctx.message.channel.send(embed=embed)

@bot.command(pass_context = True)
async def info(ctx):
    embed = discord.Embed(colour = discord.Color(0xff0000))
    embed.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="**Freddy**",value="Se déplace comme dans le vrai jeu, une fois à la porte de droite: si le joueur regarde une caméra autre que la 4B alors que la porte de droite est ouverte, Freddy entre dans le bureau.",inline=False)
    embed.add_field(name="**Freddy (power)**",value="quand vous n'avez plus de power, Freddy arrive à gauche et chante avant de vous tuez. A noté que Chica et Bonnie ne peuvent plus vous tuer même si ils sont dans le burreau (Foxy lui peut quand même).",inline=False)
    embed.add_field(name="**Chica**",value="Est plus rapide que Bonnie mais a plus de chance de reculer, arrive uniquement par la droite.",inline=False)
    embed.add_field(name="**Bonnie**",value="Est plus lent mais recule moins souvent, il peut lui arrivé de zapper une caméra, arrive par la gauche.",inline=False)
    embed.add_field(name="**Foxy**",value="Tous les X secondes, il changera de position sauf si on l'a regardé au moins une fois pendant se temps.",inline=False)
    embed.add_field(name="**les caméras**",value="enlève 1 power à chaque utilisation sauf pour la MAP, pas d'easter eggs pour le moment désolé.",inline=False)
    embed.add_field(name="**les portes**",value="-1 power tous les 3 secondes par portes fermées, ne ferme pas si plus de courant ou qu'un animatronique est dans le bureau.",inline=False)
    embed.add_field(name="**les lumières**",value="enlève 1 power à chaque utilisation, activé la lumière ouvre automatiquement la porte ciblée.",inline=False)
    await ctx.message.channel.send(embed=embed)
    
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def quite(ctx):
    global start
    global salon
    global game
    global pif
    global debut
    global activity
    global joueur
    global freddy
    global bonnie
    global chica
    global foxy
    global nuits
    global IAs
    global minuteur
    global portel
    global porter
    global power
    global look
    global go
    try:
        if joueur:
            game = False
            start = False
            go = False
            await bot.change_presence(status=discord.Status.online, activity=activity)
            await ctx.message.channel.send("**le gardien de nuit a étais renvoyé, une nouvelle game peux être lancée**.")
            del joueur
            del freddy
            del bonnie
            del chica
            del foxy
            del nuits
            del IAs
            del minuteur
            del portel
            del porter
            del power
            del look
    except NameError:
        await ctx.message.channel.send("**Personne n'a été embauché en tant que gardien de nuit.**")
@quite.error
async def quite_error(error,ctx):
    return   

@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def msg(ctx, message):
    msg = ctx.message.content.replace(prefix+"msg","")
    await ctx.message.channel.purge(limit=1)
    await ctx.message.channel.send(msg)
@msg.error
async def msg_error(error,ctx):
    return

@bot.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, nb=100):
    await ctx.message.channel.purge(limit=nb+1)
    await ctx.message.channel.send("j'ai supprimé {} messages.".format(nb))
@clear.error
async def clear_error(error,ctx):
    return

@bot.command(pass_context = True)
async def invite(ctx):
    await ctx.message.channel.purge(limit=1)
    await ctx.message.channel.send("https://discord.gg/vY2tQVSBtF")

@bot.command(pass_context = True)
async def game(ctx):
    pass
@bot.command(pass_context = True)
async def nuits(ctx):
    pass
@bot.command(pass_context = True)
async def start(ctx):
    pass
@bot.command(pass_context = True)
async def stop(ctx):
    pass
@bot.command(pass_context = True)
async def cam(ctx):
    pass
@bot.command(pass_context = True)
async def left(ctx):
    pass
@bot.command(pass_context = True)
async def right(ctx):
    pass
@bot.command(pass_context = True)
async def power(ctx):
    pass
@bot.command(pass_context = True)
async def time(ctx):
    pass

bot.run(TOKEN)