# Clase que representa un bloque de instrucciones
class Bloque:
    def __init__(self):
        # La lista 'instrucciones' almacena las instrucciones dentro del bloque
        self.instrucciones = []
    
    # Método para agregar una instrucción al bloque
    def agregarInstrucction(self, instruccion):
        self.instrucciones.append(instruccion)

# Clase que representa una estructura condicional 'Si' (similar a un 'if' en Python)
class Si:
    def __init__(self, condicion, entonces, si_no):
        # La condición del 'if'
        self.condicion = condicion
        # Bloque de instrucciones que se ejecuta si la condición es verdadera
        self.entonces = entonces
        # Bloque de instrucciones que se ejecuta si la condición es falsa (equivalente a 'else')
        self.si_no = si_no
    
    # Método que permite que un visitante interactúe con esta instrucción
    def acepta(self, visitante):
        visitante.visitaSi(self)

# Clase que representa un bucle 'MientrasQue' (similar a 'while' en Python)
class MientrasQue:
    def __init__(self, condicion, bloque):
        # La condición del bucle
        self.condicion = condicion
        # Bloque de instrucciones que se ejecuta mientras la condición sea verdadera
        self.bloque = bloque
    
    # Método que permite que un visitante interactúe con esta instrucción
    def acepta(self, visitante):
        visitante.visitaMientrasQUe(self)

# Clase que representa la acción de mostrar un mensaje (similar a 'print' en Python)
class Mostrar:
    def __init__(self, mensaje):
        # El mensaje que se quiere mostrar
        self.mensaje = mensaje
    
    # Método que permite que un visitante interactúe con esta instrucción
    def acepta(self, visitante):
        visitante.visitaMostrar(self)

# Clase Visitante, que recorre las instrucciones y las "traduce" a código Python
class Visitante:
    def __init__(self):
        # Controla la cantidad de tabulaciones (sangrías) para el formato de salida
        self.tabulacion = 0

    # Método para imprimir un mensaje con las tabulaciones correspondientes
    def tabular(self, mensaje):
        print("{}{}".format("\t" * self.tabulacion, mensaje))

    # Método para procesar un bloque de instrucciones
    def escribirBloque(self, bloque):
        # Aumenta la tabulación al entrar en un bloque
        self.tabulacion += 1
        # Recorre todas las instrucciones del bloque y les pide que acepten al visitante
        for instruccion in bloque.instrucciones:
            instruccion.acepta(self)
        # Disminuye la tabulación al salir del bloque
        self.tabulacion -= 1

    # Método que procesa una instrucción 'Si'
    def visitaSi(self, si):
        # Imprime la condición 'if' con la tabulación adecuada
        self.tabular("if {}:".format(si.condicion))
        # Procesa el bloque de instrucciones que se ejecuta si la condición es verdadera
        self.escribirBloque(si.entonces)
        # Imprime 'else' con la tabulación adecuada
        self.tabular("else:")
        # Procesa el bloque de instrucciones que se ejecuta si la condición es falsa
        self.escribirBloque(si.si_no)

    # Método que procesa una instrucción 'MientrasQue'
    def visitaMientrasQUe(self, mientrasque):
        # Imprime el 'while' con la condición y la tabulación adecuada
        self.tabular("while {}:".format(mientrasque.condicion))
        # Procesa el bloque de instrucciones dentro del bucle 'while'
        self.escribirBloque(mientrasque.bloque)
    
    # Método que procesa una instrucción 'Mostrar'
    def visitaMostrar(self, mostrar):
        # Imprime el mensaje como si fuera un 'print' con la tabulación adecuada
        self.tabular('print("{}")'.format(mostrar.mensaje))

# Ejemplo de uso del patrón Visitante:

# Crear una instrucción 'Mostrar' que imprime "OK"
mostrar_ok = Mostrar("OK")
# Crear una instrucción 'Mostrar' que imprime "KO"
mostrar_ko = Mostrar("KO")

# Crear una estructura 'Si' (if) con la condición "2 + 2 == 4"
# Si es verdadera, ejecuta un bloque (con 'mostrar_ok') y si no, ejecuta otro bloque (con 'mostrar_ko')
alternativa = Si("2 + 2 == 4", Bloque(), Bloque())
# Agregar la instrucción de mostrar "OK" en el bloque 'entonces' del 'if'
alternativa.entonces.agregarInstrucction(mostrar_ok)
# Agregar la instrucción de mostrar "KO" en el bloque 'else' del 'if'
alternativa.si_no.agregarInstrucction(mostrar_ko)

