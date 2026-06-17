---
slug: "mvc"
url: "/mobilnisite/slovnik/mvc/"
type: "slovnik"
title: "MVC – Multi-view Video Coding"
date: 2025-01-01
abbr: "MVC"
fullName: "Multi-view Video Coding"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mvc/"
summary: "Multi-view Video Coding (MVC) je rozšíření standardu H.264/AVC pro efektivní kompresi videa z více kamer. Tvoří základ pro poskytování služeb 3D videa v mobilních sítích, umožňuje stereoskopické 3D př"
---

MVC je rozšíření standardu H.264/AVC pro efektivní kompresi videa z více kamer, které umožňuje služby 3D videa jako stereoskopické přehrávání a interaktivní výběr úhlu pohledu v mobilních sítích.

## Popis

Multi-view Video Coding (MVC) je standard pro kompresi videa vyvinutý jako dodatek k H.264/Advanced Video Coding ([AVC](/mobilnisite/slovnik/avc/)). Jeho hlavní funkcí je kódování video sekvencí snímáných současně z více kamer uspořádaných tak, aby pokryly stejnou scénu z různých úhlů. Základním technickým přístupem je hierarchická predikce B-snímků rozšířená napříč časem (v rámci jednoho pohledu) i pohledem (napříč různými perspektivami kamer). Tím vzniká predikční struktura maximalizující kompresi využitím již zakódovaných snímků z jiných pohledů jako referencí, vedle minulých a budoucích snímků ve stejném pohledu.

Architektura kodeku MVC určuje jeden pohled jako základní, který je kódován kompatibilně s profilem H.264/AVC High Profile, což zajišťuje, že jakýkoli dekodér AVC dokáže tento pohled dekódovat pro 2D přehrávání. Další pomocné pohledy jsou kódovány pomocí meziplehlové predikce. Klíčové kódovací nástroje zahrnují predikci s kompenzací pohybu pro časovou redundanci a predikci s kompenzací disparity pro prostorovou redundanci mezi pohledy. Enkodér generuje jediný datový tok obsahující všechny pohledy, prokládané podle predikční hierarchie. Datový tok obsahuje jednotky síťové abstrakční vrstvy ([NAL](/mobilnisite/slovnik/nal/)) s novými typy pro identifikaci komponent pohledu a správu pořadí dekódování.

V rámci ekosystémů 3GPP byl MVC specifikován pro použití v paketové streamovací službě (PSS) a multimediální vysílací/multicastové službě ([MBMS](/mobilnisite/slovnik/mbms/)) pro distribuci obsahu 3D videa. Síťová služba doručí MVC datový tok a kompatibilní klient (např. mobilní telefon s 3D displejem) dekóduje alespoň dva pohledy pro vykreslení stereoskopického obrazu. Specifikace 3GPP definují profily a úrovně pro MVC, jeho přenos v [MPEG-2](/mobilnisite/slovnik/mpeg-2/) Transport Streams nebo [ISO](/mobilnisite/slovnik/iso/) Base Media File Format a signalizaci v popisu relace nebo popisu mediální prezentace. Jeho úlohou bylo poskytnout standardizovanou, efektivní metodu pro distribuci 3D videa, která tvořila základ pro rané služby mobilní 3D televize.

## K čemu slouží

MVC byl vytvořen pro umožnění praktických služeb 3D videa, které vyžadují alespoň dva pohledy (pro levé a pravé oko), v době, kdy přenos dvou nezávislých [AVC](/mobilnisite/slovnik/avc/) datových toků by zdvojnásobil požadavky na šířku pásma. Hlavní problém, který řešil, byla vysoká datová náročnost videa z více pohledů, což byla zásadní překážka pro nasazení 3DTV a dalších imerzivních služeb v kanálech s omezenou kapacitou, jako jsou mobilní sítě.

Historický kontext představuje vzestup 3D kina a počáteční snahy o 3D televizi na konci let 2000. 3GPP začal začleňovat podporu pokročilých video služeb přibližně od Release 9. MVC, standardizovaný dříve organizací [MPEG](/mobilnisite/slovnik/mpeg/), byl do 3GPP přijat, aby poskytl technicky robustní řešení. Vyřešil omezení simultánního vysílání (nezávislé datové toky) tím, že poskytl typicky 20–50% úsporu datového toku pro stereoskopický obsah se dvěma pohledy, čímž se mobilní vysílání a streamování 3D videa stalo komerčně a technicky životaschopným. Položil základy pro veškerou následnou práci na kódování více pohledů v 3GPP, včetně pozdějšího standardu [MV-HEVC](/mobilnisite/slovnik/mv-hevc/).

## Klíčové vlastnosti

- Efektivní komprese pro stereoskopické (dvoupohledové) a vícepohledové video sekvence
- Zpětná kompatibilita: základní pohled lze dekódovat standardními dekodéry H.264/AVC
- Využívá hierarchické B-snímky a predikci s kompenzací disparity napříč pohledy
- Definované profily a úrovně pro interoperabilitu v službách 3GPP
- Podpora interaktivního přepínání pohledů v aplikacích s volným úhlem pohledu
- Specifikován přenos v mediálních formátech 3GPP pro streamování a vysílání

## Související pojmy

- [MV-HEVC – MultiView High Efficiency Video Coding](/mobilnisite/slovnik/mv-hevc/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework
- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS
- **TR 26.905** (Rel-19) — Study on Mobile 3D Video Services

---

📖 **Anglický originál a plná specifikace:** [MVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mvc/)
