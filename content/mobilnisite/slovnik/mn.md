---
slug: "mn"
url: "/mobilnisite/slovnik/mn/"
type: "slovnik"
title: "MN – Mobile Network"
date: 2026-01-01
abbr: "MN"
fullName: "Mobile Network"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mn/"
summary: "Kompletní infrastruktura provozovaná operátorem mobilní sítě pro poskytování bezdrátových komunikačních služeb. Zahrnuje všechny síťové prvky od rádiového přístupu po páteřní síť a podporuje hlasové,"
---

MN (mobilní síť) je kompletní infrastruktura provozovaná operátorem mobilní sítě pro poskytování bezdrátových hlasových, datových a multimediálních služeb, zahrnující všechny prvky od rádiového přístupu po páteřní síť.

## Popis

Mobilní síť (MN) je komplexní, koncový systém, který umožňuje bezdrátové telekomunikační služby pro uživatelská zařízení (UE), jako jsou chytré telefony a zařízení IoT. Z architektonického hlediska se dělí na dvě hlavní domény: rádiovou přístupovou síť (RAN) a páteřní síť (CN). RAN zahrnuje základnové stanice (např. gNB v 5G, [eNB](/mobilnisite/slovnik/enb/) v 4G, NodeB v 3G) a jejich řadiče, které spravují rádiové rozhraní včetně správy rádiových prostředků, předávání hovorů a počátečního zpracování uživatelských dat. Páteřní síť je centrálním mozkem, který zajišťuje připojení k externím sítím, jako je internet, a umožňuje správu účastníků, autentizaci, správu relací, správu mobility a vynucování pravidel. V 5G se jedná o 5G Core (5GC) s klíčovými funkcemi jako [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/) a [UPF](/mobilnisite/slovnik/upf/).

Síť funguje tak, že mezi UE a páteří sítě naváže zabezpečené, autentizované spojení. Když se zařízení zapne, připojí se k síti prostřednictvím procedur řízených funkcemi RAN a páteřní sítě. Páteřní síť autentizuje účastníka pomocí přihlašovacích údajů uložených v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)). Po autentizaci je navázána datová relace (Packet Data Unit session v 5G, [PDN](/mobilnisite/slovnik/pdn/) connection v 4G), která vytvoří tunel pro uživatelský provoz mezi UE a bránou připojenou k externí datové síti. Síť průběžně spravuje mobilitu UE, plynule přenáší jeho spojení mezi buňkami při pohybu a uplatňuje pravidla pro zajištění kvality služeb (QoS) a účtování.

Mezi klíčové komponenty patří uživatelské zařízení, uzly RAN, funkce řídicí roviny páteřní sítě (pro signalizaci), funkce uživatelské roviny (pro přeposílání dat) a systémy správy sítě ([OSS](/mobilnisite/slovnik/oss/)/BSS). Jejím úkolem je poskytovat všudypřítomné, spolehlivé a bezpečné připojení. Mobilní síť není statická; vyvíjí se prostřednictvím generací (3G, 4G, 5G), přičemž každá generace zavádí nové architektonické paradigmy, jako je přechod na plně IP páteř v 4G a architektura založená na službách s dělením sítě v 5G. Je to základní platforma, na které jsou poskytovány všechny mobilní služby – od hlasových hovorů po masivní IoT a ultra-spolehlivou komunikaci s nízkou latencí.

## K čemu slouží

Mobilní síť existuje za účelem poskytování bezdrátových komunikačních služeb v široké oblasti a řeší základní problém zajištění hlasového a datového připojení pro lidi a zařízení v pohybu. Historicky nahradila pevnou linkovou telefonii pro osobní komunikaci a nabídla nebývalou svobodu a dostupnost. Každá generace mobilní sítě byla motivována potřebou překonat omezení své předchůdkyně: 1G nabízela analogový hlas, ale byla nezabezpečená a neefektivní; 2G zavedla digitální hlas a SMS; 3G si kladla za cíl mobilní internet, ale s omezenou rychlostí; 4G LTE byla vytvořena speciálně pro poskytování vysokorychlostního, plně IP širokopásmového zážitku srovnatelného s pevnými linkami.

Vývoj směrem k 5G a dále řeší nové soubory problémů, které 4G sítě nebyly navrženy efektivně zvládat. Patří mezi ně masivní rozsah nasazení IoT, který vyžaduje podporu milionů zařízení s nízkým výkonem a nízkou datovou rychlostí; aplikace vyžadující ultra-spolehlivou komunikaci s nízkou latencí (URLLC), jako je průmyslová automatizace a vzdálená chirurgie; a potřeba vylepšeného mobilního širokopásmového připojení (eMBB) s vícegigabitovými rychlostmi pro AR/VR a video 4K/8K. Mobilní síť také řeší kritické obchodní problémy operátorů tím, že poskytuje spravovanou, účtovatelnou a bezpečnou platformu pro poskytování služeb, na rozdíl od neregulovaného spektra nebo služeb Wi-Fi typu best-effort. Její kontinuální vývoj je poháněn společenskými a ekonomickými požadavky na všudypřítomné digitální připojení jako na veřejnou službu.

## Klíčové vlastnosti

- Koncová architektura zahrnující rádiovou přístupovou síť (RAN) a páteřní síť (CN)
- Podpora plynulé mobility a předávání hovorů mezi buňkami a oblastmi sledování
- Správa účastníků včetně autentizace, autorizace a účtování (AAA)
- Zabezpečené tunelování a šifrování pro provoz uživatelské a řídicí roviny
- Řízení pravidel a účtování pro umožnění diferencovaných služeb a obchodních modelů
- Propojení s dalšími sítěmi (např. PSTN, internet, jiné mobilní sítě)

## Související pojmy

- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.327** (Rel-13) — 3GPP-WLAN Mobility Stage 2 Description
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 32.422** (Rel-20) — Telecom Management: Trace Control & Configuration
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 32.856** (Rel-15) — Energy Efficiency Assessment for RAN OAM
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.822** (Rel-8) — Security Architecture for Inter-Access Mobility
- **TS 33.825** (Rel-16) — Security for 5G URLLC Services
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [MN na 3GPP Explorer](https://3gpp-explorer.com/glossary/mn/)
