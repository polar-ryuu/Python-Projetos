import random

# 1. Criar jogadores
players = []
memories = {}

num_players = int(input("How many players? "))

for i in range(num_players):
    name = input(f"Player {i+1} name: ")
    players.append(name)

# 2. Cada jogador escolhe uma memória
for player in players:
    memory = input(f"{player}, write a memory (secret): ")
    memories[player] = memory

# 3. Embaralhar memórias
memory_list = list(memories.values())
random.shuffle(memory_list)

# Garantir que ninguém receba a própria memória
assignments = {}

for player in players:
    for mem in memory_list:
        if mem != memories[player]:
            assignments[player] = mem
            memory_list.remove(mem)
            break

# 4. Fase de descoberta
print("\n--- DISCOVERY PHASE ---\n")

for player in players:
    print(f"{player}, your memory to discover is:")
    print("👉", assignments[player])

    guess = input("Who does this memory belong to? ")

    if guess in memories and memories[guess] == assignments[player]:
        print("✅ Correct!\n")
    else:
        print("❌ Wrong.\n")