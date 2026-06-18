---
slug: "t-im-csi"
url: "/mobilnisite/slovnik/t-im-csi/"
type: "slovnik"
title: "T-IM-CSI – Terminating IP Multimedia CAMEL Subscription Information"
date: 2025-01-01
abbr: "T-IM-CSI"
fullName: "Terminating IP Multimedia CAMEL Subscription Information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/t-im-csi/"
summary: "Profil CAMEL předplatitelských dat pro služby IP Multimedia Subsystem (IMS). Umožňuje řízení služeb pro ukončující se IMS relace, což síťovým operátorům umožňuje aplikovat vlastní logiku zpracování ho"
---

T-IM-CSI je profil CAMEL předplatitelských dat pro služby IMS, který umožňuje operátorovi řízení, například předplacené účtování nebo inteligentní směrování, pro ukončující se relace, když účastník přijímá hovor nebo zprávu.

## Popis

Terminating IP Multimedia [CAMEL](/mobilnisite/slovnik/camel/) Subscription Information (T-IM-CSI) je klíčový datový profil definovaný v architektuře 3GPP, konkrétně pro IP Multimedia Subsystem (IMS). Je součástí prostředí služeb CAMEL (Customised Applications for Mobile networks Enhanced Logic), přizpůsobeného pro služby založené na IMS. T-IM-CSI je uložen na Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) jako část služebního profilu účastníka. Když je k účastníkovi iniciována ukončující IMS relace (např. příchozí VoIP hovor nebo multimediální zpráva), Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) načte T-IM-CSI z HSS. K tomuto načtení dochází během procesu registrace nebo při navazování relace. T-IM-CSI obsahuje adresu příslušného CAMEL Service Environment ([CSE](/mobilnisite/slovnik/cse/)) nebo Application Server ([AS](/mobilnisite/slovnik/as/)), který hostuje servisní logiku pro ukončující se relaci.

Po přijetí T-IM-CSI používá S-CSCF tuto informaci k aktivaci provedení specifické servisní logiky pro ukončující větev relace. Toho je dosaženo přesměrováním signalizace relace (např. [SIP](/mobilnisite/slovnik/sip/) INVITE) na určený Application Server identifikovaný v T-IM-CSI. AS následně provede vlastní servisní logiku, která může zahrnovat širokou škálu funkcí. AS komunikuje se S-CSCF pomocí rozhraní IMS Service Control ([ISC](/mobilnisite/slovnik/isc/)), což mu umožňuje ovlivnit směrování relace, upravit signalizaci nebo komunikovat s dalšími síťovými prvky, jako jsou systémy účtování.

Role T-IM-CSI je zásadní pro umožnění operátorských a účastnických služeb na ukončující straně v síti IMS. Odděluje servisní logiku od základního řízení relace, což podporuje flexibilní servisní architekturu. Mezi klíčové zapojené komponenty patří HSS (pro ukládání), S-CSCF (pro načítání a aktivaci) a Application Server (pro provedení logiky). Tento mechanismus zajišťuje, že služby jako screening příchozích hovorů, překlad čísel, předplacené účtování za přijaté hovory nebo speciální tóny upozornění mohou být konzistentně aplikovány na základě profilu účastníka, a to i v komplexním SIP-basovaném prostředí IMS.

## K čemu slouží

T-IM-CSI byl vytvořen za účelem rozšíření osvědčeného paradigmatu řízení služeb inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) založeného na CAMEL do světa all-IP v IP Multimedia Subsystem (IMS). Před nástupem IMS byl CAMEL rozsáhle využíván v okruhově přepínané (CS) a paketově přepínané (PS) doméně pro služby jako předplacené, bezplatné nebo virtuální privátní sítě. Jak se sítě vyvíjely směrem k IMS pro poskytování hlasu, videa a zpráv přes IP, vznikla jasná potřeba podporovat stejnou sofistikovanou, operátorem řízenou servisní logiku pro relace směřující k účastníkovi (ukončující).

Bez T-IM-CSI by aplikace vlastní logiky na příchozí IMS relaci vyžadovala pevné zakódování servisních spouštěčů do CSCF nebo použití méně flexibilních mechanismů, což by omezovalo inovace a personalizaci služeb. T-IM-CSI tento problém řeší tím, že poskytuje standardizovanou, profilem řízenou metodu pro vyvolání externí servisní logiky. Řeší problém přenositelnosti a konzistence služeb, což operátorům umožňuje migrovat jejich stávající ukončující služby založené na CAMEL (např. inteligentní přesměrování hovorů) do domény IMS bez nutnosti kompletního přepsání servisní logiky. Jeho vytvoření bylo motivováno snahou využít stávající investice a expertízu v oblasti IN při přechodu na architekturu sítě příští generace, což zajišťuje plynulou evoluci a bohatou kontinuitu služeb pro účastníky.

## Klíčové vlastnosti

- Uložen v HSS jako součást IMS profilu účastníka
- Aktivován S-CSCF při pokusech o ukončující IMS relaci
- Obsahuje adresu (např. SIP URI) příslušného Application Server
- Umožňuje CAMEL styl řízení služeb pro relace založené na SIP
- Podporuje operátorem definovanou logiku pro zpracování hovorů, účtování a směrování na ukončující straně
- Využívá rozhraní IMS Service Control (ISC) mezi S-CSCF a AS

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [T-IM-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-im-csi/)
