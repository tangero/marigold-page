---
slug: "hplmnb"
url: "/mobilnisite/slovnik/hplmnb/"
type: "slovnik"
title: "HPLMNB – Home Public Land Mobile Network of the B subscriber"
date: 2025-01-01
abbr: "HPLMNB"
fullName: "Home Public Land Mobile Network of the B subscriber"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hplmnb/"
summary: "HPLMN volaného účastníka (B-strana) v komunikační relaci. Používá se pro směrování hovorů, účtování a servisní logiku (např. CAMEL) k identifikaci domovské sítě příjemce, což může ovlivnit způsob zpra"
---

HPLMNB je domácí veřejná pozemní mobilní síť volaného účastníka, která se používá pro směrování hovorů, účtování a servisní logiku k identifikaci domovské sítě příjemce.

## Popis

Domácí veřejná pozemní mobilní síť účastníka B (HPLMNB) je specifická aplikace konceptu [HPLMN](/mobilnisite/slovnik/hplmn/) používaná v logice řízení hovorů a relací. Výslovně odkazuje na domovskou síť volaného účastníka (tzv. callee) v telekomunikační relaci. Tento identifikátor se stává relevantním během navazování a řízení hovoru, zprávy nebo datové relace, kdy volající účastník (A-účastník) usiluje o komunikaci s volaným účastníkem (B-účastník). Síťové elementy zapojené do směrování a obsluhy hovoru, jako jsou Mobile Switching Centers ([MSC](/mobilnisite/slovnik/msc/)), Service Control Points (SCP) nebo IMS Call Session Control Functions ([CSCF](/mobilnisite/slovnik/cscf/)), mohou potřebovat identifikovat HPLMNB, aby uplatnily specifická pravidla směrování, fakturační politiky nebo služby inteligentní sítě.

Z architektonického pohledu je HPLMNB odvozena z [IMSI](/mobilnisite/slovnik/imsi/) nebo Mobile Station International Subscriber Directory Number ([MSISDN](/mobilnisite/slovnik/msisdn/)) B-účastníka. Při uskutečnění hovoru provádí výchozí síť analýzu čísla pro určení směrování. Pokud je B-účastník mobilním uživatelem, síť identifikuje jeho HPLMN z jeho čísla nebo IMSI. Tato informace je přenášena v signalizačních zprávách, jako jsou [ISUP](/mobilnisite/slovnik/isup/) nebo SIP, při směrování hovoru. V architekturách inteligentních sítí, jako je [CAMEL](/mobilnisite/slovnik/camel/), je HPLMNB klíčovým parametrem. Například HPLMN B-účastníka může mít CAMEL předplatné, které spouští instanci servisní logiky v jeho domovské síti, aby řídila zpracování příchozích hovorů, jako je aplikace přesměrování hovoru, zákazu nebo předplaceného účtování pro přijímající větev.

Jak to funguje, zahrnuje několik síťových interakcí. V jednoduchém mobil-mobil hovoru se Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)) ve síti A-účastníka dotazuje na HLR/HSS B-účastníka (umístěné v HPLMNB) pomocí operace MAP_Send_Routing_Information. HLR HPLMNB odpoví s roamingovým číslem, což umožní směrování hovoru k MSC, které aktuálně obsluhuje B-účastníka. Pro služby s přidanou hodnotou může být vyvolána platforma inteligentní sítě HPLMNB. Identifikace HPLMNB je tedy klíčová pro určení jurisdikce – zda je hovor vnitrosíťový (ve stejné PLMN) nebo mezisíťový, což přímo ovlivňuje mezisíťové poplatky, fakturační tarify a uplatnění účastnicky specifické servisní logiky pro volaného účastníka.

## K čemu slouží

HPLMNB existuje, aby umožnila přesné a funkčně bohaté zpracování cílové strany hovoru na základě příslušnosti volaného účastníka k domovské síti. Starší telefonní systémy se primárně zaměřovaly na směrování hovorů k cílovému číslu. S příchodem mobilních sítí a inteligentních služeb však bylo nutné začít s volaným účastníkem nakládat jako s účastníkem s vlastním servisním profilem hostovaným v konkrétní domovské síti. Koncept HPLMNB umožňuje síti toto rozpoznat a začlenit politiky domovské sítě B-účastníka do průběhu hovoru.

Toto řeší několik problémů. Za prvé umožňuje správné účtování a zúčtování pro cílovou větev hovoru. Mezioperátorské zúčtovací sazby často závisí na zapojených sítích. Identifikace HPLMNB umožňuje výchozí síni správně vypočítat poplatky za doručení hovoru k účastníkovi tohoto konkrétního operátora. Za druhé umožňuje provedení služeb B-účastníka. Bez identifikace HPLMNB by funkce jako zákaz příchozích hovorů, personalizované vyzváněcí tóny nebo přijetí hovoru s předplaceným účtem řízené domovskou sítí B-účastníka nemohly fungovat, když je účastník v roamingu. Parametr HPLMNB zajišťuje, že signalizace hovoru může být směrována k příslušné servisní logice ve správné síti, což zajišťuje konzistentní uživatelský zážitek pro volaného účastníka bez ohledu na polohu volajícího nebo jeho síť.

## Klíčové vlastnosti

- Identifikuje domovskou síť volaného účastníka (B-účastníka) v komunikační relaci
- Je odvozena z MSISDN nebo IMSI B-účastníka během procedur směrování hovoru
- Používá se Gateway MSC a IMS uzly pro dotazování HLR/HSS B-účastníka na informace pro směrování
- Klíčový parametr v CAMEL a dalších IN protokolech pro spouštění servisní kontroly strany B
- Určuje jurisdikční hranice pro účtování a mezioperátorské zúčtování na cílové straně
- Umožňuje provedení servisních funkcí předplatného volaného účastníka, jako je přesměrování hovoru nebo zákaz

## Související pojmy

- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [HPLMNB na 3GPP Explorer](https://3gpp-explorer.com/glossary/hplmnb/)
