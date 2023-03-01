import streamlit as st
import plotly.graph_objs as go

# Define the initial data for each plot type
data_3d = [go.Scatter3d(x=[], y=[], z=[], mode='markers')]
data_2d = [go.Scatter(x=[], y=[], mode='markers')]
data_1d = [go.Histogram(x=[], nbinsx=10)]

# Define the layout for each plot type
layout_3d = go.Layout(
    margin=dict(l=0, r=0, b=0, t=0),
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    )
)
layout_2d = go.Layout(
    margin=dict(l=0, r=0, b=0, t=0),
    xaxis=dict(title='X'),
    yaxis=dict(title='Y')
)
layout_1d = go.Layout(
    margin=dict(l=0, r=0, b=0, t=0),
    xaxis=dict(title='X'),
    yaxis=dict(title='Count')
)

# Display the input form
with st.form("input_form"):
    plot_type = st.selectbox("Select plot type", ["3D", "2D", "1D"])
    x_input = st.text_input("Enter x value")
    y_input = st.text_input("Enter y value")
    z_input = st.text_input("Enter z value (for 3D plot only)")
    submit_button = st.form_submit_button("Add point")

# Add the new data point to the selected plot type
if submit_button:
    if plot_type == "3D":
        data_3d[0]['x'].append(float(x_input))
        data_3d[0]['y'].append(float(y_input))
        data_3d[0]['z'].append(float(z_input))
    elif plot_type == "2D":
        data_2d[0]['x'].append(float(x_input))
        data_2d[0]['y'].append(float(y_input))
    elif plot_type == "1D":
        data_1d[0]['x'].append(float(x_input))

# Display the selected plot type
if plot_type == "3D":
    fig = go.Figure(data=data_3d, layout=layout_3d)
elif plot_type == "2D":
    fig = go.Figure(data=data_2d, layout=layout_2d)
else:
    fig = go.Figure(data=data_1d, layout=layout_1d)

st.plotly_chart(fig, use_container_width=True)
