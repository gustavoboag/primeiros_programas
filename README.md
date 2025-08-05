# LOGICA DE PROGRAMAÇÃO 



# Como Executar um Arquivo .sh
cd /caminho/para/seu/script

# 2. Dê permissão de execução ao script (se necessário)
chmod +x calculadora.sh

# Forma 1 – Usando ./
./calculadora.sh

# Forma 2 – Usando bash
bash nome_do_arquivo.sh

# Exemplo completo
cd ~/meus_scripts
chmod +x iniciar_calculadora.sh
./iniciar_calculadora.sh

## execute o script python_script.sh caso não tenha python





# explicação sobre o funcionamento do seu script "calculadora.py"


A entrada dos dados é feita utilizando a função input():

O usuário escolhe a operação desejada digitando seu nome completo (ex: "soma", "divisão", etc.).
O usuário digita dois números reais (float), que serão utilizados na operação matemática.


calculadora simples
as operações são: soma, subtração, multiplicação, divisão e resto da divisão
digite a operação que deseja realizar
por exemplo
digita :soma<br>
digite o primeiro numero: 5<br>
digite o segundo numero: 3<br>
o resultado da soma dos dois numeros são: 8.0<br>

 




# Lógica de Decisão
A lógica principal do script usa estruturas condicionais if, elif e else para verificar qual operação foi escolhida

if operacao == "soma":
    # soma os dois números
elif operacao == "subtração":
    # subtrai os dois números
...
else:
    # operação inválida





