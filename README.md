# Asteroids

Versión propia del clásico juego *Asteroids* hecha en Python con Pygame.
Proyecto universitario de Introducción a la Ingeniería.

Autor: **Ignacio Patricio Faúndez Pérez**

## Cómo jugar

| Tecla | Acción |
|-------|--------|
| Flechas | Mover la nave (al salir por un borde apareces por el lado opuesto) |
| Espacio | Disparar |
| Cualquier tecla | Empezar desde la pantalla de inicio |

Hay asteroides, dos tipos de aliens (rojo y amarillo), barra de escudo y power-ups
(escudo y mejora de disparo).

## Cómo ejecutarlo

1. Instala [Python](https://www.python.org/downloads/) (se probó con 3.12).
2. Instala Pygame:
   ```
   pip install -r requirements.txt
   ```
3. Ejecuta el juego desde esta carpeta (para que encuentre `Imagenes/` y `Sonidos/`):
   ```
   python Asteroids.py
   ```

## Pendientes conocidos

- Falta un menú principal y un modo sin límites.
- Falta un scoreboard para tener ranking histórico

## Créditos

- Imágenes: pack *Space Shooter Redux* de Kenney (kenney.nl).
- Música: *Frozen Jam* de tgfcoder.
- Efectos de sonido: ver la carpeta `Sonidos/`.
