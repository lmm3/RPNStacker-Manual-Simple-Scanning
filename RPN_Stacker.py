class Token():
    def __init__(self, lexeme, type):
        self.lexeme = lexeme
        self.type = type

    def __str__(self):
        return "Token [type=" + self.type + ", lexeme=" + self.lexeme + "]"


if __name__ == "__main__":
    stk = []
    with open('./Calc1.stk') as file:
        for line in file:
            lexeme = line.strip()
            if lexeme.isdigit():
                stk.append(Token(lexeme, "NUM"))
            elif lexeme in ['+', '-', '*', '/']:
                if lexeme == '+':
                    stk.append(Token(lexeme, "PLUS"))
                elif lexeme == '-':
                    stk.append(Token(lexeme, "MINUS"))
                elif lexeme == '*':
                    stk.append(Token(lexeme, "STAR"))
                elif lexeme == '/':
                    stk.append(Token(lexeme, "SLASH"))
            else:
                raise ValueError("Unexpected Character " + lexeme)
        for item in stk:
            print(str(item))
        
            

