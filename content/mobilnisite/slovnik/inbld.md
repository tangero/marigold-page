---
slug: "inbld"
url: "/mobilnisite/slovnik/inbld/"
type: "slovnik"
title: "INBLD – Independent Non-Base Layer Decoding"
date: 2025-01-01
abbr: "INBLD"
fullName: "Independent Non-Base Layer Decoding"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/inbld/"
summary: "Technika videokódování v kodeku Enhanced Voice Services (EVS) od 3GPP, kde mohou být nerozšířující (rozšiřující) vrstvy škálovatelného datového toku dekódovány nezávisle, bez nutnosti spoléhat se na z"
---

INBLD je technika videokódování v kodeku EVS, kde mohou být rozšiřující vrstvy dekódovány nezávisle na základní vrstvě za účelem zlepšení odolnosti proti chybám a kvality zvuku při špatných síťových podmínkách.

## Popis

Independent Non-Base Layer Decoding (INBLD) je pokročilá funkce kodeku Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) od 3GPP, specifikovaná v TS 26.948. EVS je škálovatelný a vestavěný kodek, což znamená, že jeho datový tok je strukturován do vrstev: povinná základní vrstva ([BL](/mobilnisite/slovnik/bl/)) poskytující základní kvalitu zvuku a jedna nebo více rozšiřujících vrstev ([EL](/mobilnisite/slovnik/el/)), které postupně kvalitu zlepšují (např. vyšší šířkou pásma, lepším stereem). Tradičně ve škálovatelném audiokódování dekódování rozšiřující vrstvy vyžaduje úspěšné dekódování všech nižších vrstev (včetně základní vrstvy). Pokud je základní vrstva poškozena nebo ztracena kvůli ztrátě paketů, rozšiřující vrstvy se stanou nepoužitelnými, což vede k výraznému poklesu kvality zvuku.

INBLD tuto závislostní strukturu modifikuje. Umožňuje dekodéru pokusit se dekódovat a využít přijatou nerozšířující (rozšiřující) vrstvu, i když je základní vrstva pro daný snímek chybějící nebo poškozená. Toho je dosaženo návrhem kódování rozšiřující vrstvy tak, aby byla částečně soběstačná. Zatímco data rozšiřující vrstvy jsou stále optimálně predikována ze základní vrstvy pro maximální kompresní účinnost, INBLD zahrnuje dodatečné informace nebo využívá kódovací techniky umožňující záložní cestu dekódování. Když základní vrstva není k dispozici, dekodér použije tato doplňková data v rámci samotného paketu rozšiřující vrstvy spolu se stavovými informacemi z dříve správně dekódovaných snímků k syntéze věrohodného zvukového signálu. Výstupní kvalita z dekódování pouze rozšiřující vrstvy je nižší než při dekódování celého škálovatelného toku, ale je výrazně lepší než nemít žádná dekódovatelná data (což by vedlo ke skrytí snímku nebo chybě).

Z architektonického hlediska INBLD zahrnuje úpravy jak na straně kodéru, tak dekodéru. Kodér musí generovat datový tok rozšiřující vrstvy s potřebnou redundancí nebo nezávislými kódovacími prvky pro podporu záložního režimu. Dekodér musí implementovat logiku pro detekci ztráty základní vrstvy a přepnutí do nezávislého dekódovacího režimu pro rozšiřující vrstvu. Tato funkce pracuje na bázi snímek po snímku a je klíčovou součástí robustních mechanismů pro skrytí chyb a odolnosti proti ztrátě paketů v EVS, které jsou kritické pro udržení vysoké kvality hlasu přes nespolehlivé kanály jako VoLTE a VoNR.

## K čemu slouží

INBLD byl vyvinut k řešení zásadní slabiny tradičních vrstvených (škálovatelných) kodeků v prostředích ztrátových paketových sítí, jako jsou mobilní IP sítě (3G, 4G, 5G). V takových sítích je ztráta paketů běžná kvůli rádiovému rušení, přechodům mezi buňkami nebo přetížení. Škálovatelná struktura kodeku [EVS](/mobilnisite/slovnik/evs/) je účinná pro přizpůsobení šířky pásma, ale její silná závislost vrstev jej činila zranitelným: ztráta paketu základní vrstvy by zneplatnila všechny rozšiřující vrstvy pro daný snímek, což způsobilo závažné a náhlé zhoršení kvality. To bylo v rozporu s cílem EVS poskytovat vynikající kvalitu a robustnost, zejména pro Voice over LTE (VoLTE) a budoucí služby.

Tato technologie řeší tento problém snížením kritické závislosti dekodéru na základní vrstvě, čímž „rozprostře“ dopad ztráty paketů. Namísto scénáře vše-nebo-nic poskytuje INBLD cestu k postupnému snižování kvality. Když je základní vrstva ztracena, síť nebo přijímač může stále mít paket rozšiřující vrstvy (který mohl jít jinou cestou nebo být v samostatném RTP paketu). INBLD umožňuje systému zachránit tato data k vytvoření použitelného zvuku, čímž zabrání úplnému kolapsu vnímané kvality. To je obzvláště důležité pro stereo hudbu s vysokým datovým tokem nebo hovory s vysokou kvalitou zvuku, kde rozšiřující vrstvy nesou významnou percepční informaci.

Motivace pro INBLD vzešla z vyvíjejících se případů užití pro kodek EVS, který byl navržen nejen pro úzkopásmový hlas, ale také pro streamování hudby ve vysoké kvalitě, konferenční hovory a imerzivní komunikaci. Tyto aplikace vyžadují vyšší spolehlivost a konzistenci kvality. Zavedením INBLD ve verzi 13 3GPP posílilo odolnost kodeku EVS proti chybám bez obětování jeho základní škálovatelné účinnosti, čímž zajistilo, že může splnit slib vysokokvalitních audiokódovacích služeb v proměnných podmínkách mobilních širokopásmových sítí.

## Klíčové vlastnosti

- Umožňuje dekódování datových toků rozšiřující vrstvy bez odpovídající základní vrstvy
- Zlepšuje odolnost proti chybám a kvalitu zvuku při ztrátě paketů snímků základní vrstvy
- Součást specifikace kodeku Enhanced Voice Services (EVS) od 3GPP
- Poskytuje postupné snižování kvality namísto katastrofického selhání
- Vyžaduje specifickou podporu kodéru a dekodéru, jak je definováno v TS 26.948
- Pracuje v součinnosti s dalšími funkcemi robustnosti EVS, jako je režim channel-aware mode

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [INBLD na 3GPP Explorer](https://3gpp-explorer.com/glossary/inbld/)
