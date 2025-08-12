---
layout: vibecoding-default
title: "Tempo Labs Volume 2: MCP App Store, Styling Panel V2, přihlášení přes Google a několik dalších úprav"
date: 2025-06-10
---

Tempo Labs, startup z akcelerátoru Y Combinator S23, představil 9. června 2025 druhý souhrnný **balík novinek s názvem Volume 2**. Na svém účtu X stručně vyjmenoval hlavní přírůstky – MCP App Store, Styling Panel V2, přihlášení přes Google a několik dalších úprav. Níže si rozeberme, co jednotlivé novinky znamenají pro vývojáře používající Tempo jako AI-asistované IDE.

První položkou je **MCP App Store**, marketplace integrovaný do postranního panelu editoru. Uživatel vybere službu, vloží její API klíč a během zhruba jedné minuty se v canvasu objeví plně konfigurovaná funkce – například pro Stripe, OpenAI nebo Firecrawl – přičemž všechny meta­údaje ukládá protokol Model Context Protocol . Krátké video-demo ukazuje, jak agent po přidání klíče generuje volání API přímo do React komponenty i chatového rozhraní . Při uvedení na Product Hunt 29. května získal App Store více než 240 hlasů a stal se jedním z nejsledovanějších vývojářských nástrojů dne . MCP přitom abstrahuje volání externích služeb do manifestu, k němuž mají přístup Tempo agenti; LLM tak může deterministicky vytvářet „function-calling“ prompty, zatímco vývojář se soustředí na logiku a UI .

Druhou výraznou novinkou je **Styling Panel V2**. Podle oficiálního oznámení přenáší „code-level control into a visual interface“, což v praxi znamená, že změny provedené posuvníkem zapisují Tailwind utility třídy přímo do atributu className a rozdíl je okamžitě vidět v kódu . Video „Designers Can Code Too“ pak demonstruje plynulý přechod mezi vizuálním režimem a editorem bez reloadu preview . Profil firmy na Y Combinatoru dodává, že panel je součástí širšího upgradu zaměřeného na přesnější ovládání rozvržení bez odchodu z Tempo prostředí .

Volume 2 také odstraňuje bariéru při registraci: vedle GitHub účtu lze nyní Tempo založit přes **Google OAuth 2** nebo prostý email. Možnost je vidět přímo na sign-up obrazovce aplikace  a firemní post vysvětluje, že díky tomu mohou nástroj vyzkoušet i týmy bez Git workflow .

Pro společnosti spoléhající na **GitLab** přibyla obousměrná integrace repozitáře. Webhooky na push i Merge Request události synchronizují změny mezi kódem a vizuálním canvasem, jak popisuje oznámení ze 4. června .

V agentním rozhraní lze nově zvolit model **Claude 4.0**. Tým Tempo jej aktivoval hned po oficiálním uvedení Anthropicem a prezentoval v krátkém teaseru na X . Uživatel zvolí model v dropdownu chatu a prompt se automaticky přizpůsobí jeho rozhraní function-calling.

Balík zahrnuje i interní optimalizace: podle interního updatu běží buildy a preview instance nově na „Tempo on Tempo“, což urychlilo inicializaci a umožnilo designérům odesílat produkční PR bez ručního psaní kódu .

Celkově Volume 2 nerozšiřuje Tempo o jedinou velkou funkci, ale o sadu navzájem provázaných vylepšení: App Store snižuje náklady na integraci třetích stran, Styling Panel V2 přibližuje editaci kódu nedesignérům, rozšířené přihlášení zpřístupňuje platformu širší veřejnosti a GitLab integrace sjednocuje workflow napříč repozitáři. Aktivace Claude 4.0 a výkonové úpravy pak posouvají Tempo blíže k vizi „AI-as-middleware“, které orchestruje kód, design i API kontext v jedné nadstavbě.
