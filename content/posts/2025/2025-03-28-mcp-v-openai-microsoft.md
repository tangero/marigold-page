---
slug: 'mcp-v-openai-microsoft'

audio_url: null
categories:
- MCP
- vibe code
- AI
date: 2025-03-28 08:00:00
summary_points:
- MCP získal masivní podporu napříč desítkami platforem.
- OpenAI oznámila podporu MCP napříč svými produkty.
- Microsoft integruje MCP do Copilot Studio a Azure AI Foundry.
- Zapier integruje MCP pro přístup k tisícům aplikací.
thumbnail: https://ia.salesianssarria.com/wp-content/uploads/2025/03/model-context-protocol-salesians-sarria-768x427.jpg
title: MCP získává širokou podporu včetně OpenAI a Microsoftu
---

V posledních pár dnech se doslova strhla lavina novinek okolo [MCP](/ai/mcp/), neboli Model Context Protocolu. Nově ji bude podporovat také OpenAI, Microsoft a objevila se v celé řadě dalších služeb. Což je pro šíření tohoto standardu důležité. Takže si dejme sumář novinek! Jen pro jistotu upozorňuji, že článek je spíše pro lidi, kteří se chtějí hrabat maličko pod kapotou, MCP servery jsou rozšíření promptování, které má smysl dělat, když chcete napojovat nějaká svoje (či i cizí) data... 

MCP jako standardizovaná vrstva pro komunikaci mezi jazykovými modely a nástroji třetích stran dostala v uplynulém týdnu masivní podporu napříč desítkami platforem. Díky ní je možné celou řadu služeb online propojit s AI modelem a nevyužívat jen "stará" data, která se do modelu dostala při učení a ani se do něj dostat nemusely. Můžete tak připojit i svoje či jiná uživatelská data. MCP sjednocuje komunikaci napříč různými aplikacemi a službami – ať už jde o cloudová úložiště, databáze, návrhové nástroje nebo interní firemní systémy.

Pojďme se pro instpiraci podívat na nejdůležitější napojení MCP z poslední doby. 

