---
author: Patrick Zandl
categories:
- AI
- Mistral AI
- LLM
- vývoj
- API
layout: post
post_excerpt: Mistral AI Studio nabízí vývojářům jednotné prostředí pro práci s modely včetně pokročilého promptování, správy agentů a komplexního playground režimu s podporou Batch API.
summary_points:
- Mistral AI spustil AI Studio jako komplexní platformu pro vývoj a testování aplikací s jazykovými modely
- Playground umožňuje pokročilé nastavení parametrů, práci s prompty a testování s více modely současně
- Agent Builder podporuje vytváření agentů s nástroji, znalostními bázemi a možností sdílení
- Batch API zpracovává velké objemy požadavků s 50% slevou oproti standardní ceně
- Platforma nabízí přístup ke všem modelům Mistral včetně Pixtral Large a Codestral
- Fine-tuning umožňuje doladění vlastních modelů na specifická data
title: Mistral představil AI Studio pro lepší ladění LLM 
thumbnail: https://www.marigold.cz/assets/marketecture-ai-studio.png
---

Mistral AI představil AI Studio, vývojářskou platformu určenou pro práci s jazykovými modely. Jde o konsolidaci nástrojů, které firma dosud nabízela odděleně - od playground prostředí přes správu API klíčů až po nástroje pro fine-tuning. Platforma cílí na vývojáře, kteří potřebují testovat prompty, vytvářet agenty nebo zpracovávat požadavky v dávkách.

## Playground s pokročilými funkcemi

Základem platformy je playground režim, kde mohou vývojáři testovat různé konfigurace modelů. Prostředí nabízí přístup ke všem modelům Mistral, včetně multimodálního [Pixtral Large](https://mistral.ai/news/pixtral-large/) s kapacitou 123 miliard parametrů nebo specializovaného [Codestral](https://mistral.ai/news/codestral/) pro generování kódu.

![Mistral AI Studio Playground](/assets/marketecture-ai-studio.png)

Vývojáři moví nastavovat parametry jako teplotu, top-p hodnotu nebo maximální délku odpovědi. Playground podporuje režim multi-turn konverzací, kde lze vytvářet komplexnější dialogy s udržováním kontextu. Systém umožňuje paralelní testování s více modely najednou, což zjednodušuje porovnání výsledků různých konfigurací.

Součástí je knihovna předpřipravených šablon promptů pro typické úlohy - od summarizace textu přes extrakci informací až po generování kódu. Tyto šablony lze upravovat a ukládat pro pozdější použití. Vývojáři mohou exportovat úspěšné konfigurace přímo do produkčního kódu s vygenerovanými ukázkami pro Python, JavaScript nebo cURL.

## Správa promptů a verzování

Platforma obsahuje systém pro správu promptů napříč projekty. Vývojáři mohou vytvářet, ukládat a verzovat prompty včetně systémových instrukcí a příkladů. Každý prompt má vlastní historii změn, což umožňuje návrat k předchozím verzím nebo porovnání výsledků mezi různými iteracemi.

![Správa promptů v Mistral AI Studio](/assets/observability.webp)

Systém podporuje parametrizaci promptů pomocí proměnných, které lze dynamicky vyplňovat při volání API. To zjednodušuje práci s šablonami, které se liší pouze v několika konkrétních hodnotách. Prompty lze organizovat do složek a sdílet mezi členy týmu s nastavením přístupových práv.

## Agent Builder pro vytváření agentů

Agent Builder umožňuje vytváření specializovaných agentů bez nutnosti psát kód. Vývojář definuje roli agenta, jeho cíle a k dispozici nástroje. Platforma podporuje připojení vlastních nástrojů přes API nebo využití vestavěných funkcí pro práce s webem, kalendářem nebo databázemi.

![Agent Builder v Mistral AI Studio](/assets/agent-workflow.webp)

Agent může pracovat se znalostní bází nahrané dokumentace nebo dat. Systém automaticky indexuje obsah a umožňuje agentovi vyhledávat relevantní informace během konverzace. Podporovány jsou formáty PDF, DOCX, TXT nebo webové stránky přes jejich URL.

Vytvořené agenty lze nasadit přes API endpoint nebo sdílet pomocí veřejného odkazu. Každý agent má vlastní konfigurační rozhraní, kde lze upravovat parametry modelu, dostupné nástroje nebo omezení počtu požadavků. Platforma zaznamenává veškerou interakci s agentem včetně použitých nástrojů a jejich výstupů.

## Batch API pro zpracování větších objemů

Batch API je určeno pro zpracování velkých objemů požadavků, které nevyžadují okamžitou odpověď. Systém přijímá dávky požadavků ve formátu JSONL souboru, zpracovává je v průběhu 24 hodin a vrací výsledky. Cena za zpracování je o 50 % nižší než u standardního API.

/Users/patrickzandl/GitHub/marigold-page/assets/agent-workflow.webp
Služba se hodí pro úlohy jako hromadné zpracování dat, generování obsahu pro větší množství položek nebo evaluaci modelů na velkých datasetech. Platforma poskytuje rozhraní pro sledování stavu dávek, včetně počtu zpracovaných požadavků nebo odhadovaného času dokončení.

Batch API podporuje všechny modely dostupné v běžném API včetně jejich konfigurací. Vývojáři mohou nastavit priority dávek nebo je automaticky zrušit, pokud zpracování trvá příliš dlouho. Výsledky jsou dostupné ke stažení po dobu 30 dnů od dokončení.

## Fine-tuning vlastních modelů

AI Studio obsahuje nástroje pro doladění modelů na vlastní data. Vývojáři nahrají trénovací dataset ve formátu JSONL s dvojicemi prompt-odpověď, nakonfigurují hyperparametry jako learning rate nebo počet epoch a spustí trénink.


Platforma aktuálně podporuje fine-tuning modelů Mistral Small a Mistral Large. Proces trvá podle velikosti datasetu a modelu řádově hodiny. Vytvořený model je privátní a dostupný pouze přes API klíč vlastníka. Cena fine-tuningu začína na 4 dolarech za milion tokenů pro trénink.

Výsledný model lze testovat přímo v playground prostředí před nasazením do produkce. Systém poskytuje metriky kvality jako training loss nebo validation accuracy. Modely lze dále iterativně vylepšovat přidáváním nových dat nebo úpravou hyperparametrů.

## Správa API a nákladů

Platforma centralizuje správu API klíčů, nastavení limitů a sledování spotřeby. Vývojáři vidí detailní statistiky použití včetně počtu požadavků, spotřebovaných tokenů a nákladů rozčleněných podle modelů a časových období.

Systém umožňuje nastavit limity spotřeby pro jednotlivé klíče nebo projekty. Při dosažení limitu se požadavky automaticky odmítají, což chrání před neočekávanými náklady. Platforma podporuje webhooky pro notifikace o překročení nastavených prahů.

K dispozici je také monitoring výkonu API včetně latence požadavků, úspěšnosti volání nebo počtu chyb. Vývojáři mohou sledovat trendy využití a optimalizovat své aplikace podle reálných dat. Všechny statistiky jsou exportovatelné do CSV nebo dostupné přes API pro vlastní reporting.

Mistral AI Studio je dostupný na adrese [console.mistral.ai](https://console.mistral.ai). Platforma funguje na základě pay-as-you-go modelu s cenami začínajícími na 0,1 dolaru za milion vstupních tokenů pro nejmenší modely. Nové účty získávají kredit 5 dolarů pro testování.​​​​​​​​​​​​​​​​