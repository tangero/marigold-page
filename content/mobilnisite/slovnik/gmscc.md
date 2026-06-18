---
slug: "gmscc"
url: "/mobilnisite/slovnik/gmscc/"
type: "slovnik"
title: "GMSCC – Gateway MSC in HPLMNC"
date: 2025-01-01
abbr: "GMSCC"
fullName: "Gateway MSC in HPLMNC"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gmscc/"
summary: "Gateway MSC nacházející se v domovské síti účastníka v rámci kódu země (Home Public Land Mobile Network Country – HPLMNC). Jedná se o konkrétní instanci GMSCB, která zdůrazňuje její geografické a logi"
---

GMSCC je Gateway MSC nacházející se v síti domovské země účastníka (HPLMNC), který slouží jako konkrétní instance pro ukončení příchozích hovorů k tomuto účastníkovi.

## Popis

Gateway [MSC](/mobilnisite/slovnik/msc/) v [HPLMNC](/mobilnisite/slovnik/hplmnc/) (GMSCC) je specifické označení pro Gateway MSC, který se nachází v části kódu země domovské veřejné pozemní mobilní sítě účastníka ([HPLMN](/mobilnisite/slovnik/hplmn/)). HPLMNC je část kódu země v rámci Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)) a Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)), která jednoznačně identifikuje domovskou síť účastníka. GMSCC je tedy [GMSCB](/mobilnisite/slovnik/gmscb/), který je fyzicky i logicky umístěn ve stejné zemi jako operátor domovské sítě účastníka. Jeho primární funkce odpovídá standardnímu GMSCB: přijímat příchozí hovory pro účastníky své sítě a dotazovat se na [HLR](/mobilnisite/slovnik/hlr/), aby získal směrovací instrukce.

Operačně, když je mezinárodní hovor uskutečněn na mobilního účastníka, je typicky směrován do brány v cílové zemi. GMSCC je uzel v této cílové zemi (HPLMNC), který tento mezinárodní úsek hovoru přijímá. Provede dotaz na HLR, aby zjistil, zda je účastník lokalizován doma nebo v roamingu v zahraničí. Pokud je účastník doma, GMSCC směruje hovor na příslušný [VMSC](/mobilnisite/slovnik/vmsc/) v rámci země. Pokud je účastník v mezinárodním roamingu, HLR poskytne MSRN, který odkazuje na síť v cizí zemi, a GMSCC pak hovor mezinárodně směruje na VMSC této navštívené sítě.

Tento koncept je zvláště důležitý pro účtování, efektivitu směrování a soulad s regulacemi. Ukotvením hovoru v GMSC domovské země si operátor domovské sítě udržuje kontrolu nad sestavením hovoru, může uplatňovat služby a politiky specifické pro domovskou síť a zajišťuje, že záznamy o hovorech (CDR) pro účtování jsou generovány v příslušném jurisdikčním bodě. GMSCC rozhraní s mezinárodními bránami, domácí signalizační sítí SS7 pro přístup k HLR a potenciálně s IP sítěmi v novějších vydáních.

## K čemu slouží

Koncept GMSCC řeší složitosti mezinárodního směrování hovorů a regulatorní požadavky v globálních mobilních komunikacích. Definuje jasný architektonický bod v domovské zemi účastníka, kde jsou příchozí mezinárodní hovory předávány od mezinárodního dopravce operátorovi domovské mobilní sítě. To je zásadní pro stanovení jurisdikce pro účtování, zákonné odposlechy a aplikaci národních telekomunikačních předpisů.

Bez definovaného GMSCC by mohly být mezinárodní hovory potenciálně směrovány přímo na navštívenou síť, když je účastník v roamingu, a obcházet tak operátora domovské sítě. To by domovského operátora připravilo o příjmy a kontrolu. GMSCC zajišťuje, že všechny hovory určené pro MSISDN účastníka se nejprve dotknou infrastruktury domovské sítě v domovské zemi, což umožňuje kontrolu služeb, detekci podvodů a konzistentní účtování bez ohledu na polohu účastníka. Jde o klíčový koncept ve specifikacích 3GPP pro CAMEL (Customized Applications for Mobile network Enhanced Logic) a další služby inteligentních sítí, kde se spouštěč pro služby řízené domovskou sítí často aktivuje právě na GMSCC.

## Klíčové vlastnosti

- Nachází se v rámci kódu země domovské sítě účastníka (HPLMNC)
- Slouží jako první kontaktní bod v domovské zemi pro příchozí mezinárodní hovory
- Provádí dotaz na HLR pro určení polohy účastníka (domácí nebo mezinárodní roaming)
- Kotví řízení hovoru a servisní logiku pro operátora domovské sítě
- Generuje záznamy pro účtování (CDR) v rámci regulatorní jurisdikce domovské země
- Rozhraní s mezinárodními přepojovacími centry (ISC) a domácí signalizační sítí

## Související pojmy

- [GMSCB – Gateway MSC of the B subscriber](/mobilnisite/slovnik/gmscb/)
- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)

## Definující specifikace

- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [GMSCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmscc/)
