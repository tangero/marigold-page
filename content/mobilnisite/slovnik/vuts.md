---
slug: "vuts"
url: "/mobilnisite/slovnik/vuts/"
type: "slovnik"
title: "VUTS – VAMOS Uplink Test Scenario"
date: 2025-01-01
abbr: "VUTS"
fullName: "VAMOS Uplink Test Scenario"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/vuts/"
summary: "Standardizovaný testovací scénář pro ověření výkonu VAMOS (Voice services over Adaptive Multi-user channels on One Slot) v uplinku v sítích GSM/EDGE. Definuje specifické rádiové podmínky a provozní mo"
---

VUTS je standardizovaný testovací scénář pro GSM/EDGE, který definuje specifické rádiové podmínky a provozní modely pro ověření výkonu VAMOS v uplinku s ohledem na jeho schopnost zdvojnásobení hlasové kapacity.

## Popis

[VAMOS](/mobilnisite/slovnik/vamos/) Uplink Test Scenario (VUTS) je podrobný rámec pro testování shody a výkonu definovaný ve specifikaci 3GPP 51.021. Je speciálně navržen pro vyhodnocení provozu technologie VAMOS (Voice services over Adaptive Multi-user channels on One Slot) v uplinku (od mobilní stanice k základnové stanici) v rámci GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). VAMOS je klíčová funkce umožňující sdílení stejného fyzického rádiového časového slotu a kmitočtu dvěma hlasovým hovorům pomocí pokročilé modulace a řízení výkonu, čímž efektivně zdvojnásobuje hlasovou kapacitu na stávající GSM infrastruktuře. VUTS poskytuje řízené, opakovatelné laboratorní prostředí pro ověření, že síťové zařízení a mobilní stanice správně implementují složité procedury VAMOS pro uplink.

Testovací scénář funguje simulací specifických podmínek rádiového kanálu, včetně definovaných úrovní rušení, profilů útlumu (jako modely Typical Urban nebo Rural Area) a požadované síly signálu. Stanovuje přesný provozní model, ve kterém testovací mobilní stanice, vystupující jako spárovaný uživatel VAMOS, vysílá svůj signál v uplinku. Scénář definuje parametry signálu druhého spárovaného uživatele, který je simulován jako řízený rušivý zdroj s definovaným výkonem a modulací. Jádrem testu je schopnost testované základnové stanice ([BTS](/mobilnisite/slovnik/bts/)) správně demodulovat oba překrývající se signály modulované [GMSK](/mobilnisite/slovnik/gmsk/) nebo [QPSK](/mobilnisite/slovnik/qpsk/) na stejném časovém slotu za využití algoritmů pro potlačení rušení a adaptivního odhadu kanálu. Mezi klíčové měřené ukazatele výkonu patří Bit Error Rate ([BER](/mobilnisite/slovnik/ber/)), Frame Erasure Rate ([FER](/mobilnisite/slovnik/fer/)) a úspěšná aplikace technik Downlink Advanced Receiver Performance (DARP) a Uplink Noise and Interference Cancellation (UNIC) v přijímači BTS.

Role VUTS v síťovém ekosystému je klíčová pro zajištění interoperability a garantované úrovně výkonu. Před nasazením infrastruktury nebo koncových zařízení podporujících VAMOS musí tyto projít standardizovanými testy, aby prokázaly, že dokážou udržet kvalitu hovoru i v náročných podmínkách provozu se spárovanými kanály. Toto ověření je zásadní, protože VAMOS posouvá hranice tradičního oddělení kanálů v GSM a vyžaduje, aby přijímače dokázaly rozlišit dva uživatele, jejichž signály nejsou ortogonální. Poskytnutím přísného měřítka VUTS zajišťuje, že slibované kapacitní zisky VAMOS jsou dosaženy v reálných sítích bez degradace kvality hovoru, při zachování zpětné kompatibility se staršími zařízeními bez podpory VAMOS a umožnění konzistentního výkonu napříč zařízeními různých výrobců.

## K čemu slouží

VUTS byl vytvořen, aby vyřešil kritický problém ověření a standardizace výkonu přenosové cesty v uplinku u technologie VAMOS. Před VAMOS byla hlasová kapacita GSM zásadně omezena paradigmatem jednoho uživatele na časový slot. Zatímco VAMOS sliboval zdvojnásobení kapacity tím, že umožnil dvěma uživatelům sdílet slot, přineslo to významné nové výzvy pro uplink. Uplink je pro sdílení více uživateli inherentně složitější než downlink, protože signály od dvou nezávislých mobilů přicházejí do BTS bez přesné synchronizace, což vytváří neortogonální scénář omezený rušením. Bez standardizovaného testu mohl každý výrobce implementovat a měřit výkon VAMOS odlišně, což vedlo k potenciálním selháním interoperability a nepředvídatelné kvalitě sítě.

Historický kontext představoval intenzivní tlak na operátory GSM koncem roku 2000, aby zvládli rostoucí hlasový provoz v omezeném kmitočtovém spektru. VAMOS bylo přelomové, nákladově efektivní řešení, které se vyhnulo potřebě nového spektra nebo stanovišť. Jeho novátorské využití adaptivní modulace a potlačení rušení však bylo v GSM bezprecedentní. Účelem VUTS tedy bylo poskytnout na úrovni standardů nezbytný "důkaz konceptu". Poskytl výrobcům zařízení jasný cíl pro návrh přijímačů a dal operátorům jistotu, že funkce zdvojnásobení kapacity bude spolehlivě fungovat při integraci do živých sítí. Řešil omezení spočívající v absenci objektivního způsobu, jak porovnat výkon VAMOS u různých přijímačů BTS, a zajistil tak, že technologie přinese své teoretické výhody do praxe.

## Klíčové vlastnosti

- Standardizované podmínky rušení a útlumu v uplinku pro opakovatelné testování
- Ověření schopnosti přijímače BTS demodulovat dva překrývající se signály GMSK/QPSK
- Měření klíčových metrik kvality (BER, FER) za provozu se spárovanými kanály VAMOS
- Ověření algoritmů Uplink Noise and Interference Cancellation (UNIC)
- Podpora testování s mobilními stanicemi staršími i s podporou VAMOS
- Definice požadavků na referenční citlivost a výkon potlačení rušení

## Související pojmy

- [VAMOS – Voice services over Adaptive Multi-user Channels on One Slot](/mobilnisite/slovnik/vamos/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [DARP – Downlink Advanced Receiver Performance](/mobilnisite/slovnik/darp/)
- [GMSK – Gaussian Minimum Shift Keying](/mobilnisite/slovnik/gmsk/)

## Definující specifikace

- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [VUTS na 3GPP Explorer](https://3gpp-explorer.com/glossary/vuts/)
