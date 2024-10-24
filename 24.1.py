class Fruta:
    def aceptar(self, visitante):
        class_name = self.__class__.__name__
        method = getattr(visitante, 'visitar' + class_name, visitante.default)# este metodo toma de la clase VisitanteFruta que visitante es una instancia de el y busca una valor que tenga VIsitar Manzana en us interior
        return method(self)

class Manzana(Fruta):
    def __init__(self, precio):
        self.precio = precio

class Banana(Fruta):
    def __init__(self, precio):
        self.precio = precio

class VisitanteFruta:
    def visitarManzana(self, manzana):
        return manzana.precio * 1.2  # Precio con impuestos

    def visitarBanana(self, banana):
        return banana.precio * 1.1  # Precio con impuestos

    def default(self, fruta):
        return 0  # Para frutas no reconocidas

# Uso
frutas = [Manzana(100), Banana(50)]
visitante = VisitanteFruta()

for fruta in frutas:
    print(fruta.aceptar(visitante)) # es importante destacar que al heredar de frutaas tiene el metodo aceptar integrado ya con la clase `Fruta`.


"""¡Claro! Vamos a desglosar este paso en detalle, imaginando cómo funciona la pila de llamadas en el IDE. Nos enfocaremos en el momento en que `visitante` (una instancia de `VisitanteFruta`) accede al método `visitarManzana` a través de `getattr`. Aquí te explico cada parte del proceso de manera clara y sencilla.

### Contexto

Ya sabemos que tenemos una clase base `Fruta` y dos subclases: `Manzana` y `Banana`. También tenemos la clase `VisitanteFruta`, que contiene los métodos para procesar estas frutas. Vamos a enfocarnos en el método `aceptar` de la clase `Fruta`, que es donde ocurre la magia.

### Paso a Paso

1. **Instanciación del Visitante**:
   ```python
   visitante = VisitanteFruta()
   ```
   Aquí, creamos un objeto `visitante` que es una instancia de `VisitanteFruta`. Este objeto tiene métodos como `visitarManzana` y `visitarBanana` que se utilizarán más adelante.

2. **Llamada a `aceptar` desde Manzana**:
   ```python
   fruta.aceptar(visitante)
   ```
   Cuando `fruta` es una instancia de `Manzana`, se llama a `aceptar` con el `visitante` como argumento. 

3. **Dentro del Método `aceptar`**:
   ```python
   class_name = self.__class__.__name__  # class_name ahora es "Manzana"
   ```
   - Aquí, `self` es la instancia de `Manzana`. Al llamar a `self.__class__.__name__`, obtenemos el nombre de la clase, que en este caso es `"Manzana"`.

4. **Construcción del Nombre del Método**:
   ```python
   method_name = 'visitar' + class_name  # method_name ahora es "visitarManzana"
   ```
   - Concatenamos el prefijo `'visitar'` con el nombre de la clase (`class_name`), resultando en el string `"visitarManzana"`.

5. **Uso de `getattr`**:
   ```python
   method = getattr(visitante, method_name, visitante.default)
   ```
   - Aquí es donde `getattr` entra en juego. **Esta función busca un atributo o método en el objeto `visitante`**:
     - **`visitante`** es nuestra instancia de `VisitanteFruta`.
     - **`method_name`** es el string `"visitarManzana"`.
     - **`visitante.default`** es un método que se utiliza como fallback (por si no encuentra el método específico, se llamaría a este).

   - **Lo que hace `getattr`**:
     - `getattr` busca en el objeto `visitante` el método llamado `visitarManzana`. 
     - Si lo encuentra, lo devuelve. En este caso, devolverá el método `visitarManzana`.
     - Si no lo encuentra, devolvería `visitante.default`, pero como existe `visitarManzana`, este último no se ejecuta.

6. **Llamada al Método Encontrado**:
   ```python
   return method(self)  # Aquí llama a visitante.visitarManzana(self)
   ```
   - Ahora que tenemos el método `visitarManzana`, se llama a este método, pasando `self` como argumento. En este caso, `self` es la instancia de `Manzana` que tiene el precio 100.

### Resumen de la Pila de Llamadas

- Cuando se llama a `fruta.aceptar(visitante)`:
  - Entra en el método `aceptar` de `Fruta`.
  - Obtiene el nombre de la clase y construye el nombre del método para el visitante.
  - Busca ese método en el objeto `visitante` usando `getattr`.
  - Finalmente, llama al método encontrado (`visitarManzana`), pasando la instancia de `Manzana`.

### Visualización

Imagina la pila de llamadas así:

1. **Llamada a `fruta.aceptar(visitante)`**: 
   - `fruta` (Manzana) llama a `aceptar`.

2. **Dentro de `aceptar`**:
   - `self.__class__.__name__` → "Manzana".
   - `method_name` → "visitarManzana".
   - `method` → `visitante.visitarManzana`.

3. **Llamada a `visitante.visitarManzana(self)`**:
   - Pasa el objeto `Manzana` al método `visitarManzana` del visitante.

Esto permite que el visitante sepa cómo procesar diferentes tipos de frutas sin que cada clase de fruta tenga que implementar su propia lógica de procesamiento. Espero que esto aclare tu duda sobre cómo el patrón de diseño Visitante funciona en este caso. Si necesitas más aclaraciones o ejemplos, ¡no dudes en preguntar!"""