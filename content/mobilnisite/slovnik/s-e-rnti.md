---
slug: "s-e-rnti"
url: "/mobilnisite/slovnik/s-e-rnti/"
type: "slovnik"
title: "S-E-RNTI – Secondary Enhanced Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "S-E-RNTI"
fullName: "Secondary Enhanced Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/s-e-rnti/"
summary: "Sekundární dočasný identifikátor používaný v UMTS/HSPA k rozlišení vylepšených uplinkových prostředků konkrétního UE během komunikační relace. Používá se spolu s primárním E-RNTI pro scénáře, jako je"
---

S-E-RNTI je sekundární dočasný identifikátor používaný v UMTS/HSPA k rozlišení vylepšených uplinkových prostředků konkrétního UE. Používá se spolu s primárním E-RNTI pro scénáře, jako je změna obslužné buňky.

## Popis

S-E-RNTI (Secondary Enhanced Radio Network Temporary Identifier) je síťově přidělený dočasný identifikátor používaný v rádiové přístupové síti UMTS ([UTRAN](/mobilnisite/slovnik/utran/)) pro funkci Enhanced Uplink ([E-DCH](/mobilnisite/slovnik/e-dch/)). Funguje na vrstvě [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control), konkrétně v podsložkách MAC-e a MAC-es v Node B a [RNC](/mobilnisite/slovnik/rnc/). [E-RNTI](/mobilnisite/slovnik/e-rnti/) je 16bitová nebo 32bitová hodnota, která jednoznačně identifikuje kontext E-DCH UE v rámci buňky. S-E-RNTI je sekundární instance tohoto identifikátoru, zavedená pro řešení specifických procedurálních scénářů, kde je jednoznačná identifikace klíčová.

Z architektonického hlediska, když je UE nakonfigurováno pro provoz E-DCH, obslužný radiový síťový kontrolér ([SRNC](/mobilnisite/slovnik/srnc/)) mu přidělí primární E-RNTI. Tento primární identifikátor se používá pro veškeré plánování a řídicí zprávy související s uplinkem UE v obslužné buňce E-DCH. S-E-RNTI se uplatňuje během konkrétních událostí mobility nebo změn konfigurace. Nejtypičtějším scénářem je aktualizace obslužné sady rádiových spojů E-DCH ([RLS](/mobilnisite/slovnik/rls/)) nebo procedura změny obslužné buňky. Aby se předešlo nejednoznačnosti a zajistil plynulý přenos kontextu E-DCH, může síť před provedením změny předkonfigurovat UE pomocí S-E-RNTI pro cílovou buňku.

Jeho fungování je procedurální. Síť signalizuje S-E-RNTI směrem k UE prostřednictvím [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control) zpráv, například zprávy PHYSICAL CHANNEL RECONFIGURATION. UE si tento identifikátor uloží. Když je vydán příkaz ke změně obslužné buňky, UE začne používat předkonfigurované S-E-RNTI jako svůj primární identifikátor v nové buňce. Tím se zabrání kolizím, kdy by se dvě UE mohly během přechodu dočasně pokoušet použít stejný identifikátor. S-E-RNTI se používá v hlavičkách protokolových datových jednotek MAC-e a je klíčové pro to, aby Node B správně přiřadilo příchozí uplinková data ke správnému kontextu UE, zejména když může být primární E-RNTI právě přidělováno znovu. Jeho použití zajišťuje integritu procesů HARQ a plánovacích povolení během předávání spojení.

Jeho role spočívá v robustnosti a spolehlivosti správy mobility v HSPA. Poskytnutím sekundárního, vyhrazeného identifikátoru pro přechodné stavy eliminuje potenciální místo selhání (konflikt identifikátorů), které by mohlo vést ke ztrátě dat nebo zablokování protokolu. To činí službu E-DCH, která je navržena pro paketová data s nízkou latencí a vysokou spolehlivostí, odolnější během jedné z jejích nejzranitelnějších fází: předávání spojení mezi buňkami.

## K čemu slouží

Samotný mechanismus E-RNTI byl vytvořen spolu s E-DCH v Rel-5/6, aby umožnil rychlé plánování řízené Node B. Node B potřebuje krátký, na buňku specifický identifikátor, aby mohl adresovat plánovací povolení (na E-AGCH) a potvrzení (na E-HICH) konkrétnímu UE. Primární E-RNTI tuto funkci plní ve stabilním stavu. Původní návrh však narážel na problém během změn obslužné buňky.

Během aktivní relace E-DCH vyžaduje změna obslužné buňky přenos kontextu UE (včetně stavů vyrovnávací paměti HARQ, plánovacích parametrů) ze starého Node B do nového. Pokud by UE prostě přešlo na používání nového primárního E-RNTI přiděleného novou buňkou, mohlo by dojít k období, kdy by zprávy od UE (používající nové ID) nebyly Node B správně rozpoznány, pokud by jeho nastavení kontextu bylo opožděno. Naopak, pokud by stará a nová buňka používaly stejnou hodnotu E-RNTI pro různá UE, mohl by nastat konflikt. S-E-RNTI bylo zavedeno, aby tento identifikační problém během přechodu při předání spojení vyřešilo.

Poskytuje mechanismus čistého navázání spojení. Síť připraví cílovou buňku rezervací S-E-RNTI pro příchozí UE. UE je instruováno, aby tento S-E-RNTI použilo okamžitě po přístupu do nové buňky. To zaručuje, že první přenosy v nové buňce jsou jednoznačně identifikovatelné, což umožňuje Node B správně je spojit s předem připraveným kontextem. Tím se řeší omezení jediného, statického identifikátoru během dynamické rekonfigurace, což zvyšuje spolehlivost a úspěšnost změn obslužné buňky HSPA, což je nezbytné pro udržení QoS pro služby uplinku v reálném čase.

## Klíčové vlastnosti

- Dočasný 16bitový nebo 32bitový identifikátor pro kontext E-DCH UE
- Používá se jako sekundární identifikátor spolu s primárním E-RNTI
- Klíčový pro robustní procedury změny obslužné buňky E-DCH
- Předkonfigurován RNC a signalizován směrem k UE přes RRC
- Zabraňuje konfliktům identifikátorů během událostí mobility
- Zajišťuje správnou identifikaci MAC-e PDU v cílovém Node B

## Související pojmy

- [E-RNTI – E-DCH Radio Network Temporary Identifier](/mobilnisite/slovnik/e-rnti/)
- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)

## Definující specifikace

- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding

---

📖 **Anglický originál a plná specifikace:** [S-E-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-e-rnti/)
