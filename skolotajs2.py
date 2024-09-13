class Skolotajs:
    def __init__(self, sk_tips, uzvards):
        self.sk_tips = sk_tips
        self.uzvards = uzvards
    
class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, klase, st_sk):
        super().__init__(uzvards)
        self.klase = klase
        self.st_sk = st_sk

    def izd(klase, uzvards, st_sk):
        return(" Tips: sākumskolas skolotājs,\n Uzvārds: {},\n Pasniegto stundu skaits: {}\n Klase: {}").format(uzvards, st_sk, klase)

class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, pr1, pr2, pr1n, pr2n, uzvards, sk_tips):
        super().__init__(uzvards, sk_tips)
        self.pr1 = pr1
        self.pr2 = pr2
        self.pr1n = pr1n
        self.pr2n = pr2n

    def izdruka2(uzvards, pr1n, pr2n, sk_tips, pr1, pr2):
        return(" Tips: {},\nUzvārds: {},\n1. Priekšmeta nosaukums un skaits: {}, {}(sk.)\n2. Priekšmeta nosaukums un skaits: {}, {}(sk.)\nPasniegto stundu skaits: {}").format(sk_tips, uzvards, pr1n, pr1, pr2n, pr2, pr1n+pr2n)

tipi = int(input("Ievadiet skolotāja tipu: 1- sākumskolas skolotājs, 3 - vidusskolas skolotājs -> "))
uzv = str(input("Ievadiet skolotāja uzvārdu -> "))
skol = Skolotajs(tipi, uzv)

if (tipi == 1):
    stundu_sk = input("Ievadiet skolotāja stundu skaitu -> ")
    klasite = input("Ievadiet skolotāja klasi -> ")

    skol = SakumskolasSkolotajs(uzv, klasite, stundu_sk)  
    print(skol.izd(uzv, stundu_sk, skol.klase))

    
#else:
 #   print("error")

print(skol.uzvards)
print(skol.sk_tips)
print(skol.st_sk)
print(skol.klase)