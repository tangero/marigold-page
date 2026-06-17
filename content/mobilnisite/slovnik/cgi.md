---
slug: "cgi"
url: "/mobilnisite/slovnik/cgi/"
type: "slovnik"
title: "CGI – Cell Global Identifier"
date: 2025-01-01
abbr: "CGI"
fullName: "Cell Global Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cgi/"
summary: "Cell Global Identifier (CGI) je globálně jednoznačný identifikátor buňky v mobilní síti, vytvořený kombinací Mobile Country Code (MCC), Mobile Network Code (MNC), Location Area Code (LAC) a Cell Ident"
---

CGI je globálně jednoznačný identifikátor buňky mobilní sítě, vytvořený kombinací MCC, MNC, LAC a Cell Identity, který umožňuje její přesnou identifikaci a směrování v rámci celé sítě.

## Popis

Cell Global Identifier (CGI) je základní adresovací prvek v mobilních sítích 3GPP, který poskytuje globálně jednoznačný štítek pro každou buňku. Jeho primární funkcí je jednoznačně odlišit jednu buňku od všech ostatních na světě, což je klíčový požadavek pro směrování hovorů, správu předávání (handover), sledování polohy účastníka a různé úkony provozu a údržby sítě. CGI není samostatné číslo, ale strukturovaná konkatenace několika existujících identifikátorů definovaných v architektuře PLMN (Public Land Mobile Network). Tato hierarchická konstrukce zajišťuje globální jednoznačnost prostřednictvím kombinace identifikátorů země, sítě, regionu a lokálního identifikátoru.

Struktura CGI je definována jako: CGI = [MCC](/mobilnisite/slovnik/mcc/) + [MNC](/mobilnisite/slovnik/mnc/) + [LAC](/mobilnisite/slovnik/lac/) + [CI](/mobilnisite/slovnik/ci/). Mobile Country Code (MCC) je tříciferný kód (např. 234 pro UK) definovaný [ITU](/mobilnisite/slovnik/itu/). Mobile Network Code (MNC) je dvou- nebo tříciferný kód identifikující konkrétního síťového operátora v dané zemi (např. 30 pro [EE](/mobilnisite/slovnik/ee/) UK). Společně MCC a MNC tvoří PLMN ID, které jednoznačně identifikuje síť operátora. Location Area Code (LAC) je kód pevné délky (obvykle 16 bitů) přiřazený síťovým operátorem k identifikaci lokální oblasti, což je skupina buněk používaná pro paging a aktualizaci polohy. Nakonec Cell Identity (CI) je kód pevné délky (obvykle 16 bitů) přiřazený operátorem k jednoznačné identifikaci buňky v rámci dané lokální oblasti.

Z architektonického pohledu CGI využívá více síťových elementů. V rádiové přístupové síti (RAN) základnová stanice (Node B, eNodeB, gNB) vysílá své CGI (nebo jeho složky) na broadcast kanálu ([BCCH](/mobilnisite/slovnik/bcch/)), aby jejím User Equipment (UE) mohlo identifikovat obsluhující buňku. UE hlásí CGI sousedních buněk v měřicích hlášeních, která síť využívá pro rozhodování o předání. V jádře sítě je CGI klíčové pro Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE nebo pro Access and Mobility Management Function (AMF) v 5GC ke sledování přesné polohy UE pro paging a správu relací. Je také klíčovým parametrem v Gateway Mobile Location Center (GMLC) pro tísňové služby a komerční služby založené na poloze a je povinným polem pro rozhraní zákonného odposlechu.

Provozně CGI umožňuje všechny mobilní procedury. Během předání zdrojová buňka zahrnuje CGI cílové buňky do zprávy žádosti o předání, aby jednoznačně identifikovala cíl. Pro služby polohy může být žádost obsahující identifikátor účastníka přeložena sítí na poslední známé CGI, což poskytne hrubou lokalizaci. V systémech správy sítě jsou výkonnostní metriky (např. míra zrušení hovorů, vytížení) sbírány a hlášeny na úrovni CGI, což operátorům umožňuje monitorovat a optimalizovat výkon sítě na úrovni jednotlivých buněk. Jeho globální jednoznačnost zabraňuje jakékoli nejednoznačnosti při integraci sítí různých operátorů nebo během mezinárodního roamingu, což zajišťuje plynulou kontinuitu služeb a přesné účtování.

## K čemu slouží

Cell Global Identifier byl vytvořen k řešení zásadního problému jednoznačné identifikace konkrétní rádiové buňky kdekoli na světě v rámci globálního mobilního telekomunikačního systému. Před standardizovaným globálním adresováním mohly sítě používat proprietární nebo nejednoznačné identifikátory buněk, což způsobovalo konflikty při roamingu, předávání mezi operátory a integraci sítí. Tento nedostatek univerzálního schématu by bránil mobilitě, komplikoval izolaci chyb a činil celostátní nebo globální správu sítě a poskytování služeb téměř nemožným. CGI poskytuje tuto nezbytnou univerzální adresovací vrstvu.

Primární motivací byla podpora pokročilé mobility a správy sítě v digitálních celulárních sítích, jako je GSM (kde byl poprvé standardizován), a jeho nástupcích. Jak sítě rostly a stávaly se složitějšími a jak se roaming mezi operátory a zeměmi stal standardním požadavkem služby, strukturovaný, hierarchický identifikátor se stal nezbytným. CGI umožňuje síti přesně směrovat hovory a datové relace, spravovat předávání mezi buňkami (i těmi od různých dodavatelů nebo v některých případech různých operátorů) a přesně zaznamenávat události pro účtování, zabezpečení a analýzu výkonu. Je základním kamenem pro služby založené na poloze, protože poskytuje síti známou polohu účastníka.

CGI dále řeší regulatorní a provozní požadavky. Pro tísňové služby (např. E-911 v USA) musí síť poskytnout polohu volajícího. CGI slouží jako klíčová informace o poloze, kterou lze přeložit do geografické oblasti. Pro zákonné odposlechy požadují orgány záznamy a odposlechy spojené s konkrétní lokalitou, což je umožněno označováním dat pomocí CGI. Jeho návrh také zjednodušuje plánování a rozšiřování sítě, protože operátoři mohou spravovat Cell Identity v rámci svých přiřazených Location Areas a PLMN bez rizika globální kolize, což zajišťuje škálovatelný a budoucím vývojem chráněný růst sítě.

## Klíčové vlastnosti

- Globálně jednoznačná identifikace buňky prostřednictvím hierarchické konkatenace MCC, MNC, LAC a CI
- Základní prvek umožňující mobilní procedury včetně předání (handover), převýběru buňky a aktualizace lokální oblasti
- Kritický parametr pro služby založené na poloze (LBS) a lokalizaci tísňových volání
- Povinný identifikátor pro správu sítě, monitorování výkonu a hlášení chyb na úrovni buňky
- Nezbytné pole pro zákonné odposlechy a záznamy podrobností o hovorech (CDR) pro zabezpečení a účtování
- Vysílán buňkou a hlásán UE, tvoří základ pro správu rádiových zdrojů

## Související pojmy

- [ECGI – E-UTRAN Cell Global Identification](/mobilnisite/slovnik/ecgi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.031** (Rel-19) — Fraud Information Gathering System (FIGS) Stage 1
- **TS 23.031** (Rel-19) — Fraud Information Gathering System (FIGS) - Stage 2
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.709** (Rel-15) — Simplified HS-SCCH for UMTS Study
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.849** (Rel-12) — MBMS Operation on Demand (MooD)
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [CGI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cgi/)
