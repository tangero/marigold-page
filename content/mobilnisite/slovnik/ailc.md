---
slug: "ailc"
url: "/mobilnisite/slovnik/ailc/"
type: "slovnik"
title: "AILC – Assistance Information bit for Local Cache"
date: 2025-01-01
abbr: "AILC"
fullName: "Assistance Information bit for Local Cache"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ailc/"
summary: "AILC je jednobitový indikátor v signalizaci LTE RRC, který informuje uživatelské zařízení (UE), zda síť podporuje lokální ukládání asistenčních informací do mezipaměti. Umožňuje efektivní doručování l"
---

AILC je jednobitový indikátor v signalizaci LTE RRC, který informuje uživatelské zařízení (UE), zda síť podporuje lokální ukládání asistenčních informací do mezipaměti za účelem snížení signalizační režie.

## Popis

Assistance Information bit for Local Cache (AILC, bit asistenčních informací pro lokální mezipaměť) je specifický signalizační prvek definovaný v protokolu LTE Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), který je primárně dokumentován v 3GPP TS 36.331 (specifikace protokolu RRC) a odkazován v TS 36.323 (specifikace Packet Data Convergence Protocol). Funguje jako jednobitový příznak vysílaný eNodeB k uživatelskému zařízení (UE) v rámci specifických RRC zpráv, zejména v rámci System Information Block ([SIB](/mobilnisite/slovnik/sib/)) typu 2 nebo případně v rámci vyhrazené RRC signalizace. Hlavním účelem tohoto bitu je indikovat, zda síť podporuje a umožňuje UE lokálně ukládat do mezipaměti asistenční informace přijaté ze sítě, zejména informace související se službami určování polohy.

Z architektonického hlediska AILC funguje v rámci řídicí roviny LTE Radio Access Network ([E-UTRAN](/mobilnisite/slovnik/e-utran/)). eNodeB jako řídicí entita pro rádiové zdroje nastavuje hodnotu bitu AILC na základě konfigurace a možností sítě. Když UE přijme RRC zprávu obsahující bit AILC nastavený na hodnotu „true“ nebo „supported“, interpretuje to jako povolení uložit si určitá asistenční data poskytnutá sítí do své non-volatilní paměti (lokální mezipaměť). Tato data v mezipaměti typicky zahrnují prvky jako identity buněk, časové informace a další parametry, které mohou pomoci v následných postupech určování polohy, jako je Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) nebo Enhanced Cell ID ([E-CID](/mobilnisite/slovnik/e-cid/)).

Z procedurálního hlediska mechanismus funguje následovně: Během počátečního přístupu nebo relace určování polohy přijímá UE asistenční data ze sítě prostřednictvím signalizace RRC nebo LPPa/[LPP](/mobilnisite/slovnik/lpp/). Pokud je bit AILC nastaven, může si UE tato data uložit. V budoucích relacích, zejména při převýběru buňky nebo návratu z nečinného režimu, může UE nejprve zkontrolovat svou lokální mezipaměť, zda neobsahuje platné asistenční informace, než požádá síť o nový přenos. UE musí spravovat platnost dat v mezipaměti, která je často vázána na časové razítko nebo časovač platnosti rovněž poskytovaný sítí. Tento mechanismus ukládání do mezipaměti a opětovného použití významně snižuje potřebu opakované signalizace převážně statických nebo pomalu se měnících asistenčních dat.

Jeho úlohou v síti je optimalizovat signalizaci související s určováním polohy a zlepšit uživatelský zážitek ze služeb založených na poloze. Tím, že minimalizuje počet bajtů, které je třeba přenášet přes rozhraní vzduchu pro asistenci při určování polohy, AILC přispívá ke snížení latence při získávání polohy, snížení signalizační zátěže sítě a snížení spotřeby energie UE. Je klíčovým prvkem pro efektivní, síťově asistované určování polohy v LTE a slouží jako základní koncept pro podobné optimalizace v 5G NR.

## K čemu slouží

AILC byl zaveden, aby řešil neefektivitu opakovaného přenosu stejných, relativně statických asistenčních informací k uživatelskému zařízení (UE) pokaždé, když potřebovalo provést operaci určování polohy. Před jeho zavedením se asistenční data pro techniky jako [OTDOA](/mobilnisite/slovnik/otdoa/) – která zahrnují informace o referenční buňce, seznamy sousedních buněk a přesné časové údaje – typicky přenášela v plném rozsahu během každé relace určování polohy. To vytvářelo významnou a zbytečnou signalizační režii, zejména pro UE, která byla stacionární nebo se pohybovala v omezené oblasti, protože asistenční data pro blízké buňky zůstávala převážně nezměněna.

Historický kontext vzniku AILC souvisí s rostoucím významem a poptávkou po přesných lokalizačních službách s nízkou latencí v LTE sítích. Aplikace od nouzových služeb (E911) přes komerční služby založené na poloze až po sledování IoT aktiv vyžadovaly efektivní mechanismy určování polohy. Tradiční přístup plného přenosu asistenčních dat na relaci byl identifikován jako úzké hrdlo, které spotřebovávalo rádiové zdroje a prodlužovalo čas do prvního určení polohy ([TTFF](/mobilnisite/slovnik/ttff/)). AILC jako jednoduchý jednobitový indikátor poskytl elegantní a nenáročné řešení tohoto problému tím, že umožnil strategii ukládání do mezipaměti na straně klienta.

Problém řeší posunem paradigmatu z modelu „vždy přenášet“ na model „ukládat do mezipaměti a ověřovat“. Tím řeší omezení ve spektrální účinnosti, kapacitě sítě a životnosti baterie UE. Motivací bylo vytvořit standardizovaný mechanismus, který umožňuje sítím explicitně řídit a autorizovat chování ukládání do mezipaměti, což zajišťuje interoperabilitu mezi UE a síťovým vybavením od různých výrobců při dosažení požadovaných optimalizačních zisků.

## Klíčové vlastnosti

- Jednobitový indikátor v rámci RRC signalizace pro síťové řízení
- Umožňuje lokální ukládání asistenčních dat pro určování polohy do mezipaměti na straně UE
- Snižuje signalizační režii a spotřebu zdrojů rozhraní vzduchu
- Snižuje latenci při získávání polohy (Time-To-First-Fix)
- Zlepšuje energetickou účinnost UE tím, že se vyhne příjmu redundantních dat
- Standardizovaný mechanismus zajišťující interoperabilitu mezi více výrobci

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [AILC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ailc/)
