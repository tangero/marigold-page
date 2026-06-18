---
slug: "dscs"
url: "/mobilnisite/slovnik/dscs/"
type: "slovnik"
title: "DSCS – Distant Supported Codec Set"
date: 2025-01-01
abbr: "DSCS"
fullName: "Distant Supported Codec Set"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dscs/"
summary: "Sada kodeků podporovaných vzdáleným koncovým zařízením v komunikační relaci. Umožňuje efektivní vyjednávání kodeků mezi koncovými body, čímž zajišťuje kompatibilní a optimální kódování/dekódování médi"
---

DSCS je sada kodeků podporovaných vzdáleným koncovým zařízením, která umožňuje efektivní vyjednávání za účelem zajištění kompatibilního a optimálního kódování a dekódování médií pro služby, jako jsou hlasové a videohovory.

## Popis

Distant Supported Codec Set (DSCS) je koncept definovaný ve specifikacích 3GPP, především v TS 28.062, který se zabývá správou a testováním sítě. Odkazuje na soubor audio a video kodeků, které může vzdálené uživatelské zařízení (UE) nebo koncové zařízení podporovat během komunikační relace. Při typickém zřizování relace, jako je hlasový nebo videohovor, si koncové body vyměňují své podporované sady kodeků, aby vyjednaly nejvhodnější kodek pro spojení. Toto vyjednávání je klíčové pro zajištění interoperability mezi různými zařízeními a sítěmi, protože umožňuje výběr společného kodeku, který mohou oba konce efektivně kódovat a dekódovat. DSCS je typicky sdělován během protokolů pro zahájení relace, jako je [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol), kde každý koncový bod uvádí své schopnosti a síť nebo samotné koncové body určí optimální kodek na základě faktorů, jako je šířka pásma, latence a požadavky na kvalitu.

Z architektonického hlediska DSCS funguje v rámci širšího rámce zpracování médií v sítích 3GPP a zahrnuje komponenty jako UE, jádro sítě (např. IMS – IP Multimedia Subsystem) a případně mezilehlé uzly, jako jsou mediální brány. Při zahájení hovoru iniciující UE odešle svou lokálně podporovanou sadu kodeků a vzdálené UE odpoví svou DSCS. Tato výměna často probíhá prostřednictvím signalizačních zpráv, což síti umožňuje usnadnit výběr kodeku nebo v případě potřeby transkódování. Mezi klíčové zapojené komponenty patří mediální procesní jednotky UE, jádro IMS pro správu relací a funkce řízení politik, které mohou vynucovat preference kodeků na základě síťových podmínek nebo profilů účastníků. Úlohou DSCS je umožnit dynamickou adaptaci na měnící se síťová prostředí a zajistit, aby mediální proudy byly kódovány ve formátu, který vyvažuje kvalitu a využití zdrojů.

V praxi DSCS přispívá k efektivnímu využití zdrojů a lepší uživatelské zkušenosti. Vyjednáváním kodeků minimalizuje potřebu transkódování – procesu převodu médií z jednoho kodeku na druhý – který může zavádět zpoždění a zhoršovat kvalitu. Namísto toho, pokud je nalezen společný kodek v sadách obou koncových bodů, je možné přímé streamování, což snižuje režii zpracování. To je obzvláště důležité v mobilních sítích, kde jsou omezeny šířka pásma a výdrž baterie. Mechanismus DSCS podporuje širokou škálu kodeků, od starších, jako je [AMR](/mobilnisite/slovnik/amr/) (Adaptive Multi-Rate) pro hlas, po moderní, jako je [EVS](/mobilnisite/slovnik/evs/) (Enhanced Voice Services), a video kodeky, jako je H.264 nebo H.265, což sítím umožňuje vyvíjet se s pokročilou technologií při zachování zpětné kompatibility.

## K čemu slouží

DSCS bylo zavedeno, aby řešilo výzvu interoperability kodeků v heterogenních komunikačních prostředích. Před jeho standardizací mohly koncové body podporovat různé kodeky, což vedlo k neúspěšným relacím nebo suboptimální kvalitě médií kvůli vynucenému transkódování nebo použití výchozích záložních kodeků. To bylo obzvláště problematické s rozšiřováním mobilních sítí a vstupem zařízení od různých výrobců s odlišnými schopnostmi na trh. Vytvoření DSCS poskytlo strukturovaný způsob, jak mohou koncové body inzerovat svou podporu kodeků, a umožnilo automatizované vyjednávání, které zajišťuje, že relace mohou být navázány s nejlepší možnou audio a video kvalitou v daných omezeních.

Historicky se rané mobilní sítě spoléhaly na pevné kodeky, ale s příchodem 3G a později 4G/5G se rozmanitost kodeků zvýšila, aby podpořila vyšší efektivitu a nové služby, jako je [HD](/mobilnisite/slovnik/hd/) hlas a videohovory. DSCS, zavedené ve verzi 8, bylo v souladu s růstem IMS a plně IP sítí, kde se dynamická správa relací stala nezbytnou. Řešilo omezení, jako jsou pevná přiřazení kodeků, která mohla plýtvat šířkou pásma nebo způsobovat nekompatibility, zejména v roamingu nebo při mezisíťových hovorech. Tím, že umožňuje koncovým bodům sdílet své podporované sady, DSCS usnadňuje plynulejší interakce a přizpůsobuje se síťovým podmínkám, jako je přetížení, potenciálním výběrem efektivnějšího kodeku.

Dále DSCS podporuje inovace služeb tím, že umožňuje zavádění nových kodeků bez narušení stávajících zařízení. Jak se sítě vyvíjejí, operátoři mohou nasazovat pokročilé kodeky pro lepší kompresi nebo kvalitu a DSCS zajišťuje, že je použijí pouze schopná koncová zařízení, zatímco ostatní přejdou na starší varianty. Tato zpětná kompatibilita je klíčová pro udržení kontinuity služeb a spokojenosti uživatelů, což činí z DSCS základní prvek pro multimediální služby v ekosystémech 3GPP.

## Klíčové vlastnosti

- Umožňuje dynamické vyjednávání kodeků mezi komunikačními koncovými body
- Podporuje širokou škálu audio a video kodeků pro flexibilitu
- Snižuje potřebu transkódování výběrem společných podporovaných kodeků
- Integruje se s IMS a protokoly pro zahájení relace, jako je SIP
- Usnadňuje zpětnou kompatibilitu se staršími zařízeními
- Přizpůsobuje se síťovým podmínkám tím, že umožňuje výběr kodeku na základě schopností

## Související pojmy

- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [DSCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dscs/)
