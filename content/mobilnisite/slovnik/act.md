---
slug: "act"
url: "/mobilnisite/slovnik/act/"
type: "slovnik"
title: "ACT – Application Context Transfer"
date: 2026-01-01
abbr: "ACT"
fullName: "Application Context Transfer"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/act/"
summary: "ACT je služba 3GPP umožňující bezproblémový přenos kontextu aplikační relace mezi uživatelskými zařízeními a síťovými funkcemi. Zachovává kontinuitu služby při přepínání uživatelů mezi zařízeními nebo"
---

ACT je služba 3GPP umožňující bezproblémový přenos kontextu aplikační relace mezi zařízeními a sítěmi za účelem zachování kontinuity služby při přepínání uživatelů mezi zařízeními nebo způsoby přístupu.

## Popis

Application Context Transfer (ACT) je standardizovaná služba v rámci architektur 3GPP, která usnadňuje přenos kontextových informací souvisejících s aplikací mezi různými entitami v síti. Služba funguje prostřednictvím centralizované funkce ACT, která spravuje operace ukládání, získávání a přenosu kontextu. Když je třeba přenést aplikační relaci (například když uživatel přepne ze smartphonu na tablet), funkce ACT koordinuje spolupráci se zdrojovým i cílovým zařízením a zajišťuje správnou migraci všech relevantních parametrů relace, uživatelských preferencí a dat stavu aplikace.

Architektura zahrnuje několik klíčových komponent: ACT Server Function (ACT-SF), která ukládá a spravuje kontextová data; ACT Client Function (ACT-CF) umístěná v uživatelském zařízení nebo aplikačních serverech, která iniciuje žádosti o přenos; a ACT Management Function (ACT-MF), která zajišťuje autentizaci, autorizaci a vynucování politik. Tyto komponenty komunikují prostřednictvím standardizovaných rozhraní definovaných ve specifikacích 3GPP, přičemž používají RESTful API a datové formáty založené na JSON pro reprezentaci kontextu. Systém využívá pro přenos dat zabezpečené protokoly a implementuje ochranné mechanismy pro ochranu citlivých uživatelských informací.

ACT funguje prostřednictvím vícefázového procesu: zachycení kontextu, kdy je aktuální stav aplikace serializován a uložen; zahájení přenosu kontextu, spuštěné uživatelskou akcí nebo síťovými podmínkami; získání kontextu, kdy cílové zařízení získá uložený kontext; a obnovení kontextu, kdy aplikace pokračuje v činnosti s přeneseným stavem. Služba podporuje jak režimy přenosu typu push, tak pull, přičemž ACT-SF funguje jako zprostředkovatel mezi zdrojovými a cílovými entitami. Kontextová data mohou zahrnovat identifikátory relací, uživatelské preference, pozice v přehrávání médií, data z formulářů, autentizační tokeny a parametry specifické pro aplikaci.

Služba se integruje se stávajícími systémy 3GPP prostřednictvím rozhraní s Policy Control Function (PCF), Unified Data Management (UDM) a Network Exposure Function (NEF). To umožňuje ACT využívat síťové schopnosti, jako je správa kvality služeb, uživatelská autentizace a autorizace služeb. Funkce ACT může být nasazena jako součást architektury založené na službách v jádrových sítích 5G nebo jako nezávislá síťová funkce v dřívějších vydáních. Hraje klíčovou roli při zajišťování bezproblémové kontinuity služeb napříč různými přístupovými technologiemi (5G, LTE, Wi-Fi) a typy zařízení a tvoří základ pro pokročilé zážitky s více zařízeními a mobilitu aplikací.

## K čemu slouží

ACT byla vytvořena, aby řešila rostoucí potřebu bezproblémové kontinuity aplikací, protože uživatelé stále častěji používají více zařízení a přepínají mezi různými přístupovými sítěmi. Před standardizací ACT museli vývojáři aplikací implementovat proprietární řešení pro přenos stavu, což vedlo k fragmentaci, bezpečnostním slabinám a špatným uživatelským zážitkům. Tyto ad-hoc přístupy často nedokázaly zachovat integritu relace během přechodů, což mělo za následek ztrátu dat, selhání autentizace a narušení služeb.

Technologie řeší několik klíčových problémů: za prvé odstraňuje potřebu, aby uživatelé při přepínání zařízení ručně restartovali aplikace nebo znovu zadávali data; za druhé umožňuje poskytovatelům služeb nabízet konzistentní zážitky napříč různými form-faktory zařízení; za třetí podporuje nové případy užití, jako je rozšířená realita (XR), kde je zachování stavu aplikace klíčové pro ponoření; a za čtvrté usnadňuje optimalizaci sítě tím, že umožňuje inteligentní vyrovnávání zátěže mezi zařízeními bez narušení uživatelských relací.

Historicky motivací pro ACT byla proliferace chytrých zařízení a rostoucí očekávání bezproblémových digitálních zážitků. Jak se sítě 3GPP vyvíjely směrem k architekturám založeným na službách v 5G, byla rozpoznána potřeba standardizovaných mechanismů pro podporu mobility aplikací. ACT poskytuje tuto standardizaci a zároveň řeší bezpečnostní obavy prostřednictvím správných mechanismů autentizace, autorizace a ochrany dat, které často chyběly v proprietárních řešeních.

## Klíčové vlastnosti

- Standardizované datové modely kontextu pro konzistentní reprezentaci stavu aplikace
- Zabezpečené přenosové protokoly s end-to-end šifrováním a ochranou integrity
- Podpora jak režimů přenosu typu push, tak pull mezi zařízeními
- Integrace s autentizačními a autorizačními frameworky 3GPP
- Řízení založené na politikách nad tím, jaký kontext lze přenést a na která zařízení
- Zpětná kompatibilita se staršími systémy prostřednictvím adaptačních vrstev

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [ACT na 3GPP Explorer](https://3gpp-explorer.com/glossary/act/)
