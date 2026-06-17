---
slug: "esp"
url: "/mobilnisite/slovnik/esp/"
type: "slovnik"
title: "ESP – Efficiency Speed Percentage product"
date: 2025-01-01
abbr: "ESP"
fullName: "Efficiency Speed Percentage product"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/esp/"
summary: "ESP je metrika výkonu pro digitální signálové procesory (DSP) v mobilních sítích, vypočítaná jako součin účinnosti (E), rychlosti (S) a procentuálního podílu výkonu (P). Kvantifikuje zpracovatelskou k"
---

ESP je metrika výkonu pro digitální signálové procesory (DSP), která kvantifikuje jejich zpracovatelskou kapacitu a energetickou účinnost výpočtem součinu účinnosti, rychlosti a procentuálního podílu výkonu.

## Popis

ESP (součin účinnosti, rychlosti a procentuálního podílu výkonu) je složená technická metrika definovaná 3GPP pro hodnocení a srovnávání výkonu digitálních signálových procesorů ([DSP](/mobilnisite/slovnik/dsp/)). DSP je specializovaný mikroprocesor používaný v telekomunikačních zařízeních k provádění úloh zpracování signálu v reálném čase, jako je kódování řeči a zvuku, potlačení ozvěn, detekce/generace tónů a modemové funkce. Metrika ESP se vypočítává jako ESP = E * S * P, kde 'E' představuje účinnost (míru zpracovatelské kapacity na jednotku složitosti, často vztaženou ke konkrétnímu kodeku), 'S' představuje rychlost (takť procesoru nebo rychlost provádění instrukcí) a 'P' představuje procentuální podíl výkonu (odrážející charakteristiky spotřeby DSP při zatížení). Tento součin dává jediné číslo jako kritérium pro srovnání různých implementací DSP.

Z architektonického hlediska jsou DSP klíčovými komponentami v mnoha síťových prvcích. V rádiové přístupové síti (RAN) DSP v jednotkách základnového pásma zpracovávají signály fyzické vrstvy pro modulaci, kódování a formování svazku. V jádru sítě používají mediální brány ([MGW](/mobilnisite/slovnik/mgw/)) DSP pro překódování mezi různými hlasovými kodeky (např. z [AMR](/mobilnisite/slovnik/amr/) na G.711) a pro konferenční mosty. Metrika ESP poskytuje výrobcům zařízení a síťovým operátorům standardizovaný způsob hodnocení kapacity a účinnosti těchto prostředků DSP. Vyšší hodnota ESP například indikuje DSP, které dokáže obsloužit více hlasových kanálů nebo vyšší datové toky při dané úrovni výkonu, což přímo souvisí s kapacitou a spotřebou energie síťového uzlu.

Metrika funguje tak, že každá komponenta je odvozena z podrobných měření a specifikací. 'Účinnost (E)' se často určuje benchmarkováním DSP vůči referenčnímu algoritmu zpracování signálu definovanému v testovacích specifikacích 3GPP (např. pro konkrétní řečový kodek jako AMR). Odráží, kolik instancí tohoto algoritmu může DSP spouštět souběžně. 'Rychlost (S)' je normalizovaná míra pracovní frekvence procesoru nebo [MIPS](/mobilnisite/slovnik/mips/) (miliónů instrukcí za sekundu). 'Procentuální podíl výkonu (P)' je faktor zohledňující spotřebu DSP, typicky definovaný jako procento vůči maximální nebo jmenovité spotřebě, což metrice umožňuje zahrnout energetickou účinnost. Součin je navržen tak, aby byl úměrný užitečné zpracovatelské práci, kterou DSP dokáže poskytnout.

Její role v síťovém ekosystému je primárně v oblasti zadávání veřejných zakázek, návrhu a plánování kapacity. Když výrobce vyvíjí mediální bránu nebo základnovou stanici, vybírá hardware DSP. Metrika ESP, na kterou odkazuje mnoho specifikací 3GPP (např. TS 29.368 pro řízení mediálních bran), umožňuje objektivní srovnání nabídek DSP od různých výrobců čipů. Pro síťové operátory pochopení ESP DSP v jejich nasazených zařízeních pomáhá při dimenzování – výpočtu, kolik simultánních hovorů nebo relací může mediální brána podporovat. Souvisí také s požadavky na napájení a chlazení v datových centrech a strojovnách. Přestože se jedná o metriku zaměřenou na hardware, má přímý dopad na software a služby, které síť může poskytovat, protože efektivnější DSP umožňují bohatší zpracování médií (jako je hlas ve vysoké kvalitě nebo transkódování videa v reálném čase) a snižují celkové náklady na vlastnictví.

