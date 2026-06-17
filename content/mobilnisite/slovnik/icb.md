---
slug: "icb"
url: "/mobilnisite/slovnik/icb/"
type: "slovnik"
title: "ICB – Incoming Calls Barred (within the CUG)"
date: 2026-01-01
abbr: "ICB"
fullName: "Incoming Calls Barred (within the CUG)"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/icb/"
summary: "Doplňková služba, která umožňuje účastníkovi v rámci uzavřené skupiny uživatelů (CUG) zakázat příchozí hovory z vnějšku skupiny. Vynucuje skupinové soukromí a řízenou komunikaci, čímž zajišťuje, že js"
---

ICB je doplňková služba, která umožňuje účastníkovi v rámci uzavřené skupiny uživatelů (CUG) zakázat příchozí hovory z vnějšku skupiny, čímž vynucuje soukromí a zajišťuje, že jsou přijímány pouze autorizované interní hovory.

## Popis

Incoming Calls Barred (ICB) je doplňková služba definovaná v rámci standardů 3GPP, která funguje ve spojení se službou Uzavřené skupiny uživatelů ([CUG](/mobilnisite/slovnik/cug/)). Slouží jako mechanismus řízení hovorů, který zabraňuje účastníkovi, který je členem CUG, přijímat příchozí hovory pocházející od čísel mimo tuto předem definovanou skupinu. Službu zřizuje a spravuje síťový operátor, obvykle v rámci Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) jako součást profilu služeb účastníka. Při pokusu o hovor na účastníka s aktivní službou ICB dotazovací [MSC](/mobilnisite/slovnik/msc/) nebo funkce řízení relace zkontroluje data účastníka. Pokud volající není členem stejné CUG, je hovor zakázán a volajícímu může být přehrána hláška nebo tón oznamující toto omezení.

Architektonická implementace zahrnuje uzly jádra sítě odpovědné za řízení hovorů a správu dat účastníků. V okruzově spínaných doménách spolupracuje Mobile Switching Center (MSC) s HLR při ověřování členství v CUG a stavu ICB během navazování hovoru. V IP Multimedia Subsystem (IMS) použije Serving-Call Session Control Function (S-CSCF) počáteční filtrační kritéria, která mohou aktivovat servisní logiku (často prostřednictvím Application Serveru ([AS](/mobilnisite/slovnik/as/))), aby vynutila zákaz na základě profilu účastníka načteného z HSS. Servisní logika porovná identitu volající strany (např. [MSISDN](/mobilnisite/slovnik/msisdn/)) se seznamem autorizovaných členů CUG asociovaných s volanou stranou.

Klíčové komponenty zahrnují předplatitelská data CUG, která obsahují index CUG a přidružený interlock kód, a indikátor ICB v rámci těchto dat. Síť tyto informace používá k provedení kontroly členství. Služba je nedílnou součástí poskytování přizpůsobených komunikačních služeb pro podniky, vládní agentury nebo jakékoli organizace vyžadující řízený přístup. Zajišťuje, že komunikace zůstává v rámci důvěryhodného okruhu, čímž zvyšuje bezpečnost a provozní zaměření eliminací nežádoucích nebo externích přerušení, a podporuje tak specializované služby nad rámec standardní veřejné telefonie.

## K čemu slouží

ICB byla vytvořena pro řešení potřeby řízené a soukromé komunikace v rámci specifických skupin uživatelů, což je požadavek výrazný v obchodním a organizačním kontextu. Před existencí takových služeb mobilní sítě primárně nabízely veřejné, neomezené volání, což bylo nedostatečné pro subjekty potřebující vynutit pouze interní komunikaci z důvodů bezpečnosti, kontroly nákladů nebo provozní efektivity. Samotný koncept Uzavřené skupiny uživatelů ([CUG](/mobilnisite/slovnik/cug/)) byl vyvinut pro emulaci funkcionality privátní telefonní ústředny (PBX) na veřejných mobilních sítích a ICB slouží jako kritická komponenta k vynucení 'uzavřené' povahy omezením příchozího přístupu.

Služba řeší problém nežádoucích externích hovorů, které narušují skupinové aktivity nebo ohrožují důvěrnost. Například společnost může nasadit mobilní telefony pro terénní pracovníky, které by měly přijímat hovory pouze od kolegů nebo ústředny, nikoli od osobních kontaktů nebo externích klientů na toto číslo. Toto omezení předchozích přístupů – kdy byly všechny příchozí hovory povoleny, pokud nebyly individuálně blokovány – vyžadovalo skupinové, spravovatelné řešení. ICB jako součást sady služeb CUG poskytla standardizovaný, síťově-centrický mechanismus pro efektivní implementaci takových politik napříč velkými bázemi účastníků, což usnadnilo adopci mobilních služeb pro korporátní zákazníky a zvýšilo příjmy síťových operátorů prostřednictvím služeb s přidanou hodnotou.

## Klíčové vlastnosti

- Omezuje příchozí hovory pouze na ty, které pocházejí ze stejné Uzavřené skupiny uživatelů (CUG)
- Síťově vynucený zákaz aplikovaný během navazování hovoru na základě profilu účastníka
- Integruje se s HLR/HSS pro správu dat účastníků a autorizaci služeb
- Podporuje jak okruzově spínané, tak IMS-based architektury řízení hovorů
- Poskytuje standardizovaný mechanismus pro skupinové soukromí a řízenou komunikaci
- Funguje jako doplňková služba, kterou lze kombinovat s dalšími funkcemi CUG, jako je přístup pro odchozí hovory

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 23.085** (Rel-19) — Closed User Group (CUG) Supplementary Service Stage 2
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- **TS 24.411** (Rel-8) — ACR and CB Service Protocol Specification
- **TS 24.454** (Rel-8) — Closed User Group (CUG) Protocol Specification
- **TS 24.607** (Rel-19) — OIP and OIR Supplementary Services Stage 3
- **TS 24.611** (Rel-19) — Anonymous Communication Rejection & Barring
- **TS 24.654** (Rel-19) — Closed User Group (CUG) supplementary service
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.292** (Rel-19) — IMS Centralized Services (ICS) Interworking
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [ICB na 3GPP Explorer](https://3gpp-explorer.com/glossary/icb/)
