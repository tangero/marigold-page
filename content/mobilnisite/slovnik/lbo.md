---
slug: "lbo"
url: "/mobilnisite/slovnik/lbo/"
type: "slovnik"
title: "LBO – Load Balancing Optimization"
date: 2026-01-01
abbr: "LBO"
fullName: "Load Balancing Optimization"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lbo/"
summary: "Soubor funkcí a procedur správy sítě navržený k optimalizaci distribuce síťového provozu mezi síťové zdroje, jako jsou buňky nebo síťové řezy. Je klíčový pro zvýšení efektivity sítě, předcházení přetí"
---

LBO je soubor funkcí a procedur správy sítě navržený k optimalizaci distribuce síťového provozu mezi síťové zdroje za účelem zvýšení efektivity a předcházení přetížení.

## Popis

Load Balancing Optimization (LBO) ve standardech 3GPP je komplexní rámec pro správu a optimalizaci distribuce provozu v mobilních sítích. Funguje jako klíčová funkce v širším kontextu samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)) a síťové automatizace, řízená primárně systémem pro provoz, správu a údržbu ([OAM](/mobilnisite/slovnik/oam/)). Architektura zahrnuje centralizované a distribuované entity, které sbírají klíčové výkonnostní ukazatele ([KPI](/mobilnisite/slovnik/kpi/)), jako je zatížení buňky, využití zdrojů a propustnost uživatele. Na základě předdefinovaných politik a algoritmů funkce LBO rozhoduje o přesunu provozu z přetížených buněk nebo síťových řezů na nedostatečně vytížené. Toho je dosaženo úpravou parametrů předávání spojení (např. individuálních posunů buňky), změnou priorit převýběru buňky nebo směrováním provozu mezi různými technologiemi rádiového přístupu ([RAT](/mobilnisite/slovnik/rat/)) nebo frekvenčními vrstvami.

V jádru LBO funguje prostřednictvím kontinuálního cyklu monitorování, analýzy, rozhodování a provedení. Síťové prvky, jako jsou gNB v 5G nebo [eNB](/mobilnisite/slovnik/enb/) v 4G, hlásí metriky zatížení systému OAM nebo centralizovanému SON serveru. Sofistikované algoritmy tato data analyzují k identifikaci nerovnováh. Optimalizační akce jsou následně vypočteny a provedeny, často zahrnují změnu parametrů zasílaných uzlům rádiové přístupové sítě (RAN) prostřednictvím standardizovaných rozhraní. V 5G je LBO těsně integrováno s dělením sítě, což zajišťuje vyrovnávání zátěže nejen geograficky, ale také napříč logickými instancemi řezů, aby byly splněny různé smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)).

Jeho role je klíčová pro efektivitu sítě a kvalitu služeb (QoS). Tím, že předchází lokalizovanému přetížení, LBO pomáhá udržovat vysoké datové rychlosti a nízkou latenci pro koncové uživatele. Také zlepšuje celkové využití kapacity sítě, což operátorům umožňuje obsloužit více provozu se stejnou infrastrukturou. Tato funkce je nezbytná pro automatizovaný provoz sítě, snižuje potřebu manuálního zásahu a umožňuje proaktivní optimalizaci v reakci na předvídatelné události, jako jsou shromáždění na stadionech nebo každodenní dojíždění.

## K čemu slouží

LBO bylo vytvořeno k řešení základní výzvy nerovnoměrné distribuce provozu v celulárních sítích, která vede k neefektivnímu využití zdrojů a zhoršenému uživatelskému zážitku. V raných sítích se nerovnováhy v zatížení často ručně korigovaly síťovými inženýry, což byl proces pomalý, náchylný k chybám a neschopný reagovat na rychlé změny v poptávce uživatelů. Rozšíření chytrých telefonů a datově náročných aplikací tento problém prohloubilo a vytvářelo hotspoty přetížení, zatímco jiné síťové zdroje zůstávaly nevyužité.

Motivací pro standardizaci LBO v rámci 3GPP, zejména od vydání 8 s příchodem LTE a konceptů [SON](/mobilnisite/slovnik/son/), byla automatizace a optimalizace tohoto procesu. Řeší problémy přetížení buněk, které způsobují přerušení hovorů, snížení datových rychlostí a zvýšení latence. Dynamickým vyvažováním zátěže LBO maximalizuje využití nasazených síťových aktiv, oddaluje potřebu nákladných nasazení nových stanovišť buněk a zajišťuje rovnoměrnější a spolehlivější kvalitu služeb v celé pokryté oblasti. V éře 5G se jeho účel rozšířil o správu komplexních požadavků na distribuci zátěže pro dělení sítě, kde různé řezy (např. pro vylepšenou mobilní širokopásmovou komunikaci, ultra-spolehlivou komunikaci s nízkou latencí a masivní IoT) mají značně odlišné požadavky na zdroje a výkon, které musí být vyváženy současně.

## Klíčové vlastnosti

- Vyvažování zátěže napříč více RAT a více vrstvami přes LTE, NR a další přístupové technologie
- Integrace s rámci samoorganizujících se sítí (SON) pro automatizovanou optimalizaci
- Podpora distribuce zátěže s ohledem na dělení sítě a správy SLA specifických pro řezy
- Optimalizace řízená politikami na základě operátorem definovaných pravidel a klíčových výkonnostních ukazatelů (KPI)
- Centralizované a distribuované koordinační modely pro flexibilní nasazení
- Dynamické nastavování parametrů předávání spojení a převýběru buňky pro směrování uživatelských zařízení

## Související pojmy

- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)
- [MRO – Mobility Robustness Optimisation](/mobilnisite/slovnik/mro/)
- [CAC – Communication Admission Control](/mobilnisite/slovnik/cac/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TS 23.894** (Rel-10) — IMS Local Breakout & Optimal Media Routing Study
- **TR 26.803** (Rel-17) — 5G Media Streaming Extensions for Edge Processing
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TR 28.827** (Rel-18) — Technical Report on 5G Charging for Roaming Scenarios
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.522** (Rel-11) — SON Policy NRM IRP Information Service
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.827** (Rel-14) — LI for S8 Home Routed VoLTE Roaming

---

📖 **Anglický originál a plná specifikace:** [LBO na 3GPP Explorer](https://3gpp-explorer.com/glossary/lbo/)
