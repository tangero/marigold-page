---
slug: "cc-pp"
url: "/mobilnisite/slovnik/cc-pp/"
type: "slovnik"
title: "CC/PP – Composite Capability / Preference Profiles"
date: 2025-01-01
abbr: "CC/PP"
fullName: "Composite Capability / Preference Profiles"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cc-pp/"
summary: "CC/PP je rámec pro popis schopností zařízení a preferencí uživatele využívající RDF. Umožňuje adaptaci obsahu a personalizaci služeb v mobilních sítích tím, že serverům poskytuje informace o charakter"
---

CC/PP je rámec využívající RDF pro popis schopností zařízení a preferencí uživatele, který umožňuje adaptaci obsahu a personalizaci služeb v mobilních sítích.

## Popis

Composite Capability / Preference Profiles ([CC](/mobilnisite/slovnik/cc/)/[PP](/mobilnisite/slovnik/pp/)) je standardizovaný rámec založený na Resource Description Framework ([RDF](/mobilnisite/slovnik/rdf/)) pro reprezentaci a přenos informací o hardwarových a softwarových schopnostech klientského zařízení spolu s uživatelskými preferencemi na obsahový server nebo aplikaci. Poskytuje strukturovanou slovní zásobu pro popis atributů, jako je velikost obrazovky, podporované mediální kodeky, barevná hloubka, vstupní metody a verze prohlížečového softwaru. Hlavní architektonickou rolí CC/PP je fungovat jako mechanismus pro výměnu metadat mezi uživatelským zařízením (UE) a síťovým serverem, nejčastěji [HTTP](/mobilnisite/slovnik/http/) proxy nebo původním serverem, za účelem usnadnění adaptace obsahu.

Při provozu je profil CC/PP typicky uložen na klientském zařízení nebo na něj odkazováno pomocí [URI](/mobilnisite/slovnik/uri/). Když klient zahájí relaci nebo požádá o obsah, je tento profil předán serveru, často v rámci HTTP hlaviček pomocí protokolu pro výměnu CC/PP definovaného ve spojení s [WAP](/mobilnisite/slovnik/wap/). Adaptační engine na straně serveru následně tento [XML](/mobilnisite/slovnik/xml/)/RDF profil zpracuje. Porovná uvedené schopnosti a preference s dostupnými verzemi nebo reprezentacemi požadovaného obsahu (např. obrázek v různých rozlišeních nebo video v různých kódovacích formátech). Na základě tohoto porovnávacího procesu server vybere a případně i překóduje nejvhodnější variantu obsahu pro doručení klientovi.

Klíčovými součástmi rámce CC/PP jsou Model dat profilu, který definuje strukturu informací o schopnostech pomocí RDF schémat, a protokol pro výměnu CC/PP, který specifikuje způsob přenosu těchto profilů přes sítě jako HTTP. Samotný profil se skládá z komponent (např. komponenta 'HardwarePlatform', 'SoftwarePlatform' a 'BrowserUA'), z nichž každá obsahuje sadu atribut-hodnota popisující konkrétní vlastnosti. Kritickým aspektem je použití dvouúrovňové struktury sestávající z profilového diffu a referenčního profilu. Klient může odeslat pouze rozdíly (diff) od známého referenčního profilu uloženého na URI, což významně snižuje objem dat přenášených přes rozhraní vzduchového rozhraní.

V rámci architektury 3GPP je CC/PP nedílnou součástí Transparentní koncové paketové streamovací služby ([PSS](/mobilnisite/slovnik/pss/)) a služby multimediálního vysílání/multicastu (MBMS). Umožňuje serveru a klientovi PSS vyjednat mediální formáty, čímž zajišťuje efektivní využití rádiových prostředků a poskytuje uživatelský zážitek přizpůsobený zobrazovacím a výpočetním schopnostem zařízení. Jeho role se rozšiřuje i na IP Multimedia Subsystem (IMS) pro personalizaci služeb, což z něj činí základní prvek pro poskytování adaptabilních multimediálních služeb v heterogenním ekosystému zařízení.

## K čemu slouží

CC/PP bylo vytvořeno, aby řešilo základní problém přístupu 'jedna velikost pro všechny' při doručování webového a multimediálního obsahu, který se stal neudržitelným s explozí různorodých mobilních zařízení na počátku 21. století. Před jeho standardizací měly servery omezené nebo ad-hoc metody (jako parsování řetězce User-Agent) pro odvození schopností klienta, což vedlo ke špatným uživatelským zkušenostem, plýtvání šířkou pásma odesíláním nepodporovaného obsahu a zvýšené spotřebě energie zařízení zpracováním nevhodných mediálních formátů. Omezení předchozích přístupů zahrnovala nedostatek strukturované, rozšiřitelné a standardizované slovní zásoby pro komplexní popis vlastností zařízení a uživatelských voleb.

Historický kontext vývoje CC/PP úzce souvisí s fórem Wireless Application Protocol (WAP) a jeho sloučením do Open Mobile Alliance (OMA). Byl motivován potřebou efektivní adaptace obsahu v mobilních sítích s omezenou šířkou pásma (2.5G a 3G) za účelem zlepšení dostupnosti a kvality služeb. Poskytnutím robustního, XML-based popisného rámce CC/PP vyřešilo problém umožnění síťovým serverům a proxy činit informovaná, automatizovaná rozhodnutí o transformaci, výběru a doručování obsahu, čímž optimalizovalo koncovou službu jak pro síťového operátora, tak pro účastníka.

Dále CC/PP položilo základy pro sofistikovanější personalizaci služeb a správu zařízení. Vyřešilo problém škálovatelného nasazení služeb na fragmentovaném trhu zařízení zavedením standardního rozhraní pro zjišťování schopností. To umožnilo poskytovatelům obsahu a mobilním operátorům vytvořit adaptační logiku jednou, na základě standardu CC/PP, namísto udržování databází specifických pro jednotlivá zařízení, čímž se snížila složitost a urychlilo se zavádění bohatých multimediálních služeb, jako je streamování videa a mobilní prohlížení, na širokou škálu přístrojů.

## Klíčové vlastnosti

- Standardizované RDF-based schéma pro popis hardwarových, softwarových a prohlížečových schopností zařízení
- Podporuje efektivní přenos pomocí profilových diffů odkazujících na základní profil uložený na URI
- Umožňuje adaptaci obsahu na straně serveru, vyjednávání a výběr mediálních formátů
- Integruje se s HTTP pro výměnu profilů mezi klientem a serverem
- Poskytuje základ pro popis uživatelských preferencí pro personalizaci služeb
- Usnadňuje optimalizaci šířky pásma tím, že zabraňuje doručování nepodporovaných formátů obsahu

## Související pojmy

- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification

---

📖 **Anglický originál a plná specifikace:** [CC/PP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cc-pp/)
