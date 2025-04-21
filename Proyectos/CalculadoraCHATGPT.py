# Calculadora o conversor de tiempo a salario neto
print("Bienvenidos al sistema de conversión laboral.\n")

# Función para validar que el input sea un número
def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error de caractér. Ingrese un valor numérico.")

# Datos a pedir con validación
horas_trabajadas = pedir_numero("Ingrese cantidad de horas trabajadas al día: ")
dias_trabajados = pedir_numero("Ingrese la cantidad de días semanales trabajados: ")
salario_neto = pedir_numero("Ingrese en números su salario neto mensual: ")
salario_por_hora = pedir_numero("Ingrese el monto del salario por hora: ")

# Cálculos / Conversión
conversion_semanal = horas_trabajadas * dias_trabajados  # Horas trabajadas semanalmente
conversion_mensual = conversion_semanal * 4.33  # Horas trabajadas mensualmente (aprox.)
conversion_por_hora = salario_neto / conversion_mensual  # Salario por hora calculado
conversion_hora_a_mensual = salario_por_hora * conversion_mensual  # Salario mensual según horas
conversion_hora_a_semanal = salario_por_hora * conversion_semanal  # Salario semanal según horas

# Datos finales
print("\n------ RESULTADOS ------\n")
print(f"Tiempo trabajado semanalmente: {conversion_semanal:.2f} horas")
print(f"Tiempo trabajado mensualmente: {conversion_mensual:.2f} horas")
print(f"Salario calculado por hora (desde el salario neto): ${conversion_por_hora:.2f}")
print(f"Salario mensual según horas y valor por hora: ${conversion_hora_a_mensual:.2f}")
print(f"Salario semanal según horas y valor por hora: ${conversion_hora_a_semanal:.2f}")

from datetime import datetime

def calcular_indemnizacion(sueldo_bruto, fecha_ingreso, fecha_despido):

# Calcular antigüedad
    años = fecha_despido.year - fecha_ingreso.year
    if fecha_despido.month < fecha_ingreso.month or (fecha_despido.month == fecha_ingreso.month and fecha_despido.day < fecha_ingreso.day):
        años -= 1

    meses_extra = (fecha_despido.year - fecha_ingreso.year) * 12 + (fecha_despido.month - fecha_ingreso.month)
    if fecha_despido.day >= fecha_ingreso.day:
        meses_extra += 1
    fraccion_mayor_3_meses = (meses_extra % 12) > 3
    if fraccion_mayor_3_meses:
        años += 1

# Indemnización por antigüedad
    indemnizacion_antiguedad = sueldo_bruto * años

# Preaviso (1 mes si antigüedad ≤ 5 años, 2 meses si > 5 años)
    preaviso = sueldo_bruto * (2 if años > 5 else 1)

# Integración del mes de despido
    dias_del_mes = 30  # estándar en cálculos laborales
    dias_restantes = dias_del_mes - fecha_despido.day
    integracion_mes_despido = sueldo_bruto / dias_del_mes * dias_restantes

# Días de vacaciones según antigüedad
    if años >= 20:
        dias_vacaciones = 35
    elif años >= 10:
        dias_vacaciones = 28
    elif años >= 5:
        dias_vacaciones = 21
    elif años >= 1:
        dias_vacaciones = 14
    else:
        dias_trabajados = (fecha_despido - fecha_ingreso).days
        dias_vacaciones = int((dias_trabajados / 365) * 14)

# Vacaciones no gozadas
    vacaciones_no_gozadas = sueldo_bruto / 25 * dias_vacaciones

# SAC proporcional (aguinaldo)
    meses_trabajados = fecha_despido.month - 1 + fecha_despido.day / 30
    sac_proporcional = sueldo_bruto / 12 * meses_trabajados / 6

# Suma total
    total = (
        indemnizacion_antiguedad +
        preaviso +
        integracion_mes_despido +
        vacaciones_no_gozadas +
        sac_proporcional
    )

    return {
        "Antigüedad": indemnizacion_antiguedad,
        "Preaviso": preaviso,
        "Integración Mes": integracion_mes_despido,
        "Vacaciones no Gozadas": vacaciones_no_gozadas,
        "SAC Proporcional": sac_proporcional,
        "Total Estimado": total
    }
# ============================
# 🧾 PROGRAMA PRINCIPAL
# ============================

print("📋 CALCULADORA DE INDEMNIZACIÓN ARGENTA")
print("Este script calcula la indemnización por despido sin causa según la Ley de Contrato de Trabajo.")
print("Vas a necesitar ingresar el sueldo bruto y las fechas de ingreso y egreso.")
print("-" * 60)

try:
    # Ingreso del sueldo
    sueldo_bruto = float(input("💰 Ingresá tu último sueldo bruto ($): ").replace(",", "."))

    # Fechas (formato dd/mm/aaaa)
    fecha_ingreso_str = input("📅 Ingresá la fecha de ingreso (dd/mm/aaaa): ")
    fecha_despido_str = input("📅 Ingresá la fecha de despido (dd/mm/aaaa): ")

    fecha_ingreso = datetime.strptime(fecha_ingreso_str, "%d/%m/%Y").date()
    fecha_despido = datetime.strptime(fecha_despido_str, "%d/%m/%Y").date()

    # Cálculo
    resultado = calcular_indemnizacion(sueldo_bruto, fecha_ingreso, fecha_despido)

    print("\n📊 RESULTADO DEL CÁLCULO:")
    for concepto, valor in resultado.items():
        print(f"{concepto}: ${valor:,.2f}".replace(",", ".").replace(".", ",", 1))

except Exception as e:
    print(f"\n⚠️ ¡Opa! Algo salió mal con los datos ingresados.\nDetalle del error: {e}")