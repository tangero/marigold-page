---
slug: "drq"
url: "/mobilnisite/slovnik/drq/"
type: "slovnik"
title: "DRQ – Delete Request"
date: 2025-01-01
abbr: "DRQ"
fullName: "Delete Request"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/drq/"
summary: "Řídicí procedura používaná k vyžádání smazání dat účastníka nebo konfiguračních entit sítě. Jedná se o základní operaci pro údržbu databází účastníků a integrity síťových zdrojů, která zajišťuje možno"
---

DRQ je řídicí procedura používaná k vyžádání smazání dat účastníka nebo konfiguračních entit sítě za účelem zachování integrity databází a zdrojů.

## Popis

Delete Request (DRQ) je standardizovaná řídicí procedura v rámci architektury 3GPP, primárně dokumentovaná ve specifikaci 23.976. Funguje jako příkaz nebo zpráva, kterou používají funkce správy sítě nebo jiné síťové elementy k pokynu cílové entitě, jako je databáze účastníků (např. [HSS](/mobilnisite/slovnik/hss/), [UDM](/mobilnisite/slovnik/udm/)) nebo úložiště politik, aby odstranila konkrétní datové záznamy. Procedura je klíčová pro správu životního cyklu profilů účastníků, konfigurací služeb a pravidel politik.

Operačně zpráva DRQ obsahuje identifikátory entity, která má být smazána, a konkrétních datových atributů nebo celého záznamu určeného k odstranění. Zdrojový systém, často Operations Support System ([OSS](/mobilnisite/slovnik/oss/)) nebo síťová funkce provádějící údržbu, požadavek formuluje. Přijímající entita DRQ zpracuje, ověří autorizaci a provede smazání ze svého trvalého úložiště. Odpověď je typicky vrácena k označení úspěchu nebo neúspěchu a může obsahovat chybové kódy, pokud požadovaná data neexistují nebo pokud žadatel nemá dostatečná oprávnění.

Její role je nedílnou součástí síťové automatizace a datové hygieny. Umožňuje automatizované odstranění dat účastníka při ukončení služby, opravu konfiguračních chyb a údržbu při rekonfiguraci sítě nebo vyřazování síťových řezů. Procedura zajišťuje, že síťové databáze zůstávají synchronizovány se skutečným stavem účastníků a služeb, čímž předchází konfliktům, bezpečnostním problémům nebo únikům zdrojů, které by mohly vzniknout ze zastaralých dat.

## K čemu slouží

Procedura DRQ byla zavedena, aby poskytla standardizovaný a spolehlivý mechanismus pro mazání dat v telekomunikačních sítích. Před standardizací správa dat účastníků a konfiguračních dat často závisela na proprietárních, manuálních nebo skriptových metodách, které byly náchylné k chybám, pomalé a obtížně automatizovatelné v prostředí více dodavatelů. Tento nedostatek společné procedury mohl vést k nekonzistentnostem mezi síťovými elementy a databázemi.

Její vytvoření bylo motivováno potřebou efektivních operací, správy a údržby ([OAM](/mobilnisite/slovnik/oam/)), jak sítě rostly v komplexitě a základna účastníků se rychle rozšiřovala. Automatizované zřizování a rušení zřizování se staly nezbytnými. DRQ jako součást sady řídicích procedur (včetně požadavků na vložení a aktualizaci) umožňuje plnou správu životního cyklu. Řeší problém bezpečného a přesného odstranění dat, což je stejně důležité jako jejich vytváření, aby se uvolnily zdroje, zachovalo soukromí (např. soulad s GDPR pro vymazání dat účastníka) a zajistilo, že síťové konfigurace odrážejí aktuální provozní požadavky.

## Klíčové vlastnosti

- Standardizovaný formát zprávy pro požadavky na smazání napříč rozhraními 3GPP
- Podpora cíleného mazání konkrétních datových atributů nebo celých záznamů
- Integrace se správou dat účastníků (např. HSS/UDM) a správou politik
- Poskytnutí mechanismů odpovědí úspěch/neúspěch s ošetřením chyb
- Nezbytnost pro automatizované pracovní postupy OAM a správu životního cyklu služeb
- Umožnění souladu s předpisy o ochraně osobních údajů prostřednictvím řízených postupů vymazání

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TR 23.976** (Rel-19) — Push Service Requirements Analysis

---

📖 **Anglický originál a plná specifikace:** [DRQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/drq/)
