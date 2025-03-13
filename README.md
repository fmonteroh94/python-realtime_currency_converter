# 💱 Conversor de Monedas

## 📌 Descripción

Esta es una aplicación de escritorio desarrollada en Python con una interfaz gráfica basada en Tkinter. Permite convertir valores entre diferentes monedas en tiempo real utilizando la API gratuita ExchangeRate-API.

Se pueden añadir más divisas al proyecto al agregar su código a los Combobox, siempre y cuando sean compatibles con la API que recibe estos parámetros.

## ✨ Características

✅ Conversión en tiempo real de múltiples monedas.

✅ Interfaz gráfica moderna e intuitiva con Tkinter.

✅ Muestra la tasa de conversión actual entre las monedas seleccionadas.

✅ Soporta múltiples monedas, incluyendo:

- 🇺🇸 USD (Dólar estadounidense)

- 🇪🇺 EUR (Euro)

- 🇬🇧 GBP (Libra esterlina)

- 🇯🇵 JPY (Yen japonés)

- 🇲🇽 MXN (Peso mexicano)

- 🇦🇷 ARS (Peso argentino)

- 🇧🇷 BRL (Real brasileño)

- 🇨🇱 CLP (Peso chileno)

✅ Uso de una API gratuita para obtener tasas de cambio actualizadas.

## 🛠 Requisitos

Asegúrate de tener instalado Python 3.x y las siguientes bibliotecas antes de ejecutar la aplicación:

```sh
pip install requests
```

Además, debes obtener una clave de API gratuita desde [ExchangeRate-API](https://www.exchangerate-api.com/) e insertarla en el código donde se indica (Línea 7).

Para obtener la clave solo es necesario registrarse al plan gratuito con un correo válido.

## 🚀 Uso

🔹 Ejecutar la aplicación
```sh
python main.py
```

🔹 Pasos para convertir una moneda

1. Ingresa el monto a convertir en el campo correspondiente.

2. Selecciona la moneda de origen en el primer desplegable.

3. Selecciona la moneda de destino en el segundo desplegable.

4. Haz clic en "Convertir".

5. Se mostrará el monto convertido junto con la tasa de conversión actual.

## 📸 Capturas de Pantalla

![image](https://github.com/user-attachments/assets/3ed57f8a-674b-47d6-a4d2-dd4848397362)

![image](https://github.com/user-attachments/assets/56124bb1-a3fc-4505-b18d-ae33e49e8993)

## 🤝 Contribuciones

Si deseas mejorar esta aplicación, ¡las contribuciones son bienvenidas! Puedes hacer un fork del repositorio y enviar un pull request con tus mejoras.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo libremente con fines personales y comerciales.

### 💻 Desarrollado por Felipe Montero H.
