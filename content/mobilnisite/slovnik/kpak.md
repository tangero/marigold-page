---
slug: "kpak"
url: "/mobilnisite/slovnik/kpak/"
type: "slovnik"
title: "KPAK – KMS Public Authentication Key"
date: 2025-01-01
abbr: "KPAK"
fullName: "KMS Public Authentication Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/kpak/"
summary: "Veřejný klíč používaný v rámci architektury služby správy klíčů (KMS) pro ověřování. Umožňuje bezpečné ověření zařízení a navázání klíčů bez použití certifikátů, což je klíčové pro zabezpečení IoT a M"
---

KPAK je veřejný klíč používaný v rámci architektury služby správy klíčů (KMS) pro ověřování zařízení bez certifikátů a navázání klíčů. Tvoří základ odlehčené bezpečnostní architektury 3GPP pro omezená IoT a MTC zařízení.

## Popis

Veřejný ověřovací klíč [KMS](/mobilnisite/slovnik/kms/) (KPAK) je základní kryptografický prvek v architektuře služby správy klíčů (KMS) standardizované 3GPP pro komunikaci mezi stroji ([MTC](/mobilnisite/slovnik/mtc/)) a zařízení internetu věcí (IoT). Funguje jako dlouhodobý veřejný klíč náležící serveru KMS. Architektura je asymetrická: každý server KMS má unikátní KPAK a odpovídající privátní klíč, zatímco zařízení jsou během výroby nebo počáteční inicializace vybavena KPAK jejich domovského serveru KMS. Toto nastavení vytváří kořen důvěry bez nutnosti individuálních certifikátů pro zařízení, což je klíčový konstrukční aspekt pro levná, hromadně nasazovaná IoT zařízení, kde je režie správy certifikátů neúnosná.

Operační postup zahrnující KPAK začíná, když se zařízení pokouší připojit k síti nebo potřebuje navázat bezpečné relakční klíče. Zařízení použije předem zřízený KPAK k ověření zpráv ze sítě a k odvození sdílených tajemství. Konkrétně síťová strana (např. [MME](/mobilnisite/slovnik/mme/) nebo SCEF fungující jako KMS-Client) komunikuje se serverem KMS. Server KMS použije svůj privátní klíč k vygenerování ověřovacích vektorů nebo klíčového materiálu, který je pak odeslán síťové entitě. Zařízení může ověřit pravost tohoto materiálu pomocí KPAK a následně odvodit stejné relakční klíče, což umožní vzájemné ověření a navázání zabezpečeného kanálu. Tento proces, detailně popsaný v TS 24.582, je ústřední pro procedury inicializace a odvozování klíčů založené na KMS.

Klíčovými komponentami v tomto ekosystému jsou server KMS (držící privátní klíč KPAK), KMS-Client (síťová funkce jako MME) a UE/zařízení. Role KPAK spočívá v tom, že funguje jako statický, široce distribuovaný veřejný ověřovací klíč. Jeho bezpečnost závisí na utajení odpovídajícího privátního klíče, který je bezpečně uložen na serveru KMS. Tento model odděluje identitu zařízení od kryptografických klíčů, což umožňuje efektivní skupinové zabezpečení a zjednodušený management životního cyklu. KPAK je nedílnou součástí protokolů jako je inicializace pro MTC založená na KMS (KMS-BM) a poskytuje škálovatelnou alternativu k tradičnímu protokolu Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) pro scénáře masivního IoT, kde ověřování založené na SIM nemusí být proveditelné nebo optimální.

## K čemu slouží

KPAK byl zaveden, aby řešil specifické bezpečnostní a škálovatelnostní výzvy komunikace mezi stroji ([MTC](/mobilnisite/slovnik/mtc/)) a internetu věcí (IoT) v sítích 3GPP. Tradiční mobilní ověřování, založené na modulu univerzální identifikační karty účastníka (USIM) a sadě algoritmů MILENAGE, zahrnuje složitou signalizaci a správu stavu, což může být přítěží pro jednoduchá, nízkopříkonová zařízení nasazená ve velkém množství. Primární motivací bylo vytvořit odlehčený rámec pro ověřování bez certifikátů, který snižuje signalizační režii, zjednodušuje výrobu zařízení a podporuje efektivní skupinové zabezpečení.

Historicky zabezpečení IoT zařízení často zahrnovalo zřizování unikátních certifikátů nebo sdílených tajemství, což představovalo významné problémy se správou a distribucí klíčů. Architektura [KMS](/mobilnisite/slovnik/kms/) s KPAK v jádru to řeší vytvořením centralizované kotvy důvěry. Zařízení potřebuje znát pouze veřejný KPAK svého domovského serveru KMS, čímž odpadá potřeba individuálních certifikátů zařízení nebo složité distribuce klíčů během výroby. Tento přístup výrazně snižuje náklady a složitost zřizování zařízení při zachování silného kryptografického zabezpečení založeného na principech veřejného klíče. Byl navržen tak, aby umožnil zabezpečenou komunikaci pro zařízení, která nemusí mít UICC, a podporoval scénáře jako senzorové sítě a průmyslový monitoring, kde je tradiční ověřování založené na SIM nepraktické.

## Klíčové vlastnosti

- Umožňuje ověřování IoT/MTC zařízení bez certifikátů
- Slouží jako statický, předem zřízený veřejný kořen důvěry v zařízeních
- Podporuje odvození bezpečných relakčních klíčů mezi zařízením a sítí
- Umožňuje odlehčené inicializační procedury (KMS-BM)
- Umožňuje škálovatelnou, skupinovou správu zabezpečení
- Snižuje signalizační režii ve srovnání s kompletními průběhy AKA

## Související pojmy

- [KMS – Key Management Service](/mobilnisite/slovnik/kms/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols

---

📖 **Anglický originál a plná specifikace:** [KPAK na 3GPP Explorer](https://3gpp-explorer.com/glossary/kpak/)
