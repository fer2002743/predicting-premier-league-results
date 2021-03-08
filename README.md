<div align="center">
  <h1>Curso de Fundamentos de Web Scraping con Python y Xpath</h1>
</div>

<div align="center"> 
  <img src="http://clipart-library.com/images_k/python-logo-transparent/python-logo-transparent-5.png" width="250">
</div>

<h1>¿Qué es el web scraping?</h1>

Web scraping es una tecnica usada por backend developers y data scientist que nos sirve para extraer informacion de internet, por ejemplo de una pagina web.

Para aplicar esta tecnica vamos a usar Xpath, que es un lenguaje expeciaizado en web scraping.

<h1>¿Por qué aprender web scraping hoy?</h1>

El web scraping es utilizado por todo tipo de instituciones, desde agencias de inteligencia para seguirnos el paso hasta tiendas online para recolectar informacion de sus competidores y de esta manera tomar las mejores decisiones. Es por ello que dominar esta tecnica es de gran relevancia para poder conseguir empleo en estas instituciones que usan web scraping. Ademas de esto, hay gran demanda de freelance web scrapers en todo el mundo 

<h1>Python: el lenguaje más poderoso para extraer datos</h1>

En este curso vamos a usar el lenguaje de programacion Python puesto que es el que mas soporte tiene dentro de la comunidad open source para poder desarrollar esta tecnica. Ademas, es uno de los mas espcializados en ciencia de datos. Python ademas nos provee con numerosos modulos que nos facilitaran la tarea de hacer web scraping, algunos de esos modulos son:

- **Request:** Es una libreria que nos permite controlar http
- **BeautifulSoup:** Es otra libreria que nos permite extraer informacion de archivos HTML
- **Selenium:** Este no es libreria, es un framework que nos permite crear navegadores fantasma para controlar sitios web de manera automatica. Un framework es como una aplicacion o conjunto de modulos que nos permiten desarrollar nuestras tareas de una forma mas sencilla. 
- **Scrapy:** Es otro modulo avanzado para hacer web scraping

<h1>Entender HTTP</h1>

HTTP significa Hypertext Transfer Protocol, y es un conjunto de reglas a partir del cual dos ordenadores se comunican en internet. Estos ordenadores tienen un nombre, su nombre es: por un lado el cliente y por otro lado el servidor. El cliente es quien realiza una peticion y el servidor es el que responde a esta peticion.

Una peticion de un cliente al servidor se ve asi:

```py
# Request
GET / HTTP/1.1 #en este metodo mi ordenador le pide al data center que traiga este documento y tambien podemos ver la version del protocolo
Host: developer.mozilla.org  
Accept-Language: fr #el lenguaje que aceptamos para la informacion que solicitamos

#una vez enviamos estos datos el servidor nos responde

# Response  
HTTP/1.1 200 OK #version del protocolo, el numero 200 significa que todo esta OK.
Date: Sat, 09 Oct 2010 14:28:02 GMT #fecha de respuesta
Server: Apache #servidor desde donde se da la respuesta
Last-Modified: Tue, 01 Dec 2009 20:18:22 GMT  ETag: "51142bc1-7449-479b075b2891b" #ultima fecha de modificaion de la respuesta que se nos da
Accept-Ranges: bytes  Content-Length: 29769  Content-Type: text/html #tipo de respuesta que recibimos
<!DOCTYPE html... (here comes the 29769 bytes of the  requested web page)
```

Ahora vamos a identificar donde se encuentra HTTP dentro de la web, por debajo de HTTP encontramos los siguientes protocolos: 

- IP: Internet Protocol, que  es de donde salen las direcciones unicas que identifican de a nuestros ordenadores en la red.

- TCP: Transmission Control Protocol, que es un protocolo que establece como se va a transferir informacion a bajo nivel.

- UDP: User Data Protocol, parecido a TCP

- TlS: Tansport Layer Security, encargado de encriptar la informacion que transmitimos para que ningun atacante pueda acceder a ella

- DNS: Domain Name System, que es el que resuelve un nombre de nominio a una IP.

Finalmente, encima de todo esto esta HTTP. HTTP nos permite transportar los siguientes elementos:

