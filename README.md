# Proyecto Web Scraping para Factoría F5

En este tercer proyecto de **Factoría F5**, se me pidió realizar un **web scraping** de una página web de mi elección. He decidido hacer scraping en **InfoJobs** para obtener las ofertas de trabajo disponibles según una palabra clave de búsqueda.

### Descripción

El objetivo del proyecto es crear un scraper que recoja las ofertas de trabajo de InfoJobs según un término ingresado por el usuario en un frontend. Los datos clave que se extraen son:

🔹 **Datos clave a obtener**:
- Nombre de la oferta
- Empresa que lo sube
- URL de InfoJobs de la empresa
- Ciudad
- Modalidad
- Salario
- Tipo de contrato
- Tipo de jornada

### Problemas encontrados y soluciones

‼️ **Problemas encontrados**:
1. **Problema con el número de ofertas**: Inicialmente, el scraper solo traía las primeras 5 ofertas, aunque la página mostraba 23. La solución fue calcular la altura del contenedor de una oferta de trabajo y realizar un scroll lento usando esa altura multiplicada por 4 (la cantidad que se ve por defecto por pantalla).
   
2. **Detección de automatización**: Al usar Mozilla Firefox, InfoJobs detectó que estaba utilizando Selenium, por lo que decidí cambiar a Chrome con las dependencias `user_agent` y `undetected_chromedriver` para evitar la detección.

3. **Modal de cookies**: El script se detenía si no aceptaba el modal de cookies manualmente. Gracias a una compañera, entendí que también podía automatizar ese 'click' para aceptar las cookies.

4. **Dockerización**: Al intentar dockerizar el proyecto con Chrome, encontré algunos errores. Por eso, opté por dockerizar la versión con Firefox utilizando el argumento `--headless`, pero debido a que InfoJobs detecta el scraping en Firefox, mi imagen no puede realizar búsquedas, solo muestra el historial de búsquedas anteriores en caso de que exista.

### Próximas mejoras

- Actualmente no puedo obtener la página web de la empresa, solo la URL de InfoJobs. Mi plan es crear una nueva tabla que conecte con el ID de la empresa, extraer la URL de su LinkedIn mediante otro **view** nuevo, y así obtener su página web para luego mostrarla en el frontend en formato HTML.
- Añadir filtros en la página offers, para que el usuario pueda filtrar por salario, por ciudad, etc.
- Añadir gráfico que muestre una media de salarios.

> **Nota**:  
> Tuve un pequeño problema con Github, ya que dentro de mi repositorio local creé sin querer otro repositorio, lo que me generaba conflictos a la hora de hacer commits. Finalmente, pude borrar y desvincular el repositorio local y creé una nueva rama `feature/scraping-v2` para continuar trabajando.

### URLs disponibles

- **Búsqueda**: [http://127.0.0.1:8000/search](http://127.0.0.1:8000/search) - Realiza una búsqueda con el término que desees.
- **Ofertas**: [http://127.0.0.1:8000/offers](http://127.0.0.1:8000/offers) - Muestra las ofertas de trabajo relacionadas con tu búsqueda o todas las búsquedas realizadas (disponibles en la base de datos).
- **Error**: [http://127.0.0.1:8000/error](http://127.0.0.1:8000/error) - Página de error cuando algo no sale bien.

### Comandos para ejecutar tests unitarios

Para ejecutar los tests unitarios, usa los siguientes comandos:

```bash
python manage.py test scraper.tests.test_models --keepdb
python manage.py test scraper.tests.test_views --keepdb
```


Se usa ``--keepdb``para que cada vez que corremos los test no cree una nueva base de datos y así no dar errores.


### Diagrama de actividad

![Diagrama de actividad del proyecto](./images/Activity-Diagram-Web-Scraper.png)

### Demo del proyecto

Demo here...

### Usar mi imagen desde Docker Hub

Para poder ejecutar este proyecto mediante Docker, sigue estos pasos:

- Asegúrate de tener instalado **Docker** en tu máquina. Si no lo tienes, puedes descargarlo e instalarlo desde [aquí](https://www.docker.com/get-started).

- Además, abre **Docker Desktop** y asegúrate de que Docker esté en ejecución.

#### Descargar la imagen de Docker
Para descargar la imagen del proyecto desde Docker Hub, abre tu terminal y ejecuta el siguiente comando:

```bash
docker pull allaharuty/scraper:latest
```

#### Ejecutar el contenedor:
Una vez descargada la imagen, puedes ejecutar el contenedor con el siguiente comando:

```bash
docker run -d --name scraper allaharuty/scraper:latest
```

#### Verificar el funcionamiento:
Para comprobar que el contenedor se está ejecutando correctamente, puedes ver los logs con el siguiente comando:
```bash
docker logs scraper
```

#### Detener después de usar:
Cuando hayas terminado de usarlo, puedes detener el contenedor con:
```bash
docker stop scraper
```

#### Eliminar después de detener:
Y si deseas eliminar el contenedor después de detenerlo, ejecuta:
```bash
docker rm scraper
```
