---
slug: "isdn"
url: "/mobilnisite/slovnik/isdn/"
type: "slovnik"
title: "ISDN – Integrated Services Digital Network"
date: 2026-01-01
abbr: "ISDN"
fullName: "Integrated Services Digital Network"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/isdn/"
summary: "Soubor komunikačních standardů pro simultánní digitální přenos hlasu, videa, dat a dalších síťových služeb po tradičních telefonních okruzích. V 3GPP je na ISDN odkazováno v souvislosti se zastaralým"
---

ISDN je soubor zastaralých komunikačních standardů pro digitální přenos hlasu, videa a dat po telefonních okruzích, na který se v 3GPP odkazuje pro propojení raných mobilních systémů, jako je GSM.

## Popis

Integrated Services Digital Network (ISDN) je systém telefonní sítě s přepojováním okruhů, který zajišťuje digitální přenos hlasu a dat po běžných měděných telefonních linkách a nabízí lepší kvalitu a vyšší přenosové rychlosti než tradiční analogový systém. V rámci architektury 3GPP není ISDN technologií definovanou 3GPP, ale je klíčovým zastaralým systémem, s nímž byly navrženy pro vzájemné propojení rané sítě GSM a UMTS. Specifikace 3GPP rozsáhle odkazují na protokoly, číslování a koncepty služeb ISDN, aby zajistily bezproblémové vzájemné fungování mezi mobilními sítěmi a pevnou infrastrukturou ISDN. Toto vzájemné fungování je primárně zajišťováno v páteřní síti, konkrétně v doméně s přepojováním okruhů, kde se ústředny mobilního přepojování ([MSC](/mobilnisite/slovnik/msc/)) rozhraní s ústřednami ISDN pomocí signalizačních protokolů, jako je ISDN User Part ([ISUP](/mobilnisite/slovnik/isup/)).

Z architektonického hlediska ISDN definuje dva hlavní typy rozhraní: Basic Rate Interface ([BRI](/mobilnisite/slovnik/bri/)) a Primary Rate Interface (PRI). BRI poskytuje dva 64 kbps přenosové (B) kanály pro hlas nebo data a jeden 16 kbps delta (D) kanál pro signalizaci, což je vhodné pro malé kanceláře nebo rezidenční použití. PRI, typicky používaný pro větší připojení, nabízí 23 B kanálů (30 v Evropě) a jeden D kanál o rychlosti 64 kbps, což dohromady dává 1,544 Mbps (T1) nebo 2,048 Mbps (E1). V kontextu 3GPP páteřní mobilní síť tyto rozhraní emuluje. Například MSC funguje jako ústředna ISDN pro mobilní účastníky a poskytuje služby podobné ISDN, jako jsou hlasové hovory s přepojováním okruhů, fax a doplňkové služby jako přesměrování hovoru a identifikace volajícího. Signalizace mezi MSC a externí sítí ISDN využívá ISUP, který je součástí sady Signalizačního systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)), k navázání, správě a ukončení hovorů.

Jak funguje při vzájemném propojení: Když mobilní účastník uskuteční hovor na pevný ISDN telefon, MSC přijme žádost o hovor prostřednictvím mobilního rádiového rozhraní (např. pomocí signalizace [BSSAP](/mobilnisite/slovnik/bssap/) od základnové stanice). MSC následně tuto žádost přeloží do zprávy ISUP Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)) obsahující číslo volaného účastníka a další parametry, kterou odešle přes síť SS7 na ústřednu ISDN. Ústředna ISDN hovor směruje k cíli. Podobně pro příchozí hovory z ISDN na mobilního účastníka odešle ústředna ISDN zprávu ISUP na MSC, které vyvolá mobilní stanici a naváže rádiový kanál. Po celou dobu hovoru je hlas přenášen přes 64 kbps okruhy (kódované [PCM](/mobilnisite/slovnik/pcm/)) mezi MSC a sítí ISDN. Tento paradigma přepojování okruhů je zrcadleno v části páteřní sítě mobilní sítě s přepojováním okruhů.

