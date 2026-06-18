---
slug: "tgcfn"
url: "/mobilnisite/slovnik/tgcfn/"
type: "slovnik"
title: "TGCFN – Transmission Gap Connection Frame Number"
date: 2025-01-01
abbr: "TGCFN"
fullName: "Transmission Gap Connection Frame Number"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tgcfn/"
summary: "Časový parametr používaný v UMTS pro synchronizaci vzorů přenosových mezer (Transmission Gap) pro komprimovaný mód a měření mezi UE a Node B. Definuje počáteční bod periodické sekvence přenosových mez"
---

TGCFN je Connection Frame Number, který definuje počáteční bod pro periodickou sekvenci přenosových mezer (Transmission Gap) v UMTS, umožňující synchronizované mezery pro měření mezi UE a Node B.

## Popis

Transmission Gap Connection Frame Number (TGCFN) je kritický časový referenční parametr používaný v UMTS (Universal Mobile Telecommunications System) [WCDMA](/mobilnisite/slovnik/wcdma/) radio přístupových sítích. Je specificky spojen s provozem komprimovaného módu, techniky, při které UE (User Equipment) a Node B dočasně komprimují přenos dat do kratších časových intervalů, aby vytvořily řízené 'mezery' v časové osě přenosu. Tyto mezery umožňují přijímači UE naladit se na jiné frekvence nebo jiné radio přístupové technologie ([RAT](/mobilnisite/slovnik/rat/)) k provedení nezbytných měření, například pro přípravu přenosu (handover) na GSM nebo jiný nosič UMTS, aniž by se ztratilo primární spojení. TGCFN je hodnota Connection Frame Number ([CFN](/mobilnisite/slovnik/cfn/)), při kterém začíná specifická sekvence vzoru přenosových mezer (Transmission Gap Pattern Sequence, TGPS).

Connection Frame Number je 12-bitový čítač (rozsah 0-4095), který cykluje a poskytuje běžnou časovou referenci mezi UE a [UTRAN](/mobilnisite/slovnik/utran/) (UMTS Terrestrial Radio Access Network) pro daný radio link. TGCFN je signalizován [RNC](/mobilnisite/slovnik/rnc/) (Radio Network Controller) jak UE, tak Node B jako část konfigurace komprimovaného módu. Toto zajistí, že obě strany radio linku jsou perfektně synchronizované na začátku a konci přenosových mezer. Transmission Gap Pattern definuje strukturu těchto mezer (např. délka mezery, perioda opakování). Ukotvením začátku tohoto vzoru na specifický TGCFN síť koordinuje přesné radio rámy, během kterých je přenos na primární frekvenci zastaven.

Architektonicky je TGCFN parametr uvnitř zpráv protokolu Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), například PHYSICAL CHANNEL RECONFIGURATION nebo TRANSPORT CHANNEL RECONFIGURATION. RNC vypočítá a přidělí TGCFN na základě aktuálního CFN a požadovaného časového začátku měření. Node B používá TGCFN k naplánování svých přenosových mezer na downlinku, zatímco UE ho používá, aby vědělo, kdy očekávat mezery (a tedy nepřenášet na uplinku) a kdy přeladit svůj přijímač k provedení měření mezi různými frekvencemi/RAT. Tato přesná synchronizace je klíčová k prevenci ztráty dat a udržení kvality linku, protože mezery jsou typicky jen několik slotů dlouhé v rámci 10ms radio rámu. TGCFN je tedy klíčový umožňovatel pro seamless mobilitu v multi-carrier a multi-RAT UMTS sítích, zajišťující, že měřicí aktivity nenaruší probíhající komunikaci.

## K čemu slouží

TGCFN byl vytvořen k řešení základního problému provádění měření na jiných frekvencích nebo radio systémech při zachování aktivního spojení v [WCDMA](/mobilnisite/slovnik/wcdma/) síti. WCDMA je technologie kontinuálního přenosu, což znamená, že UE normálně nemůže 'odposlouchávat' jiné frekvence bez degradace nebo ztráty svého aktuálního linku. Komprimovaný mód byl řešením, uměle vytvářejícím periody pro odposlech. Pro fungování komprimovaného módu však síť a UE musí mít absolutní synchronizaci na čas, kdy tyto přenosové mezery nastávají, aby se zabránilo přenosu dat do mezery (vedoucí ke ztrátě) nebo zameškanému přenosu, protože UE odposlouchávalo jiný signál.

Účelem TGCFN je poskytnout tento přesný synchronizační kotvu. Před jeho definicí neexistoval standardizovaný způsob koordinace začátku komplexních, periodických vzorů mezer mezi síťovým a potenciálně pohyblivým UE. TGCFN, spojený s běžnou [CFN](/mobilnisite/slovnik/cfn/) časovou osou, poskytuje jednoduchý, jednoznačný referenční bod. Řeší omezení ad-hoc nebo nesynchronizovaného vytváření mezer, které vedlo k ne spolehlivým měřením a ztraceným hovorům. Jeho zavádění bylo motivováno potřebou robustního mezisystémového přenosu (handover) (např. UMTS na GSM) a přenosu mezi frekvencemi v raných UMTS deploymentech, které byly často vrstveny nad existující GSM sítě. Umožnil efektivní síťově řízenou mobilitu, základní kámen 3GPP systémů.

## Klíčové vlastnosti

- Synchronizační kotva pro začátek vzoru přenosových mezer (Transmission Gap Pattern)
- Spojený s 12-bitovou časovou osou Connection Frame Number (CFN)
- Signalizován prostřednictvím protokolu RRC z RNC do UE a Node B
- Umožňuje přesnou koordinaci pro provoz komprimovaného módu
- Podporuje měření mezi různými frekvencemi a různými RAT
- Prevenuje ztrátu dat během naplánovaných přenosových mezer

## Související pojmy

- [CFN – Connection Frame Number](/mobilnisite/slovnik/cfn/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification

---

📖 **Anglický originál a plná specifikace:** [TGCFN na 3GPP Explorer](https://3gpp-explorer.com/glossary/tgcfn/)
