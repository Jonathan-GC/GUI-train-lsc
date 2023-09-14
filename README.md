

# GUI-train-lsc
#### By _**Miguel Yael Montero, Jonathan Gonzalez**_


Esta interfaz permite a los usuarios clasificar clips de videos sobre LSC para despues ser etiquetados y usados para el entrenamiento de una IA

## Requisitos

1. Debe tener python 3.11
2. Instalar Opencv
3. Instalar numpy
4. Instalar Pillow
5. Instalar ImageMagic

## Como Iniciar

1.- Cree un ambiente virtual  
```bash
python -m venv nombre_de_la_maquina
```


2.- Una vez que haya instalado ImageMagick, sera detectado automaticamente por MoviePy, excepto en windows. Antes de instalar manualmente MoviePy, deber ingresar `moviepy/config_defaults.py` y darle la direccion del archivo binario _ImageMagick_, el cual se llama magick. Esto luce como esto 


```
IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick_VERSION\\magick.exe"
```


```bash
pip install opencv-python
```
```bash
pip install numpy
```
```bash
pip install Pillow
```


