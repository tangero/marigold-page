---
slug: "anid"
url: "/mobilnisite/slovnik/anid/"
type: "slovnik"
title: "ANID – Access Network Identity"
date: 2025-01-01
abbr: "ANID"
fullName: "Access Network Identity"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/anid/"
summary: "ANID je standardizovaný identifikátor pro konkrétní přístupovou síť v rámci systémů 3GPP i jiných (non-3GPP). Umožňuje síti jednoznačně identifikovat bod připojení pro uživatelské zařízení (UE), což j"
---

ANID je standardizovaný identifikátor pro konkrétní přístupovou síť, který jednoznačně identifikuje uživatelův bod připojení a umožňuje správu mobility, vymáhání politik a kontinuitu služeb napříč různými technologiemi.

## Popis

Identita přístupové sítě (ANID) je klíčový parametr definovaný v dokumentu 3GPP TS 24.302 pro správné objekty (Management Objects) funkce [ANDSF](/mobilnisite/slovnik/andsf/) a související procedury. Slouží jako jednoznačný identifikátor pro přístupovou síť, který umožňuje uživatelskému zařízení (UE) a síti, aby se bez nejasností odkazovaly na konkrétní bod připojení. ANID není jediný, monolitický identifikátor, nýbrž strukturovaný datový typ, který může obsahovat různé typy identit v závislosti na použité přístupové technologii. Pro přístupové sítě 3GPP, jako jsou [GERAN](/mobilnisite/slovnik/geran/), UTRAN nebo [E-UTRAN](/mobilnisite/slovnik/e-utran/), se ANID typicky skládá z mobilního kódu země ([MCC](/mobilnisite/slovnik/mcc/)), mobilního síťového kódu ([MNC](/mobilnisite/slovnik/mnc/)) a kódu lokální oblasti ([LAC](/mobilnisite/slovnik/lac/)) nebo směrovací oblasti (RAC) pro 2G/3G, případně kódu sledovací oblasti (TAC) pro LTE/5G. Pro jiné přístupové sítě (non-3GPP), jako je WLAN, to může být identifikátor sady služeb (SSID), homogenní rozšířený identifikátor sady služeb ([HESSID](/mobilnisite/slovnik/hessid/)) nebo identifikátor domény (realm).

Architektonicky se ANID používá v rámci funkce ANDSF pro usnadnění vyhledávání a výběru přístupové sítě. Server ANDSF, umístěný v páteřní síti, může poskytnout uživatelskému zařízení správné objekty obsahující politiky a informace o dostupných přístupových sítích, z nichž každá je identifikována svým ANID. UE používá ANID k přiřazení těchto síťových politik vůči charakteristikám a identitám přístupových sítí, které detekuje ve svém rádiovém okolí. Tento proces přiřazování je zásadní pro implementaci řízeného směrování provozu, směrovacích politik a bezproblémové mobility mezi 3GPP a jinými přístupy (non-3GPP).

V praxi, když uživatelské zařízení skenuje dostupné sítě, může je identifikovat pomocí jejich vysílaných identifikátorů (jako je PLMN ID, SSID). UE může tyto zjištěné identifikátory namapovat na odpovídající formát ANID. Když UE komunikuje se serverem ANDSF, ať už vyžádáním informací nebo přijetím push zprávy, může nahlásit své aktuální či okolní ANID. Server ANDSF pak používá tato ANID k výběru a doručení odpovídajících politik mezisystémové mobility ([ISMP](/mobilnisite/slovnik/ismp/)) nebo směrování mezi APN (IARP). Například politika může stanovit, že pro ANID představující konkrétní firemní WLAN by měl být veškerý podnikový provoz směrován přes tuto WLAN, zatímco ostatní provoz použije buněčné připojení.

