---
slug: "msrp"
url: "/mobilnisite/slovnik/msrp/"
type: "slovnik"
title: "MSRP – Multiple Stream Registration Protocol"
date: 2026-01-01
abbr: "MSRP"
fullName: "Multiple Stream Registration Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/msrp/"
summary: "Protokol pro správu relací používaný v IP Multimedia Subsystem (IMS) k navázání a řízení více mediálních toků v rámci jedné multimediální relace. Umožňuje aplikace jako videokonference a přenos soubor"
---

MSRP je protokol pro správu relací používaný v IMS k navázání a řízení více mediálních toků v rámci jedné multimediální relace, což umožňuje aplikace jako videokonference.

## Popis

Multiple Stream Registration Protocol (MSRP) je aplikační protokol definovaný v rámci 3GPP IMS, standardizovaný ve spolupráci s [IETF](/mobilnisite/slovnik/ietf/) (RFC 4975, RFC 4976). Je navržen pro přenos série souvisejících instantních zpráv nebo mediálních bloků, jako jsou soubory nebo text v reálném čase, v rámci navázané IMS relace. MSRP funguje nad spolehlivými transportními protokoly, jako je TCP nebo TLS, přičemž pro navázání a vyjednání relace používá SIP (Session Initiation Protocol), ale pro vlastní přenos objemných dat přechází na MSRP.

MSRP funguje tak, že mezi koncovými body naváže jednu nebo více MSRP relací. Tyto relace jsou logické kanály pro odesílání samostatných zpráv nebo velkého obsahu rozděleného na bloky. Klíčovým mechanismem je použití MSRP URI (Uniform Resource Identifiers) k identifikaci koncových bodů a relací. Během výměny nabídky/odpovědi SIP/SDP (Session Description Protocol) koncové body vyjednají parametry MSRP, jako je cesta, port a přijetí přenosu po blocích. Jakmile je SIP relace navázána, koncové body otevřou přímé TCP (nebo TLS) spojení pro MSRP provoz, nezávisle na signalizační cestě SIP.

V rámci MSRP relace je obsah odesílán v MSRP zprávách přenášených v SDP. Odesílatel může rozložit velký kus obsahu (např. soubor) na více bloků, z nichž každý je odeslán v samostatném požadavku SEND. Příjemce potvrdí každý blok odpovědí 200 OK, čímž zajišťuje řízení toku a spolehlivost. MSRP také podporuje oznámení o doručení pro úspěšný příjem. Protokol zahrnuje mechanismy pro udržování relace (keep-alive), hlášení chyb a řádné ukončení relace. Jeho návrh umožňuje průchod přes Network Address Translators ([NAT](/mobilnisite/slovnik/nat/)) a firewally při použití společně s technikami jako Interactive Connectivity Establishment ([ICE](/mobilnisite/slovnik/ice/)).

## K čemu slouží

MSRP byl vytvořen, aby řešil omezení použití těl SIP zpráv pro přenos velkého množství obsahu nebo nepřetržitého proudu souvisejících instantních zpráv. SIP, ačkoli je výborný pro signalizaci relací, není optimalizován pro přenos objemných dat. Vkládání velkých souborů do požadavků SIP MESSAGE mohlo vést k problémům s výkonem, fragmentaci a obtížím s mezilehlými proxy. MSRP poskytuje pro tento obsah samostatný, efektivnější kanál, což umožňuje SIP soustředit se na řízení relace.

Řeší problém správy více mediálních toků nebo samostatných položek obsahu v rámci jedné multimediální relace. Před MSRP vyžadovaly aplikace jako přenos souborů v rámci chatovací relace nebo videokonference s více toky ad hoc řešení nebo samostatné mechanismy mimo pásmo. MSRP tento proces standardizuje a umožňuje interoperabilní, spolehlivé a vyjednatelné doručování obsahu. Jeho vytvoření bylo motivováno růstem služeb rich communication services (RCS) a IMS multimediálních aplikací vyžadujících více než jen jednoduchou výměnu hlasu nebo jediného obrázku.

## Klíčové vlastnosti

- Spravuje přenos série souvisejících zpráv nebo velkých bloků obsahu
- Pro přenos dat používá spolehlivý transport (TCP/TLS) oddělený od SIP signalizace
- Podporuje přenos po blocích s individuálním potvrzením (200 OK na blok)
- Vyjednává se prostřednictvím SDP v rámci navazování SIP relace
- Zahrnuje mechanismy pro průchod přes NAT/firewally (např. s ICE)
- Poskytuje hlášení o doručení a oznámení o chybách pro odeslaný obsah

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 23.279** (Rel-19) — Combined CS and IMS Services (CSI) Architecture
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.247** (Rel-19) — IMS Messaging Service Protocol Details
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.980** (Rel-19) — Multi-stream Multiparty Conferencing Media Handling
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.311** (Rel-19) — Service Level Interworking for Messaging
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [MSRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/msrp/)
