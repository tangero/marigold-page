---
slug: "ncr-mt"
url: "/mobilnisite/slovnik/ncr-mt/"
type: "slovnik"
title: "NCR-MT – Network Controlled Repeater – Mobile Termination"
date: 2026-01-01
abbr: "NCR-MT"
fullName: "Network Controlled Repeater – Mobile Termination"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ncr-mt/"
summary: "Komponenta síťově řízeného opakovače, která zahrnuje funkci mobilní terminace a umožňuje opakovači připojit se k síti jako UE. Umožňuje centralizované řízení a optimalizaci provozu opakovačů, čímž zle"
---

NCR-MT je komponenta typu mobilní terminace v síťově řízeném opakovači, která mu umožňuje připojit se k síti jako uživatelské zařízení za účelem centralizovaného řízení a optimalizace.

## Popis

Network Controlled Repeater – Mobile Termination (NCR-MT) je funkční komponenta zavedená ve specifikaci 3GPP Release 18 jako součást architektury síťově řízeného opakovače ([NCR](/mobilnisite/slovnik/ncr/)). Odkazuje na aspekt mobilní terminace v rámci NCR, který umožňuje opakovači navázat spojení se sítí obdobně jako uživatelské zařízení (UE). To síti umožňuje spravovat a řídit opakovač prostřednictvím standardních signalizačních protokolů, namísto toho aby fungoval jako samostatné, neřízené zařízení. NCR-MT umožňuje centralizovanou optimalizaci parametrů opakovače, jako je zesílení nebo beamforming, na základě stavu sítě a nastavených politik.

Z architektonického hlediska se NCR skládá ze dvou hlavních částí: mobilní terminace (NCR-MT) a opakovačové terminace (NCR-RT). NCR-MT zajišťuje spojení řídicí roviny se sítí, včetně procedur jako registrace, autentizace a přijímání řídicích příkazů. Používá standardní protokoly pro UE, jako jsou [RRC](/mobilnisite/slovnik/rrc/) a [NAS](/mobilnisite/slovnik/nas/), ke komunikaci s gNB a jádrem sítě. NCR-RT na druhé straně spravuje zesílení a přeposílání provozu uživatelské roviny mezi UE a sítí. Oddělením těchto funkcí NCR-MT umožňuje síti přistupovat k opakovači jako k řízenému uzlu, což umožňuje jeho dynamickou konfiguraci a monitorování.

Princip fungování NCR-MT spočívá v tom, že opakovač iniciuje připojení k síti pomocí své [MT](/mobilnisite/slovnik/mt/) funkce, podobně jako když se UE připojuje k buňce. Po připojení může síť odesílat řídicí zprávy pro úpravu nastavení opakovače, například zapínání nebo vypínání konkrétních paprsků, úpravu úrovní zesílení nebo vyžádání hlášení o stavu. Toho je dosaženo prostřednictvím definovaných signalizačních procedur, které často využívají stávající protokoly pro UE rozšířené o příkazy specifické pro opakovače. NCR-MT zajišťuje, že opakovač pracuje v souladu s cíli optimalizace sítě, jako je minimalizace interference nebo zlepšení pokrytí v určených oblastech.

Klíčové součásti NCR-MT zahrnují protokolový stack pro signalizaci řídicí roviny, rozhraní pro přijímání síťových příkazů a mechanismy pro převod těchto příkazů na akce na straně opakovačové terminace. Integruje se se systémy správy sítě, aby umožnil automatizované řídicí smyčky, v nichž síť upravuje parametry opakovače na základě zpětné vazby v reálném čase. NCR-MT hraje klíčovou roli při zvyšování inteligence a síťového povědomí opakovačů, což je posun oproti tradičním analogovým nebo jednoduchým digitálním opakovačům. To zvyšuje škálovatelnost a efektivitu nasazení opakovačů v sítích 5G a budoucích generacích.

## K čemu slouží

NCR-MT byl vytvořen, aby řešil omezení tradičních opakovačů, které často fungovaly nezávisle bez koordinace se sítí, což vedlo k problémům jako interference, neoptimální výkon a obtížná správa. Vzhledem k tomu, že sítě 5G vyžadují vyšší kapacitu a pokrytí, zejména v náročných prostředích, vznikla potřeba opakovačů, které by mohly být centrálně řízeny a optimalizovány. NCR-MT tento problém řeší tím, že umožňuje opakovačům připojit se k síti jako řízené entity, což umožňuje dynamické přizpůsobování jejich chování na základě stavu sítě.

Historický kontext zahrnuje vývoj technologie opakovačů od jednoduchých zařízení typu zesiluj-a-předej ke komplexnějším inteligentním řešením. Dřívější opakovače postrádaly síťové povědomí, což je činilo náchylnými k vytváření interference nebo zesilování šumu. NCR-MT jako součást širšího rámce [NCR](/mobilnisite/slovnik/ncr/) zavádí standardizované řídicí mechanismy, které operátorům umožňují integrovat opakovače do jejich ekosystémů správy sítě. Tím se zaplňuje mezera mezi samostatnými nasazeními opakovačů a síťově řízenou infrastrukturou.

Motivace pro NCR-MT zahrnuje potřebu flexibilního rozšíření pokrytí v sítích 5G, podporu beamformingu a massive [MIMO](/mobilnisite/slovnik/mimo/) a snížení provozních nákladů prostřednictvím automatizace. Díky umožnění síťového řízení řeší problémy spojené s konfigurací, optimalizací a odstraňováním závad opakovačů, čímž zvyšuje celkový výkon sítě. To je obzvláště důležité pro hustě zastavěné městské oblasti, vnitřní pokrytí a rozšíření na venkově, kde opakovače hrají klíčovou roli v poskytování služeb.

## Klíčové vlastnosti

- Poskytuje funkci mobilní terminace pro síťově řízené opakovače
- Umožňuje centralizované řízení prostřednictvím standardních signalizačních protokolů pro UE
- Podporuje dynamickou konfiguraci parametrů opakovače, jako je zesílení a paprsky
- Integruje se se správou sítě pro automatizovanou optimalizaci
- Umožňuje hlášení stavu a monitorování z opakovačů
- Zlepšuje pokrytí a kapacitu při současné minimalizaci interference

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.114** (Rel-19) — EMC Requirements for NR Repeaters and NCR
- **TS 38.115** (Rel-19) — NR Repeater RF Conformance Testing Part 1
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TR 38.867** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [NCR-MT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ncr-mt/)
