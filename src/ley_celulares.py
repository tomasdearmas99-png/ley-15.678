# ===========================================================================================
# Laboratorio de Programación (LPR 5° Año) — EEST N.º 1 - “Eduardo Ader” Vicente López
# ACTIVIDAD 10 BIS: Simulador de Normativa de Celulares en el Aula (Ley 15.678)
# DOCENTE: Mansilla Muñoz York Elías
# ESTUDIANTE: Leonel De Armas
# ===========================================================================================

print("==================================================")
print("=== SISTEMA DE ASESORAMIENTO NORMATIVO ESCOLAR ===")
print("==================================================\n")

# Simulamos las variables de contexto del aula
autorizacion_docente = False  # Cambiar a True si el profe habilitó la actividad digital
emergencia_familiar = False   # Cambiar a True si fue validado por preceptores

print(f"Estado de Autorización Docente : {autorizacion_docente}")
print(f"Estado de Emergencia Validada  : {emergencia_familiar}\n")

# Estructura de decisión
if autorizacion_docente == True:
    print("[ACCESO PERMITIDO] El celular solo para estudiar y para aprender (Fines Pedagogicos).")
elif emergencia_familiar == True:
    print("[CANALIZACIÓN INSTITUCIONAL] Gestionar la comunicación urgente a través de preceptoría y/o dirección.")
else:
    print("[RESTRICCIÓN LEY 15.678] Tu celular debe permanecer guardado en la mochila.")

print("==================================================")
