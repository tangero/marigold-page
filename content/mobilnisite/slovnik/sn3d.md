---
slug: "sn3d"
url: "/mobilnisite/slovnik/sn3d/"
type: "slovnik"
title: "SN3D – Spherical Harmonics Normalization 3D"
date: 2025-01-01
abbr: "SN3D"
fullName: "Spherical Harmonics Normalization 3D"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sn3d/"
summary: "Spherical Harmonics Normalization 3D (SN3D) je normalizační schéma používané v 3D audio kódování, zejména pro Ambisonics vyššího řádu (HOA). Definuje, jak jsou škálovány bázové funkce sférických harmo"
---

SN3D je normalizační schéma pro 3D audio kódování, které škáluje bázové funkce sférických harmonik, aby zajistilo konzistentní reprezentaci energie, což je klíčové pro přesný prostorový zvuk a interoperabilitu systémů.

## Popis

Spherical Harmonics Normalization 3D (SN3D) je specifická normalizační konvence aplikovaná na funkce sférických harmonik používané v trojrozměrných audio reprezentacích, jako je Ambisonics vyššího řádu ([HOA](/mobilnisite/slovnik/hoa/)). Sférické harmoniky tvoří sadu ortogonálních bázových funkcí definovaných na povrchu koule, používaných k rozkladu zvukového pole na jeho směrové složky. Normalizace je zásadní, protože na tyto matematické funkce lze aplikovat různá škálovací schémata, což ovlivňuje amplitudu a energii každé harmonické složky. SN3D používá schéma, které normalizuje sférické harmoniky tak, aby měly jednotkový výkon na kouli, což znamená, že integrál druhé mocniny každé harmonické přes kouli je roven jedné.

V praktických termínech, v rámci 3GPP audio kodeku, jako jsou Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) nebo specifikace pro imerzivní audio, normalizace SN3D zajišťuje, že ambisonické složky (signály B-formátu) jsou reprezentovány konzistentně. Při snímání, zpracování nebo vykreslování audio obsahu použití SN3D zaručuje, že energie každého koeficientu sférické harmoniky správně odpovídá fyzickému zvukovému poli. To je klíčové pro zachování vnímané hlasitosti a prostorových charakteristik audia, když je dekódováno a přehráno přes reproduktorové pole nebo prostřednictvím binauračního vykreslování pro sluchátka.

Technická implementace zahrnuje aplikaci specifických škálovacích faktorů na přidružené Legendreovy polynomy, které tvoří sférické harmoniky. Tyto faktory jsou definovány matematicky a jsou aplikovány během procesů kódování (analýzy) a dekódování (syntézy). V systému 3GPP, když jsou audio objekty nebo scény kódovány pro přenos, použití SN3D, na rozdíl od jiných normalizací jako je N3D (která zahrnuje kosinovou váhu), zajišťuje interoperabilitu. Dekodéry a vykreslovací systémy, které jsou v souladu se specifikací 3GPP, očekávají koeficienty normalizované pomocí SN3D, což umožňuje přesnou rekonstrukci prostorového audio obrazu bez zavedení chyb zesílení nebo zkreslení prostorových stop.

## K čemu slouží

Normalizace SN3D byla zavedena, aby vyřešila problém nekonzistentních reprezentací prostorového audia mezi různými výrobci, výzkumnými institucemi a nástroji pro tvorbu obsahu. V raném vývoji Ambisonics a 3D audia se používaly různé normalizační konvence (jako SN3D, N3D a Schmidtova semi-normalizace), což vedlo k nekompatibilitě. Audio soubory nebo streamy zakódované jednou konvencí by zněly nesprávně vyváženě nebo prostorově zkresleně při dekódování systémem, který očekává jinou, což bránilo adopci imerzivního audia.

Standardizace SN3D v rámci 3GPP, zejména od Release 15 pro imerzivní média, poskytuje jednotnou základnu. To umožňuje spolehlivou výměnu a přehrávání prostorového audio obsahu v mobilních a streamovacích službách. Řeší omezení předchozích ad-hoc přístupů tím, že zajišťuje, že matematická reprezentace zvukového pole je jednoznačná. To je obzvláště důležité pro nové aplikace, jako je virtuální realita ([VR](/mobilnisite/slovnik/vr/)), rozšířená realita ([AR](/mobilnisite/slovnik/ar/)) a 360stupňové video, kde je přesné prostorové audio klíčové pro imerzi. Tím, že 3GPP v příslušných specifikacích nařizuje SN3D, umožňuje konzistentní ekosystém pro tvorbu, přenos a vykreslování audio zážitků nové generace.

## Klíčové vlastnosti

- Definuje normalizaci s jednotkovým výkonem pro funkce sférických harmonik
- Zajišťuje konzistentní reprezentaci energie napříč audio složkami
- Klíčová pro interoperabilitu v systémech 3D audia a HOA
- Používá se ve specifikacích 3GPP pro imerzivní audio a kodeku EVS
- Poskytuje jednoznačné škálování pro ambisonické signály B-formátu
- Podporuje přesné vykreslování prostorového audia pro aplikace VR/AR

## Související pojmy

- [HOA – Higher Order Ambisonics](/mobilnisite/slovnik/hoa/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TR 26.933** (Rel-19) — Study on Diverse Audio Capturing System

---

📖 **Anglický originál a plná specifikace:** [SN3D na 3GPP Explorer](https://3gpp-explorer.com/glossary/sn3d/)
