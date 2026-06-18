---
slug: "map"
url: "/mobilnisite/slovnik/map/"
type: "slovnik"
title: "MAP – Mobile Application Protocol"
date: 2025-01-01
abbr: "MAP"
fullName: "Mobile Application Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/map/"
summary: "Signalizační protokol jádra sítě používaný pro komunikaci mezi síťovými prvky jako HLR, VLR a MSC v sítích GSM, UMTS a raných LTE. Umožňuje správu dat účastníka, služby mobility (jako aktualizace polo"
---

MAP je signalizační protokol jádra sítě používaný pro komunikaci mezi prvky, jako jsou HLR a MSC, který umožňuje správu dat účastníka, služby mobility a doplňkové služby v sítích GSM, UMTS a raných LTE.

## Popis

Protokol Mobile Application Protocol (MAP) je klíčový signalizační protokol v rámci jádra sítě (CN) systémů GSM, UMTS a raných LTE, který funguje nad protokolovými zásobníky [SS7](/mobilnisite/slovnik/ss7/) (Signaling System No. 7) a později SIGTRAN (Signaling Transport). Umožňuje komunikaci mezi různými síťovými uzly v doméně s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) a paketů ([PS](/mobilnisite/slovnik/ps/)), především pro správu mobility, manipulaci s daty účastníka a poskytování služeb. MAP je aplikační protokol, který pro svůj transport využívá Transaction Capabilities Application Part ([TCAP](/mobilnisite/slovnik/tcap/)), což umožňuje strukturované dialogy mezi síťovými entitami. Jeho operace jsou definovány prostřednictvím souboru MAP služeb a přidružených Application Service Elements (ASEs), které jsou vyvolávány pomocí specifických MAP operací a parametrů přenášených v rámci komponent TCAP.

Z architektonického hlediska jsou MAP rozhraní definována mezi klíčovými síťovými prvky. Nejvýznamnější je rozhraní MAP-D mezi Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)), které zajišťuje aktualizace polohy, načítání dat účastníka a autentizaci. Rozhraní MAP-C spojuje HLR s Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro směrovací informace během hovorů ukončovaných na mobil. Rozhraní MAP-G mezi VLR podporuje aktualizace polohy mezi VLR, když se účastník pohybuje mezi různými oblastmi VLR. V doméně s přepojováním paketů rozhraní MAP-Gr mezi HLR a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) spravuje data účastníka GPRS a informace o poloze. MAP zprávy přenášejí kritické informace jako International Mobile Subscriber Identity (IMSI), Mobile Station Integrated Services Digital Network Number (MSISDN) a různé profily služeb účastníka.

Role MAP je ústřední pro umožnění funkcí jádra sítě. Pro správu mobility podporuje procedury jako aktualizace polohy, která informuje HLR o aktuálně obsluhujícím VLR nebo SGSN účastníka, a předání hovoru (handover), kde může být zapojen přenos kontextu účastníka. Pro správu dat účastníka umožňuje VLR nebo SGSN načíst autentizační triplety a profily služeb účastníka z HLR. Pro doplňkové služby podporuje aktivaci, deaktivaci a dotazování na služby jako přesměrování hovoru a zákazy. Návrh protokolu je stavový a transakčně orientovaný, což zajišťuje spolehlivou výměnu informací klíčových pro provoz sítě a zkušenost účastníka. Ačkoli byl v podstatě nahrazen protokoly založenými na Diameteru v 4G EPC a 5G Core pro nativní funkce, MAP zůstává životně důležitý pro interoperabilitu se staršími 2G/3G sítěmi a pro některé služby.

## K čemu slouží

MAP byl vytvořen, aby poskytl standardizovaný, robustní signalizační mechanismus pro správu mobility a služeb v digitálních celulárních sítích, počínaje GSM. Před jeho zavedením chybělo celulárním systémům jednotné, interoperabilní protokolové řešení pro komunikaci mezi síťovými prvky různých výrobců, což bránilo rozsáhlému nasazení a roamingu. MAP tento problém vyřešil definováním komplexní sady operací pro kritické funkce, jako je sledování polohy účastníka, ověřování uživatelů a správa směrování hovorů, které jsou nezbytné pro umožnění automatického roamingu a celostátní (a později mezinárodní) celulární služby.

Protokol řešil základní potřebu sítě udržovat konzistentní přehled o stavu a poloze mobilního účastníka při jeho pohybu. Umožnil, aby HLR domovské sítě bylo centrální úložiště dat účastníka, zatímco prvky navštívené sítě (VLR, MSC) mohly dočasně ukládat potřebné informace pro obsluhu účastníka. Toto oddělení odpovědností mezi domovskou a navštívenou sítí bylo klíčové pro uzavírání roamingových dohod mezi operátory. MAP také poskytl rámec pro zavádění pokročilých doplňkových služeb (jako čekání na hovor, přesměrování) standardizovaným způsobem napříč různými síťovými implementacemi.

Jak se sítě vyvíjely z GSM přes UMTS k raným LTE, účel MAP se rozšířil o podporu služeb s přepojováním paketů prostřednictvím rozhraní k uzlům sítě GPRS. Stal se spojovacím článkem mezi jádry s přepojováním okruhů a paketů, což umožnilo koordinovanou správu mobility a služeb. Jeho závislost na zásobníku SS7 však představovala omezení ve světě orientovaném na IP, což vedlo k jeho postupnému vytlačování ve prospěch protokolu Diameter v Evolved Packet Core (EPC). Nicméně, konstrukční principy MAP pro mobilitu účastníka a správu dat hluboce ovlivnily pozdější protokoly.

## Klíčové vlastnosti

- Umožňuje komunikaci mezi HLR, VLR, MSC a SGSN pro správu mobility a služeb
- Podporuje kritické procedury jako aktualizace polohy, předání hovoru a autentizaci účastníka
- Přenáší identifikátory účastníka (IMSI, MSISDN) a profily služeb přes síťová rozhraní
- Poskytuje operace pro řízení doplňkových služeb (např. aktivace přesměrování hovoru)
- Využívá TCAP nad SS7 nebo SIGTRAN pro spolehlivou, transakčně orientovanou signalizaci
- Umožňuje roaming tím, že navštíveným sítím dovoluje dotazovat se na data účastníka v domovské síti

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 26.565** (Rel-19) — Split Rendering Media Service Enabler
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [MAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/map/)
