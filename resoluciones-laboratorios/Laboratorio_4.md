
1) Alcance de Redes y Virtualización 
a) Investigar cómo se clasifican las redes según su alcance. Mencionar brevemente las características principales de cada una y colocar en cada cuadro de la Figura el acrónimo de red que corresponda. 
b) ¿Qué es una vLAN? ¿Cómo se clasifican?
c) Investigar y resumir el protocolo IEEE 802.1Q. ¿Cómo se relaciona con las VLAN?
d) En el contexto de los dos ítems anteriores ¿Qué es el Tagging? 

1a) Según su alcance, podemos clasificar las redes de la siguiente manera:
- Red de Área Personal (PAN): Es una red de muy corto alcance. Por ejemplo al conectar el celular  a los auriculares por Bluetooh.
- Red de Área Local (LAN): Es la red de ámbito local. Son rápidas y de muy baja latencia.
- Red de Área Metropolitana (MAN): Cobertura a nivel de una ciudad o municipio. Es la infraestructura que utilizan los proveedores para interconectar varias LANs repartidas en distintos barrios.
- Red de Areas Extensa (WAN): Abarca países, continentes o el mundo entero. Usa enlaces de larga distancia y routers de alto rendimiento.  

1b) Una VLAN (Virtual Local Área Network) es una subred lógica que permite dividir un switch físico en varios switches independientes por software. Sirve para agrupar las computadoras por área o función en lugar de su ubicación física. Esto permite que el trafico de cada grupo quede aislado para mejorar su seguridad y el rendimiento de la red. Se clasifican teniendo en cuenta:
- Puertos
- Datos
- Gestion
- Voz
- Nativa
- Dinamicas

1c) La relación del protocolo IEEE 802.1Q pasa por el hecho de que Ethernet estándar no distingue a que VLAN pertenece una trama. Para solucionar esto entra el protocolo, que le asigna una etiqueta digital de 4 bytes donde va anotado el numero de VLAN. El switch interpreta esa etiqueta y se la entrega a la PC correspondiente
