---
slug: "bcie"
url: "/mobilnisite/slovnik/bcie/"
type: "slovnik"
title: "BCIE – Bearer Capability Information Element"
date: 2025-01-01
abbr: "BCIE"
fullName: "Bearer Capability Information Element"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bcie/"
summary: "BCIE je strukturovaný informační prvek v signalizačních protokolech 3GPP, který definuje charakteristiky a požadavky přenosové služby (bearer). Přenáší se během procedur sestavování hovoru a vytváření"
---

BCIE je strukturovaný informační prvek v signalizaci 3GPP, který definuje charakteristiky přenosové služby (bearer). Přenáší se během sestavování hovoru za účelem vyjednání a konfigurace přenosových prostředků mezi síťovými entitami.

## Popis

Bearer Capability Information Element (BCIE) je základní součást signalizace řídicí roviny v sítích 3GPP, primárně definovaná ve specifikaci 24.008 pro vrstvu Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)). Jedná se o strukturovaný datový kontejner, který zapouzdřuje technické parametry potřebné k vytvoření, změně nebo uvolnění přenosové služby (bearer) mezi uživatelským zařízením (UE) a jádrem sítě (CN), nebo přímo mezi síťovými entitami. BCIE je přenášena v klíčových signalizačních zprávách, jako je ACTIVATE PDP CONTEXT REQUEST v [GPRS](/mobilnisite/slovnik/gprs/)/UMTS nebo PDN CONNECTIVITY REQUEST v LTE/5G, což umožňuje vyjednání charakteristik služby ještě před přidělením prostředků uživatelské roviny.

Z architektonického hlediska BCIE funguje na vrstvě NAS, která se nachází nad vrstvou Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Když UE zahájí datovou relaci, vyplní BCIE požadovanými parametry služby a zahrne ji do počáteční NAS zprávy. Tato zpráva je transparentně přenesena přes RRC a rádiovou přístupovou síť k obsluhujícímu uzlu jádra sítě (např. SGSN v UMTS, [MME](/mobilnisite/slovnik/mme/) v LTE, [AMF](/mobilnisite/slovnik/amf/) v 5G). Uzel jádra sítě následně interpretuje BCIE, případně upraví parametry na základě síťových politik a profilů účastníka, a použije tyto informace pro komunikaci s dalšími síťovými funkcemi, jako je Gateway GPRS Support Node (GGSN), Packet Data Network Gateway (PGW) nebo Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), aby přidělil potřebné prostředky.

Vnitřní struktura BCIE je definována řadou standardizovaných identifikátorů informačních prvků ([IEI](/mobilnisite/slovnik/iei/)) a odpovídajících hodnot. Klíčové součásti typicky zahrnují typ přenosové služby (např. paketově přepínaná, okruhově přepínaná), třídu provozu (konverzační, streamovací, interaktivní, na pozadí), maximální a garantované přenosové rychlosti pro uplink i downlink, přenosové zpoždění a indikátory spolehlivosti. V pozdějších vydáních specifikací také zahrnuje parametry pro specifické aplikace, identifikátory třídy kvality služby ([QCI](/mobilnisite/slovnik/qci/)) a 5G indikátory kvality služby (5QI). Prvek používá kódovací formát Type-Length-Value (TLV), což jej činí rozšiřitelným pro nové parametry zaváděné v následujících vydáních 3GPP.

Jeho role v síti je klíčová pro správu kvality služby (QoS) na koncích. Poskytnutím standardizovaného mechanismu pro předání požadavků služby BCIE zajišťuje, že každý síťový segment – od rádiového rozhraní UE přes přenosovou síť až po bránu jádra sítě – může být nakonfigurován s konzistentními parametry. To umožňuje síti implementovat vhodné politiky plánování, řízení přístupu a rezervace prostředků. Dále BCIE usnadňuje diferenciaci služeb, což operátorům umožňuje nabízet datové služby různých úrovní a zajišťuje, že aplikace citlivé na zpoždění, jako je Voice over LTE (VoLTE) nebo hry v reálném čase, získají potřebnou prioritu oproti běžnému best-effort provozu.

## K čemu slouží

BCIE byla vytvořena za účelem řešení základního problému dynamického vytváření přenosových služeb (bearer) se specifickými charakteristikami kvality a výkonu v digitálních celulárních sítích. Před její standardizací v GSM a následným vývojem v rámci 3GPP byly rané mobilní datové služby většinou omezeny na jednoduché, best-effort připojení bez podrobné kontroly nad šířkou pásma, zpožděním nebo spolehlivostí. BCIE zavedla formální, vyjednanou smlouvu mezi uživatelským zařízením a sítí, která přesně specifikovala, jaký druh datového kanálu je požadován. To bylo zásadní pro umožnění širokého portfolia služeb přesahujícího jednoduché prohlížení webu, včetně streamování videa, hlasových hovorů přes paketové sítě (VoIP) a aplikací pro kritické mise, z nichž každá má odlišné síťové požadavky.

Historicky byl její vývoj motivován přechodem od okruhově přepínaných sítí orientovaných na hlas k paketově přepínaným multislužebním sítím ve 2.5G (GPRS) a 3G (UMTS). Tento přechod vyžadoval signalizační mechanismus schopný popsat složité atributy přenosové služby pro podporu současných služeb s různými profily na jediném zařízení. BCIE tento mechanismus poskytla, což síti umožnilo provádět inteligentní řízení přístupu a přidělování prostředků. Řešila tak omezení statického poskytování služeb, kde byly služby předkonfigurovány v síti bez flexibility pro vyjednání na vyžádání a pro každou relaci založenou na potřebách aplikace.

Dále slouží BCIE jako základní kámen interoperability a neutrality vůči výrobcům. Definováním přesné syntaxe a sémantiky pro parametry přenosové služby zajišťuje, že UE od jednoho výrobce může úspěšně požadovat a vytvořit přenosovou službu prostřednictvím síťového zařízení od jiného výrobce. Tím odděluje logiku služby od hardwarové implementace, podporuje konkurenční ekosystém a urychluje inovace. Její rozšiřitelný design také zajistil standardu budoucí odolnost, což umožnilo začlenění nových parametrů (jako jsou parametry pro 5G síťové segmenty nebo ultra-spolehlivou komunikaci s nízkým zpožděním) bez narušení stávajících implementací, čímž podporuje kontinuální vývoj mobilních sítí napříč generacemi.

## Klíčové vlastnosti

- Standardizovaná struktura kódovaná formátem TLV pro rozšiřitelnost a interoperabilitu
- Nese komplexní parametry QoS včetně třídy provozu, přenosových rychlostí a zpoždění
- Přenášena v rámci NAS signalizačních zpráv pro vyjednání přenosové služby na koncích
- Umožňuje dynamické vytváření a modifikaci služeb založených na relaci
- Podporuje současné vytváření více přenosových služeb s různými profily pro jedno UE
- Usnadňuje síťovým uzlům řízení přístupu a vynucování politik

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [BCIE na 3GPP Explorer](https://3gpp-explorer.com/glossary/bcie/)
