#el primer paso es importar todas las libreias que voy
#a utilizar:

import requests
from lxml import html #la funcion HTML sirve para convertir archivos de HTML a un tipo de archivo con el cual pueda aplicar XPath
import os #vamos a utilizar este modulo para crear una carpeta con la fecha de hoy
import datetime #nos permite traer la fecha de hoy

#despues debo crear las constantes que me llevaran 
#al cuerpo, el titulo y el resumen de la noticia.

#contiene el link a la pagina principal de la republica
HOME_URL = 'https://www.larepublica.co'

XPATH_LINK_TO_ARTICLE = '//div[@class="V_Title"]/h2/a/@href'
XPATH_LINK_TO_TITLE = '//div[@class="mb-auto"]/h2/span/text()'
XPATH_LINK_TO_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_LINK_TO_BODY = '//div[@class="html-content"]/p[not(@class)]/text()'


#ahora voy a crear las funciones de este programa

#la funcion parse_home es la que se encarga de obtener
#los links a las noticias:


def parsed_notice(link, today):
    #envuelvo en un bloque try en caso de que el status_code de mi
    #peticion sea distinto a 200
    try:
        response = requests.get(link)#solicito respusta al link de la noticia
        if response.status_code == 200:
            #primero quiero traer el documento html de la noticia
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)#lo convierto a un documento para aplicar xpath

            #el error contra el que me quiero proteger es si summary no tiene indices
            #es decir, no existe, en ese caso lo que quiero es salirme de la fucnion porque no
            #quiero noticias sin resumen
            try:
                #a estas variables pongo indices porque el resultado de aplicar xpath
                #a un html con superpoderes (parsed) nos devuleve una lista que puede tener uno a varios elementos
                #en este caso nosotros sabemos que el titulo, el resumen y el cuerpo
                #son el elemento 1 de una lista (index 0)
                title = parsed.xpath(XPATH_LINK_TO_TITLE)[0]
                #ahora voy a manejar el posible error de que el titulo tenga comillas
                #este link explica porque https://platzi.com/comentario/2198698/
                title = title.replace('\"','')
                summary = parsed.xpath(XPATH_LINK_TO_SUMMARY)[0]
                #a body lo dejamos sin indice porque body es una lista de parrafos
                body = parsed.xpath(XPATH_LINK_TO_BODY)
            except IndexError:
                return 
    #ahora vamos a guardar esta informacion. with es un gestor de contexto
    #es como un try bloc, en caso de que algo salga mal hace que el 
    #archivo no se corrompa. despues uso la funcion open para abrir archivo. Con esta fucnion
    #busco la carpeta que se creo con la fecha de hoy y dentro de esa carpeta
    #guardo un archivo que tiene como nombre el titulo de la noticia.
    #dentro de la funcion open el primer parametro nos indica la ruta del archivo, el segundo
    #nos dice que entramos en modo escritura, y el encoding nos permite guardar los caracteres especiales
    #de manera correcta para que no haya errores. Finalmente, nombro todo esto como
    # f
            with open(f'{today}/{title}.txt','w', encoding='utf-8') as f:
                f.write(title)
                f.write('/n/n')
                f.write(summary)
                f.write('/n/n')
                #necesito el for porque el body es una lista de parrafos
                for p in body:
                    f.write(p)
                    f.write('/n')

            
        else:
            raise ValueError(f'ERROR: {response.status_code}')
    except ValueError as ve:
        print(ve)

def parse_home():
    #sin embargo, tendo que proteger mi codigo en caso
    #de errores como el codigo 404
    try:
        #con la funcion de request me traigo el archivo
        #HTML de la pagina
        response = requests.get(HOME_URL)#con esto no solo obtengo el documentos HTML sino tambien http, como las cabeceras
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            #.content traer el archivo HTML y el .decode('utf-8') 
            #me ayuda a convertir los caracteres raros (ñ, tildes) en algo que 
            #python pueda entender
            
            parsed = html.fromstring(home)
            #toma el archivo html de home y lo convierte en un tipo de archivo 
            #a partir del cual yo puedo hacer XPath


            #ahora lo que me falta es obtener una lista de los links
            #que obtenga que he obtenido hasta ahora
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            #print(links_to_notices)
            
            today = datetime.date.today().strftime('%d-%m-%Y')
            #del modulo datetime traemos la funcion date y traemos
            #la fecha de hoy. Hasta esta parte guardamos un objeto 
            #que nos da la fecha de hoy, pero lo que yo quiero es una string
            #que me de la fecha en el formato dia/mes/año, par ello uso
            #la funcion .strftime('%d-%m-%Y')

            
            
            #os.path.isdir(today) trae un booleano cuyo valor dependen de si hay 
            #o no una carpeta con el nombre que hemos establecido (today) en la
            #carpeta en la que estamos. Si esa carpeta no existe creamos esa carpeta
            if not os.path.isdir(today):
                #con esto creamos una carpeta con el nombre de la fecha de hoy
                os.mkdir(today)

                #por cada link en la lista vamos a entrar y extraer lo que queremos
                for link in links_to_notices:
                    #esta funcion entra al link y extrae la infomacion que queremos
                    #y eso lo va a guardar usando la fecha de hoy.
                    parsed_notice(link, today)
            
            
        else:
            raise ValueError(f'ERROR: {response.status_code}')
    except ValueError as ve:
        print(ve)



#la siguiente es la funcion principal, la que se va a ejecutar

def run():
    parse_home()


if __name__ == '__main__':
    run()