aparelho = input("Digite o nome do seu aparelho (ex.:Geladeira): ")

potencia = int(input(f"Digite a potencia do(a) {aparelho} em watts (W): "))

horasDia = float(input(f"DItige o tempo médio de uso diário do(a) {aparelho} em horas: "))

consumoMensal = (potencia * horasDia * 30) / 1000

print("-" * 40)
print(f"O consumo mensal do(a) {aparelho} é de: {consumoMensal:.2f} kWh")
print("-" * 40)
