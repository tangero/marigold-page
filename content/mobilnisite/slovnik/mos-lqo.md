---
slug: "mos-lqo"
url: "/mobilnisite/slovnik/mos-lqo/"
type: "slovnik"
title: "MOS-LQO – Mean Opinion Score – Listening Quality Objective"
date: 2026-01-01
abbr: "MOS-LQO"
fullName: "Mean Opinion Score – Listening Quality Objective"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mos-lqo/"
summary: "Objektivní, instrumentální predikce subjektivního Mean Opinion Score (MOS) pro kvalitu pouze poslechu řeči. MOS-LQO je číselné skóre, které poskytují standardizované algoritmy (jako PESQ nebo POLQA) a"
---

MOS-LQO je objektivní, instrumentální predikce subjektivního skóre kvality pouze poslechu řeči. Výstup standardizovaných algoritmů, jako je PESQ nebo POLQA, slouží k odhadu lidského vnímání bez potřeby živého panelu posluchačů.

## Popis

Mean Opinion Score – Listening Quality Objective (MOS-LQO) je vypočítaná metrika představující odhadované subjektivní skóre kvality poslechu. Na rozdíl od klasického [MOS](/mobilnisite/slovnik/mos/) získaného z lidských panelů je MOS-LQO generován výhradně softwarovými algoritmy definovanými v normách [ITU-T](/mobilnisite/slovnik/itu-t/), jako jsou P.862 (PESQ) a P.863 (POLQA). Tyto algoritmy jsou modely s úplnou referencí (full-reference), což znamená, že porovnávají degradovaný řečový signál (jak byl přijat po průchodu sítí a kodeky) s původním, neporušeným referenčním signálem. Analýzou specifických percepčních rozdílů mezi oběma signály – jako jsou zkreslení, šum, zpoždění a artefakty kodeků – algoritmus vypočítá skóre, které vysoce koreluje s průměrným subjektivním hodnocením lidí (MOS). Výstupem je číslo, typicky na škále podobné MOS (např. 1,0 až 4,5 nebo 1,0 až 5,0 v závislosti na algoritmu).

Architektura měřicího systému MOS-LQO zahrnuje testovací uspořádání, ve kterém je známý referenční řečový soubor vložen do testovaného systému (např. cesta hovoru přes IMS síť). Výstupní signál je zachycen a časově synchronizován s referencí. Objektivní model (např. POLQA) poté provede sofistikovanou percepční analýzu. Modeluje lidský sluchový systém a aplikuje koncepty jako vnímání hlasitosti, maskovací efekty a kognitivní modelování k identifikaci vad, které by si posluchač všiml. Model agreguje tyto percepční poruchy do jediného číselného skóre – MOS-LQO. Tento proces je plně automatizovaný, opakovatelný a lze jej provádět v reálném čase nebo na nahraných souborech, což jej činí výrazně škálovatelnějším než subjektivní testování.

V rámci 3GPP je MOS-LQO specifikováno jako primární metoda pro testování shody a benchmarkování výkonu řečových kodeků, systémů Voice over IP (VoIP) a celých síťových cest. Specifikace definují testovací podmínky (např. úrovně šumu na pozadí, profily ztrát paketů) a minimální požadované hodnoty MOS-LQO, kterých musí kodek nebo zařízení dosáhnout. Například 3GPP TS 26.179 definuje požadavky na výkon kodeku Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) pomocí cílů MOS-LQO za různých chybových podmínek. Operátoři sítí také používají měření MOS-LQO z drive testů nebo pasivních sond ke sledování hlasové kvality koncového uživatele v celé své síti, což jim umožňuje proaktivně identifikovat degradaci kvality a optimalizovat síťové parametry.

## K čemu slouží

MOS-LQO bylo vyvinuto za účelem překonání hlavních praktických omezení subjektivního testování [MOS](/mobilnisite/slovnik/mos/): je extrémně časově náročné, drahé a nevhodné pro monitoring živé sítě nebo rychlé vývojové cykly produktů. Zatímco subjektivní MOS poskytuje definitivní kvalitativní benchmark, nelze jej použít pro nepřetržité zajišťování kvality v provozních sítích nebo pro testování všech možných síťových podmínek. Účelem MOS-LQO je poskytnout praktický, automatizovaný a přesný proxy ukazatel pro subjektivní kvalitu poslechu.

Jeho vytvoření bylo motivováno potřebou standardizovaného, instrumentálního hodnocení kvality, které by mohlo být integrováno do testovacích zařízení, síťových sond a certifikačních laboratoří zařízení. Tím, že poskytuje objektivní predikci silně korelující s lidským vnímáním, umožňuje MOS-LQO inženýrům provádět srovnání a hodnocení kvality ve velkém měřítku a v reálném čase. Řeší tak kritický požadavek průmyslu na kvantifikaci Quality of Experience (QoE) způsobem, který je vědecky platný a provozně proveditelný, a tvoří základ pro moderní správu kvality hlasových služeb a benchmarkování v sítích 2G, 3G, 4G, 5G a [OTT](/mobilnisite/slovnik/ott/) komunikačních službách.

## Klíčové vlastnosti

- Objektivní predikce subjektivní kvality poslechu (MOS) pomocí algoritmických modelů
- Založeno na porovnání s úplnou referencí (full-reference) mezi původním a degradovaným řečovým signálem
- Implementuje percepční modely lidského sluchového systému (např. v POLQA)
- Umožňuje automatizované, opakovatelné a škálovatelné testování kvality řeči
- Používá se pro testování shody kodeků, certifikaci zařízení a monitoring kvality sítě v 3GPP
- Výstupem je číselné skóre vysoce korelující s výsledky z subjektivních panelů posluchačů

## Související pojmy

- [MOS – Mean Opinion Score](/mobilnisite/slovnik/mos/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 22.179** (Rel-20) — MCPTT Service Requirements
- **TR 26.954** (Rel-19) — UE Headset Electrical Interface Testing

---

📖 **Anglický originál a plná specifikace:** [MOS-LQO na 3GPP Explorer](https://3gpp-explorer.com/glossary/mos-lqo/)
