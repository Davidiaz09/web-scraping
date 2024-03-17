#Importando librerias necesarias:
import bs4
import requests

#Código encragado de extraer los titulos de los libros mejor puntuados (4-5 estrellas) de un sitio web.

#lista de titulos de libros mejor puntuados:
lista_libros = []

#Bucle principal que cambia la "url" del sitio web para acceder a cada una de sus paginar e iterar en ellas:
for l in range(1, 51):
    link_p = f"https://books.toscrape.com/catalogue/page-{l}.html"
    
    #haciendo solicitud HTTPS":
    urls = requests.get(link_p)
    
    #Comprobando si hay errores de apertura en el sitio web:
    urls.raise_for_status()
    
    #Convirtiendo la solicitud en un obejto de "bs4" aplicando la propiedad ".text" y el parametro de apertura "lxml"
    contenido = bs4.BeautifulSoup(urls.text, "lxml")
    
    #Creando una lista de todos los libros:
    libros = contenido.select(".product_pod")
    
    #Creando bucle que recorrerá todos los libros y agregará los que tengan una puntuacion igual o superior a 4 estrellas:
    for libro in libros:
        #verificando puntuación:
        if len(libro.select(".star-rating.Five")) >= 1 or len(libro.select(".star-rating.Four")) >= 1:
            
            #Los titulos se encuentran dentro de la etiqueta "a" que contiene dos elementos key-value, el segundo corresponde al titulo.
            #obteniendo el titulo y agregandolo a la lista.
            lista_libros.append(libro.select("a")[1].get("title"))
            
            
#Mostrar los resultados en pantalla:           
for n in lista_libros:
    print(n)
            




"""link_p = f"https://books.toscrape.com/catalogue/page-{1}.html"
urls = requests.get(link_p)
contenido = bs4.BeautifulSoup(urls.text, "lxml")
libros = contenido.select(".product_pod")"""

  
    