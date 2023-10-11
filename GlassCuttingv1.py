import streamlit as st
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout='wide')

_, h1, _ = st.columns([1.5,2,1.5])
h1.header('Glass Cutting Problem')
st.write('----')

 
import pulp

# Create the ILP problem
problem = pulp.LpProblem("GlassCutting", pulp.LpMinimize)

# Define variables
buff1, col1, col2, buff2 = st.columns([1,2,2,1])
col1.markdown('#### Glass Sheet Dimensions')
col2.markdown('#### Piece Dimensions')

_,col1, col2,_, col3, col4,_,_ = st.columns(8)
m = col1.number_input('Width of the glass sheet (in inches)',1,100,10,1)  # Width of the glass sheet (in inches)
n = col2.number_input('Height of the glass sheet (in inches)',1,100,10,1)  # Width of the glass sheet (in inches)
a = col3.number_input(f'Width of each piece          \n  (in inches)',1,100,3,1)  
b = col4.number_input(f'Height of each piece        \n  (in inches)',1,100,3,1)  

st.write('----')
st.subheader('Trying with different Orientations')

class GlassCutter():
    def __init__(self,m,n,a,b):
        super().__init__()
        self.m = m
        self.n = n
        self.a = a
        self.b = b 
        # define all possible orientations
        self.orientationDict = {
            0: [(m,n),(a,b)], 
            1: [(m,n),(b,a)], 
            2: [(n,m),(a,b)], 
            3: [(n,m),(b,a)], 
        }

    def process(self):
        # placeholder to capture coordinates 
        self.coordDict = {
            0 : [],
            1 : [],
            2 : [],
            3: []
        }
        self.wastage = []

        # iterate through all combinations of orientation and retrieve the coordinates 
        for k in self.coordDict.keys():
            for i in range(0,m,a):
                for j in range(0,n,b):
                    if i + a <=m and j + b <=n: #constraint to avoid overflow
                        self.coordDict[k].append((i,j))

        # calculate Wastage 
        for k, vCoordinates in self.coordDict.items():
            vColor = False 
            # Sheet Array
            S = np.ones(shape=(m,n))
            # Piece Array Mask
            P = np.ones(shape=(m,n))
            # for visualization
            PMask = np.ones(shape=(m,n))
            for coord in vCoordinates:
                P[coord[0]:coord[0]+a, coord[1]:coord[1]+b] = 0
            # Overlay Sheet and Pieces
            W = S*P
            
            self.wastage.append(W.sum())
            # Visualize 
            _, colfig, _ = st.columns([0.25,2,0.25])
            with colfig.expander(f"Dimension {self.orientationDict[k]} Wastage:{W.sum()}", expanded=True if k==0 else False):
                # color variations 
                colorArray = np.linspace(0,0.5,num=len(vCoordinates))
                textArray = []

                for idx, (coord, color) in enumerate(zip(vCoordinates,colorArray)):
                    W[coord[0]:coord[0]+a, coord[1]:coord[1]+b] = color
                    textArray.append(
                        go.Scatter(
                            y = [(coord[0]+(a/2)-0.5)], #expects array input
                            x = [(coord[1]+(b/2)-0.5)],
                            text = idx+1,
                            mode = 'text',
                            textposition='middle center',
                            textfont=dict(size=20, color='white' if color<=0.25 else 'black')
                            
                        )
                    )



                labels = {
                    'x':"Sheet Width (m)",
                    'y':"Sheet Height (n)" ,
                    'color':'Z Label'      
                    }
                fig = px.imshow(
                    W,
                    labels=labels, 
                    # x = np.arange(1,m+1,step=1),
                    # y = np.arange(1,n+1,step=1),
                    color_continuous_scale='RdYlGn_r',
                    aspect = 'equal'
                    )
                    
                fig.update_layout(coloraxis_showscale=False
                                  )
                fig.update_xaxes(side='top')
                for idx, text in enumerate(textArray):
                    fig.add_trace(text)
                    fig.data[idx+1].update(showlegend=False)
                st.plotly_chart(fig)


                st.write('Wastage (in inches^2)')
                st.error(W.sum())
                st.write('Total Pieces')
                st.info(len(vCoordinates))
                st.write('Coordinates')
                st.info(vCoordinates)



        
        
            
                


            



        



    



glasscutter = GlassCutter(m,n,a,b)
glasscutter.process()

