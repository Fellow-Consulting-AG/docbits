# E-mails de entrada

## Ativando E-mail de Entrada para Processamento de Documentos

Para começar a usar o e-mail de entrada para processamento de documentos, siga estas etapas:

1. **Vá para Configurações**: Comece navegando até o menu **Configurações** do aplicativo.
2. **Selecione Processamento de Documentos**: Nas configurações, escolha **Processamento de documentos** para acessar as opções de configuração relacionadas.
3. **Abra Módulos**: Na seção de Processamento de documentos, clique em **Módulos**.
4. **Role até Tipo de Documento**: Role para baixo até encontrar **Tipo de documento**.
5. **Ative E-mail de Entrada**: Encontre **E-mail de Entrada** e ative-o alternando o interruptor.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_1.png)

## Configurando E-mail de Entrada para Importação de Documentos

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_2.png)

Após ativar o e-mail de entrada, configure as configurações para controlar como os documentos são importados. Veja como:

1. **Volte para Processamento de Documentos**: Nas configurações, navegue até **Processamento de documentos**.
2.  **Selecione Importar**: Escolha **Importar** para acessar as configurações do e-mail de entrada.

    Você verá as seguintes opções:

    * **Campo de E-mail**: Este campo exibe um endereço de e-mail único, gerado pelo sistema, com base no ID da sua organização. O formato é `org_id@environment.inbound.docbits.com`. Envie ou encaminhe e-mails com documentos para este endereço para importação automatizada.
    * **Importar Documento Somente de E-mail(s) Predefinidos**: Ative esta opção para restringir as importações a e-mails recebidos apenas de endereços específicos e predefinidos.
    * **Responder a este E-mail se a Importação Não Puder Ser Feita**: Ative esta opção se você quiser que o sistema responda automaticamente quando uma tentativa de importação falhar.
3. **Salvar Configurações**: Após configurar essas opções, clique em **Salvar** para aplicá-las.

## E-mail(s) Predefinido(s)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_3.png)

Quando a opção **Importar Documento Somente de E-mail(s) Predefinidos** está habilitada, você pode gerenciar quais endereços de e-mail estão autorizados a enviar documentos para o e-mail de entrada.

1. **Digite E-mails Autorizados**: No campo **Coloque o e-mail aqui**, digite cada endereço de e-mail que você deseja autorizar.
2. **Atribuir a Suborganização (Opcional)**:
   * Se nenhuma suborganização for selecionada, o documento será atribuído à organização principal.
   * Se uma suborganização for selecionada, o documento será direcionado apenas para essa suborganização.
3. **Adicionar E-mail**: Clique em **Adicionar** para salvar cada e-mail na lista de endereços autorizados.
4. **Excluir E-mail**: Para remover um e-mail autorizado, clique em **Excluir** ao lado da entrada de e-mail.

Com esta configuração, documentos de endereços de e-mail não autorizados serão ignorados, garantindo que apenas fontes específicas possam enviar documentos para importação.

## **Responder a este e-mail se a importação não puder ser feita**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_4.png)

Se você ativar **Responder a este e-mail se a importação não puder ser feita**, um campo adicional aparecerá onde você pode inserir um endereço de e-mail. Este endereço de e-mail receberá uma notificação se qualquer tentativa de importação de documento falhar, permitindo que você fique informado sobre quaisquer problemas no processo de importação.

1. **Ativar Notificação de Falha**: Ative **Responder a este e-mail se a importação não puder ser feita**.
2. **Digite o E-mail de Notificação**: No novo campo, insira o endereço de e-mail onde você gostaria de receber notificações de falha.

Com este recurso ativado, quaisquer tentativas de importação falhadas acionarão uma resposta automática para o e-mail especificado, ajudando você a resolver rapidamente problemas de importação.

**Após configurar todas as configurações, não se esqueça de clicar em Salvar para aplicar suas alterações.**
