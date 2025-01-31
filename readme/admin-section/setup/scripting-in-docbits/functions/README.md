# Funções

**Documentação Funcional**

Este módulo contém funções para manipular dados de documentos e realizar várias operações relacionadas a campos de documentos.

**Funções**

1. **set\_field\_value(document\_data, field\_name, value)**
   * Descrição: Define o valor de um campo nos dados do documento.
   * Parâmetros:
     * document\_data (dict): Os dados do documento contendo informações do campo.
     * field\_name (str): O nome do campo a ser definido.
     * value: O valor a ser definido para o campo.
   *   Exemplo:

       ```
       set_field_value(document_data, "name", "John Doe")
       ```
2. **set\_date\_value(document\_data, field\_name, value, add\_days=0, skip\_weekend=False)**
   * Descrição: Define o valor de um campo de data nos dados do documento.
   * Parâmetros:
     * document\_data (dict): Os dados do documento contendo informações do campo.
     * field\_name (str): O nome do campo de data a ser definido.
     * value: O valor da data a ser definido no formato ISO (por exemplo, "2020-12-31").
     * add\_days (int): Adiciona dias adicionais à data fornecida.
     * skip\_weekend (bool): Ignora a data se cair no final de semana.
   *   Exemplo:

       ```
       set_date_value(document_data, "promised_delivery_date", "2020-12-31", add_days=2, skip_weekend=True)
       ```
3. **set\_amount\_value(document\_data, field\_name, value)**
   * Descrição: Define o valor de um campo de valor nos dados do documento.
   * Parâmetros:
     * document\_data (dict): Os dados do documento contendo informações do campo.
     * field\_name (str): O nome do campo a ser definido.
     * value: O valor a ser definido para o campo.
   *   Exemplo:

       ```
       set_amount_value(document_data, "number", "123456")
       ```
4. **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
   * Descrição: Obtém o valor de um campo dos dados do documento.
   * Parâmetros:
     * document\_data (dict): Os dados do documento contendo informações do campo.
     * field\_name (str): O nome do campo a ser definido.
     * default\_value (opcional): Retorna default\_value se nenhum valor de campo for encontrado.
     * is\_clean (opcional): Converte o valor para maiúsculas e remove espaços em branco.
   * Retorna:
     * Valor do campo.
   *   Exemplo:

       ```
       value = get_field_value(document_data, "name")
       ```
5. **create\_new\_field(field\_name, value="")**
   * Descrição: Cria um novo campo com o nome e valor especificados.
   * Parâmetros:
     * field\_name (str): O nome do campo a ser criado.
     * value: O valor inicial para o campo (o padrão é uma string vazia).
   * Retorna:
     * Dicionário do novo campo criado.
   *   Exemplo:

       ```
       dict = create_new_field("address", "")
       ```
6. **delete\_field(document\_data, field\_name)**
   * Descrição: Exclui um campo dos dados do documento.
   * Parâmetros:
     * document\_data (dict): Os dados do documento contendo informações do campo.
     * field\_name (str): O nome do campo a ser definido.
   * Retorna:
     * Document\_data como json e como dict após o campo ser excluído.
   *   Exemplo:

       ```
       //json, dict = (document_data, "name")
       ```
7. **set\_is\_required(document\_data, field\_name, value)**
   * Descrição: Define o atributo 'is\_required' de um campo nos dados do documento.
   * Parâmetros:
     * document\_data (dict): Os dados do documento contendo informações do campo.
     * field\_name (str): O nome do campo a ser definido.
     * value: O valor a ser definido para o campo.
   *   Exemplo:

       ```
       set_is_required(document_data, "bank_id", True)
       ```
8. **set\_force\_validation(document\_data, field\_name, value)**
   * Descrição: Define o atributo 'force\_validation' de um campo nos dados do documento.
   * Parâmetros:
     * document\_data (dict): Os dados do documento contendo informações do campo.
     * field\_name (str): O nome do campo a ser definido.
     * value (bool): O valor a ser definido para o campo.
   *   Exemplo:

       ```
       set_force_validation(document_data, 'supplier_name', True)
       ```
