# Notas de versão

## Release Winter 10 de Dezembro de 2025

### Melhorias no DocBits:

* **Personalização Aprimorada de Regras de Correspondência de Pedidos:**\
  O DocBits agora oferece controle granular sobre as regras de correspondência de pedidos de compra. Você pode configurar exatamente quais colunas devem ser correspondidas para cada tipo de documento, definir tolerâncias por coluna e escolher se cada regra se aplica à correspondência manual, automática ou ambas. Essas melhorias fornecem aos usuários a flexibilidade para ajustar o processo de correspondência às suas necessidades operacionais específicas.
*   **Suporte para Múltiplas Contas Financeiras de Fornecedores:**\
    O DocBits agora suporta múltiplas contas financeiras para fornecedores através do BOD RemitToPartyMaster da Infor. Uma nova configuração está disponível para ativar este recurso.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_1.png)
*   **Adicionar Acesso de Usuário aos Resultados de Extração OCR:**\
    O botão Vista OCR na tela de Validação de Campo agora está acessível a todos os usuários com acesso de validação, não apenas aos administradores, permitindo que todos os usuários revisem os resultados de extração OCR e pesquisem conteúdo específico nos documentos.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_2.png)
* **Renderização Dinâmica de Colunas nas Telas de Aprovação:**\
  Visualizações de aprovação aprimoradas para exibir dinamicamente apenas as colunas configuradas para comparação nas preferências de banco de dados de cada organização. Anteriormente, colunas como Código de Unidade e Data de Entrega Prometida apareciam vazias quando não configuradas para comparação, causando confusão. Agora, as visualizações de aprovação mostram apenas os campos que estão sendo ativamente comparados. Isso fornece telas de aprovação mais claras e específicas da organização, sem colunas vazias ou irrelevantes.
* **Campo Tipo de Pedido Adicionado à Pesquisa de Dados Mestre**:\
  A lista de cabeçalhos de pedidos de compra agora inclui uma coluna "Tipo de Pedido" (type\_code) na pesquisa de dados mestre, fornecendo capacidades de categorização adicionais.
* **Melhorias no Painel de Filtros Personalizados:**\
  Funcionalidade de compartilhamento de painel aprimorada ao permitir que usuários compartilhados editem os filtros do painel. Os usuários que têm painéis compartilhados com eles agora podem modificar os filtros para uma visualização mais flexível e personalizada.
* **Prefixos Personalizáveis para Colunas de Tela de Aprovação:**\
  Adicionada uma opção configurável para exibir prefixos antes das colunas de documentos nas telas de aprovação. O prefixo pode ser definido no construtor de layout, permitindo que os usuários escolham se os prefixos aparecem e a quais tipos de documentos se aplicam.\


### Melhorias Gerais

* Melhorado o registro de erros para tabelas mal treinadas na extração de tabelas.
* Adicionado um limite de compartilhamento para painéis de até 10 usuários ou 5 grupos, juntamente com uma mensagem de erro clara quando o limite é atingido.
* Melhorado o tratamento de erros para painéis personalizados quando um usuário tenta criar um painel com um nome que já existe.

### Correções de Bugs:

* Corrigido um problema em que emails pareciam ser enviados com sucesso na seção Detalhes do Fornecedor, mas não eram entregues aos destinatários.
* Corrigido um problema em que campos suspensos adicionados às telas de aprovação/rejeição não eram exibidos.
* Corrigido um problema em que todos os documentos exportados eram marcados como atualizados por último pelo usuário errado.
* Corrigido um problema em que importações FTP não coletavam documentos.
* Corrigido um problema em que documentos mostravam o status "Fluxo de trabalho em andamento", mas nenhum fluxo de trabalho era executado e o registro permanecia vazio.
* Corrigido um problema em que usuários não relacionados eram atribuídos aos documentos no momento da exportação sem realizar nenhum trabalho neles.
* Corrigido um problema em que usuários com permissões corretas não podiam rejeitar documentos atribuídos e recebiam erros.
* Corrigido um problema em que os ícones de fluxo de documentos não eram exibidos para algumas organizações.
* Corrigido um problema em que um popup aparecia ao carregar documentos com arrastar e soltar no painel.
* Corrigido um problema em que as flags E-TEXT eram exibidas como ativadas na interface do usuário, embora a resposta da API mostrasse todos os valores como falsos.
* Corrigido um problema em que ocorria um erro ao carregar documentos contendo páginas em branco.
* Corrigido um problema em que os hiperlinks de tarefas nas notificações por email usavam a URL de aprovação v2 em vez de v3.
* Corrigido um problema em que a Pesquisa de Dados Mestre não exibia nenhum fornecedor quando a sub-organização "Cross" era selecionada, impedindo que os usuários visualizassem dados de fornecedores entre organizações.
* Corrigido um problema em que documentos carregados no Cross não eram atribuídos a um ID de sub-organização.
* Corrigido um problema em que importações de email recebidas falhavam para remetentes com letras maiúsculas em seus endereços de email devido à comparação de email sensível a maiúsculas e minúsculas.

