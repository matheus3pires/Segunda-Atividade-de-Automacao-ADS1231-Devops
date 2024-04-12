# Segunda Atividade de Automação.
Este código é um simples programa de gerenciamento de clientes em Python. Ele permite adicionar novos clientes, visualizar todos os clientes cadastrados e buscar um cliente específico por nome. Os dados dos clientes são armazenados em um arquivo CSV (clientes.csv).

## Funcionalidades
- Adicionar Cliente: Permite adicionar um novo cliente fornecendo seu nome, e-mail e telefone.
- Visualizar Clientes: Exibe todos os clientes cadastrados com seus respectivos nomes, e-mails e telefones.
- Buscar Cliente: Permite buscar um cliente específico pelo nome e exibe suas informações se encontrado.
- Encerrar Programa: Encerra a execução do programa.

## Estrutura do Arquivo CSV (clientes.csv)
O arquivo CSV utilizado para armazenar os dados dos clientes segue o seguinte formato:
| Nome   | Email       | Telefone                           |
| :---------- | :--------- | :---------------------------------- |

Cada linha subsequente no arquivo contém as informações de um cliente, separadas por vírgula, na ordem: nome, e-mail e telefone.

## Instruções de Uso Docker
1. Navegue para o Diretório do Projeto.
2. Construa a Imagem Docker:
   
        docker build -t segunda-atividade . 
       
3. Execute o Container Docker:
   
        docker run -it segunda-atividade 
       
4. Interaja com o programa:
   * Uma vez que o container esteja em execução, você poderá interagir com o programa Python usando o terminal. Siga as instruções no console para usar os recursos do programa de gerenciamento de clientes.
  
 ![imagem](https://github.com/matheus3pires/Segunda-Atividade-de-Automacao-ADS1231-Devops/assets/87993331/399ed993-4490-4544-8f3d-996d2600d625)


## Print de execução

![Anotação 2024-03-26 145644](https://github.com/matheus3pires/Segunda-Atividade-de-Automacao-ADS1231-Devops/assets/87993331/13c36a70-40fa-41ae-b699-78919fd1a75a)
![Anotação 2024-03-26 145807](https://github.com/matheus3pires/Segunda-Atividade-de-Automacao-ADS1231-Devops/assets/87993331/d09cbafe-404d-4527-a33f-8ddef8dd6cd9)

## Minhas Redes
Fique conectado para mais novidades e atualizações. Não hesite em entrar em contato!
 
- Linkedin: [linkedin.com/in/matheuspiress](https://www.linkedin.com/in/matheuspiress/)
