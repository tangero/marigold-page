---
slug: "rwb"
url: "/mobilnisite/slovnik/rwb/"
type: "slovnik"
title: "RWB – Resolution Bandwidth"
date: 2025-01-01
abbr: "RWB"
fullName: "Resolution Bandwidth"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rwb/"
summary: "Rozlišovací šířka pásma (RWB) je měřicí parametr v 3GPP specifikacích pro testování shody rádiových kmitočtů. Definuje šířku pásma mezifrekvenčního filtru ve spektrálním analyzátoru a ovlivňuje přesno"
---

RWB je měřicí parametr v testování shody rádiových kmitočtů podle 3GPP, který definuje šířku pásma mezifrekvenčního filtru spektrálního analyzátoru a ovlivňuje přesnost měření výkonu signálu a nežádoucích emisí.

## Popis

Rozlišovací šířka pásma (RWB) je klíčový parametr definovaný v technických specifikacích 3GPP, zejména v dokumentech pro testování shody jako je TS 21.905 (Slovník pro specifikace 3GPP). Odkazuje na šířku pásma mezifrekvenčního ([IF](/mobilnisite/slovnik/if/)) filtru používaného ve spektrálním analyzátoru nebo podobném měřicím přijímači při provádění měření ve frekvenční oblasti. V podstatě RWB určuje schopnost měřicího zařízení rozlišit spektrální složky, které jsou blízko u sebe ve frekvenci. Užší RWB poskytuje vyšší frekvenční rozlišení, umožňující detekci jemných spektrálních detailů, ale vyžaduje delší dobu měření kvůli sníženému šumovému pásmu. Naopak širší RWB umožňuje rychlejší měření, ale může rozmazat blízko umístěné signály, čímž snižuje přesnost.

Z architektonického hlediska je RWB implementována v rámci měřicího uspořádání používaného pro testování rádiového výkonu uživatelského zařízení (UE) a základnových stanic. V typickém spektrálním analyzátoru prochází vstupní signál směšovačem, který jej převede na mezifrekvenci, kde je aplikován IF filtr s nastavitelnou šířkou pásma (RWB). Tento filtr tvaruje šumové a signálové pásmo před detekcí. Mezi klíčové komponenty patří lokální oscilátor pro frekvenční převod, soustava IF filtrů a detektor obálky. Volba RWB ovlivňuje měření, jako je výkon kanálu, poměr úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)), nežádoucí emise a shoda s maskou spektrální emise ([SEM](/mobilnisite/slovnik/sem/)). Pro testy 3GPP specifikace často předepisují konkrétní hodnoty RWB, aby zajistily konzistentní a reprodukovatelné výsledky v různých laboratořích.

Fungování RWB spočívá v její roli při hledání kompromisu mezi rychlostí měření, šumovým podložím a frekvenčním rozlišením. Při měření výkonové spektrální hustoty signálu filtr RWB integruje energii ve svém propustném pásmu. Naměřený výkon je úměrný součinu výkonové spektrální hustoty a RWB. Pro šumové signály širší RWB propouští více šumového výkonu, čímž zvyšuje šumové podloží. Proto se pro citlivá měření, jako jsou nežádoucí emise, používá úzká RWB pro dosažení nižšího šumového podloží a detekci slabých signálů. U modulovaných signálů se širokým pásmem, jako jsou nosné 5G NR, však musí být RWB dostatečně široká, aby zachytila celý signál bez zkreslení, a zároveň přesně specifikovaná, aby se předešlo chybám měření. Kalibrační postupy zajišťují přesnost nastavení RWB, protože chyby mohou vést k nesplnění požadavků v regulačním testování.

Role RWB v síti je zásadní pro zajištění toho, aby rádiová zařízení splňovala požadavky 3GPP a regulatorní požadavky na spektrální čistotu a kontrolu interference. Standardizací hodnot RWB v testovacích specifikacích 3GPP zaručuje, že UE a základnové stanice od různých výrobců vykazují konzistentní rádiový kmitočtový výkon, čímž předcházejí škodlivému rušení a zajišťují efektivní využití spektra. Je nedílnou součástí procesů typového schvalování a testování shody, což ovlivňuje certifikaci zařízení pro komerční nasazení. RWB tedy není jen detail měření, ale klíčový faktor umožňující interoperabilitu a správu spektra v mobilních sítích.

## K čemu slouží

RWB byla definována za účelem standardizace metodik měření rádiových kmitočtů v celém odvětví, což zajišťuje přesné a srovnatelné hodnocení výkonu vysílačů a přijímačů. Před standardizací mohly testovací laboratoře používat různá nastavení rozlišovací šířky pásma, což vedlo k nekonzistentním výsledkům měření, jako jsou nežádoucí emise nebo výkon kanálu. Tato variabilita mohla způsobit, že zařízení prošla testy v jedné laboratoři, ale v jiné nikoli, což vytvářelo nejistotu pro výrobce a regulátory. RWB poskytuje jednotný parametr pro řízení frekvenční selektivity měřicího zařízení, čímž řeší tento problém reprodukovatelnosti.

Motivace pro specifikaci RWB v dokumentech 3GPP vychází z potřeby přísného testování shody pro udržení kvality sítě a dodržování globálních spektrálních předpisů. Jak se mobilní technologie vyvíjely od 2G po 5G, šířky pásma signálů se zvětšovaly a masky emisí se stávaly složitějšími, což vyžadovalo přesné měřicí techniky. RWB umožňuje testovacím inženýrům vyvažovat protichůdné požadavky na přesnost, rychlost a citlivost měření. Například při testování širokopásmových signálů 5G NR zajišťují vhodná nastavení RWB správné změření jak emisí v pásmu, tak mimopásmových emisí, čímž se předchází rušení sousedních kanálů.

Historicky koncept rozlišovací šířky pásma vychází z návrhu analogových spektrálních analyzátorů, ale 3GPP je formalizovala ve svém slovníku a testovacích specifikacích počínaje Release 5. Toto začlenění řešilo omezení ad-hoc měřicích postupů a poskytlo společný jazyk a technický základ pro všechny zúčastněné strany. Definováním RWB umožňuje 3GPP vývoj konzistentních testovacích plánů, kalibračních postupů a kritérií shody, která jsou nezbytná pro globální interoperabilitu mobilních zařízení. Podporuje ekosystém tím, že zkracuje dobu uvedení nového zařízení na trh a zajišťuje, že sítě fungují efektivně bez rušivého vlivu interference.

## Klíčové vlastnosti

- Definuje šířku pásma IF filtru ve spektrálních analyzátorech pro měření ve frekvenční oblasti
- Ovlivňuje kompromis mezi frekvenčním rozlišením, šumovým podložím a rychlostí měření
- Standardizována v testovacích specifikacích 3GPP pro reprodukovatelné testování shody
- Kritická pro přesná měření výkonu kanálu, ACLR a nežádoucích emisí
- Zajišťuje konzistentní hodnocení rádiového výkonu v různých testovacích laboratořích
- Podporuje shodu s regulatorními maskami spektrálních emisí a limity interference

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [RWB na 3GPP Explorer](https://3gpp-explorer.com/glossary/rwb/)
