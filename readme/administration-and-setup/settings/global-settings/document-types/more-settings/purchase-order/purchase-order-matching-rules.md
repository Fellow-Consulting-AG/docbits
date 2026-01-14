# Regras de Correspondência de Pedido de Compra

## Introdução: Pedidos de Compra e Gerenciamento de Regras de PO

A Correspondência de Pedido de Compra (PO) é um processo crítico para garantir a consistência entre os Pedidos de Compra (POs) e as faturas de entrada correspondentes ou recebimentos de mercadorias. Um conjunto robusto de regras é essencial para alcançar uma alta taxa de correspondência automática, prevenir fraudes e garantir pagamentos corretos.

Esta página de configuração é usada para definir e gerenciar as regras que determinam _como_ os itens de linha da PO são correspondidos ao documento de entrada correspondente (Fatura, Confirmação de Pedido)

***

## Como Acessar

1.  Navegue até **Configurações --> Configurações Globais --> Tipos de Documento**

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  Selecione o tipo de documento desejado e clique em **Mais Configurações**.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Em seguida, vá para a seção Pedido de Compra e clique no botão (PO match server side) e depois clique em Configurar Regras de Correspondência de PO

    <figure><img src="../../../../../../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Configurações Globais (Regras Base)

Estas configurações estabelecem a estrutura que se aplica a todas as regras de correspondência:

* **Configuração:** Corresponder Quantidade Em
  * **Objetivo:** Define qual campo de quantidade específico deve ser usado principalmente como ponto de referência para corresponder itens de linha de pedido de compra em todas as regras.
  * **Valores Válidos:** Quantidade ou outros campos de quantidade disponíveis no sistema, dependendo da estrutura de dados (por exemplo, um campo de quantidade normalizado alternativo).
  * **Dependência:** Determina a base para todas as regras de correspondência que incluem quantidade em seus critérios de comparação.
* **Configuração:** Tolerância Padrão (Tolerância Default)
  * **Objetivo:** Define o desvio percentual permitido na quantidade para que uma correspondência seja considerada válida. Ele compensa pequenos arredondamentos ou diferenças de quantidade.
  * **Valor Válido:** Um número decimal (por exemplo, 0,005 corresponde a 0,5%).
  * **Dependência:** Aplica-se a regras que usam campos de quantidade para correspondência e têm a opção "Permitir Tolerância" ativada.

***

## Lista de Regras

A Lista de Regras exibe todas as regras de correspondência disponíveis e gerencia sua ordem de execução.

#### Estrutura e Execução

* **Prioridade:** Este campo numérico (por exemplo, 1, 2, 3) dita a sequência de execução das regras. Regras com um número de prioridade menor são tentadas primeiro. Isso permite que os administradores estruturem uma hierarquia, normalmente começando com as regras mais específicas e rigorosas (por exemplo, correspondência por número de linha e número da peça) e recorrendo a regras mais amplas ou menos restritivas.
* **Nome e Descrição:** Fornece identificação clara e contexto para a regra, explicando os critérios primários usados (por exemplo, "Regra Padrão nº 1: Correspondência baseada em Número de Linha, ID da Peça e Quantidade").
* **Ativa:** Um simples interruptor que permite a ativação ou desativação instantânea da regra sem a necessidade de excluir sua configuração.

**Fluxo de Execução:** O sistema realiza a correspondência em uma sequência em cascata. Se uma regra (por exemplo, Prioridade 1) corresponder com sucesso a um item de linha, o processo para esse item para. Se nenhuma correspondência for encontrada, o sistema prossegue para a próxima regra na sequência de prioridade (por exemplo, Prioridade 2).

***

## Configuração da Regra (Configurações de Detalhe)

Esta área de configuração detalhada define a lógica e os critérios específicos para uma regra individual.

#### Parâmetros Base

