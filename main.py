import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Función para obtener tasas de cambio
def get_exchange_rate(base_currency, target_currency):
    API_KEY = "TU_API_KEY"  # Reemplaza con tu clave de ExchangeRate-API
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"
    
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return data["conversion_rates"].get(target_currency, None)
        else:
            messagebox.showerror("Error", f"Error en la API: {data['error-type']}")
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "No se pudo conectar con la API.")
        return None

# Función para convertir moneda
def convert_currency():
    try:
        amount = float(entry_amount.get())
        base_currency = combo_base.get()
        target_currency = combo_target.get()
        rate = get_exchange_rate(base_currency, target_currency)
        
        if rate:
            converted_amount = round(amount * rate, 2)
            label_result.config(text=f"{amount} {base_currency} = {converted_amount} {target_currency}")
        else:
            messagebox.showerror("Error", "No se pudo obtener la tasa de cambio.")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un monto válido.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Conversor de Monedas")
root.geometry("400x300")
root.configure(bg="#1E1E2E")

frame = tk.Frame(root, bg="#282A36", padx=20, pady=20)
frame.pack(pady=20)

tk.Label(frame, text="Monto:", bg="#282A36", fg="white").pack()
entry_amount = tk.Entry(frame)
entry_amount.pack(pady=5)

tk.Label(frame, text="Moneda Base:", bg="#282A36", fg="white").pack()
combo_base = ttk.Combobox(frame, values=["USD", "EUR", "GBP", "JPY", "MXN", "ARS", "BRL", "CLP"])
combo_base.pack(pady=5)
combo_base.set("USD")

tk.Label(frame, text="Moneda Destino:", bg="#282A36", fg="white").pack()
combo_target = ttk.Combobox(frame, values=["USD", "EUR", "GBP", "JPY", "MXN", "ARS", "BRL", "CLP"])
combo_target.pack(pady=5)
combo_target.set("EUR")

tk.Button(frame, text="Convertir", command=convert_currency, bg="#50FA7B", fg="black").pack(pady=10)
label_result = tk.Label(frame, text="", bg="#282A36", fg="white", font=("Arial", 12))
label_result.pack()

root.mainloop()
