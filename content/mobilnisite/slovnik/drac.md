---
slug: "drac"
url: "/mobilnisite/slovnik/drac/"
type: "slovnik"
title: "DRAC – Dynamic Resource Allocation Control"
date: 2025-01-01
abbr: "DRAC"
fullName: "Dynamic Resource Allocation Control"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/drac/"
summary: "Dynamic Resource Allocation Control (DRAC) je algoritmus správy rádiových prostředků (RRM) pro UMTS (WCDMA), který v reálném čase spravuje přidělování a uvolňování rádiových prostředků pro uplink a do"
---

DRAC je algoritmus správy rádiových prostředků v UMTS, který dynamicky přiděluje výkon a kódy pro uplink a downlink v reálném čase za účelem optimalizace kapacity sítě a kvality služeb na základě provozu, stavu kanálu a zatížení.

## Popis

Dynamic Resource Allocation Control (DRAC) je základní funkce správy rádiových prostředků (RRM) definovaná pro UMTS Terrestrial Radio Access Network (UTRAN) ve specifikacích 3GPP. Funguje v rámci Radio Network Controller (RNC) a spravuje přidělování kritických, sdílených rádiových prostředků na rozhraní vzduch-vzduch: vysílacího výkonu a kanalizačních kódů ([OVSF](/mobilnisite/slovnik/ovsf/) kódů). DRAC je zodpovědný za nastavení, modifikaci a uvolnění těchto prostředků pro vyhrazené kanály ([DCH](/mobilnisite/slovnik/dch/)) přidělené uživatelskému zařízení (UE) pro přenos přepojovaných okruhů ([CS](/mobilnisite/slovnik/cs/)) a přepojovaných paketů (PS). Jeho činnost je kontinuální a dynamická, reagující na změny několika klíčových vstupů.

Algoritmus funguje tak, že vyhodnocuje požadavky na prostředky (např. z procedury Radio Bearer Setup nebo Radio Bearer Reconfiguration) vůči aktuálnímu stavu buňky. Mezi klíčové vstupy patří naměřené rušení na uplinku (Rise Over Thermal - RoT), vysílací výkon na downlinku, dostupný prostor stromu kanalizačních kódů a parametry QoS požadované služby (např. garantovaný bitový tok, třída provozu). Pro uplink DRAC primárně řídí maximální povolený výkon pro UE, což přímo omezuje jeho datový tok. Pro downlink spravuje přidělování OVSF kódů a výkonový rozpočet pro každé spojení. Jádrem rozhodovací logiky je řízení přístupu (admission control) a řízení zahlcení (congestion control). Řízení přístupu rozhoduje, zda lze nový požadavek povolit bez porušení stability nebo QoS stávajících spojení. Řízení zahlcení (nebo řízení zatížení) aktivně monitoruje buňku a může spustit snížení prostředků pro stávající uživatele, pokud zatížení (rušení nebo výkon) překročí předdefinované prahové hodnoty.

Implementace DRAC je úzce spojena s dalšími funkcemi RRM, jako je Packet Scheduler (PS), který zpracovává prostředky sdílených kanálů ([HSDPA](/mobilnisite/slovnik/hsdpa/)/[HSUPA](/mobilnisite/slovnik/hsupa/)), a Handover Control. Pro služby na vyhrazených kanálech může DRAC spolupracovat s výběrem Transport Format Combination (TFC) v UE, kde UE volí datový tok (transportní formát), který nepřekračuje prostředky přidělené RNC prostřednictvím DRAC. Tato dynamická a reaktivní regulační smyčka je zásadní pro správu povahy WCDMA, která je limitována rušením, zajišťuje stabilitu systému, maximalizuje spektrální účinnost a poskytuje dohodnutou QoS koncovým uživatelům za různých podmínek v síti.

## K čemu slouží

DRAC byl vytvořen k řešení základní výzvy správy prostředků v sítích UMTS založených na WCDMA, které jsou inherentně limitovány rušením a používají sdílené vyhrazené kanály s proměnnou rychlostí. Na rozdíl od přidělování založeného na časových slotech v GSM jsou prostředky WCDMA (výkon a kódy) kontinuální a sdílené všemi uživateli, což činí jejich správu složitou. Primární problém, který DRAC řeší, je efektivní a stabilní využití těchto sdílených prostředků při zároveň garantování Quality of Service (QoS) pro různé třídy provozu (konverzační, streamovací, interaktivní, na pozadí).

Před takovou dynamickou kontrolou by byly jednodušší statické nebo polostatické metody přidělování vysoce neefektivní, buď by plýtvaly kapacitou nadměrným poskytováním, nebo by způsobovaly degradaci služeb a přerušení hovorů při zahlcení. Dynamická povaha DRAC byla motivována potřebou efektivně podporovat trhavý paketový datový provoz. Umožňuje síti rychle přidělit vysoké prostředky, když je uživatel aktivní (např. stahuje soubor), a rychle je snížit nebo uvolnit během období nečinnosti, čímž uvolní kapacitu pro ostatní uživatele. To je klíčové pro zisk ze statistického multiplexování. Navíc díky kontinuálnímu monitorování rušení na uplinku (RoT) DRAC chrání buňku před nestabilitou – situací, kdy rostoucí rušení způsobí, že všechna UE zvýší výkon, což vede k nekontrolovatelnému efektu „dýchání buňky“ nebo kolapsu. Poskytuje nezbytnou zpětnou vazbu v reálném čase k udržení sítě v jejím plánovaném provozním rozsahu.

## Klíčové vlastnosti

- Přidělování a uvolňování výkonu pro uplink a OVSF kódů pro downlink v reálném čase
- Řízení přístupu (Admission Control) pro přijetí nebo odmítnutí nových požadavků na rádiový bearer na základě zatížení buňky
- Řízení zahlcení/zatížení (Congestion/Load Control) pro snížení přidělených prostředků během vysokého rušení nebo výkonových podmínek
- Správa prostředků s ohledem na QoS pro různé třídy provozu
- Interakce s řízením Transport Format Combination (TFC) v UE
- Základní prvek pro správu rušení a stability v sítích WCDMA

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [DRAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/drac/)
