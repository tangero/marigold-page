---
slug: "ngeo"
url: "/mobilnisite/slovnik/ngeo/"
type: "slovnik"
title: "NGEO – Non-Geostationary Earth Orbiting"
date: 2025-01-01
abbr: "NGEO"
fullName: "Non-Geostationary Earth Orbiting"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ngeo/"
summary: "Označuje satelitní systémy na negeostacionárních drahách, jako je nízká oběžná dráha (LEO). Standardy 3GPP se vyvíjejí, aby tyto satelity integrovaly jako přístupové uzly 5G NTN, což poskytuje globáln"
---

NGEO je 3GPP termín pro satelitní systémy na negeostacionárních drahách, jako je LEO, které jsou integrovány jako přístupové uzly v 5G NTN pro poskytnutí globálního pokrytí.

## Popis

NGEO (Non-Geostationary Earth Orbiting) v kontextu 3GPP označuje integraci satelitních komunikačních systémů, které operují na jiných drahách než geostacionární oběžná dráha ([GEO](/mobilnisite/slovnik/geo/)), do ekosystému 5G. Jedná se především o satelity na nízké oběžné dráze ([LEO](/mobilnisite/slovnik/leo/)) a střední oběžné dráze ([MEO](/mobilnisite/slovnik/meo/)). Na rozdíl od GEO satelitů ve výšce cca 36 000 km, které se jeví jako stacionární, se NGEO satelity pohybují vůči zemskému povrchu, což vytváří dynamickou topologii sítě s předáváním spojení mezi satelity a pozemními bránami. 3GPP od verze Release 16 standardizuje, jak mohou tyto satelity fungovat jako přístupové uzly v 5G Neterestriální síti ([NTN](/mobilnisite/slovnik/ntn/)), a zajišťovat tak bezproblémovou integraci s pozemními sítěmi.

Technický provoz NTN založené na NGEO vyžaduje několik specifických úprav standardního rádiového protokolového zásobníku 5G. Klíčovou výzvou je extrémně dlouhá doba šíření (desítky milisekund pro LEO, oproti <1 ms v pozemních sítích) a vysoký Dopplerův posun způsobený pohybem satelitu. Specifikace 3GPP (např. TS 38.101, TS 38.821) definují úpravy fyzické vrstvy pro kompenzaci těchto efektů. To zahrnuje vylepšené mechanismy časového předstihu, modifikované procedury náhodného přístupu a specifický návrh referenčních signálů. Architektura typicky zahrnuje satelit (často fungující jako 'průchozí' nebo transparentní přenosový modul), který přeposílá signály mezi uživatelským zařízením (UE) na zemi a pozemní bránou, která je připojena k 5G Core síti. Brána spravuje připojení k jádru sítě a řeší funkce jako správu mobility mezi pohyblivými satelitními paprsky.

Klíčové komponenty systému NGEO NTN zahrnují konstelaci NGEO satelitů (např. LEO nebo MEO), UE s modemem podporujícím satelitní komunikaci (který může být vylepšen pro vyšší výkon nebo citlivost), pozemní bránové stanice (GWS) s propojovacími spoji k satelitům a 5G Core síť. Servisní spojení je mezi satelitem a UE, zatímco propojovací spoj spojuje satelit s bránou. Úloha NGEO v síti 5G spočívá v rozšíření pokrytí do odlehlých, námořních a leteckých oblastí, kde je pozemní nasazení ekonomicky nebo fyzicky nemožné. Poskytuje kontinuitu služeb pro pohyblivé platformy jako letadla a lodě a podporuje hromadná nasazení IoT v zemědělství, logistice a monitorování životního prostředí po celém světě. Dále zvyšuje odolnost sítě tím, že poskytuje záložní konektivitu při výpadcích pozemní sítě způsobených katastrofami.

## K čemu slouží

Účelem standardizace satelitního přístupu NGEO v 3GPP je naplnit vizi 5G o poskytnutí konektivity všude a pro všechno. Tradiční pozemní sítě mají zásadní omezení v pokrytí, což zanechává rozsáhlé geografické oblasti (oceány, pouště, polární regiony) nepokryté. [GEO](/mobilnisite/slovnik/geo/) satelity sice pokrytí poskytují, ale často s vysokou latencí a omezenou kapacitou, což je činí nevhodnými pro interaktivní služby 5G. Vznik mega-konstelací [LEO](/mobilnisite/slovnik/leo/) satelitů (např. Starlink, OneWeb) vytvořil novou příležitost pro globální pokrytí s nízkou latencí a vysokou propustností, ale vyžadoval standardizaci pro bezproblémovou integraci s všudypřítomným ekosystémem 5G.

NGEO [NTN](/mobilnisite/slovnik/ntn/) řeší několik kritických problémů. Za prvé řeší mezeru v pokrytí a umožňuje skutečně globální službu 5G pro širokopásmové připojení, IoT a komunikace zásadní důležitosti. Za druhé poskytuje konektivitu pohyblivým platformám, kde je nepřetržité předávání mezi pozemními buňkami nemožné, jako je komerční letectví a globální námořní doprava. Za třetí zvyšuje odolnost sítě tím, že poskytuje neterestriální záložní vrstvu, což je klíčové pro scénáře veřejné bezpečnosti a obnovy po katastrofách, kdy může být pozemní infrastruktura narušena.

Historický kontext představuje konvergence satelitní a pozemní komunikace. Dříve byly satelitní sítě proprietární a izolované. Práce 3GPP, započatá studijními položkami v Release 16 zdokumentovanými v TR 38.821, měla za cíl tyto bariéry odstranit. Řeší omezení předchozích neintegrovaných přístupů definováním toho, jak může UE použít jediný protokolový zásobník pro připojení k pozemnímu gNB nebo satelitnímu uzlu, spravovanému stejným 5G Core. To motivuje vytvoření jednotné globální sítě, kde služba následuje uživatele bez ohledu na jeho polohu a využívá nejlepší dostupnou přístupovou technologii – pozemní nebo neterestriální.

## Klíčové vlastnosti

- Integrace konstelací LEO a MEO satelitů jako přístupových uzlů 5G NTN
- Standardizované úpravy pro dlouhé doby šíření a vysoký Dopplerův posun v rádiových protokolech
- Podpora jak průchozích (bent-pipe), tak regenerativních (s palubním zpracováním) satelitních přenosových modulů
- Umožňuje bezproblémovou kontinuitu služeb pro uživatele v letecké a námořní mobilitě
- Poskytuje globální pokrytí pro hromadné IoT, širokopásmové připojení a služby v mimořádných situacích
- Zvyšuje odolnost sítě tím, že slouží jako záloha pro pozemní infrastrukturu

## Související pojmy

- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)
- [LEO – Low-Earth Orbiting satellites](/mobilnisite/slovnik/leo/)
- [GEO – Geostationary satellite Earth Orbit](/mobilnisite/slovnik/geo/)
- [TN – Terrestrial Network](/mobilnisite/slovnik/tn/)

## Definující specifikace

- **TR 36.763** (Rel-17) — NB-IoT/eMTC Support for Non-Terrestrial Networks
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.821** (Rel-16) — NR Support for Non-Terrestrial Networks
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec

---

📖 **Anglický originál a plná specifikace:** [NGEO na 3GPP Explorer](https://3gpp-explorer.com/glossary/ngeo/)
