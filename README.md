# Mitigación de la Contaminación Bentónica en Acuicultura con Inteligencia Artificial y Nanoburbujas

![plantacion-salmonera](https://github.com/user-attachments/assets/871f20c2-e7b4-40e0-b36f-69bd428be76a)

## Problemática 

La intensiva acuicultura del salmón en el sur de la Patagonia genera acumulación de desechos orgánicos en el fondo marino, creando zonas anóxicas caracterizadas por la formación de alfombras bacterianas blancas. 
La presencia de alfombras bacterianas blancas en los fondos marinos es un indicador clave y reconocido del impacto ambiental de la industria salmonera intensiva.
Esta acumulación masiva de desechos orgánicos (alimento no consumido y fecas) provenientes de las jaulas de cultivo genera condiciones de eutrofización (exceso de nutrientes) en los sedimentos del fondo.

![fondo-salmonera](https://github.com/user-attachments/assets/9e826588-ab69-436e-a87b-c8c6e14e885f) 
![fondo-salmonera2](https://github.com/user-attachments/assets/5ee2b070-e0ce-4c22-9e97-be40f540393d)

---

## Impacto en el Ecosistema:

- **Anoxia/Hipoxia:** La descomposición de esta materia orgánica consume grandes cantidades de oxígeno, creando zonas con niveles muy bajos o nulos de oxígeno (anóxicas), donde solo pueden sobrevivir bacterias especializadas, como las que forman las alfombras blancas.
- **Pérdida de Biodiversidad:** Esto desplaza o elimina a la fauna bentónica nativa, que no puede sobrevivir en estas condiciones, alterando gravemente el ecosistema local.
- **Resistencia a Antibióticos:** El uso extensivo de antibióticos en la salmonicultura chilena (mucho mayor que en otros países productores) contribuye a la propagación de bacterias resistentes a los antibióticos en el medio marino, lo que representa un riesgo para la salud pública y el medio ambiente. 

---

## Respuesta Científica y Social

La ciencia y las organizaciones ambientales chilenas han estudiado y denunciado repetidamente esta situación, destacando la necesidad de una regulación y fiscalización más estrictas, así como la reubicación de centros de cultivo fuera de áreas protegidas para preservar los ecosistemas prístinos de la Patagonia. Gracias a los avances tecnológicos, hoy existen muchas empresas que por intermedio de distintas tecnologías, trabajan arduamente a diario esta problemática...

---

## Implementar los avances tecnológicos como solución innovadora

Este proyecto aborda esta problemática en dos frentes clave:
Detección Inteligente (IA & Python)
Presentamos una aplicación desarrollada en Python que utiliza algoritmos de Inteligencia Artificial (específicamente visión por computadora) para detectar, mapear y monitorear automáticamente estas formaciones bacterianas a partir de datos visuales submarinos. Esto permite una identificación precisa y en tiempo real del impacto ambiental, que en conjunto a otras tecnologías, se puede mapear las zonas con que presentan estas problemáticas y enfocar los esfuerzos para mitigarlas según su densidad.

---

## Integración de la Inteligencia Artificial

El enfoque o mejor dicho, la consideración de tener en cuenta los últimos avances tecnologicos sobre vision artificial e inteligencia artificales, son excelentes herramientas para trabajar esta problematica, ya que la IA puede automatizar y mejorar significativamente la identificación de las alfombras bacterianas, que son un indicador de contaminación.

- **Detección Automatizada:** Una aplicación de Python que utiliza visión por computadora o aprendizaje automático (machine learning) puede analizar imágenes (como la que proporcionaste) o datos de sensores submarinos para identificar de manera rápida y precisa la presencia y extensión de estas formaciones bacterianas.

- **Monitoreo Continuo:** Esto permite un monitoreo continuo y menos dependiente de la inspección manual, facilitando una respuesta oportuna antes de que la contaminación se agrave.

Una captura del microorganismo:

![ejemploBASE](https://github.com/user-attachments/assets/14b8dbcd-4dfb-408e-aac7-30e2915ff57c)

Y una captura post procesamiento con IA:

<img width="1365" height="614" alt="reconocimientoBASE" src="https://github.com/user-attachments/assets/b6a62700-b563-413a-bce1-ea73b0d12740" />

---

# La version DEMO de nuestra aplicacion de reconocimiento con vision artificial e inteligencia artificial... 

## ¿Qué es este programa?

Este programa es una herramienta de monitoreo visual que permite analizar imágenes, videos o cámaras en vivo para detectar automáticamente zonas de lodo, 
mantos orgánicos o presencia biológica (como peces o formaciones blanquecinas) en ambientes acuáticos.
Su objetivo es convertir imágenes y videos en información medible, útil para estudios ambientales, acuicultura o monitoreo científico.

**¿Qué puede analizar?**

El sistema es flexible y puede trabajar de tres maneras:

📷 Cámara en vivo (por ejemplo, una cámara submarina o de superficie).

🎥 Videos grabados (MP4, AVI).

🖼️ Imágenes estáticas (fotos JPG o PNG).

Esto permite usar tanto material nuevo como registros históricos. 

**¿Cómo funciona, explicado de forma simple?**

- El programa “mira” las imágenes de forma similar a una persona entrenada:

- Observa cada imagen o cuadro de video.

- Busca patrones visuales asociados a lodo, mantos o presencia biológica.

- Marca automáticamente las zonas detectadas con recuadros visibles.

- Calcula cuánto espacio ocupan esas zonas dentro de la imagen.

- Guarda los resultados en un registro para análisis posterior.

- Todo esto ocurre de forma automática y en tiempo real si se usa una cámara.

**¿Qué información genera?**

Además de mostrar el resultado en pantalla, el sistema:

- Calcula el porcentaje de cobertura del lodo o manto detectado.

Registra:

- Fecha y hora

- Tamaño total de la imagen

- Área detectada

- Porcentaje de cobertura

- Guarda todo en un archivo de registro (planilla) que luego puede abrirse con Excel u otros programas similares.

- Esto permite comparar datos en el tiempo y hacer seguimiento de cambios.

**¿Y si el sistema no detecta algo importante?**

El programa incluye una función clave para ciencia real:

👉 Etiquetado manual

-Si el sistema no reconoce una zona relevante:

-El operador puede dibujar un rectángulo sobre la imagen.

-Esa información se guarda como ejemplo.

-Esos ejemplos pueden usarse luego para mejorar el sistema.

-Esto combina automatización con criterio humano, algo fundamental en estudios ambientales.

**¿Qué tan compleja es la tecnología?**

- Aunque el resultado es avanzado, la base es accesible:

- Funciona en una computadora común.

- Usa cámaras estándar.

- No necesita internet.

- Se apoya en herramientas de uso científico ampliamente difundidas.

- Puede ser operado por personas sin conocimientos de programación.

- La interfaz es visual y sencilla: botones, ventanas y mensajes claros.

**¿Para qué tipo de trabajos sirve?**

Este sistema puede usarse en:

- Monitoreo ambiental y marino.

- Acuicultura y control de fondos.

- Estudios de impacto ambiental.

- Análisis de material submarino.

- Seguimiento de zonas con acumulación orgánica.

- Apoyo a campañas científicas y relevamientos visuales.

**NOTA:** _Este programa demuestra que con herramientas relativamente simples se puede hacer análisis serio de imágenes y videos científicos.
No reemplaza al especialista, pero lo asiste, acelera el trabajo y transforma imágenes en datos objetivos... Esta version DEMO no cuenta con 
el nuevo dataset y modelo nuevo que generamos, entre otras caracteristicas funcionales que sumamos en la version profesional._

---

## Mitigación con Nanotecnología (Nanoburbujas)

En paralelo, mostramos el potencial de un generador de nanoburbujas desarrollado por ETI Patagonia y que fue mostrado publicamente en la planta de tratamiento de efluentes cloacales (PTEC). 
Las nanoburbujas de oxígeno tienen la capacidad de saturar eficientemente el agua y los sedimentos con oxígeno, mitigando las condiciones anóxicas y revirtiendo la proliferación bacteriana en la zona afectada.
Este proyecto demuestra cómo la tecnología avanzada puede ser una herramienta poderosa para la sostenibilidad de la industria acuícola en la Patagonia chilena."

![Prueba_BETA_PTEC_21](https://github.com/user-attachments/assets/e059e4d5-9d6f-4fb2-9b4b-ff5cb3873dfb)

![Prueba_BETA_PTEC_24](https://github.com/user-attachments/assets/7918c595-1ae2-4c22-842f-f724f2ba4ecd)

![Prueba_BETA_PTEC_22](https://github.com/user-attachments/assets/08123b6a-9b5e-4545-99b6-8fdacd20a55e)


_Por razones de derechos de autoria, nos reservamos mostrar nuestro diseño modular del generador e inyector de NB_

---

## Detalles Técnicos del Generador de Nanoburbujas

### 1. Principio de Funcionamiento

La mayoría de los generadores de nanoburbujas utilizan métodos físicos para forzar la formación de burbujas extremadamente pequeñas. Los métodos comunes incluyen la cavitación hidrodinámica o la disolución a presión, seguidas de una descompresión repentina. 

**Disolución a Presión:** El gas (oxígeno, en este caso) se disuelve en agua bajo alta presión, alcanzando un estado de sobresaturación. Al liberar esta mezcla a presión atmosférica a través de una boquilla o un punto de cizallamiento (shear point) especialmente diseñado, el gas se ve forzado a salir de la solución en forma de innumerables nanoburbujas.

**Cavitación Hidrodinámica:** El agua y el gas se fuerzan a través de una constricción (como una válvula venturi o placas de cavitación), creando cambios rápidos de presión y velocidad del flujo. Estos cambios forman microcavidades que colapsan violentamente, dividiendo el gas en partículas a escala nanométrica. 

---

### 2. Propiedades Clave de las Nanoburbujas

El potencial de mitigación radica en las propiedades únicas de estas burbujas:

_**Tamaño y Estabilidad:**_ Tienen un diámetro promedio de menos de 200 nanómetros (nm), lo que las hace invisibles a simple vista. A diferencia de las burbujas normales que suben y estallan rápidamente, las nanoburbujas son casi neutramente boyantes y permanecen suspendidas en el agua durante semanas o meses, moviéndose por movimiento browniano.

_**Distribución Homogénea de Oxígeno:**_ Su estabilidad y movimiento aseguran que el oxígeno se distribuya de manera uniforme en toda la columna de agua, desde la superficie hasta el fondo, donde se encuentran las alfombras bacterianas.

_**Carga Superficial:**_ Tienen una carga negativa en su superficie, lo que evita que se fusionen (coalescencia) y les permite adherirse a contaminantes y biofilm, ayudando en su eliminación.

_**Alta Eficiencia de Transferencia de Gas:**_ El área de superficie por volumen de las nanoburbujas es exponencialmente mayor que la de las burbujas tradicionales, lo que resulta en una eficiencia de transferencia de oxígeno de más del 85%, mucho mayor que los métodos de aireación convencionales. 

### 3. Rol en la Mitigación de la Problemática Patagonica

_**Al inyectar nanoburbujas de oxígeno en los sedimentos enriquecidos:**_

Se aumentan los niveles de oxígeno disuelto en el fondo, combatiendo las condiciones anóxicas.
Esto ayuda a degradar la materia orgánica acumulada y a suprimir las bacterias dañinas que forman las alfombras, restaurando el equilibrio del ecosistema bentónico.

---

# SOFTWARE/APP de calculo de Inyeccion

<img width="1326" height="643" alt="capturaAppINYECCION" src="https://github.com/user-attachments/assets/94ce2801-e07a-4cce-b290-ad2d47bdf42e" />


## Antes que nada: ¿por qué nanoburbujas?

La inyección de nanoburbujas de oxígeno es una herramienta muy potente para mejorar fondos marinos degradados, pero no es mágica.

**Lo bueno:**

- El oxígeno llega mejor al sedimento.

- Dura más tiempo disuelto en el agua.

- Puede ayudar a recuperar zonas con bajo oxígeno.

- Reduce malos olores y procesos anaeróbicos.

**Pero también tiene contras importantes, y acá está el punto clave:**

❌ Si se inyecta poco oxígeno, el fondo no mejora.

❌ Si se inyecta demasiado, se desperdicia energía y equipos.

❌ Cada lugar es distinto: no sirve una receta única.

❌ Las corrientes pueden llevarse el oxígeno antes de que llegue al fondo.

❌ La profundidad cambia completamente el comportamiento del sistema.

❌ Sin cálculo, es fácil invertir mucho dinero sin resultados claros.

Por eso, el problema no es la tecnología, sino cómo se usa.

**¿Por qué se buscó una solución a nivel software?**

Justamente porque en muchos casos la inyección de nanoburbujas se aplica:

- “por experiencia”

- copiando valores de otro centro

- o sobredimensionando “por las dudas”

Eso genera costos altos y resultados difíciles de justificar...

Este programa nace para responder una pregunta simple pero crítica:

 ### 👉¿Cuánto oxígeno hace falta realmente en este lugar y en estas condiciones?

**_¿Qué hace este programa?_**

Este programa permite calcular de forma simple cuánta inyección de nanoburbujas necesita el fondo marino debajo de una jaula de cultivo, considerando:

- Tamaño de la jaula

- Profundidad

- Tipo de ambiente (mar abierto o estuario)

- Corrientes

- Demanda real del sedimento

- Pérdidas y eficiencia del sistema

- Todo eso se traduce en números concretos, fáciles de entender.

**¿Qué problema resuelve?**

_Evita dos errores muy comunes:_

❌ Sistemas que no alcanzan y no remedian

❌ Sistemas sobredimensionados que encarecen la operación

_El programa apunta al equilibrio, donde la biorremediación es:_

- efectiva

- medible

- justificable técnica y económicamente

_¿Qué entrega como resultado?_

- Cuánto oxígeno se necesita por día

- Cuánto oxígeno hay que inyectar por hora

- Qué tipo de equipo es el más adecuado para ese escenario

En pocas palabras: _**"Una base objetiva para tomar decisiones"**_



“Las nanoburbujas funcionan, pero solo cuando se usan en la cantidad correcta.
Este programa existe para pasar de la prueba y error a decisiones basadas en datos.”

### Desarrollado por:
prof.martintorres@educ.ar

