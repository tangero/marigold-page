---
slug: "manova"
url: "/mobilnisite/slovnik/manova/"
type: "slovnik"
title: "MANOVA – Multivariate Analysis of Variance"
date: 2025-01-01
abbr: "MANOVA"
fullName: "Multivariate Analysis of Variance"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/manova/"
summary: "Statistická metoda používaná při testování výkonu v rámci 3GPP k simultánní analýze více závislých proměnných napříč různými skupinami nebo podmínkami. Pomáhá vyhodnocovat vliv parametrů sítě na různé"
---

MANOVA je statistická metoda používaná při testování výkonu v rámci 3GPP k simultánní analýze více závislých proměnných za účelem vyhodnocení vlivu parametrů sítě na různé metriky kvality.

## Popis

Multivariate Analysis of Variance (MANOVA) je pokročilá statistická technika používaná v rámci standardizace 3GPP, zejména ve specifikacích pro charakterizaci a testování výkonu (např. TS 26.935). Rozšiřuje jednorozměrnou analýzu rozptylu ([ANOVA](/mobilnisite/slovnik/anova/)) tím, že umožňuje simultánní analýzu dvou nebo více korelovaných závislých proměnných. V kontextu 3GPP jsou těmito závislými proměnnými typicky vícečetné klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)) nebo metriky kvality uživatelského prožitku ([QoE](/mobilnisite/slovnik/qoe/)) – jako například skóre kvality videa, skóre kvality zvuku, čas počátečního bufferingu a poměr zamrznutí – které jsou měřeny během testů výkonu sítě nebo služby. Nezávislé proměnné jsou testované faktory nebo podmínky, jako různé typy kodeků, profily šířky pásma sítě, míry ztrát paketů nebo kategorie zařízení.

Metodologie funguje na principu vytvoření matematického modelu, který vyhodnocuje, zda rozdíly v průměrech mezi skupinami na kombinaci závislých proměnných pravděpodobně vznikly náhodou. Vypočítává testovací statistiky jako Wilksovo lambda, Pillaiho stopu, Hotellingovu stopu a Royův největší kořen. Každá z těchto statistik vyhodnocuje celkový vliv nezávislých faktorů na multivariační soubor závislých proměnných. Pokud MANOVA indikuje statisticky významný efekt (typicky s p-hodnotou < 0,05), následují dodatečné post-hoc analýzy, jako je diskriminační analýza nebo jednorozměrné ANOVA pro každou závislou proměnnou, aby bylo přesně určeno, které metriky se mezi skupinami liší. Tento přístup kontroluje celkovou chybu I. typu (falešně pozitivní výsledky), která by narostla, pokud by bylo provedeno více samostatných ANOVA testů.

V praxi pracovní skupiny 3GPP používají MANOVA k důkladné analýze výsledků rozsáhlých subjektivních nebo objektivních testovacích kampaní. Například při hodnocení nového videokodeku, jako je Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)), nebo adaptačního algoritmu pro streamování, testeři shromažďují vícerozměrná data o výkonu za různých podmínek degradace sítě. MANOVA pomáhá určit, zda nová technologie produkuje statisticky významné zlepšení v celkovém profilu uživatelského prožitku ve srovnání s výchozím stavem, když jsou brány v úvahu všechny dimenze kvality společně. To je klíčové pro přijímání standardizovaných, na důkazech založených rozhodnutí o adopci nových funkcí. Proces zahrnuje pečlivý experimentální design, sběr dat, kontrolu předpokladů (např. multivariační normalita, homogenita kovariančních matic) a interpretaci pomocí statistického softwaru, což zajišťuje, že doporučení 3GPP jsou robustní a vědecky platná.

## K čemu slouží

MANOVA byla v rámci 3GPP přijata, aby řešila složitost hodnocení moderních multimediálních služeb, jejichž výkon nelze zachytit jedinou metrikou. Tradiční jednorozměrné testy analyzovaly každý [KPI](/mobilnisite/slovnik/kpi/) izolovaně, což mohlo přehlédnout interakce mezi metrikami a zvýšit riziko chybných závěrů kvůli vícenásobnému porovnávání. Například nový videokodek může mírně zlepšit ostrost, ale zhoršit zamrzávání; jednorozměrná analýza každé metriky nemusí tento celkový kompromis odhalit. MANOVA poskytuje holistický pohled a testuje kombinovaný efekt na všechny relevantní dimenze kvality současně.

Tato statistická přísnost se stala nezbytnou, jak se specifikace 3GPP rozvíjely a zahrnovaly bohaté mediální služby jako Voice over LTE (VoLTE), Video over LTE (ViLTE) a imerzivní [VR](/mobilnisite/slovnik/vr/)/[AR](/mobilnisite/slovnik/ar/). Standardizační proces vyžaduje objektivní, reprodukovatelné metody pro porovnání konkurenčních technologií a pro zajištění, že povinné funkce skutečně zlepšují uživatelský prožitek. MANOVA umožňuje odborníkům s jistotou posoudit, zda pozorované rozdíly v testovacích datech lze připsat studovanému faktoru (např. novému protokolu), a nikoli náhodné variaci. Podporuje princip standardizace řízené daty a zajišťuje, že vydání 3GPP začleňují technologie, které přinášejí statisticky ověřená zlepšení napříč multivariačním spektrem výkonu sítě a kvality.

## Klíčové vlastnosti

- Simultánní analýza více korelovaných závislých proměnných (KPI/QoE metrik)
- Používá testovací statistiky jako Wilksovo lambda a Pillaiho stopu k vyhodnocení celkových efektů
- Kontroluje celkovou chybu I. typu (family-wise error rate) ve srovnání s více jednorozměrnými testy
- Podporuje složité experimentální návrhy s více nezávislými faktory
- Umožňuje následnou post-hoc diskriminační analýzu pro interpretaci rozdílů mezi skupinami
- Aplikována při testování výkonu v 3GPP pro hodnocení kodeků a benchmarkování služeb

## Související pojmy

- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)
- [ANOVA – Analysis of Variance](/mobilnisite/slovnik/anova/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia

---

📖 **Anglický originál a plná specifikace:** [MANOVA na 3GPP Explorer](https://3gpp-explorer.com/glossary/manova/)
