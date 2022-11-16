# Proyecto-3-SO | Tercer proyecto del curso Principios de Sistemas Operativos

## Requisitos

Deberá tener instalado python en su computadora, preferiblemente en su versión 3.9 o posterior.

Instalar varias librerías como:

psutil:

```console
pip install psutil
```

## Uso del programa

La idea de este programa es ver cómo afecta un ramsonware al rendimiento del CPU. Para esto se encripta un archivo de texto plano con un llave secreta de determinado tamaño, y posteriormente, mediante fuerza bruta, se trata de adivinar esa clave y con ello descifrar el archivo. El argoritmo de encriptación utilizado es el RC4.

Para ver cúanto afecta a la ejecución de un programa, dentro de la carpeta **/imgFilter**, se encuentra un programa con el nombre **program.py**, el cual lo que hace es aplicar 10.000 veces un filtro a una imagen que vienen dentro de esa carpeta, usando 10 hilos en el proceso. La idea es medir cuánto dura la ejecución del programa **sin** en ataque y ***con*** el ataque.

Para poder medir este comportamiento, primero se ejecuta el **program.py** solo. Para esto hay que abra una consola y siga los siguientes comandos:

```console
cd imgFilter 
python3 program.py
```

Le saldrá algo como esto:

Se le abrirá una ventana como la siguiente:

![SinAtaque](https://res.cloudinary.com/dnxt7nqdg/image/upload/v1668632986/Proyecto3-SO/Captura_de_pantalla_2022-11-16_150936_ru6nxt.png)

Ahora debemos ejecutar el ataque mientras el **program.py** es ejecutado. Pero antes, debe saber como funciona el Ransomware.

Este se ejecuta de la siguiente manera:

```console 
python3 ransomware.py <filename> <keySize>
```

Donde \<filename> corresponde a la ruta y/o el nombre del archivo que quiera encriptar, y \<keySize> corresponde al largo de la llave utilizada para el cifrado. Tenga en cuenta que, entre más grande la llave, más costará descifrar el archivo y por consiguiente el ataque durará más tiempo.

Por ejemplo, puede ejecutar los siguientes comandos abriendo una consola en el directorio raíz del proyecto:

```console
cd ransomware
python3 ransomware.py example.txt 3
```

Obtendrá algo como lo siguiente, donde además se muestran algunas estadísticas:

![ataque](https://res.cloudinary.com/dnxt7nqdg/image/upload/v1668633686/Proyecto3-SO/Captura_de_pantalla_2022-11-16_152112_smevbi.png)

### Ejecución del experimento

Para el experimento, primero deberá ejecutar el **program.py** con los pasos ya mencionados, y al **mismo tiempo**, ejecutar el ransomware también con los pasos ya descritos.

Puede usar la consola dividida como se muestra a continuación:

Durante la ejecución:

![ejecucion](https://res.cloudinary.com/dnxt7nqdg/image/upload/v1668633847/Proyecto3-SO/Captura_de_pantalla_2022-11-16_152303_yk7ihd.png)

Una vez terminada la ejecución:

![terminada](https://res.cloudinary.com/dnxt7nqdg/image/upload/v1668633847/Proyecto3-SO/Captura_de_pantalla_2022-11-16_152351_jdc5dr.png)

Se puede ver como la duración en la ejecución de **program.py** se ve afectada.

Cabe destacar que entre menos capacidad de procesamiento y/o menos núcleos en el CPU, este ataque afectará en mayor medida a su equipo.