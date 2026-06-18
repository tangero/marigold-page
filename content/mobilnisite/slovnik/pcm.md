---
slug: "pcm"
url: "/mobilnisite/slovnik/pcm/"
type: "slovnik"
title: "PCM – Pulse Code Modulation"
date: 2025-01-01
abbr: "PCM"
fullName: "Pulse Code Modulation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pcm/"
summary: "Standardní metoda pro digitální reprezentaci analogových audio signálů, konkrétně hlasu, využívající kódování ITU-T G.711 A-law nebo μ-law při 64 kbit/s. Tvoří základní digitální formát pro hlas v tra"
---

PCM je standardní metoda pro digitální reprezentaci analogových hlasových signálů pomocí kódování ITU-T G.711 při 64 kbit/s, která tvoří základní hlasový formát pro tradiční telefonii a referenční bod v systémech 3GPP.

## Popis

Pulse Code Modulation (PCM) v kontextu 3GPP konkrétně odkazuje na digitální reprezentaci hlasových signálů definovanou doporučením [ITU-T](/mobilnisite/slovnik/itu-t/) G.711. Zahrnuje tříkrokový proces: vzorkování, kvantování a kódování. Nejprve je spojitý analogový hlasový signál vzorkován rychlostí 8000 vzorků za sekundu (8 kHz) v souladu s Nyquistovým teorémem pro hlasový pásmový přenos do 4 kHz. Každý vzorek je následně kvantován, což znamená, že jeho amplituda je namapována na jednu z konečného počtu úrovní. G.711 definuje dva kompandingové zákony – A-law (používaný primárně v Evropě a na mezinárodních trasách) a μ-law (používaný primárně v Severní Americe a Japonsku) – které signál kvantují nerovnoměrně, poskytují větší přesnost pro signály s nižší amplitudou (které jsou v řeči častější) a menší pro vyšší amplitudy, čímž zlepšují poměr signálu k šumu.

Kvantovaný vzorek je pak zakódován do 8bitového digitálního slova (nebo kódového slova), což vede na konstantní datový tok 64 kbit/s (8000 vzorků/s * 8 bitů/vzorek). Tento 64 kbit/s PCM proud je základním stavebním kamenem digitální okruhově přepínané telefonie, známým jako DS0 timeslot v systémech T1/E1. Ve specifikacích 3GPP se PCM typicky nepoužívá jako rádiový kodek pro přenos vzduchem kvůli jeho vysoké datové neefektivitě. Místo toho se pro optimalizaci rádiového rozhraní používají pokročilejší kodeky jako [AMR](/mobilnisite/slovnik/amr/) (Adaptive Multi-Rate). PCM však plní několik klíčových architektonických rolí.

V jádrové síti, zejména v okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) doméně, je PCM standardním formátem pro propojení mezi síťovými prvky, jako jsou Mobile Switching Centers ([MSC](/mobilnisite/slovnik/msc/)), a mezi [PLMN](/mobilnisite/slovnik/plmn/) a veřejnou telefonní sítí ([PSTN](/mobilnisite/slovnik/pstn/)). Media Gateways ([MGW](/mobilnisite/slovnik/mgw/)) v síti často provádějí transkódování mezi různými hlasovými kodeky (jako je AMR z rozhraní) a standardizovaným PCM formátem pro přenos přes [TDM](/mobilnisite/slovnik/tdm/) (Time-Division Multiplexing) páteřní sítě. Dále PCM slouží jako společný referenční bod pro testování a srovnávání kvality hlasu. Mnoho specifikací výkonu 3GPP (např. TS 26.132 o kvalitě řeči) používá PCM jako vstupní nebo výstupní referenci při definování testovacích metodologií pro jiné kodeky, což zajišťuje, že srovnání kvality probíhá vůči této dobře známé normě.