9. **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
   * Descrição: Marca um campo como inválido nos dados do documento.
   * Parâmetros:
     * document\_data (dict): Os dados do documento contendo informações do campo.
     * field\_name (str): O nome do campo a ser marcado como inválido.
     * message (str): A mensagem de validação para o campo.
     * code (opcional): Código de erro para a validação (o padrão é None).
   *   Exemplo:

       ```
       --set_field_as_invalid(document_data, "email", "Formato de email inválido", "EMAIL_FORMAT_INVALID")
       ```
10. **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
    * Descrição: Define um atributo personalizado de um campo nos dados do documento.
    * Parâmetros:
      * document\_data (str): Os dados do documento contendo informações do campo.
      * field\_name (str): O nome do campo a ser definido.
      * attribute\_name (str): O nome do atributo a ser definido.
      * value (bool): O valor a ser definido para o atributo.
    *   Exemplo:

        ```
        set_field_attribute(document_data, "address", "is_verified", True)
        ```
11. **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
    * Descrição: Verifica se um fornecedor é válido com base nos critérios fornecidos.
    * Parâmetros:
      * user (UserAuthentication): O usuário autenticado.
      * filter\_data\_json: Critérios de filtragem para validar o fornecedor.
      * sub\_org\_id (opcional): ID de sub-organização opcional para filtragem.
    * Retorna:
      * True, se o usuário for válido.
      * False se o usuário não for válido.
    *   Exemplo:

        ```
        bool = is_supplier_valid(user, {"name": "Supplier Inc."})
        ```
12. **get\_document\_content(document\_data)**
    * Descrição: Retorna o conteúdo do documento com base nos dados do documento.
    * Parâmetros:
      * document\_data (str): Os dados do documento contendo informações do campo.
    * Retorna:
      * Conteúdo do documento dos dados do documento.
    *   Exemplo:

        ```
        document_content = get_document_content(doc)
        ```
13. **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
    * Descrição: Atualiza o status de um documento com o ID especificado.
    * Parâmetros:
      * doc\_id (str): O ID do documento a ser atualizado.
      * user: O usuário que está realizando a atualização (pode ser o ID do usuário ou objeto UserAuthentication).
      * org\_id: O ID da organização à qual o documento pertence.
      * status (str): O novo status do documento.
      * message: Mensagem opcional associada à atualização de status.
      * doc\_classification\_class: Classe de classificação de documento opcional.
    *   Exemplo:

        ```
        update_document_status_with_doc_id("123456", user, "org_id", "approved", "Documento aprovado")
        ```
14. **get\_lov\_values(org\_id, key, return\_type="list\_of\_objects", sub\_org\_id=None)**
    * Descrição: Obtém os valores LOV de um org\_id específico.
    * Parâmetros:
      * org\_id: O ID da organização à qual o documento pertence.
      * return\_type (opcional): O tipo no qual os dados devem ser retornados.
      * sub\_org\_id (opcional): ID de sub-organização opcional para filtragem.
    * Retorna:
      * Valores LOV como uma lista de objetos ou como uma lista.
    *   Exemplo:

        ```
        supplier_to_check = get_lov_values(org_id, 'BlacklistSupplier', return_type="list_of_values")
        ```
15. **format\_decimal\_to\_locale(value, to\_locale="en\_US.UTF-8", max\_decimal\_places=4, min\_decimal\_places=2)**
    * Descrição: Formata um valor decimal para o formato en\_US.UTF-8.
    * Parâmetros:
      * value: O valor que deve ser formatado.
      * to\_locale (opcional): O formato no qual o valor deve ser transformado.
      * max\_decimal\_places (opcional): O máximo de casas decimais que devem ser consideradas.
      * min\_decimal\_places (opcional): O mínimo de casas decimais que devem ser consideradas.
    * Retorna:
      * O valor formatado.
    *   Exemplo:

        ```
        formatted_value = format_decimal_to_locale(value, document_json['amount_format_locale'])
        ```
16. **compare\_values(value1, value2)**
    * Descrição: Compara dois valores para igualdade, lidando com vários tipos de dados.
    * Parâmetros:
      * value1: O primeiro valor a ser comparado.
      * value2: O segundo valor a ser comparado.
    * Retorna:
      * True se os valores forem iguais e False se forem diferentes.
    *   Exemplo:

        ```
        result = compare_values(10, "10")
        ```
