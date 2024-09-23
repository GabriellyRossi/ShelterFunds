import tkinter as tk 
#biblioteca para interface gráfica GUI

from tkinter import ttk, messagebox
#módulo adicional do tkinter pra widgets avançados - não é o tk

import pandas as pd
#biblioteca de dados e dataframes

import matplotlib.pyplot as plt
#gráfico pizza aqui! 



# onde está o arquivo CSV da função financeira
arquivo_csv = "transacoes.csv"

# def é para definir Função que carrega o arquivo CSV e o pd pra carregar o arquivo se existir ou retorna vazio
def carregar_dados():
    try:
        df = pd.read_csv(arquivo_csv, parse_dates=['Data']) #lê os dados data
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Data', 'Tipo', 'Valor', 'Descrição']) #se não encontrar, faz um dataframe vazio  
    return df


# função carregar dados inicializa o dataframe e ve se o arquivo existe, carrega os dados ou cria um dataframe vazio
df = carregar_dados()


# Função para incuir, processar ou adc nova transação 
def inserir_transacao():
    try:
        #docs pandas converte a data pra formato datetime
        data = pd.to_datetime(data_entry.get(), format='%d/%m/%Y')
       
        #se é receita ou despesa
        tipo = tipo_combobox.get()
        valor = float(valor_entry.get().replace(',', '.')) #valor com vírgula e 2 casas - testar, ta estranho
        descricao = descricao_entry.get()

        if tipo == 'Despesas': #saída de valor, tem que ser negativo 
            valor = -valor

        #nova trasnação novo dataframe
        nova_transacao = pd.DataFrame({'Data': [data], 'Tipo': [tipo], 'Valor': [valor], 'Descrição': [descricao]})
        global df

        #adc nova transação em dataframe já exist ver doc uso de pd.concat para combar dataframes
        df = pd.concat([df, nova_transacao], ignore_index=True)
       
        #salva o dataframe atualizado de volta no csv
        df.to_csv(arquivo_csv, index=False)

        atualizar_lista_transacoes()
        limpar_campos()


    #msg de erro - ver docs tkinter messagebox.showerror
    except ValueError:
        messagebox.showerror("Algo não deu certo", "Confira a data, o valor ou outros campos.")

# função reiniciar limpa os campos de entrada após a transação
def limpar_campos():
    #ver docs Tkinter Entry widget 'delete()' method ou a 'Entry.delete()' method 
    data_entry.delete(0, tk.END)
    valor_entry.delete(0, tk.END)
    descricao_entry.delete(0, tk.END)

# Função q atualiza a lista de transações e exibe saldo
def atualizar_lista_transacoes():
    lista_transacoes.delete(0, tk.END)
    for _, transacao in df.iterrows():
        lista_transacoes.insert(tk.END, f"{transacao['Data'].strftime('%d/%m/%Y')} - {transacao['Tipo']} - R$ {transacao['Valor']:,.2f} - {transacao['Descrição']}")
    
    #atualiza saldo na label
    saldo = df['Valor'].sum()
    saldo_label.config(text=f"Saldo: R$ {saldo:,.2f}".replace('.', ','))

# Função apaga a transação SELECIONADA atualiza cvs e interface
def apagar_transacao():
    selecionado = lista_transacoes.curselection()
    if selecionado:
        index = selecionado[0]
        global df
        df = df.drop(df.index[index])
        df.to_csv(arquivo_csv, index=False)
        atualizar_lista_transacoes()
        #passouaq

        # Função para gerar o relatório de pizza (proporção receitas e despesas)
def gerar_relatorio():
    try:
        global df
        valores = df.groupby('Tipo')['Valor'].sum() #grup valores por tipo ver dosc pandas groupby e sum

        # Verificar se há valores negativos (para despesas)
        if any(valores < 0):
            valores = valores.abs()  # Tomar o valor absoluto para o gráfico de pizza

        cores = {'Receitas': 'green', 'Despesas': 'red'}
        plt.pie(valores, labels=valores.index, autopct='%1.1f%%', startangle=90, colors=[cores.get(tipo, 'gray') for tipo in valores.index])
        plt.axis('equal')
        plt.title("Distribuição de Receitas e Despesas")
        plt.show() #grafico de pizza pronto mostra

    except ValueError as e:
        messagebox.showerror("Erro ao gerar relatório", str(e))


#janela principal tkinter
root = tk.Tk()
root.title("Controle Financeiro")
root.geometry('500x500')

#labels e campos de entrada data
tk.Label(root, text="Data (dd/mm/yyyy):").grid(row=0, column=0, padx=5, pady=5, sticky='w')
data_entry = tk.Entry(root)
data_entry.grid(row=0, column=1, padx=5, pady=5, sticky='we')

#label e combobox pra escolher receita ou despesa
tk.Label(root, text="Tipo:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
tipo_combobox = ttk.Combobox(root, values=['Receitas', 'Despesas'])
tipo_combobox.grid(row=1, column=1, padx=5, pady=5, sticky='we')

#label e campo de imput texto valor
tk.Label(root, text="Valor (R$):").grid(row=2, column=0, padx=5, pady=5, sticky='w')
valor_entry = tk.Entry(root)
valor_entry.grid(row=2, column=1, padx=5, pady=5, sticky='we')

#label e input descrição da transaçaõ
tk.Label(root, text="Descrição:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
descricao_entry = tk.Entry(root)
descricao_entry.grid(row=3, column=1, padx=5, pady=5, sticky='we')

# Botões
tk.Button(root, text="Inserir Transação", command=inserir_transacao).grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky='we')
tk.Button(root, text="Gerar Relatório", command=gerar_relatorio).grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky='we')
tk.Button(root, text="Apagar Transação", command=apagar_transacao).grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky='we')

# Lista transações e exibe
lista_transacoes = tk.Listbox(root)
lista_transacoes.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky='we')

# Exibe saldo atualizado
saldo_label = tk.Label(root, text="Saldo: R$ 0,00", font=('Arial', 14))
saldo_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky='we')

# chama a função q atualiza a lista de transações já salvas e config a interface 
atualizar_lista_transacoes()

# Ajustar tamanho da coluna
root.grid_columnconfigure(1, weight=1)

#loop principal permite interação do user 
root.mainloop()

#test12passou