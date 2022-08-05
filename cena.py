import pandas as pd
from manim import *

x = [0.0,12.0,24.0,36.0,48.0,60.0,72.0,84.0,96.0,108.0,120.0]
y=[0.0,1.9230769230769234,1.9697849107029295,1.9938428368372687,2.0063391436575917,2.0128575697818114,2.0162651523742987,2.0180485103429047,2.01898237763818,2.0194715532152125,2.019727832749883]

x1=[0.0,6.0,12.0,18.0,24.0,30.0,36.0,42.0,48.0,54.0,60.0,66.0,72.0,78.0,84.0,90.0,96.0,102.0,108.0,114.0,120.0]
y1=[0.0, 0.9615384615384617, 1.25968032394436, 1.4619071003386892, 1.6054521645195743, 1.7097779284915822, 1.7866902593804734, 1.8439245263030979, 1.8867888701421112, 1.9190366907091971, 1.943376728340387, 1.9617920309019767, 1.9757493846734486, 1.9863418853065178, 1.9943886605063121, 2.0005060653010487, 2.005159306550947, 2.0087003213423333, 2.0113958205712583, 2.0134481940048223, 2.0150111755301565]
class Plot(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 120,20], y_range=[0,3], axis_config={"include_tip": False,"include_numbers": True}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")
        
        title = Text("Método numérico de Euler",font_size=20).to_edge(UP)
        author = Text("Alejandro da Rocha Loureiro",font_size=15).to_edge(UR)
        self.play(Create(title))
        self.wait()
        self.play(Create(ax))
        self.play(Create(labels))
        self.play(Create(author))

        line1 = ax.plot_line_graph(x, y, add_vertex_dots=True)
        line2 = ax.plot_line_graph(x1, y1, add_vertex_dots=True)
        self.play(Create(line1))
        self.wait()
        self.play(ReplacementTransform(line1,line2))
        self.wait()