17. **create\_document\_task( user, document\_data, title, description, priority,**\
    **assigned\_to\_user\_id, assigned\_to\_group\_id, send\_email: bool)**
    * Descrição: Cria uma tarefa de documento.
    * Parâmetros:
      * user: O usuário que está realizando a atualização (pode ser o ID do usuário ou objeto UserAuthentication).
      * document\_data: Os dados do documento contendo informações do campo.
      * title (str): O título da tarefa.
      * description (str): A descrição da tarefa.
      * priority: A prioridade da tarefa.
      * assigned\_to\_user\_id: O ID do usuário ao qual a tarefa deve ser atribuída.
      * assigned\_to\_group\_id: O ID do grupo ao qual a tarefa deve ser atribuída.
      * send\_email (bool): Determina se um email deve ser enviado ou não.
    * Retorna:
      * Dict que indica se o processo foi bem-sucedido ou não.
    *   Exemplo:

        ```
        dict = create_document_task(user, document_data, "País de origem fora da UE", "A confirmação vem de um país fora da UE. Por favor, anexe o documento MRN.", "alto", 1007, None, False)
        ```
18. **set\_document\_sub\_org\_id(document\_data, sub\_org\_id)**
    * Descrição: Define o sub\_org\_id dos dados do documento especificado.
    * Parâmetros:
      * document\_data: Os dados do documento contendo informações do campo.
      * sub\_org\_id (str): ID de sub-organização opcional para filtragem.
    *   Exemplo:

        ```
        set_document_sub_org_id(document_data, sub_org_id)
        ```
19. **get\_user\_by\_id(user\_id)**
    * Descrição: Obtém o usuário com o ID correspondente.
    * Parâmetros:
      * user\_id (str): O ID do usuário.
    * Retorna:
      * O usuário com o ID correspondente.
    *   Exemplo:

        ```
        user = get_user_by_id("123456")
        ```
20. **get\_group\_by\_id(group\_id)**
    * Descrição: Obtém o grupo com o ID correspondente.
    * Parâmetros:
      * group\_id (str): O ID do grupo.
    * Retorna:
      * O grupo com o ID correspondente.
    *   Exemplo:

        ```
        group = get_group_by_id("123456")
        ```
21. **add\_table\_column(table, col\_name, default\_value=None)**
    * Descrição: Adiciona uma coluna à tabela correspondente.
    * Parâmetros:
      * table: A tabela onde a coluna deve ser adicionada.
      * col\_name: O nome da coluna.
      * default\_value (opcional): O valor inicial para o campo (o padrão é uma string vazia).
    *   Exemplo:

        ```
        add_table_column(table, "UNIT_PRICE_PER")
        ```
22. **get\_column\_value(row, column\_name, default\_value=None, is\_clean=False)**
    * Descrição: Obtém um valor de uma coluna especificada.
    * Parâmetros:
      * row: A linha onde o valor está localizado.
      * col\_name: O nome da coluna.
      * default\_value (opcional): Retorna default\_value se nenhum valor de campo for encontrado.
      * is\_clean (opcional): Converte o valor para maiúsculas e remove espaços em branco.
    *   Exemplo:

        ```
        original_unit_price = get_column_value(row, "ORIGINAL_UNIT_PRICE")
        ```
23. **set\_column\_value(row, column\_name, value)**
    * Descrição: Define um valor de uma coluna especificada.
    * Parâmetros:
      * row: A linha onde o valor está localizado.
      * col\_name: O nome da coluna.
      * value: O valor que será definido na localização especificada.
    * Retorna:
      * True se a alteração foi bem-sucedida.
    *   Exemplo:

        ```
        success = set_column_value(row,"SUPPLIER_ID", supplier_id)
        ```
24. **set\_column\_date\_value(document\_data, row, column\_name, value, add\_days=0)**
    * Descrição: Define um valor de uma coluna especificada.
    * Parâmetros:
      * document\_data: Os dados do documento contendo informações do campo.
      * row: A linha onde o valor está localizado.
      * col\_name: O nome da coluna.
      * value: O valor da data a ser definido no formato ISO (por exemplo, "2020-12-31").
      * add\_days (int): Adiciona dias adicionais à data fornecida.
    *   Exemplo:

        ```
        set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
        ```
