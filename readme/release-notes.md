# Notas de versão

## Lançamento Spring Bloom – 23 de Abril de 2025

### Melhorias no DocBits:

* **Opção de Filtro para o Log de Importação de Email:** Os usuários agora têm a capacidade de filtrar os logs de importação e classificar a tabela para uma visão mais clara e eficiente. Essa melhoria agiliza o processo de identificação e gerenciamento de entradas de email, melhorando a solução de problemas e o gerenciamento geral de logs.
* **Suporte Multilíngue para Lista de Valores:** Expandimos as capacidades multilíngues para o recurso Lista de Valores. Os administradores agora podem definir rótulos em vários idiomas, garantindo que o rótulo correto seja exibido automaticamente com base nas configurações de idioma do sistema do usuário. Essa melhoria promove maior acessibilidade e localização, facilitando a interação dos usuários em todo o mundo com a plataforma em seu idioma nativo.
* **Melhorias nos Detalhes do Usuário nas Configurações:** A interface de configurações agora exibe informações abrangentes do usuário. Os administradores podem facilmente visualizar afiliações a grupos, detalhes de sub-organizações e dados adicionais importantes, permitindo uma melhor gestão dos papéis dos usuários e uma compreensão mais clara das estruturas da equipe.
* **Informações de Contabilidade Automática na Tela de Aprovação:** A tela de aprovação agora apresenta detalhes de contabilidade automática juntamente com as informações da fatura. Essa melhoria fornece uma visão mais profunda dos dados da transação, facilitando processos de revisão mais suaves e uma tomada de decisão mais informada em relação às faturas.
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

​

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
