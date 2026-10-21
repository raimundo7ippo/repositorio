class CPU:
    def __init__(self):
        self.registradores = {"R0": 0, "R1": 0, "R2": 0, "R3": 0}
        self.memoria = [0] * 16
        self.pc = 0
        self.halted = False

    def limitar_8bits(self, valor):
        return valor & 0xFF

    def ula(self, operacao, a, b):
        if operacao == "ADD":
            resultado = a + b
        elif operacao == "SUB":
            resultado = a - b
        elif operacao == "AND":
            resultado = a & b
        elif operacao == "OR":
            resultado = a | b
        elif operacao == "XOR":
            resultado = a ^ b
        else:
            raise ValueError("Operação da ULA inválida")
        return self.limitar_8bits(resultado)

    def executar_instrucao(self, instrucao):
        if not instrucao or isinstance(instrucao, int): 
            return
            
        partes = instrucao.replace(",", "").split()
        operacao = partes[0]

        if operacao == "LOAD":
            registrador = partes[1]
            valor = int(partes[2])
            self.registradores[registrador] = self.limitar_8bits(valor)
            self.pc += 1

        elif operacao == "STORE":
            registrador = partes[1]
            endereco = int(partes[2])
            self.memoria[endereco] = self.registradores[registrador]
            self.pc += 1

        elif operacao in ["ADD", "SUB", "AND", "OR", "XOR"]:
            reg_dest = partes[1]
            reg_orig = partes[2]
            resultado = self.ula(operacao, self.registradores[reg_dest], self.registradores[reg_orig])
            self.registradores[reg_dest] = resultado
            self.pc += 1

        elif operacao == "JMP":
            endereco = int(partes[1])
            self.pc = endereco

        elif operacao == "HALT":
            self.halted = True

        else:
            raise ValueError(f"Instrução desconhecida: {operacao}")

    def ciclo(self):
        instrucao = self.memoria[self.pc]
        print("\n--------")
        print("PC:", self.pc)
        print("Instrução:", instrucao)
        self.executar_instrucao(instrucao)
        self.mostrar_estado()

    def executar(self):
        while not self.halted:
            self.ciclo()

    def mostrar_estado(self):
        print("Registradores:")
        for nome, valor in self.registradores.items():
            print(f"{nome} = {valor:02X} ({valor})")