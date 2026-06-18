---
slug: "alcap"
url: "/mobilnisite/slovnik/alcap/"
type: "slovnik"
title: "ALCAP – Access Link Control Application Protocol"
date: 2025-01-01
abbr: "ALCAP"
fullName: "Access Link Control Application Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/alcap/"
summary: "ALCAP je signalizační protokol transportní sítě používaný v sítích 3GPP UMTS pro dynamické zřizování, správu a uvolňování transportních přenosových kanálů pro uživatelskou rovinu. Funguje mezi síťovým"
---

ALCAP je signalizační protokol transportní vrstvy používaný v sítích 3GPP UMTS pro dynamické zřizování, správu a uvolňování transportních přenosových kanálů (bearerů) pro uživatelskou rovinu mezi prvky, jako je RNC a Node B.

## Popis

Access Link Control Application Protocol (ALCAP) je klíčový signalizační protokol v architektuře 3GPP UMTS, konkrétně navržený pro řídicí rovinu transportní síťové vrstvy. Funguje přes rozhraní Iub mezi Radiový síťový řadič ([RNC](/mobilnisite/slovnik/rnc/)) a Node B (základnová stanice) a přes rozhraní Iur mezi dvěma RNC. Primární funkcí ALCAP je dynamicky zřizovat, spravovat, upravovat a uvolňovat transportní přenosové kanály pro data uživatelské roviny. Tyto kanály jsou typicky [AAL2](/mobilnisite/slovnik/aal2/) ([ATM](/mobilnisite/slovnik/atm/) Adaptation Layer 2) spojení, která jsou vhodná pro přenos citlivého na zpoždění a proměnlivého toku dat, jako je hlas a interaktivní video. ALCAP sám nenese uživatelská data; místo toho pracuje ve spojení s řídicími protokoly vyšší vrstvy, jako je [NBAP](/mobilnisite/slovnik/nbap/) (Node B Application Part) a [RNSAP](/mobilnisite/slovnik/rnsap/) (Radio Network Subsystem Application Part). Když RNC určí potřebu nového radiového přístupového kanálu ([RAB](/mobilnisite/slovnik/rab/)), použije NBAP/RNSAP k nastavení radiových zdrojů a poté aktivuje ALCAP k zřízení odpovídajícího AAL2 transportního spojení mezi zúčastněnými síťovými uzly.

Architektonicky je ALCAP součástí Řídicí roviny transportní sítě (TNCP), která je oddělena od Řídicí roviny radiové sítě (RNCP). Toto oddělení řídicích rovin je klíčovým konstrukčním principem v UMTS. RNCP (pomocí NBAP, RNSAP) zpracovává signalizaci specifickou pro rádiové rozhraní, zatímco TNCP (pomocí ALCAP) zpracovává signalizaci potřebnou ke správě zdrojů podkladové transportní sítě. Zprávy ALCAP jsou přenášeny přes specifická ATM virtuální kanálová spojení ([VCC](/mobilnisite/slovnik/vcc/)) určená pro signalizaci. Protokol definuje procedury pro zřizování spojení (pomocí zpráv ERQ - Establish Request a [ECF](/mobilnisite/slovnik/ecf/) - Establish Confirm), uvolnění (pomocí REL - Release a RLC - Release Complete) a údržbu. Zahrnuje mechanismy pro zpracování chyb, identifikaci přenosových kanálů a vyjednávání parametrů kvality služby souvisejících s AAL2 spojením, jako je špičková rychlost buněk a udržitelná rychlost buněk.

Při provozu poskytuje ALCAP spolehlivou službu doručování svých signalizačních zpráv ve správném pořadí. Jde o protokol typu peer-to-peer, což znamená, že RNC a Node B (nebo dva RNC) komunikují přímo. Klíčovou součástí je entita protokolu ALCAP, která sídlí jak v řídicím uzlu (např. RNC), tak v řízeném uzlu (např. Node B). Tato entita spravuje lokální zdroje AAL2 přepínání a provádí signalizační procedury. Protokol používá jedinečný Binding ID k asociaci transportního kanálu zřízeného ALCAP s konkrétním radiovým spojením nebo radiovým přístupovým kanálem, který byl nastaven procedurami vyšší vrstvy NBAP nebo RNSAP. Toto propojení je klíčové pro zajištění, že data uživatelské roviny z konkrétního hovoru jsou směrována přes správnou transportní cestu. Dynamická povaha ALCAP umožňuje efektivní statistické multiplexování více uživatelských spojení přes sdílené ATM zdroje, což je významné zlepšení oproti statickým, předem zřízeným TDM linkám používaným v dřívějších rozhraních GSM Abis.

