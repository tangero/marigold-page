---
slug: "lstr"
url: "/mobilnisite/slovnik/lstr/"
type: "slovnik"
title: "LSTR – Listener SideTone Rating"
date: 2025-01-01
abbr: "LSTR"
fullName: "Listener SideTone Rating"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/lstr/"
summary: "LSTR je subjektivní metrika kvality zvuku používaná k hodnocení výkonu bočního tónu (side-tone) v telefonních koncových zařízeních. Boční tón je záměrný únik vlastního hlasu mluvčího zpět do jeho sluc"
---

LSTR je subjektivní metrika kvality zvuku, která hodnotí, jak přirozeně a komfortně zní záměrný únik vlastního hlasu mluvčího zpět do jeho sluchátka, což ovlivňuje vnímanou kvalitu hovoru.

## Popis

Listener SideTone Rating (LSTR) je standardizovaná metodologie subjektivního testování definovaná ve specifikacích 3GPP, jako jsou TS 26.131 a TS 26.132, pro hodnocení akustických charakteristik bočního tónu u terminálů pro hlasovou komunikaci, včetně mobilních telefonů, sluchátek a pevných telefonních přístrojů. Boční tón označuje jev, kdy část vlastního hlasového signálu mluvčího, snímaného mikrofonem zařízení, je řízeně přiváděna zpět do jeho vlastního přijímače (sluchátka nebo náhlavní soupravy). Tato akustická zpětná vazba napodobuje přirozený zvuk vlastního hlasu slyšený při běžném rozhovoru (způsobený kostním a vzdušným vedením) a její správná implementace je klíčová pro přirozený a komfortní konverzační zážitek. LSTR poskytuje kvantitativní měřítko této percepční kvality.

Proces testování LSTR zahrnuje řízené laboratorní experimenty s lidskými subjekty (posluchači). V typickém testovacím uspořádání subjekt používá testovaný terminál v simulovaném konverzačním scénáři, často v akusticky izolované kabině. Subjekt vyslovuje předdefinovaný řečový materiál a zároveň poslouchá boční tón produkovaný terminálem. Subjekt poté ohodnotí vnímanou kvalitu bočního tónu na standardizované stupnici názorů, jako je například stupnice absolutního kategoriálního hodnocení ([ACR](/mobilnisite/slovnik/acr/)) v rozsahu od 1 (špatné) do 5 (vynikající). Mezi klíčové hodnocené parametry patří hlasitost bočního tónu (neměl by být příliš tichý ani hlasitý), jeho spektrální vyváženost (měla by odpovídat přirozenému zvuku hlasu) a absence nežádoucích artefaktů, jako je zkreslení, zpoždění nebo nadměrný šum. Testy se opakují s více subjekty a terminály, aby bylo možné získat statisticky významné střední hodnotící skóre ([MOS](/mobilnisite/slovnik/mos/)) specificky pro boční tón, což je hodnota LSTR.

Z architektonického hlediska LSTR není síťovou funkcí, ale metrikou zajištění kvality, která ovlivňuje návrh terminálů a plánování sítě. Interaguje s akustickým návrhem terminálu, včetně citlivosti mikrofonu, výstupu přijímače a algoritmů digitálního zpracování signálu ([DSP](/mobilnisite/slovnik/dsp/)), které aplikují zesílení a filtraci na dráhu bočního tónu. Úloha LSTR v širším ekosystému 3GPP spočívá v zajištění základní úrovně uživatelského zážitku u hlasových služeb. Špatný výkon bočního tónu může vést k tomu, že uživatelé mluví příliš hlasitě nebo tiše, což způsobuje nepohodlí a únavu a degraduje celkovou kvalitu konverzace. Standardizací metody měření umožňuje 3GPP výrobcům navrhovat terminály splňující kvalitativní standardy a operátorům ověřovat výkon terminálů při jejich pořizování a auditech kvality sítě, čímž zajišťuje konzistentní kvalitu hlasových služeb napříč různými zařízeními.

## K čemu slouží

LSTR byl vytvořen, aby řešil subtilní, ale kritický aspekt kvality telefonie: uživatelovo vnímání vlastního hlasu během hovoru. V raných telefonních systémech se boční tón přirozeně vyskytoval kvůli analogovému propojení, ale jeho úroveň byla často nekontrolovaná a mohla být nadměrná (což vedlo uživatele ke snižování hlasu) nebo nedostatečná (což vedlo uživatele ke křiku). Jak se terminály stávaly sofistikovanějšími s digitálním zpracováním signálu, získali konstruktéři možnost přesně řídit dráhu bočního tónu. Bez standardizovaného způsobu měření percepční kvality tohoto řízeného bočního tónu se však uživatelský zážitek mezi zařízeními značně lišil, což vedlo k nespokojenosti.

Zavedení LSTR ve verzi Release 5 poskytlo společnou, opakovatelnou metodologii pro subjektivní hodnocení bočního tónu, čímž vyřešilo problém nekonzistentních a subjektivních hodnocení ze strany výrobců. Bylo motivováno potřebou udržet vysokou kvalitu hlasu, když se mobilní telefonie stala mainstreamovou, a když nové formáty zařízení (jako malé skládací telefony nebo rané Bluetooth sluchátka) přinesly nové akustické výzvy. Definováním konkrétního testovacího postupu a hodnotící stupnice umožnilo LSTR objektivní srovnání různých konstrukcí terminálů a podpořilo zlepšování v oblasti akustického inženýrství.

Dále LSTR podporuje širší cíl komplexního řízení kvality hlasu v sítích 3GPP. Zatímco síťové metriky, jako je ztráta paketů a zpoždění, jsou důležité, akustický výkon terminálu je posledním článkem řetězce, který uživatel zažívá. Standardizované metriky jako LSTR spolu s dalšími subjektivními testy (např. pro hlasitost, hluk na pozadí) zajišťují, že terminály se nestanou úzkým hrdlem pro kvalitu. To je obzvláště důležité pro regulační shodu (např. kompatibilitu s naslouchacími pomůckami) a pro služby jako Voice over LTE (VoLTE) a Voice over NR (VoNR), kde vysoce kvalitní hlasové kodeky mohou odhalit špatný akustický návrh, pokud není boční tón správně přizpůsoben rozšířenému audio pásmu.

## Klíčové vlastnosti

- Metodologie subjektivního testování využívající lidské posluchače k hodnocení kvality bočního tónu na standardizované stupnici (např. MOS)
- Hodnotí klíčové percepční atributy: hlasitost, spektrální vyváženost a absenci zkreslení v signálu bočního tónu
- Definováno ve specifikacích 3GPP pro akustické testování terminálů (TS 26.131, TS 26.132)
- Prováděno v řízených akustických prostředích (anechoické nebo hemi-anechoické komory) pro zajištění opakovatelnosti
- Poskytuje kvantitativní metriku (skóre LSTR) pro porovnání výkonu různých telefonních terminálů
- Podporuje zajištění kvality hlasových služeb, včetně tradičních mobilních hovorů, VoLTE a VoNR

## Související pojmy

- [MOS – Mean Opinion Score](/mobilnisite/slovnik/mos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 43.050** (Rel-19) — GSM Transmission Planning for Speech Services

---

📖 **Anglický originál a plná specifikace:** [LSTR na 3GPP Explorer](https://3gpp-explorer.com/glossary/lstr/)
