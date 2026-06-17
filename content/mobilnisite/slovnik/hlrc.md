---
slug: "hlrc"
url: "/mobilnisite/slovnik/hlrc/"
type: "slovnik"
title: "HLRC – Home Location Register of the C subscriber"
date: 2025-01-01
abbr: "HLRC"
fullName: "Home Location Register of the C subscriber"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hlrc/"
summary: "HLRC je Home Location Register (HLR), který spravuje abonentní data pro 'C účastníka' ve scénáři přesměrování hovoru nebo konferenčního hovoru. Jedná se o logickou entitu definovanou pro specifické do"
---

HLRC je Home Location Register, který spravuje abonentní data pro 'C účastníka' v konkrétních doplňkových službách, jako je přesměrování hovorů nebo konferenční hovory.

## Popis

Home Location Register C účastníka (HLRC) je logická síťová entita definovaná v rámci specifikací 3GPP, konkrétně pro obsluhu určitých doplňkových služeb v okruhově komutovaných sítích. Na rozdíl od [HLRB](/mobilnisite/slovnik/hlrb/), který je zapojen do standardních mobilních příchozích hovorů, se HLRC uplatňuje během složitějších hovorových scénářů zahrnujících tři strany: účastníky A (volající), B (původně volaný) a C (přesměrovaný nebo přidaný). HLRC je [HLR](/mobilnisite/slovnik/hlr/), který obsahuje abonentní profil a servisní data pro tohoto třetího 'C účastníka'. Jeho primární rolí je poskytovat směrovací informace a autorizaci služby, když je hovor přesměrován na nebo zahrnuje tuto třetí stranu, jako u služeb Přesměrování hovoru ([ECT](/mobilnisite/slovnik/ect/)) nebo Konferenčního hovoru (MPTY).

Architektonicky je HLRC identický s jakýmkoli jiným HLR – jedná se o databázový uzel v jádru sítě. Jeho odlišení je čistě funkční a kontextové v rámci specifických signalizačních toků. Když účastník B iniciuje Přesměrování hovoru na účastníka C, obsluhující [MSC](/mobilnisite/slovnik/msc/) účastníka B zpracuje požadavek. Pro dokončení přesměrování může potřebovat vytvořit nové hovorové rameno k účastníkovi C. To vyžaduje dotaz na HLR účastníka C (HLRC) za účelem získání směrovacích informací, podle postupu podobného standardnímu nastavení příchozího hovoru. MSC (nebo vyhrazený Service Control Point v některých architekturách) odešle požadavek [MAP](/mobilnisite/slovnik/map/)_SEND_ROUTING_INFORMATION do HLRC. HLRC tento požadavek zpracuje ověřením servisního profilu C účastníka, kontrolou případných služeb zákazu nebo přesměrování hovorů a interakcí s aktuálním VLR C účastníka pro získání Mobile Station Roaming Number ([MSRN](/mobilnisite/slovnik/msrn/)) pro směrování.

Provoz HLRC je těsně integrován s servisní logikou doplňkových služeb definovanou v 3GPP TS 23.079. Používá stejná MAP rozhraní (C a D) jako HLRB. Klíčový rozdíl spočívá v triggeru a kontextu volání. Dotaz na HLRC není iniciován Gateway MSC pro příchozí hovor, ale typicky navštíveným MSC provádějícím servisní logiku pro aktivní hovor. To zdůrazňuje roli HLRC při umožnění dynamických interakcí funkcí během hovoru. Jeho správná funkce zajišťuje, že pokročilé služby jako Explicit Call Transfer, kde uživatel může přenést probíhající hovor na třetí číslo, fungují bezproblémově napříč síťovými hranicemi, včetně roamingu. HLRC tak rozšiřuje základní paradigma směrování založené na HLR pro podporu bohatších telefonních služeb.

## K čemu slouží

HLRC bylo definováno za účelem formalizace síťového chování a signalizace vyžadované pro pokročilé doplňkové služby zahrnující třetí stranu. Základní mobilní telefonie vyžadovala pouze správu dvou stran (A a B). Aby však zvýšily hodnotu a funkčnost mobilních sítí, standardizační orgány zavedly funkce jako Přesměrování hovoru a Konferenční hovor. Tyto funkce vytvářejí scénáře, kdy síť musí komunikovat a směrovat hovory k třetímu účastníkovi (C), jehož předplatné je nezávislé na původních dvou stranách. Koncept HLRC poskytuje jasný referenční bod ve standardech pro tuto interakci.

Řeší problém nejednoznačnosti služeb a zajišťuje konzistentní implementaci napříč různými síťovými dodavateli a operátory. Bez definovaného konceptu pro [HLR](/mobilnisite/slovnik/hlr/) C účastníka by signalizační postupy pro služby jako Explicit Call Transfer byly špatně specifikovány, což by vedlo k problémům s interoperabilitou. HLRC řeší omezení jednoduchého modelu účastníků A/B rozšířením osvědčeného mechanismu dotazování HLR na třetí stranu. To umožnilo operátorům nabízet sofistikované obchodní a osobní komunikační funkce využívající stejnou spolehlivou, centralizovanou infrastrukturu abonentní databáze. Jeho vytvoření bylo motivováno snahou vyrovnat se a překonat funkční sadu tradičních obchodních telefonních systémů (PBX) v mobilních sítích.

## Klíčové vlastnosti

- Ukládá trvalá abonentní data pro třetí stranu (C účastníka) ve službách s více účastníky
- Poskytuje směrovací informace (MSRN) pro scénáře přesměrování a přenosu hovorů
- Autorizuje vyvolání služby pro C účastníka (např. kontrolou zákazů)
- Integruje se s logikou doplňkových služeb definovanou v 3GPP TS 23.079
- Využívá standardní MAP signalizační rozhraní (C a D) pro dotazy a aktualizace
- Umožňuje pokročilé hovorové funkce jako Explicit Call Transfer a službu Konferenčního hovoru

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HLRB – Home Location Register of the B subscriber](/mobilnisite/slovnik/hlrb/)
- [ECT – Explicit Congestion Notification-Capable Transport](/mobilnisite/slovnik/ect/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [HLRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/hlrc/)