### ✨ OpenAI přijímá standard konkurence
Hned v úvodu je třeba zmínit, že největší zpráva přišla od OpenAI, která oznámila podporu MCP napříč svými produkty. Sam Altman osobně potvrdil, že lidé MCP milují a OpenAI chce rozšířit podporu tohoto protokolu. MCP je už nyní dostupný [v SDK pro agent](https://openai.github.io/openai-agents-python/mcp/) a brzy přibude také podpora pro desktopovou aplikaci ChatGPT a responses API. To je významný krok, protože OpenAI přijímá standard původně vyvinutý konkurenční společností Anthropic. MCP se může stát univerzálním standardem pro interakce mezi AI a externími nástroji. Teď to chce ještě podporu v [[DeepSeek](/item/deepseek/)](/deepseek/) a Google Gemini, u číňanů bych viděl problém spíše v času, než že by nechtěli a Google snad nenapadne pro Gemini dělat něco vlastního... 

### Microsoft také přináší MCP do svého portfolia
Shinya Yanagihara oznámil integraci MCP do Microsoft Copilot Studio, vývojářské platformy pro tvorbu vlastních Copilot chatbotů a asistentů. Tato implementace zjednodušuje integraci AI aplikací a agentů v prostředí Microsoft. Zároveň došlo k [integraci MCP s Microsoft Azure AI Foundry](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/), cloudovou platformou pro vývoj AI řešení, což umožňuje AI modelům dynamicky přistupovat k nástrojům a informacím. Vysvětlení je tady prosté, Microsoft používá OpenAI a jeho podpora MCP se tedy promítla, ale samozřejmě to kluci mohli zablokovat, naštěstí to neudělali a to je pro Azure uživatele důležité.

### 🔌 Zapier: AI konečně ovládá 8000+ aplikací

Jedním z nejvýraznějších oznámení týdne je integrace MCP do platformy Zapier, což je populární nástroj pro automatizaci workflow. Díky tomu získávají modely přístup ke 30 000+ akcím napříč více než osmi tisíci aplikacemi – bez nutnosti psát jakékoliv API volání. Detailní popis spolu s implementací a také u konkurenční služby Make.com jsme [si již přinesli](/item/zapier.mcp), takže další podívání vynecháme. 

### 🐫 Camel-AI: Toolkit pro pokročilé agentní systémy

Platforma [Camel AI](https://www.camel-ai.org), zaměřená na vývoj multiagentních architektur, uvedla MCP Toolkit, který umožňuje propojit agenty s externími nástroji bez potřeby budovat vlastní konektory. CAMEL tím zásadně rozšiřuje své možnosti a agenti se díky MCP stávají skutečně „hands-on“ – mohou manipulovat s reálnými systémy. Vývojáři CAMELu navíc ohlásili integraci s AgentOps, což je platforma pro orchestraci agentů v produkčním nasazení.

### 🧠 LiteLLM a univerzální proxy pro modely

Další zajímavou možnost skýtá podpora MCP v projektu [LiteLLM](https://www.litellm.ai), který funguje jako sjednocující rozhraní pro různé LLM (Claude, Mistral, OpenAI aj.). Nově může LiteLLM fungovat jako MCP bridge, tedy jakýsi překladač, který zpřístupňuje MCP nástroje všem podporovaným modelům.

To otevírá dveře k „agent-agnostickému“ vývoji – můžete nasadit nástroj jednou a použít ho v jakémkoliv prostředí, které LiteLLM podporuje.

### 📦 Box, Telegram, Figma, iOS – a další "drobnosti"

V rámci MCP boomu jsme zaznamenali i následující novinky:
- Box (resp komunita kolem něj) předvedl [ukázku MCP serveru](https://github.com/box-community/mcp-server-box) s podporou modelu Claude od Anthropic – AI může přímo spravovat soubory v cloudovém úložišti.
- [Telegram MCP server](https://github.com/sparfenyuk/mcp-telegram) umožňuje, aby agenti AI posílali zprávy, čtou historii chatu nebo spravovali skupiny.
- Cursor x Figma: Projekt „[Talk to Figma(https://github.com/sonnylazuardi/cursor-talk-to-figma-mcp)]“ umožňuje AI upravovat návrhy ve Figmě čistě na základě přirozeného jazyka – bez kódu.
- [iOS Simulator MCP](https://github.com/atom2ueki/mcp-server-ios-simulator): Vývojáři mohou nyní používat agenty ke spuštění a testování aplikací v iOS simulátoru. Skvělé pro QA scénáře.
- [Neon Database](https://neon.tech/guides/neon-mcp-server): nativní podpora MCP a zároveň napojení na Azure AI Agent Service – vývoj komplexních agentních systémů s přímým přístupem k databázím je o krok blíž.

### 🛠 Haystack, Cursor, Firecrawl, Fleek, Brex…

Tím výčet nekončí:
- Haystack AI [implementuje MCP](https://haystack.deepset.ai/integrations/mcp) pro rozšiřování pipeline o externí nástroje.
- [Firecrawl](https://github.com/mendableai/firecrawl-mcp-server/) ve spojení s MCP umožňuje AI klonovat weby jen na základě textového zadání.
- Fleek vytvořil [MCP plugin pro ElizaOS](https://github.com/fleek-platform/eliza-plugin-mcp), čímž umožňuje frameworkům AI přístup ke všem REST API bez potřeby psát vlastní kód.
- Brex získal vlastní [MCP server](https://github.com/crazyrabbitLTC/mcp-brex-server/blob/main/README.md), díky němuž může Claude nebo jiný model zpracovávat vaše účetní výdaje. Opatrně! (ale u nás se Brex asi moc nepoužívá)

### 🌀 Spiral MCP Server pro Spiral Computer
Jason Liu publikoval [Spiral MCP Server](https://github.com/jxnl/spiral-mcp), implementaci [[Model Context Protocol](/ai/mcp/)](/model-context-protocol/) v Pythonu pro Spiral Computer od společnosti Every (nástroj pro interaktivní práci s dokumenty a informacemi). Tento server poskytuje čtyři MCP nástroje (list_models, generate, atd.), zpracovává text, soubory a URL adresy s chytrou extrakcí článků a podporuje asynchronní operace.

### 🦗 Rhino/Grasshopper MCP server
Nikhil Bang sdílel ukázku svého MCP serveru pro Rhino/Grasshopper, populární platformu pro 3D modelování a parametrický design využívanou architekty a designéry. Server umožňuje propojit a ovládat Rhino a Grasshopper pomocí Claude LLM. Toto propojení otevírá nové možnosti pro automatizaci návrhových procesů v oblasti 3D modelování a generativního designu.

### 🕹️ KiCad MCP Server: AI v elektronickém designu
[KiCad MCP Server](https://github.com/lamaalrajih/kicad-mcp) je další specializovanou implementací, která umožňuje interakci s KiCad, open-source softwarem pro návrh elektronických schémat a plošných spojů. Uživatelé mohou pomocí přirozeného jazyka zobrazovat projekty, analyzovat návrhy PCB, spouštět kontroly návrhových pravidel a vizualizovat PCB layouty.

A vznikla také celá řada serverů, které nabízejí odkazy na nejrůznější MCP služby, vygooglujete je snadno, například [Awesome MCP Servers](https://mcpservers.org) ... 

Tak šťastné experimentování.