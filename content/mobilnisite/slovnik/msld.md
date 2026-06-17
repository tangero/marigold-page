---
slug: "msld"
url: "/mobilnisite/slovnik/msld/"
type: "slovnik"
title: "MSLD – Minimum Security Level Data"
date: 2002-01-01
abbr: "MSLD"
fullName: "Minimum Security Level Data"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/msld/"
summary: "Bezpečnostní mechanismus definovaný ve 3GPP pro zajištění základní úrovně ochrany přenosu dat. Slouží k vynucení povinných bezpečnostních algoritmů a délek klíčů, čímž brání použití slabých nebo kompr"
---

MSLD je bezpečnostní mechanismus 3GPP, který vynucuje povinnou základní úroveň ochrany pro přenos dat tím, že vyžaduje specifické algoritmy a délky klíčů, aby zabránil použití slabých nebo kompromitovaných bezpečnostních nastavení.

## Popis

Minimum Security Level Data (MSLD, data s minimální bezpečnostní úrovní) je bezpečnostní rámec specifikovaný v dokumentu 3GPP TS 23.048. Jeho primární funkcí je stanovit minimální přijatelnou úroveň kryptografické ochrany pro komunikaci v síti. Mechanismus funguje tak, že definuje sadu bezpečnostních algoritmů a příslušných délek klíčů, které jsou považovány za bezpečné a musí je podporovat a používat síťové prvky a uživatelská zařízení (UE). Při vytváření bezpečnostního kontextu, například během procedur autentizace a dohody o klíči ([AKA](/mobilnisite/slovnik/aka/)), síť porovná dostupné bezpečnostní schopnosti UE s nakonfigurovaným MSLD. Pokud UE podporuje pouze algoritmy nebo délky klíčů slabší, než je stanovené minimum, může být spojení odmítnuto nebo omezeno, čímž je zajištěno, že k výměně dat nedojde s použitím nedostatečné bezpečnosti. Toto vynucování typálně zajišťují funkce jádra sítě, jako je Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v Evolved Packet Core (EPC) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G Core, ve spolupráci s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), které mohou pro účastníka uchovávat politiku MSLD. Koncept MSLD je nedílnou součástí strategie obrany v hloubce, neboť poskytuje konfigurovatelnou vrstvu politiky sloužící jako záchranná síť. Brání náhodným nebo úmyslným downgrade útokům, při nichž by útočník mohl vynutit použití zastaralých, prolomených kryptografických sad, jako jsou určité rané šifrovací nebo integritní algoritmy. Stanovením této minimální úrovně mohou operátoři garantovat, že i když novější a silnější algoritmy nejsou všeobecně dostupné, komunikace nikdy neklesne pod předem definovaný bezpečnostní práh, který je revidován a aktualizován s vývojem kryptografického výzkumu.

## K čemu slouží

MSLD byl zaveden, aby řešil kritickou potřebu garantované základní bezpečnostní úrovně v mobilních sítích. S vývojem kryptografických standardů se starší algoritmy stávají zranitelnými vůči novým útokům. Bez povinného minima hrozí, že zařízení nebo starší síťové uzly vyjednají a použijí tato kompromitovaná bezpečnostní nastavení, čímž vytvoří zneužitelné slabiny. Hlavním problémem, který MSLD řeší, je riziko snížení bezpečnostní úrovně. V heterogenní síti se zařízeními různých generací a od různých dodavatelů může proces bezpečnostního vyjednávání vést k výběru nejslabšího společného algoritmu. MSLD slouží jako bod pro vynucování politiky a zajišťuje, že takové vyjednávání nikdy nevyústí v bezpečnostní úroveň, kterou operátor nebo standardizační orgán považuje za nepřijatelnou. Jeho vznik byl motivován rostoucím významem služeb mobilních dat a odpovídajícím nárůstem bezpečnostních hrozeb. Poskytuje operátorům standardizovaný nástroj pro řízení kryptografické flexibility a řízené vyřazování slabých algoritmů, čímž zvyšuje celkovou odolnost sítě proti odposlechu a manipulaci s daty.

## Klíčové vlastnosti

- Vynucuje povinnou minimální sílu kryptografických algoritmů
- Zabraňuje útokům na snížení bezpečnostní úrovně během vyjednávání algoritmů
- Konfigurovatelné operátorem sítě na základě bezpečnostní politiky
- Integruje se s procedurami autentizace a nastavení zabezpečení v jádru sítě
- Může vyvolat odmítnutí spojení, pokud nejsou splněny minimální úrovně
- Napomáhá řízenému vyřazování zastaralých, slabých bezpečnostních algoritmů

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management

---

📖 **Anglický originál a plná specifikace:** [MSLD na 3GPP Explorer](https://3gpp-explorer.com/glossary/msld/)