## Release Autumn Summit 22 de outubro de 2025

### Melhorias no DocBits:

*   #### Aperfeiçoamentos no Design do Modelo de Email:

    O editor de modelos de email foi redesenhado para fornecer uma estrutura mais clara e uma experiência mais suave. Selecionar campos de documento agora é mais intuitivo, e anexos podem ser incluídos diretamente nos modelos. Essas melhorias tornam mais rápido e fácil criar emails profissionais e personalizados.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdv4oDlfkRyD0W9yWGAA4%252Fimage.png%3Falt%3Dmedia%26token%3D14bf7ebd-d886-4758-8184-d7b94447518a\&width=768\&dpr=4\&quality=100\&sign=88405d9c\&sv=2)
*   #### Aperfeiçoamentos no Painel de Controle:

    O painel de controle foi expandido para melhorar a navegação e a personalização. Com novas abas, os usuários podem alternar mais rapidamente entre diferentes tipos de documentos, reduzindo o tempo gasto procurando a visualização correta.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmpO7WSIrkL0I8Rje3HQt%252Fimage.png%3Falt%3Dmedia%26token%3D77d03fe7-e626-4645-b191-e332715a25fb\&width=768\&dpr=4\&quality=100\&sign=93fa9925\&sv=2)
*   #### Painéis de Filtro Personalizados:

    Além disso, os painéis de controle agora podem ser personalizados e filtrados de acordo com as preferências individuais. Esses painéis personalizados também podem ser compartilhados com colegas, facilitando a criação de visualizações de relatórios consistentes em toda a equipe.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn5rPvGnRltT3mTIDoJwV%252Fimage.png%3Falt%3Dmedia%26token%3D22d065e3-81eb-4f16-828c-7f9134c25b1b\&width=768\&dpr=4\&quality=100\&sign=eb11d3a3\&sv=2)
*   #### Logs de Notificações por Email:

    Um novo recurso de registro está disponível para todas as notificações por email. Os usuários agora podem revisar um histórico de notificações enviadas, facilitando a verificação de entregas e a resolução de problemas caso os emails não sejam recebidos.
*   #### Suporte a Fatura Eletrônica: e-SLOG 1.6 & 2.0:

    Foi introduzido suporte para formatos adicionais de fatura eletrônica. O sistema agora pode processar e gerar versões e-SLOG 1.6 e 2.0, expandindo a compatibilidade com parceiros e requisitos regulatórios.
*   #### Aperfeiçoamentos na Detecção de Duplicatas:

    A detecção de duplicatas foi aprimorada com duas opções de configuração poderosas. O **Intervalo de Detecção de Duplicatas** permite que você defina um intervalo de tempo para verificar duplicatas com mais precisão, enquanto a configuração **Impedir Exportação de Duplicatas** impede automaticamente a exportação de documentos detectados como duplicatas. Juntos, esses aprimoramentos oferecem mais controle e garantem uma maior precisão dos dados.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXHRKTmuSxTlDt9lDEkE7%252Fimage.png%3Falt%3Dmedia%26token%3D96b56af6-c644-4b0f-a488-8bc16a03c11f\&width=768\&dpr=4\&quality=100\&sign=9b723b7f\&sv=2)
*   #### Aperfeiçoamentos na Árvore de Decisão:

    As árvores de decisão agora são mais versáteis, com a capacidade de retornar valores de campos de documento. Isso permite lógica de automação mais avançada, possibilitando que os fluxos de trabalho tomem decisões com base em dados reais do documento.
*   #### Novos Cartões de Fluxo de Trabalho:

    Dois novos cartões de fluxo de trabalho expandem as capacidades de automação. O primeiro permite verificar se um documento pertence a uma sub-organização específica, facilitando o manuseio de configurações multi-entidades. O segundo introduz uma verificação de tolerância de data de entrega, que compara datas de entrega com a data atual em dias úteis para ajudar a gerenciar e aplicar requisitos de entrega de forma mais eficaz.
*   #### Melhorias na Exportação CSV:

    O recurso de exportação CSV foi significativamente aprimorado. Em vez de exportar apenas os documentos exibidos na página atual, o sistema agora exporta todos os documentos em um conjunto de dados. Cada exportação cria uma entrada de log, e o CSV resultante é enviado automaticamente por email, proporcionando um processo de exportação mais completo e confiável.
