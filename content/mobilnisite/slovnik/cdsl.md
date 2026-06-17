---
slug: "cdsl"
url: "/mobilnisite/slovnik/cdsl/"
type: "slovnik"
title: "CDSL – Compressed Data Stream Length"
date: 2025-01-01
abbr: "CDSL"
fullName: "Compressed Data Stream Length"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cdsl/"
summary: "CDSL je parametr definovaný v 3GPP TS 23.042 pro kompresi SMS, který určuje délku komprimovaného datového proudu. Je nezbytný pro efektivní přenos SMS tím, že umožňuje síti správně parsovat komprimova"
---

CDSL je parametr pro kompresi SMS, který určuje délku komprimovaného datového proudu, což umožňuje správné parsování za účelem snížení velikosti přenášených dat a šetření rádiovými prostředky v sítích GSM a UMTS.

## Popis

Compressed Data Stream Length (CDSL) je technický parametr specifikovaný v 3GPP Technické specifikaci 23.042, která definuje kompresní mechanismy služby krátkých zpráv (SMS). Funguje jako kritické pole v rámci protokolových datových jednotek (PDU) používaných pro komprimované SMS zprávy. Konkrétně CDSL udává přesnou délku komprimovaného datového segmentu, která následuje ve zprávě, v oktetech. Tyto informace o délce jsou nezbytné pro přijímající entitu – ať už jde o mobilní stanici nebo síťový prvek – aby mohla správně vymezit a extrahovat komprimovaná data z okolních protokolových hlaviček a dalších informačních prvků. Bez přesné hodnoty CDSL by dekodér nebyl schopen určit, kde komprimovaná data končí, což by vedlo k chybám parsování a nedoručení zprávy.

Parametr je nedílnou součástí kompresního postupu definovaného pro SMS. Když je zpráva komprimována pomocí algoritmů, jako jsou ty založené na Huffmanově kódování nebo jiných specifikovaných kompresních metodách, jsou původní uživatelská data (UD) transformována na komprimovaný bitový proud. Tento komprimovaný proud je následně zapouzdřen do SMS Submit nebo Deliver PDU. Hodnota CDSL je vypočtena a vložena do vyhrazeného pole v rámci struktury PDU, typicky jako součást Hlavičky uživatelských dat (UDH) nebo v rámci specifických informačních prvků souvisejících s kompresí. Kódování délky musí být jednoznačné, aby přijímač mohl alokovat správnou velikost bufferu pro zpracování dekomprese. Dekompresní algoritmus pak tuto délku použije k přečtení přesně správného počtu bitů nebo oktetů před pokusem o rekonstrukci původního obsahu zprávy.

Z architektonického hlediska CDSL funguje v rámci aplikačního protokolu vrstvy 7 pro SMS a interaguje s podkladovými transportními vrstvami. Jeho role je čistě administrativní pro proces komprese/dekomprese; neúčastní se samotného kompresního algoritmu, ale je nezbytnou metadatovou komponentou. V síťovém provozu, když SMS centrum (SMSC) nebo mobilní stanice podporuje kompresi, bude generovat PDU obsahující CDSL. Mezilehlé síťové uzly, které SMS přeposílají, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN), typicky zacházejí s PDU transparentně a přeposílají jej bez interpretace CDSL, pokud nejsou specificky vybaveny možnostmi propojení SMS nebo komprese/dekomprese. Spolehlivost celé kompresní funkce závisí na přesném generování a interpretaci CDSL napříč různými implementacemi od různých výrobců.

