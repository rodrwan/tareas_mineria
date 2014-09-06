# Script para tarea 2 de Minería de datos
## Prelimares

1.- Se deben agregar los archivos correspondientes a la carpeta data, donde estarán alojados los archivos con los datos.

2.- Se debe modificar el archivo config.json con los nombres de los distintos archivos.
## Esquema de directorios
```
|-- data # aquí van los archivos con las consultas
|-- folds
|   |-- models # modelos generados de los datos de entrenamiento
|   |-- results # resultados SVM.
|   |-- splits
|       |-- test # fold para testeo.
|       |-- train # fold para entrenar.
|-- json_data
|-- logs # logs para ejecución del script que crea los features.
|-- svm_light
|-- vectors # se guardan los vectores que serán utilizados por SVM.
```
## Install

**NOTE:** se debe tener instalado Python 2.7 y [pip](http://pip.readthedocs.org/en/latest/installing.html) para poder instalar las demás dependencias.

```sh
  $ git clone git@github.com:rodrwan/tareas_mineria.git
  $ cd Tarea2
  $ pip install -r requirements.txt
  $ python feature_1.py # creamos las características
  $ python generate_vectors.py # con esto se generan los vectores
  $ python make_folds.py # con esto se generan los folds para el cross validation
```

Con esto se crearan los archivos por cada categoría correspondientes a los features encontrados en los archivos de las preguntas de Yahoo Answers.

### Paquetes usados

* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [MontyLingua](http://web.media.mit.edu/~hugo/montylingua/)(Modificado)
* [tabulate](https://pypi.python.org/pypi/tabulate)
* [pip](http://pip.readthedocs.org/en/latest/installing.html)

### Formato de features
#### Primer grupo de features
```json
{
  "0": {
    "cuenta": 1,
    "features_1": {
      "CAT_SINTACTICA_MD": 1,
      "ES_TOKEN": -1,
      "FULL_MAYUSCULAS": 0,
      "FULL_MINUSCULAS": 0,
      "INICIO_MAYUSCULAS_RESTO_MINUSCULAS": 1,
      "PALABRA_LARGO": 4,
      "PALABRA_Will": 1,
      "TIENE_RAIZ": 0,
      "qid": "20140618003957AA2mrn7"
    }
  }
}
```

### Problemas

1.- Problema con bases de datos de MontyLingua. Causa: Distintas arquitecturas.

Si obtienes el error 'EOFError: not enough items in file' la posible solución está en este [link](http://frdcsa.org/~andrewdo/WebWiki/MontyLingua.html)

#### Environment
* MacBook Pro Retina
* Procesador 2.6 GHz Intel Core i5
* 8 GB 1600 Mhz DDR3
* Arquitectura x64
* OS X 10.9.4 (13E28)

#### TODOS

* Terminar script para la generación de los demás features.
* Falta crear script para generar los folds para poder utilizar SVM
* Falta crear script para hacer undersampling de tokens