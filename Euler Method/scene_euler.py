import pandas as pd
import numpy as np
from manim import *
'''
DATA:
A .csv archive with the coordnates of the points.
The data in columns 0 and 1 have x and y values for a number of points,
On columns 2 and 3 there's x and y values for another sets of points, etc.
'''
df = pd.read_csv('data.csv',header=0)


x = []
y = []
for i in range(0,len(df.columns)-2,2):
  x1 = []
  y1 = []
  for j in range(len(df)):
    if(str(df[str(i)][j])=='nan'):
      break
    else:
      x1.append(df[str(i)][j])
      y1.append(df[str(i+1)][j])
  
  x.append(x1)
  y.append(y1)

'''
INPUT:
Two matrixes:

x - values of the x coordnate, each array contaning a set of values (x[0] is a set, 
meant to be paired with y[0], x[1] is another,etc.)

y - same as x
'''

class Plot(Scene):
    def construct(self):

        #Create the axes
        ax = Axes(
            x_range=[0, 120,20], y_range=[0,3], axis_config={"include_tip": False,"include_numbers": True}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        #Title
        title = Text("Euler Method",font_size=20).to_edge(UP)

        #Ceating the axes and title
        self.play(Create(title))
        self.wait()
        self.play(Create(ax))
        self.play(Create(labels))

        #First animation - animate the first batch of points and 
        #displays the number of points on screen
        text = Text(f"Nº of points :{len(x[0])-1}",font_size=15).to_edge(UL*2.5)
        self.play(Create(text))


        line = ax.plot_line_graph(x[0], y[0], add_vertex_dots=True,line_color=BLACK,vertex_dot_radius=0.04)
        self.play(Create(line))
         
        #Iterative animation - animates the rest of the points and updates
        #the number of points on screen acordingly

        for i in range(1,len(x),4):
            text1 = Text(f"Nº of points :{len(x[i])-1}",font_size=15).to_edge(UL*2.5)
            line1 = ax.plot_line_graph(x[i], y[i], add_vertex_dots=True,line_color=BLACK,vertex_dot_radius=0.04)
            self.play(ReplacementTransform(text,text1))
            self.play(ReplacementTransform(line,line1))

            
            line = line1
            text = text1
