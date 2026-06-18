---
slug: "pbid"
url: "/mobilnisite/slovnik/pbid/"
type: "slovnik"
title: "PBID – PhoneBook IDentifier"
date: 2025-01-01
abbr: "PBID"
fullName: "PhoneBook IDentifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pbid/"
summary: "Jedinečný identifikátor používaný v aplikacích USIM k odkazování na záznamy telefonního seznamu uložené na UICC. Umožňuje efektivní správu a přístup k kontaktním informacím a propojuje záznamy napříč"
---

PBID je jedinečný identifikátor používaný v aplikacích USIM k odkazování na záznamy telefonního seznamu uložené na UICC, což umožňuje efektivní správu a přístup k kontaktním informacím.

## Popis

PhoneBook IDentifier (PBID) je standardizovaný identifikátor definovaný ve specifikacích 3GPP, konkrétně v TS 31.102 pro aplikační toolkit [USIM](/mobilnisite/slovnik/usim/) a TS 21.905 pro terminologii. Slouží jako jedinečný referenční klíč pro jednotlivé záznamy v rámci úložiště telefonního seznamu na univerzální integrované obvodové kartě (UICC), jako je [SIM](/mobilnisite/slovnik/sim/) nebo USIM. Každý záznam kontaktu – včetně polí jako jméno, telefonní číslo a e-mail – má přiřazen PBID, což aplikacím umožňuje načíst, aktualizovat nebo smazat konkrétní položky bez nutnosti prohledávat celý telefonní seznam. Identifikátor je typicky implementován jako celé číslo nebo strukturovaná hodnota v rámci souborového systému UICC, často spojená s elementárním souborem ([EF](/mobilnisite/slovnik/ef/)) používaným pro ukládání dat telefonního seznamu.

Z architektonického hlediska PBID funguje v aplikační vrstvě UICC a je přístupný prostřednictvím příkazů definovaných ve standardech [ETSI](/mobilnisite/slovnik/etsi/)/3GPP pro komunikaci s kartou. Když mobilní zařízení nebo síťová aplikace potřebuje manipulovat s daty telefonního seznamu, použije PBID ve spojení s příkazy [APDU](/mobilnisite/slovnik/apdu/) (Application Protocol Data Unit) k cílení na přesné záznamy. To je klíčové pro funkce jako synchronizace s externími servery, záložní operace nebo přidružené služby, které upravují kontakty. PBID může být asociován s dalšími atributy, jako je viditelnost záznamu nebo členství ve skupině, což podporuje pokročilou správu telefonního seznamu.

V praxi PBID umožňuje plynulou interakci mezi UICC a softwarem zařízení nebo platformami pro správu na dálku ([OTA](/mobilnisite/slovnik/ota/)). Například při synchronizaci kontaktů může server odkazovat na PBID, aby aktualizoval pouze změněné záznamy, čímž snižuje objem přenášených dat. Také podporuje více telefonních seznamů (např. telefonní seznam SIM vs. zařízení) tím, že poskytuje konzistentní schéma odkazování. Role identifikátoru sahá až k zabezpečení, protože přístup k datům spojeným s PBID může být řízen oprávněními apletu UICC, což zajišťuje soukromí uživatele. Standardizací PBID zajišťuje 3GPP interoperabilitu napříč zařízeními a sítěmi a usnadňuje tak spolehlivou správu kontaktů v mobilních ekosystémech.

## K čemu slouží

PBID byl zaveden, aby řešil potřebu efektivní a standardizované správy záznamů telefonního seznamu na UICC, která se stávala stále důležitější s tím, jak [SIM](/mobilnisite/slovnik/sim/) karty začaly ukládat více kontaktních dat. Před jeho standardizací byl přístup k telefonnímu seznamu závislý na pozičním indexování nebo proprietárních metodách, což vedlo k fragmentaci a problémům s kompatibilitou napříč zařízeními a operátory. Release 6 3GPP formalizoval PBID, aby poskytl univerzální, jedinečný identifikátor pro každý kontakt, umožňující přesné operace [CRUD](/mobilnisite/slovnik/crud/) (Create, Read, Update, Delete).

Vytvoření PBID bylo motivováno rozvojem mobilních služeb, které interagují s telefonními seznamy, jako je provisioning na dálku (OTA), zálohování kontaktů a přidružené služby, jako je vylepšení identifikace volajícího. Řeší problémy s poškozením dat během aktualizací a neefektivní synchronizací tím, že umožňuje cílenou manipulaci se záznamy. Historicky, jak telefony začaly podporovat větší seznamy kontaktů a scénáře s více SIM kartami, se robustní identifikátor stal nezbytným pro udržení integrity dat a uživatelského zážitku. PBID také podporuje regulační funkce, jako je ukládání nouzových kontaktů, tím, že zajišťuje spolehlivý přístup ke konkrétním záznamům. Jeho zařazení do standardů 3GPP odráží posun odvětví směrem k interoperabilním aplikacím UICC, což snižuje náklady a zlepšuje nasazování služeb.

## Klíčové vlastnosti

- Jedinečný identifikátor pro záznamy telefonního seznamu na UICC/USIM
- Umožňuje přesný přístup a manipulaci prostřednictvím standardizovaných příkazů APDU
- Podporuje procesy synchronizace a zálohování se sníženou režií dat
- Kompatibilní s více aplikacemi a souborovými strukturami telefonního seznamu
- Umožňuje správu kontaktních dat na dálku (OTA)
- Integruje se s bezpečnostními mechanismy pro řízený přístup k záznamům

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [APDU – Application Protocol Data Unit](/mobilnisite/slovnik/apdu/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification

---

📖 **Anglický originál a plná specifikace:** [PBID na 3GPP Explorer](https://3gpp-explorer.com/glossary/pbid/)
