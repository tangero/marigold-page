---
slug: "foob"
url: "/mobilnisite/slovnik/foob/"
type: "slovnik"
title: "FOOB – Frequency Offset Out-of-Band boundary"
date: 2025-01-01
abbr: "FOOB"
fullName: "Frequency Offset Out-of-Band boundary"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/foob/"
summary: "Definovaná frekvenční hranice v 5G NR, která odděluje oblast emisí mimo pásmo (Out-of-Band, OOB) od oblasti nežádoucích emisí (Spurious). Jde o klíčový referenční bod pro testy RF shody, který určuje,"
---

FOOB je definovaná frekvenční hranice v 5G NR, která odděluje oblast emisí mimo pásmo (Out-of-Band) od oblasti nežádoucích emisí (Spurious) pro testy RF shody.

## Popis

Hranice frekvenčního odstupu mimo pásmo (Frequency Offset Out-of-Band boundary, FOOB) je technický parametr definovaný ve specifikacích 3GPP pro New Radio (NR), zejména ve specifikacích pro testy shody jako TS 38.521-1. Nejde o fyzickou součást, ale o koncepční hodnotu frekvenčního odstupu, která vymezuje dvě odlišné oblasti pro rádiové (RF) emise z vysílače uživatelského zařízení (UE): oblast emisí mimo pásmo (Out-of-Band, OOB) a oblast nežádoucích emisí (Spurious). Tato hranice je definována vzhledem k okraji šířky kanálu přiděleného pro přenos UE.

Provozně platí, že emise měřené na frekvencích v oblasti OOB (blíže k vysílanému nosnému signálu) podléhají limitům pro emise mimo pásmo. Tyto emise jsou primárně způsobeny modulací, nelinearitou výkonového zesilovače a šumem a jejich limity jsou navrženy tak, aby chránily sousední kanály ve stejném nebo jiném provozním pásmu. Měřicí šířka pásma pro emise OOB je typicky zarovnána s šířkou pásma zdrojového bloku. Za hranicí frekvenčního odstupu FOOB spadají emise do oblasti nežádoucích emisí (Spurious). Nežádoucí emise jsou nežádoucí emise na diskrétních frekvencích, často harmonické nebo intermodulační produkty, které mohou způsobovat rušení systémům pracujícím v úplně jiných kmitočtových pásmech. Limity pro nežádoucí emise jsou obecně přísnější a měří se s pevnou referenční šířkou pásma.

Přesná hodnota FOOB není jediné číslo, ale je definována vzorcem založeným na šířce kanálu NR a rozestupu podnosných. Například se často vypočítá jako šířka kanálu dělená dvěma plus specifický odstup. Tento výpočet zajišťuje, že se hranice přiměřeně škáluje s různými konfiguracemi NR. Během testů RF shody UE měří standardizované testovací sestavy emise vysílače v širokém spektru. FOOB je klíčovým bodem, který určuje, která sada limitních tabulek (OOB nebo Spurious) ze základní specifikace TS 38.101-1 se musí použít na naměřenou úroveň výkonu při daném frekvenčním odstupu, čímž se zajišťuje, že zařízení splňuje regulatorní požadavky a požadavky na koexistenci.

## K čemu slouží

FOOB byl definován, aby vytvořil jasnou a standardizovanou technickou demarkaci pro řízení emisí v zařízeních 5G NR. Jak se rádiové systémy stávaly složitějšími s velkými šířkami pásma a agregací nosných, spektrum nežádoucích emisí z vysílače je rozsáhlé. Regulátoři a normalizační orgány potřebovali konzistentní pravidlo pro kategorizaci těchto emisí pro účely testování a shody. Problémem bylo rozlišit emise, které ovlivňují blízké kanály (OOB), od těch, které by mohly ovlivnit vzdálené, nesouvisející služby (Spurious).

Historicky různé normy nebo regiony mohly používat odlišné definice, což komplikovalo globální certifikaci zařízení. Zavedení FOOB ve 3GPP Release 17 poskytlo jednotnou, na vzorci založenou definici vnitřně spojenou s parametry technologie NR. Tím se vyřešila nejednoznačnost v aplikaci správných testovacích limitů, zejména pro nové širokopásmové nosné NR, kde tradiční pevné frekvenční odstupy ze starších technologií jako LTE byly nedostatečné.

K jeho vytvoření vedla potřeba přesných a škálovatelných testovacích požadavků pro ekosystém 5G NR. Řeší omezení univerzální hranice tím, že váže FOOB přímo na šířku kanálu, což zajišťuje, že přechodový bod mezi oblastmi emisí je vždy logicky vztažen k vlastní obsazené šířce pásma signálu. To umožňuje efektivní správu spektra, chrání širokou škálu dalších rádiových služeb před rušením a poskytuje výrobcům jasné cíle pro návrh vysílače a implementaci filtrů.

## Klíčové vlastnosti

- Vymezuje přechod z oblasti emisí mimo pásmo (Out-of-Band, OOB) do oblasti nežádoucích emisí (Spurious) pro vysílače NR UE.
- Definován vzorcem založeným na šířce kanálu NR a rozestupu podnosných, což zajišťuje škálovatelnost.
- Klíčový pro určení příslušných limitů testů RF shody ve specifikacích TS 38.101 a TS 38.521.
- Zajišťuje konzistentní globální metodiku testování nežádoucích emisí.
- Chrání služby jak v sousedních kanálech, tak ve vzdálených kmitočtových pásmech před rušením.
- Poskytuje jasný cíl pro návrh filtrů vysílače a požadavky na linearitu.

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.124** (Rel-19) — NR UE EMC Requirements
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.741** (Rel-19) — NTN L-/S-band for NR Technical Specification
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec

---

📖 **Anglický originál a plná specifikace:** [FOOB na 3GPP Explorer](https://3gpp-explorer.com/glossary/foob/)
