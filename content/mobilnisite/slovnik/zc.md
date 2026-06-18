---
slug: "zc"
url: "/mobilnisite/slovnik/zc/"
type: "slovnik"
title: "ZC – Zone Code"
date: 2025-01-01
abbr: "ZC"
fullName: "Zone Code"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/zc/"
summary: "Geografický identifikátor používaný v sítích 3GPP k definování konkrétní zóny pro lokalizační služby a správu sítě. Umožňuje síti uplatňovat politiky, směrování nebo služby na základě zóny uživatele a"
---

ZC je geografický identifikátor používaný v sítích 3GPP k definování konkrétní zóny pro uplatňování lokalizačních politik, směrování a služeb.

## Popis

Kód zóny (Zone Code, ZC) je standardizovaný identifikátor ve specifikacích 3GPP, který představuje definovanou geografickou oblast nebo zónu v mobilní síti. Je to základní prvek používaný pro lokalizační referencování, který umožňuje síti a aplikacím spojit polohu uživatelského zařízení (UE) s konkrétní logickou zónou. Samotný kód je typicky číselný nebo alfanumerický řetězec definovaný operátorem sítě nebo regulačními orgány a jeho struktura a přidělování jsou podrobně popsány v technických specifikacích 3GPP, především v TS 21.905 (Vocabulary for 3GPP Specifications).

Z architektonického hlediska ZC není samostatný síťový uzel, ale datový atribut používaný napříč různými síťovými funkcemi. Je generován, ukládán a zpracováván entitami jako Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) a v určitých scénářích i samotným UE. Když je poloha UE určena metodami jako Cell-ID, [OTDOA](/mobilnisite/slovnik/otdoa/) nebo [A-GNSS](/mobilnisite/slovnik/a-gnss/), síť může převést geografické souřadnice nebo informaci o obsluhující buňce na odpovídající kód zóny. Tento převod často vychází z předdefinovaných mapovacích tabulek nebo geografických informačních systémů (GIS) integrovaných do jádra sítě.

V provozu hraje ZC klíčovou roli v servisní logice. Například v lokalizačních službách ([LBS](/mobilnisite/slovnik/lbs/)) může aplikační server požadovat ZC účastníka namísto surových souřadnic, čímž zjednodušuje servisní logiku a nakládání s ochranou soukromí. Síť zpřístupňuje ZC prostřednictvím standardizovaných rozhraní, jako je rozhraní Le pro služby tísňového volání nebo rozhraní S6a/S6d pro data účastníka. Jeho hlavní rolí je abstrahovat přesnou polohu do říditelné, z hlediska politik relevantní oblasti, což umožňuje spouštění zónově specifických akcí pro účtování (např. tarify domácí zóny), zákonné odposlechy, regulatorní shodu (jako hranice států) a vylepšené směrování tísňových volání 911/112, kde je hovor směrován na příslušné středisko tísňového volání ([PSAP](/mobilnisite/slovnik/psap/)) na základě zóny.

## K čemu slouží

Kód zóny byl zaveden, aby řešil potřebu standardizované, na síť zaměřené metody identifikace geografických oblastí pro provozní a servisní účely. Před jeho standardizací používali operátoři proprietární nebo služebně specifické metody pro definování zón, což vedlo k problémům s interoperabilitou, zejména u roamujících účastníků a služeb napříč sítěmi, jako jsou tísňová volání. Nedostatek společného identifikátoru komplikoval účtování lokalizačních tarifů, regulatorní reporting a vývoj konzistentních lokalizačních aplikací.

Jeho vytvoření bylo motivováno vývojem mobilních sítí za hranice jednoduchých hlasových služeb směrem k bohatým datovým a lokalizačním nabídkám. Standardy jako [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile networks Enhanced Logic) pro inteligentní síťování a směrnice EU E112 pro lokalizaci tísňových volajících zdůraznily nutnost jednotné koncepce zóny. ZC poskytuje vrstvu abstrakce, která odděluje technické detaily lokalizace (které se mohou lišit v přesnosti a technologii) od servisní logiky, která potřebuje vědět, 've které zóně' se uživatel nachází. Tím se řeší problémy s přenositelností služeb a zjednodušuje se implementace složitých lokalizačně závislých politik napříč síťovými prostředími více dodavatelů.

## Klíčové vlastnosti

- Standardizovaný geografický identifikátor ve specifikacích 3GPP
- Umožňuje abstrakci přesných souřadnic do logických servisních oblastí
- Podporuje lokalizační účtování a vynucování politik
- Usnadňuje směrování služeb tísňového volání (např. na správné PSAP)
- Používá se pro regulatorní lokalizační reporting a zákonné odposlechy
- Integruje se se síťovými funkcemi jako HSS, GMLC a SCP pro servisní logiku

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [ZC na 3GPP Explorer](https://3gpp-explorer.com/glossary/zc/)
