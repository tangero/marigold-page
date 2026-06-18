---
slug: "scpich"
url: "/mobilnisite/slovnik/scpich/"
type: "slovnik"
title: "SCPICH – Secondary Common Pilot Channel"
date: 2025-01-01
abbr: "SCPICH"
fullName: "Secondary Common Pilot Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/scpich/"
summary: "Downlinkový fyzický kanál v UMTS (WCDMA) používaný k poskytnutí fázové reference pro demodulaci a odhad kanálu, konkrétně pro Sekundární společný řídicí fyzický kanál (S-CCPCH). Napomáhá příjmu stránk"
---

SCPICH je downlinkový fyzický kanál v UMTS, který poskytuje fázový referenční signál pro demodulaci S-CCPCH a napomáhá příjmu stránkovacích a vysílacích informací.

## Popis

Sekundární společný pilotní kanál (SCPICH) je vyhrazený downlinkový fyzický kanál v rádiovém rozhraní Universal Mobile Telecommunications System (UMTS) Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([WCDMA](/mobilnisite/slovnik/wcdma/)). Je to kontinuální kanál vysílaný Node B (základnovou stanicí) a slouží jako známý referenční signál. Na rozdíl od Primárního společného pilotního kanálu ([P-CPICH](/mobilnisite/slovnik/p-cpich/)), který je specifický pro buňku a používá se jako primární fázová reference pro mnoho kanálů, je SCPICH specificky asociován se Sekundárním společným řídicím fyzickým kanálem ([S-CCPCH](/mobilnisite/slovnik/s-ccpch/)). S-CCPCH přenáší důležité transportní kanály: Stránkovací kanál ([PCH](/mobilnisite/slovnik/pch-text-pch/)) a Kanál přímého přístupu ([FACH](/mobilnisite/slovnik/fach/)).

Primární technickou funkcí SCPICH je poskytovat koherentní fázovou referenci pro demodulaci S-CCPCH. Ve WCDMA přijímač používá pilotní signál k odhadu charakteristik rádiového kanálu, jako je fázová rotace a útlum amplitudy způsobený prostředím šíření. UE používá známé bity vysílané na SCPICH k provedení odhadu kanálu. Tato odhadnutá odezva kanálu je následně aplikována pro správnou demodulaci datových symbolů na přidruženém S-CCPCH. SCPICH je charakterizován svým kanalizačním kódem a volitelně i skramblovacím kódem. Vysílá předdefinovanou sekvenci bitů (typicky samé nuly nebo známý vzor).

Z architektonické perspektivy je SCPICH součástí struktury kanalizace a skramblování fyzické vrstvy. Sám nepřenáší informace vyšších vrstev, ale je podpůrným kanálem pro signalizaci řídicí roviny. Přítomnost a konfigurace SCPICH je síťou signalizována uživatelskému zařízení (UE) prostřednictvím bloků systémových informací ([SIB](/mobilnisite/slovnik/sib/)) nebo vyhrazených zpráv řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)). Použití vyhrazeného SCPICH pro S-CCPCH, namísto spoléhání se pouze na P-CPICH, může v určitých scénářích zlepšit výkon příjmu, například když je S-CCPCH vysílán s jiným anténním diagramem (např. beamforming) nebo když je primární pilot nedostatečný pro spolehlivý odhad kanálu na specifické kódové dráze řídicího kanálu.

## K čemu slouží

SCPICH byl zaveden za účelem zvýšení spolehlivosti a výkonu příjmu kritických downlinkových řídicích informací přenášených na S-CCPCH, konkrétně stránkovacích a zpráv společných kanálů. V původním návrhu UMTS Release 99 sloužil P-CPICH jako výchozí fázová reference pro většinu fyzických kanálů. Nicméně S-CCPCH, který přenáší PCH a FACH, je zásadní pro přístup k síti, stránkování mobilních zařízení a odesílání vysílacích informací. Spoléhání se pouze na P-CPICH pro demodulaci těchto kanálů by mohlo být suboptimální, pokud S-CCPCH zažívá odlišné podmínky rádiového kanálu.

SCPICH tento problém řeší tím, že poskytuje vyhrazený pilotní signál ve stejném kanálu, specificky přizpůsobený přenosovým charakteristikám S-CCPCH. Toto zajišťuje přesnější odhad kanálu pro samotný S-CCPCH, což vede k nižší chybovosti při dekódování stránkovacích a přístupových zpráv. Tím se zlepšuje úspěšnost příjmu stránkování (kritická pro nastavení hovoru a úsporu energie) a spolehlivost vysílání systémových informací na FACH. Jeho zavedení bylo motivováno potřebou zajistit robustní provoz řídicích kanálů v různých scénářích nasazení, včetně těch, kde mohou být pro společné kanály použity pokročilé anténní techniky, čímž se zvyšuje celková dostupnost a spolehlivost systému.

## Klíčové vlastnosti

- Poskytuje vyhrazenou fázovou referenci pro Sekundární společný řídicí fyzický kanál (S-CCPCH)
- Přenáší předdefinovanou, známou bitovou sekvenci pro odhad kanálu
- Definován specifickým kanalizačním kódem v rámci WCDMA downlinku
- Podporuje demodulaci Stránkovacího kanálu (PCH) a Kanálu přímého přístupu (FACH)
- Konfigurace je vysílána k UE prostřednictvím systémových informací
- Zvyšuje spolehlivost příjmu pro kritickou signalizaci v režimu nečinnosti a připojení

## Související pojmy

- [S-CCPCH – Secondary Common Control Physical Channel](/mobilnisite/slovnik/s-ccpch/)
- [P-CPICH – Primary Common Pilot Channel](/mobilnisite/slovnik/p-cpich/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)

## Definující specifikace

- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications

---

📖 **Anglický originál a plná specifikace:** [SCPICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/scpich/)
