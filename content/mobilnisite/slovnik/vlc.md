---
slug: "vlc"
url: "/mobilnisite/slovnik/vlc/"
type: "slovnik"
title: "VLC – Variable Length Code"
date: 2025-01-01
abbr: "VLC"
fullName: "Variable Length Code"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vlc/"
summary: "Technika zdrojového kódování, při níž jsou symboly reprezentovány kódovými slovy s proměnnou bitovou délkou. Častěji se vyskytujícím symbolům jsou přiřazena kratší kódová slova, čímž se optimalizuje c"
---

VLC je technika zdrojového kódování, při níž jsou symboly reprezentovány kódovými slovy s proměnnou bitovou délkou, přičemž častěji se vyskytujícím symbolům jsou přiřazena kratší kódová slova za účelem optimalizace datového toku. Používá se v řečových a audio kodecích 3GPP pro efektivní entropické kódování.

## Popis

Variable Length Coding (VLC) je základní bezeztrátový kompresní algoritmus založený na principech teorie informace, konkrétně na Huffmanově kódování. Základní myšlenkou je přiřazení kratších binárních kódových slov zdrojovým symbolům (např. indexům parametrů, transformačním koeficientům), které mají vyšší pravděpodobnost výskytu, a delších kódových slov méně pravděpodobným symbolům. Tím se sníží průměrný počet bitů na symbol, čímž je dosaženo komprese bez ztráty informace. Kodek (codebook), který mapuje symboly na bitové sekvence proměnné délky, musí být znám jak kodéru, tak dekodéru. Dekodér jednoznačně parsuje příchozí bitový proud, protože žádné kódové slovo není prefixem jiného (vlastnost bezprefixovosti), což umožňuje jednoznačný dekódovací proces.

V rámci specifikací 3GPP se VLC primárně používá ve fázi zdrojového kódování řečových a audio kodeků definovaných v řadě 3GPP TS 26, jako je kodek Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a kodek Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)). Tyto kodeky fungují tak, že analyzují vstupní řečový signál za účelem extrakce parametrů, jako jsou Line Spectral Frequencies ([LSF](/mobilnisite/slovnik/lsf/)), pitch lag a indexy algebraického kodeku. Statistické rozdělení těchto parametrů není rovnoměrné; některé hodnoty se vyskytují mnohem častěji než jiné. VLC se používá k efektivnímu zakódování těchto parametrů pro přenos. Například po kvantizaci je index reprezentující LSF vektor vložen do VLC modulu, který na výstupu poskytne kompaktní bitovou sekvenci proměnné délky. Tento bitový proud je následně multiplexován s dalšími zakódovanými parametry do jednoho rámce pro přenos přes rozhraní rádiového přístupu.

Implementace zahrnuje návrh optimalizovaných kodeků přizpůsobených pravděpodobnostnímu rozdělení parametrů pro různé provozní režimy (např. různé datové toky, podmínky s pozadím šumu). V pokročilých kodecích, jako je EVS, může být dynamicky přepínáno mezi více VLC tabulkami na základě charakteristik signálu za účelem maximalizace účinnosti kódování. Dekódovací proces v přijímači zahrnuje bit po bitu parsování přijatého rámce za použití stejné VLC tabulky k rekonstrukci indexů parametrů, které jsou následně použity pro syntézu řečového signálu. Toto efektivní entropické kódování je klíčovým důvodem, proč moderní kodeky mohou poskytovat vysoce kvalitní řeč při velmi nízkých datových tocích, což přímo ovlivňuje spektrální účinnost a uživatelskou kapacitu v mobilních sítích.

## K čemu slouží

VLC byla vyvinuta pro řešení potřeby efektivní digitální reprezentace informací s minimalizací počtu bitů potřebných pro uložení nebo přenos. Před těmito technikami entropického kódování se používalo kódování s pevnou délkou, které plýtvalo bity na reprezentaci málo pravděpodobných událostí stejně dlouhými kódy jako události vysoce pravděpodobné. Teorie informace Clauda Shannona stanovila, že optimální délka kódu pro symbol by měla být úměrná zápornému logaritmu jeho pravděpodobnosti. Algoritmy VLC, jako je Huffmanovo kódování, poskytují praktickou metodu pro dosažení nebo přiblížení se tomuto teoretickému limitu, čímž řeší problém redundantního přidělování bitů v systémech digitální komunikace.

Začlenění VLC do řečových kodeků 3GPP bylo motivováno přísnými omezeními šířky pásma v raných buněčných systémech (2G/3G) a neustálou snahou o vyšší kapacitu. Hlas byl vždy primární službou a efektivní kódování přímo znamená více simultánních hovorů na buňku. Aplikací VLC na parametry řečových kodeků mohli konstruktéři významně snížit průměrný datový tok zakódovaného řečového rámce bez degradace percepční kvality. To umožnilo vývoj vícerychlostních kodeků, jako je [AMR](/mobilnisite/slovnik/amr/), které mohly efektivně fungovat za různých podmínek kanálu. Vývoj směrem k širokopásmovému a super-širokopásmovému audiu ([EVS](/mobilnisite/slovnik/evs/)) dále využíval pokročilé VLC techniky k zachování vysoké kvality při konkurenceschopných datových tocích, což zajišťuje efektivní využití prostředků jak přepojovaných okruhů, tak přepojovaných paketů (VoLTE, VoNR). VLC je tedy základní technologií, která umožňuje nákladově efektivní a vysoce kvalitní hlasové služby tvořící základ mobilní telekomunikace.

## Klíčové vlastnosti

- Bezeztrátová komprese založená na pravděpodobnosti symbolů (entropické kódování)
- Přiřazuje častějším symbolům kratší kódová slova za účelem snížení datového toku
- Používá bezprefixové kódy (např. Huffmanovy kódy) pro jednoznačné dekódování
- Integrální součást řečových/audio kodeků 3GPP (AMR, EVS) pro kódování parametrů
- Dynamicky volitelné kodeky se přizpůsobují různým řečovým statistikám
- Přímo zlepšuje spektrální účinnost hlasových služeb v mobilních sítích

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks

---

📖 **Anglický originál a plná specifikace:** [VLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/vlc/)
