---
slug: "cg-uci"
url: "/mobilnisite/slovnik/cg-uci/"
type: "slovnik"
title: "CG-UCI – Configured Grant Uplink Control Information"
date: 2025-01-01
abbr: "CG-UCI"
fullName: "Configured Grant Uplink Control Information"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cg-uci/"
summary: "CG-UCI je řídicí informace v uplinku, kterou UE vysílá na prostředku s nakonfigurovaným grantem (CG) bez dynamického plánování. Umožňuje nízkolatentní a spolehlivou řídicí signalizaci v uplinku, což j"
---

CG-UCI je řídicí informace v uplinku, kterou UE vysílá na prostředku s nakonfigurovaným grantem bez dynamického plánování, což umožňuje nízkolatentní a spolehlivé řídicí signalizace v uplinku pro služby jako URLLC v 5G NR.

## Popis

Configured Grant Uplink Control Information (CG-UCI) je klíčový mechanismus v rámci struktury řídicího kanálu fyzické vrstvy pro uplink v 5G New Radio (NR), specifikovaný v 3GPP TS 38.212. Odkazuje na řídicí informace v uplinku (UCI), které uživatelské zařízení (UE) vysílá pomocí předem nakonfigurovaných, semi-perzistentních prostředků v uplinku známých jako nakonfigurované granty ([CG](/mobilnisite/slovnik/cg/)), konkrétně nakonfigurované granty typu 1 nebo typu 2. Na rozdíl od dynamicky plánovaných UCI na fyzickém řídicím kanálu pro uplink (PUCCH) nebo multiplexovaných na fyzickém sdíleném kanálu pro uplink (PUSCH) se CG-UCI vysílá na prostředku nakonfigurovaného grantu pro fyzický sdílený kanál v uplinku (CG-PUSCH). To znamená, že UE nevyžaduje pro každou instanci přenosu dynamický grant prostřednictvím řídicí informace v downlinku ([DCI](/mobilnisite/slovnik/dci/)) od gNodeB, což umožňuje přístup do uplinku bez grantu.

Fungování CG-UCI je vnitřně propojeno se strukturou nakonfigurovaného grantu (CG) zavedenou pro data v uplinku. Když je prostředek CG aktivován pro UE prostřednictvím signalizace řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) (typ 1) nebo kombinací RRC a aktivačního DCI (typ 2), je UE přiděleno periodické přidělení prostředků na PUSCH. UE může tyto prostředky použít k vysílání dat v uplinku bez žádosti o plánování (SR) nebo grantu, čímž se snižuje latence. CG-UCI využívá tytéž předem přidělené prostředky k přenosu nezbytných řídicích informací. Datová část UCI pro CG-UCI typicky zahrnuje potvrzení hybridního automatického opakování na vyžádání ([HARQ-ACK](/mobilnisite/slovnik/harq-ack/)) pro přenosy v downlinku, hlášení informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) a indikace žádosti o plánování (SR). Tyto řídicí informace jsou multiplexovány s daty v uplinku na CG-PUSCH podle pravidel multiplexování fyzické vrstvy definovaných v TS 38.212.

Z architektonického hlediska se CG-UCI nachází v rámci zpracovatelského řetězce fyzické vrstvy UE. Vrstva řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) poskytuje informace HARQ-ACK a SR, zatímco měření fyzické vrstvy generují CSI. Tyto informace jsou zakódovány, přizpůsobeny přenosové rychlosti a multiplexovány s datovými transportními bloky před mapováním na přidělený časově-frekvenční rastr prostředku CG-PUSCH. gNodeB, který má konfiguraci CG na vědomí, tyto periodické prostředky monitoruje, aby dekódoval jak data, tak vložené CG-UCI. Mezi klíčové komponenty umožňující CG-UCI patří parametry konfigurace CG (periodicita, časové/frekvenční prostředky, modulace a kódovací schéma), postupy kódování UCI a pravidla pro sdílení prostředků mezi datovými a řídicími bity na PUSCH.

