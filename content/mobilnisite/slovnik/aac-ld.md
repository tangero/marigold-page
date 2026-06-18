---
slug: "aac-ld"
url: "/mobilnisite/slovnik/aac-ld/"
type: "slovnik"
title: "AAC-LD – Advanced Audio Coding – Low Delay"
date: 2025-01-01
abbr: "AAC-LD"
fullName: "Advanced Audio Coding – Low Delay"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aac-ld/"
summary: "AAC-LD je audio kodek s nízkým zpožděním standardizovaný organizací 3GPP pro služby komunikace v reálném čase. Poskytuje vysoce kvalitní stereo zvuk s algoritmickým zpožděním pouhých 20 ms, což umožňu"
---

AAC-LD je audio kodek s nízkým zpožděním standardizovaný organizací 3GPP pro služby komunikace v reálném čase, jako je VoLTE, poskytující vysoce kvalitní stereo zvuk s minimální latencí pro přirozené konverzace.

## Popis

Advanced Audio Coding – Low Delay (AAC-LD) je člen rodiny audio kodeků MPEG-4 [AAC](/mobilnisite/slovnik/aac/), speciálně optimalizovaný pro aplikace vyžadující velmi nízké koncové zpoždění při zachování vysoké zvukové kvality. Jak je standardizováno v 3GPP TS 26.923, AAC-LD je transformační percepční audio kodek. Funguje tak, že rozdělí vstupní audio signál do překrývajících se bloků, transformuje je do frekvenční domény pomocí modifikované diskrétní kosinové transformace ([MDCT](/mobilnisite/slovnik/mdct/)) a aplikuje sofistikované psychoakustické modely k identifikaci a kvantizaci pouze percepčně relevantních složek signálu. Tento proces umožňuje efektivní kompresi dat odstraněním neslyšitelných informací. Kodek podporuje širokou škálu vzorkovacích frekvencí (např. 8 kHz až 48 kHz) a datových toků, typicky od 32 kbps do 64 kbps na kanál pro vysoce kvalitní stereo komunikaci.

Architektonicky je AAC-LD navržen jako profil s nízkým zpožděním kodeku AAC. Jeho klíčovou inovací je zmenšení vyrovnávací paměti pro předhlédnutí a použití kratšího transformačního okna. Zatímco standardní AAC kodeky používají pro vysokou účinnost 2048-vzorkové okno, AAC-LD používá kratší 512- nebo 480-vzorkové okno (v závislosti na vzorkovací frekvenci), což radikálně snižuje algoritmické zpoždění. Výsledkem je celkové zpoždění kodeku přibližně 20 ms, což je zásadní pro zachování kvality konverzace při obousměrné komunikaci. Struktura kodeku zahrnuje moduly pro mapování čas/frekvence, percepční tvarování šumu, kvantizaci a bezeztrátové kódování (pomocí Huffmanova kódování). Zahrnuje také nástroje jako Temporal Noise Shaping ([TNS](/mobilnisite/slovnik/tns/)) pro kontrolu artefaktů předozvěně, které jsou výraznější u kratších oken.

V rámci ekosystému 3GPP funguje AAC-LD jako povinný kodek pro určité služby komunikace v reálném čase. Je integrován do funkcí zpracování médií v IP Multimedia Subsystem (IMS) pro paketově přepínané hlasové a video služby. Například ve službách Voice over LTE (VoLTE) a Video over LTE (ViLTE) lze o AAC-LD vyjednávat během výměny nabídky/odpovědi Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)) jako součást signalizace Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)). Zakódované audio rámce jsou paketovány do paketů Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) pro přenos přes IP přenosovou vrstvu. Jeho úlohou je poskytovat vysoce věrný audio zážitek s nízkou latencí, který je percepčně nerozlišitelný od osobní konverzace, což je základním požadavkem pro přijetí telefonních a konferenčních služeb přes mobilní širokopásmové sítě uživateli.

