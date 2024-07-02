import instaloader
import time
import random

BOT = []
BOT.append(["#####","#####"])
BOT.append(["#####","#####"])
BOT.append(["#####","#####"])
i = random.randint(0, len(BOT) - 1)
userbot = BOT[i][0]
password =  BOT[i][1]
j = i
while(j == i):
    j = random.randint(0, len(BOT) - 1)
    userbot2 = BOT[j][0]
    password2 = BOT[j][1]


class InstaJuju:
    def __init__(self, userinsta,username2 = userbot ,mdp = password, username3 = userbot2, mdp2 = password2):
        self.userinsta = userinsta
        self.username2 = username2
        self.mdp = mdp
        self.username3 = username3
        self.mdp2 = mdp2

    def Verif_Abo(self):
        nb = 0
        tabreturn = []

        L = instaloader.Instaloader()

        try:
            # Charger le profil de l'utilisateur
            L.login(self.username2, self.mdp)

            profile = instaloader.Profile.from_username(L.context, self.userinsta)

            print(self.username2)
            print("----------------------------------------------------")
    
            # Récupérer la liste des abonnés
            followers = []
            for follower in profile.get_followers():
                tps = random.uniform(0.5, 1)
                time.sleep(tps)
                print(follower.username)
                followers.append(follower.username)

    
            # Afficher la liste des abonnés
            nb_follower= len(followers)
            print("Liste des abonnés:", followers)  
            print("Nombre d'abonnés:", nb_follower)
        
        except instaloader.exceptions.ProfileNotExistsException as e:
            rep = f"Le profil '{self.userinsta}' n'existe pas."
            print(rep)
            return rep
        except instaloader.exceptions.ConnectionException as e:
            rep = "Erreur de connexion. Vérifiez votre connexion Internet."
            print(rep)
            return rep
        except instaloader.exceptions.PrivateProfileNotFollowedException as e:
            rep = f"Le profil {self.userinsta} est en privé"
            print(rep)
            return rep
        except instaloader.exceptions.BadCredentialsException as e:
            rep = f"Identifiants incorrects pour {self.username2}. Veuillez vérifier votre nom d'utilisateur et votre mot de passe."
            print(rep)
            return rep
        except Exception as e:
            rep = f"Une erreur s'est produite: {e}, le bot {self.username2} est possiblement en panne réessayez."
            print(e)
            print(rep)
            return rep

        try:
            L.login(self.username3, self.mdp2)

            profile = instaloader.Profile.from_username(L.context, self.userinsta)

            print(self.username3)
            print("----------------------------------------------------")

            # Récupérer la liste des abonnements
            followings = []
            for following in profile.get_followees():
                tps = random.uniform(0.5, 1)
                time.sleep(tps)
                print(following.username)
                followings.append(following.username)

            nb_following= len(followings)
            print("Liste des abonnements:", followings)
            print("Nombre d'abonnements:", nb_following)

            for abonnement in followings:
                if abonnement not in followers:
                    print(f"Le profil '{abonnement}' ne followback pas")
                    nb = nb + 1
                    tabreturn.append(abonnement)

            print(f"Il y a {nb} personnes qui ne followback pas")
            if nb_follower == 0 and nb_following == 0:
                rep = f"Le profil {self.userinsta} est en privé"
                print(rep)
                return rep
            else:
                return tabreturn
    
        except instaloader.exceptions.ProfileNotExistsException as e:
            rep = f"Le profil '{self.userinsta}' n'existe pas."
            print(rep)
            return rep
        except instaloader.exceptions.ConnectionException as e:
            rep = "Erreur de connexion. Vérifiez votre connexion Internet."
            print(rep)
            return rep
        except instaloader.exceptions.PrivateProfileNotFollowedException as e:
            rep = f"Le profil {self.userinsta} est en privé"
            print(rep)
            return rep
        except instaloader.exceptions.BadCredentialsException as e:
            rep = f"Identifiants incorrects pour {self.username3}. Veuillez vérifier votre nom d'utilisateur et votre mot de passe."
            print(rep)
            return rep
        except Exception as e:
            rep = f"Une erreur s'est produite: {e}, le bot {self.username3} est possiblement en panne réessayez."
            print(e)
            print(rep)
            return rep    