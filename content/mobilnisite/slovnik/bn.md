---
slug: "bn"
url: "/mobilnisite/slovnik/bn/"
type: "slovnik"
title: "BN – Bit Number"
date: 2025-01-01
abbr: "BN"
fullName: "Bit Number"
category: "Physical Layer"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/bn/"
summary: "Bitové číslo (BN) je základní koncept ve specifikacích 3GPP, který identifikuje pozici konkrétního bitu v rámci datové struktury, rámce nebo protokolové datové jednotky. Poskytuje přesnou adresaci jed"
---

BN (Bit Number) je číslo, které identifikuje pozici konkrétního bitu v rámci datové struktury, rámce nebo protokolové datové jednotky ve specifikacích 3GPP.

## Popis

Bitové číslo (BN) je systematický indexovací mechanismus používaný v celých technických specifikacích 3GPP k odkazování na jednotlivé bity v definovaných datových strukturách. Tyto struktury zahrnují protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)), transportní bloky, řídicí zprávy a různé formáty rámců používané jak v rádiové přístupové síti (RAN), tak v jádrové síti (CN). Každému bitu v rámci struktury je přiřazeno jedinečné BN, typicky začínající od 0 nebo 1, které slouží jako absolutní souřadnicový systém pro daný konkrétní datový formát.

Systém BN funguje hierarchicky ve vnořených datových strukturách. U složitých protokolových zpráv obsahujících více informačních prvků ([IE](/mobilnisite/slovnik/ie/)) má každý IE svou vlastní interní adresaci BN, zatímco celá zpráva zachovává hlavní sekvenci BN. To umožňuje inženýrům přesně lokalizovat konkrétní bity reprezentující kritické parametry, jako jsou indikátory kvality služeb (QoS), bezpečnostní klíče, příznaky správy mobility nebo uživatelská datová užitečná zatížení. Odkazy na BN jsou hojně používány v diagramech specifikací, testovacích postupech a implementačních pokynech k zajištění interoperability mezi zařízeními různých výrobců.

V praktické implementaci plní BN více technických funkcí. Během procesů kódování určuje BN přesnou pozici, na kterou jsou umístěny konkrétní informační bity v rámci přenosových rámců. Během dekódování pomáhá BN extrahovat a interpretovat přijaté bity podle předdefinovaných formátů. To je obzvláště důležité pro pole s proměnnou délkou a volitelné parametry, kde pozice následujících bitů závisí na předchozích prvcích. Systém BN také usnadňuje bitové operace, jako je maskování, posun a kontrola chyb, tím, že poskytuje jednoznačné odkazy pro každou bitovou pozici.

V různých technických specifikacích 3GPP se BN objevuje v různých kontextech se stejnými principy, ale specifickým použitím. Ve specifikacích rádiového rozhraní (jako 45.912) identifikuje BN bity v rámcích fyzické vrstvy a transportních kanálů. Ve specifikacích zabezpečení (jako 31.117 a 31.127) odkazuje BN na bity v rámci kryptografických algoritmů a funkcí odvozování klíčů. Ve specifikacích terminologie (jako 21.905) poskytuje BN základní definici, která zajišťuje konzistentní použití ve veškeré dokumentaci 3GPP. Tato univerzálnost činí z BN klíčový koncept pro pochopení toho, jak jsou bity organizovány a zpracovávány v celém protokolovém zásobníku.

## K čemu slouží

Bitové číslo (BN) bylo zavedeno k řešení základní výzvy jednoznačné specifikace bitových pozic v rámci složitých digitálních komunikačních systémů. Jak se standardy 3GPP vyvíjely od jednoduchých hlasových služeb k sofistikovaným datovým a multimediálním aplikacím, protokolové struktury se stávaly stále složitějšími se stovkami parametrů zakódovaných v binárních formátech. Bez standardizovaného systému adresace bitů mohly různé implementace interpretovat bitové pozice rozdílně, což vedlo k problémům s interoperabilitou a výpadkům komunikace mezi síťovými prvky různých výrobců.

Zavedení BN vyřešilo problém přesné technické specifikace na nejpodrobnější úrovni. Předchozí přístupy často používaly relativní popisy jako „třetí bit za hlavičkou“ nebo nejednoznačné termíny, které vedly k rozdílům v implementaci. BN poskytlo absolutní souřadnicový systém, který odstranil nejednoznačnost, což umožnilo autorům specifikací přesně definovat, který bit nese kterou informaci. To bylo obzvláště důležité pro volitelné parametry, podmíněná pole a prvky s proměnnou délkou, kde pozice bitů závisí na předchozím obsahu ve zprávě.

Historicky se potřeba BN stala zřejmou během přechodu ze systémů 2G na 3G, kde se složitost protokolů dramaticky zvýšila. Zavedení paketově přepínaných datových služeb v Rel-5 vyžadovalo sofistikovanější řídicí signalizaci a formáty uživatelských dat. BN umožnilo přesnou specifikaci těchto nových struktur při zachování zpětné kompatibility se stávajícími systémy. Poskytnutím konzistentního schématu adresace na úrovni bitů BN snížilo implementační chyby, zjednodušilo testovací a validační postupy a zajistilo, že všechna kompatibilní zařízení budou interpretovat protokolové zprávy shodně, bez ohledu na výrobce.

## Klíčové vlastnosti

- Absolutní adresování bitové pozice v rámci datových struktur
- Univerzální použití napříč všemi protokolovými vrstvami 3GPP
- Umožňuje přesnou specifikaci volitelných a podmíněných polí
- Usnadňuje bitové operace, jako je maskování a posun
- Podporuje kódování parametrů s proměnnou délkou
- Poskytuje základ pro testování interoperability

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.117** (Rel-19) — USIM Application Toolkit Test for Non-Removable UICC
- **TS 31.127** (Rel-18) — UICC-terminal interaction testing specification
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [BN na 3GPP Explorer](https://3gpp-explorer.com/glossary/bn/)
