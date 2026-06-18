---
slug: "efr"
url: "/mobilnisite/slovnik/efr/"
type: "slovnik"
title: "EFR – Enhanced Full Rate speech codec"
date: 2025-01-01
abbr: "EFR"
fullName: "Enhanced Full Rate speech codec"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/efr/"
summary: "Enhanced Full Rate (EFR) je standard kodeku řeči pro sítě GSM, který poskytuje výrazně lepší kvalitu hlasu ve srovnání s původním kodekem s plnou rychlostí (FR). Pracuje při 12,2 kbps a využívá algori"
---

EFR je standard kodeku řeči se zvýšenou plnou rychlostí pro sítě GSM, který pracuje při 12,2 kbps a využívá algoritmus ACELP k poskytnutí audia téměř srovnatelné kvality s pevnou linkou, což výrazně zlepšuje původní kodek s plnou rychlostí.

## Popis

GSM Enhanced Full Rate (EFR) je kodek řeči s přenosovou rychlostí 12,2 kbps standardizovaný organizacemi 3GPP a [ETSI](/mobilnisite/slovnik/etsi/). Používá kódovací techniku Algebraic Code Excited Linear Prediction ([ACELP](/mobilnisite/slovnik/acelp/)), která byla v době svého zavedení špičkovou metodou. Kodek zpracovává 20ms rámce řeči, z nichž každý obsahuje 160 vzorků při vzorkovací frekvenci 8 kHz. Pro každý rámec analyzuje kodér řečový signál, aby extrahoval parametry reprezentující lineární prediktivní filtr ([LPC](/mobilnisite/slovnik/lpc/)), adaptivní kodebook (pitch) a pevný algebraický kodebook (inovace). Tyto parametry jsou následně kvantovány a přenášeny přes rádiové rozhraní při čisté přenosové rychlosti 12,2 kbps, která se po aplikaci kanálového kódování pro ochranu proti chybám vejde do hrubé přenosové rychlosti GSM kanálu.

Dekodér EFR na přijímací straně rekonstruuje řečový signál průchodem excitačního signálu (odvozeného z adaptivního a pevného kodebooku) přes syntézní filtr (definovaný parametry LPC). Kritickou součástí EFR jsou jeho robustní kanálové kódování a mechanismy pro maskování chyb. Používá konvoluční kód s poměrem 1/2 pro dopřednou korekci chyb ([FEC](/mobilnisite/slovnik/fec/)) a zahrnuje sofistikované algoritmy pro detekci a maskování chybných rámců, což zajišťuje přijatelnou kvalitu hlasu i při středních podmínkách rádiového kanálu. Kodek je navržen tak, aby byl interoperabilní, a jeho podpora je povinná pro GSM koncová zařízení v příslušných kmitočtových pásmech.

Architektura EFR je integrována do GSM kanálu pro přenos hovoru s plnou rychlostí ([TCH/FS](/mobilnisite/slovnik/tch-fs-2/)). Při sestavování hovoru mohou síť a mobilní stanice vyjednat použití EFR, pokud jej obě podporují, jinak dojde k návratu k původnímu kodeku s plnou rychlostí ([FR](/mobilnisite/slovnik/fr/)) nebo s poloviční rychlostí ([HR](/mobilnisite/slovnik/hr/)). Výkon kodeku je charakterizován vysokými hodnotami středního známkování ([MOS](/mobilnisite/slovnik/mos/)), které často přesahují 4,0 za čistých kanálových podmínek, což byl podstatný pokrok oproti hodnotě MOS kodeku FR kolem 3,5. Díky tomu se EFR stal klíčovým prvkem pro komerční mobilní hlasové služby vysoké kvality.

## K čemu slouží

Kodek EFR byl vyvinut, aby řešil hlavní uživatelskou výtku v raných sítích GSM: kvalitu hlasu, která byla znatelně horší než u telefonie přes pevnou linku. Původní GSM kodek s plnou rychlostí (FR), ačkoli byl ve své době revolučním digitálním kodekem, měl omezení v kvalitě zvuku, zejména při přítomnosti šumu na pozadí nebo u určitých typů mluvčích. Konkurenční prostředí a uživatelská očekávání si vyžádaly mobilní hlasovou službu srovnatelnou s kvalitou pevné linky.

K jeho vzniku motivoval pokrok v algoritmech kódování řeči, zejména technika ACELP, která nabízela lepší kompromis mezi přenosovou rychlostí, složitostí a kvalitou. Cílem bylo vyvinout kodek, který by mohl využívat stávající strukturu GSM kanálu (kanál s plnou rychlostí) bez nutnosti změn rádiové infrastruktury, což zajistilo hladkou cestu upgradu. EFR to poskytl tím, že jeho datový tok 12,2 kbps se vešel do kapacity kanálu po aplikaci podobné režie kanálového kódování jako u kodeku FR.

EFR vyřešil problém vnímané kvality hlasu, což bylo klíčové pro spokojenost zákazníků a diferenciaci sítě. Umožnil operátorům nabízet kvalitu hlasu 'jako na pevné lince'. Jeho robustnost vůči přenosovým chybám navíc zajišťovala, že zlepšení kvality bylo zachováno i v reálných podmínkách buněčných sítí. EFR stanovil nový standard pro mobilní hlas a připravil cestu pro následující kodeky, jako je AMR, který zahrnul EFR jako jeden ze svých provozních režimů.

## Klíčové vlastnosti

- Pracuje při čisté přenosové rychlosti 12,2 kbps s využitím algoritmu ACELP
- Poskytuje vysokou kvalitu hlasu s hodnotami MOS často nad 4,0
- Využívá robustní kanálové kódování (konvoluční kód s poměrem 1/2) pro ochranu proti chybám
- Zahrnuje pokročilé techniky pro zpracování chybných rámců a maskování chyb
- Plně zpětně kompatibilní s GSM kanálem pro přenos hovoru s plnou rychlostí (TCH/FS)
- Povinná podpora v GSM koncových zařízeních v pásmech, kde je specifikován

## Související pojmy

- [TCH-FS – Traffic Channel Full rate Speech](/mobilnisite/slovnik/tch-fs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.813** (Rel-10) — Enhanced Voice Services for EPS Study
- **TS 26.077** (Rel-19) — AMR Noise Suppression Minimum Performance Requirements
- **TS 26.090** (Rel-19) — AMR Speech Codec Detailed Mapping Specification
- **TS 26.447** (Rel-19) — EVS Frame Loss Concealment Procedure
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description
- **TS 43.068** (Rel-19) — Voice Group Call Service (VGCS) Stage 2
- **TS 43.069** (Rel-19) — Voice Broadcast Service (VBS) Stage 2
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance
- **TS 46.085** (Rel-19) — GSM Speech Codec Interoperability Test Report

---

📖 **Anglický originál a plná specifikace:** [EFR na 3GPP Explorer](https://3gpp-explorer.com/glossary/efr/)
