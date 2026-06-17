---
slug: "amr-wb"
url: "/mobilnisite/slovnik/amr-wb/"
type: "slovnik"
title: "AMR-WB – Adaptive Multi-Rate Wideband Speech Codec"
date: 2025-01-01
abbr: "AMR-WB"
fullName: "Adaptive Multi-Rate Wideband Speech Codec"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/amr-wb/"
summary: "AMR-WB je širokopásmový řečový kodek standardizovaný organizací 3GPP, který poskytuje výrazně lepší kvalitu hlasu ve srovnání s úzkopásmovými kodeky. Pracuje se vzorkovací frekvencí 16 kHz a pokrývá f"
---

AMR-WB je širokopásmový řečový kodek standardizovaný organizací 3GPP, který díky vzorkovací frekvenci 16 kHz pokrývající širší frekvenční rozsah poskytuje vynikající, přirozenou kvalitu hlasu pro mobilní sítě.

## Popis

Adaptivní víceúrovňový širokopásmový řečový kodek (Adaptive Multi-Rate Wideband, AMR-WB) je sofistikovaný algoritmus komprese zvuku navržený speciálně pro mobilní telekomunikace. Na rozdíl od tradičních úzkopásmových kodeků pracujících se vzorkováním 8 kHz (pokrývající 300-3400 Hz) využívá AMR-WB vzorkování 16 kHz k zachycení frekvencí od 50 Hz do 7 kHz. Tento rozšířený frekvenční rozsah výrazně zlepšuje kvalitu řeči, její přirozenost a srozumitelnost, díky čemuž konverzace zní věrohodněji a snižuje se únava posluchače. Kodek využívá technologii algebraického kódového excitovaného lineárního prediktoru (Algebraic Code Excited Linear Prediction, [ACELP](/mobilnisite/slovnik/acelp/)) s víceúrovňovým provozem, což mu umožňuje přizpůsobit se různým podmínkám přenosového kanálu při zachování optimální kvality hlasu.

AMR-WB pracuje s devíti různými přenosovými rychlostmi v rozsahu od 6,60 kbit/s do 23,85 kbit/s, přičemž nejčastěji používané rychlosti jsou 12,65 kbit/s a 23,85 kbit/s. Kodek používá délku rámce 20 milisekund, což odpovídá 320 vzorkům při vzorkovací frekvenci 16 kHz. Každý rámec je rozdělen na čtyři podrámce po 5 ms pro efektivnější zpracování. Enkódér analyzuje řečový signál pomocí analýzy lineární predikce k extrakci spektrálních parametrů (lineární spektrální frekvence), parametrů základního tónu (adaptivní kodebook) a inovačních parametrů (pevný kodebook). Tyto parametry jsou kvantovány a přenášeny do dekodéru, který rekonstruuje řečový signál pomocí syntetického filtrování.

Architektura kodeku zahrnuje několik klíčových komponent: modul předzpracování pro horní propust a škálování signálu, modul analýzy lineární predikce pro odhad spektrální obálky, analýzu základního tónu s otevřenou smyčkou pro počáteční odhad a uzavřenou smyčkou pro zpřesněné parametry. Prohledávání inovačního kodebooku využívá algebraické kodebooky s pozicemi a znaménky pulzů optimalizovanými pro efektivní kódování. Dekodér provádí inverzní operace, včetně dekódování parametrů, generování excitace a syntetického filtrování pro rekonstrukci řečového signálu. Postprocessing zahrnuje adaptivní postfiltrování pro zlepšení percepční kvality rekonstruované řeči.

AMR-WB obsahuje sofistikované mechanismy detekce hlasové aktivity (VAD) a generování komfortního šumu ([CNG](/mobilnisite/slovnik/cng/)) pro efektivní přerušovaný přenos během období ticha. Kodek podporuje více provozních režimů včetně plné rychlosti, poloviční rychlosti a proměnné rychlosti v závislosti na podmínkách sítě. Obsahuje robustní techniky maskování chyb pro zvládání ztrát rámců a přenosových chyb, což zajišťuje postupnou degradaci kvality hlasu při špatných podmínkách kanálu. Návrh kodeku klade důraz jak na účinnost komprese, tak na optimalizaci výpočetní složitosti, což jej činí vhodným pro implementaci v mobilních zařízeních s omezeným výpočetním výkonem a životností baterie.

V sítích 3GPP je AMR-WB integrován do řetězce zpracování médií hlasových služeb a komunikuje s transportními protokoly jako RTP/UDP/IP pro přepojované pakety hlasu. Kodek podporuje provoz bez překódování v koncových scénářích, kdy oba koncové body podporují AMR-WB, čímž zachovává plnou širokopásmovou kvalitu po celé trase hovoru. Byl rozšířen o vylepšené verze jako AMR-WB+ pro hudbu a obecný audio obsah a EVS-WB, který poskytuje ještě lepší kvalitu a účinnost. Široké přijetí AMR-WB napříč generacemi mobilních sítí od 3G po 5G dokládá jeho zásadní roli při poskytování kvalitních hlasových služeb v moderní telekomunikaci.

