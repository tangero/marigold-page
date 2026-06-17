---
slug: "flo"
url: "/mobilnisite/slovnik/flo/"
type: "slovnik"
title: "FLO – Flexible Layer One"
date: 2025-01-01
abbr: "FLO"
fullName: "Flexible Layer One"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/flo/"
summary: "Flexible Layer One (FLO) je koncept architektury fyzické vrstvy GSM/EDGE, který odděluje zpracovací řetězec transportního kanálu od specifických hlasových kodeků. Umožňuje dynamické mapování více typů"
---

FLO je architektura fyzické vrstvy GSM/EDGE, která odděluje zpracování transportního kanálu od konkrétních hlasových kodeků, což umožňuje dynamické mapování více datových typů na fyzické kanály pro efektivnější využití rádiových zdrojů.

## Popis

Flexible Layer One (FLO) je zásadní architektonické vylepšení fyzické vrstvy GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), specifikované v řadě technických specifikací 3GPP včetně TS 45.902. Jeho klíčovou inovací je oddělení zpracování transportního kanálu od pevných, na řeč orientovaných kanálových struktur. V tradičním GSM byl zpracovací řetězec fyzické vrstvy těsně integrován s výstupem hlasového kodeku Full-Rate ([FR](/mobilnisite/slovnik/fr/)) nebo Half-Rate ([HR](/mobilnisite/slovnik/hr/)), což vytvářelo pevné mapování. FLO zavádí obecnější a flexibilnější zpracovací řetězec, který dokáže pojmout různé typy transportních kanálů – přenášejících nejen kódovanou řeč, ale i data přepojovaná okruhy (např. pro fax) a, což je nejdůležitější, paketový provoz pro Enhanced Data rates for GSM Evolution (EDGE).

Jak to funguje: FLO předefinovává stupně mezi výstupem kodeku (nebo zdroje dat) a vstupem do modulátoru. Namísto pevné cesty definuje sadu konfigurovatelných funkcí: segmentaci, přidání koncových bitů, kanálové kódování (konvoluční nebo turbokódování), prokládání a mapování na blesky fyzického kanálu. Klíčové je, že parametry pro každou funkci – jako jsou kódová rychlost, hloubka prokládání a počet bitů na rádiový blok – lze dynamicky vybírat a signalizovat prostřednictvím zpráv vrstvy 3. Vytváří tak „sadu nástrojů“, ze které si síť může vybrat optimální kombinaci zpracování podle požadavků na kvalitu služby a přenosovou rychlost. Pro EDGE je tato flexibilita zásadní, protože umožňuje použití modulace vyššího řádu ([8-PSK](/mobilnisite/slovnik/8-psk/) vedle [GMSK](/mobilnisite/slovnik/gmsk/)) a různých kódových rychlostí k dosažení různých modulačních a kódových schémat ([MCS](/mobilnisite/slovnik/mcs/)), která definují přenosové rychlosti EDGE.

Architektura zahrnuje FLO zpracovací řetězec jak v mobilní stanici ([MS](/mobilnisite/slovnik/ms/)), tak v základnové stanici (BSS). Mezi klíčové komponenty patří kanálový kodér (podporující více vzorů punktování), prokládací jednotka (s přizpůsobitelnou velikostí bloku a hloubkou) a jednotka mapování fyzického kanálu. Řízení zajišťuje protokol Radio Resource (RR), který pomocí přiřazovacích zpráv konfiguruje fyzickou vrstvu MS konkrétními FLO parametry pro daný dočasný blokový tok (TBF) nebo kanál provozu. Role FLO spočívá v tom, že slouží jako přizpůsobitelný motor fyzické vrstvy pro vývoj GERAN. Umožňuje efektivní podporu smíšených typů provozu na stejné rádiové infrastruktuře, maximalizuje spektrální účinnost díky možnosti adaptace spoje a poskytuje základnu pro vysoké špičkové přenosové rychlosti (až několik set kbps) spojené s technologií EDGE.

## K čemu slouží

FLO bylo koncipováno za účelem překonání omezení původní fyzické vrstvy GSM, která byla navržena primárně pro hlas přepojovaný okruhy. Tento návrh používal pevnou, univerzální kanálovou strukturu, která byla pro datové služby neefektivní. Jak se GSM vyvíjelo k podpoře vyšších přenosových rychlostí s GPRS a později EDGE, potřeba přizpůsobitelnější fyzické vrstvy se stala kritickou. Stávající struktura nemohla snadno pojmout proměnné velikosti bloků, různé potřeby ochrany proti chybám a pokročilá modulační schémata vyžadovaná pro efektivní přenos paketových dat. FLO bylo řešením této nepružnosti.

Existuje proto, aby řešilo problém spektrální účinnosti a multiplexování služeb. Vytvořením flexibilní, parametrizované fyzické vrstvy umožňuje FLO síti přesně přizpůsobit rádiový přenos požadavkům přenášené zátěže. Pro hlasové volání může použít silné kanálové kódování a prokládání pro odolnost. Pro paketovou datovou relaci může zvolit slabší kódové schéma kombinované s 8-PSK modulací pro maximalizaci propustnosti při dobrých rádiových podmínkách. Tato dynamická adaptace spoje je klíčem k výkonu EDGE. Dále FLO umožňuje současnou podporu různorodých služeb na stejném nosiči, což operátorům umožňuje migrovat své sítě k nabídce jak hlasu, tak dat připomínajících broadband, aniž by potřebovali oddělenou fyzickou infrastrukturu.

Zavedené v kontextu standardizace EDGE v Rel-6 (ačkoli koncepty se objevily dříve), představovalo FLO zásadní filozofický posun pro GERAN. Řešilo základní omezení návrhu optimalizovaného pro hlas zavedením konfigurovatelné fyzické vrstvy, která bere v potaz data. Toto nejen odemklo vysoké přenosové rychlosti EDGE, ale také zajistilo budoucí použitelnost cesty GSM/EDGE tím, že poskytlo rámec, který by bylo možné v principu rozšířit o nové kódovací nebo modulační techniky, čímž zajistilo dlouhověkost rodiny technologií GSM tváří v tvář vyvíjejícím se požadavkům na datové služby.

## Klíčové vlastnosti

- Odděluje zpracování transportního kanálu od specifických hlasových kodeků
- Poskytuje konfigurovatelný zpracovací řetězec s parametrizovaným kanálovým kódováním, prokládáním a mapováním
- Podporuje více modulačních schémat (GMSK a 8-PSK) pro EDGE
- Umožňuje dynamickou adaptaci spoje prostřednictvím výběru modulačního a kódového schématu (MCS)
- Umožňuje efektivní multiplexování provozu přepojovaného okruhy a pakety
- Tvoří základ fyzické vrstvy pro vysokorychlostní paketová data EDGE (EGPRS)

## Související pojmy

- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [EGPRS – Enhanced GPRS](/mobilnisite/slovnik/egprs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TR 45.902** (Rel-19) — Flexible Layer One (FLO) for GERAN

---

📖 **Anglický originál a plná specifikace:** [FLO na 3GPP Explorer](https://3gpp-explorer.com/glossary/flo/)
