#animal exercicio beecrowd

verte_inverte = input()

def verte():
    mama_ave = input()
    if mama_ave == "ave":
        carni_oni()
    else:
        oni_herbi()

def inverte():
    inseto_anelideo = input()
    if inseto_anelideo == "inseto":
        hema_herbi()
    else:
        anelideo()

def hema_herbi():
    hema_herbi = input()
    if hema_herbi == "hematofago":
        print("pulga")
    else:
        print("lagarta")

def anelideo():
    anelide = input()
    if anelide == "hematofago":
        print("sanguessuga")
    else:
        print("minhoca")


def oni_herbi():
    onii_herbi = input()
    if onii_herbi == "onivoro":
        print("homem")
    else:
        print("vaca")

def carni_oni():
    carni_oni = input()
    if carni_oni == "carnivoro":
        print("aguia")
    else:
        print("pomba")


if verte_inverte == "vertebrado":
    verte()
else:
    inverte()





