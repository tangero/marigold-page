---
slug: "chi"
url: "/mobilnisite/slovnik/chi/"
type: "slovnik"
title: "CHI – Command Header Identifier"
date: 2002-01-01
abbr: "CHI"
fullName: "Command Header Identifier"
category: "Other"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/chi/"
summary: "Command Header Identifier (CHI) je pole používané v architektuře zákonného odposlechu (LI) definované 3GPP. Jednoznačně identifikuje konkrétní typ příkazu nebo zprávy v rámci protokolu předávacího roz"
---

CHI je pole v architektuře zákonného odposlechu 3GPP, které jednoznačně identifikuje typ příkazu nebo zprávy na předávacím rozhraní (Handover Interface) pro spolehlivé doručování příkazů k odposlechu a hlášení.

## Popis

Command Header Identifier (CHI) je kritická komponenta v rámci architektury zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)) 3GPP, konkrétně používaná na standardizovaném předávacím rozhraní ([HI](/mobilnisite/slovnik/hi/)). HI je rozhraní mezi zařízením pro monitorování vynucování zákona ([LEMF](/mobilnisite/slovnik/lemf/)) – systémem na straně orgánu – a jedním či více řídicími prvky odposlechu ([ICE](/mobilnisite/slovnik/ice/)) v doméně síťového operátora, jako je například SGSN nebo GGSN v [GPRS](/mobilnisite/slovnik/gprs/)/UMTS jádrových sítích. CHI je pole v rámci protokolových datových jednotek (PDU) vyměňovaných na tomto rozhraní. Jeho primární funkcí je jednoznačně identifikovat typ odesílaného příkazu nebo typ doručovaného hlášení, čímž slouží jako identifikátor typu zprávy, který určuje, jak musí přijímající entita zpracovat a analyzovat přidružená datová část.

Technicky je CHI definováno jako součást specifikace protokolu HI (rozhraní [HI2](/mobilnisite/slovnik/hi2/) a [HI3](/mobilnisite/slovnik/hi3/)) založené na ASN.1. Každá operace zákonného odposlechu, jako je aktivace odposlechu, deaktivace nebo doručení hlášení o informacích souvisejících s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) či obsahu komunikace (CC), je reprezentována specifickým typem příkazu nebo zprávy. Hodnota CHI v hlavičce PDU tento typ signalizuje přijímači. Například jedna hodnota CHI odpovídá příkazu 'activateIntercept' z LEMF do ICE, zatímco jiná, odlišná hodnota CHI odpovídá hlášení 'IRIReport' odesílanému z ICE do LEMF. Toto jasné rozlišení je zásadní pro spolehlivý, stavovým automatem řízený provoz relace odposlechu.

Architektura se spoléhá na CHI, aby zajistila správné provedení složitých, vícestupňových procedur odposlechu. Po přijetí PDU síťová entita (ICE nebo LEMF) nejprve prozkoumá CHI. Na základě tohoto identifikátoru vyvolá příslušnou obslužnou funkci a použije odpovídající definici struktury ASN.1 k dekódování zbytku těla zprávy, které obsahuje parametry jako identifikátor cíle (např. IMSI), rozsah odposlechu a adresy pro doručení. Toto oddělení identifikace příkazu (prostřednictvím CHI) od analýzy parametrů je základním návrhovým vzorem, který zvyšuje robustnost protokolu, zjednodušuje implementaci a zajišťuje, že poškozené nebo neočekávané zprávy mohou být odmítnuty nebo zpracovány řádným způsobem, což je prvořadé pro právně citlivý systém.

V širší architektuře LI je role CHI základní, ale omezená. Neřídí samotnou logiku odposlechu, ale je klíčem, který odemyká správnou interpretaci každé transakce na HI. Její standardizovaná definice napříč všemi 3GPP-kompatibilními síťovými prvky a LEMF je tím, co umožňuje interoperabilitu mezi různými dodavateli. Orgán činný v trestním řízení může vydat příkaz k odposlechu pomocí zařízení od dodavatele A a bude správně pochopen a proveden jádrovým síťovým uzlem od dodavatele B právě proto, že oba dodržují stejné hodnoty CHI a přidružené struktury zpráv, jak jsou kodifikovány v 3GPP TS 33.108 a protokolově specifických specifikacích jako TS 29.228 (pro IMS). Tato interoperabilita je nezbytným požadavkem pro fungování zákonného odposlechu v moderních heterogenních sítích.

## K čemu slouží

Command Header Identifier (CHI) bylo vytvořeno, aby vyřešilo zásadní problém v automatizaci a standardizaci zákonného odposlechu napříč globálními telekomunikačními sítěmi. Před komplexními standardy, jako jsou ty od 3GPP, byly mechanismy odposlechu často proprietární, specifické pro dodavatele nebo pro danou zemi. To vytvářelo významné překážky pro orgány činné v trestním řízení (LEA), které potřebovaly odposlouchávat komunikaci v sítích postavených ze zařízení od více dodavatelů, a pro síťové operátory, kteří čelili složitým a nákladným integračním výzvám pro každé nové rozhraní LEA nebo upgrade sítě. CHI jako součást standardizovaného protokolu HI poskytuje společný 'jazyk' pro příkazy k odposlechu.

Konkrétním účelem CHI je zajistit jednoznačnou komunikaci. V právně nařízeném a technicky složitém procesu, jako je zákonný odposlech, není tolerance k nesprávné interpretaci. Příkaz k 'aktivaci odposlechu' se nikdy nesmí zaměnit za 'doručovací hlášení'. Pole CHI funguje jako tento jednoznačný štítek. Jeho vytvoření bylo motivováno potřebou robustního, stavově orientovaného protokolu, který by mohl spravovat celý životní cyklus odposlechu – aktivaci, periodická hlášení, doručování obsahu a deaktivaci – přes potenciálně nespolehlivé síťové IP spojení mezi LEA a operátorem. Tím, že jasně identifikuje každý typ zprávy, umožňuje CHI přijímacímu systému udržovat správný stav relace a provádět správné procedury, což je klíčové pro zachování integrity důkazů a dodržování soudních příkazů.

CHI dále usnadňuje škálovatelnost a budoucí rozvoj. Když jsou vyžadovány nové typy zpráv souvisejících s odposlechem nebo vylepšené schopnosti (např. pro nové služby jako IMS nebo 5G), lze definovat a standardizovat nové hodnoty CHI bez nutnosti přepracování celého protokolového rámce. To umožňuje architektuře zákonného odposlechu vyvíjet se spolu se samotnou sítí. CHI tedy není jen technickým polem, ale umožňovatelem standardizovaného, interoperabilního a právně shodného ekosystému odposlechu, který vyvažuje operační potřeby LEA s technickými a obchodními realitami síťových operátorů.

## Klíčové vlastnosti

- Jednoznačně identifikuje typy příkazů a hlášení zákonného odposlechu
- Umožňuje spolehlivou analýzu a zpracování zpráv protokolu HI
- Tvoří základ pro stavově orientovaný provoz relací odposlechu
- Zajišťuje interoperabilitu mezi různými dodavateli zařízení LEMF a síťového vybavení
- Usnadňuje jednoznačnou komunikaci pro právně citlivé operace
- Umožňuje rozšiřitelnost protokolu definicí nových hodnot

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management

---

📖 **Anglický originál a plná specifikace:** [CHI na 3GPP Explorer](https://3gpp-explorer.com/glossary/chi/)
