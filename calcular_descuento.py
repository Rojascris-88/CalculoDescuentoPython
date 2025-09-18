def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento a partir del monto total y un porcentaje dado.
    :param monto_total: (float) Monto total de la compra
    :param porcentaje_descuento: (float) Porcentaje de descuento (por defecto 10)
    :return: (float) Monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

if __name__ == "__main__":
    # Primera: solo monto total (usa 10% por defecto)
    monto1 = 100.0
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1
    print(f"Valor de la compra: ${monto1} - Descuento: ${descuento1} - Total a pagar: ${total1}")

    # Segunda: monto total y descuento
    monto2 = 200.0
    descuento2 = calcular_descuento(monto2, 20)
    total2 = monto2 - descuento2
    print(f"Valor de la compra: ${monto2} - Descuento: ${descuento2} - Total a pagar: ${total2}")

  # tercera: monto total y descuento
    monto3 = 400.0
    descuento3 = calcular_descuento(monto3, 30)
    total3 = monto3 - descuento3
    print(f"Valor de la compra: ${monto3} - Descuento: ${descuento3} - Total a pagar: ${total3}")