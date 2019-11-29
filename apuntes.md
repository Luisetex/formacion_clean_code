# Clean Code (Python Turbo Edition)

## Definición

No hay una definición única de _Clean Code_, pero podemos ver algunas directrices generales que suelen tomarse como referencia a la hora de "medir" la limpieza del código. En general, los siguientes conceptos están relacionados con el concepto de __Deuda Técnica__. La Deuda Técnica se relaciona con los problemas generados el código debido a una planificación pobre y mala toma de decisiones.

Imaginemos, por ejemplo, que tenemos un camino para llegar de un punto de partida A a un punto de llegada B. Este camino está lleno de obstáculos, plantas espinosas que debemos sortear para poder llegar ahí.Podemos correr a nuestro destino esquivando estas trabas, dejándolas atrás y cumplir nuestro objetivo en poco tiempo.

Quizá ahora no lo tengamos en cuenta, pero nuestro paso por el camino ha podido empeorar la situación: con el paso del tiempo, esas zarzas van a crecer más y quizá hayamos traído con nosotros unas semillas de otras plantas que crecerán en el futuro. Nosotros, que ya hemos cruzado, tendremos una idea de cuáles son los pasos que debemos tomar para poder hacer el camino de nuevo sin resultar heridos, pero tras un tiempo esos problemas pueden ser mayores. Es más, una persona que no haya hecho ese camino con nosotros no conocerá los trucos que hemos empleado para salir airosos de la situación y tendrá que enfrentarse a un problema mayor si cabe.

Esto es lo que sería la deuda técnica en el código. Si no tenemos cuidado y tomamos un camino rápido, sin estructurar, organizar, limpiar y aplicar una serie de estrategias en el código, a la hora de revisitarlo o que una persona nueva quiera trabajar sobre él, llevará más tiempo solucionar los retos que se nos puedan plantear. Es importante no tener en cuenta solo el presente, sino también el futuro y ver el código como un ente vivo en continuo cambio.

La deuda técnica además no es un problema claro que se pueda solucionar como un bug, en el que tenemos excepciones y avisos que nos pueda decir que algo va mal. En cambio, es un __problema silencioso__ que cuando despierte será difícil de solucionar en el corto plazo.

Para poder prevenir este problema vamos a ver una serie de requerimientos que debemos tener muy presentes a la hora de escribir.

## Directrices básicas

### __0. Formato del código__

El formato del código es un primer paso para conseguir nuestro objetivo. En pocas palabras, se trata de adecuar lo que escribimos a una serie de reglas impuestas en un estándar. Estas convenciones nos ayudan a mantener un estilo consistente en nuestro código particular y también en grandes proyectos en el que colaboren varias personas.

En el caso de Python, el estilo de código al que nos adheriremos será __PEP-8__. No hace falta aprender las reglas que lo componen ya que tenemos unos programas llamados _linters_ que nos recuerdan en tiempo real las pifias que hayamos hecho comparando nuestro código con el estándar. No solo nos echarán una mano para recordar que los nombres de las clases comienzan por mayúscula o que las keywords en los métodos no han de tener espacio entre el nombre, el símbolo de igual y la variable que le asignemos, sino que también nos avisarán de algunos bugs potenciales relacionados con la sintaxis del código antes de ejecutarlo.

Para poder verlo en vivo y directo en nuestro editor (por ejemplo, en VS Code), podemos instalar la librería _pylint_ en nuestros entornos virtuales e indicar al editor que utilice ese _linter_ para valorar nuestro código. Con el tiempo, se podrá aprender de los fallos que cometamos ya que nuestro _linter_ nos avisará de qué estamos liándola.

### __1. Documentación y nombrado__

En Python podemos utilizar los conocidos como _docstrings_ para dar explicaciones de nuestras clases y métodos, los parámetros de entrada, sus salidas y una pequeña descripción de su funcionamiento. Estas han de ser mínimas y no debemos perder mucho tiempo. Nuestro código ha de ser lo suficientemente limpio y bien escrito para ser autoexplicativo.

