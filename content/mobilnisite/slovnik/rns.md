---
slug: "rns"
url: "/mobilnisite/slovnik/rns/"
type: "slovnik"
title: "RNS – Radio Navigation Satellite"
date: 2025-01-01
abbr: "RNS"
fullName: "Radio Navigation Satellite"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rns/"
summary: "Satelitní systém používaný pro služby určování polohy, navigace a času, jako je GPS nebo Galileo, který lze integrovat se sítěmi 3GPP pro služby založené na poloze. Poskytuje uživatelskému zařízení ge"
---

RNS je satelitní systém, jako GPS nebo Galileo, který poskytuje uživatelskému zařízení data o poloze, navigaci a čase pro integraci se sítěmi 3GPP a službami založenými na poloze.

## Popis

Radio Navigation Satellite (RNS) označuje satelitní systémy, které vysílají signály používané k určení polohy, rychlosti a času ([PVT](/mobilnisite/slovnik/pvt/)) na Zemi. V kontextu specifikací 3GPP zahrnuje RNS globální navigační satelitní systémy ([GNSS](/mobilnisite/slovnik/gnss/)), jako jsou [GPS](/mobilnisite/slovnik/gps/) (USA), Galileo (EU), [GLONASS](/mobilnisite/slovnik/glonass/) (Rusko) a BeiDou (Čína), které jsou integrovány do mobilních sítí pro poskytování lokalizačních služeb. Tyto systémy fungují nasazením konstelací satelitů na střední oběžné dráze Země, z nichž každý vysílá přesná časová a orbitální data. Uživatelské zařízení (UE), například smartphone, přijímá signály z více satelitů, vypočítává časové zpoždění pro každý signál a používá trilateraci k výpočtu svých geografických souřadnic s přesností od metrů po centimetry v závislosti na technologii a asistenčních datech.

Integrace RNS do sítí 3GPP zahrnuje několik architektonických komponent a protokolů. UE obsahuje přijímač GNSS schopný zpracovávat satelitní signály, zatímco síť poskytuje asistenční data prostřednictvím protokolů, jako je LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) nebo Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Tato asistenční data, doručovaná z entit jako Enhanced Serving Mobile Location Center ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)), zahrnují informace jako efemeridy satelitů, almanach a časování, což urychluje čas do prvního určení polohy a zlepšuje přesnost, zejména v náročném prostředí, jako jsou městské kaňony. Specifikace 3GPP definují rozhraní a procedury pro asistovaný GNSS (A-GNSS), kde síť pomáhá UE při získávání a zpracování satelitních signálů, čímž snižuje spotřebu energie a zlepšuje výkon.

RNS hraje klíčovou roli ve službách 3GPP, zejména u nouzových volání (např. E911 v USA), kde regulační požadavky nařizují přesné hlášení polohy. Podporuje také komerční aplikace, jako je navigace, geofencing a reklama založená na poloze. V 5G a dalších generacích se integrace RNS rozšiřuje na případy užití, jako je komunikace vozidlo-se-vším (V2X), průmyslový IoT a synchronizace sítě. Specifikace jako 23.271 (Location Services) a 25.305 (Stage 2 functional specification of UE positioning in UTRAN) podrobně popisují požadavky a procedury, zajišťující interoperabilitu mezi satelitními systémy a mobilními sítěmi. Vývoj směrem k hybridnímu určování polohy, které kombinuje RNS s pozemními metodami, jako je OTDOA nebo Wi-Fi, dále zvyšuje spolehlivost a přesnost v různých scénářích.

## K čemu slouží

Systémy Radio Navigation Satellite (RNS) byly začleněny do standardů 3GPP, aby uspokojily rostoucí poptávku po přesných službách založených na poloze v mobilních sítích. Před integrací se mobilní určování polohy spoléhalo primárně na síťové metody, jako je Cell-ID nebo časový posun, které nabízely omezenou přesnost (stovky metrů až kilometry). Jelikož aplikace, jako jsou nouzové služby, navigace a sledování majetku, vyžadovaly přesnější lokalizační data, začlenění satelitního určování polohy tyto limity odstranilo poskytnutím globálního pokrytí a přesnosti na úrovni metrů.

Motivace pro integraci RNS vycházela z regulačních nařízení, jako jsou požadavky FCC na E911 ve Spojených státech, které nutily operátory poskytovat přesné informace o poloze pro nouzová volání. Navíc vzestup smartphonů a aplikací využívajících polohu poháněl komerční potřebu spolehlivého určování polohy. Standardy 3GPP se vyvíjely, aby podporovaly asistovaný GNSS (A-GNSS), kde sítě doručují UE asistenční data ze satelitů, čímž se snižuje čas a energie potřebná pro určení polohy. Tento přístup překonal výzvy, jako je pomalé získávání samostatného GNSS a špatný příjem signálu v interiérech.

Standardizací rozhraní a procedur RNS umožnilo 3GPP interoperabilitu napříč různými satelitními konstelacemi a mobilními technologiemi, od 2G do 5G. Vyřešilo problémy související s přesností, dostupností a energetickou účinností, čímž podpořilo širokou škálu služeb od veřejné bezpečnosti po autonomní řízení. Vývoj pokračuje s pokroky, jako je dvoufrekvenční GNSS a integrace s určováním polohy v 5G NR, což zlepšuje výkon pro budoucí případy užití.

## Klíčové vlastnosti

- Poskytuje globální služby určování polohy, navigace a času
- Integruje se se sítěmi 3GPP prostřednictvím protokolů asistovaného GNSS
- Podporuje více konstelací, jako jsou GPS, Galileo a GLONASS
- Umožňuje přesnost na úrovni metrů až centimetrů s asistenčními daty
- Snižuje čas do prvního určení polohy a spotřebu energie v UE
- Nezbytný pro regulační nouzové služby a komerční aplikace

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TR 23.908** (Rel-5) — Pre-paging in GSM/UMTS networks
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [RNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rns/)
