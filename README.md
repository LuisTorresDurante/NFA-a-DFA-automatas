# Convertidor de NFA a DFA
![Estado: Desarrollo Activo](https://img.shields.io/badge/Estado-Desarrollo%20Activo-green)

## Descripción
Esta aplicación web permite convertir Autómatas Finitos No Deterministas (NFA) a Autómatas Finitos Deterministas (DFA). La herramienta proporciona una interfaz gráfica intuitiva para ingresar los componentes del NFA y visualizar el DFA resultante tanto en forma de diagrama como en tabla de transiciones.

## Características
- Interfaz web intuitiva y fácil de usar
- Conversión en tiempo real de NFA a DFA
- Visualización del diagrama de estados
- Generación de tabla de transiciones
- Posibilidad de descargar el diagrama generado
- Validación de entrada de datos
- Manejo de errores con mensajes informativos

## Tecnologías Utilizadas
- **Frontend**: HTML, JavaScript, Tailwind CSS
- **Backend**: Python, Flask
- **Bibliotecas**:
  - `automata-lib`: Para el procesamiento de autómatas
  - Flask: Para el servidor web
  - Tailwind CSS: Para los estilos

## Requisitos de Instalación
1. Python 3.7 o superior
2. pip (gestor de paquetes de Python)
3. Navegador web moderno

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/LuisTorresDurante/NFA-a-DFA-automatas
cd NFA-a-DFA-automatas
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r flask 'automata-lib[visual]' graphviz
```

4. Ejecutar la aplicación:
```bash
python app.py
```

5. Abrir el navegador y acceder a:
```
http://localhost:5000
```

## Uso

### 1. Ingresar los Componentes del NFA
- **Estados**: Lista de estados separados por comas (ejemplo: q0,q1,q2)
- **Símbolos de Entrada**: Símbolos del alfabeto separados por comas (ejemplo: 0,1)
- **Estado Inicial**: Estado inicial único (ejemplo: q0)
- **Estados Finales**: Lista de estados finales separados por comas (ejemplo: q1,q2)

### 2. Definir Transiciones
- Hacer clic en "Agregar Transición" para cada transición necesaria
- Para cada transición, especificar:
  - Estado de origen
  - Símbolo de entrada
  - Estado(s) destino (pueden ser múltiples, separados por comas)

### 3. Realizar la Conversión
- Hacer clic en "Convertir a DFA"
- El resultado mostrará:
  - Diagrama de estados del DFA
  - Tabla de transiciones correspondiente

### 4. Visualizar y Exportar
- El diagrama puede descargarse haciendo clic en "Descargar Diagrama"
- La tabla de transiciones muestra:
  - Estados con indicadores (→ para inicial, * para final)
  - Todas las transiciones posibles

## Estructura del Proyecto
```
nfa-dfa-converter/
├── app.py              # Servidor Flask y lógica principal
├── templates/
│   └── index.html      # Interfaz de usuario
├── static/
│   └── css/
│       └── style.css   # Estilos adicionales (si los hay)
├── requirements.txt    # Dependencias del proyecto
└── README.md          # Documentación
```
