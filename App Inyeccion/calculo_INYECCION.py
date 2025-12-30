import streamlit as st
import math

def calcular_sistema():
    st.set_page_config(page_title="Dimensionamiento Nanoburbujas ETI Patagonia", layout="wide")
    st.title("📊 Calculador de Biorremediación de Sedimentos (Nanoburbujas)")
    st.markdown("### Proyección para Centros de Cultivo de Salmon/Truchas/etc")
    st.markdown("### ETI Patagonia - prof.martintorres")

    # --- BARRA LATERAL (ENTRADAS COMUNES) ---
    st.sidebar.header("Configuración de la Jaula")
    ancho = st.sidebar.number_input("Ancho de la jaula (m)", value=30.0)
    largo = st.sidebar.number_input("Largo de la jaula (m)", value=30.0)
    profundidad = st.sidebar.number_input("Profundidad del fondo (m)", value=60.0)
    area = ancho * largo

    # --- SECCIONES DE INTERFACE ---
    tab1, tab2 = st.tabs(["🌊 Mar Abierto", "🏞️ Mar Protegido (Estuario)"])

    with tab1:
        st.subheader("Configuración: Alta Energía / Mar Abierto")
        col1, col2 = st.columns(2)
        with col1:
            corriente = st.slider("Velocidad de corriente (m/s)", 0.1, 1.5, 0.5, key="c1")
            sod = st.number_input("Demanda O2 Sedimento (g/m2/día)", value=20.0, key="sod1")
        with col2:
            eficiencia = st.slider("Eficiencia de Transferencia (%)", 80, 98, 95, key="ef1")
            factor_seguridad = 2.5  # Mayor dispersión en mar abierto

        # Cálculos Mar Abierto
        presion_atm = 1 + (profundidad / 10)
        demanda_teorica = area * sod
        # El factor de corriente aumenta la demanda necesaria para mantener saturación
        demanda_total = (demanda_teorica * factor_seguridad) * (1 + corriente)
        
        mostrar_resultados(demanda_total, eficiencia, presion_atm, "Mar Abierto")

    with tab2:
        st.subheader("Configuración: Baja Energía / Estuario")
        col3, col4 = st.columns(2)
        with col3:
            corriente_est = st.slider("Velocidad de corriente (m/s)", 0.01, 0.3, 0.05, key="c2")
            sod_est = st.number_input("Demanda O2 Sedimento (g/m2/día)", value=12.0, key="sod2")
        with col4:
            eficiencia_est = st.slider("Eficiencia de Transferencia (%)", 80, 98, 92, key="ef2")
            factor_seguridad_est = 1.3 # Menor pérdida por corriente

        # Cálculos Estuario
        presion_atm_est = 1 + (profundidad / 10)
        demanda_teorica_est = area * sod_est
        demanda_total_est = demanda_teorica_est * factor_seguridad_est
        
        mostrar_resultados(demanda_total_est, eficiencia_est, presion_atm_est, "Estuario")

def mostrar_resultados(demanda_kg_dia, eficiencia, presion, tipo):
    # Conversión a kg/día (asumiendo entrada en gramos)
    kg_necesarios = demanda_kg_dia / 1000
    kg_reales = kg_necesarios / (eficiencia / 100)
    
    st.info(f"#### Resultados Proyectados: {tipo}")
    c1, c2, c3 = st.columns(3)
    c1.metric("O2 Requerido (kg/día)", f"{kg_reales:.2f}")
    c2.metric("Presión en Fondo (ATM)", f"{presion:.1f}")
    
    # Recomendación de Equipos (Lógica 2025)
    tiempo_op = 18 # Horas estándar de operación
    capacidad_hora = kg_reales / tiempo_op
    
    st.write(f"**Sugerencia de Inyección:**")
    st.success(f"Se requiere un sistema que aporte **{capacidad_hora:.2f} kg O2/hora** durante {tiempo_op} horas al día.")
    
    if capacidad_hora < 1.0:
        st.write("✅ **Equipo Sugerido:** Generador de Nanoburbujas Compacto (Serie S).")
    elif capacidad_hora < 3.0:
        st.write("🚀 **Equipo Sugerido:** Generador Industrial (Serie M) con mangueras de difusión microperforadas.")
    else:
        st.write("🏢 **Equipo Sugerido:** Planta de Oxigenación centralizada con múltiples cabezales de inyección.")

if __name__ == "__main__":
    calcular_sistema()