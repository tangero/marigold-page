---
slug: "pabx"
url: "/mobilnisite/slovnik/pabx/"
type: "slovnik"
title: "PABX – Private Automatic Branch eXchange"
date: 2025-01-01
abbr: "PABX"
fullName: "Private Automatic Branch eXchange"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pabx/"
summary: "Privátní automatická pobočková ústředna (PABX) je privátní telefonní ústředna používaná v rámci podniku nebo organizace. V 3GPP je modelována jako síťová entita, která se rozhraním připojuje k jádru m"
---

PABX je privátní telefonní ústředna pro podnik, která se rozhraním připojuje k jádru mobilní sítě a umožňuje funkce jako přímé volání dovnitř (DID) a privátní číslovací plány.

## Popis

V architektuře 3GPP není Privátní automatická pobočková ústředna (PABX) jako taková síťovou funkcí definovanou 3GPP, ale spíše referencovanou externí entitou zákaznické přípojky ([CPE](/mobilnisite/slovnik/cpe/)). Představuje starší nebo současnou místní telefonní ústřednu, která slouží soukromé organizaci, jako je firma, vládní úřad nebo kampus. Specifikace 3GPP definují, jak veřejná mobilní síť, konkrétně jádrová síť (CN), rozhraním připojuje a poskytuje služby takovým PABX systémům. To je primárně řešeno konceptem PABX předplatného, kde je PABX považována za jediného účastníka s více přidruženými telefonními čísly (např. blokem [MSISDN](/mobilnisite/slovnik/msisdn/)).

Architektonicky se PABX připojuje k jádru mobilní sítě přes standardizovaná rozhraní. Historicky to mohlo být přes okruhově přepínané propojení (např. pomocí [ISDN](/mobilnisite/slovnik/isdn/) PRI přes linky E1/T1) k ústředně [MSC](/mobilnisite/slovnik/msc/). V moderních nasazeních založených na IP může připojení využívat [SIP](/mobilnisite/slovnik/sip/) trunking směrem k IP Multimedia Subsystem (IMS). PABX obsahuje vlastní vnitřní přepínací matici, logiku řízení hovorů a typicky podporuje funkce jako držení, přesměrování, konferenční hovory a privátní číslovací plán (volání na interní linky). Z pohledu mobilní sítě se PABX jeví jako jediná účastnická entita, ale se schopností směrovat příchozí hovory na konkrétní interní linky na základě vytočeného MSISDN.

Její role v ekosystému 3GPP spočívá v usnadnění podnikových komunikačních služeb. Klíčové specifikace jako TS 29.007 (Obecné požadavky na vzájemné propojení veřejné pozemní mobilní sítě a jiných sítí) podrobně popisují signalizační požadavky pro propojení [PLMN](/mobilnisite/slovnik/plmn/) s PABX, pokrývající aspekty jako sestavení hovoru, překlad čísel a obsluha doplňkových služeb. TS 21.905 ji zahrnuje do slovníku pojmů. Síť poskytuje PABX skupinu trunků nebo rozsah veřejných čísel a spravuje mobilitu pro jakákoliv přidružená mobilní rozšíření (např. prostřednictvím řešení mobility [PBX](/mobilnisite/slovnik/pbx/)). Tato integrace umožňuje zaměstnancům mít jednotnou identitu (např. jedno firemní číslo, které zvoní na stolním telefonu i mobilu).

## K čemu slouží

Koncept PABX existuje, aby rozšířil dosah a funkce veřejné telefonní sítě do soukromých organizačních domén. Řeší problém efektivní vnitřní komunikace a správy externích hovorů pro firmy bez nutnosti samostatné, veřejně přepínané linky pro každého zaměstnance. Tím, že funguje jako privátní ústředna, umožňuje krátké číslování mezi linkami, centralizované směrování hovorů a kontrolu nákladů.

V kontextu standardizace 3GPP explicitní odkazování na PABX řeší kritickou potřebu vzájemného propojení mezi veřejnými mobilními sítěmi a zavedenou privátní telefonní infrastrukturou. To bylo obzvláště důležité během éry 2G/3G, kdy firemní komunikace silně závisela na starších PABX systémech. Standardy 3GPP musely definovat, jak mohou hovory iniciované z mobilu končit na lince PABX a jak mohou být hovory z veřejné sítě ([PSTN](/mobilnisite/slovnik/pstn/)) určené konkrétní osobě ve firmě směrovány přes mobilní síť na mobilní telefon této osoby, přičemž je s PABX nakládáno jako s prostředníkem nebo logickou skupinou. Toto vzájemné propojení vyřešilo omezení mobilních sítí jako čistě 'veřejných' a umožnilo sofistikované firemní telefonní funkce, čímž položilo základ pro pozdější řešení konvergence pevné a mobilní sítě (FMC) a jednotné komunikace (UC).

## Klíčové vlastnosti

- Funguje jako privátní přepínací systém zákaznické přípojky rozhraním připojený k PLMN
- Podporuje privátní číslovací plán pro vnitřní volání na linky
- Typicky je přidružena k bloku veřejných MSISDN od mobilního operátora
- Umožňuje funkce jako přesměrování hovoru, držení a konferenční hovory v rámci podniku
- Připojuje se přes standardizovaná propojovací rozhraní (např. ISDN PRI, SIP)
- Usnadňuje podniková řešení mobility a jednotné komunikace

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [ISDN – Integrated Services Digital Network](/mobilnisite/slovnik/isdn/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.007** (Rel-19) — PLMN-PSTN/ISDN Interworking Requirements

---

📖 **Anglický originál a plná specifikace:** [PABX na 3GPP Explorer](https://3gpp-explorer.com/glossary/pabx/)
