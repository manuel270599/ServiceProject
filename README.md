# Práctica Calificada N°4 
La estructura del proyecto se establece de la siguiente manera:

![image](https://github.com/user-attachments/assets/4c18ea72-d1c5-4181-b2c1-bf9f1f349f37)

## Herramientas:

El uso de todas las herramientas son necesarias para la funcionalidad del proyecto, consiste en la contenerizacion e interacción entre ellas.Las herramientas a usar son:

DevContainer: Nos va a ayudar en la interacción de servicios web a traves de flask.Nos permite crear un entorno aislado utilizando contenedores Docker.

Aquí definimos el nombre,la ruta del archivo en docker-compose y tambien definimos el servicio.

![image](https://github.com/user-attachments/assets/868c592a-e865-44d6-852f-5951f0c20dbe)

El dockerfile de manera general:

![image](https://github.com/user-attachments/assets/ccbde006-31a2-4a95-b6f7-229c0496cbde)

Docker Compose: Se hace uso de esta herramienta para la ejecución de múltiples contenedores Docker. Este evaluación involucra varios servicios (product_catalog/user_management).
Nos facilita la orquestación de estos contenedores, permitiendo que se conecten entre sí de manera sencilla.

![image](https://github.com/user-attachments/assets/c97cb660-dbce-44f6-8878-f775a66e6745)

## Explicación del código principal para ambos servicios
# Product_catalog:

-Importo Flask para crear una aplicación web y jsonify para devolver respuestas JSON esto es útil para intercambiar datos entre servicios.
-Inicializo la aplicación Flask.

![image](https://github.com/user-attachments/assets/1c829153-acf6-455c-8df5-e8d2fd2288a8)

Se define una ruta **/products** que responde a solicitudes **HTTP** de tipo **GET**.
Al accder a esta ruta se ejecuta la función get_products.

**get_products():** Devuelve una lista de productos, esto a fin de que cada producto es un diccionario con un id y nombre.

![image](https://github.com/user-attachments/assets/f9398a3c-30a3-419a-8f7d-71192d82ff06)

Por último el servidor flask se ejecuta desde cualquier ip en el puerto **5002**

![image](https://github.com/user-attachments/assets/7241c45b-b59c-435c-855b-cd4be4a28895)


## User_management:

-Importo **Flask** para crear el servidor web y la librería **requests** para realizar solicitudes HTTP a otros servicios.
-Inicializa **otra** aplicación Flask.

![image](https://github.com/user-attachments/assets/ac7d202c-dd00-40d2-9775-64de36c2bd6f)

-Se define la ruta /users, que responde a solicitudes GET.
-Se ejecuta la función get_users():Realiza una solicitud HTTP (GET) al servicio de productos (**http://product_catalog:5002/products**) utilizando requests.get
-Devuelve un mensaje indicando que el servicio funciona, junto con la lista de productos obtenida del servicio de productos caso contrario un error(HTTP 500)

![image](https://github.com/user-attachments/assets/a3160c06-ad39-44d1-a321-e0a394373fa9)

Elservidor Flask se ejecuta en el puerto 5001.

![image](https://github.com/user-attachments/assets/6b91d308-4d17-4ea3-9408-7a0e92081e29)


## Ejecución de los servicios

Creacion de los contenedores:

![image](https://github.com/user-attachments/assets/7dc911fd-faf7-4f5e-9f80-b6bb13a6c768)

Confirmamos si la ejecución fue correcta y vemos lo siguiente:

![image](https://github.com/user-attachments/assets/3367f005-b2da-4bd8-81f2-c4a7686b35c5)

Se creo el contenedor principal para ambos servicios y tambien ambos servicios contenerizados.Por tanto se logro la contenerización para cada servicio.

![image](https://github.com/user-attachments/assets/231c2fd7-38f0-41f2-b9d8-e700f2f07bb4)

verificamos cada puerto y vemos que efectivamente ambos servicios estan en comunicación:

![image](https://github.com/user-attachments/assets/7fe356e0-5ab3-45e5-9a1d-ebc619b86666)


![image](https://github.com/user-attachments/assets/2a755f33-e5ed-425c-9428-9629ea298ed9)


Tambien desde una terminal:

![image](https://github.com/user-attachments/assets/8259010d-188e-410f-b65e-4e1a7afad258)


## Pruebas

## Product_catalog:

-**test_client()** es un método que crea un cliente simulado para realizar solicitudes HTTP a 
la aplicación Flask probando las rutas de la API sin necesidad de un servidor en ejecución.

-**response = client.get('/products'):** Realiza una solicitud GET a la ruta **/products** de la aplicación Flask. **response** contendrá la respuesta del servidor

-**self.assertEqual(response.status_code, 200)**: La función assertEqual compara el primer argumento con el segundo. Si los valores no son iguales, la prueba falla.

![image](https://github.com/user-attachments/assets/5d1c971b-1d56-4d25-8404-081f1d6eb2a5)

##

Ejecución:

![image](https://github.com/user-attachments/assets/4255bb7e-ac84-4de7-8d7b-1636e9011024)

![image](https://github.com/user-attachments/assets/ffbbc72d-d2df-482a-8c05-9e897065614b)



## User_management:

-**test_client():** Crea un cliente simulado para realizar solicitudes **HTTP** a la aplicación Flask sin necesidad de un servidor real.
-**response = client.get('/users'):** Realiza una solicitud HTTP de tipo **GET** a la ruta **/users.** Esta ruta es la que se quiere probar.
-**self.assertEqual(response.status_code, 500):** Este es un método de afirmación que verifica si el código de estado de la respuesta (response.status_code) es igual a 500.

            -Si el código de estado es 500, la prueba pasará.
            
            -Si el código de estado es diferente a 500, la prueba fallará.

            
  ![image](https://github.com/user-attachments/assets/dc34a8ee-0798-4002-a501-0a91374c32ba)

Ejecución:

![image](https://github.com/user-attachments/assets/805d5e10-306c-4b63-b87a-591aad2e82a1)

![image](https://github.com/user-attachments/assets/00f5ad94-b75c-47b8-91d1-af47ddde9d64)