Z procedurálního hlediska začlenění CDSL umožňuje dynamickou adaptaci na různé kompresní poměry. Různé zprávy se komprimují na různé velikosti a CDSL poskytuje flexibilitu pro efektivní označení této proměnné délky. Parametr je ve specifikaci definován s konkrétní bitovou délkou, která určuje maximální komprimovatelný datový proud, který může popsat. Tento návrh zajišťuje zpětnou kompatibilitu a interoperabilitu, protože zařízení, která nepodporují kompresi, mohou stále přijímat zprávy (často v nekomprimovaném režimu fallback) bez nesprávného pochopení struktury PDU, za předpokladu správného nastavení protokolových příznaků. CDSL je tedy základním, byť často přehlíženým prvkem, který umožňuje efektivní využití spektra a vylepšený uživatelský zážitek pro SMS v sítích 2G a 3G.

## K čemu slouží

CDSL byl vytvořen, aby řešil inherentní omezení služby krátkých zpráv (SMS) v raných digitálních celulárních sítích, konkrétně limit 160 znaků na segment SMS při použití výchozí 7bitové abecedy. Toto omezení se stalo významným problémem pro uživatelskou komunikaci, zejména pro delší zprávy, které by se rozdělily do více segmentů, což zvyšuje náklady, latenci a síťovou zátěž. Primární motivací bylo vyvinout standardizovaný kompresní mechanismus, který by mohl efektivně zvýšit informační obsah přenášený v rámci jedné SMS PDU, čímž by se zlepšil uživatelský zážitek a síťová efektivita. Kompresí textu nebo dat se do omezeného přenášeného objemu vešlo více informací, což snížilo počet potřebných segmentů pro danou zprávu.

Technický problém, který CDSL řeší, je potřeba spolehlivého a jednoznačného způsobu komunikace velikosti komprimovaného datového bloku v rámci SMS protokolu. Kompresní algoritmy produkují výstupní proudy proměnné délky v závislosti na entropii a vzorcích v původním textu. Přijímací zařízení musí přesně vědět, kolik oktetů tvoří komprimovaná data, aby je mohlo správně oddělit od ostatních protokolových polí a předat správné množství dat do dekompresního enginu. Bez definovaného ukazatele délky, jako je CDSL, by protokol vyžadoval alternativní, složitější metody rámcování, jako je použití specifických oddělovačů (které by se mohly vyskytnout v datovém proudu) nebo komprese s pevnou délkou, což by bylo velmi neefektivní. CDSL poskytuje jednoduché, robustní řešení, které se bezproblémově integruje do stávající struktury SMS PDU definované v dřívějších vydáních.

Historicky byly komprese SMS a CDSL zavedeny v 3GPP Release 99, což odpovídá době, kdy využití SMS explodovalo a síťoví operátoři hledali způsoby, jak optimalizovat provoz bez nutnosti upgradů základních transportních mechanismů. Předchozí přístupy buď kompresi nepoužívaly a trpěly segmentovým limitem, nebo se spoléhaly na proprietární, neinteroperabilní řešení. Standardizace komprese s CDSL v rámci 3GPP TS 23.042 zajistila interoperabilitu mezi více výrobci a umožnila mobilním telefonům a síťovému vybavení od různých výrobců spolehlivě vyměňovat komprimované zprávy. Vyřešila tak omezení čistě transparentního přenosu dat přidáním lehkého, nezbytného metadatového pole, které umožnilo významný skok v datové efektivitě pro jednu z nejpopulárnějších mobilních služeb své doby.

## Klíčové vlastnosti

- Určuje přesnou délku v oktetech komprimovaných dat přenášených v rámci SMS PDU
- Umožňuje přijímající entitě správně parsovat a extrahovat komprimovaná data
- Podporuje výstupy proměnné délky z kompresních algoritmů definovaných v TS 23.042
- Integruje se do Hlavičky uživatelských dat (UDH) SMS nebo specifických informačních prvků pro přenos
- Nezbytný pro interoperabilitu mezi kompresními implementacemi různých výrobců
- Usnadňuje efektivní využití rádiových prostředků snížením počtu potřebných segmentů SMS

## Definující specifikace

- **TS 23.042** (Rel-19) — Data Compression and Decompression for 3GPP

---

📖 **Anglický originál a plná specifikace:** [CDSL na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdsl/)
