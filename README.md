# PROYECTO WEB SCRAPING PARA FACTORIA F5

### En este tercer proyecto de Factoria F5, se me pide que realice un web scraping de una página web de mi gusto.

He decidido hacer scraping la página de Infojobs para ver las ofertas de trabajo disponibles según la palabra buscada.

El objetivo es tener un frontend donde podamos ingresar la palabra que queramos y que el scraper haga su trabajo y nos traiga todas las ofertas disponibles.

🔹 Datos clave a obtener:<br>
✅ Nombre de la oferta<br>
✅ Empresa que lo sube<br>
✅ Url de Infojobs de la empresa<br>
✅ Ciudad<br>
✅ Modalidad<br>
✅ Salario<br>
✅ Tipo de contrato<br>
✅ Tipo de jornada<br>

‼️ Problemas con los que me he encontrado:
- Al entrar a scrapear, sólo me traía las primeras 5 ofertas que aparecía en la página, pero yo veía que en realidad había 23. La solución fue medir el alto del contenedor de 1 oferta de trabajo, y hacer scroll lentamente usando ese heigh multiplicado por 4.
- Cuando empecé a escribir el código, opté por usar Mozila Firefox, pero Infojobs enseguida se dio cuenta que estaba usando una automatización con selenium, así que decidí usar Chrome con las dependencias user_agent y undetected_chromedriver.
- Cada vez que el scraping empezaba, me saltaba el modal de la politica de cookies, y esperaba a ser aceptado manualmente, si no lo aceptaba el script se detenía con error. Gracias a una compaeñera, entendí que ese 'click' también podría automatizar. 

TODO: No puedo traer la pagina web de la empresa, solo la url de Infojobs. Crear una nueva tabla que conecte con el id de la empresa, entrar a su url de linkedin mediante otro view nuevo, extraer la página web para luego poder mostrarlo en html.

