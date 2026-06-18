---
slug: "ncsg"
url: "/mobilnisite/slovnik/ncsg/"
type: "slovnik"
title: "NCSG – Network Controlled Small Gap"
date: 2025-01-01
abbr: "NCSG"
fullName: "Network Controlled Small Gap"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ncsg/"
summary: "Plánovací mechanismus, při kterém síť instruuje zařízení, aby vytvářelo krátké, naplánované mezery v příjmu/vysílání na obsluhující buňce za účelem provádění měření na jiných frekvencích nebo technolo"
---

NCSG je síťově řízený plánovací mechanismus, který zařízení instruuje, aby vytvářelo krátké, naplánované mezery ve své komunikaci za účelem provádění měření na jiných frekvencích nebo technologiích rádiového přístupu.

## Popis

Network Controlled Small Gap (NCSG, síťově řízená krátká mezera) je mechanismus konfigurace měřicích mezer definovaný ve specifikacích 3GPP pro LTE a NR. Měřicí mezera je období, kdy je uživatelskému zařízení (UE) dovoleno dočasně přeladit svůj přijímač z frekvence obsluhující buňky, aby provedlo měření na jiných frekvencích nebo jiných technologiích rádiového přístupu ([RAT](/mobilnisite/slovnik/rat/)), například měření buňky LTE při připojení k buňce NR nebo naopak. Na rozdíl od autonomních mezer, kde načasování rozhoduje UE, je NCSG explicitně plánována a řízena sítí (gNB nebo [eNB](/mobilnisite/slovnik/enb/)) prostřednictvím signalizace řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)).

Z architektonického hlediska provoz NCSG zahrnuje koordinaci mezi vrstvou RRC v síti a UE. Síť určuje potřebu měření na základě faktorů, jako jsou mobilní politiky nebo vyrovnávání zátěže. Poté nakonfiguruje UE pomocí vzoru NCSG prostřednictvím RRC zprávy (např. RRCConnectionReconfiguration v LTE nebo RRCReconfiguration v NR). Tento vzor specifikuje parametry, jako je délka mezery, perioda (nebo offset) opakování mezery a účel měření (např. kterou frekvenci nebo RAT měřit). Fyzická vrstva a plánovač UE se pak tohoto vzoru drží a přerušují komunikaci s obsluhující buňkou během těchto předem definovaných krátkých mezer, aby provedly požadovaná měření.

Klíčovým technickým aspektem je „krátká“ a „řízená“ povaha mezery. Síť má přesnou znalost o tom, kdy bude UE nedostupné, což jí umožňuje plánovat downlinkové přenosy a uplinkové granty kolem těchto mezer, aby se minimalizovalo přerušení datového toku. To je pro určité scénáře efektivnější než dlouhé, periodické vzory měřicích mezer (jako vzor #0), protože poskytuje jemnější úroveň kontroly. NCSG hraje klíčovou roli v nasazeních s agregací nosných a duální konektivitou, kde UE potřebuje měřit sekundární komponentní nosné nebo buňky na sekundárním uzlu, aniž by na delší dobu ztratila synchronizaci s primární obsluhující buňkou.

## K čemu slouží

NCSG byl vyvinut jako flexibilnější a efektivnější alternativa k tradičním vzorům měřicích mezer s pevnou periodou pro mezifrekvenční a mezisystémová mobilní měření. Tradiční vzory mezer (např. 6 ms mezera každých 40 ms nebo 80 ms) jsou rigidní a mohou způsobit významné přerušení datového toku, zejména u služeb citlivých na latenci. Jak se sítě vyvíjely s agregací nosných, duální konektivitou a hustými nasazeními, potřeba častých, cílených měření vzrostla, čímž se režie dlouhých periodických mezer stala nežádoucí.

Účelem NCSG je dát síti explicitní kontrolu nad načasováním a délkou těchto přerušení pro měření. To síti umožňuje plánovat mezery během méně kritických období pro konkrétní datovou relaci UE, čímž optimalizuje propustnost a latenci. Je motivován zejména scénáři duální konektivity LTE-NR ([EN-DC](/mobilnisite/slovnik/en-dc/), [NGEN-DC](/mobilnisite/slovnik/ngen-dc/)), kde UE připojené k kotvící buňce LTE potřebuje provádět měření na buňkách NR. NCSG umožňuje efektivní objevování a měření vrstvy NR bez vážného dopadu na probíhající datovou relaci LTE. Řeší omezení univerzálních vzorů mezer zavedením konfigurovatelné, sítí optimalizované schopnosti plánování měření.

## Klíčové vlastnosti

- Konfigurováno sítí prostřednictvím RRC signalizace (např. MeasGapConfig)
- Definuje specifické, krátkodobé mezery (např. submilisekundové nebo několikamilisekundové) pro měření
- Umožňuje přesné plánování přerušení pro měření, aby se minimalizoval dopad na datovou relaci
- Podporuje měření pro mezifrekvenční LTE, NR a mezisystémové scénáře
- Nezbytné pro efektivní provoz v nastaveních s agregací nosných a duální konektivitou
- Lze konfigurovat na frekvenci nebo na měřicí objekt, což poskytuje jemnozrnnou kontrolu

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.894** (Rel-13) — Study on LTE Measurement Gap Enhancement
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [NCSG na 3GPP Explorer](https://3gpp-explorer.com/glossary/ncsg/)