- HTML: Es el lenguaje que contiene la informacion que usamos para hacer web scraping.

- CSS: Un lenguaje que nos permite establecer el diseño de las paginas web.

- JavaScript: Lenguaje que nos permite crear la interaccion entre el usuario y la pagina web.

- Web APIs: APIs is Application Programming Interface which is a software that acts as an intermediary to allow to applications to comunicate between them.

En esta imagen podemos apreciar todo lo anterior:
<div align="center"> 
  <img src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fdd7a74b3-8b8e-4eb5-b89a-08f4aed238c7%2FUntitled.png?table=block&id=ad82d0a3-00c2-4743-9d85-5b35153074f1&width=1190&userId=&cache=v2" width="250">
</div>


**Reto Statuscode mas utilizadoss**
- Statuscode	Significado
- 200	OK
- 301	Redirección permanenze
- 302	Encontrado
- 303	See other– Mirar en otra página
- 307	Redirección temporal
- 404	No encontrado
- 410	No encontrado permanentemente
- 500	Error del servidor
- 503	Servidor no responde

**Retos cabeceras HTTP mas utilizadas**

- Server: indica el tipo de servidor HTTP empleado.
- Age: indica el tiempo que ha estado el objeto servidor almacenado en un proxy cache (en segundos)
- Cache-control: lo usa el servidor para decirle al navegador que objetos cachear, durante cuanto tiempo, etc..
- Content-Encoding: se indica el tipo de codificación empleado en la respuesta
- Expires: indica una fecha y hora a partir del cual la respuesta HTTP se considera obsoleta. Usado para gestionar caché.
- Location: usado para especificar una nueva ubicación en casos de redirecciones.
- P3P: se usa para especificar el tipo de política de privacidad empleado en la web. No está muy extendido.
- Set-Cookie: sirve para crear cookies. Las famosos cookies viajan entre el servidor y el navegador a través de estas cabeceras HTTP.

<h1>HTML</h1>

HTML stands for Hypertext Markup Langauge, es un lenguaje que nos permite determincar la estructura que va a tener una pagina web. Por otro lado, CSS nos permite desarrollar los estilos visulaes y JavaScript nos permite crear la interaccion entre la pagina web y el usuario.

En HTML, a lo que esta encerrado entre corchetes angulares(<>) lo llamamos etiqueta, y dentro de esta etiqueta es donde nosotros guardamos el contenido. Ademas las etiquetas pueden tener atributos, por ejemplo <p> para indicar un parrafo o  <a> que significa links.

**Reto utilidad etiqueta script en HTML:** Esta etiqueta se usa para poder insertar o hacer referencia a un script ejecutable dentro de un documento HTML.

**Definicion metadatos:** Los metadatos son datos que proveen informacion acerca de la propia pagina web que los contiene. por ejemplo: autor, título, fehca, palabras clave

**etiquta iframe:** La etiqueta iframe nos permite mostrar una pagina externa dentro de HTML

<h1>Robots.txt: permisos y consideraciones al hacer web scraping</h1>

Robots.txt es un documento que se encuentra en la raiz de un sitio e indica a que partes de el pueden acceder y a que partes no pueden acceder los rastreadores de motores de busuqueda. Principalmente, se utiliza para evitar que tu sitio web se sobrecargue con solicitudes.
En el contexto de webscraping, le dice al scraper que puede y no extraer. Es decir hasta donde puede llegar. Ya que infrigir en la violación
de estas directivas puede acarrear un problema legal con el sitio web al que estamos scrapeando.

Este archivo contiene algunos elementos como:

- **USER-AGENT:** Identifica quien puede acceder al sitio web

- **Directivas:** Las direstivas son: **allow**, este directorio se usa para permitir a los motores de busqueda rastrear un subdirectorio o una pagina. Por otro lado **disallow** se utiliza para idicar que archivos y paginas no se esta permitido acceder.


<h1>XML Path Langugage</h1>

Extensible Markup Language es un lenguaje muy parecido a HTML que se utilizo para crear interfaces y que al igual que HTML esta integrado por etiquetas. Una tecnica para extraer datos de este lenguaje es usando XPATH. Entonces, como HTML es un lenguaje tan parecedo a Extensive Markup Language, podemos usar Xpath para extraer datos de HTML sin ningun problema.

