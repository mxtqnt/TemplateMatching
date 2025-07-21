# Template Matching com OpenCV

Este repositório demonstra o uso de template matching para localizar selos específicos dentro de uma imagem de embalagem utilizando OpenCV com Python.

## Tecnologias Utilizadas
- Python
- OpenCV
- NumPy

## Descrição

A imagem `embalagem.png` é analisada em tempo real para localizar selos presentes na pasta `Selos/`. Utiliza-se `cv.matchTemplate` com o método `cv.TM_CCOEFF_NORMED`, e os resultados são salvos na imagem `resultado.png`.

## Funcionalidades

- Leitura e conversão de imagem principal para escala de cinza
- Leitura dos templates de selos em escala de cinza
- Detecção dos selos com `matchTemplate`
- Marcação dos selos detectados com retângulos vermelhos
- Geração de uma imagem com os resultados (`resultado.png`)