## K čemu slouží

Metrika ESP byla vytvořena k řešení problému objektivního srovnávání výkonu různých digitálních signálových procesorů v kontextu telekomunikačních zařízení. V počátcích digitálních mobilních sítí (2G, 3G) se technologie [DSP](/mobilnisite/slovnik/dsp/) rychle vyvíjela a výrobci nabízeli procesory s různými architekturami, takty a instrukčními sadami. Výrobci síťového zařízení potřebovali standardizovaný způsob, jak vyhodnotit, který DSP poskytne požadovanou kapacitu (např. počet hlasových kanálů) a účinnost pro jejich produkty, aniž by se spoléhali pouze na tvrzení specifická pro daného výrobce, jako je [MIPS](/mobilnisite/slovnik/mips/), která mohou být zavádějící.

Historický kontext je spjat s rozšířením hlasových kodeků a funkcí zpracování médií v systémech 3GPP. Jak se sítě vyvíjely z GSM přes UMTS k LTE, zaváděly množství kodeků ([FR](/mobilnisite/slovnik/fr/), [EFR](/mobilnisite/slovnik/efr/), AMR, AMR-WB atd.) a pokročilé funkce jako provoz bez transkódování a multimediální konferenční hovory. To zvýšilo složitost benchmarkingu DSP. Součin ESP, zavedený ve vydání 4, poskytl vícerozměrnou metriku, která zachycovala nejen hrubou rychlost, ale také algoritmickou účinnost a spotřebu energie – klíčové faktory pro vysoce hustá, provozovatelské třídy zařízení, která musí nepřetržitě fungovat v prostředí s omezeným příkonem.

Dále ESP řešila ekonomické a provozní výzvy škálování sítí. Telekomunikační operátoři nakupují mediální brány a základnové stanice na základě kapacity (např. v erlangech nebo simultánních hovorech). Bez standardní metriky jako ESP bylo obtížné ověřit, zda zařízení různých výrobců využívají prostředky DSP srovnatelným způsobem. ESP umožnila přesnější plánování kapacity a spravedlivější srovnání během výběrových řízení. Také motivovala výrobce čipů DSP k optimalizaci nejen pro špičkový výkon, ale pro konkrétní úlohy zpracování signálu definované ve standardech 3GPP, čímž sladila vývoj hardwaru se skutečnými potřebami síťových operátorů po efektivní, vysokokapacitní a energeticky šetrné infrastruktuře.

## Klíčové vlastnosti

- Složená metrika výkonu pro digitální signálové procesory (DSP)
- Vypočítává se jako součin účinnosti (E), rychlosti (S) a procentuálního podílu výkonu (P)
- Poskytuje standardizované benchmarkování kapacity a energetické účinnosti DSP
- Používá se při dimenzování síťového zařízení, jako jsou mediální brány a základnové stanice
- Odkazuje se na ni v mnoha specifikacích 3GPP pro shodu zařízení
- Umožňuje objektivní srovnání hardwaru DSP od různých výrobců

## Související pojmy

- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.327** (Rel-12) — Mobility between I-WLAN and GPRS
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 29.368** (Rel-19) — Tsp Reference Point Stage 3 Specification
- **TS 29.468** (Rel-19) — MB2 Reference Point Protocol Definition
- **TS 33.141** (Rel-19) — Security for Presence Service (Ut reference point)
- **TS 33.203** (Rel-19) — IMS Security Specification
- **TS 33.210** (Rel-19) — UMTS Security for IP Networks
- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- **TS 33.402** (Rel-19) — Security for non-3GPP access to EPS
- **TS 33.820** (Rel-8) — Home NodeB/eNodeB Security Architecture
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [ESP na 3GPP Explorer](https://3gpp-explorer.com/glossary/esp/)
