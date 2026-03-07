#main de la calculatrice

from model import CalculatorModel #importation de la class calculatormodel du model
from view import CalculatorView
from controller import CalculatorController #importation de la class calculatorcontroller de la class contriller

model = CalculatorModel() #creation de l'objet model
view = CalculatorView() #creation de l'objet view pour la calculatrice basique et la calculatrice scientifique

controller = CalculatorController(model,view) #creation de l'objet controller avec le model et le view comme argumant

view.mainloop() #affichage de la fenetre 



#Membres du groupe

#Jean Yvenson CLERVIL
#Ezna CORNET
#Judekerly DELY
#Mitcheyda GACHETTE
#Fritz Roll-Handy GASPARD
#Mike Clarens GENOIT