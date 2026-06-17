---
slug: "msrd"
url: "/mobilnisite/slovnik/msrd/"
type: "slovnik"
title: "MSRD – Mobile Station Receive Diversity"
date: 2025-01-01
abbr: "MSRD"
fullName: "Mobile Station Receive Diversity"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/msrd/"
summary: "Mobile Station Receive Diversity (MSRD), známá také jako Downlink Advanced Receiver Performance (DARP) fáze II, je technika vylepšení přijímače uživatelského zařízení (UE) pro GSM. Využívá více antén"
---

MSRD je vylepšení přijímače mobilní stanice GSM, které využívá více antén nebo pokročilé zpracování ke zlepšení kvality, kapacity a pokrytí signálu na lince dolů, zejména v podmínkách omezených interferencí.

## Popis

Mobile Station Receive Diversity (MSRD) je funkce pro zvýšení výkonu definovaná pro mobilní stanice (terminály) GSM/[GPRS](/mobilnisite/slovnik/gprs/)/[EDGE](/mobilnisite/slovnik/edge/) ve specifikacích 3GPP. Spadá do širší kategorie vylepšení Downlink Advanced Receiver Performance ([DARP](/mobilnisite/slovnik/darp/)). MSRD konkrétně cílí na zlepšení příjmu na lince dolů v uživatelském zařízení (UE) využitím diverzitních technik pro potlačení úniků a interferencí. Primární metodou je anténní diverzita, kdy je UE vybaveno dvěma přijímacími anténami. Signály z těchto antén jsou kombinovány pomocí algoritmů, jako je Maximum Ratio Combining ([MRC](/mobilnisite/slovnik/mrc/)) nebo Selection Combining, za účelem vytvoření robustnějšího přijímaného signálu. Alternativně mohou být pod hlavičkou MSRD využity i pokročilé techniky potlačení interferencí pro jednu anténu (SAIC). Zlepšením poměru signálu k šumu a interferencím (SINR) umožňuje MSRD síti pracovat s vyššími faktory opakování kmitočtů, čímž zvyšuje celkovou kapacitu sítě. Také rozšiřuje pokrytí buňky tím, že umožňuje komunikaci při nižších úrovních signálu. Funkce je definována souborem požadavků na výkon (v TS 45.005 a souvisejících specifikacích), které musí UE splňovat, aby byla certifikována jako podporující MSRD. Síť může být informována o UE podporujících MSRD (prostřednictvím signalizace schopností) a může přizpůsobit správu rádiových prostředků, případně přidělovat kanály pro přenos s vyššími úrovněmi interference s vědomím, že je UE zvládne. Tím se zlepšuje spektrální účinnost v celé síti GSM.

## K čemu slouží

MSRD bylo vyvinuto pro řešení kritických omezení kapacity a kvality zralých sítí GSM. S růstem počtu účastníků GSM se sítě stávaly stále více omezené interferencí, přičemž ko-kanálové a sousední kanálové interference byly hlavními limity kapacity a kvality hovoru. Počáteční vylepšení přijímačů (jako [DARP](/mobilnisite/slovnik/darp/) fáze I) přinesla určité zisky, ale bylo potřeba více. MSRD (DARP fáze [II](/mobilnisite/slovnik/ii/)), zavedené v 3GPP Rel-8, poskytlo významný skok ve výkonu na lince dolů využitím diverzitního příjmu na mobilní stanici. Tím se vyřešil problém hlubokých úniků a silných interferencí, se kterými se potýkaly přijímače s jednou anténou. Umožnilo to operátorům zpřísnit vzory opakování kmitočtů a umístit více buněk a nosných do dané oblasti bez zhoršení kvality služeb. Motivací bylo prodloužit životnost a konkurenceschopnost sítí GSM tváří v tvář se vyvíjejícím 3G technologiím, a to dodáním více bitů na Hertz a zlepšením uživatelského zážitku, zejména na okrajích buněk a v hustých městských prostředích, aniž by bylo nutné okamžité hardwarové aktualizace v celé síti – pouze nové, schopné koncové přístroje.

## Klíčové vlastnosti

- Zlepšuje výkon na lince dolů v sítích GSM pomocí diverzitního příjmu nebo potlačení interferencí.
- Typicky implementována pomocí dvouanténového příjmu s algoritmy pro kombinaci signálu (např. MRC).
- Definována jako součást požadavků DARP (Downlink Advanced Receiver Performance) fáze II.
- Zvyšuje kapacitu sítě umožněním těsnějšího opakování kmitočtů a vyššího zatížení provozem.
- Zlepšuje pokrytí tím, že umožňuje spolehlivý příjem při nižších úrovních signálu.
- Zpětně kompatibilní; UE podporující MSRD fungují ve všech sítích GSM a poskytují výhody tam, kde jsou nasazeny.

## Související pojmy

- [DARP – Downlink Advanced Receiver Performance](/mobilnisite/slovnik/darp/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 45.015** (Rel-19) — DARP Phase II Requirements for Release 5 MS
- **TS 45.871** (Rel-14) — MIMO for GSM/EDGE Downlink Study
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [MSRD na 3GPP Explorer](https://3gpp-explorer.com/glossary/msrd/)
