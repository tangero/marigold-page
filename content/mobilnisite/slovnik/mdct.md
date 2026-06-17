---
slug: "mdct"
url: "/mobilnisite/slovnik/mdct/"
type: "slovnik"
title: "MDCT – Modified Discrete Cosine Transform"
date: 2025-01-01
abbr: "MDCT"
fullName: "Modified Discrete Cosine Transform"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mdct/"
summary: "MDCT je překrývající se transformace používaná pro efektivní kompresi audio signálu v 3GPP kodecích, jako je Enhanced Voice Services (EVS) a AMR-WB+. Převádí audio vzorky z časové oblasti na koeficien"
---

MDCT je překrývající se transformace používaná v 3GPP audiokodecích k převodu vzorků v časové oblasti na koeficienty ve frekvenční oblasti za účelem efektivní, vysoce kvalitní komprese audia s nízkým datovým tokem.

## Popis

Modifikovaná diskrétní kosinová transformace (MDCT) je klíčový algoritmus zpracování signálu v rámci 3GPP audiokodeků, jako je například kodek Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) specifikovaný v TS 26.410 a TS 26.411. Patří do rodiny překrývajících se transformací, navržených ke zpracování audio rámců s 50% překryvem mezi po sobě jdoucími bloky. Tato překrývající se struktura je klíčová pro její výkon; pomáhá zmírnit blokové artefakty – slyšitelné nespojitosti, které se mohou vyskytnout na hranicích rámců u tradičních blokových transformací – a tím poskytuje plynulejší a kvalitnější rekonstrukci audia, zejména při nižších datových tocích.

Technicky MDCT funguje tak, že vezme otevřený segment audio vzorků v časové oblasti a transformuje je na sadu koeficientů ve frekvenční oblasti. K vstupnímu signálu je aplikována okenní funkce, typicky sinusové nebo Kaiser-Bessel odvozené ([KBD](/mobilnisite/slovnik/kbd/)) okno, za účelem snížení spektrálního úniku. 50% překryv znamená, že každý vzorek přispívá ke dvěma po sobě jdoucím transformacím, což poskytuje redundanci. Během inverzní transformace (IMDCT) tento proces překrytí a sečtení rekonstruuje původní signál dokonale při absenci kvantizace, což je vlastnost známá jako potlačení aliasingu v časové oblasti (TDAC). Díky tomu je MDCT obzvláště efektivní, neboť se jedná o formu kriticky vzorkované banky filtrů.

V rámci architektury 3GPP kodeku se MDCT často používá ve spojení s dalšími nástroji, jako je lineární prediktivní kódování ([LPC](/mobilnisite/slovnik/lpc/)) pro řeč nebo modifikované diskrétní sinusové transformace ([MDST](/mobilnisite/slovnik/mdst/)) pro určitá pásma. V EVS je například MDCT použito pro kódování vysokofrekvenčního pásma nebo celého signálu v režimu obecného audia. Transformační koeficienty jsou následně kvantovány a entropicky kódovány podle percepčního modelu, který přiděluje bity na základě sluchových maskovacích prahů. Celý tento proces umožňuje kodeku dosáhnout transparentní audio kvality při tocích již od 9,6 kbps pro řeč až po 128 kbps pro hudbu, což tvoří páteř služeb vysokokvalitního hlasu v sítích LTE a 5G.

## K čemu slouží

MDCT byla zavedena, aby uspokojila potřebu vysoce efektivní a kvalitní komprese audia v mobilních sítích. Předchozí techniky transformačního kódování, jako standardní diskrétní kosinová transformace ([DCT](/mobilnisite/slovnik/dct/)) používaná v dřívějších kodecích, trpěly při nízkých datových tocích blokovými artefakty, které degradovaly percepční kvalitu audia. Překrývající se struktura MDCT s jejím inherentním potlačením aliasingu v časové oblasti byla vyvinuta, aby tyto artefakty odstranila bez obětování kódovací efektivity, což umožnilo robustní přenos audia přes bezdrátové kanály s omezenou šířkou pásma.

Její přijetí ve standardech 3GPP, zejména od Release 8 s [AMR-WB](/mobilnisite/slovnik/amr-wb/)+ a později v [EVS](/mobilnisite/slovnik/evs/), bylo hnáno vývojem mobilních služeb od základní telefonie k multimediální komunikaci. Spotřebitelé požadovali studiově kvalitní hlas a streamování hudby, což vyžadovalo kodeky schopné poskytovat vynikající audio věrnost při proměnných datových tocích a zároveň zachovat odolnost vůči ztrátám paketů. Matematické vlastnosti MDCT ji pro tento účel učinily ideální, neboť poskytuje téměř optimální časově-frekvenční reprezentaci pro percepční kódování, což umožňuje návrhářům kodeků agresivně využívat psychoakustické principy k odstranění neslyšitelných složek signálu.

Navíc MDCT umožnila sjednocení kódování řeči a audia v rámci jediného kodekového rámce. Tradiční řečové kodeky se silně spoléhaly na zdrojové modely (jako [LPC](/mobilnisite/slovnik/lpc/)), které špatně fungovaly pro neřečové signály, jako je hudba. Začleněním MDCT mohou 3GPP kodeky jako EVS plynule přepínat mezi režimy specifickými pro řeč a režimy obecného audio kódování, což zajišťuje optimální výkon napříč širokým spektrem audio obsahu. Tato univerzálnost byla klíčová pro podporu pokročilých služeb, jako je Voice over LTE (VoLTE), vysokokvalitní hlasové hovory a multimediální streamování, a tvoří základní technologii pro audio zážitek v moderních celulárních sítích.

## Klíčové vlastnosti

- Překrývající se transformace s 50% překryvem mezi po sobě jdoucími bloky pro prevenci blokových artefaktů
- Poskytuje dokonalou rekonstrukci prostřednictvím potlačení aliasingu v časové oblasti (TDAC) při absenci kvantizace
- Používá se pro frekvenční kódování jak řečových, tak obecných audio signálů v 3GPP kodecích
- Umožňuje vysokou kompresní efektivitu prostřednictvím percepční kvantizace frekvenčních koeficientů
- Podporuje proměnné velikosti rámců a tvary oken (např. sinusové, KBD) pro adaptivní zpracování signálu
- Integrální součást kodeku Enhanced Voice Services (EVS) pro vysokokvalitní hlas v sítích LTE a 5G

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.255** (Rel-19) — IVAS Frame Loss Concealment Procedure
- **TS 26.410** (Rel-19) — Enhanced aacPlus Floating-Point ANSI-C Code
- **TS 26.411** (Rel-19) — Enhanced aacPlus Fixed-Point ANSI-C Code

---

📖 **Anglický originál a plná specifikace:** [MDCT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdct/)
