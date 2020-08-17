"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time 

def loadCSVFile (file, lst, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    del lst[:]
    print("Cargando archivo ....")
    
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
     
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
<<<<<<< HEAD
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Consultar buenas peliculas de Director")
=======
    print("3- Contar elementos filtrados por palabra clave del titulo de una pelicula")
    print("4- Consultar las peliculas buenas de un director")
>>>>>>> origin/master
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0 #Cantidad de repeticiones
        for element in lst:
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, list1,list2):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
<<<<<<< HEAD
    """    
=======
    """
    t1_start = process_time() #tiempo inicial
    vota=0
    id=0
    buenas=0
    sumsi=0
    for f in range(1,len(list2)):
            if criteria== list2[f]["director_name"]:
                id=list2[f]["id"] 
                if id==list1[f]["id"]:
                    vota=list1[f]["vote_average"]
                if float(vota) >=6.0:
                    sumsi+=float(vota)
                    buenas+=1
    if buenas !=0:
        prom=round(sumsi/buenas,2)
    else:
        prom=0
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return [buenas,prom]
>>>>>>> origin/master

    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        for element in lst:
            if element[column].lower() == criteria.lower():
                counter+=1
        t1_stop = process_time()
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter 
 
def countElementsBy2Criteria(criteria_1,lst_1,lst_2):
    lst_prov=[]#inicializa lista_provisional
    count=0#inicializa conteo
    prom=0#inicializa promedio
    if len(lst_1)== len(lst_2) == 0   : #verifica que ninguna lista esté vacia
        print("La lista esta vacía")
        return -1
    elif len(lst_1) != len(lst_2): #verifica que ambas listas de datos tengan misma longitud
        print("La listas no coinciden")
        return -1
    else:
        t1_start = process_time()
        for element in lst_2:
            if element["director_name"]== criteria_1:#filtra por director
                lst_prov.append(element["id"])#guarda id de filtrados
        for element in lst_1:
            if element["id"]in lst_prov and float(element["vote_average"])>=6: # filtra por director y si cumple con que es buena pelicula
                count+=1
                prom+=float(element["vote_average"])
        del lst_prov[:]# elimina lista provisional
        t1_stop = process_time()
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
        return count,round(prom/count,1)
    
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
<<<<<<< HEAD
    detalles = [] #instanciar lista vacia archivo detalles
    casting = []  #instanciar lista vacia archivo casting
    x= True
    while x:
=======
    lista1 = []
    lista2=[] #instanciar una lista vacia
    while True:
>>>>>>> origin/master
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
<<<<<<< HEAD
                opcion=input("Seleccione 1 para agregar todos los datos y 0 para datos de prueba\n5")
                if int(opcion)==1:
                    loadCSVFile("Data/themoviesdb/AllMoviesDetailsCleaned.csv", detalles) #llamar funcion cargar datos
                    loadCSVFile("Data/themoviesdb/AllMoviesCastingRaw.csv", casting)
                    pass
                elif int(opcion)==0:
                    loadCSVFile("Data/SmallMoviesDetailsCleaned.csv", detalles) #llamar funcion cargar datos
                    loadCSVFile("Data/MoviesCastingRaw-small.csv", casting)
                    pass
                print("Datos cargados, "+str(len(casting)+len(detalles))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if len(detalles)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene "+str(len(detalles))+" elementos")
            elif int(inputs[0])==3: #opcion 3
                criteria =input('Ingrese el criterio de búsqueda\n')
                counter=countElementsFilteredByColumn(criteria, "title", detalles) #filtrar una columna por criterio  
                print("Coinciden ",counter," elementos con el criterio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                criteria =input('Ingrese el criterio de búsqueda\n')
                counter=countElementsByCriteria(criteria,0,detalles)
                print("Coinciden ",counter," elementos con el criterio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==5: #opcion 5
                director = input('Ingrese el nombre del director ')
                counter= countElementsBy2Criteria(director,detalles,casting)
                print("Coinciden ",str(counter[0])," peliculas buenas para el director: '", director ,"con un promedio de calificación: ",str(counter[1]))
=======
                loadCSVFile("Data/AllMoviesDetailsCleaned.csv", lista1)
                loadCSVFile("Data/AllMoviesCastingRaw.csv", lista2) #llamar funcion cargar datos
                print("Datos cargados, "+str(len(lista1))+" elementos cargados")
                print("Datos cargados, "+str(len(lista2))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if len(lista1)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else: print("La lista del archivo1 tiene "+str(len(lista1))+ " elementos")
                if len(lista2)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")        
                else: print("La lista del archivo2 tiene "+str(len(lista2))+" elementos")
            elif int(inputs[0])==3: #opcion 3
                criteria =str(input('Ingrese el criterio de búsqueda\n'))
                counter=countElementsFilteredByColumn(criteria, "title", lista1) #filtrar una columna por criterio  
                print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                criteria =input('Ingrese el nombre del director:\n')
                counter=countElementsByCriteria(criteria,lista1,lista2)
                print("El director",criteria,"tiene",counter[0],"buenas peliculas y este tiene un promedio de votaciones de: ", counter[1])
>>>>>>> origin/master
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()
