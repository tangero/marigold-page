---
slug: "e-facch"
url: "/mobilnisite/slovnik/e-facch/"
type: "slovnik"
title: "E-FACCH – Enhanced Fast Associated Control Channel"
date: 2025-01-01
abbr: "E-FACCH"
fullName: "Enhanced Fast Associated Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-facch/"
summary: "E-FACCH je vylepšená verze FACCH v GSM/EDGE sítích. Je to signalizační kanál používaný pro přenos urgentních řídicích zpráv, jako jsou příkazy pro přenos spojení, pomocí \"kradení\" burstů z asociovanéh"
---

E-FACCH je vylepšený signalizační kanál GSM/EDGE, který spolehlivě přenáší urgentní řídicí zprávy, například příkazy pro přenos spojení, pomocí "kradení" burstů z asociovaného kanálu pro přenos dat.

## Popis

Enhanced Fast Associated Control Channel (E-FACCH) je klíčový signalizační kanál v architekturu rádiového přístupové sítě GSM/[EDGE](/mobilnisite/slovnik/edge/). Je evolucí klasického Fast Associated Control Channel ([FACCH](/mobilnisite/slovnik/facch/)), který je samotný metodou pro přenos časově kritické řídicí signalizace předběhnutím nebo "kradením" rámců z dedikovaného kanálu pro přenos dat ([TCH](/mobilnisite/slovnik/tch/)). E-FACCH funguje ve asociaci s TCH, což znamená, že nemá své vlastní permanentní fyzické prostředky, ale místo toho dočasně využívá prostředky alokované pro uživatelský hlasový nebo datový přenos, když je vyžadována urgentní signalizace. Toto je indikováno přijímači pomocí "stealing" flagů v normálním burstu.

Technicky, když potřebuje být odeslána řídicí zpráva (například příkaz pro přenos spojení nebo immediate assignment), systém použije E-FACCH. Nahradí blok uživatelských dat na TCH řídicími daty. "Enhanced" aspekt, jak je definován v specifikacích 3GPP, typicky souvisí s vylepšeními v kódování a interleaving schématech ve srovnání s legacy FACCH. Tyto vylepšení zvyšují robustnost řídicí signalizace vůči chybám, což je klíčové pro kritické příkazy, které, pokud jsou ztraceny, mohou vést ke zrušení spojení. E-FACCH může využívat silnější kanálové kódování (jako ty zaváděné s EDGE modulačními schématy) nebo jiné interleaving hloubky pro zlepšení výkonu, obzvláště v náročných rádiových podmínkách.

Z pohledu provozu sítě je E-FACCH nezbytný pro management mobility a řízení spojení. Jeho primární role je umožnit rychlý a spolehlivý přenos Layer 3 zpráv mezi Mobile Station ([MS](/mobilnisite/slovnik/ms/)) a Base Station System ([BSS](/mobilnisite/slovnik/bss/)) během aktivního hlasového spojení nebo datové session. Protože využívá již navázané TCH linky, vyhne se zpoždění spojenému s nastavením samostatného signalizačního kanálu. Vylepšení poskytované E-FACCH zvyšuje pravděpodobnost úspěšného dekódování těchto klíčových příkazů, tím zlepšuje celkové metriky výkonu sítě jako úspěšnost přenosů spojení a míra zrušení spojení. Reprezentuje optimalizaci v rámci zralých GSM/EDGE standardů pro získání dodatečné spolehlivosti a kapacity.

## K čemu slouží

E-FACCH byl vytvořen pro řešení problémů spolehlivosti s standardním [FACCH](/mobilnisite/slovnik/facch/) v GSM sítích, obzvláště jak se sítě vyvíjely s [EDGE](/mobilnisite/slovnik/edge/) a čelily náročnější datovým službám a hustým deploymentům. Klasický FACCH používal specifický konvoluční kód a interleaving schéma, které, i když funkční, mělo nezanedbatelnou míru chyb v podmínkách slabého signálu. Vzhledem k tomu, že FACCH přenáší nejkritičtější signalizační zprávy – jako příkazy pro přenos spojení – selhání mohlo přímo způsobit zrušení spojení nebo neúspěšnou packet data transakci. Jak rostly očekávání kvality služby sítě, zlepšení robustnosti tohoto kanálu se stalo prioritou.

Účelem E-FACCH je zvýšit odolnost řídicí signalizace v prostředích s fadingem a rušením bez vyžadování dodatečné šířky pásma. Použitím vylepšených kanálových kódových technik, možná převzatých z pokročilejších EDGE datových kanálových ([MCS](/mobilnisite/slovnik/mcs/)) schémat, E-FACCH nabízí lepší schopnost korekce chyb. Toto řeší problém bottlenecku řídicího kanálu během podmínek na hranici cell nebo během událostí s vysokým rušením. Motivace byla potřebou udržet kontinuitu služby pro hlasové spojení a podporovat spolehlivější packet-switched datové session, které jsou citlivé na signalizační zpoždění a selhání.

Historicky, jeho zavádění odráží cyklus kontinuálního zlepšení GSM technologie. I když byl nasazován 3G UMTS, operátoři potřebovali udržovat a optimalizovat své rozsáhlé GSM footprinty. Vylepšení jako E-FACCH jim umožnilo zlepšit klíčové performance indikátory (KPIs) jako míra zrušení spojení a úspěšnost přenosů spojení, vedoucí k lepší zkušenosti uživatele na legacy síti. Reprezentuje inteligentní, backward-compatible upgrade základního signalizačního mechanismu.

## Klíčové vlastnosti

- Funguje "kradením" burstů z asociovaného kanálu pro přenos dat (TCH) pro signalizaci
- Přenáší urgentní Layer 3 řídicí zprávy (například příkazy pro přenos spojení, reassignments kanálů)
- Využívá vylepšené kanálové kódování pro zlepšenou ochranu proti chybám ve srovnání s legacy FACCH
- Udržuje nízkou latenci pro kritickou signalizaci využitím navázané TCH linky
- Indikováno přijímači pomocí "stealing" flagů v normální burst struktuře
- Zlepšuje metriky spolehlivosti sítě jako úspěšnost přenosů spojení a míra zrušení spojení

## Související pojmy

- [FACCH – Fast Associated Control CHannel](/mobilnisite/slovnik/facch/)
- [TCH – Traffic Channel](/mobilnisite/slovnik/tch/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)

## Definující specifikace

- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [E-FACCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-facch/)
