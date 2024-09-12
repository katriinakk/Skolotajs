from winreg import KEY_ALL_ACCESS


class Skolotajs:
    def __init__(self, sk_tips, uzvards):
        self.sk_tips = sk_tips
        self.uzvards = uzvards
    
class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, klase, uzvards, st_sk, sk_tips = 1):
        super().__init__(sk_tips, uzvards)
        self.klase = klase
        self.st_sk = st_sk

    def izd(uzvards, klase, st_sk, sk_tips = "sākumskolas skolotājs"):
        return("Tips: {},\n Uzvārds: {},\n Pasniegto stundu skaits: {}\nKlase: {}").format(sk_tips, uzvards, st_sk, klase)

class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, pr1, pr2, pr1n, pr2n, uzvards, sk_tips = 3):
        super().__init__(uzvards, sk_tips)
        self.pr1 = pr1
        self.pr2 = pr2
        self.pr1n = pr1n
        self.pr2n = pr2n

    def izdruka2(uzvards, pr1n, pr2n, sk_tips, pr1, pr2):
        return("Tips: {},\nUzvārds: {},\n1. Priekšmeta nosaukums un skaits: {}, {}(sk.)\n2. Priekšmeta nosaukums un skaits: {}, {}(sk.)\nPasniegto stundu skaits: {}").format(sk_tips, uzvards, pr1n, pr1, pr2n, pr2, pr1n+pr2n)

tipi = input("Ievadiet skolotāja tipu: 1- sākumskolas skolotājs, 3 - vidusskolas skolotājs -> ")
uzv = input("Ievadiet skolotāja uzvārdu -> ")

if (tipi == 1):
    stundu_sk = input("Ievadiet skolotāja stundu skaitu -> ")
    klasite = input("Ievadiet skolotāja klasi -> ")

    skol = SakumskolasSkolotajs(klasite, uzv, stundu_sk, "sākumskolas skolotājs")
    print(skol.izd())
