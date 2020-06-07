## Acerca
CPL - Cartagena Potholes Locator

## Desarrollo
### Requerimientos
- [Python](https://www.python.org/)
- [NPM](https://www.npmjs.com/)

### Preparar (Front-end)
```sh
  # Instalar dependecias
  npm install

  # Compilar para desarrollo
  npm run dev

  # O compilar para cuando hayan cambios
  # (En una consola independiente)
  # npm run watch

  # O compilar para producción
  # npm run prod
```

### Preparar (Back-end)
```sh
  # Instalar ambiente virtual
  py -m venv venv

  # Activar ambiente virtual
  venv\scripts\activate

  # Instalar requerimientos
  pip install -U -r requirements.txt
```

### Configurar
```sh
  # Definir
  set FLASK_APP=application.py

  # Modo debug
  set FLASK_ENV=development
```

### Datos de prueba
```shell
  # Abrir
  flask shell

  # Importar
  from database import seeder

  # Generar
  seeder.run()

  # Cerrar usando ^Z (CTRL + Z)
```

### Ejecutar
```sh
  # Ejecutar
  flask run

  # Ir a http://127.0.0.1:5000
```

## Registro de Cambios
Todos los cambios notables a este proyecto están documentados en esta parte del archivo. El formato está basado en [Keep a Changelog](http://keepachangelog.com/).

#### [x.y.z] - AAAA-MM-DD
- **x** para versiones principales relacionadas con adiciones o cambios importantes.
- **y** para versiones menores relacionadas con adiciones o cambios menores en la versión principal actual.
- **z** para versiones menores relacionadas con adiciones o cambios menores en la versión menor actual.

#### Extras
- **Agregado** para nuevas funciones.
- **Modificado** por cambios en la funcionalidad existente.
- **Obsoleto** para funciones que se eliminarán próximamente.
- **Removido** para funciones eliminadas.
- **Corregido** cualquier corrección de errores.
- **Seguridad** en caso de vulnerabilidades.

### [1.3.0] - 2020-06-05
#### Agregado
- Multiples mejoras.
- Nuevas dependecias.
- Funcionalidades de guardado y ubicación.

#### Modificado
- `Front-end` mejorado.
- Limpieza del código.

### [1.2.0] - 2020-06-05
#### Agregado
- Multiples mejoras.
- Nuevas dependecias.
- `Front-end` mejorado.
- `Back-end` mejorado.
- `Seeders`.
- `Api`.

#### Modificado
- Nuevos requerimientos agregados a `requirements.txt`.
- `app.py` vuelve a ser `applicacion.py`.

#### Removido
- Archivos sobrantes `.vscode` y `.gitkeep`.

#### Seguridad
- Removidos archivos `*.db` que no pueden ser compartidos en el repo.

### [1.1.0] - 2020-06-04
#### Agregado
- Modelado de los datos con `SQLAlchemy`
- Controladores para mostrar y guardar `Plotholes`
- Controladores agregados a `controllers/main.py`

#### Modificado
- Nuevos requerimientos agregados a `requirements.txt`.
- `applicacion.py` ahora es `app.py`.
- Cambios mínimos en el front-end con `Miligram`

### [1.0.1] - 2020-04-26
#### Modificado
- `requirements` agregados.

### [1.0.0] - 2020-04-04
#### Added
- Estructura del proyecto propuesta para ajustarse al patrón `MVC`.
```txt
  /
    /controllers    <- Controladores
    /database       <- Base de datos
    /models         <- Modelos / Clases
    /resources      <- Archivos sin compilar
    /static         <- Archivos compilados
    /templates      <- Vistas / Plantillas
  application.py    <- App principal
  webpack.mix.js    <- Compilador de archivos
```
- `Webpack` implementado usando `Laravel-mix` para compilar y mixear archivos.
- `Commit` inicial.