<h1>Tipos de nodos en XPath</h1>

Un nodo es lo mismo que una etiqueta y su contenido. En esta clase nos familiarizamos con el lenguaje HTML y sus etiquetas, dado que vamos a usar XPath para acceder a las etiquetas que tienen la informacion que queremos para extraer su informacion.

<h1>Expresiones en XPath</h1>

La primera expresion que vamos a utilizar es:
```py
$x('/')
#en este caso en  concreto selecciono a todo el documento

$x('/html')
#En este caso solo selecciono el documento HTML
```
Con esta expresion podemos movernos de un sitio a otro de la pagina web. Pero que pasa cuando queremos acceder a un nodo en particular pero queremos evitar poner toda la ruta hasta alli??. Pues muy facil, escribimos dobre eslash y ponemos la ruta directamente:

```py
$x('//h1')
#en este caso estoy seleccionando todos los nodos con la etiqueta h1

#ahora supongamos que quiero seleccionar el texto de ese nodo, para ello escribo:

$x('//h1/text()')

#por otro lado, si queremos seleccionar el nodo actual lo que hacemos es:

$x('//span/.')

#esto que acabamos de hacer es lo mismo que lo que habiamos hecho antes:

$x('//span')

#pero si queremos seleccionar a todos los nodos por encima del que nos encontramos escribimos:

$x('//span/..')
```

Finalmente, vamos a aprender a extraer atributos, lo cual hacemos con la siguiente expresion:
```py
$x('//span/@class')

#con esta expresion extraemos todos los atributos de tipo class que hay en span. Cuando escribimos @ despues de un slash significa que vamos a extraer un atributo, y despues escribimos el atributo.
```

<h1>Predicados en Xpath</h1>

Con lo aprendido en la clase anterior no es suficiente para poder filtrar todo lo que queremos de las paginas web, para ello necesitamos los predicados.

Supongamos que tengo la siguiente expresion:

```py
$x('/html/body/div/div')
```

Sin embargo supongamos que yo no quiero a los dos nodos div, yo solo quiero el primero, para ello uso el predicado [1], que se pone al final del ultimo nodo. 

```py
$x('/html/body/div/div[1]')
```

Pero ahora supongamos que yo quiero el ultimos predicado, para ello en vez de usar [1], uso el predicado [last].

```py
$x('/html/body/div/div[last()]')
```

Ahora supongamos que quiero traer todos los elementos que hay en el nodo span, pero quiero poner una condicion, y dicha condicion es que al menos contengan el atributo class, para ello escribo

```py
$x('//span[@class]')
```

Pero ahora me voy a volver mas exquisito, y es que ahora ademas de que los elementos tengan la clase class, quiero que esa clase sea un texto, en este caso tengo que escribir:

```py
$x('//span[@class="text"]')
```

<h1>Operadores en Xpath</h1>

Para ser capaces de filtrar de una forma mas avanzada nos vamos a valer de operadores. Supongamos que quiero traer todos los elementos de spam que tienen una clase distinta a texto, para ello hacemos esto:

```py
$x('//span[@class != "text"]')
```

Si recordamos clases anteriores, cuando usamos el predicado [1] o [last()] traemos el ultimo o el primer elemento, sin embargo, que pasa cuando tengo mucho elementos??. En este caso puedo usar un operador para filtrar que elementos quiero, por ejemplo:

```py
$x('/HTML/body/div/div[position()>1]')
#esta expresion me trae los elementos que estan de uno para arriba
```

Por otro lado, tambien podemos usar los operadores logicos "and" y "or", por ejemplo

```py
#operador logico and
$x('//span[@class="text and @class="tag-item"]')

#operador logico or
$x('//span[@class="text" or @class="tag-item"]')

#operador not

$x('//span[not (@class="text")]')
```


<h1>Wildcards en Xpath</h1>

Que pasa si no sabemos el lugar exacto en el que se encuentra el nodo que queremos escrapear, pero si sabemos mas o menos donde se encuentra?. En estos casos tenemos una solucion llamada wildcards, o en español, comodines.