# Crear un bloque de instrucciones y agregar la estructura 'Si'
bloque_alternativa = Bloque()
bloque_alternativa.agregarInstrucction(alternativa)

# Crear una estructura de bucle 'MientrasQue' (while) que se ejecuta indefinidamente (condición 'True')
# Dentro de este bucle, se evaluará la condición 'Si' que hemos creado
bucle = MientrasQue("True", bloque_alternativa)

# Crear un objeto Visitante para procesar y traducir las instrucciones a código Python
visitante = Visitante()
# El visitante recorre el bucle y todas las instrucciones dentro
bucle.acepta(visitante)


"""Vamos a analizar el recorrido del programa en detalle, enfatizando cómo se realizan los saltos entre métodos y qué significa cada parte del proceso. Para ello, desglosaremos la ejecución paso a paso, indicando específicamente cuándo y por qué se realizan los saltos a otros métodos.

### Estructura General del Programa

El programa está basado en un diseño orientado a objetos que utiliza un **patrón de visitante**. Aquí están las clases y métodos principales:

- **Clases**:
  - `MientrasQue` (representa un bucle `while`).
  - `Si` (representa una estructura `if`).
  - `Mostrar` (representa una acción de mostrar un mensaje).
  - `Visitante` (responsable de visitar y procesar los elementos).

- **Métodos relevantes**:
  - `acepta(self, visitante)` (en cada clase, recibe un visitante).
  - `visitaMientrasQUe(self, mientrasque)` (en `Visitante`, procesa `MientrasQue`).
  - `visitaSi(self, si)` (en `Visitante`, procesa `Si`).
  - `visitaMostrar(self, mostrar)` (en `Visitante`, procesa `Mostrar`).

### Ejecución Paso a Paso

1. **Inicialización del Programa**:
   ```python
   visitante = Visitante()
   bucle.acepta(visitante)
   ```
   - **Pila**:
     - (vacía)

   - Se crea un objeto `visitante` de la clase `Visitante`.

2. **Llamada a `bucle.acepta(visitante)`**:
   - Se llama al método `acepta` del objeto `bucle`, que es una instancia de `MientrasQue`.

   - **Pila**:
     - `acepta(bucle)`

3. **Dentro de `acepta` de `MientrasQue`**:
   ```python
   def acepta(self, visitante):
       visitante.visitaMientrasQUe(self)
   ```
   - Aquí se llama a `visitaMientrasQUe`, pasando `self` (el objeto `MientrasQue`) al visitante.

   - **Pila**:
     - `acepta(bucle)`
     - `visitaMientrasQUe(mientrasque)`

4. **Método `visitaMientrasQUe` en `Visitante`**:
   - Se imprime la línea del bucle `while` y luego llama a `escribirBloque` para procesar el bloque de instrucciones dentro del bucle.

   - **Pila**:
     - `acepta(bucle)`
     - `visitaMientrasQUe(mientrasque)`
     - `escribirBloque(bloque)`

5. **Método `escribirBloque`**:
   - En `escribirBloque`, se recorre cada instrucción del bloque. Solo hay una instrucción, que es `Si`.

   - Aquí, se llama a `acepta` de la instrucción `Si`.

   - **Pila**:
     - `acepta(bucle)`
     - `visitaMientrasQUe(mientrasque)`
     - `escribirBloque(bloque)`
     - `acepta(si)`

6. **Dentro de `acepta` de `Si`**:
   - Se llama al método `visitaSi`, pasando `self` (el objeto `Si`).

   - **Pila**:
     - `acepta(bucle)`
     - `visitaMientrasQUe(mientrasque)`
     - `escribirBloque(bloque)`
     - `acepta(si)`
     - `visitaSi(si)`

7. **Método `visitaSi`**:
   - Se imprime la condición del `if` y luego llama a `escribirBloque` para procesar el bloque `entonces`.

   - **Pila**:
     - `acepta(bucle)`
     - `visitaMientrasQUe(mientrasque)`
     - `escribirBloque(bloque)`
     - `acepta(si)`
     - `visitaSi(si)`
     - `escribirBloque(entonces)`

8. **Dentro de `escribirBloque` del bloque `entonces`**:
   - En este bloque, se llama a `acepta` de la instrucción `Mostrar`.

   - **Pila**:
     - `acepta(bucle)`
     - `visitaMientrasQUe(mientrasque)`
     - `escribirBloque(bloque)`
     - `acepta(si)`
     - `visitaSi(si)`
     - `escribirBloque(entonces)`
     - `acepta(mostrar_ok)`

9. **Dentro de `acepta` de `Mostrar`**:
   - Se llama al método `visitaMostrar`, pasando `self` (el objeto `Mostrar`).

   - **Pila**:
     - `acepta(bucle)`
     - `visitaMientrasQUe(mientrasque)`
     - `escribirBloque(bloque)`
     - `acepta(si)`
     - `visitaSi(si)`
     - `escribirBloque(entonces)`
     - `acepta(mostrar_ok)`
     - `visitaMostrar(mostrar_ok)`

10. **Método `visitaMostrar`**:
    - Imprime "OK". Después de imprimir, este método termina y se retira de la pila.

    - **Pila**:
      - `acepta(bucle)`
      - `visitaMientrasQUe(mientrasque)`
      - `escribirBloque(bloque)`
      - `acepta(si)`
      - `visitaSi(si)`
      - `escribirBloque(entonces)`

11. **Regresando a `visitaSi`**:
    - Después de completar el bloque `entonces`, el control regresa a `visitaSi`. 
    - Aquí se llama a `escribirBloque` para procesar el bloque `si_no`.

    - **Pila**:
      - `acepta(bucle)`
      - `visitaMientrasQUe(mientrasque)`
      - `escribirBloque(bloque)`
      - `acepta(si)`
      - `visitaSi(si)`
      - `escribirBloque(entonces)`
      - `tabular("else:")`
      - `escribirBloque(si_no)`

12. **Procesando el bloque `si_no`**:
    - Se llama a `acepta` en la instrucción `Mostrar` dentro del bloque `si_no`.

    - **Pila**:
      - `acepta(bucle)`
      - `visitaMientrasQUe(mientrasque)`
      - `escribirBloque(bloque)`
      - `acepta(si)`
      - `visitaSi(si)`
      - `escribirBloque(entonces)`
      - `tabular("else:")`
      - `escribirBloque(si_no)`
      - `acepta(mostrar_ko)`
      - `visitaMostrar(mostrar_ko)`

13. **Dentro de `visitaMostrar` para `si_no`**:
    - Imprime "KO". Luego, se sale de `visitaMostrar`.

    - **Pila**:
      - `acepta(bucle)`
      - `visitaMientrasQUe(mientrasque)`
      - `escribirBloque(bloque)`
      - `acepta(si)`
      - `visitaSi(si)`
      - `escribirBloque(entonces)`

### Proceso de Salto a Otros Métodos

Cada vez que se llama a un método (como `visitaMientrasQUe`, `visitaSi`, o `visitaMostrar`), estás "saltando" a ese método:

- **Salto**: Ocurre cuando llamas a otro método (usando `.` y el nombre del método, como `visitante.visitaMientrasQUe(self)`).
- **Retorno**: Cuando un método termina (al llegar al final o usar `return`), se "retorna" al método anterior que lo llamó, que se encuentra en la parte superior de la pila.

### Visualización del Salto

Aquí hay una visualización simplificada de cómo se realiza el salto:

1. **Llamada a un método**:
   - `acepta(bucle)` -> Llama a `visitaMientrasQUe(mientrasque)`.
   - `Pila`: [ `acepta(bucle)`, `visitaMientrasQUe(mientrasque)` ]

2. **Dentro de `visitaMientrasQUe`**:
   - Llama a `escribirBloque(bloque)`.
   - `Pila`: [ `acepta(bucle)`, `visitaMientrasQUe(mientrasque)`, `escribirBloque(bloque)` ]

3. **Dentro de `escribirBloque`**:
   - Llama a `acepta(si)`.
   - `Pila`: [ `acepta(bucle)`, `visitaMientrasQUe(mientrasque)`, `escribirBloque(bloque)`, `acepta(si)` ]

4. **Regresa de `visitarSi` a `escribirBloque`**:
   - Cuando `visitarSi` termina, se retorna a `escribirBloque`.
   - `Pila`: [ `acepta(bucle)`, `visitaMientrasQUe(mientrasque)`, `escribirBloque(bloque)` ]

5. **Continúa en `escribirBloque`**:
   - Luego continúa con el siguiente bloque, y así sucesivamente.

### Conclusión

El control de flujo en este programa sigue un patrón de llamadas y retornos que permite proces"""