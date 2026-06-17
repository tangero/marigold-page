---
slug: "atvn"
url: "/mobilnisite/slovnik/atvn/"
type: "slovnik"
title: "ATVN – AMR-TFO Version Number"
date: 2025-01-01
abbr: "ATVN"
fullName: "AMR-TFO Version Number"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/atvn/"
summary: "ATVN je parametr identifikující verzi protokolu AMR Tandem Free Operation (TFO) používaného mezi transkodéry v mobilní síti. Zajišťuje kompatibilitu mezi různými síťovými prvky během hlasových hovorů,"
---

ATVN je parametr identifikující verzi protokolu AMR Tandem Free Operation používaného mezi transkodéry za účelem zajištění kompatibility a správného vyjednávání schopností během hlasových hovorů.

## Popis

Číslo verze AMR-TFO (ATVN) je klíčový parametr ve specifikacích 3GPP, který slouží jako identifikátor verze protokolu Adaptive Multi-Rate Tandem Free Operation. TFO je mechanismus umožňující hlasovým kodekům pracovat v režimu bez tandemového řazení mezi transkodéry v mobilní síti, což znamená, že pokud oba konce hovoru podporují stejný režim kodeku, může být zakódovaná řeč přenášena sítí bez dalšího překódování. Parametr ATVN je vyměňován během sestavování hovoru mezi jednotkami transkodéru za účelem vyjednání a navázání kompatibilního provozu TFO.

Z architektonického hlediska ATVN funguje v jednotkách transkodéru umístěných v Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) v jádru sítě. Při sestavení hovoru mezi mobilními účastníky si transkodéry na obou koncích vymění informace o schopnostech TFO včetně hodnoty ATVN. Tato výměna typicky probíhá prostřednictvím signálování v pásmu (in-band) uvnitř samotného hlasového kanálu, za použití specifických bitových vzorů, které nenarušují přenášenou řeč. ATVN udává, kterou verzi protokolu TFO transkodér podporuje, včetně konkrétních funkcí, struktury rámců a signalizačních procedur.

Technická implementace ATVN zahrnuje specifické bitové vzory definované v 3GPP TS 28.062. Různé hodnoty ATVN odpovídají různým verzím protokolu TFO s odlišnými schopnostmi. Například ATVN=0 může označovat základní provoz TFO, zatímco vyšší hodnoty mohou označovat vylepšené verze s dodatečnými funkcemi, jako je lepší obnova při chybách, podpora širšího rozsahu režimů kodeku nebo lepší kompatibilita s různými konfiguracemi sítě. Během vyjednávání TFO transkodéry porovnají své hodnoty ATVN a vyberou nejvyšší společnou verzi, kterou oba podporují, čímž je zajištěna zpětná kompatibilita při maximalizaci využití funkcí.

Role ATVN v síti je klíčová pro zachování kvality hlasu a optimalizaci síťových zdrojů. Tím, že umožňuje správné vyjednávání TFO, ATVN pomáhá zabránit zbytečným operacím transkódování, které mohou degradovat kvalitu hlasu prostřednictvím více cyklů kódování/dekódování. Když je TFO úspěšně navázáno za použití kompatibilních hodnot ATVN, řeč zůstává v komprimovaném formátu po celé síťové cestě, čímž je zachována původní kvalita a sníženo zatížení síťových prvků. To je obzvláště důležité pro udržení konzistentní kvality hlasu v heterogenních sítích, kde různé síťové prvky mohou podporovat různé verze protokolu TFO.

Parametr také hraje roli ve vývoji sítě a interoperabilitě. Jak se protokoly TFO vyvíjejí s novými vydáními, ATVN poskytuje mechanismus pro plynulou migraci. Novější síťové prvky s vyššími hodnotami ATVN mohou stále spolupracovat se staršími prvky díky návratu k nižším společným hodnotám ATVN. To zajišťuje, že síťové aktualizace mohou probíhat postupně, aniž by došlo k narušení stávajících služeb. Proces vyjednávání ATVN je typicky transparentní pro koncové uživatele, ale tvoří základní část mechanismů optimalizace kvality hlasu v sítích 3GPP.

## K čemu slouží

ATVN byl vytvořen, aby řešil základní problém degradace kvality hlasu v mobilních sítích způsobený vícenásobnými operacemi transkódování. V raných mobilních sítích, když hovor procházel mezi dvěma mobilními účastníky, byla řeč typicky dekódována na PCM na každém transkodéru a poté znovu zakódována, což způsobovalo ztrátu kvality tímto tandemovým řazením. TFO byl vyvinut, aby toto zbytečné překódování odstranil v případě, že oba konce podporovaly kompatibilní kodeky, ale bez mechanismu verzování nemohly různé síťové implementace správně vyjednat schopnosti TFO.

Historický kontext vývoje ATVN vychází z vývoje hlasových kodeků v sítích 2G a 3G. Jak se kodeky [AMR](/mobilnisite/slovnik/amr/) staly standardem a sítě se rozšiřovaly, operátoři nasazovali zařízení od více dodavatelů s různými implementacemi TFO. Bez standardizované identifikace verze nemohly transkodéry spolehlivě navazovat relace TFO, což vedlo k nekonzistentní kvalitě hlasu a promarněným příležitostem pro optimalizaci kvality. ATVN poskytl chybějící prvek, který umožnil předvídatelné vyjednávání TFO napříč více-dodavatelskými sítěmi.

Předchozí přístupy k implementaci TFO trpěly problémy s interoperabilitou, protože každý dodavatel implementoval proprietární signalizační metody. To ztěžovalo sítím používajícím zařízení od různých výrobců spolehlivě navazovat relace TFO. ATVN standardizoval proces identifikace verze, což umožnilo transkodérům zjistit společné schopnosti a navázat nejvyšší možnou úroveň provozu TFO. Tím byl vyřešen kritický problém interoperability a zároveň byl vytvořen rámec pro budoucí vylepšení TFO prostřednictvím přírůstků verzí.

## Klíčové vlastnosti

- Identifikace verze pro kompatibilitu protokolu TFO
- Vyjednávání prostřednictvím signálování v pásmu (in-band) uvnitř hlasového kanálu
- Zpětná kompatibilita prostřednictvím návratu k nižší verzi
- Podpora interoperability mezi více dodavateli
- Umožňuje optimalizaci kvality vyhýbáním se zbytečnému transkódování
- Rámec pro vývoj protokolu prostřednictvím přírůstků verzí

## Definující specifikace

- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [ATVN na 3GPP Explorer](https://3gpp-explorer.com/glossary/atvn/)
