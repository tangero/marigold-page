---
slug: "w-apn"
url: "/mobilnisite/slovnik/w-apn/"
type: "slovnik"
title: "W-APN – WLAN - APN"
date: 2025-01-01
abbr: "W-APN"
fullName: "WLAN - APN"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/w-apn/"
summary: "W-APN je název přístupového bodu (Access Point Name) používaný speciálně pro směrování datového provozu uživatele mezi mobilním zařízením připojeným přes bezdrátovou lokální síť (WLAN) a paketovou dat"
---

W-APN je název přístupového bodu (Access Point Name) používaný pro směrování datového provozu mezi mobilním zařízením v síti WLAN a paketovou datovou sítí, který identifikuje bránu a službu pro přístup přes Wi-Fi.

## Popis

[WLAN](/mobilnisite/slovnik/wlan/) - [APN](/mobilnisite/slovnik/apn/) (W-APN) je specializovaný název přístupového bodu (Access Point Name) používaný v architekturách 3GPP k zajištění paketové datové konektivity pro uživatelské zařízení (UE), když přistupuje k síti přes ne-3GPP bezdrátovou lokální síť (WLAN), jako je Wi-Fi. APN je klíčový identifikátor v mobilních paketových jádrových sítích; jedná se v podstatě o plně kvalifikovaný název domény ([FQDN](/mobilnisite/slovnik/fqdn/)), který síť používá k určení správné brány paketové datové sítě ([PGW](/mobilnisite/slovnik/pgw/) v 4G/EPC) nebo Packet Gateway ([PGW-U](/mobilnisite/slovnik/pgw-u/)+[PGW-C](/mobilnisite/slovnik/pgw-c/) v 5G) a k výběru konkrétní externí paketové datové sítě ([PDN](/mobilnisite/slovnik/pdn/)), ke které se uživatel chce připojit, jako je internet nebo síť IP Multimedia Subsystem (IMS). Předpona 'W-' explicitně označuje jeho použití pro scénáře přístupu přes WLAN.

Když se UE připojuje k síti přes WLAN, zahrne W-APN do své žádosti o připojení. Tuto žádost obvykle zpracovává důvěryhodná přístupová brána WLAN ([TWAG](/mobilnisite/slovnik/twag/)) nebo v novějších architekturách funkce pro propojení s ne-3GPP sítěmi (N3IWF). Síťový prvek překládá W-APN, aby identifikoval příslušnou PGW/SMF+UPF a přidružený profil služby. Proces překladu zahrnuje dotazování na Domain Name System (DNS) jádrové sítě. Vybraná brána poté vytvoří pro datový provoz uživatele tunel založený na GTP nebo PMIP (např. S2a nebo tunel N3IWF-UPF) a uplatní specifické zásady, pravidla účtování a parametry QoS spojené s daným W-APN.

W-APN je klíčový pro vynucování politik a diferenciaci služeb. Operátorům umožňuje nabízet přes přístup WLAN různé úrovně služeb nebo vyhrazené služební sítě (např. APN pro 'VoWiFi' pro hlasové služby přes Wi-Fi založené na IMS). Funguje v součinnosti s autentizačními mechanismy, jako je EAP-AKA nebo EAP-AKA', aby zajistil zabezpečený přístup. Správa konfigurací W-APN je součástí předplatitelských dat UE uložených na Home Subscriber Server (HSS) nebo Unified Data Management (UDM), což zajišťuje, že uživatelé jsou autorizováni pro služby WLAN, k nimž se pokoušejí přistoupit. Tento mechanismus poskytuje standardizovaný způsob integrace WLAN do servisního rámce mobilního operátora.

## K čemu slouží

W-APN byl vyvinut k řešení výzvy integrace přístupu přes WLAN (Wi-Fi) v nelicencovaném pásmu do ekosystému mobilních sítí 3GPP řízeným a na služby zaměřeným způsobem. Zpočátku bylo WLAN vnímáno jako samostatná, na nejlepší výkon orientovaná technologie přístupu k internetu bez integrace s buněčnými službami. To vedlo k nesouvislému uživatelskému zážitku, kdy se služby jako hlasové hovory nebo zabezpečený podnikový přístup přerušily při přechodu mezi buněčnou sítí a Wi-Fi. Vytvoření W-APN, které je součástí širších standardů 3GPP pro propojení s WLAN (I-WLAN) a později důvěryhodného přístupu WLAN (TWAN), poskytlo standardizovaný identifikátor k překlenutí této mezery.

Jeho účelem je umožnit mobilní jádrové síti identifikovat a uplatňovat stejné sofistikované mechanismy řízení politik, účtování a kontinuity služeb pro přístup přes WLAN, jako to činí pro 3GPP radiový přístup. Před zavedením W-APN byl provoz Wi-Fi často přímo odkloněn na internet bez průchodu operátorovským jádrem, čímž operátor přicházel o přehled a kontrolu. Použitím W-APN může operátor směrovat vybraný provoz přes své jádrové síťové brány, což umožňuje služby jako operátorské Voice over Wi-Fi (VoWiFi), plynulé odkládání provozu a přístup k službám hostovaným operátorem (např. IMS, IPTV). Řešil tak obchodní a technickou potřebu konvergence sítí, což operátorům umožnilo používat Wi-Fi jako komplementární technologii radiového přístupu při zachování kvality služeb, zabezpečení a možností monetizace.

## Klíčové vlastnosti

- Identifikuje cílovou PDN a bránu pro datové relace uživatele zřízené přes přístup WLAN.
- Umožňuje řízení politik a účtování (PCC) pro provoz WLAN prostřednictvím jádrové sítě.
- Podporuje diferenciaci služeb (např. samostatné APN pro internet, IMS, podnikový přístup) přes Wi-Fi.
- Integruje se s autentizačními a bezpečnostními rámci 3GPP (EAP-AKA/AKA').
- Usnadňuje plynulou kontinuitu služeb a řízení provozu mezi 3GPP a WLAN přístupem.
- Konfiguruje se jako součást předplatitelských dat uživatele v HSS/UDM.

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 29.161** (Rel-12) — 3GPP-WLAN Interworking Requirements
- **TS 33.234** (Rel-19) — 3GPP-WLAN Interworking Security

---

📖 **Anglický originál a plná specifikace:** [W-APN na 3GPP Explorer](https://3gpp-explorer.com/glossary/w-apn/)
