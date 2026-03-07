#controller du projet


class CalculatorController: #creation de la class calculatorcontroller

    def __init__(self, model, view): #constructeur de la class

        self.model = model
        self.view = view

        self.actuel = "" #variable string pour stocker les donnees saisi par l'utilisateur en temps reel
        self.expression = [] #liste pour conserver les donnees rentrer par l'utilisateur

        for key, btn in self.view.buttons.items(): #recuperation de la cle et les valeur des bouton 
            btn.configure(command=lambda x=key:self.on_click(x)) #configuration d'une action pour chaque boutons

    def close_fenetre(self):
        self.model.clear_historique()
        self.view.history_fenetre.destroy()

    def on_click(self, char): #methode pour determiner l'action des boutons qui prend char comme parametre

        if char.isdigit() or char == '.':
            self.actuel += char
            self.view.set_display(''.join(self.expression) + self.actuel)

        elif char in "+*/x-":
            if self.actuel:
                self.expression.append(self.actuel)
                self.expression.append(" "+char+ " ")
                self.actuel=""
                self.view.set_display(''.join(self.expression))
            elif self.expression and (self.expression[-1] == ")"or self.expression[-1].isdigit()):
                self.expression.append(self.actuel)
                self.expression.append(" "+char+ " ")
                self.view.set_display(''.join(self.expression))
            else:
                pass

        elif char=="C":
            self.view.display.configure(state="normal")
            self.actuel=""
            self.expression=[]
            self.view.set_display("")
            

        elif char=="⌫": 
            if self.actuel:             
                self.actuel=self.actuel[:-1]
            elif not self.actuel:
                self.expression = self.expression[:-1]
            self.view.set_display(''.join(self.expression)+ self.actuel)  

        elif char == "🗑" :
            self.view.textebox.configure(state = "normal")
            self.view.textebox.delete('1.0', "end")
            self.model.historique.clear()
            self.view.textebox.insert('end', self.model.get_history())
            self.view.textebox.configure(state = "disabled")


        elif char == "(":
            if  self.actuel:
                pass
            elif self.expression and self.expression[-1].isdigit():
                pass
            else:
                self.expression.append('(') 
            self.view.set_display(''.join(self.expression))

        elif char == ")":
            if self.actuel or self.expression.count(')') < self.expression.count('('): 
                self.expression.append(self.actuel)
                self.expression.append(")")
                self.actuel = ""
                self.view.set_display(''.join(self.expression))
            else:
                pass

        # Functions that expect an argument: append function name and an
        # opening parenthesis so the model receives tokens like ['sin','(','0',')'].
        # We'll auto-close any unmatched parentheses before evaluation.
        elif char in ("sin", "cos", "tan", "log", "ln", "eˣ"):
            if self.actuel:
                self.expression.append(self.actuel)
                self.expression.append(' '+ 'x'+ ' ')
            # append function token and an explicit '('
            self.expression.append(char)
            self.expression.append("(")
            self.actuel = ""
            self.view.set_display(''.join(self.expression) )

        elif char == "xⁿ":
            if self.actuel:
                self.expression.append(self.actuel)
                self.expression.append("^")
            self.actuel = ""
            self.view.set_display(''.join(self.expression))
 
        elif char in ("√",):
            if self.actuel and self.actuel.isdigit():
                self.expression.append(self.actuel)
                self.expression.append('x')
                self.expression.append("√")
                self.expression.append("(")
                self.view.set_display(''.join(self.expression))

            if not self.actuel:
                self.expression.append("√")
                self.expression.append("(")
                self.view.set_display(''.join(self.expression))
           
        elif char=="%":
            if self.actuel.isdigit and self.actuel != "":
                self.expression.append(self.actuel)
                self.expression.append("%")
                self.actuel=""
                self.view.set_display(''.join(self.expression))
            else:
                pass

        elif char == 'π':
            self.expression.append('π')
            self.actuel=""
            self.view.set_display(''.join(self.expression))

        elif char == '⏱':
            data = self.model.get_history()
            if self.view.fonction_fenetre.winfo_ismapped():
                self.view.arrangement_fenetre('tout')
                self.view.history_fonction_fenetre(data)
            else:
                self.view.arrangement_fenetre('calc+history')
                self.view.history_fenetre_fonc( data)
               
        elif char == "EFF":
            if self.view.fonction_fenetre.winfo_ismapped():
                self.view.arrangement_fenetre('calc+fonction')
                self.view.fonction_fenetre_fonc()
            else:
                self.view.arrangement_fenetre('calc')
            

        elif char == "←":
            data = self.model.get_history()
            if self.view.history_fenetre.winfo_ismapped():
                self.view.arrangement_fenetre('tout')
                self.view.history_fonction_fenetre(data)
            else:
                self.view.arrangement_fenetre('calc+fonction')
                self.view.fonction_fenetre_fonc()

        elif char == "→":
            data = self.model.get_history()
            if self.view.history_fenetre.winfo_ismapped():
                self.view.arrangement_fenetre('calc+history')
                self.view.history_fenetre_fonc(data)
            else:
                self.view.arrangement_fenetre('calc')
        
            

        elif char == "e":
            if self.actuel:
                self.expression.append(self.actuel)
                self.expression.append('x')
            self.expression.append("e")
            self.actuel = ""
            self.view.set_display(''.join(self.expression))


        elif char == '³√':
            if self.actuel:
                self.expression.append('³√(')
                self.expression.append(self.actuel)
                self.expression.append(')')
                self.actuel=""
            else:
                self.expression.append("³√")
                self.expression.append("(") 
            self.view.set_display(''.join(self.expression))

        elif char == '±':
            if self.actuel:
                self.actuel = self.model.nbre_contraire(self.actuel)
                self.view.set_display(''.join(self.expression)+ self.actuel)
            
        elif char == '1/x':
            if self.actuel:
                self.expression.append("1/")
                self.expression.append(self.actuel)
            self.actuel = ""
            self.view.set_display(''.join(self.expression))

        elif char == '10ˣ':
            if self.actuel:
                self.expression.append(self.actuel)
                self.expression.append(' '+ "x"+ ' ')
                self.expression.append('10^')
            self.actuel = ""
            self.view.set_display(''.join(self.expression))

        elif char == '|x|':
            if self.actuel:
                self.expression.append('abs(')
                self.expression.append(self.actuel)
                self.expression.append(")")
            self.actuel = ""
            self.view.set_display(''.join(self.expression))  

        elif char == 'x²':
            if self.actuel:
                self.expression.append(self.actuel)
                self.expression.append("^2")
            self.actuel = ""
            self.view.set_display(''.join(self.expression))

        elif char == 'x³':
            if self.actuel:
                self.expression.append(self.actuel)
                self.expression.append("^3")
            self.actuel = ""
            self.view.set_display(''.join(self.expression))

        elif char == "MOD":
            if self.actuel:
                self.expression.append(self.actuel)
                try:
                    result=self.model.string_mod(self.expression)
                    self.view.set_display(result)
                    self.expression=[]
                    self.actuel=result
                    
                except:
                    self.view.set_display("Error")            
                    self.expression=[]
                    self.actuel="" 

                finally:
                    self.view.display.configure(state="disabled")
            else: 
                pass

        # Before evaluation, auto-close any unmatched '(' tokens so expressions
        # like ['sin','(','0'] become ['sin','(','0',')'] for the model.
        elif char == "=":
            if self.actuel:
                self.expression.append(self.actuel)
            elif self.actuel in ["Error", "IMPAIR", "PAIR"]:
                pass

            # auto-close parentheses
            open_count = self.expression.count('(')
            close_count = self.expression.count(')')

            while close_count < open_count:
                self.expression.append(')')
                close_count += 1

            try:
                result=self.model.calculate(self.expression)
                self.view.set_display(result)
                self.model.history(self.expression, result)
                self.actuel=result
                self.expression = []
            except:
                self.view.set_display("Error")
                self.view.display.configure(state = "disabled")
                self.expression=[]
                self.actuel=""

            finally:
                if self.view.history_fenetre.winfo_ismapped():
                    self.view.textebox.configure(state = "normal")
                    self.view.textebox.delete('1.0', "end")
                    self.view.textebox.insert('end', self.model.get_history())
                    self.view.textebox.configure(state = "disabled")
                else: pass


    
        
            
            
          
               
    
   
     