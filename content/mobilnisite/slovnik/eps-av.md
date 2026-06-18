---
slug: "eps-av"
url: "/mobilnisite/slovnik/eps-av/"
type: "slovnik"
title: "EPS-AV – EPS Authentication Vector"
date: 2025-01-01
abbr: "EPS-AV"
fullName: "EPS Authentication Vector"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/eps-av/"
summary: "Soubor kryptografických parametrů používaných k autentizaci UE a navázání bezpečnostních klíčů v Evolved Packet System (EPS). Generuje jej HSS/AuC a zasílá MME k provedení vzájemné autentizace a odvoz"
---

EPS-AV je soubor kryptografických parametrů generovaných HSS/AuC a zasílaných MME k autentizaci UE a navázání bezpečnostních klíčů pro zabezpečenou komunikaci v Evolved Packet System.

## Popis

EPS Authentication Vector (EPS-AV) je základní bezpečnostní datová struktura v Evolved Packet System (EPS) dle 3GPP, definovaná v TS 33.401. Generuje ji Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a jeho Authentication Centre (AuC) pro konkrétního uživatele a slouží jako podklad pro proceduru Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) mezi sítí a User Equipment (UE). Každý EPS-AV obsahuje čtyři základní složky: náhodný výzvu ([RAND](/mobilnisite/slovnik/rand/)), očekávanou odpověď ([XRES](/mobilnisite/slovnik/xres/)), šifrovací klíč ([CK](/mobilnisite/slovnik/ck/)) a integritní klíč ([IK](/mobilnisite/slovnik/ik/)). Dále zahrnuje autentizační token ([AUTN](/mobilnisite/slovnik/autn/)), který umožňuje UE ověřit si síť, čímž je zajištěna vzájemná autentizace. HSS/AuC generuje EPS-AV pomocí dlouhodobého tajného klíče účastníka (K) a pořadového čísla ([SQN](/mobilnisite/slovnik/sqn/)), aby zajistil aktuálnost a zabránil opakovaným útokům.

Když se UE připojuje k síti EPS, Mobility Management Entity (MME) vyžádá autentizační vektory od HSS. Po obdržení jednoho nebo více EPS-AV MME zahájí proceduru AKA zasláním RAND a AUTN z jednoho vektoru do UE. UE použije svou vlastní kopii tajného klíče (K) ke zpracování AUTN, čímž ověří pravost sítě, a vypočítá odpověď (RES) na výzvu RAND. UE také lokálně odvodí stejné CK a IK. MME porovná RES od UE s očekávaným XRES z EPS-AV. Pokud se shodují, je autentizace úspěšná a MME a UE přistoupí k odvození následné hierarchie klíčů používaných pro NAS a AS zabezpečení, konkrétně K_ASME, z CK a IK.

Role EPS-AV je klíčová, protože je základem pro všechny následné bezpečnostní klíče v EPS, včetně těch pro šifrování a integritní ochranu řídicí roviny (NAS) a uživatelské roviny (AS). Jeho návrh zajišťuje jak autentizaci uživatele, tak autentizaci sítě, a chrání před útoky vydávání se za jiného. Vektorový přístup umožňuje MME předem načíst více EPS-AV, což umožňuje efektivní autentizaci během událostí mobility, jako je předávání hovoru, bez nutnosti pokaždé dotazovat HSS, a tím se snižuje latence a signalizační zátěž. Bezpečnost celého EPS závisí na důvěrnosti a integritě generování a přenosu EPS-AV mezi HSS a MME, který je chráněn uvnitř páteřní sítě.

## K čemu slouží

EPS Authentication Vector byl zaveden v 3GPP Release 8, aby poskytl robustní mechanismus autentizace a dohody o klíčích pro nový Evolved Packet System (EPS/LTE). Řešil potřebu standardizované, bezpečné metody k navázání vzájemné důvěry mezi zařízením uživatele a sítí, čímž nahradil a vylepšil autentizační vektory používané v legacy systémech UMTS (3G). Hlavní problém, který řeší, je umožnění bezpečného počátečního přístupu a odvození klíčů v plně IP ploché architektuře, které chyběly prvky s okruhovým přepojením předchozích generací.

Jeho vytvoření bylo motivováno evolucí ke zjednodušené síťové architektuře LTE, která zavedla nové síťové elementy jako MME a vyžadovala hierarchii klíčů odlišnou od UMTS. EPS-AV poskytuje kryptografický materiál potřebný pro vygenerování K_ASME, kořenového klíče pro zabezpečení EPS, což zajišťuje plynulá předávání hovoru a konzistentní správu bezpečnostního kontextu v celé vyvinuté síti. Zachovává principy zpětné kompatibility s UMTS AKA, zároveň se přizpůsobuje novým rozhraním páteřní sítě, jako je S6a mezi MME a HSS.

## Klíčové vlastnosti

- Obsahuje RAND (náhodná výzva), XRES (očekávaná odpověď), CK (šifrovací klíč), IK (integritní klíč) a AUTN (autentizační token)
- Umožňuje vzájemnou autentizaci mezi UE a sítí prostřednictvím procedury AKA
- Slouží jako kryptografický zdroj pro odvození K_ASME a celé hierarchie klíčů EPS
- Umožňuje MME dávkové přednačítání pro podporu efektivních následných autentizací
- Generován HSS/AuC pomocí dlouhodobého tajného klíče účastníka a pořadového čísla
- Základní pro navázání bezpečnostního kontextu NAS a AS pro šifrování a integritní ochranu

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [SQN – Sequence Number](/mobilnisite/slovnik/sqn/)

## Definující specifikace

- **TS 33.401** (Rel-19) — EPS Security Architecture

---

📖 **Anglický originál a plná specifikace:** [EPS-AV na 3GPP Explorer](https://3gpp-explorer.com/glossary/eps-av/)
