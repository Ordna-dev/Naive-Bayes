import pandas, tkinter, random
from tkinter import filedialog

import pandas, tkinter, random
from tkinter import filedialog

def main(): #Funcion que se encarga de leer el archivo csv y ejecuta las funciones de ZeroR y OneR

    notCatchedData = True

    while(notCatchedData):

        window = tkinter.Tk() 
        window.withdraw() #Código para abrir la ventana de explorador de archivos

        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")]) #El usuario sólo puede seleccionar archivos csv

        #Si el usuario cancela la seleccion de archivo, se sale del loop
        if filename == '':
            print("Se cancelo la seleccion de archivo")
            break

        try:
            read = pandas.read_csv(filename) #Si lee el archivo se asignan los atributos y las instancias a una variable
            notCatchedData = False
        except FileNotFoundError:
            print(f"No se encontro el archivo {filename}.") #En caso contrario, mandará mensaje de error a consola

    data = read.head(50) if filename else None #Leer maximo 50 instancias

    if data is not None:
        test, train = divideData(data) #Se asignan las instancias a los conjuntos de entrenamiento y prueba

        print("\nConjunto de entrenamiento:\n")
        print(train)

        print("\nConjunto de prueba:\n")
        print(test)

        class_attribute = input("Introduce el nombre del atributo clase: ")

        print("\nTabla de frencuencias en el conjunto de entrenamiento:")
        tables(train, class_attribute)

        print("\nTabla de frecuencias en el conjunto de prueba:")
        tables(test, class_attribute)

        #Aca se va a llamar la función tables()


def divideData(data):
    #Se mezclan el orden de los datos
    data = data.sample(frac=1)

    #Calculo de el indice donde se dividen los datos
    divide_index = int(len(data) * 0.7)

    #Se dividen los datos los conjuntos de entrenamiento y prueba
    train = data[:divide_index]
    test = data[divide_index:]

    #Retornamos los conjuntos
    return test, train

def testing(data, class_attribute): #Función puramente para pruebas, pueden tomarlo como base para la realizacion de ZeroR y OneR
    
    counts = data[class_attribute].value_counts() 
    counts_string = str(counts) #Toma los atributos y los cuenta
    counts_string = '\n'.join(counts_string.split('\n')[:-1]) #No imprimir la ultima linea de impresión ya que hay informacion basura

    print(f"\nRecuentos para el atributo clase {class_attribute}:\n{counts_string}")

def tables(data, class_attribute): #Tabla de frecuencias y verosimilitud
    # Iteracion sobre cada columna
    for column in data.columns:
        
        # Se crea la tabla de frecuencias
        frequency_table = data.groupby([column, class_attribute]).size()

        # Se imprime el nombr del atributo
        print(f"\nAtributo: {column}.")

        # Iteracion sobre cada valor unico en la columna
        for value in data[column].unique():
            # Imprimir conteos para vada valor de la clase atributo
            
            counts = []
            for class_value in data[class_attribute].unique():
                count = frequency_table.get((value, class_value), 0)
                counts.append(f"{class_value}: {count}")

            print(f"Valor: {value}. {', '.join(counts)}.")


def naiveBayes(): #Algoritmo de Naive Bayes

    return 0