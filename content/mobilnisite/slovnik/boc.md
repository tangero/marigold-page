---
slug: "boc"
url: "/mobilnisite/slovnik/boc/"
type: "slovnik"
title: "BOC – Bell Operating Company"
date: 2025-01-01
abbr: "BOC"
fullName: "Bell Operating Company"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/boc/"
summary: "Bell Operating Company (BOC) označuje místní telefonní společnosti vzniklé po rozdělení AT&T v roce 1984. V kontextu 3GPP se jedná o zastaralý termín používaný v raných specifikacích k popisu určitých"
---

BOC je zastaralý termín z raných specifikací 3GPP popisující místní telefonní společnosti vzniklé po rozdělení AT&T, používaný pro určité poskytovatele služeb a jejich okruhově přepínané domény.

## Popis

V rámci specifikací 3GPP je termín Bell Operating Company (BOC) historickým odkazem na specifický typ poskytovatele telekomunikačních služeb. Pochází z regulačního prostředí ve Spojených státech po rozdělení monopolu AT&T v roce 1984, které vedlo ke vzniku několika nezávislých regionálních společností (RBOC). Ve specifikacích 3GPP, zejména v raných verzích jako Rel-4, byl tento termín používán k označení administrativní a operační domény takového místního přepínače. Tato doména byla relevantní pro definování hranic služeb, fakturačních vztahů a bodů propojení pro tradiční telefonní služby, které byly integrovány do raných mobilních sítí nebo s nimi rozhraní.

Technická role BOC v architektuře 3GPP se primárně týkala okruhově přepínané jádrové sítě, konkrétně Mobilní ústředny ([MSC](/mobilnisite/slovnik/msc/)) a její interakce s telefonní veřejnou komutovanou sítí (PSTN). BOC představovala operátora PSTN, na kterého mohlo být volání mobilního účastníka směrováno nebo od kterého mohlo volání pocházet. MSC by zpracovávala řízení a směrování hovorů, případně komunikovala s ústřednami BOC pomocí signalizačních protokolů jako [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part). Specifikace odkazující na BOC (jako 22.060) používaly tento termín k definování požadavků na služby a síťových scénářů zahrnujících propojení pevné a mobilní sítě.

Architektonicky byla BOC externí entitou vůči 3GPP definované veřejné pozemní mobilní síti (PLMN). Byla součástí širšího telekomunikačního ekosystému, se kterým PLMN potřebovala interoperabilitu. Rozhraní mezi PLMN (přes Gateway MSC neboli [GMSC](/mobilnisite/slovnik/gmsc/)) a sítí BOC bylo kritickým bodem pro doručování hovorů, překlad čísel a interakci služeb. Ačkoli samotný termín nepopisuje protokol nebo síťový uzel v rámci 3GPP, definuje smluvní a operační hranici, která ovlivňovala požadavky na číslování, adresování, směrování a účtování.

V pozdějších verzích 3GPP explicitní použití termínu 'Bell Operating Company' ustoupilo, protože specifikace se staly obecnějšími a mezinárodně zaměřenými. Koncept se vyvinul ve standardizovanější termíny jako 'PSTN/ISDN síť', 'pevná síť' nebo prostě 'externí síť'. Funkční požadavky původně spojené s propojením BOC byly absorbovány do širších specifikací pro síťovou spolupráci a roaming, což učinilo specifickou terminologii BOC v technických popisech síťové architektury do značné míry zastaralou, i když zůstává jako historický artefakt v některých názvech a oblastech dokumentů.

## K čemu slouží

Zařazení termínu Bell Operating Company do raných specifikací 3GPP mělo specifický účel: poskytnout konkrétní reálný referenční bod pro definování požadavků souvisejících s propojením pevné a mobilní sítě. Během vývoje systémů 2G a raného 3G byl hlavním případem užití mobilní telefonie spojení s existující rozsáhlou telefonní sítí pevných linek. V severoamerickém kontextu tuto síť z velké části provozovaly společnosti BOC. Specifikace požadavků pro scénáře zahrnující BOC tedy zajišťovala, že návrhy systémů 3GPP mohly bezproblémově spolupracovat s tímto dominantním segmentem globální telekomunikační infrastruktury.

Termín řešil problém definování jasných hranic služeb a administrativních odpovědností. Pomáhal specifikovat, který síťový subjekt (PLMN nebo BOC) byl odpovědný za funkce jako směrování hovorů, účtování a poskytování služeb účastníkovi v bodě propojení. To bylo klíčové pro vyúčtování mezi operátory, zákonný odposlech a zajištění kvality služeb přes síťové hranice. Použití dobře známého průmyslového termínu jako BOC poskytlo inženýrům navrhujícím rozhraní a protokoly pro Gateway [MSC](/mobilnisite/slovnik/msc/) okamžitý kontext.

Historicky to odráželo přechodné období, kdy mobilní sítě nebyly samostatnými systémy, ale rozšířeními stávajících pevných sítí a potřebovaly se s nimi hluboce integrovat. Omezení předchozích, více proprietárních mobilních systémů spočívala v jejich často úzkých nebo dodavatelsky specifických možnostech spolupráce. Formálním odkazem na entity jako BOC chtělo 3GPP vytvořit standardizované, robustní modely propojení, které by fungovaly globálně, i když konkrétní termín byl regionálně odvozený. Jak se průmysl posunul k plně IP jádrovým sítím a operační prostředí se vyvíjelo s novými typy poskytovatelů služeb, potřeba tohoto specifického zastaralého termínu odezněla a jeho účel byl naplněn obecnějšími a technologicky neutrálními síťovými definicemi.

## Klíčové vlastnosti

- Definovala externí doménu operátora PSTN pro propojení
- Poskytovala model pro směrování hovorů a hranice služeb mezi pevnou a mobilní sítí
- Ovlivňovala požadavky na číslování a adresování (čísla E.164) na síťových hranicích
- Stanovila kontext pro účtování a vyúčtování mezi síťovými operátory
- Sloužila jako referenční bod pro regulační a servisní scénáře v raných specifikacích
- Představovala zastaralou administrativní hranici v telekomunikacích

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description

---

📖 **Anglický originál a plná specifikace:** [BOC na 3GPP Explorer](https://3gpp-explorer.com/glossary/boc/)
