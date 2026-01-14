# Configurando Propriedades de Campo

## Instruções detalhadas sobre a definição de propriedades como Obrigatório, Somente Leitura, Oculto e OCR.

### Obrigatório (Required):

<figure><img src="../../../../../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

Se um campo estiver marcado como Obrigatório, significa que este campo deve ser preenchido antes que o documento possa ser salvo ou processado.

**Para definir esta propriedade:**

* Navegue até as configurações do campo no seu sistema DocBits.
* Ative a opção Obrigatório para o campo relevante.

**Impacto:**

* Esta configuração garante que informações importantes sejam capturadas e que nenhum documento possa ser processado sem os dados obrigatórios.

### Somente Leitura (Read Only):

<figure><img src="../../../../../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>

Se um campo estiver marcado como Somente Leitura, significa que os usuários podem ver o conteúdo deste campo, mas não podem fazer nenhuma alteração nele.

**Para definir esta propriedade:**

* Vá para as Opções de Campo. Ative a opção Somente Leitura para o campo desejado.

**Impacto:**

* Esta configuração pode ser útil para proteger informações sensíveis ou para garantir que dados importantes não sejam alterados acidentalmente.

### Oculto (Hidden):

<figure><img src="../../../../../.gitbook/assets/image (113).png" alt=""><figcaption></figcaption></figure>

Se um campo estiver marcado como "Oculto", significa que o campo ficará escondido na interface do usuário e os usuários não poderão vê-lo nem acessá-lo.

**Para definir esta propriedade:**

* Vá para as opções do campo.
* Ative a opção "Oculto" para o campo correspondente.

**Impacto:**

* Esta configuração é frequentemente usada para ocultar campos internos ou técnicos que são irrelevantes para o usuário final ou que são necessários apenas para processamento interno.

### OCR (Reconhecimento Óptico de Caracteres):

<figure><img src="../../../../../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

Se um campo estiver configurado para OCR, significa que o sistema tentará extrair o texto do documento e inseri-lo neste campo. Esta configuração é geralmente usada para campos que devem ser preenchidos automaticamente.

**Para configurar isso:**

* Ative a opção OCR para o campo correspondente.
* Se necessário, configure os parâmetros de OCR, como idioma, fonte, etc.

**Impacto:**

* O uso de OCR permite que os documentos sejam processados automaticamente, extraindo informações de textos e inserindo-as nos campos apropriados, reduzindo o esforço manual e aumentando a eficiência.

### Validação forçada (Forced validation):

<figure><img src="../../../../../.gitbook/assets/image (115).png" alt=""><figcaption></figcaption></figure>

Configure as regras de validação adequadamente, como limites numéricos, expressões regulares ou relações com outros campos.

**Para configurar isso:**

* Salve as alterações.

**Impacto:**

* A validação forçada verifica os dados inseridos em relação aos critérios especificados para garantir que sejam válidos. Isso ajuda a detectar erros precocemente e a melhorar a qualidade dos dados.

### Pontuação de Correspondência (Match Score):

<figure><img src="../../../../../.gitbook/assets/image (116).png" alt=""><figcaption></figcaption></figure>

Ao comparar os dados de entrada com os dados de referência, o Match Score pode ajudar a confirmar a precisão e a validade dos dados. Se o Match Score exceder um determinado limite, a correspondência é considerada bem-sucedida.

**Para configurar isso:**

* Ative a opção Match Score e defina o limite desejado.
* Salve as alterações.

**Impacto:**

* O Match Score é usado para avaliar a precisão das correspondências entre os dados de entrada e os valores de referência. Se a pontuação obtida exceder o limite definido, a correspondência é considerada bem-sucedida. Isso é especialmente útil para campos que exigem validação de dados ou correspondência de dados, como campos com nome, endereço de e-mail, etc. por exemplo, ao verificar dados de clientes.

<figure><img src="../../../../../.gitbook/assets/image (117).png" alt="" width="258"><figcaption></figcaption></figure>

Ao configurar cuidadosamente essas propriedades de campo, você pode otimizar os fluxos de trabalho de processamento de documentos e garantir que seus dados sejam capturados corretamente, protegidos e processados com eficiência.
