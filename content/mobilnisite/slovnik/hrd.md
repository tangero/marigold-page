---
slug: "hrd"
url: "/mobilnisite/slovnik/hrd/"
type: "slovnik"
title: "HRD – Hypothetical Reference Decoder"
date: 2025-01-01
abbr: "HRD"
fullName: "Hypothetical Reference Decoder"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hrd/"
summary: "Teoretický model dekodéru používaný ve standardech videokódování (jako Advanced Video Coding - AVC a High Efficiency Video Coding - HEVC) k definici shody. Specifikuje matematicky přesný dekódovací pr"
---

HRD je teoretický model dekodéru používaný ve standardech videokódování k definici přesného dekódovacího procesu, který musí dodržovat všechny kompatibilní bitové toky a implementace, čímž zajišťuje interoperabilitu.

## Popis

Hypothetical Reference Decoder (HRD) je zásadní, normativní součástí standardů videokódování vyvinutých organizacemi [ITU-T](/mobilnisite/slovnik/itu-t/) a [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/), jako jsou H.264/[AVC](/mobilnisite/slovnik/avc/) a H.265/[HEVC](/mobilnisite/slovnik/hevc/), přičemž 3GPP tyto kodeky přijímá pro multimediální služby. Nejde o fyzickou implementaci, ale o abstraktní matematický model, který definuje hypotetický dekódovací proces se specifikovaným modelem bufferu a časovou osou operací. Primárním účelem HRD je poskytnout jednoznačnou definici kompatibilního bitového toku a kompatibilního dekodéru. Bitový tok je považován za vyhovující, pokud při jeho vstupu do modelu HRD podle pravidel standardu nedojde k přetečení nebo podtečení bufferu a je vytvořena deterministická výstupní sekvence obrazů.

Model HRD se skládá ze dvou klíčových konceptuálních komponent: Coded Picture Buffer ([CPB](/mobilnisite/slovnik/cpb/)) a Decoded Picture Buffer ([DPB](/mobilnisite/slovnik/dpb/)). CPB modeluje vstupní buffer dekodéru. Bitový tok přichází do CPB podle specifikovaného časového plánu příchodu (často vázaného na datový tok). HRD následně odebírá bity z CPB pro dekódování v přesných, předem stanovených časech, známých jako časy odebrání. Tím se modeluje proces dekódování. DPB modeluje paměť, která uchovává dekódované obrazy pro budoucí referenci (pro mezisnímkovou predikci) a pro výstupní zobrazení. HRD striktně definuje správu DPB, včetně ukládání, označování a odstraňování dekódovaných obrazů.

Fungování je definováno prostřednictvím řady rovnic a stavových proměnných. Standard definuje parametry HRD (jako počáteční zpoždění odebrání z CPB, datový tok, velikost bufferu), které mohou být signalizovány v bitovém toku (např. v Video Parameter Set nebo Sequence Parameter Set). Implementace dekodéru, aby byla standardu kompatibilní, musí produkovat stejný výstup jako HRD při zpracování kompatibilního bitového toku, ačkoli její vnitřní správa bufferu a časování se mohou lišit. HRD pracuje s konceptem 'hypotetického plánovače toku' a 'hypotetického dekodéru', který obrazy dekóduje okamžitě. Tato abstrakce odděluje logickou správnost bitového toku od časových omezení konkrétního hardwaru.

Ve specifikacích 3GPP je HRD klíčový pro definici bodů shody pro multimediální vysílací a streamovací služby, jako jsou [MBMS](/mobilnisite/slovnik/mbms/) a Packet-Switched Streaming Service (PSS). Zajišťuje, že video obsah zakódovaný jedním výrobcem může být spolehlivě dekódováno přijímačem od jiného výrobce, čímž garantuje základní interoperabilitu v celém ekosystému. Parametry HRD umožňují tvůrcům obsahu přizpůsobit bitový tok pro konkrétní scénáře doručování (např. streamování s konstantním nebo proměnným datovým tokem) a zároveň poskytují výrobcům dekodérů jasný cíl pro návrh správy bufferu.

## K čemu slouží

HRD existuje, aby řešil kritický problém interoperability v systémech digitálního videa. Před jeho formalizací standardy videokodeků primárně specifikovaly syntaxi bitového toku a dekódovací kroky pro jednotlivé bloky a obrazy. To však bylo nedostatečné pro zaručení, že kontinuální datový tok bude přijímačem s konečnou pamětí bufferu dekódovatelný v reálném čase. Bez standardizovaného modelu bufferu mohl bitový tok, který byl syntakticky správný, stále způsobit selhání reálného dekodéru tím, že by dodával data příliš rychle (přetečení bufferu) nebo příliš pomalu (podtečení bufferu způsobující zastavení dekodéru). HRD byl vytvořen, aby poskytl úplnou systémovou definici shody.

Historický kontext vychází z vývoje MPEG-2 Video, kde se správa bufferu stala hlavním problémem pro přenos s konstantním datovým tokem, jako jsou DVD a digitální vysílání. Koncept HRD byl formálněji a rigorózněji definován v H.264/AVC. Řeší omezení dřívějších, méně přesných specifikací tím, že poskytuje ověřitelný matematický model. To umožňuje generátorům bitových toků (enkodérům) testovat svůj výstup proti modelu a zajistit jeho 'dekódovatelnost', a návrhářům dekodérů znát minimální potřebné prostředky bufferu a správný výstupní pořádek.

Pro 3GPP bylo přijetí kodeků s dobře definovaným HRD zásadní pro spolehlivé doručování multimédií přes nepředvídatelné mobilní sítě. Umožňuje robustní streamovací služby tím, že umožňuje síti a klientovi dohodnout se na modelech bufferu a omezeních datového toku. HRD zajišťuje, že i za proměnných síťových podmínek, pokud bitový tok dodržuje signalizované parametry HRD, jej kompatibilní dekodér bude schopen dekódovat bez vnitřních chyb souvisejících s časováním nebo správou bufferu, čímž se udržuje kvalita služby pro koncového uživatele.

## Klíčové vlastnosti

- Definuje normativní, abstraktní model pro správu bufferu dekodéru (CPB a DPB)
- Poskytuje formální definici shody bitového toku a shody dekodéru
- Používá matematicky přesné plány odebrání a výstupu pro dekódovací operace
- Parametry HRD (počáteční zpoždění, datový tok, velikost bufferu) mohou být signalizovány v bitovém toku
- Zajišťuje interoperabilitu mezi enkodéry a dekodéry od různých výrobců
- Odděluje logický proces dekódování od implementačně specifických časových omezení

## Definující specifikace

- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [HRD na 3GPP Explorer](https://3gpp-explorer.com/glossary/hrd/)
