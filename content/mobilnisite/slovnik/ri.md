---
slug: "ri"
url: "/mobilnisite/slovnik/ri/"
type: "slovnik"
title: "RI – Roaming Intermediary"
date: 2026-01-01
abbr: "RI"
fullName: "Roaming Intermediary"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ri/"
summary: "Síťová entita nebo funkce, která zprostředkovává roamingové služby mezi domácí sítí a navštívenou sítí. Působí jako prostředník pro autentizaci, autorizaci, účtování a poskytování služeb a zajišťuje b"
---

RI je síťová entita, která zprostředkovává roamingové služby tím, že funguje jako prostředník mezi domácí a navštívenou sítí při autentizaci, autorizaci, účtování a poskytování služeb.

## Popis

Roaming Intermediary (RI) je konceptuální a funkční entita v architektuře 3GPP, která hraje klíčovou roli při umožňování a správě roamingových vztahů mezi mobilními síťovými operátory ([MNO](/mobilnisite/slovnik/mno/)). Nejde o jediný monolitický síťový uzel, ale spíše o soubor funkcí, které mohou být implementovány specializovanými poskytovateli služeb nebo v rámci vlastní infrastruktury operátora. Hlavním účelem RI je stát mezi domácí veřejnou pozemní mobilní sítí ([HPLMN](/mobilnisite/slovnik/hplmn/)) a navštívenou veřejnou pozemní mobilní sítí ([VPLMN](/mobilnisite/slovnik/vplmn/)) a zjednodušovat složité procesy potřebné k tomu, aby účastník mohl využívat služby v cizí síti.

Z architektonického hlediska RI rozhraní s klíčovými síťovými funkcemi v domácí i navštívené síti. Na straně HPLMN komunikuje s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Authentication Centre (AuC) pro ověření přihlašovacích údajů a s fakturačními systémy. Na straně VPLMN se připojuje k Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) v okruhově přepínaných doménách nebo k Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE/5G pro paketově přepínané domény. Činnost RI začíná, když se roamingový účastník pokusí připojit k VPLMN. VPLMN může místo přímého kontaktování HPLMN směrovat požadavek na autentizaci a autorizaci prostřednictvím RI. RI pak tento požadavek proxyuje do příslušných systémů HPLMN, předává odpověď a může provádět překlad mezi různými verzemi protokolů nebo formáty používanými oběma operátory.

Kromě základního připojení RI usnadňuje několik kritických roamingových procesů. Je klíčová pro roamingová rozhraní založená na protokolu Diameter (např. S6a, S8, S9) v Evolved Packet Core (EPC) a 5G Core (5GC). Spravuje zabezpečenou výměnu autentizačních vektorů, dat profilu účastníka a informací o politikách. Dále hraje RI klíčovou roli ve finančním vypořádání tím, že shromažďuje a koreluje záznamy o účtování dat (CDRs/EDRs) z VPLMN, aplikuje dohodnuté tarify a předkládá konsolidované záznamy HPLMN. V pokročilých scénářích může také umožňovat roamingové služby s přidanou hodnotou, jako je směrování roamingu (SoR) k preferovaným partnerským sítím, nebo poskytovat detekci podvodů analýzou vzorců roamingového provozu napříč více VPLMN. Její implementace abstrahuje složitost přímých peer-to-peer spojení, zejména pro operátory se stovkami roamingových partnerů.

## K čemu slouží

Koncept Roaming Intermediary se vyvinul k řešení významných výzev škálovatelnosti, složitosti a nákladů spojených s přímými bilaterálními roamingovými dohodami. V raných celulárních sítích (GSM) vyžadoval roaming přímé signalizační spojení (přes [SS7](/mobilnisite/slovnik/ss7/)) a finanční dohodu mezi každou dvojicí operátorů. Pro operátora s globální působností to znamenalo správu tisíců jednotlivých spojení, každé s vlastní technickou integrací, testováním a komerční smlouvou – vysoce neefektivní model.

RI tyto omezení řeší tím, že funguje jako rozbočovač (hub). Operátor potřebuje navázat pouze jedno robustní spojení k poskytovateli RI, který je naopak připojen ke stovkám dalších operátorů. Tento model hub-and-spoke drasticky snižuje počet potřebných vzájemných propojení. Z technického hlediska řeší problémy interoperability; RI může provádět mediaci protokolů mezi operátory používajícími různé verze 3GPP nebo implementace specifické pro dodavatele. Také zjednodušuje zavádění nových služeb (jako je roaming 4G LTE nebo roaming VoLTE), protože RI může být centrálně upgradována na podporu nových standardů, namísto toho, aby vyžadovala koordinovanou současnou aktualizaci každé dvojice operátorů.

Historicky se potřeba takových zprostředkovatelů stala naléhavou s explozivním růstem globálního roamingu mobilních dat v éře 3G a 4G. Objem signalizace a datového provozu spolu s potřebou řízení politik a účtování v reálném čase učinily přímé propojení (peering) pro mnohé neudržitelným. Model RI, formalizovaný a odkazovaný v četných specifikacích 3GPP napříč mnoha vydáními, poskytl standardizovaný rámec pro provoz těchto poskytovatelů hubů (často nazývaných [GRX](/mobilnisite/slovnik/grx/)/IPX poskytovatelé v kontextu datového roamingu). Umožnil bezproblémový, bezpečný a komerčně životaschopný globální roamingový ekosystém, který máme dnes, podporující vše od hlasu a SMS po vysokorychlostní mobilní broadband a služby IoT.

## Klíčové vlastnosti

- Funguje jako centralizovaný rozbočovač pro signalizaci autentizace a autorizace mezi domácí a navštívenou sítí.
- Poskytuje překlad protokolů a interoperabilitu mezi různými síťovými generacemi a implementacemi dodavatelů.
- Agreguje a zpracovává záznamy o účtování dat (CDRs/EDRs) pro finanční vypořádání mezi operátory.
- Umožňuje směrování roamingu (SoR) ovlivňováním výběru sítě roamingovými účastníky.
- Podporuje služby s přidanou hodnotou, jako je správa podvodů a analýza provozu roamingových účastníků v reálném čase.
- Snižuje provozní složitost správy velkého počtu přímých bilaterálních roamingových dohod.

## Související pojmy

- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [VPLMN – Visited Public Land Mobile Network](/mobilnisite/slovnik/vplmn/)
- [IPX – Internetwork Packet Exchange](/mobilnisite/slovnik/ipx/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.172** (Rel-19) — Service Change and UDI Fallback (SCUDIF)
- **TS 29.573** (Rel-19) — PLMN/SNPN Interconnection Interface Stage 3
- **TS 32.373** (Rel-9) — IRP Security Services CORBA Solution
- **TS 32.376** (Rel-19) — Security services for IRP Solution Set
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.867** (Rel-13) — LTE DL 4 Rx Antenna Port Study TR
- **TS 36.871** (Rel-11) — Downlink MIMO Enhancement for LTE-Advanced
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TS 38.843** (Rel-19) — Study on AI/ML for NR Air Interface
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [RI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ri/)
