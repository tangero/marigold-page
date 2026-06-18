---
slug: "peecmon"
url: "/mobilnisite/slovnik/peecmon/"
type: "slovnik"
title: "PEECMON – PEE Control and Monitoring"
date: 2025-01-01
abbr: "PEECMON"
fullName: "PEE Control and Monitoring"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/peecmon/"
summary: "PEECMON je funkce správy podle 3GPP pro řízení a sledování aspektů výkonu a energetické účinnosti (Power and Energy Efficiency, PEE) síťového zařízení. Umožňuje operátorům spravovat energetickou spotř"
---

PEECMON je funkce správy (management function) podle 3GPP pro řízení a sledování (control and monitoring) aspektů výkonu a energetické účinnosti (Power and Energy Efficiency) síťového zařízení za účelem správy spotřeby, optimalizace využití a reportingu metrik.

## Popis

PEECMON ([PEE](/mobilnisite/slovnik/pee/) Control and Monitoring) je standardizovaná funkce správy definovaná ve specifikacích 3GPP, primárně v TS 28.305. Funguje v širším kontextu systémů správy sítě se zaměřením konkrétně na doménu výkonu a energetické účinnosti (Power and Energy Efficiency, PEE). Architektura PEECMON zahrnuje řídicí entity, které komunikují se síťovými elementy, jako jsou základnové stanice a uzly páteřní sítě, za účelem sběru energetických dat a vynucování politik pro úsporu energie. Tyto entity typicky zahrnují systém správy sítě (Network Management, [NM](/mobilnisite/slovnik/nm/)), který hostuje funkcionalitu PEECMON a komunikuje se systémy správy elementů (Element Management, [EM](/mobilnisite/slovnik/em/)) nebo přímo se síťovými funkcemi (Network Functions, [NF](/mobilnisite/slovnik/nf/)) pomocí standardizovaných rozhraní, jako je Itf-N nebo servisně orientovaná rozhraní v 5G.

V provozu PEECMON funguje tak, že definuje sadu spravovaných objektů, měření výkonu a parametrů správy poruch souvisejících se spotřebou energie. Shromažďuje data o spotřebě energie, metrikách energetické účinnosti (např. bity na joule) a environmentálních faktorech (např. teplota) ze síťového zařízení. Tato data jsou následně zpracována za účelem sledování energetického výkonu, detekce anomálií a generování reportů. PEECMON také podporuje řídicí funkce, jako je aktivace nebo deaktivace funkcí pro úsporu energie (např. režimy spánku v základnových stanicích) na základě vytížení sítě nebo politik operátora. Mezi klíčové komponenty patří služba správy PEE (PEE Management Service, PEE-MS), která poskytuje základní schopnosti, a související informační modely standardizující způsob reprezentace a výměny energetických dat.

Role PEECMON v síti je klíčová pro umožnění energeticky uvědomělých operací. Integruje se s dalšími funkcemi správy, jako je správa výkonu (Performance Management, [PM](/mobilnisite/slovnik/pm/)) a správa poruch (Fault Management, [FM](/mobilnisite/slovnik/fm/)), a poskytuje tak komplexní pohled na výkon a účinnost sítě. Díky standardizaci energetického managementu umožňuje PEECMON operátorům implementovat konzistentní strategie úspory energie v multi-vendorových sítích a zajišťuje interoperabilitu. Podporuje případy užití, jako je dynamické škálování výkonu, kdy jsou síťové zdroje přizpůsobovány na základě provozních vzorců tak, aby se snížila spotřeba energie bez kompromisů v kvalitě služeb. PEECMON navíc usnadňuje soulad s regulatorními požadavky a iniciativami udržitelnosti poskytováním ověřitelných reportů o energetické účinnosti.

## K čemu slouží

PEECMON byl vytvořen jako odpověď na rostoucí potřebu energetické účinnosti v mobilních sítích, kterou pohánějí rostoucí náklady na energii, environmentální obavy a expanze síťové infrastruktury (např. s nasazením 5G). Před jeho standardizací byl energetický management často závislý na konkrétním dodavateli, postrádal interoperabilitu a konzistentní metriky, což operátorům ztěžovalo optimalizaci využití energie v různorodém zařízení. Mezi omezení předchozích přístupů patřila fragmentovaná řídicí rozhraní, nedostatečné možnosti reportingu a absence jednotného způsobu řízení funkcí pro úsporu energie, což vedlo k neoptimálnímu energetickému výkonu a vyšším provozním nákladům.

Motivace pro PEECMON vychází z důrazu 3GPP na udržitelnost a provozní efektivitu, zvláště když sítě rostou, aby podporovaly vyšší přenosové rychlosti a více zařízení. Zavedením standardizovaného rámce pro řízení a sledování [PEE](/mobilnisite/slovnik/pee/) umožňuje 3GPP operátorům snižovat jejich uhlíkovou stopu a náklady na energii. Historicky byl energetický management řešen ad-hoc nebo prostřednictvím proprietárních řešení, ale s PEECMON se stává nedílnou součástí správy sítě v souladu s globálními snahami, jako jsou Cíle udržitelného rozvoje OSN. Řeší problémy jako nekonzistentní měření energie, nedostatečná kontrola nad mechanismy úspory energie a obtížné srovnávání účinnosti napříč segmenty sítě.

PEECMON také řeší technické výzvy moderních sítí, kde je spotřeba energie významným faktorem v celkových nákladech na vlastnictví (Total Cost of Ownership, TCO). Například v 5G sítích s massive [MIMO](/mobilnisite/slovnik/mimo/) a hustým nasazením může spotřeba energie rapidně narůstat. PEECMON poskytuje nástroje pro monitorování a zmírnění tohoto růstu a podporuje funkce jako síťové segmentování (network slicing) s energeticky uvědomělou alokací zdrojů. Díky standardizaci ve verzi 15 (Release 15) a vývoji v následujících verzích zajišťuje, že energetický management drží krok s pokrokem sítí a umožňuje inteligentnější a ekologičtější provoz.

## Klíčové vlastnosti

- Standardizovaný sběr měření energetického výkonu
- Řízení funkcí pro úsporu energie (např. režimy spánku)
- Správa poruch pro energetické anomálie
- Integrace se systémy správy sítě (NM/EM)
- Podpora multi-vendorové interoperability
- Reporting a analytika pro energetickou účinnost

## Související pojmy

- [PEE – Power, Energy and Environmental](/mobilnisite/slovnik/pee/)
- [NM – Network Management](/mobilnisite/slovnik/nm/)
- [EM – Electromagnetic Emanations](/mobilnisite/slovnik/em/)

## Definující specifikace

- **TS 28.305** (Rel-19) — PEE Control & Monitoring IRP Information Service

---

📖 **Anglický originál a plná specifikace:** [PEECMON na 3GPP Explorer](https://3gpp-explorer.com/glossary/peecmon/)
