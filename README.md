# Company location

El objetivo de este proyecto es localizar el lugar adecado para colocar una empresas segun ciertos parametros.

El proceso que seguimos es el siguente:

- Partiendo de una colección de mongo que contien una serie d empresas se toman aquellas relacionadas con nuestro campo de trabajo. Nos quedamos con las ciudades con alta concentración de empresas del sector. 
Finalmente se obtiene un conjunto de ciudades a valorar.

- Algunos de los parámtros de analisis incluyen gutos y necesidades de los empleados. Me deiante la api de Google se recopila información de locales de interes en las ciudades elegidas.\
También se ha incluido información de aeropuertos.


- Para obtener el punto mas adecuado se genera una malla en cada ciudad y se valora cada punto de esta malla.\
Final mente se toman los puntos con mejor rating. Para desempatar se ha tomada el criterio mas solicitado por los empleados. La cercanía a Madrid.


En la carpeta de Outputs se genera un html que muestra un mapa de la ciudad elegida y la valoración de cada punto en dicha ciudad.
El punto final se marca en la imagen con un _tick_

Los paramentros de busqueda en goolge y de calificación pueden modificarse en el fichero constants.py.


 