Výkon AAC-LD je charakterizován výbornou zvukovou kvalitou při nízkých datových tocích, která soupeří s kodeky s vyšším zpožděním, jako je standardní [AAC-LC](/mobilnisite/slovnik/aac-lc/), ale s profilem zpoždění vhodným pro interaktivní použití. Podporuje jak mono, tak stereo konfigurace, což jej činí vhodným pro sdílení hudby a vysoce kvalitní konferenční hovory. Důležitá je také odolnost kodeku vůči ztrátě paketů, která je často řešena ve spojení s technikami maskování chyb založenými na RTP na straně přijímače. Jeho implementace v zařízeních a síťových prvcích vyžaduje pečlivou optimalizaci výpočetní složitosti, aby bylo zajištěno efektivní fungování na mobilních procesorech při dodržení přísného rozpočtu zpoždění pro koncové mediální cesty.

## K čemu slouží

AAC-LD byl vytvořen, aby řešil specifickou potřebu vysokokvalitního audia s nízkou latencí pro obousměrnou komunikaci v reálném čase přes paketově přepínané sítě. Před jeho přijetím se mobilní telefonie primárně spoléhala na úzkopásmové řečové kodeky jako [AMR-NB](/mobilnisite/slovnik/amr-nb/), které, ačkoli měly nízké zpoždění, nabízely omezenou šířku pásma a kvalitu nevhodnou pro hudbu nebo vysoce věrný hlas. Pro multimediální služby standardní audio kodeky jako AAC-LC nebo MP3 poskytovaly vysokou kvalitu, ale zaváděly vysoké algoritmické zpoždění (často přes 100 ms) kvůli použití dlouhých analytických oken pro účinnost komprese. Toto vysoké zpoždění je škodlivé pro interaktivitu konverzace, způsobuje znatelné efekty překřikování a narušuje přirozený průběh dialogu.

Motivace pro AAC-LD vycházela z vývoje mobilních sítí směrem k plně IP architekturám, jako je LTE, a vzestupu obohacených komunikačních služeb prostřednictvím IMS. Služby jako VoLTE, ViLTE a videokonference v reálném čase vyžadovaly audio složku, která by mohla poskytovat stereo kvalitu na úrovni 'CD' bez obětování konverzační latence. Tradiční řečové kodeky pro přepojování okruhů byly pro tyto multimediální aplikace nedostatečné. AAC-LD byl standardizován, aby zaplnil tuto mezeru, a poskytl kodek použitelný pro řečový i hudební obsah se zpožděním srovnatelným s tradičními telefonními kodeky, ale s výrazně vyšší zvukovou věrností.

Řešením kompromisu mezi latencí a kvalitou umožnil AAC-LD novou třídu služeb. Umožnil síťovým operátorům a poskytovatelům služeb nabízet prémiové zážitky z hlasových a video hovorů, streamování hudby s interaktivitou a audio s nízkou latencí pro hry a aplikace rozšířené reality přes celulární sítě. Jeho zavedení podpořilo vizi 3GPP o konvergentních službách založených na IP, zajistilo, že audio zážitek držel krok se zlepšováním kvality videa a šířky pásma sítě, a tím zvýšilo celkovou spokojenost uživatelů a umožnilo komerční úspěch pokročilých telefonních služeb.

## Klíčové vlastnosti

- Algoritmické zpoždění přibližně 20 ms, umožňující přirozenou konverzaci
- Vysoká zvuková kvalita podporující plné stereo pásmo až do 20 kHz
- Široká škála podporovaných datových toků od 32 kbps do 64 kbps na kanál
- Založeno na profilu MPEG-4 AAC s posloupností oken specifickou pro nízké zpoždění
- Podporuje různé vzorkovací frekvence (8, 16, 24, 32, 48 kHz) pro flexibilitu
- Zahrnuje Temporal Noise Shaping (TNS) pro kontrolu artefaktů předozvěně

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 26.923** (Rel-19) — Study on IMS-based Telepresence Media Handling

---

📖 **Anglický originál a plná specifikace:** [AAC-LD na 3GPP Explorer](https://3gpp-explorer.com/glossary/aac-ld/)
