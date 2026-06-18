---
slug: "tch-fs-2"
url: "/mobilnisite/slovnik/tch-fs-2/"
type: "slovnik"
title: "TCH/FS – Traffic Channel / Full Rate Speech"
date: 2025-01-01
abbr: "TCH/FS"
fullName: "Traffic Channel / Full Rate Speech"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tch-fs-2/"
summary: "Plnorychlostní GSM provozní kanál speciálně konfigurovaný pro přenos řeči kódované GSM plnorychlostním (FR) řečovým kodekem. Poskytoval standardní hlasovou službu v raných sítích GSM, zabírá vyhrazený"
---

TCH/FS je plnorychlostní GSM provozní kanál konfigurovaný pro přenos řeči kódované GSM plnorychlostním kodekem, který poskytuje standardní hlasovou službu zabírající vyhrazený časový slot v každém rámci.

## Popis

[TCH](/mobilnisite/slovnik/tch/)/[FS](/mobilnisite/slovnik/fs/) je specifická instance plnorychlostního provozního kanálu ([TCH/F](/mobilnisite/slovnik/tch-f/)) optimalizovaná pro hlasovou službu využívající původní GSM plnorychlostní ([FR](/mobilnisite/slovnik/fr/)) řečový kodek. Jedná se o logický kanál, který rezervuje plný fyzický zdroj – jeden časový slot v každém [TDMA](/mobilnisite/slovnik/tdma/) rámci na dané nosné frekvenci – pro výlučné použití jednoho hovoru. GSM FR kodek používaný s TCH/FS je kodek typu Regular Pulse Excitation – Long-Term Prediction ([RPE-LTP](/mobilnisite/slovnik/rpe-ltp/)) pracující s čistou přenosovou rychlostí 13 kbit/s. Tento 13 kbit/s řečový proud je následně zpracován řetězcem GSM kanálového kódování.

Technické fungování zahrnuje několik kroků. Nejprve je analogový hlasový signál digitalizován a komprimován FR kodekem do 260bitových řečových rámců každých 20 ms. Těchto 260 bitů je klasifikováno do tříd Ia (50 bitů, nejcitlivější), Ib (132 bitů, středně citlivé) a [II](/mobilnisite/slovnik/ii/) (78 bitů, nejméně citlivé). Bity třídy Ia jsou chráněny 3bitovým [CRC](/mobilnisite/slovnik/crc/) pro detekci chyb a poté jsou bity tříd Ia a Ib společně zakódovány konvolučním kódem s poměrem 1/2. Bity třídy II jsou přenášeny bez jakéhokoli kanálového kódování. Výsledkem je celkem 456 zakódovaných bitů na 20ms blok, což odpovídá hrubé přenosové rychlosti 22,8 kbit/s. Těchto 456 bitů je následně prokládáno a rozloženo do 8 normálních záblesků v rámci TDMA struktury.

Kanál se nachází ve standardním 26rámcovém multirámci. Z 26 rámců je 24 použito pro přenos těchto prokládaných řečových bloků, jeden je použit pro pomalý přidružený řídicí kanál (SACCH) pro přenos průběžných měřicích reportů a jeden je nečinný. Tato struktura zajišťuje periodickou signalizaci bez přerušení řečového toku. TCH/FS poskytuje konstantní, předvídatelnou kvalitu služby a byl hlavním nástrojem pro hlasovou komunikaci v sítích GSM před zavedením vylepšených a adaptivních kodeků.

## K čemu slouží

TCH/FS byl vytvořen jako výchozí kanál pro hlasové služby v úvodních sítích GSM. Jeho účelem bylo poskytovat telefonní kvalitu digitálního hlasu přes rádiové rozhraní, což byl významný pokrok oproti analogovým systémům, které nahradil. GSM FR kodek a kanál TCH/FS společně řešily klíčové problémy analogové buněčné sítě: špatnou kvalitu hlasu náchylnou k šumu a útlumu, nedostatek zabezpečení (hovory bylo možné snadno odposlouchávat) a neefektivní využití frekvencí.

Konstrukce TCH/FS byla motivována potřebou robustního, standardizovaného digitálního přenosu. Pevná přenosová rychlost 13 kbit/s a specifické schéma kanálového kódování byly navrženy jako kompromis mezi kvalitou řeči, odolností vůči chybám a spektrální účinností. Stanovil spolehlivou základní linii – jeden časový slot, jeden hovor – což zjednodušilo návrh sítě, fakturaci (založenou na době připojení) a interoperabilitu mezi zařízeními různých výrobců. Přestože jeho kvalita řeči byla později překonána vylepšeným plnorychlostním (EFR) a AMR kodekem, byl TCH/FS nezbytný pro počáteční nasazení a široké přijetí GSM jako prvního skutečně digitálního a globálního buněčného standardu.

## Klíčové vlastnosti

- Vyhrazený plnorychlostní kanál využívající GSM plnorychlostní (FR) RPE-LTP řečový kodek s přenosovou rychlostí 13 kbit/s.
- Používá nerovnoměrnou ochranu proti chybám: bity tříd Ia/Ib jsou konvolučně kódovány, bity třídy II nejsou kódovány.
- Generuje 456 zakódovaných bitů na 20ms řečový rámec, prokládaných přes 8 po sobě jdoucích TDMA záblesků.
- Dodržuje strukturu 26rámcového multirámce s integrovaným SACCH pro řídicí signalizaci.
- Poskytuje pevné, okruhově přepínané spojení zaručující konzistentní šířku pásma pro hlasový hovor.
- Sloužil jako primární hlasový přenos pro počáteční nasazení sítí GSM a zůstává záložní možností.

## Související pojmy

- [TCH/F – Traffic Channel / Full Rate](/mobilnisite/slovnik/tch-f/)
- [TCH/AHS – Traffic Channel / Adaptive Multi-Rate Half Rate Speech](/mobilnisite/slovnik/tch-ahs/)
- [RPE-LTP – Regular Pulse Excited codec with Long Term Prediction](/mobilnisite/slovnik/rpe-ltp/)
- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [TCH/FS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tch-fs-2/)
