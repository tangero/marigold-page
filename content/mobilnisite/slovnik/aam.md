---
slug: "aam"
url: "/mobilnisite/slovnik/aam/"
type: "slovnik"
title: "AAM – Advanced Alarming Management"
date: 2026-01-01
abbr: "AAM"
fullName: "Advanced Alarming Management"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/aam/"
summary: "Advanced Alarming Management (AAM) je rámec 3GPP pro sběr, korelaci a inteligentní zpracování síťových alarmů. Vylepšuje správu poruch snížením záplav alarmů, identifikací hlavních příčin a poskytnutí"
---

AAM je rámec 3GPP pro sběr, korelaci a inteligentní zpracování síťových alarmů za účelem vylepšení správy poruch snížením záplav alarmů a identifikací hlavních příčin.

## Popis

Advanced Alarming Management (AAM) je komplexní rámec definovaný v rámci 3GPP pro správu životního cyklu síťových alarmů. Funguje jako klíčová součást systému Operations, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)), konkrétně v oblasti Fault Management ([FM](/mobilnisite/slovnik/fm/)). Architektura typicky zahrnuje Alarm Producers (síťové elementy jako [eNB](/mobilnisite/slovnik/enb/), [MME](/mobilnisite/slovnik/mme/) nebo [S-GW](/mobilnisite/slovnik/s-gw/)), Alarm Consumers (jako Network Management Systems nebo Element Managers) a samotné funkce AAM, které mohou být centralizované nebo distribuované. Systém AAM přijímá surová alarmová hlášení od různých síťových elementů, která jsou často početná a redundantní při výskytu poruchy.

Jádro funkcionality AAM spočívá v jeho pokročilých zpracovatelských schopnostech. Provádí korelaci alarmů, jejich filtrování a obohacování. Korelační algoritmy analyzují příchozí alarmy na základě časových, prostorových a logických vztahů, aby identifikovaly jedinou hlavní příčinu z mnoha symptomatických alarmů, čímž účinně potlačují 'alarmovou bouři'. Filtrování odstraňuje duplicitní nebo nevýznamné alarmy na základě konfigurovatelných pravidel. Obohacování přidává k alarmům kontextové informace, jako je ovlivněná služba nebo dopad na zákazníka, pomocí křížového odkazování na další data správy, například z Configuration Management ([CM](/mobilnisite/slovnik/cm/)) nebo Performance Management ([PM](/mobilnisite/slovnik/pm/)).

AAM také definuje standardizovaná alarmová rozhraní a informační modely, jako jsou ty ve specifikacích řady 32.12x, což zajišťuje interoperabilitu mezi síťovými elementy a systémy správy od různých dodavatelů. Podporuje stavovou správu alarmů, sleduje životní cyklus alarmu od stavu 'vyvolán' až po 'zrušen'. Dále AAM usnadňuje automatizované nebo poloautomatizované nápravné akce tím, že poskytuje dobře strukturované, korelované informace o poruchách vyšším orchestrátorům nebo systémům assurance. Tím transformuje surová, chaotická data událostí na strukturované, smysluplné informace o poruchách, na které mohou síťoví operátoři reagovat.

V praxi je AAM nedílnou součástí dosažení vysoké dostupnosti sítě a efektivních operací. Inteligentním zpracováním alarmů výrazně snižuje Mean Time To Repair (MTTR) a provozní zátěž personálu Network Operations Center (NOC). Jeho role se stává stále důležitější s rostoucí komplexitou sítí při zavádění 5G, síťových řezů a cloud-nativních architektur, kde domény poruch zasahují napříč fyzickou infrastrukturou, virtualizovanými síťovými funkcemi a softwarovými vrstvami.

## K čemu slouží

AAM byl zaveden, aby řešil kritickou provozní výzvu přetížení alarmy v stále složitějších a automatizovanějších telekomunikačních sítích. Před jeho standardizací byly systémy správy sítě často zaplaveny záplavou surových, nekorelovaných alarmů od jednotlivých síťových elementů při výpadku. Tato 'alarmová bouře' ztěžovala operátorům rychlou identifikaci hlavní příčiny problému, což vedlo k prodlouženým výpadkům služeb, zvýšeným provozním nákladům a vysokému riziku lidské chyby v diagnostickém procesu. Primární motivací byl přechod od reaktivního, na element zaměřeného přístupu správy poruch k proaktivnímu přístupu zaměřenému na službu.

Vytvoření AAM v 3GPP Release 8 bylo součástí širšího úsilí o vylepšení [OAM](/mobilnisite/slovnik/oam/) schopností pro nový Evolved Packet System (EPS). Jak se sítě vyvíjely směrem k plně IP, plochým architekturám, potřeba inteligentní, centralizované správy poruch se stala prvořadou. AAM poskytl standardizovaný rámec, který umožnil agregaci a inteligentní analýzu dat o poruchách napříč celou sítí, namísto v izolovaných silách. Vyřešil problém informačního přetížení aplikací korelačních technik pro potlačení redundantních alarmů a zvýraznění základního problému.

Dále AAM umožnil efektivnější automatizaci. Dodáváním jasných, korelovaných a obohacených informací o poruchách vytvořil spolehlivý základ pro automatizovanou analýzu hlavních příčin a následně pro uzavřené smyčky operací pro samoléčící sítě. To bylo zásadní pro škálování síťových operací potřebných ke správě obrovského počtu elementů v sítích 4G a budoucích sítích 5G, což zlepšilo jak spolehlivost služeb, tak provozní výdaje (OPEX).

## Klíčové vlastnosti

- Standardizovaný alarmový informační model a rozhraní pro interoperabilitu mezi více dodavateli
- Pokročilá korelace alarmů pro identifikaci hlavních příčin a potlačení symptomatických alarmů
- Stavová správa životního cyklu alarmů (např. vyvolán, potvrzen, zrušen)
- Filtrování alarmů a detekce duplicit pro snížení informačního přetížení
- Obohacování alarmů kontextovými daty z CM a PM
- Podpora automatizované diagnostiky poruch a integrace s orchestrace systémy

## Definující specifikace

- **TR 22.843** (Rel-19) — Study on Uncrewed Aerial Vehicle (UAV) Phase 3
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 32.122** (Rel-19) — Advanced Alarm Management IRP Information Service
- **TS 32.123** (Rel-9) — Advanced Alarm Management IRP CORBA Solution Set
- **TS 32.125** (Rel-9) — AAM IRP XML File Format Definition
- **TS 32.126** (Rel-19) — AAM IRP Solution Set Definitions
- **TS 32.127** (Rel-9) — AAM IRP SOAP Solution Set
- **TS 32.832** (Rel-10) — Alarm Correlation and Root Cause Analysis Study

---

📖 **Anglický originál a plná specifikace:** [AAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/aam/)