## K čemu slouží

ALCAP byl vytvořen, aby řešil zásadní posun v požadavcích na transportní síť, který přineslo rozhraní WCDMA UMTS a jeho podpora různorodých služeb s přenosovou kapacitou na vyžádání. V legacy sítích GSM používalo rozhraní Abis mezi BTS a BSC typicky statické, okruhově přepínané TDM (E1/T1) linky. Každý časový slot byl trvale alokován, což vedlo k neefektivnímu využití zdrojů, zejména pro přerušovaný datový provoz. UMTS, navržené od počátku pro podporu multimediálních služeb (hlas, video, paketová data) s proměnlivou a garantovanou přenosovou rychlostí, vyžadovalo flexibilnější a efektivnější transportní mechanismus. Primárním účelem ALCAP je umožnit dynamické, na požádání zřizování a rušení transportních spojení, která odpovídají okamžitým potřebám uživatelských relací, a tím optimalizovat využití nákladných zdrojů přenosové sítě (backhaul).

Protokol řeší problém propojení správy radiových zdrojů se správou transportních zdrojů. Před ALCAP byly tyto funkce často propleteny nebo vyžadovaly manuální konfiguraci. ALCAP zavádí jasné oddělení mezi Řídicí rovinou radiové sítě (spravující radiová spojení) a Řídicí rovinou transportní sítě (spravující AAL2 spojení). Toto oddělení umožňuje nezávislý vývoj a škálování radiových a transportních sítí. Také umožňuje pokročilé funkce, jako je měkký handover, kdy je jediný datový proud uživatele rozdělen mezi více Node B; ALCAP může efektivně zřídit více potřebných AAL2 spojení pro různé větve handoveru. Motivací pro použití AAL2 jako technologie přenosových kanálů byla jeho efektivita pro provoz s nízkou přenosovou rychlostí a citlivý na zpoždění, což umožňuje multiplexovat více komprimovaných hlasových hovorů do jedné ATM buňky, čímž se snižuje zpoždění balení a režie ve srovnání s IP v té době.

Historicky byl vývoj ALCAP ve verzi Release 99 základním kamenem architektury pozemní radiové přístupové sítě UMTS (UTRAN). Řešil omezení statického GSM Abis tím, že poskytoval dynamickou transportní vrstvu s podporou QoS, která dokázala držet krok s rychlým zřizováním a rušením radiových kanálů vyžadovaných pro paketově přepínané služby a pokročilé mobilní scénáře. I když jeho relevance poklesla s migrací na čistě IP transport (GTP-U přes IP) v LTE a 5G, ALCAP představoval kritický evoluční krok k tomu, aby se transport mobilních sítí stal agilním a službově orientovaným.

## Klíčové vlastnosti

- Dynamické zřizování a uvolňování AAL2 transportních kanálů
- Oddělení Řídicí roviny transportní sítě od Řídicí roviny radiové sítě
- Podpora vyjednávání parametrů QoS pro AAL2 spojení
- Mechanismus propojení (binding) k asociaci transportních kanálů s radiovými přístupovými kanály
- Fungování přes rozhraní Iub a Iur v UTRAN
- Spolehlivé doručování signalizačních zpráv ve správném pořadí

## Související pojmy

- [NBAP – Node B Application Protocol](/mobilnisite/slovnik/nbap/)
- [RNSAP – Radio Network Subsystem Application Part](/mobilnisite/slovnik/rnsap/)
- [AAL2 – ATM Adaptation Layer type 2](/mobilnisite/slovnik/aal2/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [ALCAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/alcap/)
