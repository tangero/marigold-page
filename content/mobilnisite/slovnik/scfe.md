---
slug: "scfe"
url: "/mobilnisite/slovnik/scfe/"
type: "slovnik"
title: "SCFE – Shared Control Function Entity"
date: 2025-01-01
abbr: "SCFE"
fullName: "Shared Control Function Entity"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/scfe/"
summary: "Funkční entita v UTRAN, která spravuje sdílené rádiové prostředky pro více uživatelů, zejména v kontextu HSDPA. Zajišťuje plánování, správu priorit a řídicí signalizaci pro sdílené kanály, čímž optima"
---

SCFE je funkční entita v UTRAN, která spravuje sdílené rádiové prostředky tím, že zajišťuje plánování a řídicí signalizaci pro sdílené kanály, zejména za účelem optimalizace vysokorychlostních paketových datových služeb, jako je HSDPA.

## Popis

Shared Control Function Entity (SCFE, entita sdílené řídicí funkce) je komponenta v rámci UMTS Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), specificky definovaná ve specifikacích 3GPP pro správu sdílených rádiových prostředků. Funguje primárně v Node B (základnové stanici) a je úzce spojena s funkcionalitou High-Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)). SCFE je zodpovědná za řízení sdílených kanálů, jako je High-Speed Downlink Shared Channel ([HS-DSCH](/mobilnisite/slovnik/hs-dsch/)), které se používají pro dynamické doručování paketových dat více uživatelům. Její klíčové funkce zahrnují plánování datových přenosů, správu priorit mezi uživateli a zajišťování řídicí signalizace související s alokací sdílených prostředků. Díky centralizaci těchto řídicích aspektů umožňuje SCFE efektivní využití rádiové šířky pásma a přizpůsobení se proměnlivým požadavkům na provoz a stavům kanálu.

Z architektonického hlediska SCFE komunikuje s dalšími entitami UTRAN, jako je Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) a uživatelské zařízení (UE). Přijímá od RNC řídicí informace týkající se parametrů kvality služby (QoS) a uživatelských priorit a poté provádí rozhodnutí o plánování v reálném čase na úrovni Node B. To zahrnuje výběr, kterému UE bude obsluhováno v každém přenosovém časovém intervalu ([TTI](/mobilnisite/slovnik/tti/)), určování modulačních a kódovacích schémat a alokaci výkonových a kódových prostředků. SCFE také spravuje přidružené řídicí kanály, jako je High-Speed Shared Control Channel ([HS-SCCH](/mobilnisite/slovnik/hs-scch/)), který přenáší downlinkovou signalizaci, aby informoval UE o nadcházejících datových přenosech. Tato řídicí smyčka s nízkou latencí umožňuje rychlou adaptaci na měnící se rádiové podmínky, čímž zlepšuje propustnost a spolehlivost.

Role SCFE je klíčová pro podporu vysokorychlostních datových služeb v UMTS, protože umožňuje zisky ze statistického multiplexování díky sdílení prostředků mezi více uživateli. Funguje ve spojení s funkcemi, jako je adaptivní modulace a kódování ([AMC](/mobilnisite/slovnik/amc/)) a hybridní [ARQ](/mobilnisite/slovnik/arq/) (HARQ), za účelem optimalizace výkonu. Zatímco její význam je spojen s HSDPA ve vydáních 5 a novějších, koncept sdíleného řízení je základem pozdějších pokroků v LTE a NR, kde existují podobné plánovací entity. SCFE je příkladem posunu k distribuovanému, rychlému plánování v rádiových přístupových sítích, který přesouvá řízení blíže k rozhraní vzduchu za účelem zvýšení efektivity dat a uživatelského zážitku.

## K čemu slouží

SCFE byla zavedena, aby řešila neefektivitu alokace vyhrazených kanálů pro paketové datové služby v raných vydáních UMTS. Zpočátku UMTS spoléhalo na vyhrazené kanály pro data, které byly neefektivní pro trhavý provoz kvůli statickému přiřazování prostředků a vyšší latenci. S růstem internetových aplikací vznikla potřeba vyšších datových rychlostí a lepšího využití prostředků, což vedlo k HSDPA. SCFE umožnila provoz se sdílenými kanály, což umožnilo dynamickou alokaci prostředků mezi více uživateli na základě poptávky v reálném čase a kvality kanálu.

Přesunutím plánovacích a řídicích funkcí do Node B (prostřednictvím SCFE) snížil 3GPP latenci a zlepšil odezvu ve srovnání s centralizovaným řízením v RNC. Tím se vyřešila omezení při zpracování proměnlivého datového provozu a podpořily se pokročilé techniky, jako je rychlá adaptace spoje a HARQ. SCFE usnadnila poskytování vysokorychlostních downlinkových služeb, čímž splnila očekávání uživatelů ohledně rychlejšího přístupu k internetu a umožnila nové aplikace, jako je streamování videa. Její vytvoření bylo motivováno snahou odvětví o rádiový přístup optimalizovaný pro pakety, což připravilo cestu pro vyvinutější architektury v pozdějších technologiích.

## Klíčové vlastnosti

- Spravuje sdílené rádiové prostředky pro více uživatelů v UTRAN
- Provádí dynamické plánování a správu priorit pro kanály HSDPA
- Zajišťuje řídicí signalizaci pro alokace sdílených kanálů (např. HS-SCCH)
- Funguje na Node B pro rozhodování s nízkou latencí
- Podporuje adaptivní modulaci a kódování (AMC) a hybridní ARQ (HARQ)
- Umožňuje efektivní statistické multiplexování paketového datového provozu

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [HS-DSCH – High Speed Downlink Shared Channel](/mobilnisite/slovnik/hs-dsch/)

## Definující specifikace

- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [SCFE na 3GPP Explorer](https://3gpp-explorer.com/glossary/scfe/)