El primer comodin nos sirve para indicar que queremos traer todos los nodos que estan inmediatamente despues:

```py
$x('/*')
#con este comodin podemos traer nodos que no sabaemos como se llaman pero si sabemos donde se encuentran
```

Si recordamos, con $x('//') podemos saltar niveles en XPath, y con * seleccionamos todos los nodos que se encuentran inmediatamente despues. Pero si combinamos
estas dos expresiones, seleccionamos todos los nodos en todas direcciones, o en otras palabras, lo seleccionamos todo:

```py
$x('//*')
```

Por otro lado, el siguiente wildcard nos trae a todos los nodos span que tengan clase text:

```py
$x('//span[@class="text"]/@*')
```

El siguiente wildcard nos permite traer todos los atributos de los nodos div:

```py
$x('/HTML/body//div/@*')
```

Finalmente, tenemos un wildcard que nos permite traernos todo lo que se encuentra inmediatamente despues de donde estamos, sean nodos, texto o culaquier tipo de elementos:

```py
$x('//span[@class="text" and @itemprop="text"]/node()')

#con esto traemos todo lo que se encuentra despues, independientemente de lo que sea.
```

<h1>In-text search en Xpath</h1>

En esta clase vamos a aprender a buscar lo que queremos dentro del text.

Supongamos que quiero traer todos los autores que comienzan por determinada letra, por ejemplo la letra A, para ello hago lo siguiente:

```py
$x('//small[@class="author" and starts-with(., "A")]')

#dentro de starts-with el punto significa que busque en el nodo actual, y la letra entre comillas significa la letra
```

Pero esto no es todo, tambien podemos usar la funcion contains de la siguiente manera:

```py
$x('//small[@class="author" and contains(., "RO")]')
```

Por otro lado, tambien podemos seleccionar lo que queremos fijandonos en las letras finales:

```py
$x('//small[@class="author" and ends-with(.,"ing")]')

#en el navegador me va a salir error porque en los navegadores usan la version 1.0 de XPath, y esta funcion esta en la version 2.0, sin embargo, cuando ejeccute esta funcion en python no tendre ningun problema
```

Matches la utilizamos para encontrar un texto en un nodo que coincida con cierta expresion regular.

```py
$x('//small[@class="author" and matches(., "A.n*")]')

#esto selecciona los nombres que empiezan con A y terminan en n
```


<h1>XPath Axes</h1>

Para un nodo el su nodo padre es el que esta inmediatamente encima de el, sin embargo, todos sus antepasados son todos los nodos que estan por encima de el y que estan relacionados de manera directa. Por otro lado, los nodos hijos son aquellos nodos inmediatamente despues del nodo en el que nos encontramos. Sin embargo, todos los nodos descendientes son todos los nodos que se encuentran por debajo. Añado una imagen para que se haga mas facil entender todo lo que acabo de explicar:

<div align="center"> 
  <img src="https://static.platzi.com/media/user_upload/anchestors-cd09ebcf-160c-43dd-a7c5-e9c45b4140e2.jpg" width="250">
</div>

Por ejemplo supongamos que quiero traer el nodo en el cual me encuentro actualmente:

```py
#asi es como lo habiamos hecho antes
$x('/HTML/body/div/.')

#sin embargo, la manera completa de hacerlo es:
$('/HTML/body/div/self::nombre del nodo en el que estomos')

#en XPath los dos puntos (::) significan lo mismo que el punto (.). A esto en XPath se le conoce como azucar sintactica, que es una manera mas bonita y corta de escribir algo mucho mas largo y enrrevesado


#si por ejemplo me quiero traer los nietos hago:

$x(''/HTML/body/div/child::nombre del nodo en el que estomos')


#Pero tambien me puedo traer a los nietos, es decir todos los nodos que estan en niveles inferiores:

$x('/HTML/body/div/descendant::nombre del nodo en el que estomos')

#Pero si me quiero traer a los descendientes del nodo y a el nodo en si mismo lo que hago es:

$x('/HTML/body/div/descendant-or-self::nombre del nodo en el que estomos')
```