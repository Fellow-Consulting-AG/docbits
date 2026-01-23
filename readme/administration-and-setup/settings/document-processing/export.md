# Exportação

## Visão Geral

A página de Exportação exibe todas as configurações de exportação configuradas, incluindo se estão ativas ou inativas. A partir daqui, os usuários podem:

* Visualizar e gerenciar configurações de exportação existentes
* Criar novas conexões de exportação (ex.: para **Infor**, **Infor & IDM**, **Webhook** ou **SFTP**)
* Editar ou excluir configurações de exportação existentes

## Onde Encontrar

Você pode encontrá-lo em: **Configurações** → **Processamento de Documentos** → **Exportação**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(442).png)

## **Usando a Página de Exportação**

Quando você abre a página de Exportação, verá uma lista de todas as configurações de exportação existentes.

Cada linha na lista mostra:

* **Indicador de Status**
  * **Verde** significa que a exportação está ativa
  * **Vermelho** significa que a exportação está desativada
* **Name** – o nome da configuração de exportação
* **Document Type** – o tipo de documento para o qual a exportação está configurada
* **Sub-Organization** – se a exportação está limitada a uma sub-organização específica
* **Export Method** – para onde o documento será enviado (ex.: Infor, IDM, SFTP)
* **Actions** – botões para **editar, excluir** ou **ativar/desativar** a configuração

![DocBits Compra Pedido Exportar 7](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_purchase_order_export_7.png)

#### **Regras Importantes para Configuração de Exportação**

Para cada **tipo de documento** **dentro de uma determinada organização ou sub-organização**, aplicam-se as seguintes regras:

* Você pode ter **apenas uma exportação Infor ativa**
* Você pode ter **apenas uma exportação não-Infor ativa** (ex.: Webhook, SFTP)

No entanto, é possível ter:

* **Uma exportação Infor ativa** _e_ **uma exportação não-Infor ativa** ao mesmo tempo para o mesmo tipo de documento
* **Diferentes configurações de exportação para diferentes sub-organizações** — por exemplo, uma exportação Infor para Sub-Org A e outra exportação Infor para Sub-Org B

## **Criando uma Nova Exportação**

Para criar uma nova exportação:

1. Clique no botão **"Novo"**.\
   ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(1)%20(1)%20(1).png)
2. Selecione o **Tipo de Exportação** que deseja configurar (ex.: Infor, IDM, SFTP).
3. Preencha os campos obrigatórios com base no tipo de exportação.
4. Salve a configuração.

## Opções de Exportação

#### Webhook

<details>

<summary>Webhook</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(15)%20(1).png)

#### **Descrição dos Campos**

* **Title**\
  O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_\
  Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type**\
  Menu suspenso listando todos os tipos de documentos disponíveis.\
  Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **Export URL**\
  A URL de destino onde o documento deve ser exportado.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![DocBits Compra Pedido 4](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_purchase_order_4.png)

**Descrição dos Campos**

* **Title**\
  O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_\
  Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type**\
  Menu suspenso listando todos os tipos de documentos disponíveis.\
  Isso determina a qual tipo de documento esta configuração de exportação se aplica.

- **Username**\
  O nome de usuário usado para autenticar no servidor SFTP.
- **Password**\
  A senha correspondente para a conta SFTP. Certifique-se de que a conta tenha acesso de gravação à pasta especificada.
- **Server URL**\
  O nome do host ou endereço IP do servidor SFTP de destino.
- **Port**\
  A porta usada para conectar ao servidor SFTP.
- **Folder**\
  O caminho no servidor SFTP onde os documentos devem ser carregados (ex.: `/incoming/invoices/`).\
  Deve existir e ser gravável.
-   **XSLT File (Opcional)**

    O **arquivo XSLT** permite a transformação do formato de exportação padrão do DocBits.

    * **Quando usar:**\
      Apenas se o sistema receptor requer uma estrutura diferente ou formatação específica que difere do padrão do DocBits.
    * **Deixe vazio** se o formato de exportação padrão atende aos requisitos.

</details>

#### Infor Export to SFTP

<details>

<summary>Infor Export to SFTP</summary>

![DocBits Exportar Sftp](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_export_sftp.png)

**Descrição dos Campos**

* **Title**\
  O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_\
  Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type**\
  Menu suspenso listando todos os tipos de documentos disponíveis.\
  Isso determina a qual tipo de documento esta configuração de exportação se aplica.

