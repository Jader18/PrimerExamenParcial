
def beca(nota):
    
    if nota > 95:
        beca = True
        print("Beca otorgada")
        return 0

    else:
        print("Beca denegada")
        return 0


nota = int(input("Ingrese la nota del estudiante: "))   
beca(nota)