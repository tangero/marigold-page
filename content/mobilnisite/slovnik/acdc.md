---
slug: "acdc"
url: "/mobilnisite/slovnik/acdc/"
type: "slovnik"
title: "ACDC – Application specific Congestion control for Data Communication"
date: 2025-01-01
abbr: "ACDC"
fullName: "Application specific Congestion control for Data Communication"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/acdc/"
summary: "ACDC je síťový mechanismus řízení zahlcení, který umožňuje operátorům spravovat pokusy o přístup pro specifické aplikace při síťovém zahlcení. Zabrání přetížení sítě neprioritními aplikacemi pomocí se"
---

ACDC je síťový mechanismus řízení zahlcení, který umožňuje operátorům spravovat pokusy o přístup pro specifické aplikace při síťovém zahlcení aplikací selektivního blokování.

## Popis

Application specific Congestion control for Data Communication (ACDC, řízení zahlcení pro datovou komunikaci specifické pro aplikace) je standardizovaná funkce 3GPP navržená pro poskytnutí detailního, na aplikace zaměřeného řízení zahlcení na úrovni síťového přístupu. Na rozdíl od tradičních metod řízení zahlcení, které uplatňují plošná omezení na veškerý provoz, ACDC funguje tak, že kategorizuje aplikace do odlišných ACDC kategorií a během období síťového zahlcení uplatňuje na základě těchto kategorií mechanismy selektivního řízení přístupu (ACB). Základním principem je umožnit síti upřednostnit pokusy o přístup pro kritické nebo operátorem určené aplikace, zatímco dočasně omezit nebo oddálit pokusy o přístup od méně kritických aplikací, čímž se zmírní zahlcení signalizační a uživatelské roviny a zachová se dostupnost služeb pro případy použití s vysokou prioritou.

Architektura ACDC zahrnuje koordinaci mezi jádrem sítě (CN) a uživatelským zařízením (UE). Síť, konkrétně funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5GC nebo entita správy mobility ([MME](/mobilnisite/slovnik/mme/)) v EPS, je zodpovědná za definici a vysílání parametrů blokování specifických pro ACDC prostřednictvím systémových informačních bloků ([SIB](/mobilnisite/slovnik/sib/)). Tyto parametry, definované pro každou ACDC kategorii, zahrnují faktor blokování a dobu blokování. UE, které je vybaveno ACDC kategorií pro každou ze svých aplikací (typicky prostřednictvím [USIM](/mobilnisite/slovnik/usim/) nebo správy zařízení), tyto vysílané parametry čte. Když aplikace vyvolá žádost o službu (např. pro datovou relaci iniciovanou mobilním zařízením nebo navázání signalizačního spojení), UE vyhodnotí tuto žádost vůči parametrům blokování pro přiřazenou ACDC kategorii dané aplikace. Toto vyhodnocení zahrnuje vygenerování náhodného čísla a jeho porovnání s vysílaným faktorem blokování; pokud je přístup zablokován, UE přejde do časovačem řízeného stavu čekání před opakováním pokusu, čímž efektivně omezí pokusy o přístup od aplikací v zahlcených kategoriích.

Klíčové součásti systému ACDC zahrnují ACDC kategorii, číselný identifikátor (např. 1–16) přiřazený aplikaci; síťově definované parametry blokování pro každou kategorii; a schopnost UE pracovat s ACDC a logiku vynucování pravidel. Chování UE je specifikováno v protokolech jako TS 24.301 ([NAS](/mobilnisite/slovnik/nas/)) a TS 36.331 ([RRC](/mobilnisite/slovnik/rrc/)), což zajišťuje standardizovanou interakci s rádiovou přístupovou sítí ([E-UTRAN](/mobilnisite/slovnik/e-utran/), NG-RAN). ACDC přímo nespravuje datový tok nebo kvalitu služeb (QoS) po navázání relace; jeho role je výhradně zaměřena na počáteční fázi řízení přístupu. Funguje jako preventivní filtr na signalizační vrstvě ke zmírnění bouří zahlcení, které mohou být způsobeny obrovským počtem UE současně se pokoušejících o přístup k síti pro neurgentní služby, jako jsou aktualizace sociálních sítí nebo synchronizace na pozadí, během událostí zatěžujících kapacitu sítě.

## K čemu slouží

ACDC bylo vytvořeno, aby řešilo kritický problém signalizačního a přístupového zahlcení v mobilních sítích, zejména během hromadných událostí, nouzových situací nebo výpadků sítě. Před ACDC byly mechanismy řízení zahlcení, jako je Access Class Barring (ACB) a Extended Access Barring ([EAB](/mobilnisite/slovnik/eab/)), relativně hrubými nástroji. ACB mohlo blokovat celé třídy UE (např. na základě typu účastníka) a EAB mohlo cílit na UE nakonfigurovaná pro nízkou prioritu přístupu, ale ani jeden nedokázal rozlišit mezi různými *aplikacemi* běžícími na stejném zařízení. Toto omezení se stalo palčivým s rozšířením chytrých telefonů a aplikací na pozadí, kde jediné UE mohlo generovat četné pokusy o přístup pro nepodstatné služby, což přispívalo k přetížení sítě a potenciálně blokovalo přístup pro kritickou komunikaci, jako jsou nouzová upozornění nebo služby operátora s klíčovým významem.

Historický kontext pro zavedení ACDC ve 3GPP Release 13 byla rostoucí potřeba chytřejšího, více na aplikace zaměřeného řízení sítě. Operátoři potřebovali nástroj k zajištění odolnosti sítě a kontinuity služeb pro aplikace s vysokou hodnotou (např. hlas, IoT alarmové systémy, komunikace pro veřejnou bezpečnost) i při extrémním zatížení. ACDC to řeší posunem paradigmatu řízení zahlcení z modelu zaměřeného na zařízení nebo třídu účastníka na model zaměřený na aplikaci. Umožňuje operátorovi definovat politiky, které například povolí přístup k síti pro bankovní aplikaci nebo službu hlášení z chytrého měřiče, zatímco dočasně zablokují aplikaci pro streamování videa během události zahlcení. Tento cílený přístup zlepšuje celkovou efektivitu sítě, zvyšuje uživatelský komfort pro prioritní služby a poskytuje operátorům mocný nástroj pro politiky směrování provozu a zmírňování zahlcení, čímž tvoří základní prvek pro diferenciaci služeb a přípravy na síťové řezy (network slicing).

## Klíčové vlastnosti

- Řízení přístupu zaměřené na aplikace na základě nakonfigurovaných ACDC kategorií
- Síťově konfigurovatelné parametry blokování (faktor blokování, doba blokování) vysílané pro každou ACDC kategorii
- Vynucování na straně UE, kde zařízení aplikuje pravidla blokování na každou žádost aplikace
- Zpětná kompatibilita a koexistence se staršími mechanismy blokování, jako jsou ACB a EAB
- Podpora pro architektury sítí EPS i 5GS
- Poskytování ACDC kategorií prostřednictvím USIM (EF_ACDC) nebo správy zařízení

## Definující specifikace

- **TS 22.011** (Rel-19) — Service Accessibility Procedures
- **TR 22.818** (Rel-14) — Control of Apps When 3rd Party Servers Have Issues
- **TS 24.105** (Rel-19) — ACDC Management Object Specification
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 25.300** (Rel-19) — UTRA Radio Interface Enhancements Overview
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [ACDC na 3GPP Explorer](https://3gpp-explorer.com/glossary/acdc/)