Por ello, los nombres de las variables han de ser: concretos, precisos y únicos a ser posible. Hay que escapar de los nombres genéricos.

### __2. Principios de SOLID__

En este punto hablaremos de los principios de diseño de software __SOLID__ y cómo implementarlos de forma _pythónica_.

### 2.1 __Single responsibility principle__

El principio de responsabilidad única dice que un componente de software (una clase) debe tener solo una responsabilidad. Es decir, solo se debe encargar de una cosa en concreto, por lo que tiene por lo tanto, una única razón para modificarse. Esto hace que no sea necesario modificar a una clase a menudo porque significa que la abstracción del problema ha sido correcta.

* Ejemplo: mirar código srp_1.py

En este caso, la clase tiene métodos que se corresponden a acciones ortogonales; es decir, totalmente independientes del resto.

Esto hace que la clase, al cumplir funciones completamente distinta, sea difícil de mantener ya que debido a su ortogonalidad estructural, puede ser propensa a errores en el diseño.

Por ejemplo, si cambia la fuente de donde se lee el contenido de la operación (leyendo de una base de datos, recibiendo directamente la operación por HTTP, etc.), será necesario cambiar la clase completamente. Lo mismo se puede decir de las otras clases. Nuestro objetivo es hacer que los factores y cambios externos afecten a nuestro código lo mínimo que sea posible.

Un posible cambio sería el siguiente:

* Ejemplo: mirar código srp_2.py

Como solución, se han separado las clases en multiples con una única función independiente. De todos modos, esto no significa que cada clase tenga un solo método. Cualquiera de las clases puede tener métodos extra, siempre y cuando se correspondan a la misma lógica y tarea de la que se encarga.

### 2.2 __Open/Closed principle___

Un módulo o elemento debe ser abierto a extensiones pero cerrado a modificaciones. En otras palabras, nuestro código debe ser extensible y que se pueda adaptar a cambios en el problema. Si cuando queramos añadir algo al código, tenemos que modificar elementos ya escritos, entonces la lógica está mal diseñada.

* Ejemplo: mirar código openclosed_1.py

Como se puede observar, la lógica del programa es muy monolítica y no cumple el principio. Si queremos añadir algo nuevo, habría que modificar toda la lógica de detección de evento.

Como solución:

* Ejemplo: mirar código openclosed_2.py

Aquí se puede ver que el código es perfectamente extensible. Para añadir una función nueva bastaría con añadir una nueva clase que herede de la genérica event e implemente una condición de identificación.

El objetivo final del Open/Closed es la abstracción. A través de un contrato polimórfico (es decir, heredar de una clase genérica y hacer una nueva implementación de sus funciones) se puede hacer una extensión del modelo. De este modo la mantenibilidad del código está presente. Esto no es siempre posible, pero no es aplicable a todos los requerimientos posibles.

### 2.3 __Principio de sustitución de Liskov__

Las propiedades de un objeto deben preservarse en su diseño. En cualquier clase, se debería modificar sus subtipos de forma que el resto del programa no se rompa debido a ello. (Si S es un subtipo de T, los objetos de tipo T se pueden reemplazar por objetos de tipo S sin romperlos).

Esto se relaciona con el llamado diseño por contrato. Las funciones de un programa deben seguir unas reglas estrictas para impedir incompatibilidades entre tipos. En el caso de Python, podemos ver esto mediante extensiones que nos permitan usar un tipado estático.

* Ejemplo, mirar liskov_1.py

En este caso, Mypy nos informa de que meets_condition de LoginEvent es incompatible con el método del supertipo Event. Es decir, el objeto no cumple el mismo tipo que en la superclase. Quien llame a cualquier clase heredera de Event tiene que funcionar transparentemente igual que si se tratase de event. Lo mismo habría sucedido a la hora de devolver un objeto distinto.

Otro fallo de Liskov sería si cambiase la propia signatura de una función:

* Ejemplo, mirar liskov_2.py

Aquí, vemos que el método de meets_condition de LogoutEvent tiene un parámetro extra que Event no tiene.