Jeho role se rozšiřuje na testování služeb a vzájemné propojení. Například při testování kontinuity hovorů nebo vyjednávání kodeků se často používá PCM formát jako základní linie. Rozsáhlý seznam specifikací 3GPP odkazujících na PCM, pokrývající oblasti od slovníku (21.905) přes požadavky na služby (22-series) až po specifikace kodeků (26-series), zdůrazňuje jeho všudypřítomnou povahu jako základní digitální reprezentace hlasu, na které byl vybudován celý ekosystém buněčného hlasu a s níž stále spolupracuje, i když se sítě vyvíjejí směrem k VoLTE a VoNR, které používají IP přenos, ale stále mohou využívat G.711 pro určitá starší propojení nebo záznamové systémy.

## K čemu slouží

PCM, a konkrétně G.711, existuje jako základní standard digitálního hlasového kódování, který umožnil globální přechod z analogové na digitální telefonii. Jeho primárním účelem bylo poskytnout kvalitní, standardizovanou metodu pro převod analogových hlasových signálů do digitálního formátu vhodného pro přenos a přepínání přes digitální sítě. Problém, který řešil, byla potřeba robustního, předvídatelného a interoperabilního digitálního hlasového formátu, který by se mohl stát univerzální „měnou“ pro hlas v páteřních sítích a na síťových hranicích.

Historicky, před digitalizací, byly telefonní sítě zcela analogové, trpěly akumulací šumu, degradací signálu na dlouhé vzdálenosti a neefektivním využitím přenosové infrastruktury. Zavedení PCM se standardem G.711 v roce 1972 vytvořilo univerzální digitální formát. To umožnilo vývoj digitálních ústředen (jako MSC) a přenosových systémů (jako linky T1/E1), které byly spolehlivější, snadněji udržovatelné a umožnily časové multiplexování pro přenos více hovorů na jedné fyzické lince. Volba 64 kbit/s byla pragmatickou rovnováhou mezi kvalitou (vynikající pro telefonii, často označovanou jako 'toll quality') a standardy digitální hierarchie té doby.

V ekosystému 3GPP není účelem specifikace PCM definovat nový kodek, ale zajistit bezproblémovou spolupráci s globální telefonní infrastrukturou. Když byl vyvíjen GSM, používal efektivnější kodeky jako Full Rate (FR) pro rádiové rozhraní, ale jádrová síť a propojení s jinými sítěmi (PSTN, jiné PLMN) se spoléhaly na všudypřítomný standard 64 kbit/s PCM. To umožnilo, aby se mobilní sítě mohly přímo připojit do existující celosvětové telefonní sítě. I když se 3GPP vyvinulo a definovalo mnoho efektivnějších a pokročilejších řečových a audio kodeků (např. AMR, AMR-WB, EVS), PCM zůstává kritické jako pevný referenční bod pro testování kvality, povinný záložní nebo propojovací formát v určitých scénářích a jako formát srozumitelný prakticky všem starším síťovým zařízením a záznamovým/systémům pro legální odposlech, což zajišťuje zpětnou kompatibilitu a soulad s předpisy.

## Klíčové vlastnosti

- Standardizováno ITU-T G.711, využívá A-law nebo μ-law kompanding.
- Pevný datový tok 64 kbit/s (8 kHz vzorkování, 8 bitů/vzorek).
- Poskytuje kvalitní, 'toll-quality' reprezentaci řeči.
- Slouží jako primární digitální formát pro okruhově přepínané páteřní sítě (TDM).
- Působí jako univerzální referenční a propojovací formát mezi různými sítěmi (např. PLMN k PSTN).
- Používá se jako základní linie pro testování kvality hlasu a srovnávání jiných kodeků v 3GPP.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 26.071** (Rel-19) — AMR Speech Codec Introduction
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.115** (Rel-19) — 3GPP TS 26115: Echo Control Requirements
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.171** (Rel-19) — Introduction to AMR-WB Speech Processing
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TS 26.226** (Rel-19) — Cellular Text Telephone Modem (CTM)
- **TS 26.230** (Rel-19) — CTM C Code Implementation for Text Transmission
- **TS 26.231** (Rel-19) — CTM Minimum Performance Requirements Testing
- … a dalších 19 specifikací

---

📖 **Anglický originál a plná specifikace:** [PCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcm/)
