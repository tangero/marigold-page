---
slug: "tfo"
url: "/mobilnisite/slovnik/tfo/"
type: "slovnik"
title: "TFO – Tandem Free Operation"
date: 2025-01-01
abbr: "TFO"
fullName: "Tandem Free Operation"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tfo/"
summary: "Mechanismus, který umožňuje obejít dva transkodéry v hovoru mezi mobilními stanicemi a umožnit přímou výměnu kódovaných řečových rámců. Tím se zachová původní kvalita hlasu, protože se předejde vícená"
---

TFO je mechanismus, který obchází dva transkodéry v hovoru mezi mobilními stanicemi a umožňuje přímou výměnu kódovaných řečových rámců, čímž zachovává původní kvalitu hlasu tím, že se vyhne vícenásobným tandemovým transkódovacím operacím.

## Popis

Tandem Free Operation (TFO, provoz bez tandemového transkódování) je síťová funkce navržená ke zlepšení kvality řeči od konce ke konci v mobilní telefonii, zejména pro hovory mezi mobilními stanicemi. V tradičním sestavení hovoru je řeč z mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) zakódována pomocí specifického kodeku (např. [AMR](/mobilnisite/slovnik/amr/) v UMTS/GSM). Tento kódovaný řečový rámec je přenášen vzduchem do subsystému základnových stanic ([BSS](/mobilnisite/slovnik/bss/)), kde je transkodérem ([TC](/mobilnisite/slovnik/tc/)) dekódován na standardní [PCM](/mobilnisite/slovnik/pcm/) signál (Pulse Code Modulation) o rychlosti 64 kbps (A-zákon nebo μ-zákon) pro přenos přes páteřní síť (CN). Na druhém konci další TC překóduje PCM signál do formátu kodeku požadovaného cílovou MS. Tento dvojitý transkódovací proces se nazývá 'tandemové kódování' a zavádí kvantizační šum a zkreslení, což degraduje kvalitu řeči.

TFO funguje tak, že mezi dvěma transkodéry zapojenými do hovoru vytvoří signalizační kanál v pásmu. Když obě MS používají kompatibilní kodeky (např. obě podporují AMR), transkodéry vyjednají přechod do režimu TFO. V tomto režimu přestanou provádět plné dekódování/překódování. Místo toho extrahují přijaté kódované řečové rámce z příchozího PCM bitového toku a transparentně je vloží do odchozího PCM bitového toku směrem k druhému konci. Samotný PCM kanál zůstává standardním 64 kbps kanálem, což zajišťuje zpětnou kompatibilitu se všemi síťovými přepínacími prvky, které o TFO nevědí. Kódované řečové rámce jsou vloženy do nejméně významných bitů PCM vzorků, což je proces často označovaný jako 'bit-stealing' nebo 'rámování v pásmu'.

Klíčovými architektonickými komponentami jsou transkodéry s podporou TFO (často součást Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) v pozdějších architekturách) a protokol TFO. Protokol běží přímo mezi transkodéry přes PCM spoje, využívá definovanou rámcovou strukturu a sadu zpráv pro vyjednávání schopností, aktivaci, deaktivaci a zpracování chyb. Když je aktivní, řečová cesta se efektivně stává přímým digitálním spojením pro kódované řečové bity mezi dvěma MS, čímž se obejdou škodlivé efekty tandemového transkódování. To vede ke kvalitě řeči ekvivalentní jedinému cyklu kódování/dekódování, což výrazně zlepšuje srozumitelnost a přirozenost. TFO je obzvláště cenné v mezinárodních roamingu, kde hovor může procházet více sítěmi, z nichž každá může vkládat své vlastní transkodéry.

## K čemu slouží

TFO bylo vytvořeno, aby vyřešilo výrazné zhoršení kvality řeči způsobené vícenásobnými, zbytečnými operacemi transkódování řečových kodeků v mobilních hovorech od konce ke konci. V počátcích digitálních celulárních sítí (GSM) byla páteřní síť převážně okruhově spínaná a založená na 64 kbps [PCM](/mobilnisite/slovnik/pcm/). Transkodéry byly nezbytné pro převod nízkobitových, šířku pásma efektivních kodeků vzdušného rozhraní (jako Full Rate nebo Half Rate) na/z PCM. Nicméně, v hovoru mezi mobilními stanicemi, kde oba konce používají stejný nebo kompatibilní kodek, mezilehlá PCM konverze a dvojité transkódování neměly žádný jiný účel než síťovou kompatibilitu, zatímco aktivně poškozovaly kvalitu.

Historický kontext byl spojen se zavedením sítí 2G a následnou snahou nabídnout kvalitu hlasu konkurenceschopnou nebo lepší než u pevných služeb. Omezení předchozího přístupu (povinné tandemové transkódování) byla jasná: snížená srozumitelnost, přidaný šum a 'dutý' nebo 'kovový' zvuk charakteristický pro vícenásobnou generaci kodeků. Účelem TFO je transparentně obejít tuto neefektivitu bez nutnosti modernizace celé infrastruktury páteřní sítě. Využívá stávajících PCM tras, což z něj dělá nákladově efektivní softwarový upgrade pro transkodéry. Tímto se přímo řešil problém eroze kvality v propojených sítích a TFO se stalo klíčovou funkcí pro operátory, aby garantovali vysokou kvalitu hlasové služby, zejména s nasazením prémiových kodeků jako [AMR](/mobilnisite/slovnik/amr/) s více módy. Položilo to základy pro pokročilejší koncepty jako TrFO (Transcoder Free Operation) ve 3G, které se zcela vyhýbají umístění transkodérů do cesty.

## Klíčové vlastnosti

- Obchází tandemové transkodéry, aby zachoval původní kvalitu řečového kodeku
- Používá signalizaci v pásmu přes standardní 64 kbps PCM okruhy
- Funguje transparentně vůči přepínačům páteřní sítě
- Automaticky vyjednává mezi kompatibilními transkodéry s podporou TFO
- Podporuje různé řečové kodeky (např. GSM FR/HR/EFR, AMR, AMR-WB)
- Poskytuje zpětnou kompatibilitu; při selhání TFO přejde zpět na normální transkódování

## Definující specifikace

- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.877** (Rel-6) — Speech Recognition Framework Analysis
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description
- **TS 29.232** (Rel-19) — Mc Interface Protocol Profile
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [TFO na 3GPP Explorer](https://3gpp-explorer.com/glossary/tfo/)
