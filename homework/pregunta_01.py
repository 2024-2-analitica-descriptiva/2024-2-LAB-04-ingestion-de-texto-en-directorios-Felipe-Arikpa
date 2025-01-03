# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    import os
    import zipfile
    import pandas as pd

    with zipfile.ZipFile('files/input.zip', 'r') as directory:
        directory.extractall('files')

    root_directory = os.path.join('files', 'input')
    directorios = []

    for file in os.listdir(root_directory):
      directorios.append(file)

    output_directory = os.path.join('files', 'output')
    os.makedirs(output_directory, exist_ok=True)

    train_directory = os.path.join(root_directory, directorios[1])
    test_directory = os.path.join(root_directory, directorios[0])

    def create_dataset(directory):

        data = []
        for sentiment in ['positive', 'neutral', 'negative']:
            sentiment_path = os.path.join(directory, sentiment)
            for filename in os.listdir(sentiment_path):
                file_path = os.path.join(sentiment_path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read().strip()
                data.append({'phrase': text, 'target': sentiment})
        
        dataset = pd.DataFrame(data)

        return dataset
    
    train_dataset = create_dataset(directory=train_directory)
    test_dataset = create_dataset(directory=test_directory)

    train_dataset.to_csv(os.path.join(output_directory, 'train_dataset.csv'), index=False)
    test_dataset.to_csv(os.path.join(output_directory, 'test_dataset.csv'), index=False)

    return print('Archivos creados correctamente')