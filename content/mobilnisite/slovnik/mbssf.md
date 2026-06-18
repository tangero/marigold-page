---
slug: "mbssf"
url: "/mobilnisite/slovnik/mbssf/"
type: "slovnik"
title: "MBSSF – Multicast/Broadcast Service Security Function"
date: 2026-01-01
abbr: "MBSSF"
fullName: "Multicast/Broadcast Service Security Function"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mbssf/"
summary: "Síťová funkce v 5G Core, která poskytuje bezpečnostní služby specificky pro multicastový a broadcastový provoz. Zajišťuje správu klíčů, autentizaci a šifrování pro MBS relace, čímž zaručuje zabezpečen"
---

MBSSF je síťová funkce 5G Core, která poskytuje bezpečnostní služby pro multicastový a broadcastový provoz tím, že zajišťuje správu klíčů, autentizaci a šifrování pro zabezpečené doručování obsahu.

## Popis

Multicast/Broadcast Service Security Function (MBSSF) je klíčová bezpečnostní komponenta v architektuře služby Multicast/Broadcast Service ([MBS](/mobilnisite/slovnik/mbs/)) 5G Core sítě. Je odpovědná za kompletní bezpečnostní životní cyklus MBS relace. MBSSF generuje, spravuje a distribuuje kryptografické klíče používané k ochraně MBS provozu (důvěrnost a integrita uživatelské roviny) a související signalizace. Rozhraní má s dalšími funkcemi jádra sítě, především s [MB-SMF](/mobilnisite/slovnik/mb-smf/) (MBS Session Management Function) a [UDM](/mobilnisite/slovnik/udm/) (Unified Data Management), za účelem autentizace a autorizace uživatelských zařízení (UE) pro konkrétní MBS relace.

Operačně, když je MBS relace zřízena, MB-SMF požádá MBSSF o zahájení bezpečnostních procedur. MBSSF vygeneruje pro MBS relaci hlavní relový klíč (Master Session Key, [MSK](/mobilnisite/slovnik/msk/)). Pro každé uživatelské zařízení (UE), které se k relaci připojí, odvodí MBSSF z MSK a identifikátoru předplatného UE uživatelský specifický klíč (User-specific Key, UK). Tento UK je poté poskytnut uživatelskému zařízení prostřednictvím zabezpečeného unicastového kanálu, typicky přes MB-SMF a Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) za použití [NAS](/mobilnisite/slovnik/nas/) zabezpečení. Uživatelské zařízení tento UK použije k odvození potřebných šifrovacích klíčů pro provoz (Traffic Encryption Keys, [TEK](/mobilnisite/slovnik/tek/)) k dešifrování multicastového/broadcastového datového toku.

MBSSF také podporuje procesy obnovy a odvolání klíčů pro udržení bezpečnosti v čase. Může periodicky aktualizovat MSK a zasílat nové odvozené klíče autorizovaným uživatelským zařízením, čímž snižuje riziko kompromitace klíčů. Architektonicky může být MBSSF samostatnou síťovou funkcí (Network Function, [NF](/mobilnisite/slovnik/nf/)) nebo může být sloučena s jinou funkcí, jako je MB-SMF. Pro komunikaci s ostatními síťovými funkcemi používá rozhraní definovaná 3GPP na bázi služeb, zejména Nmbsf. Její návrh zajišťuje, že je multicastová/broadcastová bezpečnost integrována do bezpečnostního rámce 5G, přičemž využívá stávající autentizační infrastrukturu (5G AKA) a zároveň řeší unikátní model doručování typu point-to-multipoint.

## K čemu slouží

MBSSF byla vytvořena, aby řešila specifické bezpečnostní výzvy vlastní multicastovým a broadcastovým službám, které byly v 5G znovu zavedeny a vylepšeny. V modelu point-to-multipoint jsou tradiční bezpečnostní mechanismy pro unicast (jako jsou ty mezi UPF a jedním uživatelským zařízením) neefektivní a nedostatečné. Účelem MBSSF je poskytnout standardizovanou, škálovatelnou a bezpečnou metodu pro správu klíčů a řízení přístupu pro potenciálně obrovské množství příjemců.

Řeší problém bezpečné distribuce klíčů pro broadcastové skupiny. Bez specializované funkce, jako je MBSSF, by síť musela s každým uživatelským zařízením pro stejný obsah vytvářet individuální bezpečnostní kontexty, což by plýtvalo signalizačními prostředky a komplikovalo synchronizované aktualizace klíčů. Předchozí bezpečnost MBMS ve 4G používala pro podobné funkce BM-SC, ale MBSSF je přepracována jako nativní síťová funkce 5G Core na bázi služeb, která se integruje s novým autentizačním rámcem a možnostmi síťového řezání.

Motivací pro její specifikaci ve vydání Release 17 bylo rozšíření případů užití pro 5G MBS, včetně skupinové komunikace pro kritickou infrastrukturu, veřejné bezpečnosti, aplikací V2X a IPTV. Tyto služby vyžadují robustní zabezpečení, aby se zabránilo odposlechu, krádeži služby a podvržení. MBSSF poskytuje nezbytný základ pro komerční broadcastové služby, kde je ochrana obsahu (Digital Rights Management) prvořadá, a pro služby veřejné bezpečnosti, kde jsou kritická integrita komunikace a skupinová autentizace.

## Klíčové vlastnosti

- Generování a správa hlavního relového klíče (Master Session Key, MSK) pro každou MBS relaci
- Odvození a zabezpečená distribuce uživatelských specifických klíčů (User-specific Key, UK) jednotlivým uživatelským zařízením (UE)
- Podpora ochrany důvěrnosti a integrity multicastového/broadcastového provozu
- Integrace s autentizací 5G jádra (přes UDM) pro autorizaci uživatelských zařízení (UE)
- Procedury pro obnovu, odvolání a synchronizaci klíčů napříč skupinou uživatelů
- Rozhraní na bázi služeb (Nmbsf) pro interakci s ostatními síťovými funkcemi 5G Core

## Související pojmy

- [MBS – Frequency Selection Area Identity](/mobilnisite/slovnik/mbs/)
- [MB-SMF – Multicast/Broadcast Session Management Function](/mobilnisite/slovnik/mb-smf/)

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures

---

📖 **Anglický originál a plná specifikace:** [MBSSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mbssf/)
