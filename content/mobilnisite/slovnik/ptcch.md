---
slug: "ptcch"
url: "/mobilnisite/slovnik/ptcch/"
type: "slovnik"
title: "PTCCH – Packet Timing advance Control Channel"
date: 2025-01-01
abbr: "PTCCH"
fullName: "Packet Timing advance Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ptcch/"
summary: "Packet Timing advance Control Channel (PTCCH) je logický kanál v GSM/EDGE rádiové přístupové síti (GERAN) používaný pro správu časového předstihu pro mobilní stanice v paketovém režimu. Zajišťuje přes"
---

PTCCH je logický kanál v sítích GSM/EDGE používaný pro správu časového předstihu (timing advance) pro mobilní stanice v paketovém režimu, zajišťující přesné časování uplinku pro prevenci interference a efektivní služby GPRS a EDGE.

## Popis

Packet Timing advance Control Channel (PTCCH) je základní řídicí kanál v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové sítě ([GERAN](/mobilnisite/slovnik/geran/)), speciálně navržený pro podporu paketových služeb jako [GPRS](/mobilnisite/slovnik/gprs/) a EDGE. Funguje jako logický kanál mapovaný na fyzické rádiové zdroje. Jeho primární funkcí je správa a distribuce hodnot časového předstihu (Timing Advance, [TA](/mobilnisite/slovnik/ta/)) více mobilním stanicím ([MS](/mobilnisite/slovnik/ms/)) zapojeným do přenosu paketových dat. Časový předstih je klíčový parametr, který kompenzuje zpoždění šíření mezi MS a základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)), a zajišťuje, že bursty od různých MS dorazí na BTS ve svých určených časových slotech a nepřekrývají se, čímž se předchází mezi­symbolové interferenci a udržuje se kapacita a kvalita sítě.

Architektonicky je PTCCH implementován ve dvou odlišných podkanálech: PTCCH/U (Uplink) a PTCCH/D (Downlink). PTCCH/D je společný downlinkový kanál vysílaný z BTS, používaný k odesílání příkazů pro aktualizaci časového předstihu skupině MS. PTCCH/U se skládá z vyhrazených uplinkových slotů, ve kterých jednotlivé MS vysílají přístupové bursty. Síť měří časování těchto přístupových burstů, aby vypočítala přesnou hodnotu časového předstihu potřebnou pro každou MS. Tento výpočet provádí BTS a přidružený řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)), který tvoří jádro správy rádiových zdrojů pro paketová data.

Provoz kanálu je nedílnou součástí alokace zdrojů na Paketovém datovém kanálu ([PDCH](/mobilnisite/slovnik/pdch/)). Když je MS přidělen PDCH pro přenos dat, jsou mu také přiděleny zdroje na PTCCH pro periodickou údržbu časování. Proces zahrnuje vyslání přístupového burstu MS na jejím přiděleném slotu PTCCH/U. BTS změří čas příchodu, vypočítá potřebnou korekci a odešle aktualizovaný příkaz TA přes PTCCH/D. Tato uzavřená smyčka řízení umožňuje síti sledovat pohyb MS a udržovat optimální časování i během dlouhých datových relací, což je efektivnější než metoda používaná pro přepojování okruhů.

Role PTCCH je zásadní pro spektrální účinnost a spolehlivost paketových dat v GERAN. Umožněním přesného řízení časování pro více souběžných uživatelů paketových dat maximalizuje využití dostupných TDMA rámců. Bez takového mechanismu by uplinkové přenosy utrpěly časovým driftem, způsobily kolize a vyžadovaly rozsáhlé retransmise, což by výrazně degradovalo propustnost a latenci služeb jako mobilní prohlížení internetu a e-mail. Jeho návrh odráží adaptaci robustního konceptu časového předstihu GSM na dynamičtější a sdílenou povahu paketového provozu.

## K čemu slouží

PTCCH byl zaveden, aby vyřešil základní výzvu při migraci sítí GSM z čistě okruhově přepínaného hlasu na integrované paketové datové služby s GPRS. V klasickém GSM pro hovory se časový předstih stanoví během sestavení hovoru a může být aktualizován prostřednictvím signalizace v pásmu na vyhrazeném kanálu pro přenos. Nicméně paketové datové relace se vyznačují přerušovanými, nepravidelnými přenosy, kdy mobilní stanice nemusí vysílat kontinuálně, což činí vyhrazenou signalizaci v pásmu neefektivní a náročnou na zdroje.

Primární problém, který PTCCH řeší, je potřeba efektivní, sdílené kontroly časování pro více uživatelů multiplexovaných na stejných paketových datových kanálech. GPRS zavedlo koncept Dočasného blokového toku (TBF) pro krátké datové bursty. Udržování přesného časového předstihu pro potenciálně desítky mobilních stanic s občasnými datovými bursty vyžadovalo vyhrazený řídicí mechanismus s nízkou režií. PTCCH poskytuje společný zdroj, kde lze časování spravovat pro skupinu uživatelů bez spotřeby šířky pásma v jejich individuálních datových tocích, čímž řeší problém alokace zdrojů vlastní aplikaci metod pro přepojování okruhů na paketová data.

Historicky, před PTCCH, neexistovala standardizovaná metoda pro správu časového předstihu v paketovém kontextu v rámci GSM. Vytvoření PTCCH bylo motivováno potřebou zajistit technickou životaschopnost a efektivitu GPRS, což mu umožnilo podporovat životaschopný počet simultánních datových uživatelů s přijatelnou kvalitou služby. Řešilo to omezení přizpůsobení signalizace orientované na hlas, což umožnilo GERAN vyvinout se v platformu pro mobilní data, což byl klíčový krok v přechodu k 3G a dalším generacím.

## Klíčové vlastnosti

- Vyhrazený logický kanál pro řízení časového předstihu paketových dat
- Dvojitá struktura podkanálů: PTCCH/D (Downlink) a PTCCH/U (Uplink)
- Podporuje aktualizace časového předstihu pro více MS pomocí sdíleného zdroje
- Umožňuje přesnou synchronizaci uplinku pro GPRS a EDGE PDCH
- Nedílná součást správy zdrojů Dočasného blokového toku (TBF)
- Snižuje interferenci a maximalizuje spektrální účinnost v paketovém režimu

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [PDCH – Packet Data Channel](/mobilnisite/slovnik/pdch/)
- [TBF – Temporary Block Flow](/mobilnisite/slovnik/tbf/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PTCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptcch/)
