def switch_xy(imgxy:list) -> list:
    imgyx = []
    coord_x = len(imgxy)
    coord_y = len(imgxy[0])
    
    for i in range(coord_y):
        imgyx.append([0]*coord_x)
    
    for x in range(coord_x):
        for y in range(coord_y):
            imgyx[y][x] = imgxy[x][y]
    
    return imgyx
#___________________________________________________________________________________________________________________________________________________________________________________
def compress(img:list, factor:float, _format:str) -> list:
    #img -> image à comprimmer
    #factor = ratio de compression (1 = image identique; 0.5 = image diviser par 2)
    #_format = format de stockage de l'image
    def calc_avg(img:list, coor_x:int, coor_y:int, _len:int, _format:str) -> int or list:
        nb_val = 0
        if _format == "PBM" or _format == "PGM":
            val = 0
            for y in range(coor_y, coor_y + _len):
                for x in range(coor_x, coor_x + _len):
                    val = val + img[y][x]
                nb_val = nb_val + 1
            
            if nb_val != 0:
                val = int(val/nb_val)
            
            return val
            
        elif _format == "PPM":
            val = [0, 0, 0]
        
            for y in range(coor_y, coor_y + _len):
                for x in range(coor_x, coor_x + _len):
                    for _ in len(val):
                        val[_] = img[y][x][_]
                    nb_val = nb_val + 1
        
            if nb_val != 0:
                for _ in len(val):
                    val[_] = val[_] / nb_val
            
            return val
    
    
    orig_imgy = len(img)
    orig_imgx = len(img[0])
    comp_imgy = int(len(img)*factor)
    comp_imgx = int(len(img[0])*factor)
    pos_y = 0
    
    img_compress = [[0]*comp_imgx]*comp_imgy
        
    for y in range(comp_imgy):
        pos_x = 0
        for x in range(y):
            color = calc_avg(img, int(pos_x/factor), int(pos_y/factor), int(1/factor)-1, _format)
            img_compress[pos_y][pos_x] = color
            pos_x = pos_x + 1
             
        pos_y = pos_y + 1    
    
    return img_compress
#___________________________________________________________________________________________________________________________________________________________________________________
def verify(soluce:list, exo:list, _format:str):
    false = 0
    total = 0
    wrong_px = [[0]*len(soluce[0])]*len(soluce)
    for y in range(len(soluce)):
        for x in range(len(soluce[0])):
            if soluce[y][x] != exo[y][x]:
                soluce[y][x] = 1
                false = false + 1
                
            total = total + 1
    
    false_percent = (false/total)*100
    
    if false_percent == 0:
        print("Félicitation, c'est un sans faute.")
        
    elif false_percent < 5:
        print("Dommage, il y a peut-être une ou deux erreurs de frappes, tu ferras mieux la prochaine fois ! (", false_percent, "% de réponses fausses)")
        
    elif false_percent < 10:
        print("Tu y es presque, courage. (", false_percent, "% de réponses fausses)")
        
    elif false_percent < 25:
        print("Attention, il y a quelques erreurs, concentre-toi mieux la prochaine fois. (", false_percent, "% de réponses fausses)")
        
    elif false_percent <= 50:
        print("Il a beaucoup d'erreur, il serait préférable de relire l'explication avant de passer au prochain exercice. (", false_percent, "% de réponses fausses)")
        
    elif false_percent < 75:
        print("Plus de la moitié est fausse, je te conseille vivement de relire comment il faut faire. (", false_percent, "% de réponses fausses)")
        
    elif false_percent < 100:
        print("Tu as pratiquement tout faux, relis la théorie avant de continuer. Cela ne serait pas pertinent de continuer. (", false_percent, "% de réponses fausses)")
        
    elif false_percent == 100 and _format == "PBM":
        print("Je pense que tu as du confondre les valeurs, c'est à toi de voir si tu veux refaire l'exercice ou passser au suivant.")
        
    else:
        print("Aucun pixel n'est juste, je te conseille fortemtent de relire l'explication et de refaire l'exercice avant de continuer. La difficulté des exercices étant croissante ce ne serait pas judicieux de continuer, n'est-ce pas ;). (PS: courage et n'abondonne pas)")
#___________________________________________________________________________________________________________________________________________________________________________________
def write(img: list, _format: str, name: str) -> None:
    img = switch_xy(img)
    img_str: str = ''
    for x in range(len(img)):
        for y in range(len(img[x])):
            img_str = img_str + str(img[x][y]) + ' '
            
    name = name + '_exo.txt'
    f = open(name, 'w')
    f.write(_format + ' ' + str(len(img)) + ' ' + str(len(img[0]))+ ' ' + img_str)
    f.close()
#___________________________________________________________________________________________________________________________________________________________________________________
def _extract_(name: str):
    f = open(name, 'r')
    
#___________________________________________________________________________________________________________________________________________________________________________________
imgxy = [[1,0,0,0], [1,0,0,1], [1,0,0,0], [1,1,0,0]]
test_1 = [[1,0,0,0,1], [1,0,0,1,1], [1,0,1,0,1], [1,1,0,0,1], [1,0,0,0,1]]
test_2 = [[0,1,1,1,0], [0,1,1,0,0], [0,1,0,1,0], [0,0,1,1,0], [0,1,1,1,0]]
#imgyx = switch_xy(imgxy)

print(compress(imgxy, 0.5, "PBM"))
#compress(imgxy, 2)