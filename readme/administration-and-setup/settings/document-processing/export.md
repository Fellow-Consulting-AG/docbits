# Exportar

## Visão Geral

A página de Exportar exibe todas as configurações de exportação configuradas, incluindo se estão ativas ou inativas. A partir daqui, os usuários podem:

* Visualizar e gerenciar as configurações de exportação existentes
* Criar novas conexões de exportação (por exemplo, para **Infor**, **Infor & IDM**, **Webhook** ou **SFTP**)
* Editar ou excluir as configurações de exportação existentes

## Onde Encontrar

Você pode encontrá-lo em: **Configurações** → **Processamento de Documentos** → **Exportar**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn6ldlcI2sVUEgDdWb9U4%252Fimage.png%3Falt%3Dmedia%26token%3D8368818d-c899-4bee-ad21-a631d6be5c20\&width=768\&dpr=4\&quality=100\&sign=fbfcbd0c\&sv=2)

## **Usando a Página de Exportação**

Quando você abre a página de Exportar, verá uma lista de todas as configurações de exportação existentes.

Cada linha na lista mostra:

* **Indicador de Status**
  * **Verde** significa que a exportação está ativa
  * **Vermelho** significa que a exportação está desativada
* **Nome** – o nome da configuração de exportação
* **Tipo de Documento** – o tipo de documento para o qual a exportação está configurada
* **Sub-Organização** – se a exportação é limitada a uma sub-organização específica
* **Método de Exportação** – para onde o documento será enviado (por exemplo, Infor, IDM, SFTP)
* **Ações** – botões para **editar, excluir** ou **ativar/desativar** a configuração

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyN87I5gzXxwGoAqC6zMF%252Fimage.png%3Falt%3Dmedia%26token%3D7df9d573-7e57-4ace-99c6-15a83691b926\&width=768\&dpr=4\&quality=100\&sign=6221cb80\&sv=2)

#### **Regras Importantes para Configuração de Exportação**

Para cada **tipo de documento** **dentro de uma organização ou sub-organização específica**, aplicam-se as seguintes regras:

* Você pode ter **apenas uma exportação Infor ativa**
* Você pode ter **apenas uma exportação não-Infor ativa** (por exemplo, Webhook, SFTP)

No entanto, é possível ter:

* **Uma exportação Infor ativa** _e_ **uma exportação não-Infor ativa** ao mesmo tempo para o mesmo tipo de documento
* **Configurações de exportação diferentes para diferentes sub-organizações** — por exemplo, uma exportação Infor para Sub-Org A e outra exportação Infor para Sub-Org B

## **Criando uma Nova Exportação**

Para criar uma nova exportação:

1. Clique no botão **“Novo”**. \
   ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FTsHrIAUpe7EqenIzNAaJ%252Fimage.png%3Falt%3Dmedia%26token%3Dd2dbc996-b129-443c-a8df-9927a6f43a36\&width=300\&dpr=4\&quality=100\&sign=8769c331\&sv=2)
2. Selecione o **Tipo de Exportação** que deseja configurar (por exemplo, Infor, IDM, SFTP).
3. Preencha os campos obrigatórios com base no tipo de exportação.
4. Salve a configuração.

## Opções de Exportação

#### Webhook

<details>

<summary>Webhook</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCwXUqFdCbRI5lRW49ymw%252Fimage.png%3Falt%3Dmedia%26token%3D798c0f40-6c4a-4650-9320-af2c17634fe9\&width=768\&dpr=4\&quality=100\&sign=15836833\&sv=2)

#### **Descrições de Campo**

* **Título** O nome da configuração de exportação. Isso aparecerá na lista de exportação.
* **Sub-Organização** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado em branco: aplica-se à organização principal.
  * Se selecionado: a exportação se aplicará apenas à sub-organização escolhida.
* **Tipo de Documento** Menu suspenso listando todos os tipos de documento disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **URL de Exportação** O URL de destino onde o documento deve ser exportado.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzwUCWTdFETTvuTGl8qAn%252Fimage.png%3Falt%3Dmedia%26token%3D3f94b210-0128-4710-ae69-150a1363ce49\&width=768\&dpr=4\&quality=100\&sign=4ecd353\&sv=2)

#### **Descrições de Campo**

* **Título** O nome da configuração de exportação. Isso aparecerá na lista de exportação.
* **Sub-Organização** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado em branco: aplica-se à organização principal.
  * Se selecionado: a exportação se aplicará apenas à sub-organização escolhida.
