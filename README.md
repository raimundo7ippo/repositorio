# Trabalho Prático - CPU Simulada
AOC 2026.2

## Arquitetura
- CPU de 8 bits.
- Registradores: R0, R1, R2, R3 e PC.
- Memória de 16 posições.
- Operações suportadas: LOAD, STORE, ADD, SUB, AND, OR, XOR, JMP e HALT.
- Ciclo de execução: Fetch → Decode → Execute.

## Como executar
Para executar o programa customizado (que inclui LOAD, STORE e operações da ULA):
```bash
python main.py