## Act 2
### Configutación switch1:
- Hostname: **LOST1**
- Contraseña secreta: contra1
- Contraseña de consola: contracon 
- Contraseña de vty: contravty

### Configuración switch2:
- Hostname: **LOST2** 
- Contraseña secreta: contra2 
- Contraseña de consola: contracon 
-  Contraseña de vty: contravty

### IPs asignadas
<img src="media\lab4\IPs.png" width="600" />

### Switch 1
<img src="media\lab4\switch1.png" width= "600"/>

### Switch 2
<img src="media\lab4\switch2.png" width= "600"/>

### i)
<img src="media\lab4\apartado i).png" width= "600"/>


### m)
<img src="media\lab4\apartado m).png" width= "600"/>


### n)
**PC1 a PC2:**

<img src="media\lab4\ping pc1 a pc2.png" width= "600"/>


**sw2 a sw1:**
<img src="media\lab4\ping sw2 a sw1.png" width= "600"/>

#### Interpretación de los resultados: 
Ambos pings han fallado ya que la conexión entre los switches aún opera como puerto de acceso en la vLAN 1 por defecto. Al no haber un enlace Trunk configurado entre ambos switches con la encapsulación correspondiente(802.1Q), las tramas VLAN 10 (PC1/PC2) y VLAN 99 (Management) no pueden ir de un switch al otro