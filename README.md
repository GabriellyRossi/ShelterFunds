ShelterFunds  -  Controle Financeiro de Abrigo Infantil
Este projeto foi desenvolvido para gerenciar receitas e despesas de um abrigo infantil, facilitando o controle de doações e gastos que não são cobertos pelo mantenedor da instituição. Ele oferece uma interface gráfica simples para entrada de dados e geração de relatórios financeiros com gráficos ilustrativos.

1. Introdução
O Controle Financeiro é uma ferramenta voltada para o gerenciamento de finanças em um abrigo infantil, com foco na administração de doações (receitas) e gastos (despesas) não cobertos pelo responsável legal da instituição. O projeto foi desenvolvido utilizando as linguagens e ferramentas Python, Tkinter (interface gráfica) e Pandas (manipulação de dados), e tem como objetivo oferecer uma solução simples, eficiente e visual para a gestão financeira.

Tecnologias Utilizadas:
Tkinter: Escolhido para a criação de uma interface gráfica simples e acessível ao usuário.
Pandas: Usado para a manipulação e análise de dados financeiros, como a criação de relatórios e gráficos.
2. Funcionalidades Principais
Entrada de Transações: O usuário pode registrar manualmente receitas (doações) e despesas, descrevendo cada transação e inserindo a data e valor correspondente. As despesas são tratadas como valores negativos.

Relatórios por Período: Gera relatórios financeiros que mostram a movimentação de receitas e despesas em um determinado período, apresentando o saldo final.

Gráfico de Pizza: Exibe um gráfico de pizza ilustrando a proporção entre receitas e despesas, facilitando a visualização da distribuição dos valores.

3. Exemplo de Uso
Adicionar Transações:

O usuário pode inserir transações de receitas (doações) ou despesas manualmente, preenchendo os campos de valor, data e descrição.
Exemplo de entrada de dados:
Receita: R$ 500,00 (Doação) em 22/09/2024.
Despesa: R$ 200,00 (Compra de Materiais) em 23/09/2024.
Gerar Relatório:

Ao clicar no botão de gerar relatório, o sistema exibirá um saldo acumulado no período desejado e apresentará um gráfico de pizza que discrimina receitas e despesas.
4. Capturas de Tela
Aqui estão algumas capturas da interface e funcionalidades do projeto:

Tela Principal com a opção de inserir transações:

Relatório Financeiro com Gráfico de Pizza:

(As capturas de tela estão salvas na pasta img/ dentro do repositório)

5. Organização do Repositório
src/: Contém o código-fonte do projeto, incluindo a lógica para manipulação de dados e geração de relatórios.
img/: Contém as imagens (capturas de tela) utilizadas na documentação.
docs/: Contém a documentação do projeto (este arquivo README.md).
6. Dependências
Este projeto utiliza as seguintes bibliotecas Python, que precisam estar instaladas no seu ambiente:

tkinter: Para criar a interface gráfica do usuário.
pandas: Para manipulação e análise de dados financeiros.
As dependências podem ser instaladas com os seguintes comandos:

bash
Copiar código
pip install tkinter
pip install pandas

7. Licença (Opcional)
Este projeto utiliza a licença MIT. Veja o arquivo LICENSE para mais detalhes.
