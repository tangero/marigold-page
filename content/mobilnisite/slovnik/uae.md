---
slug: "uae"
url: "/mobilnisite/slovnik/uae/"
type: "slovnik"
title: "UAE – UAS Application Enabler"
date: 2026-01-01
abbr: "UAE"
fullName: "UAS Application Enabler"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uae/"
summary: "Rámec 3GPP umožňující služby bezpilotních leteckých systémů (UAS) přes mobilní sítě. Poskytuje standardizovaná rozhraní a procedury pro identifikaci dronů, autorizaci, správu letových tras a konektivi"
---

UAE je rámec 3GPP umožňující služby bezpilotních leteckých systémů (UAS) přes mobilní sítě, který poskytuje standardizovaná rozhraní pro identifikaci dronů, autorizaci, správu letových tras a konektivitu za účelem podpory bezpečných operací BVLOS.

## Popis

[UAS](/mobilnisite/slovnik/uas/) Application Enabler (UAE) je služební kapacita definovaná v rámci architektury 3GPP pro podporu bezpilotních leteckých systémů (UAS), běžně známých jako drony, využívajících sítě 3GPP. Působí jako mezivrstva mezi poskytovateli služeb UAS ([USS](/mobilnisite/slovnik/uss/)) a páteřní sítí 3GPP, která překládá požadavky služeb na aplikační úrovni na síťově specifické příkazy a procedury. Rámec UAE je primárně realizován prostřednictvím funkce [NEF](/mobilnisite/slovnik/nef/) (Network Exposure Function) v 5G Core (5GC) nebo funkce [SCEF](/mobilnisite/slovnik/scef/) (Service Capability Exposure Function) v Evolved Packet Core (EPC), které bezpečně zpřístupňují síťové kapacity autorizovaným aplikacím UAS třetích stran.

Architektonicky definuje UAE sadu aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)) a referenčních bodů, jako jsou Nudm, Nnef a N5g-eir, což umožňuje USS interagovat se sítí pro klíčové funkce UAS. Mezi klíčové procedury patří identifikace a autentizace UAS, kde může UAE dotazovat síť za účelem ověření předplatného a přihlašovacích údajů dronu. Také podporuje autorizaci letových operací kontrolou politik a zakázaných zón a usnadňuje vytváření a správu kvality služeb (QoS) pro spojení velení a řízení ([C2](/mobilnisite/slovnik/c2/)) a datové toky užitečného zatížení, čímž zajišťuje spolehlivou konektivitu s nízkou latencí nezbytnou pro bezpečný provoz dronů.

Dále UAE umožňuje služby polohy a sledování tím, že zpřístupňuje síťově založené nebo UE asistované informace o poloze UAS poskytovateli USS pro řízení letového provozu. Také podporuje síťové řezy (network slicing), což umožňuje vytváření vyhrazených logických sítí se specifickými výkonnostními charakteristikami pro provoz UAS a jeho izolaci od ostatních služeb mobilního širokopásmového připojení. Role UAE je klíčová pro integraci dronů do národního systému vzdušného prostoru, neboť poskytuje nezbytnou síťově asistovanou automatizaci, zabezpečení a soulad s předpisy pro škálovatelná komerční a vládní nasazení UAS.

## K čemu slouží

UAE bylo vytvořeno za účelem řešení rostoucí potřeby standardizované, bezpečné a spolehlivé metody pro integraci bezpilotních leteckých systémů do řízeného vzdušného prostoru pomocí všudypřítomných mobilních sítí. Před jeho specifikací byly operace dronů, zejména [BVLOS](/mobilnisite/slovnik/bvlos/), závislé na nestandardizovaných proprietárních komunikačních spojích (jako je přímé rádiové spojení), kterým chyběla škálovatelnost, inherentní podpora mobility a integrace se širšími systémy řízení letového provozu. To představovalo významné výzvy pro bezpečnost, zabezpečení a regulační dohled a omezovalo komerční potenciál služeb doručování, sledování a inspekce pomocí dronů.

Primární motivací pro UAE v rámci 3GPP bylo využít stávající i budoucí mobilní infrastrukturu – 4G LTE a 5G – k poskytnutí jednotného konektivního řešení pro [UAS](/mobilnisite/slovnik/uas/). Mobilní sítě nabízejí širokoplošné pokrytí, vysokou spolehlivost, vestavěné zabezpečení a pokročilé funkce, jako je správa mobility a QoS, které jsou ideální pro podporu dronů. Rámec UAE řeší problém, jak bezpečně zpřístupnit tyto síťové kapacity externím poskytovatelům služeb UAS a regulačním orgánům, a umožňuje tak automatizovanou letovou autorizaci, sledování v reálném čase a garantovaný komunikační výkon. Jeho vytvoření ve vydání Release 17 bylo hnací silou globálních regulačních snah, jako jsou ty ze strany FAA a EASA, o dálkovou identifikaci a sledování dronů, což pozicuje technologii 3GPP jako klíčový faktor pro digitální transformaci letectví.

## Klíčové vlastnosti

- Standardizovaná API pro integraci poskytovatele služeb UAS (USS) s páteřní sítí 3GPP
- Podpora procedur identifikace, autentizace a autorizace UAS
- Zpřístupnění síťově založených služeb polohy pro sledování UAS
- Správa QoS pro toky velení a řízení (C2) a aplikačních dat
- Podpora síťových řezů pro izolaci provozu UAS se specifickými požadavky na výkon
- Umožňuje soulad s předpisy pro dálkovou identifikaci (Remote ID) a správu letových tras

## Související pojmy

- [UAS – NF Uncrewed Aerial System Network Function](/mobilnisite/slovnik/uas/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [SCS – Subcarrier Spacing](/mobilnisite/slovnik/scs/)

## Definující specifikace

- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 29.257** (Rel-19) — Application layer support for Uncrewed Aerial System (UAS)

---

📖 **Anglický originál a plná specifikace:** [UAE na 3GPP Explorer](https://3gpp-explorer.com/glossary/uae/)
