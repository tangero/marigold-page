---
slug: "ppw"
url: "/mobilnisite/slovnik/ppw/"
type: "slovnik"
title: "PPW – PRS Processing Window"
date: 2025-01-01
abbr: "PPW"
fullName: "PRS Processing Window"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ppw/"
summary: "PPW je definované časové okno, během kterého UE zpracovává přijaté zdroje polohovacího referenčního signálu (PRS) pro odhad polohy. Koordinuje časování měření a umožňuje efektivní, energeticky úsporné"
---

PPW je definované časové okno, během kterého UE zpracovává přijaté zdroje polohovacího referenčního signálu (PRS) za účelem koordinace časování měření pro efektivní a úsporný odhad polohy.

## Popis

[PRS](/mobilnisite/slovnik/prs/) Processing Window (PPW, okno zpracování PRS) je koncept zavedený ve specifikaci 3GPP Release 17 jako součást vylepšeného polohovacího rámce pro 5G New Radio (NR). Odkazuje na konfigurovatelné časové období, které síť specifikuje pro uživatelské zařízení (UE), a během kterého má UE provádět zpracování signálu a měření na sadě přijatých zdrojů polohovacího referenčního signálu (PRS). PRS jsou speciální signály vysílané základnovými stanicemi (gNB v NR, [eNB](/mobilnisite/slovnik/enb/) v LTE) navržené speciálně pro polohování, charakteristické nízkou interferencí a předvídatelnými vzory. PPW definuje časové hranice pro sběr a zpracování těchto signálů za účelem výpočtu metrik, jako je Reference Signal Time Difference ([RSTD](/mobilnisite/slovnik/rstd/)) pro polohování Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)).

Provozně síť konfiguruje polohovací relaci prostřednictvím zpráv Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) nebo Long-Term Evolution Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)). Tato konfigurace zahrnuje sadu zdrojů PRS (které buňky/signály měřit) a přidružené parametry pro PPW, jako je časový posun začátku a doba trvání. Po přijetí této konfigurace UE aktivuje své přijímací obvody během indikovaného PPW, aby zachytila symboly PRS ze specifikovaných sousedních buněk. Okno je synchronizováno s okamžiky vysílání zdrojů PRS. Uvnitř tohoto okna UE provádí na nezpracovaných vzorcích PRS korelační, filtrační a měřicí algoritmy. Klíčové je, že UE může mimo tato naplánovaná okna vypnout napájení nebo přerozdělit své výpočetní zdroje, což vede k významné úspoře energie ve srovnání s nepřetržitým sledováním.

Z architektonického hlediska je PPW spravováno polohovacím protokolovým zásobníkem UE (LPP v uživatelské rovině, RRC v řídicí rovině) a jejími jednotkami pro zpracování fyzické vrstvy. Mezi klíčové komponenty patří plánovací funkce, která synchronizuje zpracování v UE s vysílacími příležitostmi PRS v síti, a měřicí engine, který počítá metriky založené na čase nebo úhlu. Jeho role je zásadní pro síťové a asistované UE-bázi polohovací metody v 5G NR. Umožňuje vysoce přesné polohování tím, že zajišťuje provádění měření na synchronizovaných, kvalitních signálech, a je zásadní pro dosažení nízké latence a vysoké spolehlivosti požadované pro nové případy užití, jako je průmyslový IoT a komunikace vozidlo-se-vším ([V2X](/mobilnisite/slovnik/v2x/)), kde je přesná poloha kritická.

## K čemu slouží

PPW bylo vytvořeno, aby řešilo výzvy energeticky účinného a vysoce přesného polohování v 5G NR, zejména pro zařízení s omezenou kapacitou baterie, jako jsou IoT senzory a chytré telefony. Před jeho zavedením mohly být postupy polohování UE, zejména pro [OTDOA](/mobilnisite/slovnik/otdoa/), neefektivní. UE mohla potřebovat nepřetržitě sledovat PRS signály po dlouhá období nebo napříč mnoha podrámci, aby zachytila měření z více buněk, což vedlo k vysoké spotřebě energie. Koordinace také byla menší, což mohlo způsobit, že UE zpracovávala signály v nevhodných časech nebo propásla synchronizované příležitosti pro měření.

PPW tyto problémy řeší tím, že poskytuje explicitní plánování polohovacích měření v časové doméně. Umožňuje síti přesně kontrolovat, kdy má být UE aktivně zpracovávat PRS, což přímo snižuje spotřebu energie UE – což je primární konstrukční cíl pro NR zařízení. Dále zlepšuje přesnost a spolehlivost měření. Definováním konkrétního okna síť zajistí, že UE měří zdroje PRS, které jsou vysílány koordinovaným, potenciálně řízeným způsobem z hlediska interference (např. pomocí vzorů utlumení). To vede k čistším signálům a přesnějším odhadům času příchodu. Motivace vychází z rozšířených požadavků na polohování v 5G, které vyžadují přesnost na úrovni metru nebo pod metrem pro vertikální aplikace, a to vše při zachování životnosti baterie zařízení, kterou očekávají spotřebitelé a IoT aplikace.

## Klíčové vlastnosti

- Konfigurovatelné časové okno pro sběr měření PRS
- Signalizováno UE prostřednictvím protokolů RRC nebo LPP
- Umožňuje úsporu energie UE omezením doby aktivního zpracování
- Zlepšuje přesnost a spolehlivost polohovacích měření
- Synchronizuje zpracování v UE s vysílacími příležitostmi PRS v síti
- Zásadní pro NR polohovací techniky DL-TDOA a OTDOA

## Související pojmy

- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [DL-TDOA – Downlink Time Difference Of Arrival](/mobilnisite/slovnik/dl-tdoa/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [RSTD – Reference Signal Time Difference](/mobilnisite/slovnik/rstd/)

## Definující specifikace

- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PPW na 3GPP Explorer](https://3gpp-explorer.com/glossary/ppw/)
