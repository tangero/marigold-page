---
slug: "rof"
url: "/mobilnisite/slovnik/rof/"
type: "slovnik"
title: "ROF – Resource Owner Function"
date: 2026-01-01
abbr: "ROF"
fullName: "Resource Owner Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rof/"
summary: "Funkce správy zavedená v 5G-Advanced pro zpracování vlastnictví a delegace prostředků při sdílení sítí a ve scénářích s více operátory. Funguje jako bod pro rozhodování o politikách a autorizuje využí"
---

ROF je funkce správy v 5G-Advanced, která zpracovává vlastnictví a delegaci prostředků a autorizuje další operátory k využívání síťových prostředků, jako je spektrum, ve scénářích sdílení.

## Popis

Funkce vlastníka prostředků (Resource Owner Function, ROF) je logická funkce definovaná ve specifikaci 3GPP Release 18 v rámci širší architektury pro vylepšené sdílení sítí a sítě jádra s více operátory. Jedná se o entitu pro řízení politik a autorizací, která reprezentuje vlastníka fyzického nebo virtuálního síťového prostředku. Tyto prostředky mohou zahrnovat rádiové spektrum, infrastrukturu rádiového přístupového sítě (RAN, jako jsou gNB) nebo dokonce konkrétní síťové řezy. ROF zpřístupňuje schopnosti a podmínky využití svých vlastněných prostředků a může udělit, upravit nebo odebrat práva k jejich využití jiným autorizovaným subjektům, známým jako Funkce uživatele prostředků (Resource User Function, RUF). Tato interakce se řídí politikami a smlouvami o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)).

Architektonicky je ROF součástí roviny správy a orchestrace, často spojené s modelem síťových prostředků (Network Resource Model, [NRM](/mobilnisite/slovnik/nrm/)) a rámcem správy služeb a orchestrace (Service Management and Orchestration, SMO). Rozhraní s RUF, typicky prostřednictvím standardizovaných [API](/mobilnisite/slovnik/api/) (jako jsou severozápadní API SMO), usnadňuje zjišťování, vyjednávání a pronájem prostředků. Klíčovou rolí ROF je činit autorizační rozhodnutí. Například ve scénáři neutrálního hostitele, kde vlastník budovy provozuje privátní 5G síť, by ROF tohoto vlastníka mohl autorizovat více mobilním síťovým operátorům ([MNO](/mobilnisite/slovnik/mno/)) k využití této RAN, přičemž systém správy každého MNO by fungoval jako RUF. ROF vynucuje politiky týkající se izolace prostředků, kvality služby a zabezpečení pro každého uživatele.

Jak to funguje, zahrnuje vícekrokový proces. Nejprve RUF zjistí dostupné prostředky dotazem na ROF nebo službu zjišťování. RUF poté odešle žádost o využití prostředku s uvedením požadavků. ROF tuto žádost vyhodnotí vůči svým interním politikám, SLA a aktuálnímu vytížení prostředků. Pokud je žádost autorizována, RUF prostředek pro RUF zřídí, což může zahrnovat konfiguraci RAN, přidělení spektra nebo aktivaci síťového řezu. ROF dále monitoruje využití z hlediska souladu a může spustit přehodnocení nebo ukončení na základě porušení politik nebo skončení smlouvy. Specifikace jako TS 23.222 (architektura pro sdílení sítí) a TS 33.122 (bezpečnostní aspekty) definují postupy a bezpečnostní požadavky pro tyto interakce, aby byla zajištěna bezpečná a auditovatelná autorizace.

## K čemu slouží

ROF byl vytvořen, aby řešil rostoucí složitost a poptávku po flexibilních modelech sdílení sítí v 5G a dalších generacích. Tradiční sdílení sítí (jako MORAN nebo [MOCN](/mobilnisite/slovnik/mocn/)) bylo relativně statické a vyžadovalo složité předem dohodnuté smlouvy mezi omezeným počtem operátorů. Vzestup neutrálních hostitelů, privátních sítí a scénářů dynamického sdílení spektra vyžadoval agilnější, automatizovaný a standardizovaný způsob správy vlastnictví prostředků a přístupových práv. ROF poskytuje standardizovanou logickou funkci, která umožňuje tyto dynamické trhy se síťovými prostředky.

Řeší problém provozních izolací a manuálních procesů v prostředích s více operátory. Díky jasnému rozhraní ROF-RUF mohou různé obchodní subjekty automaticky vyjednávat a využívat sdílenou infrastrukturu, čímž se snižují vstupní bariéry a podporuje se inovace. Například umožňuje autoritě letiště (ROF) dynamicky přidělit kapacitu své privátní sítě letecké společnosti (RUF) během špičky. Z bezpečnostního hlediska TS 33.122 definuje, jak zabezpečit tyto interakce delegace, aby se zabránilo neoprávněnému přístupu a zajistilo, že vlastník prostředků si udrží kontrolu. ROF je klíčovým prvkem pro obchodní modely 5G-Advanced, které překračují prostý roaming směrem k opravdovým paradigmatům prostředek-jako-sluzba.

## Klíčové vlastnosti

- Logický bod pro rozhodování o politikách pro autorizaci využití síťových prostředků
- Reprezentuje vlastníka fyzických/virtuálních prostředků (spektrum, RAN, řezy)
- Interaguje s Funkcí uživatele prostředků (RUF) prostřednictvím API pro správu
- Vynucuje obchodní politiky a SLA během delegace prostředků
- Podporuje dynamické zjišťování, vyjednávání a zřizování prostředků
- Základní prvek pro scénáře neutrálního hostování, více operátorů a sdílení sítí

## Související pojmy

- [NRM – Network Resource Model](/mobilnisite/slovnik/nrm/)

## Definující specifikace

- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 33.122** (Rel-19) — Security Architecture for CAPIF

---

📖 **Anglický originál a plná specifikace:** [ROF na 3GPP Explorer](https://3gpp-explorer.com/glossary/rof/)
