import streamlit as st
import pandas as pd

# Función para cargar datos desde CSV o Excel
def load_data():
    file = st.file_uploader("Sube tu archivo de datos", type=["csv", "xlsx"])
    if file is not None:
        if file.name.endswith('csv'):
            return pd.read_csv(file)
        elif file.name.endswith('xlsx'):
            return pd.read_excel(file)
    return None

# Función para calcular el modelo DuPont
def calculate_dupont(data):
    # Asegurarse de que los indicadores estén en el índice
    data.set_index('Indicador', inplace=True)
    
    # Calcular los resultados del modelo DuPont para cada periodo
    data['Margen Neto (%)'] = data.loc['EBIT'] / data.loc['Ventas Netas'] * 100
    data['Rotación (veces)'] = data.loc['Ventas Netas'] / data.loc['Activos Totales']
    data['Apalancamiento (veces)'] = data.loc['Activos Totales'] / data.loc['Capital Contable']
    data['ROE (%)'] = data['Margen Neto (%)'] * data['Rotación (veces)']
    data['ROA (%)'] = data['Rotación (veces)'] * data['Apalancamiento (veces)']
    data['Pay Back Capital (veces)'] = 1 / data['ROE (%)']
    data['Pay Back Activos (veces)'] = 1 / data['ROA (%)']
    
    # Calcular la variación porcentual entre los dos períodos
    t1 = data.columns[1]  # Primer período (t1)
    t2 = data.columns[2]  # Segundo período (t2)
    
    data['Variación (%)'] = ((data[t2] - data[t1]) / data[t1]) * 100
    
    # Redondear los resultados a un decimal
    data['Margen Neto (%)'] = data['Margen Neto (%)'].round(1)
    data['ROE (%)'] = data['ROE (%)'].round(1)
    data['ROA (%)'] = data['ROA (%)'].round(1)
    data['Rotación (veces)'] = data['Rotación (veces)'].round(1)
    data['Apalancamiento (veces)'] = data['Apalancamiento (veces)'].round(1)
    data['Pay Back Capital (veces)'] = data['Pay Back Capital (veces)'].round(1)
    data['Pay Back Activos (veces)'] = data['Pay Back Activos (veces)'].round(1)
    data['Variación (%)'] = data['Variación (%)'].round(1)

    return data

# Función para mostrar el reporte de resultados
def generate_report(data):
    # Crear DataFrame con el formato solicitado
    result_df = pd.DataFrame({
        "Modelo Dupont": ['Margen Neto', 'Rotación', 'Apalancamiento', 'ROE (Retorno Capital)', 
                          'ROA (Retorno Activos)', 'Pay Back Capital', 'Pay Back Activos'],
        't1': [data['Margen Neto (%)'].values[0], data['Rotación (veces)'].values[0], 
               data['Apalancamiento (veces)'].values[0], data['ROE (%)'].values[0], 
               data['ROA (%)'].values[0], data['Pay Back Capital (veces)'].values[0], 
               data['Pay Back Activos (veces)'].values[0]],
        't2': [data['Margen Neto (%)'].values[1], data['Rotación (veces)'].values[1], 
               data['Apalancamiento (veces)'].values[1], data['ROE (%)'].values[1], 
               data['ROA (%)'].values[1], data['Pay Back Capital (veces)'].values[1], 
               data['Pay Back Activos (veces)'].values[1]],
        '%': [data['Variación (%)'].values[0], data['Variación (%)'].values[1], 
              data['Variación (%)'].values[2], data['Variación (%)'].values[3], 
              data['Variación (%)'].values[4], data['Variación (%)'].values[5], 
              data['Variación (%)'].values[6]]
    })
    
    # Mostrar el reporte
    st.write("### Reporte del Modelo DuPont")
    st.write(result_df)

# Función principal de Streamlit
def main():
    st.title("Modelo DuPont para Medir Rentabilidad")
    
    # Cargar datos
    data = load_data()
    
    if data is not None:
        st.write("Datos cargados exitosamente:")
        st.write(data.head())

        # Calcular el modelo DuPont
        result = calculate_dupont(data)

        # Mostrar el reporte
        generate_report(result)
    else:
        st.warning("Por favor, carga un archivo para continuar.")

if __name__ == "__main__":
    main()
