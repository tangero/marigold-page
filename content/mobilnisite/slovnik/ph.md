---
slug: "ph"
url: "/mobilnisite/slovnik/ph/"
type: "slovnik"
title: "PH – Paging Hyperframes"
date: 2025-01-01
abbr: "PH"
fullName: "Paging Hyperframes"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ph/"
summary: "Časová struktura používaná v UMTS a LTE k organizaci příležitostí pro volání (paging occasions) pro UE v režimu nečinnosti. Definuje opakující se cyklus hyperrámců, z nichž každý obsahuje více rámců p"
---

PH (Paging Hyperframes) je opakující se časový cyklus hyperrámců v UMTS a LTE, který organizuje příležitosti pro volání (paging occasions) zařízení v režimu nečinnosti, aby efektivně plánoval zprávy a řídil spotřebu energie pomocí nespojitého příjmu (DRX).

## Popis

Paging Hyperframes (PH) představují základní časově-dělenou strukturu v rádiových přístupových sítích Universal Mobile Telecommunications System (UMTS) a Long-Term Evolution (LTE), speciálně navrženou pro řízení procedury volání (paging) pro uživatelské zařízení (UE) ve stavu nečinnosti nebo inaktivity. Systém je postaven na hierarchickém časovém rámci. Na nejvyšší úrovni je System Frame Number ([SFN](/mobilnisite/slovnik/sfn/)), který cykluje od 0 do 4095. Paging Hyperframe je definován jako souvislá sada těchto rádiových rámců a jeho délka je systémový parametr vysílaný všem UE. V rámci každého hyperrámce jsou specifické rámce určeny jako Paging Frames ([PF](/mobilnisite/slovnik/pf/)). UE vypočítá svůj jedinečný PF na základě svého International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)) a nakonfigurované délky hyperrámce. V rámci PF je jeden nebo více podrámců určeno jako Paging Occasions ([PO](/mobilnisite/slovnik/po/)), během kterých se musí UE probudit, aby sledovalo Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) kvůli Paging Radio Network Temporary Identifier ([P-RNTI](/mobilnisite/slovnik/p-rnti/)). Pokud je P-RNTI detekováno, UE následně čte přidružený Paging Channel ([PCH](/mobilnisite/slovnik/pch-text-pch/)) na Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)), aby přijalo vlastní zprávu volání.

Primární architektonickou rolí PH je umožnit efektivní Discontinuous Reception (DRX). Namísto nepřetržitého sledování downlinku UE většinu času spí a zapíná svůj přijímač pouze během své předem vypočítané Paging Occasion. To drasticky snižuje spotřebu baterie, což je klíčové pro mobilní zařízení. Síť musí sladit vysílání zpráv volání pro konkrétní UE s vypočítanou PO této UE. Struktura hyperrámce poskytuje předvídatelný a škálovatelný vzor pro toto sladění napříč celou populací buněk. Délka PH je klíčový parametr, který vyvažuje latenci volání a úsporu energie UE; delší hyperrámec snižuje frekvenci probouzení (šetří energii), ale zvyšuje maximální dobu, kterou musí síť čekat na zavolání UE (zvyšuje latenci).

Klíčové komponenty zapojené do fungování PH zahrnují vrstvu Radio Resource Control (RRC), která konfiguruje parametry DRX prostřednictvím systémové informace, a fyzickou vrstvu, která zajišťuje samotný příjem během PO. Výpočet je deterministický, což zajišťuje, že jak UE, tak síť nezávisle dojdou ke stejnému PF a PO bez explicitní signalizace pro každou událost volání. V LTE a 5G NR se tento koncept vyvinul do flexibilnějších Paging Frames a Paging Occasions vypočítávaných přímo z SFN a cyklu DRX, ale základní princip časově rozdělených, pro UE specifických vzorů probouzení iniciovaný konceptem hyperrámce zůstává ústřední pro efektivní správu mobility a spojení v režimu nečinnosti.

## K čemu slouží

Mechanismus Paging Hyperframe byl vytvořen, aby vyřešil základní výzvu spojení s mobilním zařízením, jehož přesná poloha a rádiové podmínky nejsou známy, a zároveň zachoval výdrž baterie zařízení. V raných buněčných systémech mohlo jednoduché volání vyžadovat, aby UE poslouchala často, což vedlo k vysoké spotřebě energie. Struktura PH zavádí disciplinovaný, předvídatelný rozvrh pro volání. Umožňuje síti dosáhnout UE, která je v úsporném stavu nečinnosti, a iniciovat procedury jako příchozí hovor (MT call) nebo upozornění UE na změny systémové informace či varování před zemětřesením/tsunami (ETWS/CMAS).

Historicky, jak se sítě vyvíjely od GSM přes UMTS k LTE, počet připojených zařízení exponenciálně rostl, čímž se efektivní volání stalo požadavkem na škálovatelnost. Koncept hyperrámce poskytl matematický rámec pro rovnoměrné rozdělení zatížení voláním v čase, čímž zabránil zahlcení kanálu pro volání. Řeší omezení spočívající v tom, že by všechna UE poslouchala ve stejný čas, což by bylo neefektivní a náchylné ke kolizím. Propojením rozvrhu volání s jedinečným, trvalým identifikátorem jako je IMSI, systém zaručuje rovnoměrné rozdělení UE napříč dostupnými prostředky pro volání, což zajišťuje spolehlivé doručování zpráv a kontrolovanou latenci.

Technologie je motivována dvojím cílem: efektivitou sítě a uživatelským zážitkem. Pro síť umožňuje efektivní využití rádiových prostředků pro řídicí signalizaci. Pro uživatele umožňuje paradigma trvalého připojení bez nutnosti neustále aktivního rádia, což je základním kamenem výdrže baterie moderních smartphonů. Bez takového strukturovaného přístupu k volání by podpora miliard IoT a mobilních zařízení v síti byla nepraktická kvůli signalizačním bouřím a neudržitelným energetickým nárokům zařízení.

## Klíčové vlastnosti

- Definuje opakující se časový cyklus (Hyperframe) pro organizaci událostí volání (paging).
- Umožňuje výpočet specifický pro UE pro Paging Frame (PF) a Paging Occasion (PO) pomocí IMSI.
- Základní pro umožnění Discontinuous Reception (DRX) v režimu nečinnosti.
- Rovnoměrně rozděluje zatížení voláním v čase, aby zabránil zahlcení signalizace.
- Parametry (jako délka hyperrámce) jsou vysílány v systémové informaci pro flexibilní konfiguraci sítě.
- Poskytuje deterministický rozvrh zajišťující sladění mezi probuzením UE a vysíláním volání ze sítě.

## Související pojmy

- [DRX – Discontinuous Reception](/mobilnisite/slovnik/drx/)
- [P-RNTI – Paging Radio Network Temporary Identifier](/mobilnisite/slovnik/p-rnti/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.470** (Rel-19) — F1 Interface Introduction
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [PH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ph/)
