---
slug: "pmt"
url: "/mobilnisite/slovnik/pmt/"
type: "slovnik"
title: "PMT – Program Map Table"
date: 2025-01-01
abbr: "PMT"
fullName: "Program Map Table"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pmt/"
summary: "Program Map Table (PMT) je základní datová struktura v rámci transportního toku (TS) MPEG-2 používaná pro digitální televizi a multimediální vysílání. Funguje jako adresář, který uvádí všechny element"
---

PMT (Program Map Table) je tabulka mapování programu, což je adresář v transportním toku MPEG-2, který obsahuje seznam elementárních proudů a jejich identifikátorů paketů (PID) pro konkrétní program. Je klíčová pro doručování služeb 3GPP MBMS/eMBMS.

## Popis

Program Map Table (PMT) je kritická součást specifikace [MPEG-2](/mobilnisite/slovnik/mpeg-2/) Systems ([ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 13818-1), která definuje formát transportního toku (TS) pro multiplexování digitálního videa, audia a dat. Transportní tok je navržen pro přenos více programů (např. různých [TV](/mobilnisite/slovnik/tv/) kanálů) jedním přenosovým kanálem. Každý program se skládá z jednoho nebo více elementárních proudů – například video proudu kódovaného pomocí H.264, více audio proudů v různých jazycích a pomocných datových proudů pro titulky nebo teletext. PMT je základní tabulka, která poskytuje „mapu“ pro jednotlivý program a říká dekodéru, které elementární proudy tento program tvoří a jak je najít v rámci širšího transportního toku.

Strukturálně je PMT speciální sekcí dat, která je sama přenášena v paketech transportního toku a je identifikována jedinečným identifikátorem paketu ([PID](/mobilnisite/slovnik/pid/)). Každý program v rámci transportního toku má svou vlastní PMT. PMT obsahuje hlavičku s informacemi, jako je číslo programu (jednoznačný identifikátor programu) a PID proudu Program Clock Reference (PCR) používaného pro synchronizaci audia a videa. Jádrem PMT je smyčka popisující každý elementární proud náležící k programu. Pro každý elementární proud záznam v PMT specifikuje typ proudu (např. 0x1B pro H.264 video, 0x0F pro [AAC](/mobilnisite/slovnik/aac/) audio), hodnotu PID paketů transportního toku, které nesou data tohoto elementárního proudu, a volitelné deskriptory poskytující dodatečné informace, jako je jazyk pro audio proudy nebo poměr stran pro video.

Proces funguje následovně: Přijímač naladěný na konkrétní program nejprve získá Program Association Table ([PAT](/mobilnisite/slovnik/pat/)), která je vždy na pevném, známém PID (PID 0). PAT obsahuje seznam čísel programů a jim odpovídajících PID pro PMT každého programu. Přijímač poté přečte PMT pro požadované číslo programu. Pomocí PMT přijímač zjistí PIDy pro video, audio a další komponentní proudy. Demultiplexor následně filtruje příchozí transportní tok a vybírá pouze pakety s těmito konkrétními PIDy, které předává příslušným video, audio nebo datovým dekodérům. To umožňuje rekonstrukci synchronizovaného multimediálního programu.

V kontextu 3GPP je PMT zásadní pro vysílací/multicastové služby jako Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a její rozšířená verze eMBMS (nyní součást 5G Broadcast). 3GPP TS 26.917 specifikuje použití transportního toku MPEG-2 pro doručování služeb MBMS přes mobilní sítě. Zde PMT definuje složení každé služby MBMS (např. mobilního TV kanálu). BM-SC (Broadcast Multicast Service Centre) generuje transportní tok obsahující PMT a elementární proudy. Informace z PMT jsou pak využívány síťovými prvky s podporou eMBMS a nakonec i uživatelským zařízením (UE) pro správnou identifikaci, demultiplexování a dekódování vysílané služby. PMT zajišťuje, že mobilní zařízení může bezproblémově připojit k vysílací relaci a správně složit audio a video komponenty, čímž poskytuje standardizovanou a interoperabilní metodu pro doručování bohatého multimediálního obsahu více uživatelům současně.

## K čemu slouží

Program Map Table byla vytvořena k řešení základního problému multiplexování více digitálních televizních programů a jejich příslušných audio, video a datových proudů do jediného, spojitého přenosového bitového toku (transportní tok MPEG-2). Před takovým systémem by doručování více kanálů a jejich přidružených komponent vyžadovalo samostatné, vyhrazené kanály nebo složité proprietární multiplexní schémy. PMT poskytuje standardizovaný, flexibilní a efektivní „obsah“ pro program v rámci multiplexu. Jejím účelem je umožnit přijímačům rychle a přesně identifikovat všechny části vybraného programu z moře multiplexovaných datových paketů, což je zásadní pro přepínání kanálů, výběr služeb a spolehlivé dekódování.

V konkrétním kontextu adopce 3GPP pro MBMS/eMBMS bylo účelem použití PMT a frameworku transportního toku MPEG-2 využít zralý, široce známý a robustní standard pro vysílání multimediálního obsahu. Mobilní sítě potřebovaly metodu pro efektivní doručování stejného obsahu (jako živé TV nebo aktualizace softwaru) tisícům zařízení současně. Adopcí MPEG-2 TS a jeho PMT mohlo 3GPP znovu využít stávající odborné znalosti, komerční enkodéry a dekodérové čipsety, čímž urychlilo nasazení mobilních vysílacích služeb. Poskytlo dobře definovanou strukturu, která zaručila interoperabilitu mezi poskytovateli obsahu, síťovým vybavením a telefony od různých výrobců.

Navíc je struktura PMT rozšiřitelná pomocí deskriptorů, což jí umožňuje přenášet metadata zásadní pro moderní služby. To zahrnuje informace pro správu digitálních práv (DRM), průvodce službami (Electronic Service Guide – ESG) a podmíněný přístup. Pro mobilní vysílání byla tato rozšiřitelnost klíčová. Umožnila BM-SC vložit informace o charakteristikách služby, jazycích a věkových hodnocení přímo do PMT, což umožnilo UE prezentovat bohaté uživatelské rozhraní pro objevování a výběr služeb. PMT tedy neslouží pouze jako technická mapa pro demultiplexování, ale také jako nosič metadat souvisejících se službou, což z ní činí základní kámen pro škálovatelné, funkčně bohaté vysílací služby v celulárních sítích.

## Klíčové vlastnosti

- Poskytuje mapování mezi číslem programu a identifikátory paketů (PID) jeho komponentních elementárních proudů
- Specifikuje typ proudu (např. H.264 video, AAC audio) pro každý elementární proud v rámci programu
- Nese PID proudu Program Clock Reference (PCR) pro synchronizaci audia a videa
- Obsahuje smyčky deskriptorů pro přenos dodatečných metadat (např. jazyk, poměr stran, podmíněný přístup)
- Zásadní pro demultiplexování transportních toků MPEG-2 ve vysílacích systémech jako DVB, ATSC a 3GPP MBMS
- Umožňuje přijímačům dynamicky identifikovat a dekódovat vybrané služby z multiplexu mnoha programů

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [PMT na 3GPP Explorer](https://3gpp-explorer.com/glossary/pmt/)
