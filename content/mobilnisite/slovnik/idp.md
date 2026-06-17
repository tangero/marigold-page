---
slug: "idp"
url: "/mobilnisite/slovnik/idp/"
type: "slovnik"
title: "IDP – Initial Detection Point"
date: 2025-01-01
abbr: "IDP"
fullName: "Initial Detection Point"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/idp/"
summary: "Funkční entita v rámci architektury služby CAMEL (Customised Applications for Mobile network Enhanced Logic). Je to první bod v modelu volání/stavu, kde může být vyvolána služba CAMEL, což umožňuje sí"
---

IDP je první bod v modelu volání CAMEL, kde může síť vyvolat uživatelsky přizpůsobenou službu, například předplacené účtování.

## Popis

Initial Detection Point (IDP, Počáteční detekční bod) je základní součást architektury [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile network Enhanced Logic), což je standard 3GPP umožňující implementaci specifických, inteligentních síťových služeb ([IN](/mobilnisite/slovnik/in/)) v mobilních sítích. CAMEL umožňuje servisní logice, která často sídlí na vyhrazeném Service Control Point (SCP), interagovat s funkcemi řízení hovorů a relací v jádru sítě (jako je [MSC](/mobilnisite/slovnik/msc/) nebo [GMSC](/mobilnisite/slovnik/gmsc/)). IDP představuje konkrétní, předem definovanou událost nebo stav v hovoru či relaci (např. pokus o spojení, odeslání SMS, vytvoření [GPRS](/mobilnisite/slovnik/gprs/) relace), která spustí, že jádro sítě přeruší své běžné zpracování a vyžádá si instrukce od externí servisní logiky CAMEL.

Když účastník, jehož profil indikuje podporu CAMEL, zahájí aktivitu, obslužný uzel jádra sítě (např. MSC) monitoruje nastavený Initial Detection Point. Při dosažení tohoto bodu uzel zabalí relevantní informace – jako jsou volané a volající číslo, poloha a služební klíč – do operace Initial Detection Point. Tato operace je následně odeslána přes protokol [CAP](/mobilnisite/slovnik/cap/) (CAMEL Application Part) k určenému SCP. SCP obsahující přizpůsobenou servisní logiku tento požadavek zpracuje a vrátí instrukce uzlu jádra sítě. Tyto instrukce, předávané prostřednictvím CAP operací jako Request Report [BCSM](/mobilnisite/slovnik/bcsm/) (Basic Call State Model) event, Connect, Continue nebo Apply Charging, určují, jak má hovor nebo relace pokračovat, být účtována nebo upravena.

Z architektonického hlediska je IDP klíčovým prvkem CAMEL Subscription Information ([CSI](/mobilnisite/slovnik/csi/)), staženého do jádra sítě z HLR/HSS. Definuje spouštěč pro interakci se službou. Role IDP je klíčová pro oddělení servisní logiky od přepínací logiky, což umožňuje rychlé nasazování nových služeb bez nutnosti modifikace každé ústředny jádra sítě. Je to vstupní bod pro širokou škálu přidaných služeb, včetně předplaceného účtování v reálném čase, kontroly podvodů, virtuálních privátních sítí (VPN) a služeb založených na poloze, a tvoří tak most mezi tradičním jádrem sítě s přepojováním okruhů nebo paketů a inteligentními servisními platformami.

## K čemu slouží

IDP byl vytvořen, aby řešil omezení tradičního poskytování služeb založeného na ústřednách v mobilních sítích. Před CAMEL a koncepty jako je IDP vyžadovaly nové služby proprietární, na dodavateli závislé implementace přímo v každém Mobile Switching Centre (MSC), což činilo nasazení pomalým, nákladným a nekonzistentním v rámci sítě. Účelem IDP je poskytnout standardizovaný, dobře definovaný spouštěcí mechanismus, který umožňuje externí, centralizované servisní platformě (SCP) zasáhnout do řízení hovorů a relací.

Toto řeší problém přenositelnosti služeb a rychlé inovace. Umožňuje síťovým operátorům vyvíjet a nasazovat přizpůsobené, inteligentní služby nezávisle na dodavatelích jejich infrastruktury jádra sítě. IDP jako počáteční spouštěč je katalyzátorem této interakce. Konkrétně řeší potřebu kontrolovaného, standardizovaného bodu interakce, kde může být servisní logika vyvolána na základě profilů účastníků, což umožňuje sofistikované řízení služeb, účtování v reálném čase a personalizované funkce, které bylo obtížné nebo nemožné implementovat v čistě ústřednově orientovaném modelu. Jeho vytvoření bylo motivováno konkurenční potřebou operátorů odlišit své nabídky a technickou potřebou flexibilnější, otevřenější servisní architektury podobné konceptu Inteligentní sítě (IN) z pevné telefonie, ale přizpůsobené pro mobilitu a roamingový kontext GSM a UMTS.

## Klíčové vlastnosti

- Standardizovaný spouštěcí bod v modelu volání/stavu CAMEL
- Definován v CAMEL Subscription Information (CSI) účastníka
- Spouští CAP dialog mezi uzlem jádra sítě (gsmSSF) a Service Control Point (SCP)
- Nese základní informace o hovoru/relaci, jako jsou volající/volaná čísla a poloha
- Umožňuje přerušení zpracování v jádru sítě pro instrukce externí servisní logiky
- Základ pro služby jako předplacené účtování, správa podvodů a překlad čísel

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)
- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)

## Definující specifikace

- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture

---

📖 **Anglický originál a plná specifikace:** [IDP na 3GPP Explorer](https://3gpp-explorer.com/glossary/idp/)
