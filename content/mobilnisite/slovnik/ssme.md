---
slug: "ssme"
url: "/mobilnisite/slovnik/ssme/"
type: "slovnik"
title: "SSME – Service Switching Function Management Entity"
date: 2025-01-01
abbr: "SSME"
fullName: "Service Switching Function Management Entity"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ssme/"
summary: "SSME je řídicí entita zodpovědná za řízení a správu funkce přepínání služeb (SSF) v rámci architektury CAMEL. Zprostředkovává interakci mezi SSF a řídicí funkcí služeb (SCF), čímž umožňuje služby inte"
---

SSME je řídicí entita v architektuře CAMEL, která řídí funkci přepínání služeb (SSF) a zprostředkovává její interakci s řídicí funkcí služeb (SCF) za účelem umožnění služeb inteligentní sítě.

## Popis

Service Switching Function Management Entity (SSME) je klíčová komponenta v architektuře 3GPP Customised Applications for Mobile network Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)), definovaná jako součást rámce Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) pro mobilní sítě. Funguje jako rozhraní pro správu a řízení funkce přepínání služeb ([SSF](/mobilnisite/slovnik/ssf/)), která je typicky integrována v Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) nebo Gateway MSC. Primární funkcí SSME je správa detekčních bodů ([DP](/mobilnisite/slovnik/dp/)) a spouštěcích mechanismů v rámci SSF, které identifikují, kdy hovor nebo relace vyžaduje aplikační logiku založenou na CAMEL. Působí jako zprostředkovatel, přijímá a zpracovává instrukce od řídicí funkce služeb ([SCF](/mobilnisite/slovnik/scf/)), která hostí vlastní aplikační logiku (např. pro předplacené účtování nebo přesměrování hovorů), a zajišťuje jejich správné provedení přepínací funkcí.

Z architektonického hlediska je SSME definována pro zpracování interakcí protokolu [CAP](/mobilnisite/slovnik/cap/) (CAMEL Application Part). Při sestavení hovoru nebo relace SSF pod správou SSME monitoruje specifické spouštěcí události definované v CAMEL Subscription Information ([CSI](/mobilnisite/slovnik/csi/)) účastníka. Po detekci spouštěče SSME sestaví zprávu CAP InitialDP a odešle ji příslušné SCF. SCF poté vrátí CAP instrukce (např. ApplyCharging, Connect, Continue), které SSME interpretuje a vynutí na SSF za účelem řízení směrování hovoru, účtování a dalších služebních funkcí. Tímto je aplikační logika oddělena od základního zpracování hovoru, což umožňuje flexibilní nasazení služeb.

SSME spravuje klíčové zdroje a stavy spojené s CAMEL dialogy. Je zodpovědná za udržování stavu CAMEL relace pro každý aktivní hovor, správu časovačů pro operace jako je kontrola účtování a řešení chybových stavů. Její role zajišťuje, že síť může konzistentně a spolehlivě poskytovat pokročilé, operátorské služby, a to i pro účastníky roamující mimo domácí síť, díky standardizaci interakce mezi přepínací a řídicí vrstvou. Specifikace, zejména TS 23.078 a TS 29.078, podrobně popisují její procedury a využívaný protokol CAP.

## K čemu slouží

SSME byla zavedena za účelem poskytnutí standardizovaného, spravovatelného rozhraní pro funkci přepínání služeb (SSF) v rámci rámce CAMEL. Před zavedením CAMEL byly pokročilé telefonní služby z velké části proprietární a vázané na konkrétní dodavatele ústředen, což operátorům ztěžovalo nasazení konzistentních služeb v celé síti, zejména pro roamující účastníky. Koncept Inteligentní sítě si kladl za cíl oddělit aplikační logiku od přepínacího hardwaru a SSME je realizací 3GPP pro správu SSF potřebnou k fungování tohoto konceptu v sítích GSM a UMTS.

Její zavedení vyřešilo problém, jak spolehlivě spouštět a provádět externí aplikační logiku během základního řízení hovoru. Definováním specializované řídicí entity zajistila 3GPP, že služby CAMEL jako předplacené, bezplatná čísla nebo virtuální privátní sítě mohou být vyvolány standardizovaným způsobem. SSME abstrahuje složitost podkladové ústředny a poskytuje SCF jednotné CAP rozhraní. To umožňuje vývojářům aplikační logiky a síťovým operátorům soustředit se na tvorbu služeb bez nutnosti znát specifika implementace každého dodavatele MSC, což podporuje inovace a interoperabilitu v nabídce mobilních služeb.

## Klíčové vlastnosti

- Spravuje spouštění detekčních bodů (DP) a zpracování událostí v rámci SSF
- Slouží jako protokolový koncový bod pro CAMEL Application Part (CAP) dialog se SCF
- Interpretuje a provádí instrukce řízení služeb (např. Connect, ApplyCharging) od SCF
- Udržuje stav a časovače pro aktivní relace služeb CAMEL
- Zpracovává obnovu po chybě a záložní procedury pro interakce CAMEL
- Podporuje více fází CAMEL a scénářů služeb (např. řízení MO, MT, SMS)

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [SSF – Service Switching Function](/mobilnisite/slovnik/ssf/)
- [SCF – Service Control Function (IN context), Service Capability Feature (VHE/OSA context)](/mobilnisite/slovnik/scf/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4

---

📖 **Anglický originál a plná specifikace:** [SSME na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssme/)
