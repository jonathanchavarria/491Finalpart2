# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.

def main():
    eq = '8-4'
    return (eq + '=' + Helper.integration(eq))

class Calculations:
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mult(x, y):
        return x * y

    def div(x, y):
        return int(x/y)

    def exp(x,y):
        return x ** y

class Helper:
    def find_all_operations(eq):
        lst = []
        for pos,char in enumerate(eq):
            if(char in ['+','-','/', '*']):
                lst.append(pos)
        return lst

    def integration(eq):
        eq = eq.replace(' ','')
        print(eq, "=")
        return Parser.recursiveadd(Parser.recursivemult(eq))

class Parser:
    def recursivemult(eq):
        md = ["/", "*"]                     
        op_pos = Helper.find_all_operations(eq)
        if not any(x in eq for x in md):
            return eq
        else:
            for pos, val in enumerate(eq):  
                if val == '/' or val == '*':
                    if(op_pos.index(pos) == 0 and len(op_pos)==1):
                        x = int(eq[:pos])
                        y = int(eq[pos+1:])
                    elif (op_pos.index(pos) == 0 and len(op_pos)!=1):
                        x = int(eq[:pos])
                        y = int(eq[pos+1:op_pos[op_pos.index(pos)+1]])
                    elif (op_pos.index(pos) == op_pos.index(op_pos[-1])):
                        x = int(eq[op_pos[op_pos.index(pos)-1]+1:pos])
                        y = int(eq[pos+1:])
                    else:
                        x = int(eq[op_pos[op_pos.index(pos)-1]:pos])
                        y = int(eq[pos+1:op_pos[op_pos.index(pos)+1]])

                    if val == '*':
                        if(op_pos.index(pos) == 0 and len(op_pos)==1):
                            eq = eq.replace(eq[:], str(Calculations.mult(x,y)))
                        elif (op_pos.index(pos) == 0 and len(op_pos)!=1):
                            eq = eq.replace(eq[:op_pos[op_pos.index(pos)+1]], str(Calculations.mult(x,y)))   
                        elif (op_pos.index(pos) == op_pos.index(op_pos[-1])):
                           eq = eq.replace(eq[op_pos[op_pos.index(pos)-1]+1:], str(Calculations.mult(x,y)))
                        else:
                            eq = eq.replace(eq[op_pos[op_pos.index(pos)-1]+1:op_pos[op_pos.index(pos)+1]], str(Calculations.mult(x,y)))
                    elif val == '/':
                        if(op_pos.index(pos) == 0 and len(op_pos)==1):
                            eq = eq.replace(eq[:], str(Calculations.div(x,y)))
                        elif (op_pos.index(pos) == 0 and len(op_pos)!=1):
                            eq = eq.replace(eq[:op_pos[op_pos.index(pos)+1]], str(Calculations.div(x,y)))
                        elif (op_pos.index(pos) == op_pos.index(op_pos[-1])):
                           eq = eq.replace(eq[op_pos[op_pos.index(pos)-1]+1:], str(Calculations.div(x,y)))
                        else:
                            eq = eq.replace(eq[op_pos[op_pos.index(pos)-1]+1:op_pos[op_pos.index(pos)+1]], str(Calculations.div(x,y)))

                    return Parser.recursivemult(eq)

    def recursiveadd(eq):
        ad = ["+", "-"]
        op_pos = Helper.find_all_operations(eq)
        if not any(x in eq for x in ad):
            return eq
        else:
            for pos, val in enumerate(eq): 
                if pos == 0 and val == '-':
                    raise Exception("Sorry, this produced a negative number! Not what this calculator is for!") 
                if val == '+' or val == '-':
                    if(op_pos.index(pos) == 0 and len(op_pos)==1):
                        x = int(eq[:pos])
                        y = int(eq[pos+1:])
                    elif (op_pos.index(pos) == 0 and len(op_pos)!=1):
                        x = int(eq[:pos])
                        y = int(eq[pos+1:op_pos[op_pos.index(pos)+1]])
                    elif (op_pos.index(pos) == op_pos.index(op_pos[-1])):
                        x = int(eq[op_pos[op_pos.index(pos)-1]+1:pos])
                        y = int(eq[pos+1:])
                    else:
                        x = int(eq[op_pos[op_pos.index(pos)-1]:pos])
                        y = int(eq[pos+1:op_pos[op_pos.index(pos)+1]])
                    if val == '+':
                        if(op_pos.index(pos) == 0 and len(op_pos)==1):
                            eq = eq.replace(eq[:], str(Calculations.add(x,y)))
                        elif (op_pos.index(pos) == 0 and len(op_pos)!=1):
                            eq = eq.replace(eq[:op_pos[op_pos.index(pos)+1]], str(Calculations.add(x,y)))
                        else:
                            eq = eq.replace(eq[op_pos[op_pos.index(pos)-1]+1:op_pos[op_pos.index(pos)+1]], str(Calculations.add(x,y)))
                    elif val == '-':
                        if(op_pos.index(pos) == 0 and len(op_pos)==1):
                            eq = eq.replace(eq[:], str(Calculations.sub(x,y)))
                        elif (op_pos.index(pos) == 0 and len(op_pos)!=1):
                            eq = eq.replace(eq[:op_pos[op_pos.index(pos)+1]], str(Calculations.sub(x,y)))
                        else:
                            eq = eq.replace(eq[op_pos[op_pos.index(pos)-1]+1:op_pos[op_pos.index(pos)+1]], str(Calculations.sub(x,y)))
                    return Parser.recursiveadd(eq)


# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
