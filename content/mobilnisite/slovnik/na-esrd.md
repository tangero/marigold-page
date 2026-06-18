---
slug: "na-esrd"
url: "/mobilnisite/slovnik/na-esrd/"
type: "slovnik"
title: "NA-ESRD – North American - Emergency Service Routing Digits"
date: 2025-01-01
abbr: "NA-ESRD"
fullName: "North American - Emergency Service Routing Digits"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/na-esrd/"
summary: "Sada číslic používaná v severoamerických sítích k směrování nouzových volání na příslušné středisko tísňového volání (Public Safety Answering Point, PSAP). Je odvozena z polohy volajícího a vytočeného"
---

NA-ESRD je sada číslic používaná v severoamerických mobilních sítích k směrování nouzového volání na správné středisko tísňového volání (Public Safety Answering Point) na základě polohy volajícího a vytočeného čísla.

## Popis

North American - Emergency Service Routing Digits (NA-ESRD) je směrovací mechanismus definovaný pro tísňové služby v Severní Americe, který je v souladu se specifikacemi 3GPP pro IMS nouzová volání. ESRD je klíčový parametr, typicky 10místné číslo odpovídající formátu severoamerického číslovacího plánu (North American Numbering Plan, [NANP](/mobilnisite/slovnik/nanp/)), používaný k směrování nouzové relace ze zdrojové sítě do správné sítě tísňových služeb a nakonec k příslušnému středisku tísňového volání (Public Safety Answering Point, [PSAP](/mobilnisite/slovnik/psap/)). Nejde o číslo, které lze vytočit, ale o identifikátor generovaný sítí na základě přibližné polohy volajícího (bunka, sektor nebo přesnější poloha, je-li dostupná) a typu požadované tísňové služby (např. 911). ESRD je vložen do signalizace protokolu Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) při IMS nouzovém volání, v polích jako Request-URI a hlavička P-Asserted-Identity.

Technický proces začíná, když UE zahájí nouzové volání. UE nebo síť určí potřebu nouzové relace na základě vytočených číslic. Obsluhující síť, což může být navštívená síť v případech roamingu, použije informace o poloze (např. Cell Global Identity, adresu z [GPS](/mobilnisite/slovnik/gps/)) k dotazu na funkci překladu polohy na službu nebo použije lokální konfigurační mapy. Tento proces vygeneruje příslušné ESRD, které odpovídá PSAP obsluhujícímu danou geografickou oblast. Toto ESRD je pak použito jako cílová adresa pro požadavek SIP INVITE. Volání je směrováno přes IP síť, potenciálně prostřednictvím funkce Emergency Call Session Control Function ([E-CSCF](/mobilnisite/slovnik/e-cscf/)) a Border Control Function ([BCF](/mobilnisite/slovnik/bcf/)), do sítě tísňových služeb, která použije ESRD k výběru konečného PSAP.

Z architektonického hlediska je NA-ESRD součástí frameworku IMS nouzových volání definovaného v 3GPP TS 23.167 a souvisejících specifikacích. Funguje ve spojení s dalšími tísňovými identifikátory, jako je Emergency Service Query Key ([ESQK](/mobilnisite/slovnik/esqk/)), a informacemi o poloze volajícího (poskytnutými prostřednictvím [PIDF-LO](/mobilnisite/slovnik/pidf-lo/)). ESRD zajišťuje, že volání dorazí k PSAP, který je schopen jej obsloužit, a to ještě předtím, než je přesná poloha volajícího sdělena verbálně. To je zásadní pro tichá volání nebo volání, kdy volající není schopen mluvit. Funkce je spravována a provozována síťovými operátory ve spolupráci s národními orgány tísňových služeb, což zajišťuje přesnost a aktuálnost mapování mezi geografickými oblastmi a hodnotami ESRD. Jeho zařazení do standardů 3GPP zajišťuje interoperabilitu pro nouzová volání pocházející ze sítí založených na 3GPP (jako LTE a 5G) v kontextu severoamerických regulatorních požadavků.

## K čemu slouží

NA-ESRD byl vytvořen, aby vyřešil kritický problém přesného a efektivního směrování nouzových volání z moderních IP mobilních sítí na správné místní středisko tísňového volání v Severní Americe. Tradiční okruhově spínaný systém 911 používal pro směrování volané číslo a informace o buňce/sektoru. S migrací na plně IP jádrové sítě, jako je IMS, byl vyžadován standardizovaný, spolehlivý digitální směrovací mechanismus, který by zachoval a vylepšil stávající schopnosti tísňových služeb. ESRD toto poskytuje tím, že představuje směrovatelné číslo, které zapouzdřuje přibližnou servisní oblast volajícího, což umožňuje IP síti nasměrovat volání na příslušný PSAP bez nutnosti spoléhat se na starší okruhově spínané trunky založené pouze na telefonním čísle volajícího.

Historický kontext zahrnuje vývoj severoamerického systému 911 směrem k Next Generation 911 (NG911), což je systém založený na IP. Definice NA-ESRD v 3GPP zajišťuje, že mobilní sítě 3GPP mohou bezproblémově komunikovat se sítěmi NG911. Řeší omezení dřívějších metod, kde směrování na základě polohy v paketově spínaných sítích nebylo standardizováno, což mohlo vést k chybně směrovaným voláním a opožděné reakci záchranných služeb. Mechanismus ESRD umožňuje podrobnější směrování než jen na oblast pokrytí buňky, protože může být odvozen z přesnějších informací o poloze, jsou-li dostupné, čímž podporuje požadavky enhanced 911 (E911) Fáze II pro bezdrátové operátory.

Dále NA-ESRD podporuje regulatorní soulad pro mobilní síťové operátory v USA, Kanadě a dalších regionech následujících NANP. Umožňuje zákonné zpracování nouzových volání, včetně těch od roamujících účastníků, tím, že poskytuje konzistentní směrovací klíč, který mohou sítě tísňových služeb zpracovat. Také usnadňuje funkci zpětného volání; pokud volání selže, může PSAP zavolat zpět pomocí ESRD, které je směrováno zpět do příslušné sítě a obecné oblasti původního volajícího. Jeho účel je tedy zásadní pro veřejnou bezpečnost, neboť zajišťuje, že život zachraňující funkce nouzového volání je zachována a vylepšena při přechodu na 5G a plně paketově spínané telekomunikační architektury.

## Klíčové vlastnosti

- 10místné směrovací číslo pro nouzová volání ve formátu NANP
- Odvozeno z polohy volajícího a typu požadované tísňové služby
- Vloženo do SIP signalizace jako cílová adresa pro směrování IMS nouzových volání
- Umožňuje směrování na správné středisko tísňového volání (Public Safety Answering Point, PSAP)
- Podporuje procedury zpětného volání ze strany PSAP do zdrojové sítě
- Nezbytné pro interoperabilitu Next Generation 911 (NG911) se sítěmi 3GPP

## Definující specifikace

- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)

---

📖 **Anglický originál a plná specifikace:** [NA-ESRD na 3GPP Explorer](https://3gpp-explorer.com/glossary/na-esrd/)
