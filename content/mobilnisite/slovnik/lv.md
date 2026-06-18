---
slug: "lv"
url: "/mobilnisite/slovnik/lv/"
type: "slovnik"
title: "LV – Length and Value"
date: 2025-01-01
abbr: "LV"
fullName: "Length and Value"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lv/"
summary: "Základní schéma kódování používané v protokolech 3GPP pro reprezentaci informačních prvků (IE) v zprávách. Skládá se z pole délky udávajícího velikost následujícího pole hodnoty, které obsahuje vlastn"
---

LV je základní schéma kódování protokolů 3GPP, ve kterém se informační prvek skládá z pole délky udávajícího velikost následujícího pole hodnoty obsahujícího vlastní data.

## Popis

Length and Value (LV) je základní formát kódování dat rozšířený napříč technickými specifikacemi 3GPP, dokumentovaný v TS 21.905 (Vocabulary for 3GPP Specifications). Používá se k zapouzdření informačních prvků ([IE](/mobilnisite/slovnik/ie/)) v protokolových zprávách, kde je každý IE reprezentován jako konkatenace ukazatele délky následovaného vlastní datovou hodnotou. Pole délky explicitně definuje velikost (v oktetech) pole hodnoty, což přijímajícím entitám umožňuje jednoznačně parsovat zprávy bez nutnosti spoléhat se na pevné pozice nebo oddělovače. Tento formát je zjednodušenou variantou kódování Type-Length-Value ([TLV](/mobilnisite/slovnik/tlv/)), která vynechává explicitní pole typu, je-li typ implicitně znám z kontextu.

Při činnosti LV kódování funguje tak, že nejprve specifikuje délku hodnotové složky. Samotné pole délky může mít pevnou nebo proměnnou velikost v závislosti na specifikaci protokolu; běžné implementace používají jeden nebo dva oktety. Například pole délky o jednom oktetu může reprezentovat velikosti hodnot od 0 do 255 oktetů. Za polem délky následuje pole hodnoty obsahující vlastní data, což může být jednoduché celé číslo, řetězec, vnořená LV struktura nebo jakákoli jiná binární či zakódovaná informace. Tato struktura umožňuje protokolům efektivně zpracovávat volitelné nebo proměnně dlouhé IE, protože přijímač může neznámé nebo nezpracovávané prvky přeskočit načtením délky a odpovídajícím posunutím ukazatele.

Z architektonického hlediska se LV používá v četných rozhraních a vrstvách 3GPP, včetně signalizace Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)), zpráv Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a managementových protokolů. Poskytuje flexibilní mechanismus pro rozšiřitelnost zpráv, což umožňuje přidávání nových IE v pozdějších vydáních bez narušení zpětné kompatibility, protože starší implementace je mohou ignorovat pomocí pole délky k jejich přeskočení. Kódování se typicky používá v binárních protokolech, kde jsou prioritou kompaktní reprezentace a rychlé parsování, na rozdíl od textových protokolů jako [XML](/mobilnisite/slovnik/xml/) nebo [JSON](/mobilnisite/slovnik/json/).

Role LV v síti je fundamentální: je základem spolehlivé výměny řídicích a uživatelských informací. Standardizací této metody kódování 3GPP zajišťuje interoperabilitu mezi síťovými prvky od různých dodavatelů. Technici navrhující nebo implementující protokoly 3GPP musí LV rozumět, aby mohli zprávy správně kódovat a dekódovat, protože nepřesnosti ve výpočtu délky mohou vést k chybám parsování, bezpečnostním zranitelnostem nebo selháním systému. Jeho jednoduchost a účinnost z něj činí pilíř filozofie návrhu protokolů 3GPP.

## K čemu slouží

LV kódování bylo zavedeno, aby vyřešilo potřebu flexibilní, efektivní a jednoznačné metody pro reprezentaci proměnně dlouhých dat v telekomunikačních protokolech. Starší telekomunikační systémy často používaly zprávy pevného formátu, které byly nepružné a nehospodárné při práci s volitelnými informacemi nebo budoucími rozšířeními. Jak se sítě 3GPP vyvíjely s 3G (UMTS) a dále, rostla složitost služeb a rozmanitost informačních prvků, což si vyžádalo schéma kódování schopné pojmout tento růst bez nutnosti přepracovávat celé struktury zpráv.

Primární problém, který LV řeší, je efektivní zpracování volitelných a proměnně dlouhých parametrů v binárních protokolech. Explicitním zahrnutím pole délky odstraňuje nejednoznačnost ohledně toho, kde jeden informační prvek končí a druhý začíná, což je klíčové pro spolehlivé parsování ve vysokorychlostních síťových prostředích. Tento přístup také usnadňuje zpětnou a dopřednou kompatibilitu; nové [IE](/mobilnisite/slovnik/ie/) lze připojit ke zprávám a starší přijímače je mohou přeskočit načtením délky, což zajišťuje plynulé síťové aktualizace a interoperabilitu mezi více dodavateli.

Historicky mají LV a jeho příbuzný [TLV](/mobilnisite/slovnik/tlv/) kořeny v ASN.1 BER kódování a dalších telekomunikačních standardech. 3GPP toto pragmatické kódování přijalo již dříve a standardizovalo ho ve vydání 5 jako součást slovníku, aby zajistilo konzistentní použití napříč specifikacemi. Vyřešilo tak omezení dřívějších ad-hoc metod kódování a poskytlo jednotný základ, který podporuje rozšiřitelnost vyžadovanou pro vyvíjející se funkce jako parametry QoS, bezpečnostní kontexty a informace o mobilitě, čímž budoucím způsobem pojistilo návrhy protokolů.

## Klíčové vlastnosti

- Explicitní pole délky pro jednoznačné parsování dat hodnoty
- Efektivně podporuje proměnně dlouhé informační prvky
- Umožňuje rozšiřitelnost protokolu a zpětnou kompatibilitu
- Široce používáno napříč signalizačními a managementovými protokoly 3GPP
- Umožňuje vnořování pro komplexní strukturovaná data
- Umožňuje přeskočení neznámých nebo volitelných prvků

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [LV na 3GPP Explorer](https://3gpp-explorer.com/glossary/lv/)
