---
slug: "bfi"
url: "/mobilnisite/slovnik/bfi/"
type: "slovnik"
title: "BFI – Bad Frame Indication"
date: 2025-01-01
abbr: "BFI"
fullName: "Bad Frame Indication"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bfi/"
summary: "BFI je signál z rádiové podsystémové vrstvy indikující, že přijatý řečový rámec obsahuje neopravitelné chyby. Umožňuje řečovému dekodéru aplikovat techniky maskování chyb k zakrytí přenosových chyb, č"
---

BFI je signál indikující, že přijatý řečový rámec obsahuje neopravitelné chyby, což umožňuje řečovému dekodéru aplikovat maskování chyb pro udržení kvality hlasu při špatných rádiových podmínkách.

## Popis

Bad Frame Indication (BFI) je kritický řídicí signál generovaný v rámci rádiové podsystémové vrstvy ([RSS](/mobilnisite/slovnik/rss/)) mobilní sítě, konkrétně při zpracování řečových rámců na rádiovém rozhraní. Když je řečový rámec přijat přes rozhraní vzdušného přenosu, fyzická vrstva provádí detekci chyb pomocí mechanismů cyklického redundantního součtu ([CRC](/mobilnisite/slovnik/crc/)). Pokud CRC indikuje, že rámec obsahuje chyby, které nelze opravit technikami dopředné korekce chyb ([FEC](/mobilnisite/slovnik/fec/)), RSS vygeneruje signál BFI, aby označil tento rámec jako nespolehlivý.

Z architektonického hlediska BFI vzniká ve fyzické vrstvě zpracování základnové stanice a je předáván směrem vzhůru přes protokolový zásobník k řečovému kodeku. V systémech GSM to zahrnuje rozhraní [TRAU](/mobilnisite/slovnik/trau/) (Transcoder and Rate Adaptation Unit), kde je bit BFI explicitně signalizován. Pro UMTS a novější systémy je BFI přenášen přes rozhraní Iub mezi Node B a [RNC](/mobilnisite/slovnik/rnc/), vestavěný v rámcích dat rámcového protokolu. Signál BFI typicky sestává z jednoho nebo více bitů, které indikují kvalitativní stav přidruženého řečového rámce.

Když řečový dekodér přijme rámec označený BFI, aktivuje algoritmy maskování chyb namísto pokusu o přímé dekódování poškozených řečových parametrů. Tyto algoritmy využívají informace z dříve správně přijatých rámců k odhadu chybějících nebo poškozených řečových parametrů. Mezi běžné techniky patří substituce tvaru vlny, při které dekodér opakuje parametry předchozího dobrého rámce s příslušným útlumem, nebo interpolace parametrů, při které dekodér plynule přechází mezi okolními dobrými rámci. Účinnost těchto strategií maskování závisí na vzoru chyb rámců a konkrétní implementaci řečového kodeku.

BFI hraje zásadní roli v systému správy kvality hlasu end-to-end. Přesnou identifikací poškozených rámců zabraňuje šíření dekódovacích chyb, které by mohly způsobit slyšitelné artefakty nebo úplná přerušení hlasu. Mechanismus BFI spolupracuje s dalšími ukazateli kvality, jako jsou [RXQUAL](/mobilnisite/slovnik/rxqual/) (přijatá kvalita) a [FER](/mobilnisite/slovnik/fer/) (míra chybovosti rámců), aby poskytl komplexní pohled na kvalitu rádiového spoje. V moderních sítích mohou být informace BFI také využity systémy optimalizace sítě k identifikaci problematických buněk nebo oblastí pokrytí vyžadujících pozornost.

## K čemu slouží

BFI bylo vytvořeno k řešení základní výzvy udržení přijatelné kvality hlasu v mobilních sítích navzdí nevyhnutelným přenosovým chybám. V raných celulárních systémech by byly poškozené řečové rámce dekódovány tak, jak jsou, což vedlo k slyšitelným kliknutím, praskání nebo úplným výpadkům hlasu, které významně degradovaly uživatelský zážitek. Mechanismus BFI poskytuje systematický způsob identifikace nespolehlivých rámců, aby mohly být aplikovány vhodné strategie zmírnění.

Před implementací BFI neměly řečové kodeky spolehlivý způsob, jak rozlišit mezi mírně poškozenými, ale použitelnými rámci a vážně poškozenými rámci, které by měly být zahozeny. To vedlo k nekonzistentní kvalitě hlasu a ztěžovalo implementaci účinného maskování chyb. Zavedení BFI ve 3GPP Release 5 standardizovalo způsob, jakým rádiové podsystémy komunikují informace o spolehlivosti rámců ke komponentám zpracování řeči, což umožnilo konzistentní zpracování chyb napříč různými výrobci síťového zařízení.

Mechanismus BFI řeší problém, jak elegantně degradovat hlasovou službu během dočasného zhoršení rádiového spoje. Označením špatných rámců namísto jejich prostého zahození systém udržuje časovou synchronizaci a integritu sekvence rámců při aplikaci maskování. Tento přístup se ukázal jako obzvláště cenný v situacích předávání hovoru (handover) a na okrajích buněk, kde se rádiové podmínky rychle mění. Standardizovaná signalizace BFI zajistila interoperabilitu mezi rádiovými přístupovými sítěmi a prvky zpracování řeči v jádru sítě, což bylo nezbytné pro úspěšné nasazení více-dodavatelských sítí.

## Klíčové vlastnosti

- Označuje rámce s neopravitelnými chybami CRC
- Umožňuje aktivaci algoritmů maskování chyb
- Udržuje časovou synchronizaci rámců během chyb
- Standardizovaná signalizace napříč síťovými rozhraními
- Funguje s více řečovými kodeky (AMR, AMR-WB, EVS)
- Podporuje monitorování kvality a optimalizaci

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.071** (Rel-19) — AMR Speech Codec Introduction
- **TS 26.091** (Rel-19) — AMR Error Concealment Procedure
- **TS 26.171** (Rel-19) — Introduction to AMR-WB Speech Processing
- **TS 26.191** (Rel-19) — AMR-WB Error Concealment Procedure
- **TS 26.255** (Rel-19) — IVAS Frame Loss Concealment Procedure
- **TS 46.002** (Rel-19) — Introduction to GSM Half-Rate Speech Processing
- **TS 46.021** (Rel-19) — GSM Half Rate DTX Frame Substitution & Muting
- **TS 46.041** (Rel-19) — GSM Half Rate Speech DTX Operation
- **TS 46.051** (Rel-19) — GSM Enhanced Full Rate Speech Processing Intro
- **TS 46.061** (Rel-19) — GSM EFR Frame Substitution and Muting Procedure
- **TS 46.081** (Rel-19) — GSM Enhanced Full Rate DTX Operation
- **TS 46.085** (Rel-19) — GSM Speech Codec Interoperability Test Report

---

📖 **Anglický originál a plná specifikace:** [BFI na 3GPP Explorer](https://3gpp-explorer.com/glossary/bfi/)