## K čemu slouží

AMR-WB byl vyvinut k řešení omezení úzkopásmových řečových kodeků, které dominovaly mobilní komunikaci od počátků celulárních sítí. Tradiční úzkopásmové kodeky jako [AMR-NB](/mobilnisite/slovnik/amr-nb/) (Adaptive Multi-Rate Narrowband) pracovaly v rozsahu 300-3400 Hz, což bylo dostačující pro základní srozumitelnost, ale postrádalo přirozenost a bohatost osobní konverzace. Toto frekvenční omezení mělo za následek tlumenou řeč, sníženou srozumitelnost některých souhlásek (zejména frikativ jako 's', 'f' a 'th') a celkovou únavu posluchače při delších hovorech. Telekomunikační průmysl uznal, že lepší kvalita hlasu může zlepšit uživatelský zážitek, snížit nedorozumění a poskytnout konkurenční výhodu na stále více nasycených mobilních trzích.

Vývoj AMR-WB byl motivován několika klíčovými faktory: dostupností vyššího výpočetního výkonu v mobilních zařízeních, lepšími možnostmi šířky pásma sítě a rostoucími očekáváními spotřebitelů ohledně lepší kvality zvuku. Výzkum v psychoakustice ukázal, že lidská řeč obsahuje důležité informace ve frekvencích mimo tradiční telefonní pásmo, zejména v rozsahu 50-300 Hz (poskytujícím přirozený bas a hlasovou teplost) a 3400-7000 Hz (zlepšujícím jasnost souhlásek a srozumitelnost řeči). Rozšířením frekvenčního rozsahu na 50-7000 Hz mohl AMR-WB zachytit tyto důležité spektrální složky, což vedlo k řeči, která zní přirozeněji, méně napjatě a více podobně osobní konverzaci.

Dalším důležitým motivem byla potřeba standardizovaného širokopásmového kodeku, který by mohl fungovat napříč různými síťovými technologiemi a poskytovateli služeb. Před standardizací AMR-WB existovaly různé proprietární širokopásmové kodeky, které však trpěly problémy s interoperabilitou. Standardizace organizací 3GPP zajistila, že AMR-WB může být konzistentně implementován napříč zařízeními a sítěmi, což usnadňuje globální roaming a kontinuitu služeb. Kodek byl navržen tak, aby byl zpětně kompatibilní s existující síťovou infrastrukturou, a zároveň poskytoval operátorům jasnou cestu ke zlepšení jejich hlasových služeb. Jeho adaptivní víceúrovňová schopnost mu umožnila udržovat dobrou kvalitu i v náročných rádiových podmínkách, což jej činí vhodným pro proměnlivou kvalitu kanálu charakteristickou pro mobilní sítě.

## Klíčové vlastnosti

- Vzorkovací frekvence 16 kHz pokrývající frekvenční rozsah 50 Hz až 7 kHz
- Devět provozních přenosových rychlostí od 6,60 kbit/s do 23,85 kbit/s
- Kódovací technologie algebraického kódového excitovaného lineárního prediktoru (ACELP)
- Délka rámce 20 ms se čtyřmi podrámci po 5 ms pro efektivní zpracování
- Sofistikovaná detekce hlasové aktivity a generování komfortního šumu
- Robustní mechanismy maskování chyb a obnovy po ztrátě rámců

## Související pojmy

- [AMR-NB – Adaptive Multi-Rate Narrowband](/mobilnisite/slovnik/amr-nb/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.813** (Rel-10) — Enhanced Voice Services for EPS Study
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 26.111** (Rel-19) — 3G-324M Terminal Specification for CS Multimedia
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.171** (Rel-19) — Introduction to AMR-WB Speech Processing
- **TS 26.173** (Rel-19) — AMR-WB Codec ANSI-C Implementation
- **TS 26.177** (Rel-19) — DSR Extended Advanced Front-end Test Sequences
- **TS 26.179** (Rel-19) — Codecs and Media Handling for MCPTT
- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.191** (Rel-19) — AMR-WB Error Concealment Procedure
- **TS 26.192** (Rel-19) — AMR-WB Comfort Noise Requirements
- **TS 26.204** (Rel-19) — AMR-WB Floating-Point Codec Specification
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- … a dalších 26 specifikací

---

📖 **Anglický originál a plná specifikace:** [AMR-WB na 3GPP Explorer](https://3gpp-explorer.com/glossary/amr-wb/)
