---
slug: "mkfc"
url: "/mobilnisite/slovnik/mkfc/"
type: "slovnik"
title: "MKFC – Multicast Key for Floor Control"
date: 2026-01-01
abbr: "MKFC"
fullName: "Multicast Key for Floor Control"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mkfc/"
summary: "Kryptografický klíč používaný ve službě Multimedia Broadcast/Multicast Service (MBMS) k zabezpečení signalizace řízení přidělování slova pro skupinovou komunikaci. Zajišťuje, že pouze autorizovaní uži"
---

MKFC je kryptografický klíč používaný v MBMS k zabezpečení signalizace řízení přidělování slova, který zajišťuje, že pouze autorizovaní uživatelé mohou žádat nebo jim může být uděleno oprávnění mluvit ve skupinové komunikaci, jako je MCPTT.

## Popis

Multicast Key for Floor Control (MKFC) je bezpečnostní klíč definovaný v rámci bezpečnostního rámce 3GPP Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), konkrétně pro zabezpečení procedur řízení přidělování slova v mission-critical službách skupinové komunikace. Řízení přidělování slova je mechanismus, který rozhoduje o přístupu ke sdílenému komunikačnímu kanálu a určuje, který uživatel ve skupině má v daném okamžiku 'slovo' neboli oprávnění vysílat média. V mission-critical push-to-talk ([MCPTT](/mobilnisite/slovnik/mcptt/)) a podobných službách je toto rozhodování klíčové pro uspořádanou a efektivní komunikaci, zejména v kritických scénářích, jako jsou operace veřejné bezpečnosti. MKFC se používá k ochraně integrity a autenticity zpráv řízení přidělování slova vyměňovaných mezi uživatelským zařízením (UE) a sítí, čímž brání neoprávněným uživatelům v uchvácení slova nebo narušení probíhající komunikace.

MKFC funguje ve vrstvě MBMS User Services (MBMS-US) a je součástí hierarchie klíčů MBMS. Je odvozen z klíčů vyšší úrovně, jako je MBMS Service Key ([MSK](/mobilnisite/slovnik/msk/)) nebo MBMS Group Key (MGK), v závislosti na konfiguraci služby a bezpečnostním režimu. Proces odvozování klíče je specifikován v bezpečnostních specifikacích 3GPP (TS 33.180, TS 33.880) a zajišťuje, že pouze uživatelé přihlášení ke konkrétní přenosové službě MBMS a autorizovaní pro řízení přidělování slova mohou generovat nebo ověřit správný MKFC. Klíč se typicky používá s kryptografickými algoritmy k vytváření kódů autentizace zpráv ([MAC](/mobilnisite/slovnik/mac/)) pro signalizační zprávy řízení přidělování slova, což zajišťuje, že požadavek na slovo, jeho udělení, zamítnutí nebo uvolnění je legitimní a nebyl pozměněn.

Z architektonického hlediska je MKFC spravován [BM-SC](/mobilnisite/slovnik/bm-sc/) (Broadcast Multicast Service Centre) nebo aplikačním serverem mission-critical služeb ve spolupráci s Key Management Function (KMF). KMF je zodpovědná za generování a distribuci potřebného klíčového materiálu autorizovaným UE. Když se UE připojí ke skupinové komunikační relaci založené na MBMS, obdrží prostřednictvím zabezpečených procedur doručování klíčů příslušné klíče včetně MKFC, často s využitím mechanismu distribuce klíčů MBMS definovaného v Generic Authentication Architecture ([GAA](/mobilnisite/slovnik/gaa/)). UE pak tento MKFC používá k zabezpečení své signalizace řízení přidělování slova po dobu trvání relace.

Úlohou MKFC v síti je umožnit bezpečné, důvěryhodné a efektivní řízení přidělování slova pro skupinovou komunikaci přes broadcast/multicast přenosy LTE a 5G NR. Tím, že kryptograficky váže akce řízení přidělování slova k autorizovaným uživatelům a konkrétní servisní relaci, brání falšování, opakovaným útokům a útokům typu denial-of-service cílícím na mechanismus řízení přidělování slova. To je obzvláště důležité pro mission-critical služby, kde je spolehlivost, přednost a bezpečnost komunikace prvořadá. MKFC tak tvoří základní prvek zabezpečení signalizační roviny služeb skupinové komunikace založených na MBMS podle standardizace 3GPP.

## K čemu slouží

MKFC byl zaveden, aby řešil specifické bezpečnostní požadavky řízení přidělování slova v mission-critical službách skupinové komunikace poskytovaných přes [MBMS](/mobilnisite/slovnik/mbms/). Před jeho standardizací služby skupinové komunikace často spoléhaly na unicast spojení nebo méně bezpečné multicast mechanismy, které neposkytovaly robustní kryptografickou ochranu pro rozhodovací signalizaci. V kritických scénářích, jako je veřejná bezpečnost, záchranné akce nebo železniční komunikace, je zásadní zajistit, že pouze autorizovaný personál může žádat o slovo a může mu být přiděleno, aby se zabránilo chaosu, zneužití identity nebo zlovolnému narušení komunikace.

Vytvoření MKFC bylo motivováno prací 3GPP na vylepšení LTE a později 5G pro kritickou komunikaci, zejména v rámci Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)) počínaje Release 13 a dále v následujících releasech. Potřeba vyhrazeného bezpečnostního klíče vyplynula z analýzy hrozeb specifických pro multicast/broadcast doručování a protokoly řízení přidělování slova. Bez takového klíče by mohly být zprávy řízení přidělování slova padělány, což by umožnilo neoprávněným uživatelům monopolizovat kanál nebo odepřít legitimním uživatelům možnost mluvit, což by vážně ohrozilo efektivitu mission-critical operací.

Definováním MKFC poskytlo 3GPP standardizovanou, kryptograficky bezpečnou metodu pro autentizaci a ochranu integrity signalizace řízení přidělování slova v rámci architektury MBMS. Tím se odstranila omezení předchozích ad-hoc nebo nestandardizovaných přístupů, což umožnilo interoperabilitu mezi různými výrobci a síťovými operátory při splnění přísných požadavků na bezpečnost a spolehlivost pro veřejnou bezpečnost a průmyslové vertikály. Tvoří část komplexního bezpečnostního rámce pro MBMS a zajišťuje, že efektivita multicastového doručování není vykoupena snížením bezpečnosti kritických řídicích funkcí.

## Klíčové vlastnosti

- Odvozen z klíčů vyšší úrovně bezpečnostního systému MBMS (např. MSK, MGK) jako součást definované hierarchie klíčů
- Používá se k ochraně integrity a autentizaci zpráv řízení přidělování slova: žádosti o slovo, jeho udělení, zamítnutí a uvolnění
- Umožňuje bezpečné rozhodování o přidělení 'slova' ve službách skupinové komunikace založených na MBMS, jako je MCPTT
- Spravován a distribuován funkcí Key Management Function (KMF) a BM-SC
- Integruje se s Generic Authentication Architecture (GAA) pro zabezpečené doručování klíčů k UE
- Chrání před falšováním, opakovanými útoky a útoky typu denial-of-service na signalizaci řízení přidělování slova

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services

---

📖 **Anglický originál a plná specifikace:** [MKFC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mkfc/)
