# Como Criar Acesso ao Banco de Dados para um Usuário Específico da Organização

### **1. Faça Login no Docbits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Vá para a página de login da sua aplicação.
2. Insira suas credenciais (nome de usuário e senha) para fazer login.

### **2. Acesse as Configurações** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Uma vez logado, localize o ícone de **Configurações** (engrenagem ⚙️) na barra lateral esquerda.
2. Clique em **Configurações** para abrir o painel de configuração do sistema.

### **3. Abra o Módulo de Processamento de Documentos** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. Nas **Configurações**, localize a seção **Processamento de Documentos**.
2. Em **Processamento de Documentos**, encontre e clique na opção **Módulo**.
   * Isso abrirá a página de configuração do módulo relevante onde você pode prosseguir com a criação do usuário para o banco de dados.

<figure><img src="../../../../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

### 4. Passos para Habilitar e Acessar o Usuário de Documentos de IA e Banco de Dados: <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Alternar Recursos**:
   * Use os interruptores à direita para habilitar ou desabilitar recursos específicos:
     * **Armazém de Documentos de IA**: Ative isso para habilitar o acesso aos recursos relacionados à IA.
     * **Acesso ao BD**: Ative isso para conceder acesso ao banco de dados ao usuário.

<figure><img src="../../../../../.gitbook/assets/image (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

2. **Credenciais do Banco de Dados**:
   * O painel fornece os seguintes detalhes de conexão com o banco de dados:
     * **Nome de usuário**: Um nome de usuário único é exibido.
     * **Senha**: Certifique-se de que a senha seja armazenada ou copiada com segurança.
     * **Banco de dados**: É o nome do Banco de Dados.
     * **Host**: Nome do Host.
     * **Porta**: É a Porta.
     * **Modo SSL:** A conexão requer `sslmode=require` para comunicação segura.
3. **Copiando Credenciais**:
   * Use os ícones de cópia ao lado de cada campo para copiar rapidamente as credenciais para uso em seu cliente de banco de dados ou aplicativo.
4. **Conexão via DBeaver:**
   *   Conectar via Host

       * escolha PostgreSQL

       <figure><img src="../../../../../.gitbook/assets/image (2) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

       * Preencha as informações necessárias

       <figure><img src="../../../../../.gitbook/assets/image (4) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

       * mude para a guia SSL e marque Usar SSL. Mova para baixo para o modo SSL e selecione require

       <figure><img src="../../../../../.gitbook/assets/image (3) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
   *   Conectar via URL

       * Preencha as informações necessárias:
         - substitua Host pelas informações de host fornecidas
         - substitua Porta pelas informações de porta fornecidas
         - substitua Banco de dados pelas informações de banco de dados fornecidas
         - para Nome de usuário selecione as informações de nome de usuário fornecidas
         - para Senha selecione as informações de senha fornecidas

       <figure><img src="../../../../../.gitbook/assets/image (5) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
5. **Testar a Conexão**:
   * Clique no botão **"Testar Conexão"** para garantir que as credenciais e os detalhes da conexão estejam corretos.
   * Se o teste for bem-sucedido, prossiga para conectar.
6. **Explorar o Banco de Dados**:
   * Uma vez conectado, navegue até a seção **esquema** ou **tabelas** em seu cliente de banco de dados.
   * Verifique as tabelas disponíveis.
