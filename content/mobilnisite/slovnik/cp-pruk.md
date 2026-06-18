---
slug: "cp-pruk"
url: "/mobilnisite/slovnik/cp-pruk/"
type: "slovnik"
title: "CP-PRUK – Control Plane Prose Remote User Key"
date: 2025-01-01
abbr: "CP-PRUK"
fullName: "Control Plane Prose Remote User Key"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cp-pruk/"
summary: "Bezpečnostní klíč používaný pro přímou komunikaci typu ProSe (Proximity Services) mezi UEs, řízený přes řídicí rovinu. Umožňuje zabezpečenou komunikaci zařízení zařízení bez směrování veškerého provoz"
---

CP-PRUK je bezpečnostní klíč řízený řídicí rovinou, používaný pro přímou komunikaci zařízení zařízení (D2D) typu ProSe, který umožňuje zabezpečená spojení bez směrování veškerého provozu přes síťové jádro.

## Popis

Control Plane [Prose](/mobilnisite/slovnik/prose/) Remote User Key (CP-PRUK) je kryptografický klíč vytvořený mezi dvěma uživatelskými zařízeními (UEs) pro zabezpečení jejich přímého komunikačního spoje ProSe. Je generován a řízen signalizačními procedurami v řídicí rovině 5G Core Networku, konkrétně za účasti ProSe Function. Odvození klíče následuje rámec 5G Authentication and Key Agreement (5G-AKA), což zajišťuje jeho kryptografickou oddělenost od jiných klíčů používaných pro přístup k síti (jako K_[AMF](/mobilnisite/slovnik/amf/)) nebo ochranu uživatelské roviny. CP-PRUK je kritickou součástí bezpečnostní architektury ProSe, poskytující ochranu důvěrnosti a integrity pro přímý komunikační kanál mezi UEs.

Architektura pro CP-PRUK zahrnuje několik síťových funkcí. ProSe Function, umístěná v domovské veřejné pozemní mobilní síti ([HPLMN](/mobilnisite/slovnik/hplmn/)) UE, je centrální entita zodpovědná za autorizaci služby ProSe a správu bezpečnosti. Když dvě UEs (UE-A a UE-B) chtějí navázat zabezpečený přímý spoj, zahájí proceduru přímého objevování nebo komunikace ProSe. Jejich požadavky jsou směrovány k jejich příslušným ProSe Functions. Tyto funkce UEs autentizují a autorizují službu ProSe. Pro navázání klíče spolu ProSe Functions komunikují, často přes referenční bod rozhraní PC5, aby se dohodly na klíčovém materiálu. Samotný CP-PRUK je následně lokálně odvozen v každém UE pomocí parametrů poskytnutých jeho ProSe Function, jako je identifikátor klíče ProSe a další nové vstupní hodnoty.

Technická operace zahrnuje hierarchii odvození klíče v několika krocích. Nejprve je mezi UE a jeho HPLMN ProSe Function během autorizace služby vytvořen kořenový klíč, ProSe Key (PK). Z tohoto PK může být pro konkrétní komunikační pár odvozen ProSe Link Key (PLK). CP-PRUK je dalším derivátem, často sloužícím jako klíč pro zabezpečení přístupové vrstvy ([AS](/mobilnisite/slovnik/as/)) mezi dvěma UEs přes rozhraní PC5. Tento vrstvený přístup zajišťuje separaci klíčů; kompromitace CP-PRUK pro jeden přímý spoj neovlivní bezpečnost síťového přístupu UE ani jeho ProSe spojů s jinými zařízeními. CP-PRUK je používán vrstvou [PDCP](/mobilnisite/slovnik/pdcp/) (Packet Data Convergence Protocol) v UE k šifrování a zajištění integrity dat uživatelské roviny a určité signalizace řídicí roviny přenášené přímo přes PC5.

