class Yin:pass
class Yang:
    def __init__(self) -> None:
        print("Yang destruido")

yin = Yin()
yang = Yang()

yin.yang = yang
print(yang)
del(yang)
yin.yang = None 
print("?") 