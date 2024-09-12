class Skolotajs:
    def __init__(self, sk_tips, uzvards):
        self.sk_tips = sk_tips
        self.uzvards = uzvards

    def tips(sk_tips):
        if sk_tips == 1:
            sk_tips = "sākumskolas skolotājs"
        if sk_tips == 3:
            sk_tips = "vidusskolas skolotājs"
        else:
            sk_tips = "error"

class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, st_sk, sk_tips, klase, uzvards):
        super().__init__(sk_tips, uzvards)
        self.st_sk = st_sk
        self.klase = klase

    def izdruka(uzvards, st_sk, sk_tips, klase):
        return("Tips: {},\n Uzvārds: {},\n Pasniegto stundu skaits: {}\nKlase: {}").format(sk_tips, uzvards, st_sk, klase)

class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, pr1, pr2, pr1n, pr2n, sk_tips, uzvards):
        super().__init__(sk_tips, uzvards)
        self.pr1 = pr1
        self.pr2 = pr2
        self.pr1n = pr1n
        self.pr2n = pr2n
        

 #   def rek(st_sk, pr1, pr2):
  #      sk = pr1 +pr2

    def izdruka2(uzvards, pr1n, pr2n, sk_tips, pr1, pr2):
        return("Tips: {},\nUzvārds: {},\n1. Priekšmeta nosaukums un skaits: {}, {}(sk.)\n2. Priekšmeta nosaukums un skaits: {}, {}(sk.)\nPasniegto stundu skaits: {}").format(sk_tips, uzvards, pr1n, pr1, pr2n, pr2, pr1n+pr2n)





skol1 = SakumskolasSkolotajs(15, 1,"2.a", "Bērziņš")
skol1.tips()
print(skol1.izdruka())

skol2 = VidusskolasSkolotajs("Matemātika", "Datorika", 12, 8, 3, "Ozols")
skol2.tips()
print(skol2.izdruka2())
