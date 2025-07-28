# Treinamento de Campos de Linha/Tabela de Treinamento

## Tabela de Treinamento: Quando e Como Usar

O DocBits utiliza extração de tabela baseada em IA por padrão, que funciona em todos os fornecedores. No entanto, quando você precisa de mais controle sobre como os itens de linha são extraídos para um fornecedor específico, você pode usar o **Treinamento de Tabela** para definir a estrutura manualmente.

#### **Importante: Treinamento Específico do Fornecedor**

O treinamento de tabela é **específico para cada fornecedor**. Se você treinar um layout de tabela para um fornecedor, as regras se aplicarão apenas aos documentos desse fornecedor.\
Outros fornecedores continuarão a usar a extração de tabela baseada em IA, a menos que sejam treinados separadamente.

#### Quando Deve Usar o Treinamento de Tabela?

Use o Treinamento de Tabela **apenas quando o layout do documento for estável**, e você deseja garantir uma extração consistente e de alta qualidade. É mais adequado para fornecedores que:

* Utilizam um **formato de fatura fixo** ao longo do tempo.
* Exigem um **mapeamento preciso** dos itens de linha para campos específicos.
* São **fornecedores de alto volume**, onde a automação consistente é valiosa.

#### Quando Não Usar o Treinamento de Tabela

Evite usar o Treinamento de Tabela se:

* O fornecedor **altera frequentemente o layout de sua fatura** (por exemplo, a cada dois meses).
* Você não recebe documentos regularmente desse fornecedor.
* A extração baseada em IA padrão funciona **suficientemente bem** sem treinamento manual.

Em tais casos, re-treinar a tabela repetidamente seria ineficiente e demorado.

## Como Usar:

O **Modo de Treinamento** é usado para ensinar ao DocBits como extrair corretamente os itens de linha do layout de documento de um fornecedor específico.

Quando você está no Modo de Treinamento, você define:

* **Onde a tabela está localizada** no documento.
* **Quais áreas correspondem a cada coluna** (por exemplo, Quantidade, Descrição, Preço Unitário).

Este modo cria um **modelo de extração reutilizável** para esse fornecedor, então documentos futuros com o mesmo layout serão processados automaticamente — sem a necessidade de re-treinamento.

**Características Chave:**

* **As colunas mapeadas são somente leitura** — você não pode alterar manualmente o texto.
* Você **não pode adicionar ou excluir linhas**.
* O foco está em **mapear posições**, não em corrigir valores.
* Depois de terminar de mapear a tabela e suas colunas, clique em **“Salvar Regras”** para que o DocBits aprenda e aplique esse treinamento a documentos semelhantes do mesmo fornecedor.

O **Modo de Correção** permite que você **corrija erros de extração** nos dados da tabela para o documento atual. É usado quando o DocBits já tentou extrair a tabela, mas os resultados precisam de pequenas correções.

Use o Modo de Correção quando:

* Alguns **valores estão faltando ou desalinhados**.
* Uma **linha vazia ou duplicada** foi extraída e precisa ser removida.

**O Que Você Pode Fazer no Modo de Correção:**

* **Ajustar manualmente valores** nas colunas mapeadas (por exemplo, corrigir deslocamentos).
* **Excluir linhas** que não devem fazer parte da tabela.
* **Adicionar linhas** que foram completamente perdidas durante a extração.
