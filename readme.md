<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://img.shields.io/badge/License-MIT-green"/>
    <img src="https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white&color=blue" />
    <img src="https://img.shields.io/github/contributors/MrDeybby/MiniMax-in-reversi-game"/>
    <img src="https://img.shields.io/github/last-commit/MrDeybby/MiniMax-in-reversi-game"/>
  </a>
</p>
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=github,py,vscode" />
  </a>
</p>

# MiniMax-in-reversi-game

Este proyecto de la asignatura *Juegos Inteligentes* es una implementación del juego **Reversi** en terminal, junto con agentes de *Búsqueda adversarial*. El sistema incluye un menú interactivo y selección de jugadores.

---


## Contenido

- [MiniMax-in-reversi-game](#minimax-in-reversi-game)
  - [Contenido](#contenido)
  - [Introducción](#introducción)
  - [1. Requisitos de Instalación](#1-requisitos-de-instalación)
      - [Ejemplo de archivo `requirements.txt`](#ejemplo-de-archivo-requirementstxt)
  - [2. Estructura del Proyecto](#2-estructura-del-proyecto)
    - [Archivos clave para iniciar](#archivos-clave-para-iniciar)
  - [3. Instalación](#3-instalación)
  - [4. Ejecución del Juego](#4-ejecución-del-juego)
    - [4.1. Lanzamiento desde la Línea de Comandos](#41-lanzamiento-desde-la-línea-de-comandos)
    - [4.2. Navegación del Menú y Selección de Jugadores](#42-navegación-del-menú-y-selección-de-jugadores)
  - [5. Modos de Juego](#5-modos-de-juego)
    - [Modo Interactivo](#modo-interactivo)
    - [Modo de Prueba de Algoritmos](#modo-de-prueba-de-algoritmos)
  - [6. Equipo de Desarrollo](#6-equipo-de-desarrollo)
  - [7. Convenciones de commits](#7-convenciones-de-commits)
  - [Licencia](#licencia)

---

## Introducción

Reversi es un juego de mesa para dos jugadores. El objetivo del juego es capturar tantas piezas en forma de disco como sea posible del oponente, atrapándolas entre las tuyas.

Los jugadores se turnan para colocar un disco (pieza del juego) en el tablero, con su color designado hacia arriba.

El objetivo de cada movimiento es atrapar uno o más discos de tu oponente entre dos de los tuyos. Cuando atrapas discos, puedes voltearlos y así invertir su color para que sean tuyos.

El juego termina cuando ambos jugadores han colocado todos sus discos en el tablero, o cuando no hay más movimientos legales posibles para ninguno de los jugadores. El jugador con más discos en el tablero es el ganador.

**MiniMax-in-reversi-game** es una implementación de este popular juego en Python.

El documento a continuación proporciona instrucciones paso a paso para **instalar, configurar y ejecutar el repositorio**. Cubre la configuración inicial, las dependencias necesarias y cómo lanzar tu primera partida usando la interfaz de línea de comandos. El objetivo es poner el sistema en funcionamiento tanto para el juego interactivo como para pruebas de algoritmos.

---

## 1. Requisitos de Instalación

El proyecto **MiniMax-in-reversi-game** está implementado en **Python**.  
La única dependencia externa no estándar es el módulo `keyboard`, utilizado para capturar entradas del teclado en la interfaz de consola.

| Requisito | Versión | Propósito |
|------------|----------|------------|
| Python | 3.7+ | Lenguaje base |
| keyboard (PyPI) | 0.13.5 | Captura de entrada por consola |

---

Todos las dependencias estan en el archivo `requirements.txt`
#### Ejemplo de archivo `requirements.txt`
```text
keyboard==0.13.5
```

---

## 2. Estructura del Proyecto

El repositorio está organizado en los siguientes componentes principales:

| Ruta | Descripción |
|------|--------------|
| `main.py` | Punto de entrada de la aplicación |
| `game/` | Lógica central del juego y utilidades |
| `players/` | Implementaciones de jugadores humanos e IA |
| `output/` | Archivos CSV de métricas de rendimiento |
| `requirements.txt` | Dependencias de Python |

### Archivos clave para iniciar
| Archivo/Directorio | Rol en el proceso de inicio |
|---------------------|-----------------------------|
| `main.py` | Lanza el juego mediante `ReversiGame.app()` |
| `game/reversiGame.py` | Lógica principal de orquestación del juego |
| `game/menu.py` | Sistema de menús para selección de jugador y modo |
| `game/control.py` | Manejo de entrada de teclado |
| `players/` | Contiene todas las clases de estrategias de jugadores |

---

## 3. Instalación

1. **Clonar repositorio**  

```bash
git clone https://github.com/MrDeybby/MiniMax-in-reversi-game
cd MiniMax-in-reversi-game
```

2. **Instalar dependencias**  

```bash
pip install -r requirements.txt
```

---

## 4. Ejecución del Juego

### 4.1. Lanzamiento desde la Línea de Comandos
Para iniciar el juego, ejecuta:

```bash
python main.py
```

Esto abrirá el menú principal, desde el cual podrás **iniciar una partida**, **elegir tipos de jugadores** o **salir**.

**Secuencia de inicio:**
1. `main.py` crea una instancia de `ReversiGame` y llama a su método `app()`.  
2. Se muestra el sistema de menús para seleccionar modo y jugadores.  
3. El bucle de juego es administrado por `ReversiGame.play()`.

---

### 4.2. Navegación del Menú y Selección de Jugadores

Al iniciar, el menú permite:
- Empezar una nueva partida  
- Seleccionar tipos de jugadores (Humano, Minimax, Greedy, Aleatorio, Peor Jugador)  
- Salir de la aplicación  

La navegación se realiza con **W / S / ENTER**.

La selección de jugador se maneja mediante el método estático `select_player` en `ReversiGame`, el cual muestra las opciones y crea una instancia de la clase seleccionada.

| Opción | Clase | Descripción |
|---------|--------|-------------|
| Humano | `HumanPlayer` | Jugador humano mediante entrada de consola |
| Minimax | `MinimaxPlayer` | IA con Minimax + poda alfa-beta |
| Greedy | `GreedyPlayer` | IA con evaluación a una profundidad |
| Aleatorio | `RandomPlayer` | IA que juega movimientos al azar |
| Peor Jugador | `BadPlayer` | Variante débil del Minimax - Selecciona la peor jugada |

---

## 5. Modos de Juego

El sistema soporta dos modos principales:

### Modo Interactivo
- Modo por defecto con interfaz de consola, retrasos y mensajes al usuario.  
- Administrado por `ReversiGame.play()`.

### Modo de Prueba de Algoritmos
- Modo rápido y no interactivo, diseñado para benchmarking de IA.  
- Administrado por `ReversiGame.play_for_algorithms()`.

---

## 6. Equipo de Desarrollo

- **Deybby Rosario**: [@Linkedln](https://www.linkedin.com/in/deybby-rosario/)
- **Sarah Peña**: [@Linkedln](https://www.linkedin.com/in/sarah-v-pena/)
- **Carlos Roa** : [@Linkedln](https://www.linkedin.com/in/carlos-roa-palacio-71674533b/)
- **Hector Reyes** : [@Linkedln](https://www.linkedin.com/in/hector-reyes-ubiera/)

---

## 7. Convenciones de commits

Para mantener un historial claro y consistente, se utilizarán los siguientes prefijos en los mensajes de commit:  

- **add** → para agregar un archivo.
- **feat** → para una nueva funcionalidad.  
- **fix** → para correcciones de errores.  
- **docs** → cambios en documentación.  
- **style** → cambios de formato, espacios, comas, nada que altere lógica.  
- **refactor** → cambios en el código que no agregan funcionalidad ni arreglan bugs.  
- **perf** → optimizaciones de rendimiento.  
- **test** → agregar o corregir pruebas.  
- **chore** → tareas de mantenimiento (configuración, build, dependencias, etc.).  
- **ci** → cambios en integración continua.  
- **build** → cambios que afectan compilación, dependencias, herramientas.  

---

## Licencia  

Este proyecto se distribuye bajo la licencia **MIT**.  