Role ANID přesahuje rámec ANDSF. Je základním prvkem pro umožnění inteligentního výběru přístupové sítě v prostředí s více přístupy. Tím, že poskytuje standardizovaný způsob identifikace jakékoli přístupové sítě, umožňuje konzistentní aplikaci politik, přesné hlášení stavu sítě a napomáhá funkcím jako je Access Network Query Protocol (ANQP) ve scénářích Hotspot 2.0. Jeho strukturovaná povaha zajišťuje, že bez ohledu na to, zda se jedná o buňku 5G NR, eNB LTE nebo přístupový bod Wi-Fi 6, mají síť i uživatelské zařízení společný jazyk pro její označení. To je nezbytné pro automatizaci, optimalizaci a poskytnutí bezproblémového uživatelského zážitku v heterogenních sítích.

## K čemu slouží

ANID byl zaveden, aby řešil problém jednoznačné a konzistentní identifikace různorodých přístupových sítí v ekosystému bezdrátového přístupu s více technologiemi. Před jeho standardizací byl výběr sítě a vymáhání politik do značné míry uzavřeny v rámci jednotlivých technologických domén (např. mobilní síť vs. Wi-Fi). S konvergencí přístupů 3GPP a non-3GPP a snahou o služby typu „Always Best Connected“ (ABC) vznikla naléhavá potřeba společného identifikátoru, který by mohly používat síťové nástroje pro správu politik k činění inteligentních rozhodnutí napříč různými rádiovými technologiemi.

Historický kontext spočívá v práci 3GPP na síťové mobilitě a řízení politik, zejména se zavedením ANDSF ve verzi 8 (Release 8) jako součásti Evolved Packet Core (EPC). Účelem ANDSF bylo pomáhat uživatelským zařízením při vyhledávání a výběru přístupových sítí. K umožnění této funkce byl zapotřebí standardizovaný způsob, jak tyto sítě „pojmenovat“. ANID tuto mezeru zaplnil a poskytl potřebnou abstraktní vrstvu. Řešil omezení předchozích ad-hoc přístupů, kde byla identifikace sítě neinteroperabilní a proprietární, což bránilo škálovatelnému, operátorem řízenému správě provozu s více přístupy.

ANID navíc umožňuje klíčové případy užití, jako je bezproblémové přesouvání provozu na Wi-Fi (offloading), směrování provozu na základě stavu sítě a předplatitelských politik a služby založené na poloze. Tím, že umožňuje síti odkazovat se na konkrétní Wi-Fi hotspot nebo sektor buňky přesným identifikátorem, mohou operátoři nasazovat sofistikované politiky (např. „pro tento ANID reprezentující bezplatnou Wi-Fi používej pro přenos videa, ale pro hlasovou službu použij ANID makrobuňky“). Stal se tak základním kamenem pro umožnění řízené mobility mezi různými RAT (Radio Access Technology) a optimalizace zdrojů v sítích 3GPP od EPC až po systém 5G (5GS), kde je integrace non-3GPP přístupů ještě hlouběji zakotvena.

## Klíčové vlastnosti

- Technologií nezávislý identifikátor podporující jak přístupové sítě 3GPP (GERAN, UTRAN, E-UTRAN, NG-RAN), tak i jiné (non-3GPP) přístupové sítě (WLAN)
- Strukturovaný formát obsahující pole jako MCC, MNC, LAC/RAC/TAC pro mobilní sítě a SSID/HESSID/Realm pro WLAN
- Jádrová komponenta správných objektů (Management Objects) funkce ANDSF pro politiky vyhledávání a výběru přístupových sítí
- Umožňuje přesné přiřazení mezi síťově detekovanými přístupovými body a operátorem definovanými pravidly politik
- Usnadňuje hlášení informací o poloze a událostech mobility ze strany uživatelského zařízení (UE) na politické servery
- Základní prvek pro politiky mezisystémové mobility (ISMP) a politiky směrování mezi APN (IARP)

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)

## Definující specifikace

- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3

---

📖 **Anglický originál a plná specifikace:** [ANID na 3GPP Explorer](https://3gpp-explorer.com/glossary/anid/)
