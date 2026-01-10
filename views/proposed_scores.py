import streamlit as st
from datetime import date
import pandas as pd

class ProposedScoresPage:
    def __init__(self):
        # Datos de ejemplo (Mock Data)
        self.proposed_scores = [
            {"participante": "Juan Pérez", "fecha": date(2026, 3, 15), "partido": "Colombia vs Argentina", "grupo": "A", "fase": "Fase de Grupos", "marcador": "2 - 1"},
            {"participante": "Juan Pérez", "fecha": date(2026, 3, 15), "partido": "Chile vs Perú", "grupo": "A", "fase": "Fase de Grupos", "marcador": "1 - 1"},
            {"participante": "María García", "fecha": date(2026, 3, 15), "partido": "Colombia vs Argentina", "grupo": "A", "fase": "Fase de Grupos", "marcador": "0 - 2"},
            {"participante": "María García", "fecha": date(2026, 3, 16), "partido": "Brasil vs Uruguay", "grupo": "B", "fase": "Fase de Grupos", "marcador": "3 - 0"},
            {"participante": "Carlos López", "fecha": date(2026, 3, 15), "partido": "Colombia vs Argentina", "grupo": "A", "fase": "Fase de Grupos", "marcador": "1 - 1"},
            {"participante": "Carlos López", "fecha": date(2026, 3, 17), "partido": "Francia vs España", "grupo": "C", "fase": "Fase de Grupos", "marcador": "2 - 2"},
            {"participante": "Andrea Ruiz", "fecha": date(2026, 7, 10), "partido": "TBD vs TBD", "grupo": "-", "fase": "Cuartos de Final", "marcador": "1 - 0"},
            {"participante": "Juan Pérez", "fecha": date(2026, 3, 16), "partido": "Brasil vs Uruguay", "grupo": "B", "fase": "Fase de Grupos", "marcador": "1 - 2"},
        ]

    def render(self):
        st.title("📋 Marcadores Propuestos")
        st.write("Explora las predicciones realizadas por todos los participantes.")

        # Sección de Filtros
        with st.expander("🔍 Filtros de Búsqueda", expanded=True):
            col1, col2 = st.columns(2)
            col3, col4 = st.columns(2)

            with col1:
                filter_date = st.date_input("Filtrar por Fecha", value=None, help="Selecciona una fecha para ver los partidos de ese día")
            
            with col2:
                # Obtener grupos únicos
                grupos = sorted(list(set(d["grupo"] for d in self.proposed_scores)))
                filter_group = st.selectbox("Filtrar por Grupo", options=["Todos"] + grupos)

            with col3:
                # Obtener fases únicas
                fases = sorted(list(set(d["fase"] for d in self.proposed_scores)))
                filter_phase = st.selectbox("Filtrar por Fase", options=["Todas"] + fases)

            with col4:
                filter_name = st.text_input("Buscar por Nombre de Participante", placeholder="Ej: Juan Pérez")

        # Lógica de Filtrado
        filtered_data = self.proposed_scores

        if filter_date:
            filtered_data = [d for d in filtered_data if d["fecha"] == filter_date]
        
        if filter_group != "Todos":
            filtered_data = [d for d in filtered_data if d["grupo"] == filter_group]
        
        if filter_phase != "Todas":
            filtered_data = [d for d in filtered_data if d["fase"] == filter_phase]
        
        if filter_name:
            filtered_data = [d for d in filtered_data if filter_name.lower() in d["participante"].lower()]

        # Mostrar Resultados
        if not filtered_data:
            st.info("No se encontraron marcadores propuestos con los filtros seleccionados. 😕")
        else:
            # Convertir a DataFrame para una visualización más limpia
            df = pd.DataFrame(filtered_data)
            
            # Formatear la fecha para mostrar
            df['fecha'] = df['fecha'].apply(lambda x: x.strftime('%d %b %Y'))
            
            # Renombrar columnas para la UI
            df.columns = [col.capitalize() for col in df.columns]
            
            # Estilizar y mostrar la tabla
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Participante": st.column_config.TextColumn("Participante", width="medium"),
                    "Fecha": st.column_config.TextColumn("Fecha", width="small"),
                    "Partido": st.column_config.TextColumn("Partido", width="large"),
                    "Marcador": st.column_config.TextColumn("Marcador", width="small"),
                }
            )

            st.caption(f"Mostrando {len(filtered_data)} resultados")
