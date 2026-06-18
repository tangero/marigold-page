---
slug: "fn-crg"
url: "/mobilnisite/slovnik/fn-crg/"
type: "slovnik"
title: "FN-CRG – Fixed Network Cable Residential Gateway Globally Unique AMF Identifier"
date: 2026-01-01
abbr: "FN-CRG"
fullName: "Fixed Network Cable Residential Gateway Globally Unique AMF Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fn-crg/"
summary: "FN-CRG je globálně jednoznačný identifikátor funkce pro správu přístupu a mobility (AMF) obsluhující kabelovou rezidenční bránu v pevné síti 5G. Jednoznačně identifikuje instanci AMF spravující řídicí"
---

FN-CRG je globálně jednoznačný identifikátor funkce pro správu přístupu a mobility (AMF) obsluhující kabelovou rezidenční bránu v pevné síti 5G.

## Popis

Globálně jednoznačný identifikátor [AMF](/mobilnisite/slovnik/amf/) pro pevnou síť a kabelovou rezidenční bránu (FN-CRG [GUAMI](/mobilnisite/slovnik/guami/)) je klíčový identifikátor definovaný ve specifikaci 3GPP Release 16 v kontextu pevného přístupu 5G přes kabelové sítě. Jedná se o specifickou aplikaci širšího konceptu GUAMI (definovaného v TS 23.003) pro kabelovou rezidenční bránu (FN-CRG), což je zařízení na straně zákazníka pro kabelový pevný širokopásmový přístup (např. [DOCSIS](/mobilnisite/slovnik/docsis/)) integrované do systému 5G. FN-CRG GUAMI jednoznačně a globálně identifikuje konkrétní instanci funkce pro správu přístupu a mobility (AMF), která je zodpovědná za správu mobility a připojení řídicí roviny daného zařízení FN-CRG.

Z architektonického hlediska, když se zařízení FN-CRG (typ rezidenční brány pevné sítě pro kabel) inicializuje a registruje v jádru sítě 5G, musí mu být přidělena AMF. Síťová funkce pro výběr (např. Network Slice Selection Function - [NSSF](/mobilnisite/slovnik/nssf/)) pomáhá vybrat vhodnou AMF na základě předplatného, síťového řezu a lokálních politik. Po výběru je identita této AMF – její GUAMI – asociována s FN-CRG. FN-CRG GUAMI je strukturován podle formátu GUAMI: obsahuje identifikátor [PLMN](/mobilnisite/slovnik/plmn/) (mobilní kód země a mobilní kód sítě) pro zajištění globální jednoznačnosti napříč operátory, následovaný AMF Region ID, AMF Set ID a AMF Pointer, které společně identifikují konkrétní instanci AMF v síti operátora.

Jak funguje: FN-CRG GUAMI se používá v signalizačních zprávách řídicí roviny mezi síťovými funkcemi. Například když funkce pro správu relací ([SMF](/mobilnisite/slovnik/smf/)) potřebuje komunikovat s AMF spravující konkrétní FN-CRG pro zřízení [PDU](/mobilnisite/slovnik/pdu/) relace, použije FN-CRG GUAMI ke správnému směrování zprávy N11. Je také klíčový při událostech mobility; pokud je třeba kontext FN-CRG přesunout z jedné AMF na druhou (např. pro vyrovnávání zátěže nebo obnovu po výpadku), GUAMI identifikuje zdrojovou a cílovou AMF. Identifikátor je uložen v Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) jako část kontextu účastníka, což zajišťuje, že následné aktualizace registrace nebo servisní požadavky mohou nalézt správnou obsluhující AMF. Toto přesné směrování je zásadní pro škálovatelnost a spolehlivost jader sítí 5G podporujících miliony pevných zařízení.

## K čemu slouží

FN-CRG GUAMI byl zaveden, aby vyřešil problémy adresování a směrování spojené se škálováním jádra 5G pro podporu obrovského množství pevných rezidenčních bran (jako kabelových modemů). V předchozích generacích a ne-3GPP pevných sítích byla správa CPE často prováděna proprietárními nebo doménově specifickými protokoly (jako TR-069) s méně podrobnými, ne globálně jednoznačnými identifikátory. Když byl kabelový přístup integrován do jádra 5G prostřednictvím FN-CRG (od Release 16), bylo nutné spravovat tato zařízení podle stejných principů škálovatelnosti, redundance a cloud-nativní bezstavovosti aplikovaných na mobilní uživatelská zařízení.

Hlavním řešeným problémem je potřeba jednoznačné identifikace a efektivního směrování ke správné entitě řídicí roviny (AMF) v dekomponované, službami založené architektuře, kde AMF mohou být dynamicky vytvářeny a škálovány. Bez globálně jednoznačného identifikátoru by mohlo docházet k chybám směrování v prostředích více dodavatelů nebo při slučování sítí operátorů. Framework GUAMI, aplikovaný specificky na FN-CRG, zajišťuje, že jakákoli síťová funkce (SMF, UDM, jiná AMF) může přesně určit a komunikovat s instancí AMF obsluhující konkrétní kabelovou bránu kdekoliv na světě. To umožňuje pokročilé funkce 5G pro pevný přístup: efektivní správu mobility (i u 'pevných' zařízení může docházet k logické mobilitě nebo přeřazení), plynulé přemístění AMF pro vyrovnávání zátěže a spolehlivou kontinuitu služeb při výpadcích síťových funkcí. Je to základní prvek pro zacházení s pevným přístupem jako se skutečným rovnocenným partnerem mobilního přístupu v jádru 5G.

## Klíčové vlastnosti

- Globálně jednoznačný identifikátor pro AMF obsluhující kabelovou rezidenční bránu (FN-CRG)
- Založený na standardní struktuře GUAMI (PLMN ID, Region ID, Set ID, Pointer) pro interoperabilitu
- Umožňuje přesné směrování zpráv N11 a dalších zpráv řídicí roviny v jádru 5G
- Podporuje procedury redundance AMF, vyrovnávání zátěže a přesunu stavu pro pevná zařízení
- Uložen v UDM jako část kontextu účastníka pro konzistentní správu relací
- Zásadní pro škálování jádra 5G na podporu masivního množství pevných širokopásmových koncových bodů

## Související pojmy

- [GUAMI – Globally Unique AMF Identifier](/mobilnisite/slovnik/guami/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.716** (Rel-16) — Wireline and Trusted Non-3GPP Access to 5G Core
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [FN-CRG na 3GPP Explorer](https://3gpp-explorer.com/glossary/fn-crg/)
