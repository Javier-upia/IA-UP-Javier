
# Proyecto: Modelo DuPont para Medir Rentabilidad

Este proyecto implementa un modelo DuPont utilizando Streamlit para analizar y visualizar la rentabilidad de un negocio. El modelo calcula varios indicadores financieros clave, tales como el Margen Neto, Rotación, Apalancamiento, ROE (Retorno sobre el Capital), ROA (Retorno sobre los Activos), y Pay Back Capital y Activos.

## Descripción

El objetivo de este proyecto es permitir que los usuarios carguen archivos de datos financieros (CSV o Excel) y obtengan un análisis del rendimiento financiero basado en el modelo DuPont. Los cálculos incluyen la variación porcentual entre dos períodos seleccionados (t1 y t2) y los resultados se presentan en un formato tabular con el cambio porcentual calculado para cada indicador.

## Requisitos

Para ejecutar el proyecto en tu máquina, asegúrate de tener las siguientes librerías instaladas:

- streamlit
- pandas

Puedes instalar estas librerías ejecutando el siguiente comando:

```bash
pip install streamlit pandas
```

## Uso

1. Guarda el archivo del código `app.py` en tu máquina.
2. Ejecuta el siguiente comando en tu terminal para iniciar la aplicación:

```bash
streamlit run app.py
```

3. Una vez que la aplicación se haya abierto en tu navegador, carga un archivo CSV o Excel que contenga los datos financieros requeridos (por ejemplo, `EBIT`, `Ventas Netas`, `Activos Totales`, `Capital Contable`).
4. El modelo calculará los indicadores financieros y mostrará un reporte con los resultados de los dos períodos, junto con la variación porcentual entre ellos.

### Estructura del archivo de datos

El archivo que subas debe tener la siguiente estructura:

| Indicador               | t1   | t2   |
|-------------------------|------|------|
| EBIT                    | 67   | 139  |
| Depreciación            | 5    | 5    |
| Cuentas por cobrar      | 129  | 292  |
| Inventarios             | 69   | 163  |
| Proveedores             | 117  | 262  |
| EBITDA                  | 72   | 144  |
| Δ CxC                   | 0    | 163  |
| Δ Inventarios           | 0    | 94   |
| Δ Proveedores           | 0    | 145  |
| Variación CT            | 0    | 402  |
| FEL (antes CapEx e impuestos) | 72 | 546 |

## Resultados

Los resultados se mostrarán en una tabla con la siguiente estructura:

| Modelo Dupont           | t1   | t2   | %    |
|-------------------------|------|------|------|
| Margen Neto             | 12.0 | 13.0 | 8.3  |
| Rotación                | 1.5  | 1.8  | 20.0 |
| Apalancamiento          | 2.0  | 2.3  | 15.0 |
| ROE (Retorno Capital)   | 18.0 | 23.4 | 30.0 |
| ROA (Retorno Activos)   | 8.5  | 9.2  | 8.2  |
| Pay Back Capital        | 5.0  | 4.3  | -14.0|
| Pay Back Activos        | 4.2  | 3.8  | -9.5 |

## Contribuciones

Si deseas contribuir al proyecto, siéntete libre de enviar un pull request con mejoras o correcciones.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
