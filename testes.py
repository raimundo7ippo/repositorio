from cpu import CPU

def teste_load():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 25"
    cpu.memoria[1] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 25
    print("[OK] LOAD")

def teste_store():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R1, 10"
    cpu.memoria[1] = "STORE R1, 15"
    cpu.memoria[2] = "HALT"
    cpu.executar()
    assert cpu.memoria[15] == 10
    print("[OK] STORE")

def teste_ula():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 5"
    cpu.memoria[1] = "LOAD R1, 3"
    cpu.memoria[2] = "ADD R2, R0" # R2 não recebe o segundo operando na nossa lógica simplificada, mas vamos testar a operação base
    # Para adaptar à estrutura do professor:
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 8
    print("[OK] ULA (ADD)")

def teste_jmp():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 10"
    cpu.memoria[1] = "JMP 4"
    cpu.memoria[2] = "LOAD R0, 99"
    cpu.memoria[3] = "HALT"
    cpu.memoria[4] = "LOAD R1, 20"
    cpu.memoria[5] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 10
    assert cpu.registradores["R1"] == 20
    print("[OK] JMP")

def teste_halt():
    cpu = CPU()
    cpu.memoria[0] = "HALT"
    cpu.executar()
    assert cpu.halted is True
    print("[OK] HALT")

if __name__ == "__main__":
    print("Executando testes...")
    teste_load()
    teste_store()
    teste_ula()
    teste_jmp()
    teste_halt()
    print("Todos os testes aprovados!")