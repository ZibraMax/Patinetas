<!-- LTeX: language=es -->

# **Patinetas**

# Requerimientos

-   [ ] ArcGIS Pro>=2.4 **con extensiones**. En su defecto ArcMap **con extensiones**.
-   [ ] Toolbox propia de creación de dataset (opcional).
-   [x] Python>=3.7.5

    Se requieren las siguientes extenisones

    -   [x] Numpy [pip install --upgrade numpy]
    -   [x] Matplotlib [pip install --upgrade matplotlib]
    -   [x] Pandas [pip install --upgrade pandas]
    -   [x] H2o (Requiere java jdk versión 8 a versión 14) [pip install --upgrade h2o]
    -   [x] TensorFlow (v=2.4.0) [pip install --upgrade tensorflow==2.4.0]

    Para instalar las librerías puede usarse anaconda o pip.

-   Información Disponible:
    -   Densidad Pob
    -   Dataset Patinetas
    -   TODO Revisar datos que paso Luis y ponerlos aquí

# Proceso

<!-- ## <a name="tabla1"></a>Creación de dataset desde ArcGIS

-   Usando el Toolbox crear un archivo csv con la siguiente estructura

    | ID  | SES   | Alimentador | CBD     | Colegios | Estaciones | Parques | Vias    | Salud   |
    | --- | ----- | ----------- | ------- | -------- | ---------- | ------- | ------- | ------- |
    | 1   | MEDIO | 4386.82     | 24977.3 | 2509.01  | 7367.53    | 5804.45 | 1180.76 | 2546.35 |

    El nombre de cada una de las columnas debe coincidir con el mostrado en la tabla anterior para que el modelo funcione.

    EL ID debe ser un identificador numérico entero.

    El SES puede estar entre estos valores ['BAJO','MEDIO','ALTO']

    Las otras columnas son valores con presicion double.

    Las columnas numéricas corresponden a la DISTANCIA EUCLIDEANA PROMEDIO MAS CERCANA desde cada zona de interés (cada celda del raster de metronamica) hasta las capas de interés (Colegios, vias, Estaciones, etc.)

    Con la herramienta de ArcGIS Pro este proceso se realizará de manera automática. Para toda bogotá se requieren por lo menos 2GB de almacenamiento libre en el disco principal, ya que ArcGIS generará archivos temporales de este tamaño.

    Si se usa ArcMap, este procedimiento puede realizarse manualmente. Consume tiempo pero es posible, para ello se siguen los siguientes pasos:

    1. Crear un `fishnet` (Herramienta **Create Fishnet**) con _snap_ al raster de metronamica
    2. Realizar un **Zonal Statistics as Table** del `fishnet` con el raster de metronamica.
    3. Hacer **Join** de la tabla generada con el zonal statistics as table con el `fishnet`. Conserve el **promedio** solamente.
    4. Renombre la columna del join anterior como SES_temp. Puede borrar el resto de columnas.
    5. Realize un **Select** sobre el `fishnet` donde seleccione solamente los que tengan un SES_temp = [1,2,3].
    6. Sobre la `capa resultado del select`
        1. Cree una columna de tipo _string_ y llámela **SES**.
        2. Mediante un **Field Calculator** asigne a la columna los valores "BAJO","MEDIO","ALTO" segun corresponda
        3. Elimine la columna SES_TEMP
    7. Renombre la `capa resultado del select` como `capa base`.
    8. <a name="paso8"></a>Elija una de las capas vector expuestas anteriormente [`Alimentador`, `CBD`, `Colegios`, `Estaciones`, `Parques`, `Vias`, `Salud`].
    9. Cree un **Euclidean Distance** de la `capa que escogió`, configure el _extent_ para que sea igual al _extent_ de la `capa base`. El tamaño de celda se debe tomar << al tamaño de celda del `raster de metronamica`, en general se recomiendan valores entre 5 y 10 metros.
    10. Realize un **Zonal Statistics as Table** del `raster resultado del Euclidean Distance` y la `capa Base`. Conserve solamente el **promedio**.
    11. Realiza un **Join** entre la tabla resultado del Zonal Statistics as Table y la `capa base`. Conserve la columna promedio (las otras columnas no son necesarias) y renombre la columna con el nombre que corresponda según la capa que eligió. Recuerde que los nombres deben coincidir con los especificados en la [Tabla](#tabla1).
    12. Volver al [paso 8](#paso8) y realizar el mismo procedimiento con cada una de las capas.
    13. Exportar la tabla de la capa base csv. Abrirla con un editor (como Excel) y revisar que las columnas tengan los nombres correctos, que los separadores de columnas sean "`,`" y que los separadores decimales sean "`.`"
    14. El archivo csv sera entrada del modelo de Random Forest de Python. -->

Si se usa Visual Studio Code, en la carpeta .vscode se encuentran una serie de archivos que automatizan los procesos de compilado y correr modelos.

## Modelos de Python

### Random Forest

### Redes Neuronales

<!--
-   No se necesitan los archivos de entrenamiento
-   Para correr el modelo se puede correr el siguiente comando:

    ```console
    >python predecir.py -i "path_to_input_file.csv" -o "path_to_output_file.csv"
    ```

    Para que funcione el archivo `predecir.py` y los archivos `ModeloValor.zip`, `ModeloDensidad.zip` deben estar en la misma carpeta.

    Los resultados del modelo de Python pueden usarse en ArcGIS importandolos como tabla y posteriormente realizando un **Join**. El atributo en común será el `OBJECTID` o `OID` o `ID`. -->
