---
slug: "tdf-u"
url: "/mobilnisite/slovnik/tdf-u/"
type: "slovnik"
title: "TDF-U – Traffic Detection Function User plane function"
date: 2025-01-01
abbr: "TDF-U"
fullName: "Traffic Detection Function User plane function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tdf-u/"
summary: "Uživatelská rovinná funkce v 5G jádře sítě odpovědná za zkoumání a detekci aplikačních toků provozu. Umožňuje vynucování politik, účtování a směrování provozu na základě hluboké kontroly paketů, čímž"
---

TDF-U je uživatelská rovinná funkce v 5G jádře sítě, která zkoumá aplikační toky provozu, aby umožnila vynucování politik, účtování a směrování provozu na základě hluboké kontroly paketů.

## Popis

Funkce pro detekci provozu v uživatelské rovině (TDF-U) je specializovaná síťová funkce v architektuře založené na službách ([SBA](/mobilnisite/slovnik/sba/)) 5G jádra (5GC), která funguje v přenosové cestě uživatelské roviny. Jejím hlavním úkolem je provádět detekci a hlášení aplikací ([ADR](/mobilnisite/slovnik/adr/)) zkoumáním datových paketů uživatelských relací. Na rozdíl od funkcí řídicí roviny je TDF-U nasazena v cestě přenosu dat, typicky mezi funkcí uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) a externí datovou sítí ([DN](/mobilnisite/slovnik/dn/)). Zkoumá hlavičky a obsah paketů pomocí technik hluboké kontroly paketů (DPI), aby identifikovala konkrétní aplikace, služby nebo typy provozu na základě předem nakonfigurovaných detekčních pravidel. Tato pravidla mohou být založena na signaturách, behaviorální analýze nebo modelech strojového učení.

Architektonicky je TDF-U řízena funkcí správy relací ([SMF](/mobilnisite/slovnik/smf/)) přes referenční bod N40 pomocí služby správy popisu toku paketů ([PFD](/mobilnisite/slovnik/pfd/)). SMF zajišťuje TDF-U detekčními pravidly a politikami pro aplikace. Když uživatelský provoz prochází TDF-U, porovnává pakety s těmito pravidly. Po detekci odpovídajícího toku provozu může TDF-U podniknout několik akcí. O události detekce může nahlásit SMF nebo funkci řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) přes rozhraní N7/N15, což pak může spustit rozhodnutí o politice. Případně může aplikovat lokální akce, jako je označování provozu, přesměrování nebo blokování, v souladu se svými nakonfigurovanými politikami.

TDF-U hraje klíčovou roli při umožnění sítí s povědomím o službách. Identifikací aplikačního provozu umožňuje operátorům implementovat diferencované účtování (např. zero-rating pro konkrétní aplikace), vynucovat politiky kvality služeb (QoS) přizpůsobené potřebám aplikace (jako je upřednostňování streamování videa) a provádět optimalizaci provozu (např. transkódování videa). Je klíčovým prvkem pro síťové segmenty (network slicing), protože dokáže identifikovat provoz patřící do konkrétního segmentu a směrovat jej na příslušné zdroje. Její integrace v rámci SBA 5GC zajišťuje, že jde o škálovatelnou, softwarově definovanou komponentu, kterou lze flexibilně nasadit v centrálních nebo edge cloudových lokalitách.

## K čemu slouží

TDF-U byla zavedena, aby řešila rostoucí potřebu detailního, na aplikace zaměřeného řízení provozu a vynucování politik v mobilních sítích. Tradiční architektury řízení politik a účtování ([PCC](/mobilnisite/slovnik/pcc/)) se silně spoléhaly na signalizaci v řídicí rovině a statická pravidla, která byla neefektivní pro dynamickou identifikaci široké škály OTT aplikací a služeb. Operátoři potřebovali metodu pro zkoumání provozu v uživatelské rovině v reálném čase, aby mohli aplikovat přesné účtování, zajistit spravedlivé využívání a nabídnout záruky kvality specifické pro služby.

Její vytvoření bylo motivováno evolucí směrem k 5G a síťovým segmentům, kde různé segmenty (např. pro rozšířené mobilní širokopásmové připojení, IoT nebo ultra-spolehlivou komunikaci s nízkou latencí) vyžadují odlišné zacházení. Obecná uživatelská rovina nemohla bez hluboké kontroly efektivně rozlišovat provoz. TDF-U poskytuje standardizovanou, na dodavateli nezávislou funkci, která odděluje detekční logiku od jádrové UPF, což umožňuje specializované možnosti DPI a nezávislé škálování. Tím se řeší problém monolitických UPF, které bylo obtížné inovovat novými detekčními schopnostmi, a umožňuje flexibilnější řetězení služeb.

Historicky podobné funkce existovaly v 4G EPC jako funkce pro detekci provozu (TDF), ale často šlo o samostatný uzel. V 5G je TDF-U integrována jako specializovaná funkce uživatelské roviny v rámci SBA, což nabízí lepší orchestraci, cloudové nasazení a bezproblémovou interakci s PCF a SMF. Tím se řeší omezení předchozích přístupů poskytnutím programovatelnější, škálovatelnější a na služby orientované architektury pro analýzu provozu v reálném čase.

## Klíčové vlastnosti

- Hluboká kontrola paketů (DPI) pro detekci aplikací a služeb
- Integrace s architekturou založenou na službách 5GC přes rozhraní N40
- Podpora detekce a hlášení aplikací (ADR) funkcím řídicí roviny
- Schopnosti směrování a přesměrování provozu na základě výsledků detekce
- Vynucování politik v uživatelské rovině pro akce účtování a QoS
- Podpora síťových segmentů (network slicing) identifikací toků provozu specifických pro segment

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [PFD – Packet Flow Description](/mobilnisite/slovnik/pfd/)

## Definující specifikace

- **TS 23.214** (Rel-19) — Control and User Plane Separation for EPC
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.844** (Rel-14) — Control and User Plane Separation for EPC Nodes

---

📖 **Anglický originál a plná specifikace:** [TDF-U na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdf-u/)
