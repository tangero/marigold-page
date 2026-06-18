---
slug: "hec"
url: "/mobilnisite/slovnik/hec/"
type: "slovnik"
title: "HEC – Header Error Control"
date: 2025-01-01
abbr: "HEC"
fullName: "Header Error Control"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hec/"
summary: "Header Error Control (HEC) je mechanismus cyklické redundance (CRC) aplikovaný na hlavičky paketů v transportních protokolech za účelem detekce bitových chyb. Zajišťuje integritu dat pro kritické řídi"
---

HEC je mechanismus cyklické redundance (CRC) aplikovaný na hlavičky paketů za účelem detekce bitových chyb, který zajišťuje integritu dat pro kritické řídicí informace v transportních protokolech.

## Popis

Header Error Control (HEC, kontrola chyb hlavičky) je základní mechanismus detekce chyb používaný v linkové vrstvě a transportních protokolech v rámci systémů 3GPP, zejména na rozhraních Iub/Iur/Iu pro UMTS a při rámcování určitých kanálů. Jedná se o formu cyklické redundance ([CRC](/mobilnisite/slovnik/crc/)), která se vypočítává nad poli hlavičky protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)). Jeho primární funkcí je detekce chyb, které mohly vzniknout během přenosu po fyzickém médiu, konkrétně v rámci hlavičkových informací, které jsou klíčové pro správné zpracování, směrování a multiplexování paketů. Vysílač vypočítá hodnotu HEC na základě bitů hlavičky a připojí ji k PDU. Příjemce nezávisle přepočítá HEC z přijaté hlavičky a porovná ji s přijatou hodnotou HEC; neshoda indikuje chybu hlavičky.

V technické implementaci, například v rámcovém protokolu ([FP](/mobilnisite/slovnik/fp/)) pro rozhraní Iub (specifikováno v 25.427), je HEC typicky 8bitové pole. Generující polynom použitý pro výpočet CRC je standardizován, aby byla zajištěna interoperabilita. HEC pokrývá všechna pole v hlavičce FP, která zahrnují informace jako číslo rámce spojení ([CFN](/mobilnisite/slovnik/cfn/)), indikátor transportního formátu a bity pro řízení výkonu. Když přijímač detekuje selhání HEC, standardním postupem je zahodit celý rámec. Důvodem je, že chybná hlavička by mohla vést k doručení uživatelských dat nesprávnému příjemci, nesprávnému časování nebo chybným příkazům pro řízení výkonu, což by mohlo být škodlivější než ztráta rámce. V některých implementacích nebo konfiguracích může kombinace dopředné korekce chyb ([FEC](/mobilnisite/slovnik/fec/)) na nižší vrstvě s HEC umožnit omezenou korekci chyb, ale primárním účelem návrhu je detekce.

Role HEC je odlišná, ale doplňková k detekci/korekci chyb prováděné na uživatelských datových přenosech (např. vrstvou [RLC](/mobilnisite/slovnik/rlc/)). Hlavičky vyžadují velmi vysokou míru integrity, protože jediná bitová chyba může způsobit nesprávné směrování nebo interpretaci celé PDU. Poskytnutím specializované, nenáročné kontroly hlavičky umožňuje HEC rychlé a spolehlivé ověření řídicích informací dříve, než jsou vynaloženy významné výpočetní prostředky na potenciálně poškozený přenos. To přispívá k celkové odolnosti a efektivitě transportní sítě v rádiové přístupové síti (RAN).

## K čemu slouží

HEC byl zaveden, aby řešil problém nezjištěných chyb v protokolových hlavičkách, které jsou katastrofální pro spolehlivost komunikace. Fyzické přenosové spoje, zejména bezdrátové backhaulové připojení, jsou náchylné k šumu, interferencím a útlumu, které mohou způsobit změny bitů. Bez detekce chyb by poškozená hlavička mohla vést k doručení rámce nesprávnému uživateli, aplikaci s nesprávným časováním nebo spuštění chybných řídicích akcí (jako nesprávné úpravy výkonu), což by degradovalo výkon a stabilitu sítě.

Motivací pro specializovanou kontrolu hlavičky, na rozdíl od spoléhání se pouze na [CRC](/mobilnisite/slovnik/crc/) přenosů nebo kontrol na vyšších vrstvách, je efektivita a specifičnost. Hlavičky jsou zpracovávány každým síťovým uzlem a jsou nezbytné pro vymezení rámců a směrování. Nenáročná CRC na hlavičce umožňuje mezilehlým uzlům nebo koncovému přijímači rychle ověřit integritu hlavičky a zahodit poškozené rámce již na začátku řetězce zpracování, čímž šetří prostředky a zabraňuje šíření chyb. To je obzvláště důležité pro řídicí data v reálném čase v RAN, kde jsou latence a spolehlivost kritické. HEC řeší omezení dopředné korekce chyb ([FEC](/mobilnisite/slovnik/fec/)) na nižší vrstvě, která nemusí zaručit zcela bezchybnou hlavičku, přidáním další cílené vrstvy ochrany pro nejkritičnější část protokolové datové jednotky.

## Klíčové vlastnosti

- Cyclic Redundancy Check (CRC) vypočítaný nad bity protokolové hlavičky
- Typicky 8bitové pole v rámcových protokolech (např. Frame Protocol)
- Umožňuje detekci bitových chyb vznikajících během přenosu
- Spouští zahození rámců s poškozenými hlavičkami, aby se zabránilo chybám zpracování
- Standardizovaný generující polynom pro interoperabilitu
- Doplňuje mechanismy detekce/korekce chyb přenosu

## Související pojmy

- [CRC – Cyclic Redundancy Check](/mobilnisite/slovnik/crc/)

## Definující specifikace

- **TS 25.411** (Rel-19) — Iu Interface Layer 1 Specification
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks

---

📖 **Anglický originál a plná specifikace:** [HEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/hec/)
