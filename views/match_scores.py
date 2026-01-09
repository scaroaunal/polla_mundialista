import streamlit as st
import json
import os
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
        st.title("⚽ Ingresar Marcadores")
        st.write("Bienvenido, aquí puedes ingresar tus predicciones para los próximos partidos.")
        
        teams_data = self._load_teams()
        # Ejemplo de partidos (esto vendría de una base de datos de partidos en el futuro)
        matches = [
            {"id": "m1", "team_a": {"name": "Colombia", "code": "co"}, "team_b": {"name": "Argentina", "code": "ar"}},
            {"id": "m2", "team_a": {"name": "Brasil", "code": "br"}, "team_b": {"name": "Uruguay", "code": "uy"}},
            {"id": "m3", "team_a": {"name": "Francia", "code": "fr"}, "team_b": {"name": "España", "code": "es"}},
        ]
        
        with st.form("match_scores_form"):
            st.subheader("Próximos Partidos")
            st.markdown("Ingresa tus pronósticos y presiona el botón al final para guardar.")
            
            user_predictions = {}
            for match in matches:
                score_a, score_b = MatchWidget.render(
                    match["team_a"]["name"], 
                    match["team_a"]["code"], 
                    match["team_b"]["name"], 
                    match["team_b"]["code"], 
                    match["id"]
                )
                user_predictions[match["id"]] = (score_a, score_b)
            
            st.markdown("---")
            submitted = st.form_submit_button("🚀 Guardar Todos mis Marcadores", use_container_width=True)
            
            if submitted:
                # Aquí se guardaría en la base de datos real
                st.success("¡Tus marcadores han sido guardados exitosamente! 🎉")
                # st.json(user_predictions)
