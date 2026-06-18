---
slug: "fips"
url: "/mobilnisite/slovnik/fips/"
type: "slovnik"
title: "FIPS – Federal Information Processing Standard"
date: 2025-01-01
abbr: "FIPS"
fullName: "Federal Information Processing Standard"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/fips/"
summary: "Soubor bezpečnostních standardů americké vlády pro kryptografické moduly, odkazovaný v 3GPP pro zajištění robustní bezpečnosti v telekomunikačních systémech. Definuje požadavky na šifrování, autentiza"
---

FIPS je soubor bezpečnostních standardů americké vlády pro kryptografické moduly, odkazovaný v 3GPP k definování požadavků na šifrování, autentizaci a generování náhodných čísel v telekomunikačních systémech.

## Popis

Federal Information Processing Standard (FIPS) je soubor standardů vydávaných americkým Národním institutem pro standardy a technologie ([NIST](/mobilnisite/slovnik/nist/)), který specifikuje požadavky na kryptografické moduly používané k zabezpečení citlivých informací. V rámci 3GPP je na FIPS odkazováno, zejména v TS 33.916, aby bylo zajištěno, že bezpečnostní implementace v telekomunikačních sítích splňují vysoké úrovně důvěryhodnosti pro vládní aplikace a aplikace kritické infrastruktury. Nejde o standard vynalezený 3GPP, ale je přijímán a profilován tak, aby odpovídal potřebám telekomunikací. FIPS se vztahuje na hardwarové, softwarové a firmwarové kryptografické moduly, které provádějí funkce jako šifrování, dešifrování, digitální podpisy a bezpečná správa klíčů. Standard definuje úrovně zabezpečení (např. FIPS 140-2 úrovně 1–4) na základě robustnosti fyzické a logické ochrany, přičemž vyšší úrovně vyžadují přísnější opatření, jako jsou známky narušení nebo testování odolnosti vůči vlivům prostředí.

Jak FIPS funguje v kontextu 3GPP, zahrnuje integraci kompatibilních kryptografických modulů do síťových prvků, jako jsou základnové stanice, funkce jádra sítě nebo uživatelská zařízení, za účelem ochrany důvěrnosti, integrity a autenticity dat. Například v systémech 5G mohou být ověřené moduly FIPS použity ve funkci autentizačního serveru ([AUSF](/mobilnisite/slovnik/ausf/)) pro odvození klíčů nebo v uživatelské rovině ([UPF](/mobilnisite/slovnik/upf/)) pro šifrování uživatelských dat. Moduly procházejí důkladným testováním a ověřováním akreditovanými laboratořemi, aby bylo zajištěno dodržování požadavků FIPS, které zahrnují schválené algoritmy (např. [AES](/mobilnisite/slovnik/aes/) pro šifrování, [SHA](/mobilnisite/slovnik/sha/) pro hashování), bezpečné generování a ukládání klíčů a samotestování pro detekci chyb. Z architektonického hlediska je soulad s FIPS často implementován jako vyhrazená bezpečnostní vrstva uvnitř síťových komponent, která komunikuje s protokoly vyšších vrstev, jako je [IPsec](/mobilnisite/slovnik/ipsec/) nebo [TLS](/mobilnisite/slovnik/tls/), a poskytuje tak komplexní ochranu.

Klíčové součásti FIPS zahrnují samotný kryptografický modul, který zapouzdřuje bezpečnostní funkce, a související bezpečnostní politiky, které řídí jeho provoz. Standard ukládá funkce jako autentizace operátorů založená na rolích, auditní záznamy bezpečnostně relevantních událostí a zmírnění útoků vedlejšími kanály. V systémech 3GPP pomáhá FIPS řešit regulatorní požadavky, zejména pro operátory obsluhující vládní nebo podnikové zákazníky, kteří vyžadují certifikované zabezpečení. Jeho role sahá až k zajištění interoperability v nasazeních více dodavatelů tím, že poskytuje společný základní rámec pro bezpečnostní implementace, což snižuje zranitelnosti způsobené slabou kryptografií. Odkazováním na FIPS 3GPP zvyšuje celkovou bezpečnostní úroveň sítí, zejména v citlivých oblastech, jako je zákonné odposlouchávání, služby tísňového volání nebo finanční transakce přes mobilní sítě.

## K čemu slouží

FIPS byl začleněn do standardů 3GPP, aby řešil potřebu vysoké důvěryhodnosti kryptografického zabezpečení v telekomunikacích, zejména pro sítě používané vládními agenturami, armádou nebo kritickou infrastrukturou. Před jeho přijetím se bezpečnostní implementace u různých dodavatelů značně lišily, což vedlo k potenciálním slabinám a problémům s dodržováním předpisů v regulovaných odvětvích. Jak se telekomunikační sítě stávaly nedílnou součástí národní bezpečnosti a ekonomické stability, rostla poptávka po standardizovaných, ověřených bezpečnostních modulech, které by odolaly sofistikovaným útokům. FIPS poskytuje dobře zavedený, vládou podporovaný rámec, který zajišťuje kryptografickou robustnost, což motivovalo jeho zařazení do 3GPP od vydání 13 dále.

Historický kontext vychází z rostoucích kybernetických hrozeb a regulatorních nařízení, jako jsou například požadavky na soulad s FIPS pro federální systémy v USA. 3GPP uznalo, že telekomunikační sítě, zejména v 5G a dalších generacích, budou zpracovávat citlivá data vyžadující silnější ochranu, než nabízely základní standardy. Odkazováním na FIPS umožňuje 3GPP operátorům splnit tyto přísné požadavky bez nutnosti vyvíjet proprietární řešení, čímž podporuje důvěru a interoperabilitu. Řeší problémy, jako je nekonzistentní síla šifrování, slabé generování náhodných čísel a nedostatečná správa klíčů, které by mohly ohrozit integritu sítě.

Navíc FIPS řeší omezení dřívějších bezpečnostních přístupů, které se zaměřovaly primárně na zabezpečení na úrovni protokolu bez povinného zajištění podkladového modulu. Doplňuje nativní bezpečnostní mechanismy 3GPP (např. autentizaci 5G-AKA) přidáním hardwarového nebo softwarového základu, který je nezávisle ověřen. To je zásadní pro globální nasazení, kde musí sítě dodržovat různá národní nařízení, protože FIPS slouží jako měřítko vysoké bezpečnosti. FIPS v konečném důsledku existuje v rámci 3GPP proto, aby zvýšil základní úroveň zabezpečení, chránil před vyvíjejícími se hrozbami a podporoval bezpečné služby v citlivých prostředích, což je v souladu s průmyslovými trendy směřujícími k architekturám s nulovou důvěrou a odolnou komunikací.

## Klíčové vlastnosti

- Definuje úrovně zabezpečení (úrovně 1–4) pro kryptografické moduly na základě požadavků na důvěryhodnost
- Ukládá použití schválených algoritmů, jako jsou AES, SHA a RSA, pro šifrování a hashování
- Vyžaduje bezpečnou správu klíčů včetně generování, ukládání a vymazání (zeroization)
- Zahrnuje mechanismy fyzické a logické odolnosti proti narušení pro ochranu modulu
- Specifikuje možnosti samotestování a detekce chyb pro zajištění průběžné bezpečnosti
- Poskytuje ověření prostřednictvím akreditovaných zkušebních laboratoří pro certifikaci shody

## Související pojmy

- [NIST – National Institute of Standards and Technology](/mobilnisite/slovnik/nist/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)
- [TLS – Transport Layer Security](/mobilnisite/slovnik/tls/)

## Definující specifikace

- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [FIPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/fips/)
