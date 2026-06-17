---
slug: "acp"
url: "/mobilnisite/slovnik/acp/"
type: "slovnik"
title: "ACP – Accelerated H.245 Procedures"
date: 2025-01-01
abbr: "ACP"
fullName: "Accelerated H.245 Procedures"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/acp/"
summary: "ACP je vylepšení protokolu 3GPP, které urychluje navázání řídicích kanálů H.245 pro multimediální relace, jako jsou videohovory, v mobilních sítích. Snižuje prodlevy při sestavování hovorů optimalizac"
---

ACP je vylepšení protokolu 3GPP, které urychluje navázání řídicích kanálů H.245 pro multimediální relace optimalizací vyjednávání kodeků a schopností, čímž snižuje prodlevy při sestavování hovorů v mobilních sítích.

## Popis

Accelerated H.245 Procedures (ACP) je optimalizace protokolu definovaná ve specifikacích 3GPP, primárně pro služby multimediální telefonie s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)). Zaměřuje se na řídicí protokol H.245, který je součástí sady H.323 používané pro multimediální komunikaci přes paketové sítě. H.245 je zodpovědný za vyjednávání schopností, logických kanálů a určení hlavního/podřízeného zařízení mezi koncovými body před začátkem toku médií. V mobilním prostředí může toto vyjednávání z důvodu více výměn zpráv přes potenciálně vysokolatentní rádiové spoje způsobit významné prodlevy. ACP tento proces zefektivňuje tím, že umožňuje koncovým bodům vyměňovat klíčové zprávy H.245 zrychleným způsobem, často jejich přidáním na existující signalizační zprávy nebo snížením počtu potřebných cyklů komunikace.

Z architektonického hlediska ACP funguje uvnitř uživatelského zařízení (UE) a síťových prvků, jako je ústředna mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)) nebo mediální brána ([MGW](/mobilnisite/slovnik/mgw/)), které zpracovávají multimediální hovory CS. Upravuje standardní sekvenci procedur H.245, která typicky zahrnuje samostatné fáze navázání spojení, výměny schopností a otevření logických kanálů. Místo toho ACP umožňuje koncovým bodům odesílat klíčové zprávy H.245, jako je TerminalCapabilitySet a OpenLogicalChannel, dříve v průběhu sestavování hovoru. Toho je dosaženo integrací těchto zpráv do počáteční signalizace řízení hovoru, například do zpráv SETUP nebo CALL PROCEEDING v protokolovém zásobníku Q.931, čímž se signalizační fáze překrývají a celková latence se snižuje.

Klíčové komponenty zapojené do ACP zahrnují entitu protokolu H.245 v UE a síti, vrstvu signalizace řízení hovoru (např. Q.931 pro hovory založené na [ISDN](/mobilnisite/slovnik/isdn/)) a podkladové transportní mechanismy. ACP funguje definováním specifických sekvencí zpráv a časovačů, které umožňují koncovým bodům předvídat a předvyjednávat schopnosti bez čekání na úplné navázání kanálu H.245. Například při sestavování videohovoru může ACP umožnit UE zahrnout své preference video kodeku přímo do počáteční žádosti o hovor, což síti umožní rychleji rezervovat prostředky a nakonfigurovat mediální cesty. Tím se zkracuje doba od zahájení uživatelem do navázání mediálního proudu, což je klíčové pro interaktivní služby v reálném čase.

V širším kontextu sítě 3GPP hraje ACP roli při zlepšování výkonu služeb multimediální telefonie přes domény CS, čímž doplňuje snahy v doménách s přepojováním paketů (PS), jako je IMS. Zatímco pozdější vydání se zaměřila na IP Multimedia Subsystem (IMS) a VoLTE, ACP zůstalo relevantní pro starší videohovory CS a scénáře interoperability. Jeho implementace je podrobně popsána v 3GPP TS 29.863 pro aspekty jádra sítě a TS 45.912/45.913 pro aspekty přístupu k rádiovému rozhraní, což zajišťuje soulad se systémy GSM/[EDGE](/mobilnisite/slovnik/edge/) a UMTS. Optimalizací efektivity řídicí roviny ACP přispívá ke zkrácení doby sestavení hovoru, zlepšení výdrže baterie díky menší signalizační režii a lepšímu uživatelskému zážitku.