*   #### Período de Exclusão de Ordem de Compra:

    Uma nova opção de configuração permite que os administradores definam um período de tempo para a exclusão de ordens de compra. Essa melhoria adiciona flexibilidade e controle sobre as políticas de retenção de dados, garantindo que as ordens de compra sejam removidas apenas quando apropriado.

### Correções de Bugs

* Corrigido um problema em que dados antigos eram incluídos ao exportar documentos.
* Corrigido o filtro para Erros de Exportação, que anteriormente mostrava outros status também.
* Resolvida uma incompatibilidade de validação de tabela em que “Preço Unitário” disparava erros, mas “Preço Unitário Por” não, apesar dos valores estarem corretos.
* Corrigido um problema em que adicionar uma nova coluna ao painel de controle falhava.
* Corrigido um problema em que as tarefas não eram visíveis na coluna de tarefas do painel de controle.
* Corrigido o comportamento de classificação aleatória para que as listas sigam agora uma ordem consistente.
* Resolvido um problema em que a alteração do tamanho da coluna não podia ser interrompida.
* Corrigido um bug que impedia a correspondência manual de linhas na tela de Correspondência de PO.
* Corrigido um problema em que a opção de anexo de email era redefinida após salvar.
* Corrigido um problema em que a contabilidade automática exibia IDs de banco de dados inicialmente.
* Corrigido o comportamento de campo difuso para que os valores não sejam mais sobrescritos incorretamente.
* Corrigido um problema em que os campos na conta automática desapareciam após excluir o conteúdo.
* Corrigido um bug em que o usuário não conseguia renomear “Nome” e “Sobrenome” na janela de configurações.
* Resolvido um problema em que os documentos podiam ficar presos em “fluxo de trabalho em andamento”.
* Corrigido um problema de cor de ícone de menu em que as cores de organização selecionadas não eram aplicadas corretamente.
* Corrigido um problema em que os códigos QR às vezes não eram reconhecidos.
* Corrigido um problema em que as contas não podiam ser removidas com a tecla de retrocesso para inserir uma diferente.
* Resolvido um problema de mistura de idiomas após o login após a atualização de produção.

## Lançamento Spring Bloom – 23 de Abril de 2025

### Melhorias no DocBits:

* **Opção de Filtro para o Log de Importação de Email:** Os usuários agora têm a capacidade de filtrar os logs de importação e classificar a tabela para uma visão mais clara e eficiente. Essa melhoria agiliza o processo de identificação e gerenciamento de entradas de email, melhorando a solução de problemas e o gerenciamento geral de logs.
* **Suporte Multilíngue para Lista de Valores:** Expandimos as capacidades multilíngues para o recurso Lista de Valores. Os administradores agora podem definir rótulos em vários idiomas, garantindo que o rótulo correto seja exibido automaticamente com base nas configurações de idioma do sistema do usuário. Essa melhoria promove maior acessibilidade e localização, facilitando a interação dos usuários em todo o mundo com a plataforma em seu idioma nativo.
* **Melhorias nos Detalhes do Usuário nas Configurações:** A interface de configurações agora exibe informações abrangentes do usuário. Os administradores podem facilmente visualizar afiliações a grupos, detalhes de sub-organizações e dados adicionais importantes, permitindo uma melhor gestão dos papéis dos usuários e uma compreensão mais clara das estruturas da equipe.
* **Informações de Contabilidade Automática na Tela de Aprovação:** A tela de aprovação agora apresenta detalhes de contabilidade automática juntamente com as informações da fatura. Essa melhoria fornece uma visão mais profunda dos dados da transação, facilitando processos de revisão mais suaves e uma tomada de decisão mais informada em relação às faturas.
* **Contador de Tarefas para Documentos na Visualização do Painel:** Documentos no painel agora podem indicar tarefas abertas associadas a eles e exibir o número total de tarefas pendentes. Este recurso fornece aos usuários uma visão rápida das ações pendentes, melhorando a gestão de tarefas e a eficiência do fluxo de trabalho.
* **Seleção de Modelo de IA Baseada em Fornecedor:** Os usuários agora podem selecionar o modelo de IA usado para extração de dados com base em cada fornecedor. Esta melhoria permite uma otimização mais precisa, garantindo melhor precisão na extração para diferentes fornecedores e melhorando os resultados gerais do processamento de dados.
* **Registros de Fluxo de Trabalho Aprimorados para Cartões de Árvore de Decisão:** Os registros agora exibem a saída da árvore de decisão, facilitando o acompanhamento e a compreensão de como as decisões foram tomadas dentro dos fluxos de trabalho.
*   **Introdução de um Novo Setup de Testes Automáticos para Melhorar a Funcionalidade e Estabilidade do Sistema:**

    Estamos empolgados em anunciar a implementação de um novo sistema de testes automatizados projetado para melhorar a funcionalidade e a confiabilidade geral de nossa plataforma. Esse novo setup realizará verificações consistentes e abrangentes em nosso sistema para identificar quaisquer problemas antes que eles impactem sua experiência. Ao automatizar esses testes, podemos garantir respostas mais rápidas a problemas potenciais e manter os mais altos padrões de qualidade para nosso sistema.

    ​

