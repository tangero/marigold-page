---
slug: "lsf"
url: "/mobilnisite/slovnik/lsf/"
type: "slovnik"
title: "LSF – Line Spectral Frequency"
date: 2025-01-01
abbr: "LSF"
fullName: "Line Spectral Frequency"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lsf/"
summary: "Matematická reprezentace koeficientů lineárně prediktivního kódovacího (LPC) filtru používaná pro efektivní kvantování a přenos parametrů řeči v hlasových kodecích. Je klíčová pro robustní kódování ře"
---

LSF je matematická reprezentace koeficientů lineárně prediktivního kódovacího filtru používaná pro efektivní kvantování a přenos parametrů řeči v hlasových kodecích, která zajišťuje robustní a kvalitní přenos hlasu v mobilních sítích.

## Popis

Line Spectral Frequency (LSF) je parametrizovaná technika pro reprezentaci koeficientů lineárně prediktivního kódovacího ([LPC](/mobilnisite/slovnik/lpc/)) filtru, který modeluje spektrální obálku řečového signálu. V algoritmech kódování řeči, jako je například kodek Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)), produkuje LPC analýzu sadu predikčních koeficientů (a-koeficientů), které popisují krátkodobý spektrální tvar. Tyto koeficienty jsou citlivé na chyby kvantování, což může vést k nestabilitě filtru. Reprezentace LSF transformuje tyto a-koeficienty na uspořádanou sadu frekvencí (LSF), které leží mezi 0 a Nyquistovou frekvencí (typicky 0 až 4000 Hz pro úzkopásmovou řeč). Tato transformace zajišťuje, že stabilita výsledného syntézního filtru se snadno udržuje – pokud jsou LSF seřazeny vzestupně, je stabilita filtru garantována. Tato vlastnost je klíčová pro spolehlivý přenos řeči přes rádiové kanály náchylné k chybám.

Generování LSF zahrnuje hledání kořenů dvou symetrických a antisymetrických polynomů odvozených z LPC polynomu. Tyto kořeny leží na jednotkové kružnici v z-rovině a jejich úhlové frekvence odpovídají LSF. Díky svému uspořádání a interpretaci ve frekvenční oblasti vykazují LSF dobré interpolační vlastnosti, což je nezbytné pro plynulý vývoj spektrální obálky mezi rámci při kódování s proměnnou přenosovou rychlostí. Dále mají LSF charakteristiku spektrální citlivosti, kde změna hodnoty LSF primárně ovlivňuje spektrální obálku v blízkosti dané frekvence, což umožňuje efektivní strategie skalárního nebo vektorového kvantování, které přidělují bity podle percepční důležitosti.

V systému 3GPP jsou LSF klíčovou součástí hlasových kodeků standardizovaných ve specifikacích řady 26 (např. 26.090 pro AMR kodek). Kvantované LSF jsou zabaleny do řečového rámce spolu s dalšími parametry, jako je základní tón a excitační signály. Příjemce dekóduje LSF, převede je zpět na LPC koeficienty a použije je v syntézním filtru pro rekonstrukci řečového signálu. Robustnost reprezentace LSF vůči chybám kvantování a přenosovým chybám přímo přispívá ke konzistentní kvalitě hlasu v službách 2G, 3G, 4G a 5G Voice over LTE (VoLTE) a Voice over NR (VoNR). Její efektivita umožňuje provoz při různých přenosových rychlostech definovaných módy kodeku a přizpůsobení se síťovým podmínkám bez kompromisů v srozumitelnosti.

## K čemu slouží

Primárním účelem reprezentace Line Spectral Frequency je umožnit efektivní, robustní a stabilní kvantování parametrů lineárně prediktivního kódování ([LPC](/mobilnisite/slovnik/lpc/)) pro digitální kompresi řeči v mobilních komunikacích. Rané hlasové kodeky přímo kvantovaly LPC koeficienty (např. ve formě reflektních koeficientů nebo přímé formy), ale tyto reprezentace byly vysoce citlivé na chyby kvantování, což často vedlo k nestabilním syntézním filtrům produkujícím slyšitelné artefakty nebo k úplnému selhání. Tato nestabilita byla hlavní překážkou pro dosažení kvalitního kódování řeči s nízkou přenosovou rychlostí, vyžadovaného pro bezdrátové spoje s omezenou šířkou pásma.

LSF byly vyvinuty za účelem překonání těchto omezení tím, že poskytují reprezentaci, kde lze stabilitu snadno kontrolovat a vynucovat (prostřednictvím jednoduchého uspořádání). Tato matematická vlastnost transformuje problém zajištění stabilního filtru na udržování monotónně rostoucí posloupnosti, což je přímočaré pro schémata kvantování a opravy chyb. Dále spektrální interpretace LSF umožňuje percepčně motivované kvantování – bity mohou být přiděleny více LSF ve frekvenčních oblastech kritických pro srozumitelnost řeči. To byl významný pokrok pro kodeky jako GSM Enhanced Full Rate ([EFR](/mobilnisite/slovnik/efr/)) a 3GPP [AMR](/mobilnisite/slovnik/amr/) kodek, které potřebovaly spolehlivě fungovat v celém spektru kanálových podmínek od čistých po velmi šumové.

Historicky bylo přijetí LSF ve standardech 3GPP (od Release 8 dále v referencovaných specifikacích, ale koncepčně dříve) hnací silou potřeby sjednocené, efektivní reprezentace parametrů řeči, která podporuje interoperabilitu, kódování s proměnnou rychlostí a plynulé předávání spojení mezi různými technologiemi radiového přístupu. Vyřešila základní problém přenosu kompaktního, na chyby odolného popisu filtru hlasového traktu, který je zásadní pro všechny kodeky řeči založené na lineární predikci tvořící páteř mobilních hlasových služeb.

## Klíčové vlastnosti

- Zajišťuje stabilitu LPC syntézního filtru, když jsou kvantované parametry seřazeny vzestupně.
- Prokazuje dobré interpolační vlastnosti pro plynulý vývoj spektra mezi řečovými rámci.
- Spektrální citlivost umožňuje percepčně efektivní přidělování bitů během kvantování.
- Umožňuje efektivní techniky skalárního a vektorového kvantování díky uspořádané struktuře.
- Klíčová sada parametrů v hlasových kodecích 3GPP jako AMR, AMR-WB a EVS.
- Umožňuje robustní kompresi a přenos řeči přes rádiové kanály náchylné k chybám.

## Definující specifikace

- **TS 26.090** (Rel-19) — AMR Speech Codec Detailed Mapping Specification
- **TS 26.092** (Rel-19) — AMR Comfort Noise for SCR Operation
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 46.060** (Rel-19) — GSM Enhanced Full Rate Speech Codec
- **TS 46.062** (Rel-19) — GSM EFR DTX Comfort Noise Specification

---

📖 **Anglický originál a plná specifikace:** [LSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lsf/)
