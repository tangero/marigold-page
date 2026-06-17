---
slug: "anm"
url: "/mobilnisite/slovnik/anm/"
type: "slovnik"
title: "ANM – Answer Message"
date: 2025-01-01
abbr: "ANM"
fullName: "Answer Message"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/anm/"
summary: "ANM je signalizační zpráva protokolu ISUP používaná v okruhově přepínané telefonii k oznámení, že volaná strana zvedla hovor. Je klíčovou součástí procedur sestavení a ukončení hovoru, umožňuje zaháji"
---

ANM je signalizační zpráva protokolu ISUP používaná v okruhově přepínané telefonii k oznámení, že volaná strana zvedla hovor, což iniciuje fakturaci a alokaci zdrojů pro konverzaci.

## Popis

Zpráva Answer Message (ANM) je specifická zpráva v rámci protokolu Integrated Services Digital Network User Part ([ISUP](/mobilnisite/slovnik/isup/)), který je klíčovou součástí sady Signalizačního systému č. 7 (SS7) používaného v tradičních telefonních sítích veřejné komutované telefonní sítě (PSTN) a v raných mobilních sítích jako GSM. ISUP je zodpovědný za sestavení, správu a ukončení hlasových hovorů přes okruhově přepínané spojení. ANM je odeslána v opačném směru, od cílové ústředny (nebo mobilní ústředny) zpět směrem k ústředně původce, po úspěšném doručení zprávy Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)) a Address Complete Message ([ACM](/mobilnisite/slovnik/acm/)).

Architektonicky je ANM generována ústřednou, která obsluhuje volaného účastníka, jakmile volané zařízení zvedne sluchátko (ve fixní síti) nebo mobilní účastník přijme hovor. Toto generování je spuštěno událostí z přístupové sítě, například zprávou CONNECT v GSM. Zpráva prochází signalizační cestou vytvořenou během sestavování hovoru a informuje každou mezilehlou ústřednu na trase, že hovor byl přijat. To umožňuje těmto ústřednám aktualizovat jejich vnitřní stav hovoru a, což je klíčové, propojit hlasovou přenosovou cestu přes okruhově přepínanou síť, čímž se umožní obousměrný hovor.

Samotná zpráva obsahuje parametry, které identifikují konkrétní hovor pomocí Circuit Identification Code ([CIC](/mobilnisite/slovnik/cic/)) a dalších směrovacích štítků. Její přijetí na ústředně původce je definitivním spouštěčem pro zahájení měření délky hovoru pro fakturační účely. V kontextu specifikací 3GPP je ANM zmíněna v souvislosti s propojením mezi jádrovými sítěmi GSM/UMTS a externími sítěmi PSTN/[ISDN](/mobilnisite/slovnik/isdn/), stejně jako v [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile network Enhanced Logic) pro řízení předplaceného účtování. Zatímco její použití je primárně v legacy okruhově přepínaných doménách, porozumění ANM je nezbytné pro pochopení signalizačních toků, ze kterých moderní IP systémy jako VoLTE a VoNR vycházejí nebo s nimiž spolupracují.

## K čemu slouží

ANM existuje jako spolehlivý signalizační mechanismus v pásmu k potvrzení, že volaná strana přijala telefonní hovor v okruhově přepínané síti. Před standardizovanými signalizačními systémy jako SS7 se dohled nad hovorem (detekce zvednutí, položení) často prováděl pomocí tónů v přenosovém pásmu nebo [DC](/mobilnisite/slovnik/dc/) smyčkového dohledu na fyzických trasách, což bylo méně spolehlivé a funkčně omezené. Protokol [ISUP](/mobilnisite/slovnik/isup/) a konkrétně zpráva ANM vyřešily problém efektivní signalizace mimo přenosové pásmo pro řízení hovorů napříč složitými telekomunikačními sítěmi více dodavatelů.

Její vznik byl motivován potřebou automatizované fakturace a efektivního využití zdrojů. Bez explicitního signálu o přijetí hovoru nemohly sítě přesně určit, kdy fakturovatelná konverzace začala, což vedlo k potenciálním ztrátám příjmů nebo sporům se zákazníky. Dále ANM umožňuje síťovým ústřednám zavázat přenosové zdroje (časový slot nebo okruh) pro hlasový přenos až poté, co je hovor potvrzen jako přijatý, čímž se zabrání plýtvání rezervací zdrojů pro hovory, které nejsou nikdy přijaty. Je základním stavebním kamenem pro vytvoření předvídatelné, fakturovatelné a spolehlivé telefonní služby v globálním měřítku.

## Klíčové vlastnosti

- Signalizuje událost přijetí hovoru v opačném směru v rámci protokolu ISUP
- Spouští start fakturačních časovačů na ústředně původce
- Nařizuje mezilehlým ústřednám propojit hlasovou přenosovou cestu
- Identifikována specifickým kódem typu zprávy v rámci datové jednotky protokolu ISUP
- Obsahuje kritické parametry jako Circuit Identification Code (CIC) pro směrování
- Nezbytná pro řízení předplacených služeb založených na CAMEL v okruhově přepínaných doménách

## Související pojmy

- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [ACM – Association for Computing Machinery](/mobilnisite/slovnik/acm/)
- [IAM – Initial Address Message](/mobilnisite/slovnik/iam/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.087** (Rel-19) — User-to-User Signalling (UUS) Stage 2
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.508** (Rel-8) — TIP and TIR Service Protocol Description
- **TS 24.604** (Rel-19) — Communications Diversion (CDIV) Protocol Spec
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging

---

📖 **Anglický originál a plná specifikace:** [ANM na 3GPP Explorer](https://3gpp-explorer.com/glossary/anm/)
