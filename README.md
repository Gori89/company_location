# Company location

El objetivo de este proyecto es localizar el lugar adecuado para colocar una empresa según ciertos parámetros.

El proceso que seguimos es el siguiente:

- Partiendo de una colección de mongo que contiene una serie d empresas se toman aquellas relacionadas con nuestro campo de trabajo. Nos quedamos con las ciudades con alta concentración de empresas del sector. 
Finalmente se obtiene un conjunto de ciudades a valorar.

- Algunos de los parámetros de análisis incluyen gustos y necesidades de los empleados. Mediante la api de Google se recopila información de locales de interés en las ciudades elegidas.\
También se ha incluido información de aeropuertos.


- Para obtener el punto más adecuado se genera una malla en cada ciudad y se valora cada punto de esta malla.\
Finalmente se toman los puntos con mejor rating. Para desempatar se ha tomada el criterio más solicitado por los empleados. La cercanía a Madrid.


En la carpeta de Outputs se genera un html que muestra un mapa de la ciudad elegida y la valoración de cada punto en dicha ciudad.
El punto final se marca en la imagen con un _tick_

Los parámetros de búsqueda en Goolge y de calificación pueden modificarse en el fichero constants.py.


 