- **IDM Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.\
  [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **BOD Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.\
  [Precisa de ajuda para criar um? Veja o Guia de Mapeamento BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
- **Folder**\
  O caminho no servidor SFTP onde os documentos devem ser carregados (ex.: `/incoming/invoices/`).\
  Deve existir e ser gravável.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![DocBits Exportar Smb](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_export_smb.png)

#### **Descrição dos Campos**

* **Title**\
  O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_\
  Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type**\
  Menu suspenso listando todos os tipos de documentos disponíveis.\
  Isso determina a qual tipo de documento esta configuração de exportação se aplica.

- **Username**\
  O nome de usuário usado para conectar ao compartilhamento SMB.
- **Password**\
  A senha correspondente para autenticação SMB.
- **Server URL**\
  O endereço do servidor SMB.
- **Port**\
  Número da porta usado para acessar o compartilhamento SMB.
- **Folder**\
  O caminho da pasta dentro do compartilhamento SMB onde os documentos devem ser salvos (ex.: `/incoming/invoices/`).\
  Deve existir e ser gravável.
-   **JPL Mapping File (Opcional)**

    O **arquivo JPL** é usado para definir uma transformação dos dados exportados antes de serem gravados no compartilhamento SMB.

    * **Quando usar:**\
      Apenas quando os dados do documento exportado precisam ser ajustados para corresponder à formatação externa ou expectativas do sistema.
    * **Deixe vazio** se nenhuma transformação for necessária.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(13)%20(1).png)

#### **Descrição dos Campos**

* **Title**\
  O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_\
  Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type**\
  Menu suspenso listando todos os tipos de documentos disponíveis.\
  Isso determina a qual tipo de documento esta configuração de exportação se aplica.

- **ION Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.
- **IDM Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.\
  [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **Cloud / On-Prem Toggle**\
  Um interruptor para indicar o tipo de implantação do Infor:
  * **Cloud**: Selecione isso se você for um cliente Infor CloudSuite.
  * **On-Prem**: Selecione isso se o Infor for auto-hospedado.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(11)%20(1).png)

#### **Descrição dos Campos**

* **Title**\
  O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_\
  Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type**\
  Menu suspenso listando todos os tipos de documentos disponíveis.\
  Isso determina a qual tipo de documento esta configuração de exportação se aplica.

- **ION Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.
- **BOD Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.\
  [Precisa de ajuda para criar um? Veja o Guia de Mapeamento BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
- **Cloud / On-Prem Toggle**\
  Um interruptor para indicar o tipo de implantação do Infor:
  * **Cloud**: Selecione isso se você for um cliente Infor CloudSuite.
  * **On-Prem**: Selecione isso se o Infor for auto-hospedado.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![DocBits Exportar Ion Bod](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_export_ion_bod.png)

#### **Descrição dos Campos**

* **Title**\
  O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_\
  Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type**\
  Menu suspenso listando todos os tipos de documentos disponíveis.\
  Isso determina a qual tipo de documento esta configuração de exportação se aplica.

- **ION Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.
- **IDM Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.\
  [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **BOD Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.\
  [Precisa de ajuda para criar um? Veja o Guia de Mapeamento BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
- **Cloud / On-Prem Toggle**\
  Um interruptor para indicar o tipo de implantação do Infor:
  * **Cloud**: Selecione isso se você for um cliente Infor CloudSuite.
  * **On-Prem**: Selecione isso se o Infor for auto-hospedado.

</details>

### Para Clientes Infor CloudSuite

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![DocBits Configurações E-mail](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_settings_email.png)

#### **Descrição dos Campos**

* **Title**\
  O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_\
  Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type**\
  Menu suspenso listando todos os tipos de documentos disponíveis.\
  Isso determina a qual tipo de documento esta configuração de exportação se aplica.

- **ION Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.
- **IDM Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.\
  [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)

* **LN Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.\
  [Precisa de ajuda para criar um? Veja o Exemplo de Mapeamento LN](../../../infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln/)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![DocBits Configurações](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_settings.png)

#### **Descrição dos Campos**

* **Title**\
  O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_\
  Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type**\
  Menu suspenso listando todos os tipos de documentos disponíveis.\
  Isso determina a qual tipo de documento esta configuração de exportação se aplica.

- **ION Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.
- **IDM Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.\
  [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **M3 Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.\
  [Precisa de ajuda para criar um? Veja o Exemplo de Mapeamento M3](../../../infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3.md)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![DocBits Fluxo de trabalho Compra Pedido 5](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_workflow_purchase_order_5.png)

#### **Descrição dos Campos**

* **Title**\
  O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_\
  Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type**\
  Menu suspenso listando todos os tipos de documentos disponíveis.\
  Isso determina a qual tipo de documento esta configuração de exportação se aplica.

- **ION Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.
- **IDM Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos.\
  [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **M3 toml Mapping File**\
  Selecione um arquivo de mapeamento do gerenciador de arquivos ou use a opção selecionar Toml para usar um toml criado com o gerenciador de regras.\
  [Precisa de ajuda para criar um? Veja o Guia do Gerenciador de Regras](rule-manager/)

</details>
