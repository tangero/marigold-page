---
slug: "pnm"
url: "/mobilnisite/slovnik/pnm/"
type: "slovnik"
title: "PNM – Personal Network Management"
date: 2025-01-01
abbr: "PNM"
fullName: "Personal Network Management"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pnm/"
summary: "PNM je servisní rámec 3GPP, který umožňuje uživateli spravovat osobní síť složenou z více osobních zařízení a vzdálených osobních zařízení. Umožňuje vytváření, konfiguraci a řízení zabezpečené, na uži"
---

PNM je servisní rámec 3GPP, který umožňuje uživateli spravovat, konfigurovat a řídit zabezpečenou osobní síť složenou z více místních a vzdálených zařízení napříč různými přístupovými technologiemi.

## Popis

Personal Network Management (PNM) je servisní schopnost definovaná 3GPP od Release 7, která poskytuje rámec pro uživatele ke správě jejich souboru zařízení jako soudržné, personalizované sítě. Osobní síť (Personal Network, [PN](/mobilnisite/slovnik/pn/)) je konstrukt zaměřený na uživatele, který zahrnuje zařízení přímo vlastněná uživatelem (Personal Devices) a zařízení dostupná na dálku (Remote Personal Devices), která se mohou nacházet na různých místech, jako je domov, kancelář nebo auto. PNM poskytuje mechanismy pro objevování, asociaci, konfiguraci a řízení těchto zařízení a služeb mezi nimi, čímž vytváří jednotný uživatelský zážitek napříč více přístupovými technologiemi (např. 3G, 4G, WiFi, Bluetooth).

Architektura PNM zahrnuje několik logických entit. Jádrem je PNM Server, který může být síťový nebo může sídlit na důvěryhodném zařízení uživatele. Spravuje konfiguraci PN, včetně seznamu členských zařízení, jejich schopností a uživatelských politik. Klíčovou součástí je Personal Network Gateway (PN GW), který funguje jako prostředník mezi zařízeními v různých sítích, poskytuje překlad protokolů, zabezpečovací funkce a zajišťuje dosažitelnost. Zařízení v rámci PN jsou identifikována a autentizována, často s využitím [IMSI](/mobilnisite/slovnik/imsi/) nebo jiných identifikátorů 3GPP jako základu. Mezi řídicí funkce patří vytváření/úprava/mazání PN, objevování služeb mezi zařízeními PN, autorizace služeb a správa životního cyklu PN.

PNM funguje tak, že umožňuje uživateli prostřednictvím řídicího klienta definovat jeho Osobní síť. Uživatel zaregistruje svá zařízení u PNM Serveru, čímž se vytvoří vztahy důvěry. Po nakonfigurování si mohou zařízení vzájemně objevovat služby prostřednictvím PNM rámce. Pro komunikaci, zejména mezi zařízeními v různých sítích (např. mobilní telefon v mobilní síti a domácí [PC](/mobilnisite/slovnik/pc/) na pevném broadbandu), spojení usnadňuje PN GW, který řeší adresování a zabezpečení. Systém využívá bezpečnostní mechanismy 3GPP k zajištění, že všechny řídicí operace a výměny dat v rámci PN jsou zabezpečené a soukromé.

Úloha PNM v síti spočívá v abstrakci složitosti připojení více zařízení a více přístupů jak pro uživatele, tak pro vývojáře aplikací. Umožňuje kontinuitu služeb a služby s přihlédnutím ke kontextu napříč uživatelovými zařízeními. Například uživatel může začít sledovat video na svém telefonu a plynule jej přenést na domácí televizi, přičemž PNM zajišťuje přenos relace a objevování zařízení. PNM tvoří základní vrstvu pro personalizované služby v IP Multimedia Subsystem (IMS) a dalších systémech, podporuje vizi prostředí uživatele, které se přizpůsobuje jeho přítomnosti a preferencím.

## K čemu slouží

PNM bylo vytvořeno k řešení rostoucího množství osobních zařízení (telefonů, tabletů, notebooků, senzorů, domácích spotřebičů) a touhy uživatele mít je bezproblémově propojené jako jednotný systém. Před PNM bylo řízení interakcí mezi zařízeními napříč různými síťovými doménami ad-hoc, vyžadovalo manuální konfiguraci a často spoléhalo na proprietární řešení, což vedlo k roztříštěnému uživatelskému zážitku. PNM si kladlo za cíl standardizovat rámec pro vytváření a správu na uživatele zaměřené, mezidoménové osobní sítě.

Primární problém, který řeší, je složitost objevování služeb, zabezpečeného připojení a konzistentního poskytování služeb napříč heterogenním souborem uživatelových zařízení. Umožňuje nové personalizované služby, jako je sdílení obsahu, synchronizace zařízení a dálkové ovládání domácích zařízení z mobilního telefonu. Motivace vycházela z konvergence telekomunikačních a internetových služeb, kde se ústředním bodem poskytování služeb stává uživatel, nikoli zařízení nebo síť. PNM poskytuje řídicí vrstvu k realizaci tohoto konceptu 'osobní sítě'.

Historicky zavedené v Release 7, PNM bylo součástí širší práce 3GPP na personalizaci a kontinuitě služeb. Řešilo omezení dřívějších modelů zaměřených na zařízení tím, že poskytlo síťově asistovaný rámec, který mohl využívat schopnosti operátora pro autentizaci, zabezpečení a dosažitelnost. To umožnilo robustnější a škálovatelnější osobní sítě ve srovnání s čistě peer-to-peer ad-hoc řešeními, a připravilo tak cestu pro pozdější koncepty jako Internet věcí (IoT) a uživatelské zážitky s více zařízeními.

## Klíčové vlastnosti

- Vytváření a správa životního cyklu Osobní sítě (PN) uživatele
- Objevování a registrace Osobních zařízení (Personal Devices) a Vzdálených osobních zařízení (Remote Personal Devices)
- Objevování služeb a výměna informací o schopnostech mezi zařízeními PN
- Zabezpečená autentizace a autorizace pro členství v PN a služby
- Propojování prostřednictvím Personal Network Gateway (PN GW) pro připojení napříč sítěmi
- Podpora uživatelsky definovaných politik a preferencí pro chování PN

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 22.259** (Rel-19) — Personal Network Management Requirements
- **TR 22.937** (Rel-13) — FMC requirements for 3GPP-WLAN service continuity
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.259** (Rel-19) — Personal Network Management (PNM) Procedures
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 32.275** (Rel-19) — MMTel Charging Specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 32.850** (Rel-14) — IMS Charging Correlation Methods Study
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security

---

📖 **Anglický originál a plná specifikace:** [PNM na 3GPP Explorer](https://3gpp-explorer.com/glossary/pnm/)