* **Tipo de Regra (por exemplo, Correspondência Única):** Especifica a cardinalidade da correspondência. Correspondência Única (Single Match) é o tipo comum, exigindo uma correspondência um-para-um (uma linha de PO para uma linha de Fatura). Outros tipos podem incluir correspondências muitos-para-um ou um-para-muitos para itens agregados ou entregas divididas.
* **Correspondência Automática:** Se ativado, o sistema tentará aplicar esta regra inteiramente de forma automática. É necessária alta confiança nos critérios para o processamento automático.
* **Correspondência Manual:** Se ativado, esta regra pode ser apresentada ou aplicada por um usuário durante a etapa de reconciliação manual, oferecendo a ele um conjunto predefinido de critérios de comparação para resolver exceções.

#### Comparação de Colunas (Critérios de Correspondência)

Esta é a definição central da lógica da regra, especificando quais campos devem se alinhar entre os documentos.

1. Definindo as Colunas para Comparar:
   * **Colunas de PO:** O campo extraído dos dados do Pedido de Compra (por exemplo, número da linha).
   * **Colunas de Tabela Extraídas:** O campo correspondente extraído ou analisado do documento de entrada (Fatura/Confirmação de Pedido) (por exemplo, `POSITION`).
2. **Tipo de Comparação:** Define a natureza da correspondência necessária (por exemplo, Tt para comparação de Texto/String, exigindo uma correspondência exata caractere por caractere; # para comparação Numérica).
3. **Permitir Tolerância:** Para campos numéricos (quantidade, preço), a ativação desta opção instrui o sistema a aplicar a Tolerância Padrão Global definida anteriormente. Se isso _não_ estiver ativado para un campo numérico, os valores devem corresponder exatamente.
4. **Ignorar na Correspondência Manual:** Se marcado, este critério é relaxado durante a intervenção manual. Isso é útil para campos como descrições ou referências internas que podem variar ligeiramente, permitindo que o usuário ignore pequenas incompatibilidades não críticas.

**Exemplo: Regra de Correspondência de PO Rigorosa (`DefaultRule#1`)**

Uma regra rigorosa típica combina verificações de identidade obrigatórias com verificações de valor:

* **Identidade Obrigatória:** O Número da Linha e o Identificador do Item devem corresponder exatamente (comparação de texto, sem tolerância).
* **Verificações de Valor:** A Quantidade Normalizada Efetiva e o Preço Unitário Normalizado Efetivo devem corresponder (comparação numérica, tolerância permitida). Somente se todos os quatro critérios forem atendidos (com tolerância para valores) uma correspondência automática é executada.

***

## Impacto no Processo de Correspondência de PO

O conjunto de regras definido governa diretamente a eficiência e a integridade do fluxo de trabalho de correspondência de PO:

* **Priorização e Fallbacks:** A Prioridade definida garante que o sistema tente primeiro o método de correspondência mais confiável. Se as regras rigorosas e de alta prioridade falharem, o sistema recorre a regras mais amplas, visando minimizar o número de exceções encaminhadas aos usuários.
* **Controlando a Qualidade da Correspondência:** Regras mais rígidas (exigindo correspondências mais exatas e menos tolerância) resultam em menos correspondências automáticas, porém altamente confiáveis. Regras mais flexíveis aumentam a taxa de correspondência automática, mas elevam o risco de falsos positivos.
* **Tratamento de Exceções (Correspondência Manual):** Ao ativar regras para Correspondência Manual, o sistema fornece opções estruturadas para os usuários. Se uma transação falhar nos critérios de correspondência automática, ela se torna uma exceção. O usuário pode então tentar resolver a exceção aplicando uma regra manual predefinida, que pode ter critérios relaxados (por exemplo, ignorar uma pequena incompatibilidade de texto conforme a configuração "Ignorar na Correspondência Manual").

***

## Personalizar as Regras de Correspondência de PO

Para editar as regras de correspondência de PO, a versão padrão pode ser clonada clicando em **"Configurar Versionamento"** e usando a opção **"Clonar como Rascunho"** das opções de cartões disponíveis

<figure><img src="../../../../../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>
