---
slug: "w-5gban"
url: "/mobilnisite/slovnik/w-5gban/"
type: "slovnik"
title: "W-5GBAN – Wireline 5G BBF Access Network"
date: 2026-01-01
abbr: "W-5GBAN"
fullName: "Wireline 5G BBF Access Network"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/w-5gban/"
summary: "Konkrétní implementace W-5GAN založená na architekturách Broadband Forum (BBF). Definuje, jak se přístupové uzly specifikované BBF (jako ONU a OLT) integrují s 5G Core prostřednictvím bránové funkce,"
---

W-5GBAN je 3GPP implementace drátové přístupové sítě 5G založená na architekturách Broadband Forum, která integruje optické přístupové uzly s 5G Core pro poskytování služeb 5G prostřednictvím pevných širokopásmových připojení.

## Popis

Wireline 5G [BBF](/mobilnisite/slovnik/bbf/) Access Network (W-5GBAN) je specializovaný architektonický profil v rámci širšího rámce [W-5GAN](/mobilnisite/slovnik/w-5gan/), který se výslovně zaměřuje na integraci s přístupovými sítěmi standardizovanými Broadband Forum (BBF). Architektury BBF, jako jsou ty pro Fiber-to-the-Home (FTTH) využívající [PON](/mobilnisite/slovnik/pon/) technologie ([GPON](/mobilnisite/slovnik/gpon/), XGS-PON), definují vlastní síťové elementy a protokoly. W-5GBAN specifikuje, jak se tyto síťové elementy BBF propojují s 5G Core za účelem poskytování služeb 5G drátovým abonentům.

Jádrem W-5GBAN je funkce pro vzájemné propojení, která je v tomto kontextu často označována jako BBF-specifická Access Gateway Function. Tato funkce ukončuje uživatelsko-rovinové a řídicí protokoly definované BBF (např. ty mezi Optical Network Unit (ONU) a Optical Line Terminal (OLT)). Mapuje relace abonentů BBF a přidružené parametry (jako identifikátory vedení, [VLAN](/mobilnisite/slovnik/vlan/)) na odpovídající 5G konstrukty. Konkrétně vytváří nezbytná rozhraní [N2](/mobilnisite/slovnik/n2/) (řídicí rovina k [AMF](/mobilnisite/slovnik/amf/)) a N3 (uživatelská rovina k [UPF](/mobilnisite/slovnik/upf/)) pro každé drátové UE, kterým je typicky residenční brána nebo CPE připojené k ONU.

Operačně, když zařízení v síti BBF požaduje služby 5G, BBF přístupová brána autentizuje abonenta u 5G Core pomocí 5G-AKA přes rozhraní N2. Po úspěšné autentizaci je zřízena PDU Session. Provoz uživatelské roviny z CPE je následně zapouzdřen pomocí 5G protokolů (jako GTP-U) přes rozhraní N3 do UPF, čímž se obejdou tradiční širokopásmové síťové brány (BNG). To umožňuje, aby SMF a PCF 5G Core spravovaly QoS relace, uplatňovaly pravidla politik a umožňovaly funkce jako network slicing přímo pro koncový bod připojený optickým vláknem. W-5GBAN tak transformuje pasivní optickou distribuční síť na přístupovou větev 5G Systému, kterou zcela spravují síťové funkce 5G Core.

## K čemu slouží

W-5GBAN byl vyvinut, aby poskytl konkrétní a standardizovanou metodu pro integraci rozsáhlé stávající i budoucí infrastruktury optického přístupu – již celosvětově nasazené na základě standardů BBF – do ekosystému 5G. Před W-5GBAN se optické sítě a mobilní sítě vyvíjely nezávisle. Optické sítě využívaly BNG pro správu abonentů a přístup k internetu, kterým chybělo dynamické řízení relací, network slicing a integrovaná kontrola politik vlastní 5G. Toto oddělení bránilo operátorům v nabídce jednotných služeb.

Konkrétní problém, který W-5GBAN řeší, je nesoulad protokolů a architektur mezi architekturami BBF založenými na TR-069, TR-101 nebo TR-178 a 3GPP 5G Service-Based Architecture. Poskytuje definovanou migrační cestu pro operátory s významnými investicemi do optických sítí, aby mohli modernizovat své sítě bez výměny fyzického optického vedení a optických uzlů. Vytvořením standardizované bránové funkce zajišťuje interoperabilitu mezi více dodavateli zařízení BBF a dodavateli 5G Core.

Motivován potřebou hluboké konvergence umožňuje W-5GBAN operátorům využít vysokou propustnost a nízkou latenci optického vlákna jako prémiové přístupové médium pro služby 5G. Umožňuje případy užití, jako je 5G pro podniky založené na optice, ultra-spolehlivý domácí broadband s SLA na úrovni 5G a efektivní distribuce multicastového videa přes plátkovanou síť. Jeho vytvoření v Release 16 společně s W-5GAN poskytlo potřebnou specifičnost pro dominantní drátovou technologii (PON), což zajišťuje rychlé přijetí a nasazení v průmyslu.

## Klíčové vlastnosti

- Standardizovaná integrace sítí PON specifikovaných BBF (GPON/XGS-PON) s 5GC
- Definuje vzájemné propojení protokolů BBF (např. OMCI, TWAMP) a rozhraní 5G N2/N3
- Umožňuje poskytování služeb 5G pro optické síťové jednotky (ONU) a CPE spravované BBF
- Podporuje mapování parametrů QoS BBF (např. třídy provozu) na 5G QoS Flows
- Umožňuje výběr optického přístupu jako typu přístupu pro instanci síťového plátku
- Usnadňuje jednotnou správu, provoz a údržbu (OAM) pro kombinované optické a 5G síťové služby

## Související pojmy

- [BBF – Bearer Binding Function](/mobilnisite/slovnik/bbf/)
- [PON – Passive Optical Network](/mobilnisite/slovnik/pon/)
- [W-5GAN – Wireline 5G Access Network](/mobilnisite/slovnik/w-5gan/)

## Definující specifikace

- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3

---

📖 **Anglický originál a plná specifikace:** [W-5GBAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/w-5gban/)
