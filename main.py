"""
MAIN — Programa Customizado
AOC 2026.2
"""

from cpu import CPU

cpu = CPU()

# ==========================================
# PROGRAMA CUSTOMIZADO
# ==========================================
# 1. Carrega 15 no R0
# 2. Carrega 10 no R1
# 3. Soma R1 ao R0 (R0 = 25)
# 4. Guarda o 25 na posição 14 da memória
# 5. Carrega 5 no R2
# 6. Subtrai R2 do R0 (R0 = 20)
# 7. Guarda o 20 na posição 15 da memória
# 8. Para a execução

cpu.memoria[0] = "LOAD R0, 15"
cpu.memoria[1] = "LOAD R1, 10"
cpu.memoria[2] = "ADD R0, R1"
cpu.memoria[3] = "STORE R0, 14"
cpu.memoria[4] = "LOAD R2, 5"
cpu.memoria[5] = "SUB R0, R2"
cpu.memoria[6] = "STORE R0, 15"
cpu.memoria[7] = "HALT"

print("======================================")
print("       CPU SIMULADA — 8 BITS")
print("======================================")

cpu.executar()

print("\n======================================")
print("RESULTADO FINAL NA MEMÓRIA")
print("======================================")
print(f"Memória [14]: {cpu.memoria[14]}")
print(f"Memória [15]: {cpu.memoria[15]}")