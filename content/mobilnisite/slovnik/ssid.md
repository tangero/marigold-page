---
slug: "ssid"
url: "/mobilnisite/slovnik/ssid/"
type: "slovnik"
title: "SSID – Service Set Identifier"
date: 2026-01-01
abbr: "SSID"
fullName: "Service Set Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ssid/"
summary: "Jedinečný identifikátor, který pojmenovává bezdrátovou lokální síť (WLAN). Je vysílán Wi-Fi přístupovými body, aby klientská zařízení mohla síť objevit a vybrat. V kontextu 3GPP je klíčový pro propoje"
---

SSID je jedinečný identifikátor bezdrátové lokální sítě (WLAN), který je vysílán Wi-Fi přístupovými body, aby umožnil detekci sítě a výběr sítě zařízeními. Je klíčový pro propojení (interworking) 3GPP sítěmi s přístupem mimo 3GPP.

## Popis

Service Set Identifier (SSID) je rozlišující malá a velká písmena, člověkem čitelný řetězec s maximální délkou 32 oktetů (znaků), který slouží jako primární název pro bezdrátovou lokální síť ([WLAN](/mobilnisite/slovnik/wlan/)) založenou na standardech [IEEE](/mobilnisite/slovnik/ieee/) 802.11. V základní sadě služeb ([BSS](/mobilnisite/slovnik/bss/)), která se skládá z jednoho přístupového bodu ([AP](/mobilnisite/slovnik/ap/)) a přidružených stanic, SSID identifikuje tuto konkrétní WLAN. V rozšířené sadě služeb (ESS), zahrnující více AP se stejným SSID, umožňuje klientům roaming mezi AP. SSID je obsažen v rámcích beacon a probe response vysílaných AP, což činí síť detekovatelnou pro skenující klientská zařízení.

V architektuře 3GPP hraje SSID klíčovou roli při propojení mezi 3GPP mobilními sítěmi (např. 4G LTE, 5G) a důvěryhodnými či nedůvěryhodnými přístupovými sítěmi mimo 3GPP, především Wi-Fi. Specifikace jako 3GPP TS 23.234 (WLAN interworking) a TS 24.502 (Access Network Discovery and Selection Function – politiky [ANDSF](/mobilnisite/slovnik/andsf/)) definují, jak se SSID používá pro objevování a výběr sítě. Mobilní zařízení může být vybaveno politikami, které mapují konkrétní SSID na určité síťové chování. Například politika může určovat, že SSID „OperatorSecureWiFi“ je důvěryhodná WLAN, která by měla být použita pro přesměrování provozu (offloading) a může navázat [IPsec](/mobilnisite/slovnik/ipsec/) tunel k důvěryhodné Non-3GPP InterWorking Function ([N3IWF](/mobilnisite/slovnik/n3iwf/)) v 5G jádru.

Proces výběru a ověřování zahrnuje skenování dostupných WLAN uživatelským zařízením (UE), které přijímá jejich vysílaná SSID. UE následně konzultuje svou lokální politiku (např. od ANDSF nebo UE Route Selection Policy – [URSP](/mobilnisite/slovnik/ursp/)), aby zjistilo, zda nalezené SSID odpovídá preferované nebo povolené síti. Pokud je nalezena shoda, UE zahájí ověřovací proceduru. Pro důvěryhodný přístup to typicky zahrnuje EAP-based ověřování (jako EAP-AKA nebo EAP-TLS) s 3GPP jádrovou sítí, přičemž SSID slouží jako klíčový selektor pro správný ověřovací server a kontext síťového řezu (slice). SSID tedy funguje jako kritický spoj mezi fyzickou Wi-Fi sítí a logickým rámcem předplatného a politik 3GPP.

Dále, ve scénářích jako Network Discovery and Selection Function (NSSF) nebo Access Network Discovery and Selection Function (ANDSF), je SSID parametrem v informacích pro objevování sítě poskytovaných UE. Pomáhá UE dělat inteligentní rozhodnutí o výběru přístupu, například přesměrovat video provoz na konkrétní Wi-Fi SSID při zachování hlasového provozu v mobilní síti, nebo vybrat Wi-Fi síť, která poskytuje přístup ke konkrétnímu síťovému řezu. Správa a standardizace použití SSID zajišťuje bezproblémovou mobilitu, kontinuitu relace a integrované ověřování napříč heterogenními rádiovými přístupovými technologiemi.

## K čemu slouží

SSID byl původně definován ve standardu IEEE 802.11, aby vyřešil základní problém identifikace sítě ve sdíleném, nelicencovaném rádiovém spektru. V prostředí s více překrývajícími se WLAN potřebovala zařízení jednoduchý způsob, jak identifikovat a připojit se k zamýšlené síti. SSID poskytl tento člověkem konfigurovatelný název, umožňující uživatelům a zařízením rozlišit mezi „HomeNetwork“, „OfficeWiFi“ a veřejnými hotspoty.

Začlenění SSID do standardů 3GPP bylo hnáno potřebou řízeného propojení mezi mobilními a Wi-Fi sítěmi. Rané přesměrování provozu na Wi-Fi (Wi-Fi offloading) bylo často jednoduchým, neřízeným přímým připojením k internetu, které obcházelo operátorskou jádrovou síť a její služby (jako IMS hlas nebo zabezpečený podnikový přístup). To pro operátory představovalo ztrátu kontroly a příjmů. Tím, že 3GPP standardy začaly zacházet s konkrétními SSID jako s „důvěryhodnými“ přístupovými body, umožnily operátorům rozšířit jejich vrstvu služeb a rámec ověřování přes Wi-Fi.

Tento přístup vyřešil klíčová omezení: Poskytl bezproblémový a bezpečný uživatelský zážitek, kde ověřování pro Wi-Fi mohlo používat stejné přihlašovací údaje založené na SIM kartě jako mobilní síť (pomocí EAP-SIM/AKA/AKA'). Také umožnil politiky řízené směrování provozu, kde operátor mohl určit, která SSID mají být použita pro které typy provozu, což umožňuje inteligentní výběr sítě a vyvažování zátěže. SSID se tak vyvinulo z jednoduchého názvu sítě v rámci ekosystému 3GPP v ukazatel politiky, nezbytný pro realizaci konvergovaných, heterogenních sítí (HetNets) a bezproblémového servisního zážitku požadovaného 5G.

## Klíčové vlastnosti

- Jedinečný identifikátor pro základní nebo rozšířenou sadu služeb WLAN
- Vysílán v rámcích beacon pro pasivní objevování sítě
- Používán v 3GPP politikách pro výběr důvěryhodného/nedůvěryhodného přístupu mimo 3GPP
- Klíčový parametr pro EAP ověřování a výběr síťového řezu
- Umožňuje bezproblémovou mobilitu a kontinuitu relace napříč typy přístupu
- Člověkem čitelný řetězec o délce až 32 bajtů

## Související pojmy

- [WLAN – Wireless Local Area Network](/mobilnisite/slovnik/wlan/)
- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [N3IWF – Non-3GPP access InterWorking Function](/mobilnisite/slovnik/n3iwf/)

## Definující specifikace

- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 24.235** (Rel-12) — I-WLAN Interworking Management Object
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 33.814** (Rel-16) — Security aspects of enhanced Location Services (eLCS)
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [SSID na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssid/)
