aparelho = input("Digite o nome do seu aparelho (ex:.Geladeira): ")
potencia = int(input(f"Digite a potêcia do(a) {aparelho} em watts (W):"))
horasDia = float(input(f"Digite o tempo médio de uso diário do(a) {aparelho} em horas: "))
consumoMensal = (potencia * horasDia * 30) / 1000
custoEstimado = (consumoMensal * 0.75)
 
print("-" * 50)
print(f"O consumo mensal do(a) {aparelho} é de: {consumoMensal:.2f} kWh")
print(f"O custo estimado mensal é de: R$ {custoEstimado:.2f}")
print("-" * 50)