Role CG-UCI v síti je klíčová pro podporu komunikací s ultra spolehlivostí a nízkou latencí (URLLC) a efektivní provoz v uplinku. Tím, že odstraňuje potřebu cyklu žádosti o plánování a grantu pro řídicí zpětnou vazbu, výrazně snižuje latenci řídicí roviny pro potvrzení a hlášení v uplinku. To je nezbytné pro aplikace, jako je průmyslová automatizace, kde je nutné včasné HARQ-ACK pro kritické příkazy v downlinku. Dále zlepšuje spektrální efektivitu a energetickou efektivitu UE tím, že umožňuje přenos řídicích informací a dat společně v jedné předem připravené přenosové dávce, a vyhýbá se tak samostatným přenosům na řídicím kanálu.

## K čemu slouží

CG-UCI bylo vytvořeno, aby řešilo přísné požadavky na latenci a spolehlivost v 5G, zejména pro případy užití URLLC. Před 5G NR Release 16 se řídicí informace v uplinku primárně přenášely na vyhrazených prostředcích PUCCH nebo byly multiplexovány na dynamicky plánovaném PUSCH. Oba přístupy s sebou nesou latenci: PUCCH vyžaduje periodické vyhrazené prostředky, které nemusí odpovídat potřebě okamžité zpětné vazby, zatímco dynamické plánování na PUSCH vyžaduje úplný postup žádosti o plánování (SR) a grantu, což přidává několik milisekund zpoždění. Pro časově kritické aplikace, jako je uzavřená smyčka řízení v tovární automatizaci nebo telechirurgie, byla tato latence nepřijatelná.

Motivace pro CG-UCI vychází z paralelního vývoje přenosu dat v uplinku s nakonfigurovaným grantem (bez grantu). Zatímco [CG](/mobilnisite/slovnik/cg/) umožnilo odesílání dat bez latence plánování, chybělo propojení: jak poskytnout potřebnou doprovodnou řídicí zpětnou vazbu (jako [HARQ-ACK](/mobilnisite/slovnik/harq-ack/) pro přiřazení v downlinku) se stejně nízkou latencí. Přenos této zpětné vazby na samostatném, dynamicky plánovaném prostředku by zrušil výhody nízké latence přenosu dat bez grantu. CG-UCI to řeší tím, že umožňuje UE odesílat tyto životně důležité řídicí informace ve stejné příležitosti pro přenos bez grantu jako svá data, a to s využitím předem nakonfigurovaných prostředků. Tím vzniká souvislá nízkolatentní cesta pro uplink jak pro data, tak pro řídicí informace.

Historicky nabízelo LTE semi-perzistentní plánování (SPS) pro uplink, ale jeho mechanismy řídicí zpětné vazby nebyly tak těsně integrované nebo optimalizované pro mikrosekundové latence, které jsou cílem 5G URLLC. CG-UCI jako součást vylepšené struktury nakonfigurovaného grantu představuje zásadní architektonický posun k podpoře deterministické, nízkolatentní komunikace v uplinku, který překračuje reaktivní, grantem založený paradigma předchozích generací.

## Klíčové vlastnosti

- Přenos UCI bez grantu na předem nakonfigurovaných prostředcích PUSCH
- Multiplexování HARQ-ACK, CSI a SR s daty v uplinku na CG-PUSCH
- Snížení latence řídicí roviny odstraněním cyklu SR/grantu pro zpětnou vazbu
- Zásadní prvek pro splnění požadavků služeb URLLC
- Zlepšená energetická efektivita UE díky kombinovanému přenosu dat a řídicích informací
- Podpora prostřednictvím nakonfigurovaných grantů typu 1 (konfigurovaných přes RRC) i typu 2 (aktivovaných přes DCI)

## Definující specifikace

- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding

---

📖 **Anglický originál a plná specifikace:** [CG-UCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cg-uci/)
