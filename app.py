import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
'''
x_limit =

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange()

# Create a random array of data that we will use for our y values
y_data = []

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')




x_limit = 100
x_axis = np.arange(x_limit+1)

y_data = [random.random() for value in x_axis]
df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)




st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')



scatter = alt.Chart(df).mark_point().encode(x=alt.X('x'), y=alt.Y('y'))
st.altair_chart(scatter, use_container_width=True)



st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)


scatter2 = alt.Chart(df, title='Random points', background = '#F8F3FE',
    padding={"left": 5, "top": 10, "right": 5, "bottom": 5}).encode(
    x=alt.X('x', axis = alt.Axis(title='')),
    y=alt.Y('y'),
    size='y').mark_square(stroke="#79A9A2", fill='False')

st.altair_chart(scatter2, use_container_width=True)


st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:20px;
}
</style>
''', unsafe_allow_html=True)

st.markdown("""
The 5 changes I made were:
- Changed the dots to squares
- Added a title
- Added a background color
- Removed x-axis label
- Increased the top padding of the chart object
""")



st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)



st.markdown("""
The 2 changes I made (to https://altair-viz.github.io/gallery/area_chart_gradient.html) were:
- Changed the gradient type from linear to radial
- Overlayed 2 gradients
"""
)




source = data.stocks()

areachart1 = alt.Chart(source).transform_filter(
    'datum.symbol==="GOOG"'
).mark_area(
    line={'color':'black'},
    color=alt.Gradient(
        gradient='radial',
        stops=[alt.GradientStop(color='#B41C3D', offset=0),
                alt.GradientStop(color='#B41C3D', offset=0.1),
               alt.GradientStop(color='#FFFFFF60', offset=1)],
        x1=0.58,
        x2=0.58,
        y1=0.01,
        y2=0.01
        ,
        r1=0.001,
        r2=0.2
    )
).encode(
    alt.X('date:T', axis = alt.Axis(title='')),
    alt.Y('price:Q')
)

areachart2 = alt.Chart(source).transform_filter(
    'datum.symbol==="GOOG"'
).mark_area(
    line={'color':'darkgrey'},
    color=alt.Gradient(
        gradient='radial',
        stops=[alt.GradientStop(color='#5055C0', offset=0),
                alt.GradientStop(color='#5055C0', offset=0.1),
               alt.GradientStop(color='#FFFFFF60', offset=1)],
        x1=0.95,
        x2=0.95,
        y1=0.16,
        y2=0.16
        ,
        r1=0.001,
        r2=0.15
    )
).encode(
    alt.X('date:T', axis = alt.Axis(title='')),
    alt.Y('price:Q')
)

areachart = areachart1+areachart2

st.altair_chart(areachart, use_container_width=True)
