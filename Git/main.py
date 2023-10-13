import os
import cv2 as cv
import numpy as np
import time 

embalagem = 'Git\\embalagem.png'

for _, _, arquivo in os.walk('Git\\Selos'):
    for selo in arquivo:
        time.sleep(2)
        selo = 'Git\\Selos\\' + selo
        print(selo)
        img_rgb = cv.imread(embalagem)

        assert img_rgb is not None, "file could not be read, check with os.path.exists()"
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

        template = cv.imread(selo, cv.IMREAD_GRAYSCALE)
        assert template is not None, "file could not be read, check with os.path.exists()"
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)

        threshold = 0.8
        loc = np.where( res >= threshold) 

        if len(loc[0]) > 0:
            print('True')

            pontos = []
            for pt in zip(*loc[::-1]):
                ponto = (pt, (pt[0] + w, pt[1] + h))
                pontos.append(ponto)
                cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
                print('localização: Inicial' + str(pt) + ' Final(' + str(pt[0] + w) + ', ' + str(pt[1] + h) + ')')

            print(pontos)

            print('--------------------------------------------')
            cv.imwrite('Git\\resultado.png', img_rgb)
        else:
            print('False')
