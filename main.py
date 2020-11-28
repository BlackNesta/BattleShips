from projectVariables import letterOrder

def inputAtack():
    wrongCoord = True
    while wrongCoord:
        coord = input("Introdu coordonatele de atac [A-H][1, 8]: ")
        coord = coord.replace(" ", "")
        coord = coord.upper()
        if coord[0] >= "A" and coord[0] <= "H" and coord[1] >= "1" and coord[1] <= "8":
            wrongCoord = False
        else:
            print("Format Incorect.")

    #   coord[0] = coordonata x
    #   coord[1] = coordonata y
    x, y = coord

    return letterOrder[x], int(y)

if __name__ == "__main__":
    print("Hellow World")
    x, y = inputAtack()
    print ("Punctul de atac este: " + str(x) + "-" + str(y))