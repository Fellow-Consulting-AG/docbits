# Campos

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.02.31.png" alt=""><figcaption></figcaption></figure>

#### Visão Geral

A configuração de Campos fornece uma interface de usuário onde os administradores podem gerenciar as propriedades e o comportamento dos campos de dados individuais associados a um tipo de documento. Cada campo pode ser ajustado para otimizar a precisão e eficiência da captura e validação de dados.

#### Principais Recursos e Opções

1. **Configuração de Campos**:
* **Nomes dos Campos**: Lista os nomes dos campos, geralmente correspondentes aos elementos de dados dentro do documento, como "Número da Fatura" ou "Data do Pedido de Compra".
* **Obrigatório**: Os administradores podem marcar campos como obrigatórios, garantindo que os dados devem ser inseridos ou capturados para que esses campos completem o processamento do documento.
* **Somente Leitura**: Os campos podem ser definidos como somente leitura para evitar modificações após a captura de dados ou durante certas etapas do processamento do documento.
* **Oculto**: Os campos podem ser ocultos da visualização na interface do usuário, útil para informações sensíveis ou para simplificar os fluxos de trabalho do usuário.
2. **Configurações Avançadas**:
* **Forçar Validação**: Garante que os dados inseridos em um campo passem por certas regras de validação antes de serem aceitos.
* **OCR (Reconhecimento Óptico de Caracteres)**: Este interruptor pode ser ativado para habilitar o processamento de OCR para um campo específico, útil para extração automatizada de dados de documentos digitalizados ou digitais.
* **Pontuação de Correspondência**: Os administradores podem definir uma pontuação de correspondência, um limiar usado para determinar o nível de confiança no reconhecimento ou correspondência de dados, impactando como a validação de dados e os controles de qualidade são realizados.
3. **Botões de Ação**:
* **Criar Novo Campo**: Permite adicionar novos campos ao tipo de documento.
* **Ícones de Edição**: Cada campo possui um ícone de edição que permite aos administradores configurar ainda mais as configurações específicas do campo, como tipo de dados, valores padrão ou lógica de negócios conectada.
* **Salvar Configurações**: Confirma as alterações feitas nas configurações do campo.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2494" %}
