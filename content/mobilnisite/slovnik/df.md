---
slug: "df"
url: "/mobilnisite/slovnik/df/"
type: "slovnik"
title: "DF – Delivery Function"
date: 2025-01-01
abbr: "DF"
fullName: "Delivery Function"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/df/"
summary: "Delivery Function (DF) je síťový prvek zodpovědný za správu a doručování obsahu, služeb nebo zpráv uživatelskému zařízení (UE). Funguje jako zprostředkovatel mezi poskytovateli služeb a mobilními sítě"
---

DF (Delivery Function) je síťový prvek, který spravuje a doručuje obsah, služby nebo zprávy uživatelskému zařízení (UE) a funguje jako zprostředkovatel mezi poskytovateli služeb a mobilními sítěmi.

## Popis

Delivery Function (DF) je standardizovaná síťová komponenta v architektuře 3GPP, která slouží jako doručovací mechanismus pro různé služby, nejvýznamněji v prostředí služby multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)). Funguje jako specializovaný server, který přijímá obsah od zdrojových aplikací nebo uživatelů, zpracovává jej podle síťových politik a profilů účastníků a následně jej předává příslušnému cíli, kterým může být zařízení jiného uživatele nebo jiný síťový prvek. DF zvládá složitosti doručování napříč potenciálně heterogenními sítěmi, spravuje operace typu store-and-forward (ulož a předej), doručovací hlášení a interoperabilitu mezi různými poskytovateli služeb.

Z architektonického hlediska DF typicky komunikuje s několika dalšími síťovými prvky. V kontextu MMS úzce spolupracuje s MMS Relay/Server (MMS-RS), který funguje jako centrální uzel pro provoz MMS. DF přijímá od MMS-RS zprávy, které je třeba doručit příjemci. Následně určuje optimální cestu doručení, což může zahrnovat dotazování na Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro zjištění stavu účastníka a směrovacích informací. Pro doručení na zařízení příjemce DF komunikuje s Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) a Serving GPRS Support Node (SGSN) v sítích 2G/3G, nebo s Packet Data Network Gateway (PGW) a Serving Gateway (SGW) v sítích 4G/5G, aby zajistil datový přenosový kanál pro přenos obsahu.

Provoz DF zahrnuje několik klíčových procesů. Za prvé provádí překlad a validaci adresy, čímž zajišťuje, že identifikátor příjemce (jako [MSISDN](/mobilnisite/slovnik/msisdn/)) je platný a dosažitelný. Za druhé aplikuje servisní logiku, která může zahrnovat kontrolu doručovacích omezení, úpravu obsahu (např. změnu velikosti obrazu podle možností zařízení příjemce) nebo aktivaci účtovacích událostí. Za třetí spravuje samotný pokus o doručení, řeší opakované pokusy, pokud první pokus selže (např. pokud je zařízení příjemce offline), a spravuje časovače vypršení platnosti. Nakonec generuje a vrací doručovací hlášení zpět do zdrojového systému, čímž potvrzuje úspěšné doručení obsahu nebo udává důvod selhání.

Kritickým aspektem DF je její schopnost podporovat různé metody doručení. Pro okamžité doručení posílá obsah přímo příjemci, když je připojen k síti. Pro odložené doručení může obsah uložit a doručit jej později, když se příjemce stane dostupným, což je základní vlastnost pro asynchronní zprávové služby jako MMS. DF také hraje roli při mezifunkční výměně zpráv, kdy může komunikovat s DF v síti jiného operátora pomocí standardizovaných rozhraní (jako rozhraní MM4 v MMS) za účelem doručení zpráv účastníkům jiných mobilních sítí. To vyžaduje podporu překladu protokolů, zabezpečení (jako vzájemné ověřování) a vypořádání mezi operátory.

## K čemu slouží

Delivery Function (DF) byla vytvořena, aby řešila potřebu spolehlivého, standardizovaného mechanismu pro doručování obsahu a zpráv v paketově přepínaných mobilních sítích, zejména když se služby vyvíjely za hranice jednoduchých hlasových hovorů a SMS. Před její standardizací existovala proprietární řešení pro doručování obsahu, což vedlo k problémům s interoperabilitou mezi různými síťovými dodavateli a mobilními operátory. Toto roztříštění bránilo rozvoji rozšířených, spolehlivých služeb s přidanou hodnotou. DF jako součást servisní architektury 3GPP poskytla společný rámec, který zajišťoval, že obsah z jakékoli kompatibilní aplikace může být doručen jakémukoli účastníkovi v jakékoli kompatibilní síti, a tím podpořila globální ekosystém pro mobilní datové služby.

Její zavedení spolu s 3GPP Release 4 bylo úzce spojeno se specifikací služby multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)), která byla koncipována jako nástupce SMS. MMS vyžadovala schopnost doručovat větší multimediální zprávy (obrázky, audio, video), které stávající infrastruktura SMS nezvládala. Na rozdíl od store-and-forward mechanismu SMS v SMSC potřeboval MMS sofistikovanější doručovací mechanismus, který by zvládal různé typy obsahu, přizpůsobil se možnostem zařízení, spravoval datové relace a poskytoval podrobná doručovací hlášení. DF tuto roli splnila, oddělila logiku doručení od jádra zprávové aplikace a umožnila efektivní využití síťových zdrojů.

Dále DF řešila problém asynchronního doručování v síti, kde uživatelé nejsou vždy připojeni. Mobilní datová připojení v raných sítích 3G nebyla vždy "always-on". Schopnost DF typu store-and-forward zajišťovala, že zprávy nebyly ztraceny, když byl příjemce offline, a pokoušela se o doručení při opětovném připojení zařízení. Také řešila účtování a vynucování politik integrací s fakturačními systémy a aplikací pravidel definovaných operátorem před doručením obsahu, což umožňovalo kontroly kreditu u předplacených služeb, filtrování obsahu a rozdílné zacházení se službami. Díky tomu byly komerční, zpoplatněné služby pro operátory realizovatelné a spravovatelné.

## Klíčové vlastnosti

- Doručování zpráv typu store-and-forward pro asynchronní komunikaci
- Spolupráce s prvky jádra sítě (HLR/HSS, GGSN/PGW) pro zjištění stavu účastníka a směrování
- Podpora úpravy obsahu na základě možností zařízení příjemce
- Generování a správa podrobných hlášení o stavu doručení
- Integrace s účtovacími systémy pro fakturaci služeb a kontroly předplaceného kreditu
- Komunikace mezi operátory prostřednictvím standardizovaných rozhraní (např. MM4)

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 31.131** (Rel-19) — C Language Binding for (U)SIM API
- **TS 31.829** (Rel-13) — ISIM Conformance Requirements Technical Report
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 34.131** (Rel-19) — SIM API C Language Test Specification

---

📖 **Anglický originál a plná specifikace:** [DF na 3GPP Explorer](https://3gpp-explorer.com/glossary/df/)
