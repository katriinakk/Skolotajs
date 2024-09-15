class Skolotajs:
    def __init__(self, sk_tips, uzvards):
        self.sk_tips = sk_tips
        self.uzvards = uzvards

    def a(uzvards):
        pass
    
class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, klase, st_sk, sk_tips):
        super().__init__(uzvards, sk_tips)
        self.klase = klase
        self.st_sk = st_sk

    def izd(self, uzvards, st_sk, sk_tips = "sākumskolas skolotājs"):
        return(" Tips: {},\n Uzvārds: {},\n Pasniegto stundu skaits: {}\n Klase: {}").format(sk_tips, uzvards, st_sk, self.klase)

class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, pr1, pr2, pr1n, pr2n, sk_tips):
        super().__init__(self, sk_tips)
        self.pr1 = pr1
        self.pr2 = pr2
        self.pr1n = pr1n
        self.pr2n = pr2n

    def izdruka2(self, pr1n, pr2n, pr1, pr2,  sk_tips = "vidusskolas skolotājs"):
        return(" Tips: {},\n Uzvārds: {},\n 1. Priekšmeta nosaukums un skaits: {} ; {}(sk.)\n 2. Priekšmeta nosaukums un skaits: {} ; {}(sk.)\n Pasniegto stundu skaits: {}").format(sk_tips, self.uzvards, pr1n, pr1, pr2n, pr2, pr1+pr2)

tipi = int(input("Ievadiet skolotāja tipu: 1- sākumskolas skolotājs, 3 - vidusskolas skolotājs -> "))
uzv = input("Ievadiet skolotāja uzvārdu -> ")



if (tipi == 1):
    
    
    stundu_sk = input("Ievadiet skolotāja stundu skaitu -> ")
    klasite = input("Ievadiet skolotāja klasi -> ")
    print("\n .-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*- ")
    skol = SakumskolasSkolotajs(uzv, klasite, stundu_sk, tipi)  
    print(skol.izd(uzv, stundu_sk))
    print(" .-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*- \n")
    
if (tipi == 3):

    
    priek1nos = input("Ievadiet 1. priekšmeta nosaukumu -> ")
    priek1 = int(input("Ievadiet 1. priekšmeta stundu skaitu -> "))
    priek2nos = input("Ievadiet 2. priekšmeta nosaukumu -> ")
    priek2 = int(input("Ievadiet 2. priekšmeta stundu skaitu -> "))
    print("\n .-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*- ")
    skol = VidusskolasSkolotajs(priek1, priek2, priek1nos, priek2nos, uzv)
    print(skol.izdruka2(priek1nos, priek2nos, priek1, priek2))
    print(" .-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*- \n")
   

else:
    print("Nepareizi ievadīti dati.")

#print(skol.uzvards)
#print(skol.sk_tips)
#print(skol.st_sk)
#print(skol.klase)