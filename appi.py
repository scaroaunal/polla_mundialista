import os
import streamlit as st
from PIL import Image

ruta_global = os.getcwd()
def main():
    st.title("Curso streamlit")
    st.header('Encabezado') 
    nombre = st.text_input('Ingresa tu nombre') 
    st.write(nombre)

    mensaje = st.text_area('Ingresa tu mensaje de felicitacion', height=200)
    st.write(mensaje)
    imagen = Image.open(os.path.join(ruta_global,'imagenes','fotomundial.png'))
    st.image(imagen)

    marcado1 = st.number_input('ingresar marcador', 1, 20,step=1)
    st.write(marcado1)

    st.text(f'hola {nombre}, como te va? ')
    st.success('Exito !!')
    # st.dataframe(df.style.highlight_max(axis=0))
    option = st.selectbox('Elige opciones',
                         ['arbol','camino'] )
    st.write(option)

    optiones = st.multiselect('Elige multiples opciones',
                         ['arbol','camino','ciudad','carretera'])
    
    fecha = st.date_input('selecciona fehca')
    st.write(fecha)

    hora = st.time_input('selecciona la hora')
    st.write(hora)
    
    st.write(optiones)

    edad = st.slider(
        'selecciona tu edad:',
        min_value=0,
        max_value=90,
        value=10,
        step=1,
    )
    st.write(edad)

    nivel = st.select_slider('selecciona tu nivel de satisfaccion:',
                            options=['malo','regular','bueno','excelente'],
                              value='regular'  )
if __name__ == '__main__':
    main()

