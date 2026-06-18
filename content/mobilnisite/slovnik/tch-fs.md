---
slug: "tch-fs"
url: "/mobilnisite/slovnik/tch-fs/"
type: "slovnik"
title: "TCH-FS – Traffic Channel Full rate Speech"
date: 2025-01-01
abbr: "TCH-FS"
fullName: "Traffic Channel Full rate Speech"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tch-fs/"
summary: "GSM provozní kanál přenášející řeč kódovanou plnou rychlostí 13 kbps. Poskytuje základní hlasovou službu a zabírá jeden fyzický časový slot v každém TDMA rámci. Tento základní typ kanálu umožnil počát"
---

TCH-FS je GSM provozní kanál, který přenáší řeč kódovanou plnou rychlostí 13 kbps a poskytuje základní hlasovou službu tím, že zabírá jeden fyzický časový slot v každém TDMA rámci.

## Popis

TCH-FS (Traffic Channel Full rate Speech, provozní kanál pro řeč plné rychlosti) je základním logickým kanálem v systému GSM, definovaným ve specifikacích 3GPP pro okruhově spínané hlasové služby. Funguje jako vyhrazený provozní kanál přidělený jedné mobilní stanici po dobu hovoru. Kanál přenáší digitálně kódovanou řeč plnou rychlostí 13 kbps, což odpovídá původnímu řečovému kodeku GSM definovanému v raných vydáních. Z pohledu fyzické vrstvy zabírá TCH-FS jeden časový slot v rámci [TDMA](/mobilnisite/slovnik/tdma/) rámce na konkrétním rádiovém kmitočtovém kanálu. Struktura kanálu využívá 26rámcový multirámec, kde 24 rámců je použito pro uživatelská řečová data, jeden rámec pro pomalý přidružený řídicí kanál ([SACCH](/mobilnisite/slovnik/sacch/)) pro přenos měřicích hlášení a signalizace a jeden rámec je nečinný. Toto strukturované přidělení zajišťuje nepřetržitý přenos řeči a zároveň umožňuje nezbytnou výměnu řídicích informací bez přerušení hovoru.

Z architektonického hlediska je TCH-FS spravován podsystémem základnových stanic ([BSS](/mobilnisite/slovnik/bss/)), konkrétně základnovou přenosovou stanicí ([BTS](/mobilnisite/slovnik/bts/)) a řadičem základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)). Při sestavení hovoru iniciovaného mobilní stanicí nebo jí přijímaného přidělí síť, je-li dostupný, TCH-FS. Řečová data z mikrofonu uživatele jsou zpracována řečovým kodekem v mobilní stanici a jednotkou pro převod kódu a přizpůsobení rychlosti ([TRAU](/mobilnisite/slovnik/trau/)), která se typicky nachází u BSC nebo ústředny mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)). Zakódovaný datový tok 13 kbps je pak namapován na fyzický rádiový zdroj. Kanál podporuje oba směry, uplink i downlink, prostřednictvím duplexu s kmitočtovým dělením ([FDD](/mobilnisite/slovnik/fdd/)) v GSM, což znamená, že pro vysílání a příjem se používají oddělené kmitočty nosných.

Jeho role v síti je zásadní; byl primárním nositelem kvalitní hlasové služby v sítích 2G. TCH-FS představuje okruhově spínaný zdroj, což znamená, že celý kanál 13 kbps je po dobu hovoru vyhrazen pro jediného uživatele, což zaručuje konzistentní kvalitu, ale s nižší spektrální účinností ve srovnání s pozdějšími kanály poloviční rychlosti nebo adaptivními vícerychlostními kanály. Výkon a správa kanálů TCH-FS přímo ovlivňovaly klíčové síťové metriky, jako je úspěšnost sestavení hovoru, míra přerušených hovorů a celková vnímaná kvalita hlasu účastníky. Ačkoli byl v moderních nasazeních z velké části nahrazen účinnějšími kodeky, porozumění TCH-FS je nezbytné pro pochopení vývoje mobilních hlasových služeb a principů správy vyhrazených provozních kanálů.

## K čemu slouží

TCH-FS byl vytvořen za účelem poskytnutí základní digitální hlasové služby pro standard GSM, která nahradila analogové celulární systémy. Jeho primárním účelem bylo nabídnout mobilním uživatelům spolehlivý, zabezpečený a kvalitní přenos řeči. Digitální kódování a přidělování vyhrazeného kanálu vyřešilo problémy vlastní analogovým systémům, jako je špatná kvalita hlasu na velké vzdálenosti, absence šifrování a neefektivní využití spektra způsobené neustálým vysíláním výkonu. Definováním kanálu plné rychlosti stanovil GSM referenční úroveň pro kvalitu hlasu a přidělování kanálových zdrojů.

Historický kontext představuje vývoj prvního panevropského digitálního celulárního standardu na konci 80. a začátku 90. let 20. století. Klíčovým konstrukčním cílem byla interoperabilita a konzistentní kvalita služeb. TCH-FS se svou pevnou rychlostí 13 kbps poskytoval známý, stabilní požadavek na zdroje pro plánování a dimenzování sítě. Vyřešil omezení spočívající v absenci standardizovaného digitálního hlasového kanálu tím, že vytvořil předvídatelný model provozu pro síťové inženýry. Pevná rychlost však také představovala omezení, protože neumožňovala dynamickou adaptaci na rádiové podmínky nebo požadavky na kapacitu, což motivovalo pozdější vývoj kanálů poloviční rychlosti a adaptivních vícerychlostních kanálů ke zlepšení spektrální účinnosti.

## Klíčové vlastnosti

- Pevný přenos řeči plnou rychlostí 13 kbps
- Zabírá jeden vyhrazený fyzický časový slot v každém TDMA rámci
- Používá strukturu 26rámcového multirámce (24 TCH, 1 SACCH, 1 nečinný)
- Poskytuje okruhově spínaný, vyhrazený zdroj pro jednoho uživatele
- Umožňuje základní signalizaci pro řízení během hovoru prostřednictvím přidruženého SACCH
- Slouží jako základní referenční bod pro výpočty kvality hlasu a kapacity v GSM

## Související pojmy

- [TCH-HS – Traffic Channel Half rate Speech](/mobilnisite/slovnik/tch-hs/)
- [TCH/AFS – Traffic Channel for Adaptive Multi-Rate Full Rate Speech](/mobilnisite/slovnik/tch-afs/)
- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)
- [TRAU – Transcoder and Rate Adaptation Unit (Frame)](/mobilnisite/slovnik/trau/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [TCH-FS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tch-fs/)