* **Tipo de Documento** Menu suspenso listando todos os tipos de documento disponíveis. Isso determina a qual tipo de documento essa configuração de exportação se aplica.
* **Nome de Usuário** O nome de usuário usado para autenticar-se no servidor SFTP.
* **Senha** A senha correspondente para a conta SFTP. Certifique-se de que a conta tenha acesso de gravação à pasta especificada.
* **URL do Servidor** O nome do host ou endereço IP do servidor SFTP de destino.
* **Porta** A porta usada para se conectar ao servidor SFTP.
* **Pasta** O caminho no servidor SFTP onde os documentos devem ser enviados (por exemplo, `/incoming/invoices/`). Deve existir e ser gravável.
*   **Arquivo XSLT (Opcional)**

    O **arquivo XSLT** permite a transformação do formato de exportação padrão do DocBits.

    * **Quando usar:** Somente se o sistema receptor exigir uma estrutura diferente ou formatação específica que difere do padrão do DocBits.
    * **Deixe em branco** se o formato de exportação padrão atender aos requisitos.

</details>

#### Exportar informações para SFTP

<details>

<summary>Exportar informações para SFTP</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FU0W4Qdy7ZlNoCn3E9wX5%252Fimage.png%3Falt%3Dmedia%26token%3D33673a12-55c4-479b-8ca8-b7c95e7a6a89\&width=768\&dpr=4\&quality=100\&sign=4af07f48\&sv=2)

#### **Descrições dos Campos**

* **Título** O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organização** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado em branco: aplica-se à organização principal.
  * Se selecionado: a exportação se aplicará apenas à sub-organização escolhida.
* **Tipo de Documento** Menu suspenso listando todos os tipos de documento disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **Arquivo de Mapeamento IDM** Selecione um arquivo de mapeamento do gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Arquivo de Mapeamento BOD** Selecione um arquivo de mapeamento do gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Pasta** O caminho no servidor SFTP onde os documentos devem ser enviados (por exemplo, `/incoming/invoices/`). Deve existir e ser gravável.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6e4B9BWQWgHvcHhduXKb%252Fimage.png%3Falt%3Dmedia%26token%3D09e9534e-9268-4221-bd7b-89b621c80670\&width=768\&dpr=4\&quality=100\&sign=b03835a\&sv=2)

#### **Descrições de Campo**

* **Título** O nome da configuração de exportação. Isso aparecerá na lista de exportação.
* **Sub-Organização** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado em branco: aplica-se à organização principal.
  * Se selecionado: a exportação se aplicará apenas à sub-organização escolhida.
* **Tipo de Documento** Menu suspenso listando todos os tipos de documento disponíveis. Isso determina a qual tipo de documento essa configuração de exportação se aplica.
* **Nome de Usuário** O nome de usuário usado para se conectar ao compartilhamento SMB.
* **Senha** A senha correspondente para autenticação SMB.
* **URL do Servidor** O endereço do servidor SMB.
* **Porta** Número da porta usado para acessar o compartilhamento SMB.
* **Pasta** O caminho da pasta dentro do compartilhamento SMB onde os documentos devem ser salvos (por exemplo, `/incoming/invoices/`). Deve existir e ser gravável.
*   **Arquivo de Mapeamento JPL (Opcional)**

    O **arquivo JPL** é usado para definir uma transformação dos dados exportados antes de serem gravados no compartilhamento SMB.

    * **Quando usar:** Somente quando os dados do documento exportado precisam ser ajustados para corresponder ao formato externo ou às expectativas do sistema.
    * **Deixe vazio** se nenhuma transformação for necessária.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FQ1AtdmTRZr1sGkH6oLwP%252Fimage.png%3Falt%3Dmedia%26token%3D720a4184-3f91-4b70-b3da-b846f3cce030\&width=768\&dpr=4\&quality=100\&sign=dc678c2c\&sv=2)

#### **Descrições de Campo**

* **Título** O nome da configuração de exportação. Isso aparecerá na lista de exportação.
* **Sub-Organização** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado em branco: aplica-se à organização principal.
  * Se selecionado: a exportação se aplicará apenas à sub-organização escolhida.
* **Tipo de Documento** Menu suspenso listando todos os tipos de documento disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **Arquivo de Mapeamento ION** Selecione um arquivo de mapeamento no gerenciador de arquivos.
* **Arquivo de Mapeamento IDM** Selecione um arquivo de mapeamento no gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Alternar Nuvem / Local** Uma chave para indicar o tipo de implantação da Infor:
  * **Nuvem**: Selecione isso se for cliente do Infor CloudSuite.
  * **Local**: Selecione isso se a Infor for auto-hospedada.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FcYDXwDYH4RSc5vcY4fmr%252Fimage.png%3Falt%3Dmedia%26token%3Da9cfac80-9795-4e8f-a664-e268c9b4856c\&width=768\&dpr=4\&quality=100\&sign=5a4b0bd0\&sv=2)

#### **Descrições de Campos**

* **Título** O nome da configuração de exportação. Isso aparecerá na lista de exportação.
* **Sub-Organização** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado em branco: aplica-se à organização principal.
  * Se selecionado: a exportação se aplicará apenas à sub-organização escolhida.