Klíčové komponenty při vzájemném fungování 3GPP-ISDN zahrnují MSC, Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)) pro rozhraní s externími sítěmi, Home Location Register (HLR) pro data účastníků a signalizační infrastrukturu SS7 s ISUP. Číslování ISDN, definované v ITU-T E.164, je také použito jako základ pro čísla mobilních účastníků (MSISDN). Dále jsou doplňkové služby ISDN, standardizované v Q.931 (vrstva 3) a souvisejících protokolech, podporovány v 3GPP prostřednictvím Customized Applications for Mobile networks Enhanced Logic (CAMEL) a dalších mechanismů pro poskytování funkcí jako čekání hovoru, hold a zákaz volání. Jak se 3GPP vyvíjelo, význam přímého propojení s ISDN poklesl s nástupem plně IP sítí (IMS a VoLTE), ale zůstává kritický pro zpětnou kompatibilitu, zejména v regionech, kde ISDN stále funguje, a pro zajištění kontinuity služeb během přechodu na sítě s přepojováním paketů.

## K čemu slouží

ISDN byl vyvinut k řešení omezení analogové telefonní sítě, která byla neefektivní pro přenos dat a omezena na hlasové služby. Jeho účelem bylo vytvořit plně digitální síť, která by mohla integrovat hlas, data, text a video po stejných linkách, nabízet vyšší kvalitu, rychlejší časy navazování a větší šířku pásma. Pro telekomunikační průmysl představoval ISDN první krok k digitální konvergenci. V kontextu 3GPP a mobilních sítí bylo účelem odkazování na ISDN zajistit, aby se nové digitální mobilní systémy (počínaje GSM) mohly bezproblémově propojit s existující pevnou digitální infrastrukturou. To bylo nezbytné pro poskytnutí všudypřítomného národního a mezinárodního volání, protože pevná síť byla v mnoha rozvinutých zemích během 90. let a počátku 21. století převážně ISDN.

Problémy, které ISDN řešil, zahrnovaly špatnou kvalitu a nízkou rychlost analogových modemů pro datové hovory, nemožnost používat stejnou linku pro více simultánních služeb a pomalé časy navazování hovorů. Poskytnutím digitální konektivity od konce ke konci umožnil ISDN spolehlivé 64 kbps datové kanály, což bylo revoluční pro vytáčený internet, videokonference a fax. Pro 3GPP byla výzvou navrhnout mobilní systém, který by mohl nabídnout ekvivalentní služby a kvalitu. Přijetím principů ISDN – jako jsou 64 kbps přenosové kanály, číslování E.164 a signalizace ISUP – se mohlo GSM prezentovat jako jen další přístupová síť k jádru ISDN, což zjednodušilo vzájemné fungování a umožnilo mobilním uživatelům přístup ke stejným doplňkovým službám jako pevným účastníkům ISDN.

Historicky sloužil ISDN jako vzor pro jádro s přepojováním okruhů v sítích 2G a 3G. Jeho omezení, jako je nepružnost přepojování okruhů pro trhaný datový provoz a složitost správy samostatných sítí pro hlas a data, však motivovala přesun k plně IP architekturám s přepojováním paketů v 3GPP Release 4 a novějších s IP Multimedia Subsystem (IMS). Navzdory tomuto vývoji zůstává propojení s ISDN specifikováno pro podporu zastaralé konektivity, zejména pro mezinárodní roaming a v oblastech, kde ISDN nebyl zcela vyřazen. Rozsáhlý seznam specifikací 3GPP odkazujících na ISDN, sahající od Release 99 do Release 19, podtrhuje jeho trvalou roli při zajišťování zpětné kompatibility a hladké migrační cesty od služeb s přepojováním okruhů k službám s přepojováním paketů v mobilních telekomunikacích.

## Klíčové vlastnosti

- Poskytuje digitální spojení s přepojováním okruhů od konce ke konci s 64 kbps přenosovými kanály (B kanály)
- Používá samostatné signalizační kanály (D kanály) pro řízení hovoru, což umožňuje rychlejší navazování a pokročilé služby
- Podporuje integrované hlasové, datové a video služby po stejné fyzické lince
- Definuje číslovací plán E.164, který je převzat pro čísla mobilních účastníků (MSISDN)
- Využívá signalizaci ISUP přes SS7 pro řízení hovorů a směrování mezi sítěmi
- Nabízí řadu doplňkových služeb (např. přesměrování hovoru, identifikace volajícího), které jsou zrcadleny v mobilních sítích

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [PSTN – Public Switched Telecommunications Network](/mobilnisite/slovnik/pstn/)

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TR 22.950** (Rel-19) — Feasibility Study on Priority Service
- **TR 22.960** (Rel-4) — UMTS Mobile Multimedia Technical Challenges
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- … a dalších 72 specifikací

---

📖 **Anglický originál a plná specifikace:** [ISDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/isdn/)
