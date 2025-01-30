# Tratamento de Faturas Duplicadas no DocBits

## Configuração para Habilitar o Tratamento de Faturas Duplicadas

Vá para _Configurações → Tipos de Documento → Fatura → Mais Configurações_ conforme mostrado na captura de tela abaixo

<figure><img src="../../.gitbook/assets/duplicate_invoice handling.png" alt=""><figcaption></figcaption></figure>

O usuário tem duas opções para detectar faturas duplicadas:

1. **Detecção de Documentos Duplicados**\
   Este recurso verifica documentos duplicados carregados no DocBits com base nos critérios selecionados. Se os critérios selecionados coincidirem entre os documentos, o sistema marcará o documento como duplicado.
2.  **Detecção de Faturas Duplicadas**\
    Este recurso requer que as Faturas de Fornecedores sejam sincronizadas do Infor para o DocBits. Ele compara os números das faturas no painel de faturas do DocBits com aqueles no Infor. Se o mesmo número de fatura for carregado mais de uma vez, ele será marcado como duplicado.

    <mark style="color:red;">**NOTA**</mark><mark style="color:red;">:</mark> Usar o recurso **Detecção de Faturas Duplicadas** resultará em uma cobrança adicional de crédito.

Uma vez que a configuração esteja ativada, o usuário pode selecionar os critérios para a detecção de duplicatas.

## Faturas Duplicadas no Painel

Uma vez que a Detecção de Duplicatas esteja habilitada nas configurações, o painel exibirá um ícone para quaisquer faturas identificadas como duplicadas com base nos critérios especificados. Clicar neste ícone abrirá os registros duplicados em uma visualização de tela dividida para fácil comparação.

<figure><img src="../../.gitbook/assets/duplicate_invoice handling2.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/duplicate_invoice handling2b.png" alt=""><figcaption></figcaption></figure>

Quando o usuário abre o documento, uma barra de aviso é exibida para as faturas duplicadas, conforme mostrado na captura de tela.

<figure><img src="../../.gitbook/assets/duplicate_invoice handling3.png" alt=""><figcaption></figcaption></figure>
