---
slug: "adp"
url: "/mobilnisite/slovnik/adp/"
type: "slovnik"
title: "ADP – Associated Delivery Procedures"
date: 2025-01-01
abbr: "ADP"
fullName: "Associated Delivery Procedures"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/adp/"
summary: "Associated Delivery Procedures (ADP) jsou soubor standardizovaných mechanismů v sítích 3GPP pro spolehlivé a koordinované doručování multimediálního obsahu, jako jsou multimediální zprávy, k uživatels"
---

ADP je soubor standardizovaných mechanismů 3GPP pro spolehlivé a řízené doručování multimediálního obsahu (např. MMS) k uživatelskému zařízení, zajišťující koordinované chování služby napříč sítěmi.

## Popis

Associated Delivery Procedures (ADP) tvoří rámec v rámci architektury služeb 3GPP, primárně definovaný v Technických specifikacích pro službu Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)) a souvisejících služebních prvcích. Tyto procedury řídí, jak je multimediální obsah, především multimediální zprávy, doručován ze služební platformy (jako je MMSC – Multimedia Messaging Service Centre) k uživatelskému zařízení (UE) a v některých případech mezi síťovými elementy. ADP není jediným protokolem, ale souborem logických procedur a interakcí, které zajišťují, že doručování je spolehlivě a efektivně z hlediska sítě pokusováno, řízeno a hlášeno.

Architektonicky ADP funguje ve vrstvě služeb, rozhraní se základními síťovými elementy, jako je [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre) nebo [SGSN](/mobilnisite/slovnik/sgsn/)/[MME](/mobilnisite/slovnik/mme/) (Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node / Mobility Management Entity) pro správu mobility a relací, a [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) pro data účastníka. Klíčovou komponentou iniciující ADP je typicky MMSC nebo jiný aplikační server. Procedury definují sekvenci signalizačních zpráv, zpracování hlášení o doručení, hlášení o přečtení a správu vypršení platnosti zprávy a pokusů o opakované doručení. Specifikují, jak se má síť chovat, když je UE nedostupné (např. mimo pokrytí), včetně mechanismů uložení a následného odeslání.

Z funkční perspektivy ADP funguje tak, že vytváří kontext pro pokus o doručení. Když je zpráva předána k doručení, procedury určují, jak je určena obsluhující síť, jak je vyhodnocena dosažitelnost UE (např. připojené, nečinné, zaneprázdněné) a jak je obsah pushován nebo je k UE odeslána notifikace pro stažení zprávy. Kritickým aspektem je přidružení doručení k jiným procedurám; například doručení může být odloženo, dokud není signalizační spojení navázáno pro jiný účel, nebo může být spuštěno konkrétní síťovou událostí. Procedury také definují zpracování chyb, zajišťující, že selhání jsou zaznamenána a případně hlášena zpět odesílateli.

Její role v síti spočívá v poskytování standardizovaného, provozovatelsky robustního mechanismu pro doručování obsahu v reálném čase. Tím, že je 'přidružená', implikuje úroveň inteligence a koordinace přesahující jednoduché uložení a odeslání. Tato koordinace pomáhá optimalizovat využití síťových prostředků využitím stávajících signalizačních spojení tam, kde je to možné, a poskytuje konzistentní uživatelský zážitek pro služby zasílání zpráv. Tvoří páteř spolehlivostních funkcí pro MMS, zajišťující, že zprávy nejsou potichu ztraceny a že uživatelé i poskytovatelé služeb obdrží potvrzení o výsledku doručení.

## K čemu slouží

ADP bylo vytvořeno k řešení problému nespolehlivého a neinteroperabilního doručování multimediálního obsahu v raných mobilních datových službách. Před jeho standardizací v 3GPP Release 5 vedly proprietární mechanismy pro doručování obrázkových zpráv a dalšího bohatého obsahu k fragmentovanému uživatelskému zážitku a omezenému přijetí služeb mezi různými operátory a výrobci zařízení. Nedostatek společných postupů ztěžoval spolehlivou implementaci služeb [MMS](/mobilnisite/slovnik/mms/) a dalších přidaných služeb mezi operátory.

Primární motivací bylo umožnit službu Multimedia Messaging Service (MMS) jako úspěšnou, všudypřítomnou službu. MMS vyžadovala složitější mechanismus doručování než [SMS](/mobilnisite/slovnik/sms/) kvůli větší velikosti zpráv, potřebě navázání datového přenosu a zpracování různých možností zařízení. ADP poskytlo potřebný procedurální rámec pro správu této složitosti, zajišťující, že zprávy mohou být doručeny i přes mobilitu uživatele, dočasnou nedostupnost sítě a různé stavy terminálu. Řešilo omezení, jako jsou nekoordinované pokusy o doručení plýtvající síťovými prostředky, a absenci standardizovaných hlášení o doručení/přečtení pro multimediální obsah.

Historicky bylo zavedení ADP v Release 5 součástí širšího úsilí o paketově přepínané multimediální služby v sítích 3G. Stanovilo základní model pro přidružené doručování, kde je přenos zprávy inteligentně propojen s dalšími síťovými aktivitami. Tím bylo vyřešeno, jak efektivně doručovat obsah bez nutnosti, aby bylo UE trvale aktivní na datovém přenosu, čímž se zlepšila výdrž baterie a efektivita sítě při zaručení spolehlivosti služby.

## Klíčové vlastnosti

- Standardizované procedury doručování a hlášení pro multimediální obsah
- Koordinace se stavy mobility UE a správy relací
- Podpora mechanismů uložení a následného odeslání pro nedostupné příjemce
- Definice hlášení o doručení a hlášení o přečtení
- Přidružení doručování obsahu k jiným síťovým signalizačním událostem
- Zpracování chyb a logika opakování pro neúspěšné pokusy o doručení

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TR 26.989** (Rel-19) — MCPTT Enhancement Analysis

---

📖 **Anglický originál a plná specifikace:** [ADP na 3GPP Explorer](https://3gpp-explorer.com/glossary/adp/)
