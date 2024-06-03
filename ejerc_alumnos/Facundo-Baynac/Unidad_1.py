"""
- Explicar con tus palabras que es un algoritmo en general. Y que es un algoritmo en el contexto de la programación.

Se llaman algoritmos el conjunto de instrucciones sistemáticas y previamente definidas que se utilizan para realizar
una determinada tarea. Estas instrucciones están ordenadas y acotadas a manera de pasos a seguir para alcanzar un objetivo.

- Cuantos tipos de lenguaje de programación hay. Enumerarlos y detallar brevemente cada uno.

Primera generación: los primeros ordenadores se programaban directamente en código de máquina (basado en sistema binario),
que puede representarse mediante secuencias de 0 y 1. No obstante, cada modelo de ordenador tiene su propia estructura interna
a la hora de programarse. A estos lenguajes se les denominaba Lenguajes de bajo nivel, porque sus instrucciones ejercen un 
control directo sobre el hardware y están condicionados por la estructura física de las computadoras que lo soportan. Dado que
este tipo de lenguaje se acerca mucho más a la lógica de la máquina que a la humana, es mucho más complicado programar con él.
El uso de la palabra bajo en su denominación no implica que el lenguaje sea menos potente que un lenguaje de alto nivel, sino
que se refiere a la reducida abstracción entre el lenguaje y el hardware. Por ejemplo, se utiliza este tipo de lenguajes para
programar tareas críticas de los sistemas operativos, de aplicaciones en tiempo real o controladores de dispositivos. Otra
limitación de estos lenguajes es que se requiere de ciertos conocimientos de programación para realizar las secuencias de
instrucciones lógicas.

Segunda generación: los lenguajes simbólicos, asimismo propios de la máquina, simplifican la escritura de las instrucciones y
las hacen más legibles. Se refiere al lenguaje ensamblador ensamblado a través de un macroensamblador. Es el lenguaje de
máquina combinado con una serie de poderosas macros que permiten declarar estructuras de datos y de control complejas.

Tercera generación: los lenguajes de alto nivel sustituyen las instrucciones simbólicas por códigos independientes de la
máquina, parecidas al lenguaje humano o al de las Matemáticas. Se crearon para que el usuario común pudiese solucionar un
problema de procesamiento de datos de una manera más fácil y rápida. Son usados en ámbitos computacionales donde se logra un
alto rendimiento con respecto a lenguajes de generaciones anteriores. Entre ellos se encuentran C, Fortran, Smalltalk, Ada,
C++, C#, Cobol, Delphi, Java y PHP, entre otros. Algunos de estos lenguajes pueden ser de propósito general, es decir, que el
lenguaje no está enfocado a una única especialidad, sino que puede usarse para crear todo tipo de programas. Para ciertas
tareas más comunes, existen bibliotecas para facilitar la programación que permiten la reutilización de código.
Cuarta generación: se ha dado este nombre a ciertas herramientas que permiten construir aplicaciones sencillas combinando
piezas prefabricadas. Hoy se piensa que estas herramientas no son, propiamente hablando, lenguajes. Cabe mencionar que,
algunos proponen reservar el nombre de cuarta generación para la programación orientada a objetos. Estos últimos tienen una
estructura muy parecida al idioma inglés. Algunas de sus características son: acceso a base de datos, capacidades gráficas,
generación de código automáticamente, así como poder programar visualmente (como por ejemplo Visual Basic o SQL). Entre sus
ventajas se cuenta una mayor productividad y menor agotamiento del programador, así como menor concentración por su parte, ya
que las herramientas proporcionadas incluyen secuencias de instrucciones. El nivel de concentración que se requiere es menor,
ya que algunas instrucciones, que le son dadas a las herramientas, a su vez, engloban secuencias de instrucciones a otro nivel
dentro de la herramienta. Cuando hay que dar mantenimiento a los programas previamente elaborados, es menos complicado por
requerir menor nivel de concentración. Por otro lado, sus desventajas consisten en que estas herramientas prefabricadas son
generalmente menos flexibles que las instrucciones directas en los lenguajes de bajo nivel. Además, se suelen crear dependencias
con uno o varios proveedores externos, lo que se traduce en pérdida de autonomía. Asimismo, es frecuente que dichas herramientas
prefabricadas contengan librerías de otros proveedores, que conlleva instalar opciones adicionales que son consideradas
opcionales. A menos que existan acuerdos con otros proveedores, son programas que se ejecutan únicamente con el lenguaje que lo
creó. Tampoco suelen cumplir con los estándares internacionales ISO y ANSI, lo cual conlleva un riesgo futuro por desconocerse
su tiempo de permanencia en el mercado. Algunos ejemplos son: NATURAL y PL/SQL.

Quinta generación: La quinta generación de lenguajes de programación [(5GL)] es un término que se refiere a un conjunto de
lenguajes de programación de alto nivel que se centran en la resolución de problemas utilizando inteligencia artificial y
técnicas de programación declarativa. Estos lenguajes de programación utilizan paradigmas de programación no convencionales para
ayudar a los desarrolladores a resolver problemas complejos.

Algunos ejemplos de lenguajes de programación de quinta generación son:

Mercury: Un lenguaje de programación funcional basado en lógica que utiliza un enfoque declarativo para la programación.
OPS5: Un lenguaje de programación basado en reglas que se utiliza en sistemas expertos.
Prolog: Un lenguaje de programación lógico que se utiliza para la programación de inteligencia artificial y sistemas expertos.
Haskell: Un lenguaje de programación funcional que se utiliza en la programación de inteligencia artificial y aprendizaje automático.
Lisp: Un lenguaje de programación funcional que se utiliza en la programación de inteligencia artificial y sistemas expertos.

- Detallar las diferencias entre un lenguaje de programación interpretado y uno compilado.

En el lenguaje interpretado el código se ejecuta línea por línea en un intérprete que realiza los procesos de
bajo nivel, por lo cual no existe un único ejecutable y el código se puede cambiar en ejecución. En cambio 
el lenguaje compilado requiere un compilador, que crea un ejecutable o librería que no puede cambiar su código
en ejecución. Python es un lenguaje INTERPRETADO.
"""