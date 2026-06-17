---
slug: "hessid"
url: "/mobilnisite/slovnik/hessid/"
type: "slovnik"
title: "HESSID – Homogeneous Extended Service Set Identifier"
date: 2025-01-01
abbr: "HESSID"
fullName: "Homogeneous Extended Service Set Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hessid/"
summary: "HESSID je jedinečný identifikátor pro bezdrátovou lokální síť (WLAN), který usnadňuje bezproblémovou integraci a spolupráci se sítěmi 3GPP. Používá se v politikách funkce pro vyhledávání a výběr příst"
---

HESSID je jedinečný identifikátor pro WLAN, který umožňuje bezproblémovou integraci se sítěmi 3GPP a používá se v politikách ANDSF k identifikaci důvěryhodných přístupových bodů pro přesměrování provozu.

## Popis

Homogeneous Extended Service Set Identifier (HESSID) je 48bitový identifikátor, formátovaný shodně s [MAC](/mobilnisite/slovnik/mac/) adresou, který jednoznačně identifikuje homogenní skupinu jednoho nebo více rozšířených servisních souborů (ESS) standardu [IEEE](/mobilnisite/slovnik/ieee/) 802.11. V kontextu spolupráce 3GPP a WLAN je HESSID klíčovým parametrem, který uživatelské zařízení (UE) používá k identifikaci konkrétních WLAN sítí, jež jsou součástí spravovaného nebo důvěryhodného ekosystému operátora. Technicky je odvozen z MAC adresy jednoho z přístupových bodů ([AP](/mobilnisite/slovnik/ap/)) v rámci ESS nebo může být speciální hodnotou nastavenou operátorem sítě. HESSID je vysílán v rámcích Beacon a Probe Response WLAN sítě jako součást elementu Interworking, což umožňuje jeho detekci zařízeními UE při skenování. V architektuře 3GPP je HESSID využíván funkcí pro vyhledávání a výběr přístupové sítě ([ANDSF](/mobilnisite/slovnik/andsf/)), což je entita jádra sítě, která poskytuje zařízení UE informace o dostupných sítích a politiky mezisystémové mobility ([ISMP](/mobilnisite/slovnik/ismp/)). Politika ANDSF může nařídit zařízení UE, aby se připojilo k WLAN s konkrétním HESSID, pokud je dostupné, což umožňuje plynulé přesměrování nebo přesun provozu z rádiové přístupové sítě 3GPP. Procesor pro spolupráci 3GPP a WLAN v zařízení UE používá HESSID k porovnání nalezených sítí s politikami přijatými od ANDSF. Dále, ve scénářích zahrnujících rozvinutou bránu paketových dat (ePDG) pro nedůvěryhodný nepřístup 3GPP, lze HESSID použít k určení, zda má být nalezená WLAN považována za důvěryhodnou či nedůvěryhodnou přístupovou síť, což ovlivňuje postup ověřování a navazování [IPsec](/mobilnisite/slovnik/ipsec/) tunelu. Tento identifikátor hraje klíčovou roli v algoritmech výběru sítě, zajišťuje, že zařízení UE upřednostňuje hotspoty určené operátorem pro konzistentní a bezpečný uživatelský zážitek.

## K čemu slouží

HESSID byl zaveden k řešení problému inteligentního a bezpečného směrování uživatelského provozu mezi sítěmi 3GPP a WLAN. Před jeho standardizací se mohla zařízení UE připojit k jakékoli dostupné WLAN, ale operátoři neměli standardizovaný způsob, jak identifikovat své vlastní spravované nebo partnerské Wi-Fi sítě za účelem podpory bezproblémového přesměrování provozu. To vedlo k neoptimálnímu uživatelskému zážitku, potenciálním bezpečnostním rizikům z připojení k nedůvěryhodným hotspotům a neefektivnímu využití síťových zdrojů. HESSID, specifikovaný od vydání 3GPP Release 11, poskytuje standardizovaný, globálně jedinečný identifikátor, který umožňuje operátorovi označit svou WLAN infrastrukturu. To umožňuje vytváření sofistikovaných politik výběru sítě. Primární problém, který řeší, je umožnění směrování provozu založeného na politikách, což je základním kamenem spolupráce 3GPP a WLAN. Umožňuje operátorům ulevit od přetížení svých mobilních sítí přesměrováním datového provozu na důvěryhodné, kvalitní Wi-Fi sítě, při zachování kontroly nad uživatelským zážitkem a bezpečnostním kontextem. Historicky se dřívější pokusy o spolupráci spoléhaly na méně specifické identifikátory, jako je SSID, které nejsou zaručeně jedinečné a lze je snadno falšovat. Jedinečnost HESSID a jeho integrace do politik [ANDSF](/mobilnisite/slovnik/andsf/) poskytly spolehlivější a bezpečnější mechanismus. Jeho vytvoření bylo motivováno explozí dostupnosti Wi-Fi a potřebou těsnější integrace mezi mobilními sítěmi a Wi-Fi jako součásti strategie heterogenních sítí (HetNet), což v konečném důsledku připravilo cestu pro bezproblémovou mobilitu a agregační technologie, jako je agregace LTE a WLAN ([LWA](/mobilnisite/slovnik/lwa/)).

## Klíčové vlastnosti

- 48bitový jedinečný identifikátor formátovaný jako IEEE MAC adresa pro homogenní skupinu WLAN ESS
- Vysílán v rámcích IEEE 802.11 Beacon a Probe Response pro detekci zařízením UE
- Klíčový parametr v politikách 3GPP ANDSF pro inteligentní výběr sítě a směrování provozu
- Používá se k rozlišení mezi důvěryhodným a nedůvěryhodným přístupem k WLAN pro bezpečnostní a autentizační procedury
- Umožňuje operátorovi kontrolu přesměrování provozu na spravované nebo partnerské Wi-Fi sítě
- Podporuje bezproblémovou mobilitu a kontinuitu služeb mezi přístupem 3GPP a WLAN

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [LWA – LTE-WLAN Radio Level Aggregation](/mobilnisite/slovnik/lwa/)
- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)

## Definující specifikace

- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.455** (Rel-19) — LTE Positioning Protocol Annex (LPPa)
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [HESSID na 3GPP Explorer](https://3gpp-explorer.com/glossary/hessid/)
