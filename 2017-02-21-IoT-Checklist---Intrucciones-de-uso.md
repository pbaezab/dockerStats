---
title: IoT Checklist - Intrucciones de uso
layout: post
author: pbaeza
permalink: /iot-checklist---intrucciones-de-uso/
source-id: 1CiYM65qBav-wEJYuuboD3TsusYlrNDS0JV6zXz763MU
published: true
---
IoT Checklist

[pbaeza@tracktec.cl](mailto:pbaeza@tracktec.cl)

martes 21 de febrero 2017

# Instrucciones de uso

1. Ingreso

<table>
  <tr>
    <td></td>
    <td>1.1 Pantalla inicial que solo permite ingresar al sistema y mostrar la versión de IoT checklist.

Los usuarios son inicialmente cargados al sistema y se mantienen actualizados a partir del listados de conductores desde el mantenedor respectivo en "plataforma".
</td>
  </tr>
  <tr>
    <td>1.2 Al seleccionar “ingresar” aparece la pantalla de inicio de sesión para ingresar el nombre de usuario y contraseña.

Un usuario puede tener alguno de los siguientes roles:

Conductor, permite crear nuevos checklist a partir del camión y rampla que el mismo conductor seleccione en el sistema.

Controlador, permite aprobar la salida de un conductor previo ingreso de un checklist. 
</td>
    <td></td>
  </tr>
</table>


2. Selección camión

<table>
  <tr>
    <td></td>
    <td>2.1 Pantalla para la búsqueda de un camión, previamente desbloqueado por el conductor a través de huella.

Se permite la búsqueda del vehiculo por patente en formato AABB11 o por el código alfanumérico interno que maneje el cliente, ejemplo T001.</td>
  </tr>
  <tr>
    <td>2.2 Una vez ingresada la búsqueda se deberá presionar [enter] o sobre el botón [buscar] representado por una lupa. 

En caso de que el camión buscado exista y esté desbloqueado por el conductor con su huella, este será seleccionado para el checklist y se habilitará el botón para pasar a la pantalla siguiente.</td>
    <td></td>
  </tr>
</table>


3. Selección rampa (o no)

<table>
  <tr>
    <td></td>
    <td>3.1 Pantalla para la búsqueda de una rampa o también poder establecer el checklist sin rampa.

Se permite la búsqueda de la rampa por patente en formato AABB11 o por el código alfanumérico interno que maneje el cliente, ejemplo S001.</td>
  </tr>
  <tr>
    <td>3.2 Una vez ingresada la búsqueda se deberá presionar [enter] o sobre el botón [buscar] representado por una lupa. 

En caso de que la rampa buscada exista, esta será seleccionado para el checklist y se habilitará el botón para pasar a la pantalla siguiente.</td>
    <td></td>
  </tr>
</table>


4. Información de la salida

<table>
  <tr>
    <td></td>
    <td>Pantalla para poder complementar con información adicional al checklist.

Se puede seleccionar el motivo de la salida,

Viaje
Taller externo
Revisión técnica
Prueba de ruta

Finalmente se puede establecer si va con carga o sin carga para tener presente a la hora del control de salida.</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
  </tr>
</table>


5. Checklist manual

<table>
  <tr>
    <td></td>
    <td>5.1 Pantalla para poder complementar con el estado de cada uno de los ítems asociados al camión y rampa previamente seleccionados.

En la pantalla se separan los ítems del camión de los ítems de la rampa.

Los ítems son inicialmente cargados al sistema y pueden variar por cada cliente.</td>
  </tr>
  <tr>
    <td>5.2 El estado de cada ítem puede ser [Sí] o [No] y significa si este está en condiciones o fuera de condiciones para la salida y ejecución de un viaje posterior.








</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>
5.3 Todos los ítems deben ser seleccionados para poder desbloquear el botón [siguiente] y seguir avanzado.</td>
  </tr>
</table>


6. Checklist automático

<table>
  <tr>
    <td></td>
    <td>6.1 Pantalla para visualizar el estado de cada uno de los dispositivos asociados al camión y que transmiten en línea información al sistema.

La idea principal es poder detectar a tiempo y preventivamente que todos los dispositivos estén transmitiendo a la hora de llenar el checklist.

En caso de estar todo ok, el botón [siguiente] queda habilitado para continuar a la siguiente pantalla.</td>
  </tr>
  <tr>
    <td>6.1 En caso de existir algún dispositivo que no esté transmitiendo será identificado y el botón [siguiente] no estará habilitado.

Cada dispositivo tiene una ventana de tiempo por defecto para transmitir, 

En el caso del AVL, FMS y Temperatura es de 30 minutos.
En el caso del botón de pánico y huella es de 12 horas.

Cabe mencionar que solo basta una transmisión en estas ventanas para considerar que el dispositivo está OK.

Si el dispositivo nunca ha transmitido desde que se cargó el camión al sistema este considerará que el dispositivo no aplica y será omitido para el checklist.</td>
    <td></td>
  </tr>
</table>


7. Resumen del checklist

<table>
  <tr>
    <td></td>
    <td>Previamente antes de guardar el checklist se mostrará un resumen con los detalles más importantes asociados a este.</td>
  </tr>
</table>


8. Confirmación de guardado

<table>
  <tr>
    <td></td>
    <td>Para finalizar el guardado del checklist se mostrará una pantalla con un mensaje de confirmación indicando que todo está OK.

Además desplegará los últimos 3  checklist llenados por conductor.</td>
  </tr>
</table>


9. Aprobación de salida (solo usuario controlador)

<table>
  <tr>
    <td></td>
    <td>9.1 Pantalla para la búsqueda de un checklist, previamente llenado y activo

Se permite la búsqueda del checklist a través del RUT del conductor.

Se vuelve a mencionar que por defecto el checklist solo estará activo para su aprobación durante una ventana de tiempo de 12Hrs desde su creación.</td>
  </tr>
  <tr>
    <td>9.2 En caso de existir un checklist activo asociado al RUT ingresado, se desplegará un resumen de este.

Adicionalmente el controlador podrá aprobar la salida del conductor o mantener el estado como pendiente de salida.

En caso de mantener como pendiente la salida, el conductor podrá llenar un nuevo checklist asociado a otro camión y que será su nuevo checklist activo.</td>
    <td></td>
  </tr>
</table>