Las clases derivadas de una base han de ser polimórficas con respecto a los métodos de la interfaz.

### 2.4 __Segregación de Interfaces__

Este principio nos indica que las interfaces han de ser lo más pequeñas posibles.

Las interfaces en general son una serie de métodos que expone un objeto. Todos los mensajes que un objeto puede recibir forman su interfaz. Separan la definición del comportamiento expuesto de una clase de su implementación. En Python, las interfaces se definen implícitamente según sus métodos (_duck typing_). En Python 3, se introdujo el concepto de clase abstracta. Este tipo de clases definen el funcionamiento básico que debe ser implementado por sus clases derivadas.

Se resume a que cuando definamos una interfaz, es mejor que la partamos en múltiples interfaces que contenga muy pocos métodos muy específicos. Al separar las interfaces tanto, las clases nuevas que quieran implementarlas serán cohesivas.

* Ejemplo: mirar interfacesegregation_1.py

Aquí vemos una interfaz que define dos métodos de forma abstracta. Las clases que hereden de ella deben implementar esos métodos para que pueda funcionar con los tipos de eventos que surjan. El problema es, ¿qué sucede si una clase que parsee otros tipos de evento no necesitan uno de los dos métodos ya que solo lo recibe en JSON? La clase abstracta no es lo suficientemente flexible para poder dar cualquier tipo de subclases.

* Ejemplo: mirar interfacesegregation_2.py

En este código observamos que al separar la interfaz en dos clases abstractas, se mantiene la ortogonalidad de las dos funciones independientes manteniendo la funcionalidad original. Aun así, esto no quiere decir que la interfaz solo tenga un método. En ocasiones, las interfaces van a requerir más de un método para funcionar correctamente, como por ejemplo las conexiones y desconexiones de un manager de bases de datos.

### 2.5 __Inversión de dependencias__

Imaginemos que dos objetos de nuestro sistema necesitan comunicarse. El objeto A trabaja con una instancia de B, pero B no es controlado directamente por nuestro código (una librería externa, otro proyecto, etc). Si nuestro código depende en gran parte de B, si este cambia, el código se romperá. PAra prevenir esto, hay que invertir la dependencia: que B dependa de A.

¿Cómo podemos realizar eso? Dando una interfaz y que sea B el obligado a cumplir e implementar dicha interfaz. Si B se va a someter a cambios continuamente, creando una interfaz con la que A se tenga que comunicar, por mucho que cambie B, el trabajo de comunicación desde el lado de A va a ser el mismo, puesto que B tiene que mantener su implementación cumpliendo el contrato que instaura la interfaz.

* Ejemplo:

Tenemos una clase llamada EventStreamer que va a monitorizar evento que se enviarán a una base que recoge los datos para ser analizados. Podemos hacerlo con una clase EventStreamer que interactúe con un destino, SysLog.

Si la clase de alto nivel, EventStreamer depende de SysLog, que implementa numerosos métodos, se puede dar la siguiente situación. Si se hace cambios en cómo se deben enviar los datos a SysLog por cambios en su implementación, habrá que modificar también EventStreamer. Si hay que enviar los datos a otro destino, habría que modificar también los métodos de envío de EventStreamer para añadir tal destino.

¿Cuál puede ser una solución? Hacer que EventStreamer interactúe con una interfaz. Así, las clases que quieran conectarse con EventStreamer necesitarán implementar exactamente los métodos requeridos por la clase abstracta.

* Ejemplo:

Hacer que la clase SysLog implemente los métodos de una clase genérica DataTargetClient. Así EventStreamer solo se tiene que preocupar de que sus métodos funcionen bien con la interfaz, puesto que el resto de subclases tendrán sus mismos métodos.

### Conclusión

En definitiva, los principios de SOLID nos dan una serie de guías útiles, que, aunque no son obligatorias y menos en el caso de Python por su tipado dinámico, nos ayudan a crear un código que, aunque pueda funcionar exactamente igual, nos va a dar una serie de garantías muy útiles a la hora de mantener nuestros proyectos por otros compañeros y sin duda por nosotros mismos.
