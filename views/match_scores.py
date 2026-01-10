import streamlit as st
import json
import os
from datetime import date
from components.match_widget import MatchWidget

class MatchScoresPage:
    def __init__(self):
        self.teams_file = "teams.json"
        
    def _load_teams(self):
        if os.path.exists(self.teams_file):
            with open(self.teams_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def render(self):
        MatchWidget.inject_custom_css()
        st.title("⚽ Ingresar Marcadores")
        st.write("Bienvenido, aquí puedes ingresar tus predicciones para los próximos partidos.")
        
        teams_data = self._load_teams()
        
        # Definición de partidos con objetos date para permitir filtrado
        matches = [
            {"id": "m1", "team_a": {"name": "Colombia", "code": "co"}, "team_b": {"name": "Argentina", "code": "ar"}, "date": date(2026, 3, 15), "time": "18:00"},
            {"id": "m2", "team_a": {"name": "Brasil", "code": "br"}, "team_b": {"name": "Uruguay", "code": "uy"}, "date": date(2026, 3, 16), "time": "20:30"},
            {"id": "m3", "team_a": {"name": "Francia", "code": "fr"}, "team_b": {"name": "España", "code": "es"}, "date": date(2026, 3, 17), "time": "15:00"},
            {"id": "m4", "team_a": {"name": "Alemania", "code": "de"}, "team_b": {"name": "Inglaterra", "code": "gb-eng"}, "date": date(2026, 3, 18), "time": "14:00"},
            {"id": "m5", "team_a": {"name": "Italia", "code": "it"}, "team_b": {"name": "Portugal", "code": "pt"}, "date": date(2026, 3, 19), "time": "19:45"},
            {"id": "m6", "team_a": {"name": "México", "code": "mx"}, "team_b": {"name": "EE.UU.", "code": "us"}, "date": date(2026, 3, 20), "time": "21:00"},
            # Partidos adicionales para probar el filtro
            {"id": "m7", "team_a": {"name": "Chile", "code": "cl"}, "team_b": {"name": "Perú", "code": "pe"}, "date": date(2026, 3, 15), "time": "20:00"},
            {"id": "m8", "team_a": {"name": "Ecuador", "code": "ec"}, "team_b": {"name": "Paraguay", "code": "py"}, "date": date(2026, 3, 15), "time": "16:00"},
        ]
        
        # Filtro por fecha
        st.markdown("### 🔍 Filtrar por Fecha")
        selected_date = st.date_input("Selecciona una fecha para ver los partidos:", value=date(2026, 3, 15))
        
        # Filtrar la lista de partidos
        filtered_matches = [m for m in matches if m["date"] == selected_date]
        
        with st.form("match_scores_form"):
            st.subheader(f"Partidos del {selected_date.strftime('%d %b %Y')}")
            
            if not filtered_matches:
                st.info(f"No hay partidos programados para el {selected_date.strftime('%d %b %Y')}. Selecciona otra fecha arriba. 📅")
                user_predictions = {}
            else:
                st.markdown("Ingresa tus pronósticos y presiona el botón al final para guardar.")
                
                user_predictions = {}
                # Renderizar en 3 columnas
                for i in range(0, len(filtered_matches), 3):
                    cols = st.columns(3)
                    
                    # Procesar hasta 3 partidos por fila
                    for j in range(3):
                        if i + j < len(filtered_matches):
                            match = filtered_matches[i + j]
                            with cols[j]:
                                # Formatear fecha para el widget
                                display_date = match["date"].strftime("%d %b")
                                score_a, score_b = MatchWidget.render(
                                    match["team_a"]["name"], match["team_a"]["code"], 
                                    match["team_b"]["name"], match["team_b"]["code"], 
                                    match["id"],
                                    match_date=display_date,
                                    match_time=match.get("time")
                                )
                                user_predictions[match["id"]] = (score_a, score_b)

            st.markdown("---")
            submitted = st.form_submit_button("🚀 Guardar Todos mis Marcadores", use_container_width=True)
            
            if submitted and filtered_matches:
                st.success("¡Tus marcadores han sido guardados exitosamente! 🎉")
            elif submitted and not filtered_matches:
                st.warning("No hay marcadores para guardar en esta fecha.")

