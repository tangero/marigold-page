---
slug: "maiohsn"
url: "/mobilnisite/slovnik/maiohsn/"
type: "slovnik"
title: "MAIOHSN – MAIO Hopping Sequence Number"
date: 2025-01-01
abbr: "MAIOHSN"
fullName: "MAIO Hopping Sequence Number"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/maiohsn/"
summary: "MAIO Hopping Sequence Number je parametr v GSM/GPRS/EDGE, který v kombinaci s MAIO definuje konkrétní vzor přeskakování frekvencí pro mobilní stanici. Určuje pořadí navštěvovaných frekvencí, což umožň"
---

MAIOHSN je parametr, který v kombinaci s MAIO definuje konkrétní pořadí sekvence přeskakování frekvencí pro mobilní stanici v systémech GSM za účelem potlačení interference.

## Popis

[MAIO](/mobilnisite/slovnik/maio/) Hopping Sequence Number (MAIOHSN) je termín, který souhrnně označuje kombinaci dvou klíčových parametrů přeskakování frekvencí v GSM/[GPRS](/mobilnisite/slovnik/gprs/)/[EDGE](/mobilnisite/slovnik/edge/): Mobile Allocation Index Offset (MAIO) a Hopping Sequence Number ([HSN](/mobilnisite/slovnik/hsn/)). Ačkoli nejde o samostatný parametr ve specifikacích, konceptuálně představuje párování, které jednoznačně definuje vzor přeskakování frekvencí mobilní stanice na provozním kanálu. HSN je celé číslo od 0 do 63, které vybírá algoritmus pro pořadí navštěvování frekvencí ze seznamu Mobile Allocation ([MA](/mobilnisite/slovnik/ma/)). HSN=0 vede k cyklickému (sekvenčnímu) přeskakování, zatímco HSN=1 až 63 generuje různé pseudonáhodné sekvence. MAIO, jak bylo popsáno dříve, je offset (0 až N-1), který posouvá počáteční bod v rámci této sekvence.

Z architektonického hlediska síť, konkrétně Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)), přiřazuje mobilní stanici jak HSN, tak MAIO při zřizování kanálu využívajícího přeskakování frekvencí. Tyto parametry jsou mobilní stanici sděleny prostřednictvím zpráv vrstvy 3, jako je Assignment Command nebo Packet Channel Description. BSC zajišťuje, aby pro danou buňku a časový slot kombinace HSN a MAIO napříč všemi aktivními uživateli vedla k nepřekrývajícím se vzorům a zabránila tak kolizím. [BTS](/mobilnisite/slovnik/bts/) i mobilní stanice používají stejný HSN, MAIO a seznam MA k synchronnímu přeskakování frekvencí po snímcích, čímž udržují rádiové spojení.

Princip fungování je zásadní pro správu interference. HSN určuje permutaci seznamu MA. Pro cyklické přeskakování (HSN=0) je vzor prostě sekvenční postup seznamem, posunutý o hodnotu MAIO. Pro pseudonáhodné přeskakování (HSN=1-63) je vzor generován předdefinovaným algoritmem používajícím HSN jako semeno, což vytváří zdánlivě náhodné pořadí, které se po cyklu opakuje. MAIO pak vybírá, kterou položku v této permutované sekvenci použít jako první frekvenci. Například pro seznam MA obsahující frekvence F1, F2, F3, F4 může HSN=5 generovat sekvenci jako F3, F1, F4, F2,... Pokud je MAIO=1, mobilní stanice začne na F1, poté přejde na F4, F2, F3,... Tento dvouparametrový systém umožňuje síti vytvořit z omezeného počtu frekvencí velkou sadu ortogonálních vzorů.