Jeho role v síti spočívá v umožnění důvěryhodné a efektivní komunikace zařízení zařízení ([D2D](/mobilnisite/slovnik/d2d/)). Tím, že správa klíčů probíhá v řídicí rovině, si síť udržuje dohled a kontrolu politik nad přímou komunikací, což je zásadní pro zákonné odposlechy, služby tísňového volání a prevenci neoprávněného použití. Mechanismus CP-PRUK umožňuje síti poskytovat zabezpečení pro přímé spoje bez nutnosti směrovat samotný datový provoz uživatele, čímž optimalizuje latenci a využití síťových zdrojů pro aplikace založené na blízkosti.

## K čemu slouží

CP-PRUK byl vytvořen k řešení bezpečnostních požadavků služeb Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) zavedených a vylepšených v 5G, zejména pro komunikace kritické z hlediska mise a pokročilé scénáře [V2X](/mobilnisite/slovnik/v2x/) (Vehicle-to-Everything). Před jeho specifikací měla přímá D2D komunikace v LTE (pod názvem ProSe nebo LTE Direct) své bezpečnostní mechanismy, ale systém 5G vyžadoval robustnější, flexibilnější a škálovatelnější bezpečnostní architekturu integrovanou s novým 5G jádrem. Účelem CP-PRUK je poskytnout standardizovanou, sítí asistovanou metodu pro navazování zabezpečených přímých spojů mezi UEs, která zajišťuje, že tyto spoje jsou stejně důvěryhodné jako tradiční spojení směrovaná přes síť.

Klíčový problém, který řeší, je, jak efektivně inicializovat a spravovat zabezpečení mezi dvěma zařízeními, která spolu předtím nemusela mít žádný vztah, bez nutnosti složité výměny klíčů mimo pásmo. V situacích veřejné bezpečnosti (např. když je buněčná síťová infrastruktura poškozena) potřebují záchranáři komunikovat přímo. CP-PRUK umožňuje jejich zařízením navazovat šifrované kanály chráněné integritou, s klíči nakonec odvozenými z jejich přihlašovacích údajů k domovské síti. Tím se řeší omezení ad-hoc bezpečnostních nastavení, která jsou zranitelná vůči útoku typu man-in-the-middle. Dále pro komerční V2X umožňuje zabezpečená varování mezi vozidly bez nutnosti spoléhat se na nepřetržitou komunikaci s vysokou latencí se vzdáleným síťovým serverem.

Historický kontext ukazuje vývoj od jednoduššího, méně integrovaného D2D zabezpečení v LTE Release 12/13 směrem k sofistikovanější, službami založené architektuře v 5G. CP-PRUK, zavedený v 5G Release 17, je součástí této evoluce, navržený tak, aby bezproblémově spolupracoval s 5G Service-Based Architecture (SBA) a poskytoval vylepšené možnosti správy klíčů. Řeší omezení předchozích přístupů tím, že nabízí lepší separaci klíčů, integraci s 5G-AKA a podporu dynamičtějších a granularnějších bezpečnostních politik řízených ProSe Function sítě.

## Klíčové vlastnosti

- Umožňuje síťově řízené vytváření zabezpečených klíčů pro přímou (PC5) komunikaci UE-UE
- Odvozen z kořenového ProSe Key (PK) spravovaného ProSe Function domovské sítě
- Poskytuje ochranu důvěrnosti a integrity pro data uživatelské roviny a řídicí roviny na rozhraní PC5
- Zajišťuje separaci klíčů od bezpečnostních klíčů přístupové sítě (např. K_AMF) a od jiných ProSe spojů
- Podporuje jak režim přímé komunikace ProSe typu jeden-jeden, tak jeden-mnoho
- Integruje se s bezpečnostním rámcem 5G Authentication and Key Agreement (5G-AKA)

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G

---

📖 **Anglický originál a plná specifikace:** [CP-PRUK na 3GPP Explorer](https://3gpp-explorer.com/glossary/cp-pruk/)