* **Tipo de Documento** Menu suspenso listando todos os tipos de documento disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **Arquivo de Mapeamento ION** Selecione um arquivo de mapeamento no gerenciador de arquivos.
* **Arquivo de Mapeamento BOD** Selecione um arquivo de mapeamento no gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Alternar Nuvem / Local** Uma chave para indicar o tipo de implantação da Infor:
  * **Nuvem**: Selecione isso se for um cliente Infor CloudSuite.
  * **Local**: Selecione isso se a Infor for auto-hospedada.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FY13EX2xxOKLZzliAAHB0%252Fimage.png%3Falt%3Dmedia%26token%3D94335922-6342-405f-8c6d-29fdf2f31a2e\&width=768\&dpr=4\&quality=100\&sign=c0322806\&sv=2)

#### **Descrições de Campo**

* **Título** O nome da configuração de exportação. Isso aparecerá na lista de exportação.
* **Sub-Organização** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado em branco: aplica-se à organização principal.
  * Se selecionado: a exportação se aplicará apenas à sub-organização escolhida.
* **Tipo de Documento** Menu suspenso listando todos os tipos de documento disponíveis. Isso determina a qual tipo de documento essa configuração de exportação se aplica.
* **Arquivo de Mapeamento ION** Selecione um arquivo de mapeamento no gerenciador de arquivos.
* **Arquivo de Mapeamento IDM** Selecione um arquivo de mapeamento no gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Arquivo de Mapeamento BOD** Selecione um arquivo de mapeamento no gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Alternar Nuvem / Local** Um interruptor para indicar o tipo de implantação da Infor:
  * **Nuvem**: Selecione isso se for cliente Infor CloudSuite.
  * **Local**: Selecione isso se a Infor for auto-hospedada.

</details>

### Para clientes Infor CloudSuite

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4SfGDqhA4KDrPfJ5vcsT%252Fimage.png%3Falt%3Dmedia%26token%3D4833c0dc-af8b-48a1-a977-6cc8ded20277\&width=768\&dpr=4\&quality=100\&sign=6301596\&sv=2)

#### **Descrições de Campo**

* **Título** O nome da configuração de exportação. Isso aparecerá na lista de exportação.
* **Sub-Organização** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado em branco: aplica-se à organização principal.
  * Se selecionado: a exportação se aplicará apenas à sub-organização escolhida.
* **Tipo de Documento** Menu suspenso listando todos os tipos de documento disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **Arquivo de Mapeamento ION** Selecione um arquivo de mapeamento no gerenciador de arquivos.
* **Arquivo de Mapeamento IDM** Selecione um arquivo de mapeamento no gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Arquivo de Mapeamento LN** Selecione um arquivo de mapeamento no gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Exemplo de Mapeamento LN](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAN4T0aQEoogbUA8PUgy9%252Fimage.png%3Falt%3Dmedia%26token%3Da2b91153-858f-4711-abcc-4ed7ad60d49a\&width=768\&dpr=4\&quality=100\&sign=bb6bda83\&sv=2)

#### **Descrições dos Campos**

* **Título** O nome da configuração de exportação. Isso aparecerá na lista de exportação.
* **Sub-Organização** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado em branco: aplica-se à organização principal.
  * Se selecionado: a exportação se aplicará apenas à sub-organização escolhida.
* **Tipo de Documento** Menu suspenso listando todos os tipos de documentos disponíveis. Isso determina a qual tipo de documento essa configuração de exportação se aplica.
* **Arquivo de Mapeamento ION** Selecione um arquivo de mapeamento no gerenciador de arquivos.
* **Arquivo de Mapeamento IDM** Selecione um arquivo de mapeamento no gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Arquivo de Mapeamento M3** Selecione um arquivo de mapeamento no gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Exemplo de Mapeamento M3](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCdoduCkkbnomw3ahZgul%252Fimage.png%3Falt%3Dmedia%26token%3D4e5c7d08-5eaf-4c3e-9918-5cce58d8e3b3\&width=768\&dpr=4\&quality=100\&sign=e984c4e0\&sv=2)

#### **Descrições de Campo**

* **Título** O nome da configuração de exportação. Isso aparecerá na lista de exportação.
* **Sub-Organização** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado em branco: aplica-se à organização principal.
  * Se selecionado: a exportação se aplicará apenas à sub-organização escolhida.
* **Tipo de Documento** Menu suspenso listando todos os tipos de documentos disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **Arquivo de Mapeamento ION** Selecione um arquivo de mapeamento no gerenciador de arquivos.
* **Arquivo de Mapeamento IDM** Selecione um arquivo de mapeamento no gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Arquivo de Mapeamento M3 toml** Selecione um arquivo de mapeamento no gerenciador de arquivos ou use a opção Toml selecionar para usar um toml criado com o gerenciador de regras. [Precisa de ajuda para criar um? Veja o Guia do Gerenciador de Regras](https://docs.docbits.com/administration-and-setup/settings/document-processing/rule-manager)

</details>

