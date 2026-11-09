ultrasonidos = 40
infrarrojos = 12
luz = 7

barra = "#" * (ultrasonidos // 5)
print(f"ultrasonidos {ultrasonidos:.1f} {barra}")

barra = "#" * (infrarrojos // 5)
print(f"infrarrojos {infrarrojos:.1f} {barra}")

barra = "#" * (luz // 5)
print(f"luz {luz:.1f} {barra}")