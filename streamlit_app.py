# app.py

import streamlit as st

# Add Title
st.title('NutritionPlanner')

# Add Text
st.write('Text')

# Show Data
df = pd.DataFrame({
    'Line1': [1, 2, 3, 4],
    'Line2': [10, 20, 30, 40]
})
st.write(df)
