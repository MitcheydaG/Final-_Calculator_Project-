import math as m # importation de la bibliotheque mathematique comme "m" pour faciliter son usage

string = ""

class CalculatorModel: #creation de la classe du model de la calculatrice pour mettre la logique de calcul et les fonctions de calcul

    def __init__(self):
        self.historique = []
        
    def calculate(self, liste_expression): #fonction pour calculer le resultat des calculs de l'utilisateur en prenant une liste d'expression "expression_list" comme argument qui stocke les nombres et les opérateurs de l'expression à calculer
        # Build a safe expression string from a token list and evaluate using
        # the math module. The previous implementation attempted to cast
        # operator strings to float and had incorrect branching which caused
        # crashes. This implementation maps known tokens to Python/math
        # equivalents and falls back to a simple eval for arithmetic.
        
        if not liste_expression:
            return ""

        # Map some tokens to Python equivalents
        mapped = []
        for tok in liste_expression:
            if tok == ' x ':
                mapped.append('*')
            elif tok == 'π' :
                mapped.append(str(m.pi))
            elif tok == 'e':
                mapped.append(str(m.e))
               
            elif tok == "%":
                if mapped:
                    mapped[-1] = f'{mapped[-1]}/100'
            else:
                mapped.append(tok)

        expr = ''.join(mapped)

        # Replace function names with math module equivalents so eval can use them
        expr = expr.replace('sin', 'm.sin')
        expr = expr.replace('cos', 'm.cos')
        expr = expr.replace('tan', 'm.tan')
        expr = expr.replace('log', 'm.log10')
        expr = expr.replace('ln', 'm.log')
        expr = expr.replace('³√', 'm.cbrt')
        expr = expr.replace('√', 'm.sqrt')
        expr = expr.replace('eˣ', 'm.exp')
        expr = expr.replace(")(", ")*(")
        expr = expr.replace(").(", ")*(")
        expr = expr.replace("^", "**")
        
        
        try:
            # Evaluate with a restricted global namespace exposing only math
            result = eval(expr, {"__builtins__": None, 'm': m, 'abs': abs})

        except Exception:
            # If evaluation fails, return an error string like the UI expects
            return "Error"

        
        return str(round(result, 8))
    
    def string_mod(self, liste_expression):
        mapp = liste_expression

        if int(mapp[-1]) % 2 == 0:
            string = "PAIR"
        else:
            string = "IMPAIR"
        return string 
    
    def history(self, expression, resultat):
        if resultat in ["Error", "IMPAIR", "PAIR"]:
            pass
        else:
            expression = ''.join(expression)
            if expression:
                history = f"{expression} = {resultat}"
            else: pass
        self.historique.append(''.join(history))
       

    def get_history(self):     
        return '\n'.join(self.historique)
    
    def clear_historique(self):
        self.historique.clear()

    def nbre_contraire(self, nombre):
        try:
            nombre = float(nombre) * -1
        except:
            return "Error"
        
        if nombre.is_integer():
            nombre = int(nombre)

        return str(nombre)
        




    

        

        


    
  
