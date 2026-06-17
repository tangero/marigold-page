---
slug: "bcd"
url: "/mobilnisite/slovnik/bcd/"
type: "slovnik"
title: "BCD – Binary Coded Decimal"
date: 2025-01-01
abbr: "BCD"
fullName: "Binary Coded Decimal"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bcd/"
summary: "Binary Coded Decimal (BCD) je třída binárních kódování pro desítková čísla, kde je každá desítková číslice reprezentována pevným počtem bitů, obvykle čtyřmi. V telekomunikacích se používá pro přesnou"
---

BCD (binárně kódovaná desítková soustava) je binární kódování pro desítková čísla, kde je každá číslice reprezentována pevným počtem bitů, používané v mobilních sítích pro přesnou reprezentaci identifikátorů, jako jsou telefonní čísla a IMSI, v signalizaci a datech SIM.

## Popis

Binary Coded Decimal (BCD) je metoda kódování desítkových čísel v binárním formátu. Ve své nejběžnější formě, známé jako packed BCD nebo jednoduše BCD, je každá desítková číslice (0-9) reprezentována svým čtyřbitovým binárním ekvivalentem (0000 až 1001). Například desítkové číslo 123 by bylo v BCD zakódováno jako 0001 0010 0011. To se liší od čistě binární reprezentace, kde je celé číslo převedeno jako celek (123 se stane 01111011). Ve specifikacích 3GPP se BCD kódování často používá pro pole proměnné délky, kde je počet číslic znám nebo indikován samostatně. Kódování je typicky zarovnáno vlevo (nejvýznamnější číslice první) v rámci oktetu, a pokud je počet číslic lichý, poslední čtyři bity finálního oktetu jsou často vyplněny 'výplňovou' hodnotou (např. 1111), aby se zachovalo zarovnání na oktet.

V rámci architektury 3GPP není BCD síťovou funkcí ani protokolem, ale základním schématem reprezentace dat používaným napříč více vrstvami a rozhraními. Je specifikováno v různých technických specifikacích (TS) pro kódování konkrétních informačních prvků. Například v TS 24.008 (protokoly jádra sítě) používá informační prvek Called Party BCD Number BCD k reprezentaci volaných číslic. V rádiových řídicích specifikacích ([RRC](/mobilnisite/slovnik/rrc/)), jako jsou TS 25.331, TS 36.331 a TS 38.331, se BCD používá pro kódování bloků systémových informací (SIB) týkajících se identit sítě a buňky. Jeho úlohou je zajistit standardizovaný, efektivní a na chyby odolný způsob přenosu číselných dat mezi síťovými uzly a uživatelským zařízením (UE).

Proces kódování zahrnuje převod řetězce desítkových číslic, kde je každá číslice převedena na svůj čtyřbitový nibble. Tyto nibbly jsou následně zřetězeny a zabaleny do oktetů. Dekódování tento proces obrací. Klíčové aspekty zahrnují zpracování lichého počtu číslic, reprezentaci nedesítkových znaků (jako '*' nebo '#'), pro které mohou být definována specifická BCD kódování, a pořadí přenosu číslic (nejvýznamnější číslice první). Jednoduchost a determinismus BCD jej činí vhodným pro ukládání na kartách SIM/USIM (jak je definováno v TS 31.101/121) pro pole jako [IMSI](/mobilnisite/slovnik/imsi/), kde je každá číslice IMSI uložena ve formátu BCD, což umožňuje kompaktní a přesné načítání.

## K čemu slouží

BCD existuje k řešení problému přesné a efektivní reprezentace desítkových čísel v binárních digitálních systémech, zejména tam, kde jsou lidsky čitelné číselné identifikátory klíčové. V telekomunikacích jsou identifikátory jako telefonní čísla ([MSISDN](/mobilnisite/slovnik/msisdn/)), mezinárodní identity mobilních účastníků ([IMSI](/mobilnisite/slovnik/imsi/)) a různé síťové kódy v zásadě desítkové. Čistě binární reprezentace celého čísla může vést ke komplikacím při parsování, zobrazování a kompatibilitě s mezinárodními číslovacími plány. BCD poskytuje přímé, číslici po číslici mapování, které jednoznačně zachovává původní desítkovou strukturu, usnadňuje zpracování, zobrazování a interoperabilitu mezi síťovými prvky od různých výrobců.

Historicky BCD kódování předchází 3GPP a bylo široce používáno v rané digitální telefonii a výpočetní technice. Jeho přijetí do standardů 3GPP (od Release 6 ve zmíněných specifikacích) bylo motivováno potřebou zpětné kompatibility a konzistence s existujícími telekomunikačními postupy, zejména těmi zděděnými z GSM. Řeší omezení alternativních kódování, jako je ASCII, které by používalo více bitů na číslici (7 nebo 8), nebo čistě binárního, které vyžaduje konverzní algoritmy a může zastřít jednotlivé číslice. Pro ukládání na SIM karty s omezenou kapacitou a pro přenos v signalizačních zprávách šetřících šířku pásma nabízí BCD kompaktní a přímočaré řešení.

Motivací pro jeho pokračující použití napříč releasy 3GPP, včetně 5G NR, je jeho spolehlivost a jednoduchost. Odstraňuje nejednoznačnost v reprezentaci čísel, což je klíčové pro směrování hovorů, identifikaci účastníků a vysílání systémových informací. Standardizací na BCD pro konkrétní číselná pole 3GPP zajišťuje, že uživatelská zařízení (UE) a síťové uzly od jakéhokoli výrobce mohou tyto základní identifikátory správně interpretovat, čímž udržuje globální interoperabilitu, která je základním kamenem celulárních sítí.

## Klíčové vlastnosti

- Přímé kódování desítkových čísel číslici po číslici do binárních nibblů
- Kompaktní reprezentace využívající 4 bity na desítkovou číslici (0-9)
- Standardizovaný mechanismus výplně (např. 1111) pro zarovnání lichého počtu číslic v oktetech
- Široké použití napříč specifikacemi 3GPP pro kódování MSISDN, IMSI a systémových informací
- Zajišťuje jednoznačnou interpretaci číselných identifikátorů napříč síťovými rozhraními
- Usnadňuje efektivní ukládání na SIM/USIM a přenos v signalizačních zprávách

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [BCD na 3GPP Explorer](https://3gpp-explorer.com/glossary/bcd/)
