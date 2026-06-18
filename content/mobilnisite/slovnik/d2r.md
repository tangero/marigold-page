---
slug: "d2r"
url: "/mobilnisite/slovnik/d2r/"
type: "slovnik"
title: "D2R – Device to Reader"
date: 2026-01-01
abbr: "D2R"
fullName: "Device to Reader"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/d2r/"
summary: "D2R (Device to Reader) je komunikační režim zavedený ve 3GPP Release 19 pro IoT a senzorové sítě. Umožňuje zařízení (např. senzorové značce) přenášet data přímo na specializovaný čtecí uzel, čímž obch"
---

D2R je komunikační režim 3GPP pro IoT, ve kterém zařízení přenáší data přímo na specializovaný čtecí uzel, čímž obchází buněčné základnové stanice za účelem efektivního sběru dat s nízkou spotřebou a v lokalizované oblasti.

## Popis

Device to Reader (D2R) je nový komunikační paradigma standardizovaný ve 3GPP Release 19, primárně dokumentovaný napříč specifikacemi jako 33.369 (zabezpečení), 38.191/194/291/300/391 (aspekty NR) a 38.769/870 (vylepšení IoT). Definuje přímé propojení mezi IoT zařízením (často jednoduchým senzorem nebo značkou s omezenou baterií) a čtecím uzlem (Reader). Reader je specializovaná síťová entita, odlišná od konvenčního gNB, optimalizovaná pro agregaci dat od potenciálně masivního počtu blízkých zařízení. Architektonicky D2R funguje v rámci širších frameworků NR (New Radio) a RedCap (Reduced Capability), ale zavádí novou topologii point-to-multipoint, kde Reader funguje jako centralizovaný sběrač dat.

Propojení D2R je navrženo pro přenosy dat, které jsou uplink-centrické, sporadické a malého objemu. Zařízení (D2R Device) iniciuje komunikaci odesláním svých dat přímo na Reader pomocí definovaných fyzických kanálů a procedur. Reader, který má ve srovnání se standardním zařízením vylepšené přijímací schopnosti, spravuje přístup více zařízení, případně za použití přístupových schémat založených na konkurenci nebo bez udělení povolení (grant-free), aby minimalizoval signalizační režii a spotřebu energie zařízení. Mezi klíčové komponenty patří D2R Device (se zjednodušenou protokolovou zásobníkem), D2R Reader (s funkcí agregace a případně přenosu) a podpůrné síťové funkce pro autentizaci, zabezpečení a přeposílání dat definované ve specifikacích jádra sítě.

Z protokolové perspektivy D2R zahrnuje modifikace fyzické vrstvy NR (vlnové formy, referenční signály), vrstvy [MAC](/mobilnisite/slovnik/mac/) pro efektivní náhodný přístup a plánování a [RRC](/mobilnisite/slovnik/rrc/) pro omezenou konfiguraci. Bezpečnostní mechanismy jsou přizpůsobeny pro odlehčenou autentizaci zařízení a integritu dat mezi zařízením a Readrem. Reader typicky má připojení k přenosové síti (např. k 5GC) pro přeposlání sebraných dat. Úlohou D2R je umožnit ultra-efektivní, škálovatelný a lokalizovaný sběr dat pro aplikace jako průmyslové senzorové sítě, chytré zemědělství a monitorování životního prostředí, kde jsou zařízení jednoduchá a cílem dat jsou jasně definovaní sběrače spíše než libovolné koncové body.

## K čemu slouží

D2R byl vytvořen, aby řešil specifické výzvy masivních nasazení IoT s nízkou složitostí, které nebyly optimálně obsluhovány existujícími buněčnými paradigmaty 3GPP jako LTE-M nebo NB-IoT. Zatímco tyto technologie vynikají v poskytování širokoplošného pokrytí, stále vyžadují, aby zařízení navazovala plná buněčná spojení se základnovými stanicemi, což zahrnuje významnou řídicí signalizaci a složitost zařízení pro scénáře, kde data potřebují dosáhnout pouze blízkého agregačního bodu. Omezení předchozích přístupů zahrnovala zbytečnou spotřebu energie pro vyhledávání buněk, synchronizaci a správu mobility v statických senzorových polích a zahlcení sítě z mnoha zařízení připojujících se k makro buňkám.

Historický kontext je rostoucí potřeba komunikace 'senzor-to-cloud' nebo 'thing-to-gateway' v aplikacích Průmysl 4.0 a chytrých měst. D2R je motivován snahou vytvořit efektivní alternativu standardizovanou 3GPP k proprietárním krátkodosahovým technologiím (jako [RFID](/mobilnisite/slovnik/rfid/) čtečky), která nabízí lepší integraci se sítěmi 5G core, vylepšené zabezpečení a garantovanou QoS. Řeší problém připojení miliard ultra-jednoduchých zařízení s omezenými náklady a energií minimalizací protokolové složitosti a umožněním velmi lokalizované komunikace s vysokou hustotou, spravované Readery, čímž odlehčuje provoz od makro RAN a jádra sítě.

## Klíčové vlastnosti

- Přímá komunikace od IoT zařízení ke specializovanému čtecímu uzlu (Reader)
- Uplink-centrický, sporadický přenos dat optimalizovaný pro malé pakety
- Podpora odlehčeného přístupu založeného na konkurenci nebo bez udělení povolení (grant-free) ke snížení signalizace
- Vylepšený přijímač Readeru pro spolehlivý příjem od mnoha nízkopříkonových zařízení
- Integrace se sítí 5G core pro autentizaci, zabezpečení (33.369) a přenos dat
- Funguje v rámci frameworků NR a RedCap s přizpůsobenými fyzickými a protokolovými vrstvami

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 33.369** (Rel-19) — Security for AIoT in Isolated Private 5G Networks
- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.194** (Rel-19) — Ambient IoT Base Station RF Spec
- **TS 38.291** (Rel-19) — Ambient IoT Physical Layer Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.391** (Rel-19) — NR; Ambient IoT MAC Protocol Spec
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR
- **TS 38.870** (Rel-19) — Enhanced OTA Test Methods for NR FR1 TRP/TRS

---

📖 **Anglický originál a plná specifikace:** [D2R na 3GPP Explorer](https://3gpp-explorer.com/glossary/d2r/)
