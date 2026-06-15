# src/motor_analisis.py

class AnalizadorAlertas:
    """
    Clase que encapsula la matriz numérica y los métodos de ordenamiento.
    Permite instanciar un motor de análisis para priorizar alertas volumétricas.
    """
    def __init__(self, lista_datos):
        """
        Inicializa el objeto guardando los datos.
        Decisión de diseño: Se encapsula la lista como atributo de la instancia (self) 
        para evitar el uso de variables globales y proteger la integridad de los datos 
        durante múltiples ejecuciones de algoritmos.
        """
        self.lista_bytes = lista_datos

    def ordenar_iterativo(self, arreglo):
        """
        Ordena una lista usando Selection Sort O(n^2).
        Decisión de diseño: Opera sobre una copia del arreglo original (.copy()) 
        para no alterar los datos base, permitiendo que otros métodos puedan 
        evaluar la misma muestra intacta más adelante.
        """
        arr = arreglo.copy()
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def ordenar_recursivo(self, arr):
        """
        Ordena una lista utilizando el algoritmo recursivo Merge Sort O(n log n).
        Decisión de diseño: Solo se encarga de la partición (Divide y Vencerás). 
        La lógica de combinación se delegó a otra función para mantener este 
        bloque simple, legible y estricto a su nivel de abstracción.
        """
        if len(arr) <= 1:
            return arr 
        
        medio = len(arr) // 2
        mitad_izq = self.ordenar_recursivo(arr[:medio])
        mitad_der = self.ordenar_recursivo(arr[medio:])
        
        return self._fusionar(mitad_izq, mitad_der)

    def _fusionar(self, izq, der):
        """
        Método auxiliar interno para combinar las mitades del Merge Sort.
        Decisión de diseño: Se abstrae bajo el Principio de Responsabilidad Única. 
        Al ser un método privado (inicia con _), se le indica a la arquitectura 
        que no debe ser llamado directamente desde el exterior del objeto.
        """
        resultado = []
        i = j = 0
        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1
        resultado.extend(izq[i:])
        resultado.extend(der[j:])
        return resultado