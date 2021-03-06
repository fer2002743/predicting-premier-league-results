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


**Reto Statuscode mas utilizadoss**
Statuscode	Significado
200	OK
301	Redirección permanenze
302	Encontrado
303	See other– Mirar en otra página
307	Redirección temporal
404	No encontrado
410	No encontrado permanentemente
500	Error del servidor
503	Servidor no responde

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

- **Directivas:**Las direstivas son: **allow**, este directorio se usa para permitir a los motores de busqueda rastrear un subdirectorio o una pagina. Por otro lado **disallow** se utiliza para idicar que archivos y paginas no se esta permitido acceder.


<h1>XML Path Langugage</h1>

Extensible Markup Language es un lenguaje muy parecido a HTML que se utilizo para crear interfaces y que al igual que HTML esta integrado por etiquetas. Una tecnica para extraer datos de este lenguaje es usando XPATH. Entonces, como HTML es un lenguaje tan parecedo a Extensive Markup Language, podemos usar Xpath para extraer datos de HTML sin ningun problema.