### Correções de Bugs

* Resolvido um problema onde as tarefas não apareciam na tela de validação/aprovação.
* Corrigida a posição do botão Próximo/Anterior para que permaneça estático.
* Corrigidos problemas de rolagem nas visualizações de script e árvore de decisão, garantindo que os botões de ação permaneçam estacionários durante a rolagem.
* Removido o campo de país de origem das faturas eletrônicas.
* Corrigido um problema com o contador de tarefas exibindo um número impreciso de tarefas.
* Adicionadas traduções ausentes.
* Corrigidos campos personalizados para exibir nomes descritivos em vez de IDs.
* Atualizada a lista de atalhos para a tela de correspondência de PO.
* Resolvido um problema onde documentos eram baixados com um nome de arquivo incorreto.
* Corrigidas inconsistências de ordenação na tabela de linhas de fatura dentro da correspondência de PO.
* Corrigido um problema que afetava a funcionalidade de criação de tarefas.
* Corrigido um problema na correspondência de PO onde a ordenação da tabela de faturas seria redefinida ao corresponder uma linha.
* Resolvidos problemas de contabilidade automática garantindo que referências de booking sejam divididas corretamente quando um valor é dividido.
* Atualizadas as informações do host ClickHouse.
* Resolvido um problema onde documentos duplicados não eram reconhecidos como duplicados.
* Corrigidos problemas de exportação causados por referências de booking que eram muito longas.
* Resolvido um problema onde checkboxes somente leitura não eram somente leitura.
* Corrigido um problema onde os usuários podiam ser adicionados a uma sub-organização duas vezes.
* Corrigido um problema onde mudar a sub-organização de um documento fazia com que o usuário ou grupo atribuído fosse redefinido.

​

## Correção Rápida de Lançamento Inverno Frost 10 de Abril de 2025

### Melhorias no DocBits:

* **Função de Script `set_column_date_value` Aprimorada:** A função `set_column_date_value` agora inclui suporte para a opção `skip_weekend`, permitindo que os valores de data pulem automaticamente os finais de semana quando aplicados.
* **Suporte Aprimorado para Upload de Arquivos:** Arquivos PNG e JPEG agora podem ser carregados diretamente e são automaticamente convertidos para o formato PDF para um manuseio de documentos mais eficiente.
* **Atualizações na Funcionalidade de Watchdog:**
  * Agora suporta exportação para **Enaio** para melhor integração do sistema.
  * Capacidades de análise aprimoradas para extrair informações de estruturas XML `Sync.ContentDocument`, permitindo um processamento de dados mais eficiente.

### Correções de Bugs

* Corrigido um problema em uma função de script.
* Resolvido um problema onde os pedidos de compra tinham um status incorreto após serem atualizados.

## Lançamento Hot Fix Winter Frost 11 de Março de 2025

### Melhorias no DocBits:

* **Extração de Dados Aprimorada:** Adicionada uma opção para extrair o **Número do Pedido de Compra** ou **Número do Item** de uma linha acima ou abaixo.
* **Acesso Expandido a Sub-Organizações Cruzadas:** Usuários não administradores agora também podem acessar o recurso **Sub-Organizações Cruzadas**.

### **Correções de Bugs:**

* Corrigido um problema onde usuários não podiam ser adicionados a um grupo.
* Corrigido um problema com falhas na importação de e-mails.
* Resolvido um problema com o treinamento de campo em documentos com mais de uma página.
* Corrigido um problema onde scripts não funcionavam corretamente.
* Resolvido um problema onde os dados do documento não eram exibidos corretamente.
* Corrigido um problema com a configuração de atualização automática do pedido de compra.
* Corrigido um problema onde os tokens de assinatura eram exibidos incorretamente.
* Resolvido um problema onde a tela de tarefas exibia uma versão desatualizada do documento.
* Corrigido um problema que fazia com que os documentos não mudassem seu status.
