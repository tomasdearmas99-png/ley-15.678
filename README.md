# Simulador de Normativa de Celulares en el Aula (Ley 15.678)

## Descripción del Proyecto

Este repositorio contiene el desarrollo de la **Actividad 10 BIS** de la materia **Laboratorio de Programación (5° Año)** de la **E.E.S.T. N° 100 "Manuel José Joaquín del Corazón de Jesús Belgrano"**. 

El proyecto implementa un algoritmo de toma de decisiones en Python que simula la aplicación de la **Ley Provincial N° 15.678** (Provincia de Buenos Aires), evaluando si un estudiante tiene permitido el uso de dispositivos digitales dentro del aula según el contexto pedagógico o institucional.

---

## Marco Normativo: Ley 15.678

La **Ley 15.678** (promulgada el 10/11/2026) modifica la Ley N° 15.534 para promover el uso seguro y responsable de pantallas en establecimientos educativos de gestión pública y privada de la Provincia de Buenos Aires:

* **Regla general:** Queda prohibido el uso de teléfonos celulares y dispositivos digitales durante la jornada escolar en niveles primario y secundario.
* **Excepción pedagógica:** Su uso se habilita únicamente ante un requerimiento o autorización explícita del docente con fines estrictamente educativos.
* **Tenencia vs. Uso:** Se permite llevar el dispositivo guardado en la mochila para seguridad en el trayecto, pero no su manipulación sin permiso en clase.
* **Emergencias:** Toda comunicación urgente debe canalizarse institucionalmente a través de preceptoría y/o dirección.

---

## Estructura del Repositorio

```text
ley15678/
├── capturas/              # Evidencias de ejecución del script en consola
├── docs/                  # Informe técnico en formato APA v7 (PDF) y documentación
├── src/
│   └── ley_celulares.py   # Código fuente principal del simulador
└── README.md              # Documentación del repositorio
```

---

## Cómo ejecutar el proyecto

### Requisitos previos
* Tener instalado **Python 3.x** en el sistema.
* Un editor de código (como Visual Studio Code) o terminal de comandos.

### Pasos de ejecución
1. Clonar este repositorio en tu máquina local:
   ```bash
   git clone https://github.com
   ```
2. Ingresar al directorio del proyecto:
   ```bash
   cd ley15678
   ```
3. Ejecutar el script principal:
   ```bash
   python src/ley_celulares.py
   ```

---

## Lógica del Algoritmo (`src/ley_celulares.py`)

El programa utiliza estructuras de control condicional (`if`, `elif`, `else`) para evaluar dos variables booleanas principales: `autorizacion_docente` y `emergencia_familiar`.

| `autorizacion_docente` | `emergencia_familiar` | Resultado en Consola |
| :---: | :---: | :--- |
| `True` | `False` / `True` | `[ACCESO PERMITIDO]` Uso exclusivo con fines pedagógicos. |
| `False` | `True` | `[CANALIZACIÓN INSTITUCIONAL]` Gestión mediante preceptoría/dirección. |
| `False` | `False` | `[RESTRICCIÓN LEY 15.678]` El celular debe permanecer en la mochila. |

---

## Casos de Prueba (Salidas en Consola)

El script fue validado probando los tres escenarios posibles definidos por la normativa escolar:

* **Caso 1 (Autorización Docente activa):** Cuando `autorizacion_docente = True` y `emergencia_familiar = False`, el sistema devuelve `[ACCESO PERMITIDO] El celular solo para estudiar y para aprender (Fines Pedagogicos).`
* **Caso 2 (Emergencia Familiar validada):** Cuando `autorizacion_docente = False` y `emergencia_familiar = True`, el sistema devuelve `[CANALIZACIÓN INSTITUCIONAL] Gestionar la comunicación urgente a través de preceptoría y/o dirección.`
* **Caso 3 (Sin autorización ni emergencia):** Cuando ambas variables son `False`, el sistema devuelve `[RESTRICCIÓN LEY 15.678] Tu celular debe permanecer guardado en la mochila.`

---

## Enlaces de Referencia

* Documentación Oficial de Python — Control de Flujo: https://python.org
* Ley 15.678 — Normativa Provincia de Buenos Aires: https://gba.gob.ar
* Marco Normativo Educativo — Argentina.gob.ar: https://argentina.gob.ar

---

## Autor

* **Estudiante:** Leonel De Armas
* **Docente:** Mansilla Muñoz York Elías
* **Curso:** 5° Año — Laboratorio de Programación (LPR 2026)
* **Institución:** E.E.S.T. N° 1 Vicente López"
