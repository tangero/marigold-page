---
slug: "nrs"
url: "/mobilnisite/slovnik/nrs/"
type: "slovnik"
title: "NRS – Network Requested Session"
date: 2025-01-01
abbr: "NRS"
fullName: "Network Requested Session"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nrs/"
summary: "Network Requested Session (NRS, relace iniciovaná sítí) je koncept správy umožňující síti iniciovat relaci pro zařízení, například pro správu zařízení nebo aktualizace softwaru. Je definován v 3GPP TS"
---

NRS je koncept správy umožňující síti iniciovat relaci pro zařízení, například pro dálkovou správu zařízení nebo aktualizace softwaru.

## Popis

Network Requested Session (NRS, relace iniciovaná sítí) je standardizovaný mechanismus v rámci architektur správy 3GPP, který umožňuje síti proaktivně navázat relaci s uživatelským zařízením (UE) bez nutnosti počáteční žádosti od samotného zařízení. Tato schopnost je zásadní pro úkoly iniciované operátorem, jako je konfigurace zařízení přes vzdušné rozhraní ([OTA](/mobilnisite/slovnik/ota/)), aktualizace firmwaru nebo diagnostické procedury. Proces se řídí principy architektury služebně orientované správy ([SBMA](/mobilnisite/slovnik/sbma/)), kde mohou managementové služby vyvolat navázání relace, jak je definováno ve specifikacích jako TS 28.404. Síť, typicky prostřednictvím Management Function ([MF](/mobilnisite/slovnik/mf/)) nebo systému Operations, Administration and Maintenance ([OAM](/mobilnisite/slovnik/oam/)), identifikuje cílové UE na základě kritérií jako jsou data předplatného nebo síťové politiky. Následně spustí proceduru navázání relace, která zahrnuje prvky jádra sítě k lokalizaci a pagingu UE, pokud je v nečinném režimu, a nakonec vytvoří datovou relaci (např. [PDP](/mobilnisite/slovnik/pdp/) kontext v [GPRS](/mobilnisite/slovnik/gprs/) nebo [PDU](/mobilnisite/slovnik/pdu/) Session v 5G) vyhrazenou pro úlohu správy. Tato relace poskytuje potřebný přenosový prostředek pro transport managementových zpráv, například používajících protokol Open Mobile Alliance Device Management ([OMA](/mobilnisite/slovnik/oma/) DM) nebo jiné managementové protokoly, přímo do zařízení. Architektura zajišťuje zabezpečené a autorizované iniciování, často s integrací home subscriber serverů a funkcí řízení politik pro ověření oprávnění. NRS hraje kritickou roli v umožnění efektivní správy zařízení ve velkém měřítku, snižuje potřebu manuální intervence a zajišťuje, aby zařízení zůstávala kompatibilní se síťovými politikami a verzemi softwaru, čímž zvyšuje celkovou spolehlivost sítě a kvalitu služeb.

## K čemu slouží

Účelem Network Requested Session (NRS, relace iniciované sítí) je řešit problém pasivní správy zařízení, kdy operátoři dříve museli čekat na připojení zařízení nebo spoléhat na akce iniciované uživatelem pro údržbové úkoly. Historicky správa milionů zařízení – jako jsou chytré telefony, IoT senzory nebo modemy – vyžadovala neefektivní metody, například čekání na periodické kontakty zařízení nebo odesílání SMS triggerů, které byly nespolehlivé a pomalé. NRS byl vytvořen, aby poskytl síťovým operátorům proaktivní kontrolu, umožňující jim iniciovat relace na vyžádání pro kritické operace, jako jsou bezpečnostní záplaty, konfigurační aktualizace nebo diagnostika chyb. Tím se řeší omezení v škálovatelnosti a včasnosti, zejména když se sítě vyvíjely pro podporu masivních IoT nasazení a vyžadovaly více automatizovaných operací. Standardizací této schopnosti v 3GPP, počínaje Release 7, poskytl jednotný rámec napříč různými přístupovými technologiemi (např. GERAN, UTRAN, E-UTRAN, NR), což zajišťuje interoperabilitu a efektivní využití zdrojů. Motivace vychází z rostoucí potřeby dálkové správy v komplexních sítích, snižování provozních nákladů a zlepšování dostupnosti služeb bez závislosti na chování uživatele.

## Klíčové vlastnosti

- Umožňuje navázání relace iniciované sítí bez žádosti od UE
- Podporuje automatizovanou správu zařízení a aktualizace softwaru
- Integruje se se systémy OAM a architekturou služebně orientované správy (SBMA)
- Funguje napříč více releasy 3GPP a přístupovými technologiemi
- Poskytuje zabezpečené a autorizované mechanismy spouštění relací
- Umožňuje rozsáhlé a efektivní dálkové operace pro IoT a spotřebitelská zařízení

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 28.307** (Rel-19) — QoE Measurement Collection IRP Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [NRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrs/)
