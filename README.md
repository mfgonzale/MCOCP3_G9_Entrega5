# MCOCP3_G9_Entrega5

# MCOC2020-P3
  
# Informe Entrega 5 sobre replicación de tesis de Contreras usando diferencias finitas 

# Introducción.
Los hormigones masivos se caracterizan por ser hormigones de gran volumen y se pueden encontrar en casi todas las obras construidas. Un factor de interés en este proyecto es la generación de calor que produce la hidratación del cemento, llegando a tener en el hormigón masivo distintos valores de temperaturas en el tiempo, los cuales pueden llegar a durar días incluso. En este caso la difusión de calor se tomará de manera bidireccional (en 2-D) y se sigue difundiendo de forma simétrica, por lo que se toman tres nodos dentro del molde, los cuales son P1(a/2,b/2), P2(a/2,3b/4) y P3(3a/4,3b/4). Para estimar los valores de temperatura en el tiempo se simulará la difusión térmica usando diferencias finitas. Luego se busca realizar la discretización de las condiciones de borde naturales.

El este proyecto se evaluaran 7 casos distintos

# Resultados.

 Al plantear un código que imprimiera gráficos para distintas condiciones de temperatura y gradiente en tres posiciones y en distintos intervalos de tiempo, los cuales son en los tiempos 0h, 2h, 6h, 12h, 24h se obtienen los siguientes gráficos y gif representando los cambios de temperatura para cada caso:
 
 Caso 1:
 
 Condiciones de borde:  
  
*20° Inicial  
*Borde Superior: 0°  
*Borde Izquierdo: 20°  
*Borde Inferior: 20°  
*Borde Derecho: 0°  

 ![imagen](/Grafico_Caso1.png)
 

![imagen](/2D_ej04_frame_Caso_1.gif)
  
  
Caso 2:
 
 Condiciones de borde:  
  
*20° Inicial  
*Borde Superior: 0°  
*Borde Izquierdo: 20°  
*Borde Inferior: 20°  
*Borde Derecho: Gradiente 0  
 
 ![imagen](/Grafico_Caso2.png)
 

![imagen](/2D_ej04_frame_Caso_2.gif)


Caso 3:
 
 Condiciones de borde:  
  
*10° Inicial  
*Borde Superior: 0°  
*Borde Izquierdo: 20°  
*Borde Inferior: 20°  
*Borde Derecho: 20°  
 
 ![imagen](/Grafico_Caso3.png)
 

![imagen](/2D_ej04_frame_Caso_3.gif)


Caso 4:

Condiciones de borde:  
  
*10° Inicial  
*Borde Superior: 0°  
*Borde Izquierdo: 20°  
*Borde Inferior: 20°  
*Borde Derecho: Gradiente 0  

 ![imagen](/Grafico_Caso4.png)
 

![imagen](/2D_ej04_frame_Caso_4.gif)


Caso 5:
 
 Condiciones de borde:  
  
*5° Inicial  
*Borde Superior: Gradiente 0  
*Borde Izquierdo: 25°  
*Borde Inferior: Gradiente 0  
*Borde Derecho: 25°  
 
 ![imagen](/Grafico_Caso5.png)
 

![imagen](/2D_ej04_frame_Caso_5.gif)


Caso 6:
 
 Condiciones de borde:  
  
*30° Inicial  
*Borde Superior: Gradiente 0  
*Borde Izquierdo: 10°  
*Borde Inferior: Gradiente 0  
*Borde Derecho: Gradiente 0  
 
 ![imagen](/Grafico_Caso6.png)
 

![imagen](/2D_ej04_frame_Caso_6.gif)


Caso 7:

Condiciones de borde:  
  
*20° Inicial  
*Borde Superior: Temperatura ambiental (sinusoide con variación de 10°, período de 1 día)  
*Borde Izquierdo: Gradiente 0  
*Borde Inferior: Gradiente 0  
*Borde Derecho: Gradiente 0  
  
 
 ![imagen](/Grafico_Caso7.png)
 

![imagen](/2D_ej04_frame_Caso_7.gif)


# Conclusión