Úloha konceptu MAIOHSN spočívá v poskytnutí flexibilního a účinného nástroje pro optimalizaci rádiových zdrojů. Pečlivým plánováním přidělování HSN a MAIO v síti mohou operátoři řídit charakter interference. Různé buňky mohou používat různé HSN pro randomizaci mezibuněčné interference, zatímco v rámci jedné buňky uživatele oddělují unikátní MAIO. Tato koordinace je klíčová pro dosažení plných výhod přeskakování frekvencí: frekvenční diverzity pro potlačení vícecestného útlumu, diverzity interference pro vyrovnání ko-kanálové interference a v konečném důsledku zlepšené kvality hovoru a vyšší kapacity sítě. Představuje základní inteligenci adaptivní fyzické vrstvy GSM.

## K čemu slouží

Koncept [MAIO](/mobilnisite/slovnik/maio/) Hopping Sequence Number existuje, aby řešil dvojí problém frekvenčně selektivního útlumu a systematické ko-kanálové interference v buňkových systémech založených na TDMA, jako je GSM. Před jeho zavedením sítě spoléhaly na pevné přiřazení frekvencí nebo jednoduché cyklické přeskakování, které poskytovalo omezenou ochranu proti hlubokým útlumům a mohlo vytvářet předvídatelné vzorce interference mezi buňkami používajícími stejný frekvenční plán. Tato předvídatelnost znamenala, že některé mobilní stanice by trvale zažívaly špatnou kvalitu, což vedlo k přerušeným hovorům a nespokojenosti uživatelů. Zavedení pseudonáhodného přeskakování řízeného HSN a MAIO bylo motivováno potřebou změnit charakter interference ze stálého, škodlivého signálu na šumům podobné, zprůměrované rušení, které může být efektivně korigováno kanálovým kódováním.

MAIOHSN tyto problémy řeší tím, že umožňuje pseudonáhodné přeskakování frekvencí. HSN poskytuje náhodnost, což zajišťuje, že sekvence navštěvovaných frekvencí má nízkou korelaci se sekvencemi v sousedních buňkách nebo na jiných časových slotech. MAIO zajišťuje, že v rámci stejné buňky a časového slotu jsou uživatelé na každém přeskoku odděleni ve frekvenční oblasti. Tato kombinace výrazně zlepšuje statistiku poměru signálu k interferenci (C/I), čímž činí spojení robustnějším. Řeší problém 'špatných míst', kde by mohla být mobilní stanice uvízlá na frekvenci prožívající hluboký útlum nebo silnou interferenci; s přeskakováním se podmínky mění každý snímek, což umožňuje kódu pro opravu chyb obnovit data.

Historicky standardizace parametrů HSN a MAIO ve fázi 2 GSM a jejich zdokonalení v pozdějších vydáních (včetně dokumentace Rel-8 v TS 45.914) představovala významný pokrok v buňkovém inženýrství. Přesunula sítě od statického, plánování náročného řízení frekvencí k dynamické, algoritmem řízené kontrole interference. To bylo obzvláště důležité s rostoucí hustotou sítí v důsledku nárůstu počtu účastníků. Rámec MAIOHSN umožnil operátorům nasadit více buněk na plochu (těsnější opakované využití) bez úměrného nárůstu interference, což přímo zvýšilo kapacitu a umožnilo masový úspěch GSM. Položil základy pro pozdější techniky potlačení interference v 3G a 4G, jako jsou scrambling kódy a frekvenčně selektivní plánování.

## Klíčové vlastnosti

- Kombinuje MAIO (offset) a HSN (algoritmus sekvence) k definici unikátního vzoru přeskakování
- Hodnoty HSN 1-63 generují pseudonáhodné sekvence pro randomizaci interference
- Hodnota HSN 0 umožňuje jednoduché cyklické (sekvenční) přeskakování
- Parametry jsou přiřazeny BSC a signalizovány mobilní stanici
- Umožňuje ortogonální přeskakování uvnitř buňky a randomizované přeskakování mezi buňkami
- Zásadní pro dosažení zisků z frekvenční diverzity a diverzity interference

## Související pojmy

- [MAIO – Mobile Allocation Index Offset](/mobilnisite/slovnik/maio/)

## Definující specifikace

- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [MAIOHSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/maiohsn/)
