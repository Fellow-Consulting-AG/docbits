# Configuração de Dados Fuzzy com Dados Mestres

## **Visão Geral**

Cada tipo de documento possui suas próprias configurações padrão e deve ser configurado separadamente. Enquanto este exemplo explica a configuração para **Faturas**, o mesmo processo se aplica a todos os tipos de documentos.

## Para configurar Dados Fuzzy, navegue até:

Configurações → Configurações Globais → Tipos de Documento → Fatura → Campos → Configurações de Dados Mestres → Consultar Dados Mestres

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fhnn2NcPGzVkUO0mLQWTy%252Fimage.png%3Falt%3Dmedia%26token%3De2f87385-fc48-4149-9bef-ca917a7328bd\&width=768\&dpr=4\&quality=100\&sign=116ee1da\&sv=2)

## **Consultas Padrão**

Existem **quatro grupos de consulta padrão** para faturas:

1. **Dados da Empresa**
2. **Cabeçalho do Pedido de Compra**
3. **Fornecedor**
4. **Código de Imposto**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4VxYFu8M62dXi6qGsPl3%252Fimage.png%3Falt%3Dmedia%26token%3Db2bc4690-805b-4b19-aa89-73f315889d88\&width=768\&dpr=4\&quality=100\&sign=835f513a\&sv=2)

Cada grupo contém campos específicos. Clique em um grupo para **expandir** e visualizar os campos. Os grupos de consulta padrão são rotulados com uma **tag "Padrão"**.

## **Status da Configuração de Consulta**

* As **configurações ativas** são marcadas com uma **tag "Ativada"**.
* As **configurações desativadas** são marcadas com uma **tag "Desativada"**.

## **Pré-requisito: Importando Dados Mestres**

Para que os Dados Fuzzy funcionem corretamente, os **dados mestres** relevantes devem ser importados. Sem isso, o sistema não tem dados de referência para usar. Aqui está como importar dados mestres:

{% content-ref url="../../../infor-integration-and-configuration/importing-customer-master-data/" %}
[importing-customer-master-data](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endcontent-ref %}

## **Gerenciando Grupos de Consulta**

Cada grupo de consulta é **ativado por padrão** mas pode ser modificado clicando nos três pontos:

* **Desativar** → Desativa um grupo. _(Disponível apenas para grupos ativados)_
* **Ativar** → Ativa um grupo. _(Disponível apenas para grupos desativados)_
* **Duplicar** → Cria uma cópia que pode ser modificada sem afetar o original.
* **Visualizar** → Exibe informações como o **tipo de documento** ao qual pertence e a **tabela de consulta** que utiliza. _(Disponível apenas para grupos padrão)_
* **Editar** → Disponível para grupos **não padrão**. Permite modificar detalhes do grupo.
* **Excluir** → Remove o grupo completamente. _(Apenas para grupos não padrão)_

## **Criando uma Nova Configuração de Consulta**

Existem **duas maneiras** de criar uma configuração de consulta:

1.  **Duplicar uma consulta existente**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZUlPcWGrx1oITQS3tgZP%252Fimage.png%3Falt%3Dmedia%26token%3D59fb300d-836e-40d0-84b7-4a405cf7f321\&width=768\&dpr=4\&quality=100\&sign=3442db8f\&sv=2)

    * Isso copia todas as informações e campos de um grupo existente.
    * Você só precisa fornecer um **novo nome**.
2.  **Criar uma consulta do zero**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNbEpo2p5Q8D1d7DUchBF%252Fimage.png%3Falt%3Dmedia%26token%3D401314b5-44d0-47df-b3e6-69fea83cce82\&width=768\&dpr=4\&quality=100\&sign=1d0ce322\&sv=2)

    * Clique em **"Criar Configuração de Consulta"**.
    * Preencha os detalhes necessários:
      * **Nome da Configuração**
      * **Tabela de Consulta** (Tabela de Dados Mestres a ser usada)
      * **Manipulador de Conflito** (Escolha um: Melhor Pontuação, Retornar Nenhum, Retornar Primeiro)
      * **Tipo de Contexto** (Cabeçalho ou Linha) precisa de contexto
      * **Corresponder Todos** (Opção de Checkbox) precisa de contexto

## **Gerenciando Campos Dentro de um Grupo de Consulta**

Cada grupo contém campos que podem ser **adicionados, removidos, editados ou visualizados**, dependendo se são campos padrão ou campos personalizados.

### **Campos Padrão**

*   Marcados com uma **tag "Padrão"**.

    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fh37McVpB0tBo5wqiAttR%252Fimage.png%3Falt%3Dmedia%26token%3Dcabce083-83a5-4881-a64f-88a8757df49b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b3739019&#x26;sv=2" alt="" width="375"></div>
* **Apenas pode ser visualizado**, não editado ou excluído.

### **Campos Não Padrão**

* **Podem ser editados ou excluídos** clicando nos três pontos e selecionando **Editar** ou **Remover**.

### **Adicionando um Novo Campo**

**Nota:** Você pode criar campos dentro de configurações de Consulta padrão.

Para adicionar um novo campo dentro de um grupo:

1.  Clique em **"Criar"** dentro do grupo relevante.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvmIXTEQQHKKNbvTJj1b4%252Fimage.png%3Falt%3Dmedia%26token%3D8569867b-9f5b-4865-90bd-f2e41e846979\&width=768\&dpr=4\&quality=100\&sign=603cb7df\&sv=2)
2. Forneça os seguintes detalhes:
   * **Campo de Consulta** → Nome da coluna da tabela de consulta de dados mestres.
   * **Campo de Validação** → Campo correspondente do DocBits.
   * **Campo Pai** → _(Mais detalhes necessários)_
   * **Operador de Busca** → Escolha um:
     * Inteligente
     * Contém
     * Exato
     * Começa com
     * Termina com
   * **Caixas de Seleção:**
     * **Acionador Automático** → Quando ativado, se outro campo em uma configuração de consulta diferente compartilhar a mesma coluna, este campo será atualizado **automaticamente** sempre que o outro campo for atualizado
     * **Pesquisável** → Ativa o campo como um campo **Fuzzy Data**, permitindo pesquisas na consulta de dados mestres (ícone azul na tela de validação).

## **Última Etapa: Adicionando Campos ao Layout**

Após configurar os campos de Dados Fuzzy, **certifique-se de adicioná-los ao layout usando o Construtor de Layout**. Se os campos não forem adicionados ao layout, eles não estarão disponíveis para uso.

{% content-ref url="../../settings/global-settings/document-types/layout-manager/" %}
[layout-manager](../../settings/global-settings/document-types/layout-manager/)
{% endcontent-ref %}