## K čemu slouží

ACP bylo vytvořeno za účelem řešení významných prodlev při sestavování hovorů, které jsou vlastní multimediálním relacím přes mobilní sítě, zejména pro videohovory s přepojováním okruhů používající protokoly založené na H.323. Před ACP zahrnovalo sestavení multimediálního hovoru sekvenční procedury: nejprve nastavení přenosového kanálu, poté vyjednávání řídicích kanálů H.245 a nakonec výměnu schopností a otevření logických kanálů pro média. Tento vícestupňový proces, kde každý krok vyžadoval cyklus signalizace přes rádiové rozhraní, vedl k dobám sestavení často přesahujícím několik sekund, což zhoršovalo uživatelský zážitek a činilo komunikaci v reálném čase pomalou a nespolehlivou. Motivace vycházela z rostoucí poptávky po mobilní videotelefonii v sítích 3G UMTS, kde uživatelé očekávali rychlé, téměř okamžité spojení podobné hlasovým hovorům.

Historicky se předchozí přístupy spoléhaly na standardní procedury H.245 definované [ITU-T](/mobilnisite/slovnik/itu-t/), které byly navrženy pro pevné sítě s nízkou latencí a dostatečnou šířkou pásma. Když byly aplikovány na mobilní prostředí s vyšší latencí, ztrátou paketů a omezenými prostředky, staly se tyto procedury úzkým hrdlem. Mezi omezení patřil nadměrný počet signalizačních zpráv, závislost na úplném navázání přenosového kanálu před vyjednáváním a absence optimalizace pro charakteristiky rádiového spoje. ACP tyto problémy vyřešilo přepracováním sekvence H.245 tak, aby se signalizační fáze překrývaly, snížil se počet zpráv a bylo využito existujících zpráv řízení hovoru pro zrychlenou výměnu schopností. To bylo obzvláště kritické ve vydání Rel-8 a novějších, protože 3GPP usilovalo o vylepšení služeb multimediálního [CS](/mobilnisite/slovnik/cs/) při přechodu na plně IP sítě.

Vytvoření ACP bylo hnací silou potřeby zlepšit kvalitu služeb (QoS) pro interaktivní služby v reálném čase, v souladu s cíli 3GPP pro lepší uživatelský zážitek a efektivitu sítě. Minimalizací prodlev při sestavování ACP umožnilo rychlejší spojení hovorů, snížilo signalizační zátěž sítě a šetřilo energii baterie UE. Také usnadnilo interoperabilitu se staršími systémy a podpořilo vývoj směrem k bezproblémové multimediální komunikaci, čímž překlenulo mezeru mezi tradičními službami CS a novými řešeními založenými na IP, jako je IMS.

## Klíčové vlastnosti

- Snižuje latenci při sestavování hovorů H.245 překrýváním signalizačních fází
- Přidává zprávy H.245 na existující signalizaci řízení hovoru (např. Q.931)
- Optimalizuje vyjednávání schopností pro kodeky a logické kanály
- Minimalizuje cykly výměny zpráv přes rádiová rozhraní
- Podporuje multimediální telefonii s přepojováním okruhů v sítích 3G/4G
- Zlepšuje uživatelský zážitek u videohovorů v reálném čase rychlejším navázáním

## Definující specifikace

- **TS 29.863** (Rel-8) — IMS-CS Multimedia Interworking Feasibility Study
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study
- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B

---

📖 **Anglický originál a plná specifikace:** [ACP na 3GPP Explorer](https://3gpp-explorer.com/glossary/acp/)