25. **set\_column\_amount\_value(document\_data, row, column\_name, value)**
    * Descrição: Realiza as seguintes ações:
      * Converte o valor para string e define o valor para a coluna.
      * Define o conteúdo da coluna para o valor.
      * Formata o valor de acordo com a localidade.
    * Parâmetros:
      * document\_data (dict): Os dados do documento contendo informações do campo.
      * row: Linha da tabela.
      * column\_name: Nome da coluna.
      * value: Valor a ser definido.
    *   Exemplo:

        ```
        set_column_amount_value(document_data, row, "UNIT_PRICE", str(unit_price))
        ```
26. **remove\_rows\_from\_table(document\_data, table\_name, count, start)**
    * Descrição: Remove linhas da tabela especificada.
    * Parâmetros:
      * document\_data (dict): Os dados do documento contendo informações do campo.
      * table\_name: O nome da tabela.
      * count: Quantas linhas devem ser excluídas.
      * start: O ponto de partida.
    *   Exemplo:

        ```
        remove_rows_from_table(document_data,"INVOICE_TABLE",count,start)   
        ```
27. **remove\_all\_rows\_except\_one\_from\_table(document\_data, line\_number)**
    * Descrição: Remove todas as linhas, exceto uma, da tabela especificada.
    * Parâmetros:
      * document\_data (dict): Os dados do documento contendo informações do campo.
      * line\_number: O número da linha que não deve ser removida.
    *   Exemplo:

        ```
        remove_all_rows_except_one_from_table(document_data, line_number) 
        ```

Você também pode utilizar algumas das funções embutidas do Python:

* abs(): Retorna o valor absoluto de um número.
* len(): Retorna o comprimento (número de itens) de um objeto, como uma lista ou string.
* isinstance(): Verifica se um objeto é uma instância de uma classe ou tipo específico.
* print(): Imprime a saída no console.
* round(): Arredonda um número de ponto flutuante para um número especificado de casas decimais.
* str\_to\_bool(): Converte uma string em um valor booleano (True ou False).
* type(): Retorna o tipo de um objeto.
* dict(): Cria um objeto dicionário.
* list(): Cria um objeto lista.
* str(): Converte um valor em uma string.
* float(): Converte um valor em um número de ponto flutuante.
* int(): Converte um valor em um inteiro.

Para mais detalhes, visite a documentação oficial do Python: [Funções Embutidas](https://docs.python.org/3.12/library/functions.html).

#### Funções da Classe String

Você também pode usar essas funções especificamente para trabalhar com strings:

* lower(): Converte todos os caracteres em uma string para minúsculas.
* upper(): Converte todos os caracteres em uma string para maiúsculas.
* split(): Divide uma string em uma lista com base em um delimitador (por exemplo, espaço ou vírgula).
* startswith(): Verifica se uma string começa com um prefixo especificado.
* endswith(): Verifica se uma string termina com um sufixo especificado.
* strip(): Remove qualquer espaço em branco no início ou no final de uma string.

#### Funções do Módulo Math do Python

Essas funções fazem parte do módulo math e são úteis para operações matemáticas:

* floor(): Retorna o maior inteiro menor ou igual a um número dado.
* ceil(): Retorna o menor inteiro maior ou igual a um número dado.

Para mais informações, confira a documentação oficial do Python: [Funções do Módulo Math](https://docs.python.org/3/library/math.html).

#### Função de Expressão Regular

* re.search(): Procura um padrão dentro de uma string e retorna a primeira correspondência.

Veja mais detalhes aqui: [Documentação re.search](https://docs.python.org/3/library/re.html#re.search).

#### Funções Externas

Aqui estão algumas funções úteis de bibliotecas externas:

* deepcopy(): Cria uma cópia de um objeto, incluindo objetos aninhados (do módulo copy).\
  [Documentação Deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Calcula o número de edições (inserções, exclusões, substituições) necessárias para transformar uma string em outra. Esta função está disponível na [biblioteca Jellyfish](https://jamesturk.github.io/jellyfish/functions/).

#### Funções de Data e Hora

Você pode usar as seguintes funções para trabalhar com datas e horas:

* strptime(): Converte uma string em um objeto datetime com base em um formato especificado.
* strftime(): Formata um objeto datetime em uma string com base em um formato especificado.

Para mais informações, confira a documentação oficial:\
[Funções de Data e Hora](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
