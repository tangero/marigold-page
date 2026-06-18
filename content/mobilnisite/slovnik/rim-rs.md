---
slug: "rim-rs"
url: "/mobilnisite/slovnik/rim-rs/"
type: "slovnik"
title: "RIM-RS – Remote Interference Management Reference Signal"
date: 2026-01-01
abbr: "RIM-RS"
fullName: "Remote Interference Management Reference Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rim-rs/"
summary: "Specifický referenční signál v downlinku definovaný v 5G NR pro účely správy vzdáleného rušení (RIM). Je vysílán základnovou stanicí, aby umožnil vzdálené základnové stanici-oběti detekovat, změřit a"
---

RIM-RS je referenční signál v downlinku v 5G NR, který základnová stanice vysílá, aby umožnila vzdálené základnové stanici-oběti detekovat, změřit a identifikovat zdroj vzdáleného rušení pro účely jeho potlačení.

## Popis

Referenční signál pro správu vzdáleného rušení (RIM-RS) je signál fyzické vrstvy definovaný ve standardu 5G New Radio (NR), specifikovaný v 3GPP TS 38.211. Je to dedikovaný referenční signál v downlinku, jehož jediným účelem je usnadnit detekci a měření vzdáleného rušení v sítích s duplexem s časovým dělením ([TDD](/mobilnisite/slovnik/tdd/)). Když gNB (základnová stanice 5G) vysílá své běžné downlinkové signály, vzdálená gNB-oběť, která přijímá nezamýšlené rušení, potřebuje způsob, jak toto rušení identifikovat a charakterizovat. RIM-RS tuto schopnost poskytuje. Je navržen se specifickými sekvencemi a je mapován na předem definované zdrojové elementy ve struktuře downlinkového rámce, což jej činí rozpoznatelným i v přítomnosti jiných signálů a šumu.

Operační procedura zahrnuje, že rušící gNB periodicky vysílá RIM-RS ve svém downlinku. Toto vysílání obvykle probíhá ve specifických symbolech, často uvnitř nebo přiléhajících k ochrannému intervalu nebo speciálním konfiguracím rámců. GNB-oběť, zatímco je nakonfigurována pro příjem ve svém uplinkovém slotu, místo toho skenuje přítomnost těchto známých sekvencí RIM-RS přicházejících ze vzdálených zdrojů. Po detekci gNB-oběť provádí přesná měření na přijatém RIM-RS. Klíčová měření zahrnují přijatý výkon signálu, který udává sílu rušení, a především čas příchodu. Porovnáním času příchodu detekovaného RIM-RS s vlastním vnitřním časováním rámce může gNB-oběť odhadnout zpoždění šíření rušivého signálu.

Toto změřené zpoždění je kritický parametr. Přímo udává, o kolik musí rušící gNB upravit své vysílací časování, aby se zabránilo překryvu jeho downlinku s uplinkem oběti. Výsledky měření, včetně identifikátoru zdroje potenciálně odvozeného ze sekvence RIM-RS, jsou zabaleny do [RIM](/mobilnisite/slovnik/rim/) reportu. Tento report je poté odeslán rušící gNB prostřednictvím aplikačního protokolu Xn (XnAP), jak je specifikováno v TS 38.473. Po přijetí reportu může rušící gNB zahájit opatření k potlačení rušení, jako je posunutí svého vysílacího okna. RIM-RS tedy funguje jako základní umožňující signál, který transformuje proces RIM z teoretického konceptu na praktický, měřitelný a akční systém, umožňující základnovým stanicím 'vidět' a kvantifikovat rušení zpoza horizontu.

## K čemu slouží

RIM-RS byl vytvořen, aby poskytl standardizovaný, optimalizovaný signál specificky pro případ použití správy vzdáleného rušení ([RIM](/mobilnisite/slovnik/rim/)) v 5G NR. Před jeho definicí mohly systémy zkoušet používat existující synchronizační nebo buňkově specifické referenční signály pro detekci rušení, ale ty nebyly ideální. Nebyly navrženy pro detekci slabých signálů na velkou vzdálenost v přijímacím pásmu jiné základnové stanice a postrádaly potřebné vlastnosti pro přesný odhad zpoždění a identifikaci zdroje v náročném scénáři vzdáleného rušení.

Konkrétní problém, který RIM-RS řeší, je potřeba spolehlivé detekce a přesného měření rušení s ultradlouhým zpožděním. Signál je navržen s dobrými vlastnostmi autokorelace a vzájemné korelace, aby bylo zajištěno, že může být detekován i při velmi nízkých poměrech signálu k rušení a šumu ([SINR](/mobilnisite/slovnik/sinr/)), což je typické pro vzdálený rušivý signál přicházející na uplinkový přijímač základnové stanice-oběti. Jeho strukturované umístění v časové doméně umožňuje přesné časové měření, které je nezbytné pro výpočet potřebného časového přizpůsobení pro potlačení.

Zavedený v 3GPP Release 16 jako součást rozšířeného RIM rámce pro NR, RIM-RS řešil omezení dřívějších, méně formalizovaných přístupů. Poskytl jednotný základ na fyzické vrstvě, který mohli implementovat všichni výrobci zařízení NR, čímž zajistil interoperabilitu a efektivní výkonnost funkce RIM napříč vícevýrobcovými 5G [TDD](/mobilnisite/slovnik/tdd/) sítěmi. Jeho vytvoření bylo motivováno očekávaným rozsáhlým nasazením 5G TDD, kde je správa vzdáleného rušení předpokladem stabilního provozu sítě, zejména s funkcemi jako koordinované plánování a synchronizace sítě, které jsou klíčové pro výkon 5G.

## Klíčové vlastnosti

- Dedikovaný referenční signál v downlinku definovaný v 3GPP TS 38.211 pro 5G NR
- Navržen pro detekci základnovými stanicemi, nikoli uživatelskými zařízeními (UE)
- Umožňuje měření výkonu rušivého signálu a přesného zpoždění šíření
- Používá specifické sekvence k umožnění identifikace rušícího zdrojového gNB
- Mapován na specifické zdrojové elementy pro usnadnění spolehlivé detekce v prostředí s vysokou hladinou šumu
- Základní umožňující prvek fyzické vrstvy pro proceduru měření a reportování RIM

## Související pojmy

- [RIM – Remote Interference Management](/mobilnisite/slovnik/rim/)
- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)

## Definující specifikace

- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [RIM-RS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rim-rs/)
