---
slug: "docsis"
url: "/mobilnisite/slovnik/docsis/"
type: "slovnik"
title: "DOCSIS – Data Over Cable Service Interface Specification"
date: 2025-01-01
abbr: "DOCSIS"
fullName: "Data Over Cable Service Interface Specification"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/docsis/"
summary: "DOCSIS je telekomunikační standard pro přenos dat s vysokou přenosovou rychlostí přes stávající systémy kabelové televize (CATV). Umožňuje kabelovým operátorům poskytovat služby přístupu k internetu,"
---

DOCSIS je telekomunikační standard pro přenos dat s vysokou přenosovou rychlostí přes systémy kabelové televize, který umožňuje přístup k internetu a podporuje konvergenci pevných a mobilních sítí v rámci 3GPP.

## Popis

Data Over Cable Service Interface Specification (DOCSIS) je soubor mezinárodních standardů vyvinutých konsorciem CableLabs a následně přijatých [ITU-T](/mobilnisite/slovnik/itu-t/), který definuje požadavky na rozhraní pro kabelové modemy a podpůrná zařízení. V rámci ekosystému 3GPP je DOCSIS odkazován primárně v kontextu specifikací IP Multimedia Subsystem (IMS), jako je TS 24.229, pro podporu konvergence pevných a mobilních sítí. Poskytuje standardizovanou metodu pro poskytování širokopásmového přístupu k internetu přes hybridní opticko-koaxiální infrastrukturu (HFC), tradičně používanou pro kabelovou televizi. Architektura se skládá z Cable Modem Termination System (CMTS) na ústředně kabelového operátora a Cable Modemu ([CM](/mobilnisite/slovnik/cm/)) u účastníka. Tyto komponenty komunikují přes sdílenou koaxiální síť pomocí rádiových kmitočtových kanálů pro přenos dat ve směru k účastníkovi (downstream) a od účastníka (upstream).

Provoz DOCSIS zahrnuje sofistikované modulační schémata, především kvadraturní amplitudovou modulaci ([QAM](/mobilnisite/slovnik/qam/)), pro kódování digitálních dat na [RF](/mobilnisite/slovnik/rf/) nosné. Downstreamový provoz je vysílán všem modemům ve služební skupině, přičemž jednotlivé modemy filtrují pakety na základě svého jedinečného Service Identifier ([SID](/mobilnisite/slovnik/sid/)). Přístup pro upstream je řízen pomocí schématu Time Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([TDMA](/mobilnisite/slovnik/tdma/)) nebo Synchronous Code Division Multiple Access (S-CDMA), kdy CMTS přiděluje jednotlivým modemům přenosové příležitosti, aby se zabránilo kolizím na sdíleném médiu. Mezi klíčové správní protokoly patří Baseline Privacy Interface Plus (BPI+) pro šifrování a správu klíčů a DOCSIS Set-top Gateway (DSG) pro přenos zpráv mimo základní pásmo k set-top boxům. Quality of Service (QoS) je vynucována pomocí služebních toků, což jsou jednosměrné logické kanály se specifickými charakteristikami provozu, jako je latence, ztrátovost a garantovaná propustnost.

V architektuře 3GPP slouží DOCSIS jako klíčová technologie pevného širokopásmového přístupu, která spolupracuje s mobilními jádrovými sítěmi, zejména pro služby založené na IMS. Umožňuje kabelovým operátorům fungovat jako poskytovatelé internetových služeb ([ISP](/mobilnisite/slovnik/isp/)) a nabízet triple-play služby (hlas, video, data). Tato integrace umožňuje plynulou kontinuitu služeb mezi pevnými a mobilními sítěmi a podporuje scénáře, kdy může být relace uživatele předána mezi přístupovým bodem Wi-Fi založeným na DOCSIS a mobilní sítí. Specifikace prošla několika verzemi, které významně zvýšily kapacitu přenosové rychlosti, zavedly podporu IPv6, vylepšily zabezpečení a umožnily aplikace citlivé na latenci pomocí technologií jako Active Queue Management (AQM) a Low Latency DOCSIS.

## K čemu slouží

DOCSIS byl vytvořen za účelem standardizace vysokorychlostního přenosu dat přes stávající, všudypřítomnou infrastrukturu kabelové televize a její přeměny na obousměrnou širokopásmovou komunikační síť. Před DOCSIS vedly proprietární řešení pro kabelový přístup k internetu k fragmentovaným trhům, problémům s interoperabilitou a vyšším nákladům pro operátory i spotřebitele. Tento standard tyto problémy vyřešil definicí jednotného rozhraní pro kabelové modemy, což umožnilo interoperabilitu mezi výrobci a úspory z rozsahu. To umožnilo kabelovým operátorům rychle zavádět internetové služby, efektivně konkurovat technologii Digital Subscriber Line (DSL) a stát se hlavním hybatelem zavádění širokopásmového připojení v domácnostech.

Z pohledu 3GPP je zařazení odkazů na DOCSIS, například ve specifikacích IMS, motivováno průmyslovým trendem směřujícím ke konvergenci pevných a mobilních sítí (FMC). Jelikož síťoví operátoři usilují o nabídku jednotných služeb napříč pevnou a mobilní doménou, standardizované přístupové technologie jako DOCSIS se stávají nezbytnou součástí celkové architektury poskytování služeb. Řeší omezení čistě mobilních sítí tím, že poskytuje pevný přístup s vysokou kapacitou a nízkými náklady, který může odlehčovat provoz, zlepšovat celkovou efektivitu sítě a poskytovat konzistentní uživatelský zážitek pro služby jako Voice over IP (VoIP) a IPTV. Vývoj DOCSIS průběžně řeší rostoucí poptávku po přenosové rychlosti, aplikace citlivé na latenci a vylepšené zabezpečení, čímž zajišťuje, že zůstává životaschopnou a klíčovou součástí strategií konvergovaných sítí.

## Klíčové vlastnosti

- Standardizované rozhraní pro kabelové modemy a CMTS umožňující interoperabilitu mezi výrobci
- Přenos dat s vysokou přenosovou rychlostí pomocí QAM modulace přes HFC sítě
- Dynamická správa QoS prostřednictvím služebních toků pro triple-play služby
- Integrované zabezpečení s Baseline Privacy Interface Plus (BPI+) pro šifrování
- Podpora adresování IPv4 i IPv6
- Správa upstreamové přenosové rychlosti pomocí přístupových schémat TDMA nebo S-CDMA

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [QAM – Quadrature Amplitude Modulation](/mobilnisite/slovnik/qam/)

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP

---

📖 **Anglický originál a plná specifikace:** [DOCSIS na 3GPP Explorer](https://3gpp-explorer.com/glossary/docsis/)
